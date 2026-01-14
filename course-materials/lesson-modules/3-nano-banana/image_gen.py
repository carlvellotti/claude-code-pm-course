"""
Gemini 图像生成模块
预构建的模块，供 Claude Code 调用 - 处理会话管理、
多轮对话和输出保存。
"""
import os
import json
import base64
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from google import genai
from google.genai import types

# 配置
SESSION_FILE = ".image_session.json"
OUTPUT_DIR = "outputs"
DEFAULT_MODEL = "gemini-3-pro-image-preview"
DEFAULT_ASPECT_RATIO = "1:1"
DEFAULT_RESOLUTION = "1K"


def _get_client():
    """初始化 Gemini 客户端"""
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("在环境中未找到 GEMINI_API_KEY。请检查您的 .env 文件。")
    return genai.Client(api_key=api_key)


def _ensure_output_dir():
    """如果输出目录不存在则创建"""
    Path(OUTPUT_DIR).mkdir(exist_ok=True)


def _load_session():
    """加载现有会话或返回空会话"""
    if os.path.exists(SESSION_FILE):
        try:
            with open(SESSION_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {"history": [], "outputs": [], "turn": 0}
    return {"history": [], "outputs": [], "turn": 0}


def _reconstruct_history(raw_history):
    """
    将原始历史字典转换回 types.Content 对象。
    这是保留多轮对话中的思维签名 (thought signatures) 所必需的。
    """
    reconstructed = []
    for item in raw_history:
        parts = []
        for part_data in item.get("parts", []):
            if "text" in part_data:
                # 文本部分
                part_kwargs = {"text": part_data["text"]}
                if "thought_signature" in part_data:
                    part_kwargs["thought_signature"] = base64.b64decode(part_data["thought_signature"])
                parts.append(types.Part(**part_kwargs))
            elif "inline_data" in part_data:
                # 图像部分
                blob = types.Blob(
                    mime_type=part_data["inline_data"]["mime_type"],
                    data=base64.b64decode(part_data["inline_data"]["data"])
                )
                part_kwargs = {"inline_data": blob}
                if "thought_signature" in part_data:
                    part_kwargs["thought_signature"] = base64.b64decode(part_data["thought_signature"])
                parts.append(types.Part(**part_kwargs))

        reconstructed.append(types.Content(
            role=item.get("role"),
            parts=parts
        ))
    return reconstructed


def _save_session(session):
    """将会话保存到文件"""
    with open(SESSION_FILE, 'w') as f:
        json.dump(session, f)


def _get_next_output_path(session):
    """生成下一个输出文件名"""
    _ensure_output_dir()
    turn = session.get("turn", 0) + 1
    timestamp = datetime.now().strftime("%H%M%S")
    return f"{OUTPUT_DIR}/output_{turn:03d}_{timestamp}.png"


def new_session():
    """清除当前会话并重新开始"""
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
    print("会话已清除。准备生成新图像。")
    return {"history": [], "outputs": [], "turn": 0}


def session_info():
    """显示当前会话状态"""
    session = _load_session()
    turn_count = session.get("turn", 0)
    outputs = session.get("outputs", [])

    if turn_count == 0:
        print("无活动会话。开始生成以创建会话。")
        return None

    print(f"当前会话: {turn_count} 轮")
    print(f"生成的输出:")
    for i, output in enumerate(outputs, 1):
        print(f"  {i}. {output}")

    return session


def revert(turns: int = 1):
    """
    撤销当前会话的最后 N 轮。

    Args:
        turns: 要撤销的轮数（默认为 1）

    Returns:
        更新后的会话，如果没有可撤销的内容则返回 None
    """
    session = _load_session()
    turn_count = session.get("turn", 0)

    if turn_count == 0:
        print("无活动会话可撤销。")
        return None

    if turns > turn_count:
        print(f"只能撤销 {turn_count} 轮。正在撤销所有。")
        turns = turn_count

    # 每一轮 = 2 个历史项（用户消息 + 模型响应）
    items_to_remove = turns * 2
    session["history"] = session["history"][:-items_to_remove]

    # 移除输出
    session["outputs"] = session["outputs"][:-turns]

    # 更新轮数
    session["turn"] = turn_count - turns

    _save_session(session)

    if session["turn"] == 0:
        print(f"已撤销 {turns} 轮。会话现在为空。")
    else:
        print(f"已撤销 {turns} 轮。现在处于第 {session['turn']} 轮。")
        print(f"最后的输出: {session['outputs'][-1] if session['outputs'] else '无'}")

    return session


def generate(
    prompt: str,
    reference_images: list = None,
    aspect_ratio: str = DEFAULT_ASPECT_RATIO,
    resolution: str = DEFAULT_RESOLUTION,
    model: str = DEFAULT_MODEL
) -> str:
    """
    生成或优化图像。自动继续现有会话。

    Args:
        prompt: 要生成/更改内容的文本描述
        reference_images: 可选的参考图像路径列表
        aspect_ratio: "1:1", "3:4", "16:9" 等
        resolution: "1K", "2K", 或 "4K"
        model: "gemini-2.5-flash-image" 或 "gemini-3-pro-image-preview"

    Returns:
        生成的图像路径
    """
    client = _get_client()
    session = _load_session()

    # 构建此轮的内容
    content_parts = [prompt]

    # 如果提供了参考图像则添加
    if reference_images:
        from PIL import Image
        for img_path in reference_images:
            if os.path.exists(img_path):
                content_parts.append(Image.open(img_path))
            else:
                print(f"警告: 未找到参考图像: {img_path}")

    # 构建配置
    config = types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        image_config=types.ImageConfig(
            aspectRatio=aspect_ratio
        )
    )

    # 检查是否继续现有会话
    if session["history"]:
        # 继续多轮对话：使用聊天模式
        print(f"继续会话 (第 {session['turn'] + 1} 轮)...")

        # 使用正确的类型重建历史记录（包括思维签名）
        reconstructed_history = _reconstruct_history(session["history"])

        # 从历史记录重建聊天
        chat = client.chats.create(
            model=model,
            config=config,
            history=reconstructed_history
        )

        response = chat.send_message(content_parts)

        # 用新的交换更新历史记录
        session["history"].append({"role": "user", "parts": [{"text": prompt}]})

    else:
        # 新会话：创建新的聊天
        print("开始新会话...")

        chat = client.chats.create(
            model=model,
            config=config
        )

        response = chat.send_message(content_parts)

        # 开始历史记录
        session["history"].append({"role": "user", "parts": [{"text": prompt}]})

    # 处理响应
    output_path = None
    response_parts = []

    for part in response.parts:
        if part.text is not None:
            print(f"模型: {part.text}")
            part_data = {"text": part.text}
            # 如果存在则保留思维签名
            if hasattr(part, 'thought_signature') and part.thought_signature:
                part_data["thought_signature"] = base64.b64encode(part.thought_signature).decode('utf-8')
            response_parts.append(part_data)
        elif part.inline_data is not None:
            # 保存图像
            output_path = _get_next_output_path(session)
            image = part.as_image()
            image.save(output_path)
            print(f"已保存: {output_path}")

            # 将图像数据存储在历史记录中以便继续
            # 注意：这会使会话文件变大，但能保留完整的上下文
            part_data = {
                "inline_data": {
                    "mime_type": part.inline_data.mime_type,
                    "data": base64.b64encode(part.inline_data.data).decode('utf-8')
                }
            }
            # 如果存在则保留思维签名（对于 Gemini 3 Pro 的多轮对话至关重要）
            if hasattr(part, 'thought_signature') and part.thought_signature:
                part_data["thought_signature"] = base64.b64encode(part.thought_signature).decode('utf-8')
            response_parts.append(part_data)

    # 更新会话
    session["history"].append({"role": "model", "parts": response_parts})
    session["turn"] = session.get("turn", 0) + 1
    if output_path:
        session["outputs"].append(output_path)

    _save_session(session)

    return output_path


# 便捷别名
def gen(prompt, **kwargs):
    """generate() 的简写"""
    return generate(prompt, **kwargs)


if __name__ == "__main__":
    # 快速测试
    print("图像生成模块已加载。")
    print("用法: generate(prompt), new_session(), session_info(), revert()")
    print("")
    print("函数:")
    print("  generate(prompt)     - 生成/优化图像")
    print("  new_session()        - 清除会话，重新开始")
    print("  session_info()       - 显示当前会话状态")
    print("  revert(turns=1)      - 撤销最后 N 轮")
