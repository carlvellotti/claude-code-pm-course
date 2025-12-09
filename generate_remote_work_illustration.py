#!/usr/bin/env python3
"""Generate remote work illustration using image_gen module"""

import sys
import os

# Add current directory to path to import image_gen
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_gen import generate

# The detailed prompt
prompt = """**Task:** Create a flat illustration of a person working remotely.

**Style:**
- Playful geometric illustration with bold shapes
- Bright, saturated colors: yellow, pink, electric blue, black
- Chunky proportions, slightly exaggerated features
- Memphis design influence with floating shapes

**Output:**
- Single 1:1 square illustration, white background
- Bold, eye-catching, modern

**Content:**
- Scene: Person working from home at desk
- Elements:
  - Person: Seated at desk with headphones, waving at screen
  - Desk: Monitor showing video call grid, keyboard, plant
  - Chair: Modern ergonomic style
  - Background: Floating geometric shapes (circles, triangles, squiggles)
  - Cat sleeping on nearby surface

**Layout:**
- Person centered, desk slightly angled
- Floating shapes scattered around edges
- Dynamic, energetic composition

**Constraints:**
- Stylized but recognizable figures (simple faces okay)
- Bold color blocks, no gradients
- No realistic textures
- No text"""

# Generate the image
print("Generating remote work illustration...")
output_path = generate(prompt)

if output_path:
    # Get absolute path
    abs_path = os.path.abspath(output_path)
    print(f"\n✓ Image generated successfully!")
    print(f"Full path: {abs_path}")
else:
    print("\n✗ Failed to generate image")
    sys.exit(1)
