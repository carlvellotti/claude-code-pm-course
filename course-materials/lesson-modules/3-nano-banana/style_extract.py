"""
Style Extraction Module
Uses Gemini 3 Pro's vision capabilities to analyze and extract
detailed style information from images.
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

from google import genai
from google.genai import types

# Gemini 2.5 Pro for vision/understanding (excellent at image analysis)
VISION_MODEL = "gemini-2.5-pro"

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
    """Initialize Gemini client"""
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment. Check your .env file.")
    return genai.Client(api_key=api_key)


def extract_style(image_path: str, custom_prompt: str = None) -> str:
    """
    Extract detailed style information from an image.

    Args:
        image_path: Path to the image to analyze
        custom_prompt: Optional custom extraction prompt (uses default if not provided)

    Returns:
        Detailed style description as text
    """
    client = _get_client()

    # Load image
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = Image.open(image_path)

    prompt = custom_prompt or STYLE_EXTRACTION_PROMPT

    print(f"Analyzing style of: {image_path}")
    print("This may take a moment...")

    # Use Gemini's vision capability
    response = client.models.generate_content(
        model=VISION_MODEL,
        contents=[prompt, image]
    )

    style_description = response.text

    print("\n" + "="*60)
    print("STYLE EXTRACTION COMPLETE")
    print("="*60 + "\n")
    print(style_description)

    return style_description


def extract_and_save(image_path: str, output_path: str = None) -> str:
    """
    Extract style and save to a markdown file.

    Args:
        image_path: Path to the image to analyze
        output_path: Where to save the style guide (auto-generated if not provided)

    Returns:
        Path to the saved style guide
    """
    style_description = extract_style(image_path)

    # Generate output path if not provided
    if not output_path:
        image_name = Path(image_path).stem
        output_path = f"styles/{image_name}_style.md"

    # Ensure directory exists
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    # Write the style guide
    with open(output_path, 'w') as f:
        f.write(f"# Style Guide: {Path(image_path).name}\n\n")
        f.write(f"*Extracted from: `{image_path}`*\n\n")
        f.write("---\n\n")
        f.write(style_description)

    print(f"\nStyle guide saved to: {output_path}")

    return output_path


if __name__ == "__main__":
    print("Style Extraction Module loaded.")
    print("")
    print("Functions:")
    print("  extract_style(image_path)           - Analyze image and return style description")
    print("  extract_and_save(image_path)        - Extract and save to styles/ folder")
