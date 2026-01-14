"""
风格库助手
通过 ID 从 style-library.html 提取风格提示词。
"""
import re
import json
import sys
from pathlib import Path


def get_style(style_id: int) -> dict:
    """
    从风格库中通过 ID 获取风格。

    Args:
        style_id: 要检索的风格编号

    Returns:
        包含风格信息（id, name, prompt, category 等）的字典
    """
    # 在此脚本的同一目录中查找 style-library.html
    script_dir = Path(__file__).parent
    html_path = script_dir / "style-library.html"

    if not html_path.exists():
        raise FileNotFoundError(f"未在 {html_path} 找到 style-library.html")

    # 读取 HTML 文件
    content = html_path.read_text()

    # 从 JavaScript 提取 styles 数组
    # 查找: const styles = [...];
    match = re.search(r'const styles = \[(.*?)\];', content, re.DOTALL)
    if not match:
        raise ValueError("无法在 style-library.html 中找到 styles 数组")

    array_content = match.group(1)

    # 解析每个 style 对象
    # 通过 '},{' 分割以获取单个对象
    style_pattern = re.compile(r'\{[^{}]*\}', re.DOTALL)
    style_matches = style_pattern.findall(array_content)

    for style_str in style_matches:
        # 提取 id
        id_match = re.search(r'id:\s*(\d+)', style_str)
        if id_match and int(id_match.group(1)) == style_id:
            # 找到我们的风格 - 提取所有字段
            style = {"id": style_id}

            # 提取 name
            name_match = re.search(r'name:\s*"([^"]*)"', style_str)
            if name_match:
                style["name"] = name_match.group(1)

            # 提取 category
            cat_match = re.search(r'category:\s*"([^"]*)"', style_str)
            if cat_match:
                style["category"] = cat_match.group(1)

            # 提取 prompt (处理多行和转义引号)
            prompt_match = re.search(r'prompt:\s*"((?:[^"\\]|\\.)*)"', style_str, re.DOTALL)
            if prompt_match:
                # 反转义 prompt
                prompt = prompt_match.group(1)
                prompt = prompt.replace('\\n', '\n').replace('\\"', '"')
                style["prompt"] = prompt

            # 提取 exampleUse
            use_match = re.search(r'exampleUse:\s*"([^"]*)"', style_str)
            if use_match:
                style["exampleUse"] = use_match.group(1)

            return style

    raise ValueError(f"在库中未找到风格 #{style_id}")


def list_styles() -> list:
    """列出所有可用风格及其 ID 和名称。"""
    script_dir = Path(__file__).parent
    html_path = script_dir / "style-library.html"

    content = html_path.read_text()

    # 查找所有 id 和 name 对
    styles = []
    pattern = re.compile(r'id:\s*(\d+),\s*name:\s*"([^"]*)"')
    for match in pattern.finditer(content):
        styles.append({"id": int(match.group(1)), "name": match.group(2)})

    return styles


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python get_style.py <style_id>")
        print("       python get_style.py --list")
        sys.exit(1)

    if sys.argv[1] == "--list":
        styles = list_styles()
        print(f"可用风格 (共 {len(styles)} 个):\n")
        for s in styles:
            print(f"  #{s['id']:2d}: {s['name']}")
    else:
        try:
            style_id = int(sys.argv[1])
            style = get_style(style_id)
            print(f"风格 #{style['id']}: {style['name']}")
            print(f"类别: {style.get('category', 'N/A')}")
            print(f"示例用途: {style.get('exampleUse', 'N/A')}")
            print(f"\n提示词:\n{style['prompt']}")
        except ValueError as e:
            print(f"错误: {e}")
            sys.exit(1)
