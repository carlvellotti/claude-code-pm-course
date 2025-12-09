#!/usr/bin/env python3
"""Generate UX journey map using image_gen module"""

from image_gen import generate

prompt = """**Task:** Create a UX user journey map.

**Style:**
- Clean minimalist aesthetic with soft gray lines and muted blue accent color
- Rounded rectangles for each stage, thin connecting arrows
- Light drop shadows for subtle depth
- Modern sans-serif typography

**Output:**
- Single 16:9 infographic, white background
- Clear hierarchy between headings, labels, and body text

**Content:**
- Title: "User Journey – Pro Plan Signup"
- Stages: Awareness → Consideration → Signup → Onboarding → Activation → Retention
- Stage details:
  - Awareness: "Discovers product via ad or referral" / Metric: Impressions
  - Consideration: "Visits pricing page, reads reviews" / Metric: Site visits
  - Signup: "Creates free account" / Metric: Signups
  - Onboarding: "Completes setup wizard" / Metric: Completion rate
  - Activation: "Invites first team member" / Metric: Activation %
  - Retention: "Returns weekly, upgrades to paid" / Metric: WAU

**Layout:**
- Horizontal flow from left to right with arrows between stages
- Title at top center
- Each stage as a card with description above and metric below

**Constraints:**
- English text only
- All text fully readable at 1080p
- No decorative illustrations, icons, or characters

Save the output with filename containing "journey-map-minimalist". Return the full path to the generated image."""

# Generate with 16:9 aspect ratio as specified in the prompt
output_path = generate(
    prompt=prompt,
    aspect_ratio="16:9",
    resolution="1K"
)

if output_path:
    import os
    absolute_path = os.path.abspath(output_path)
    print(f"\n✓ Image generated successfully!")
    print(f"Full path: {absolute_path}")
else:
    print("\n✗ No image was generated.")
