#!/usr/bin/env python3
"""Generate wireframe image using image_gen module"""

import sys
sys.path.insert(0, '/Users/carl/Documents/Coding projects/claude-code-pm-course')

from image_gen import generate

prompt = """Create a mobile app wireframe.

Style:
- Clean grayscale wireframe aesthetic
- Simple rectangles, lines, and placeholder shapes
- No color except shades of gray
- Annotations in blue for callouts

Output:
- Single mobile screen (9:19.5 aspect ratio), white background
- Low-fidelity, sketch-level detail

Content:
- Screen: "Home Dashboard"
- Elements:
  - Status bar at top (time, battery, signal placeholders)
  - Header: "Good morning, Sarah" with avatar circle
  - Search bar with magnifying glass icon
  - Section: "Recent Projects" with 3 horizontal card placeholders
  - Section: "Quick Actions" with 4 icon button placeholders
  - Bottom navigation: 4 tab icons (Home, Search, Add, Profile)

Layout:
- Standard mobile layout, elements stacked vertically
- Consistent padding and spacing
- Blue annotation arrows pointing to key elements with labels

Constraints:
- Grayscale only (no color in UI, blue for annotations only)
- Placeholder text like "Lorem ipsum" or "Project Title"
- No realistic images or icons, just shapes"""

# Generate with 9:16 aspect ratio (mobile/portrait)
output_path = generate(prompt, aspect_ratio="9:16")

if output_path:
    print(f"\n✓ Image generated successfully!")
    print(f"Full path: {output_path}")
else:
    print("✗ Failed to generate image")
    sys.exit(1)
