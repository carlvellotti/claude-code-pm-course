#!/usr/bin/env python3
"""
One-time script to generate portrait image
"""
import os
import shutil
from image_gen import generate

# The prompt
prompt = """**Task:** Create a professional persona portrait.

**Style:**
- Warm natural light aesthetic, golden hour feel
- Slightly shallow depth of field, soft bokeh background
- Authentic, candid energy rather than posed
- Warm color grade with lifted shadows

**Output:**
- Single 4:5 vertical portrait, blurred outdoor background
- Film-like quality with subtle grain

**Content:**
- Subject: Man, late 20s, startup founder
- Appearance: Short beard, wavy brown hair, friendly eyes
- Clothing: Heather gray crewneck sweater
- Expression: Genuine smile, relaxed, approachable

**Layout:**
- Head and shoulders with slight negative space above
- Subject slightly off-center (rule of thirds)
- Background suggests outdoor café or park, blurred

**Lighting:**
- Natural golden hour sunlight from side
- Soft shadows, warm highlights on face
- No harsh contrasts

**Constraints:**
- Photorealistic with subtle film emulation
- Feels authentic, not stock photo
- No text, logos, or distracting elements"""

# Generate with 4:5 aspect ratio for portrait
output_path = generate(prompt, aspect_ratio="4:5", resolution="2K")

if output_path:
    # Create a copy with the custom filename
    custom_path = output_path.replace(os.path.basename(output_path),
                                      f"portrait-natural-{os.path.basename(output_path)}")
    shutil.copy(output_path, custom_path)
    print(f"\n✓ Image generated successfully!")
    print(f"Original path: {os.path.abspath(output_path)}")
    print(f"Custom path: {os.path.abspath(custom_path)}")
else:
    print("Error: No image was generated")
