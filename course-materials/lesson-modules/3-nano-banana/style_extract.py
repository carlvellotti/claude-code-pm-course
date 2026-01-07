"""
风格提取模块
使用 Gemini 3 Pro 的视觉能力来分析并提取
从图像中提取详细的风格信息。
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

from google import genai
from google.genai import types

# Gemini 2.5 Pro 用于视觉/理解（擅长图像分析）
VISION_MODEL = "gemini-2.5-pro"

# 风格提取提示词 (STYLE_EXTRACTION_PROMPT)
# 注意：此提示词故意保留为英文，以确保 Gemini 模型的最佳性能。
STYLE_EXTRACTION_PROMPT = """Analyze this image and deconstruct its complete visual style. I want to be able to recreate this exact aesthetic for completely different subjects.

Describe in detail:

**Color Palette:** What are the dominant colors? Secondary colors? Describe the color temperature (warm, cool, neutral), saturation levels, and any notable color relationships or contrasts. Are there specific hex codes or color names that define this look?

**Lighting:** What type of lighting is used? Describe the direction, quality (soft, hard, diffused), color temperature of the light, shadows, highlights, and any atmospheric lighting effects like rim light, backlighting, or volumetric rays.

**Composition & Framing:** How is the image composed? Describe the perspective, camera angle, focal length feel (wide, telephoto, macro), depth of field, rule of thirds usage, leading lines, symmetry, or any other compositional techniques.

**Textures & Materials:** What surface qualities are present? Describe any grain, noise, smoothness, glossiness, or material properties that define the look.

**Mood & Atmosphere:** What emotional tone does this convey? Describe the overall vibe, energy level, and feeling the viewer gets.

**Artistic Style:** Is this photorealistic, illustrated, painterly, graphic, retro, futuristic, minimal, maximalist? What art movement or design era does it reference, if any?

**Typography & Graphics:** If text or graphic elements are present, describe the font style, weight, treatment, and how it integrates with the image.

**Special Effects:** Any glows, blurs, distortions, overlays, duotone treatments, or post-processing effects?

Write this as a cohesive style guide I can reference when generating new images. Be specific enough that someone could recreate this aesthetic without seeing the original."""


def _get_client():
    """初始化 Gemini 客户端"""
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("在环境中未找到 GEMINI_API_KEY。请检查您的 .env 文件。")
    return genai.Client(api_key=api_key)


def extract_style(image_path: str, custom_prompt: str = None) -> str:
    """
    从图像中提取详细的风格信息。

    Args:
        image_path: 要分析的图像路径
        custom_prompt: 可选的自定义提取提示词（如果未提供则使用默认值）

    Returns:
        作为文本的详细风格描述
    """
    client = _get_client()

    # 加载图像
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"未找到图像: {image_path}")

    image = Image.open(image_path)

    prompt = custom_prompt or STYLE_EXTRACTION_PROMPT

    print(f"正在分析风格: {image_path}")
    print("这可能需要一点时间...")

    # 使用 Gemini 的视觉能力
    response = client.models.generate_content(
        model=VISION_MODEL,
        contents=[prompt, image]
    )

    style_description = response.text

    print("\n" + "="*60)
    print("风格提取完成")
    print("="*60 + "\n")
    print(style_description)

    return style_description


def extract_and_save(image_path: str, output_path: str = None) -> str:
    """
    提取风格并保存到 markdown 文件。

    Args:
        image_path: 要分析的图像路径
        output_path: 风格指南的保存位置（如果未提供则自动生成）

    Returns:
        保存的风格指南路径
    """
    style_description = extract_style(image_path)

    # 如果未提供输出路径则生成
    if not output_path:
        image_name = Path(image_path).stem
        output_path = f"styles/{image_name}_style.md"

    # 确保目录存在
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    # 写入风格指南
    with open(output_path, 'w') as f:
        f.write(f"# 风格指南: {Path(image_path).name}\n\n")
        f.write(f"*提取自: `{image_path}`*\n\n")
        f.write("---\n\n")
        f.write(style_description)

    print(f"\n风格指南已保存至: {output_path}")

    return output_path


if __name__ == "__main__":
    print("风格提取模块已加载。")
    print("")
    print("函数:")
    print("  extract_style(image_path)           - 分析图像并返回风格描述")
    print("  extract_and_save(image_path)        - 提取并保存到 styles/ 文件夹")
