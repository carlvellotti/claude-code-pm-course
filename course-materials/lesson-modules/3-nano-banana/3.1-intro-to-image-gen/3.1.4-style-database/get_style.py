"""
Style Library Helper
Extracts style prompts from style-library.html by ID.
"""
import re
import json
import sys
from pathlib import Path


def get_style(style_id: int) -> dict:
    """
    Get a style by ID from the style library.

    Args:
        style_id: The style number to retrieve

    Returns:
        Dictionary with style info (id, name, prompt, category, etc.)
    """
    # Find the style-library.html in the same directory as this script
    script_dir = Path(__file__).parent
    html_path = script_dir / "style-library.html"

    if not html_path.exists():
        raise FileNotFoundError(f"style-library.html not found at {html_path}")

    # Read the HTML file
    content = html_path.read_text()

    # Extract the styles array from the JavaScript
    # Look for: const styles = [...];
    match = re.search(r'const styles = \[(.*?)\];', content, re.DOTALL)
    if not match:
        raise ValueError("Could not find styles array in style-library.html")

    array_content = match.group(1)

    # Parse each style object
    # Split by '},{' to get individual objects
    style_pattern = re.compile(r'\{[^{}]*\}', re.DOTALL)
    style_matches = style_pattern.findall(array_content)

    for style_str in style_matches:
        # Extract id
        id_match = re.search(r'id:\s*(\d+)', style_str)
        if id_match and int(id_match.group(1)) == style_id:
            # Found our style - extract all fields
            style = {"id": style_id}

            # Extract name
            name_match = re.search(r'name:\s*"([^"]*)"', style_str)
            if name_match:
                style["name"] = name_match.group(1)

            # Extract category
            cat_match = re.search(r'category:\s*"([^"]*)"', style_str)
            if cat_match:
                style["category"] = cat_match.group(1)

            # Extract prompt (handles multi-line and escaped quotes)
            prompt_match = re.search(r'prompt:\s*"((?:[^"\\]|\\.)*)"', style_str, re.DOTALL)
            if prompt_match:
                # Unescape the prompt
                prompt = prompt_match.group(1)
                prompt = prompt.replace('\\n', '\n').replace('\\"', '"')
                style["prompt"] = prompt

            # Extract exampleUse
            use_match = re.search(r'exampleUse:\s*"([^"]*)"', style_str)
            if use_match:
                style["exampleUse"] = use_match.group(1)

            return style

    raise ValueError(f"Style #{style_id} not found in library")


def list_styles() -> list:
    """List all available styles with their IDs and names."""
    script_dir = Path(__file__).parent
    html_path = script_dir / "style-library.html"

    content = html_path.read_text()

    # Find all id and name pairs
    styles = []
    pattern = re.compile(r'id:\s*(\d+),\s*name:\s*"([^"]*)"')
    for match in pattern.finditer(content):
        styles.append({"id": int(match.group(1)), "name": match.group(2)})

    return styles


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_style.py <style_id>")
        print("       python get_style.py --list")
        sys.exit(1)

    if sys.argv[1] == "--list":
        styles = list_styles()
        print(f"Available styles ({len(styles)} total):\n")
        for s in styles:
            print(f"  #{s['id']:2d}: {s['name']}")
    else:
        try:
            style_id = int(sys.argv[1])
            style = get_style(style_id)
            print(f"Style #{style['id']}: {style['name']}")
            print(f"Category: {style.get('category', 'N/A')}")
            print(f"Example use: {style.get('exampleUse', 'N/A')}")
            print(f"\nPrompt:\n{style['prompt']}")
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
