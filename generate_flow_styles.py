#!/usr/bin/env python3
"""
Generate all 13 Flow category styles for the style database
"""
import sys
import os
sys.path.insert(0, '/Users/carl/Documents/Coding projects/claude-code-pm-course')

from image_gen import generate, new_session

# Ensure clean session
new_session()

output_dir = "/Users/carl/Documents/Coding projects/claude-code-pm-course/course-materials/lesson-modules/3-nano-banana/3.1-intro-to-image-gen/3.1.4-style-database/thumbnails"

prompts = [
    # PROCESS STYLES (3)
    {
        "name": "Clean Corporate Process Flow",
        "filename": "process-corporate.png",
        "prompt": """**Task:** Create a horizontal business process diagram showing a product development workflow

**Style:**
- Clean corporate aesthetic with crisp geometric shapes
- Professional color palette: navy blue (#1e40af) for main process boxes, light gray (#f3f4f6) background
- Sans-serif typography (Helvetica/Arial style)
- Subtle drop shadows for depth

**Output:**
- 16:9 landscape orientation
- White background with light grid pattern

**Content:**
- Title: "Product Development Workflow"
- 5 process stages: "Discovery" → "Design" → "Development" → "Testing" → "Launch"
- Each stage has 2-3 sub-bullets (e.g., Discovery: User Research, Market Analysis)
- Arrows connecting each stage

**Layout:**
- Horizontal flow left to right
- Rounded rectangle boxes with consistent spacing
- Bold directional arrows between stages
- Sub-bullets listed below each main stage

**Constraints:**
- English text only
- All text fully readable
- Professional presentation-ready quality"""
    },
    {
        "name": "Whiteboard Sketch Process Cycle",
        "filename": "process-whiteboard.png",
        "prompt": """**Task:** Create a hand-drawn style circular process diagram for agile sprint cycle

**Style:**
- Whiteboard sketch aesthetic with wobbly hand-drawn lines
- Black marker on white background
- Hand-written style font (casual, slightly irregular)
- Arrows with sketchy texture

**Output:**
- Square aspect ratio (1:1)
- White background like a whiteboard

**Content:**
- Title: "2-Week Sprint Cycle" (hand-written at top)
- 6 stages in circular flow: "Planning" → "Daily Standups" → "Development" → "Testing" → "Review" → "Retrospective" → back to Planning
- Small icons next to each stage (simple sketches: calendar, people, laptop, checklist, presentation, chat bubbles)

**Layout:**
- Circular arrangement clockwise
- Each stage in a hand-drawn cloud/bubble shape
- Curved arrows connecting stages in circle
- Center text: "Repeat Every 2 Weeks"

**Constraints:**
- English text only
- All text fully readable
- Authentic whiteboard marker aesthetic"""
    },
    {
        "name": "Colorful Gradient Onboarding Flow",
        "filename": "process-gradient.png",
        "prompt": """**Task:** Create a colorful vertical process diagram for user onboarding flow

**Style:**
- Modern colorful aesthetic with gradient backgrounds
- Vibrant gradient colors: purple to blue (#8b5cf6 to #3b82f6)
- Clean sans-serif white text on colored backgrounds
- Smooth rounded corners and flowing shapes

**Output:**
- Vertical portrait orientation (9:16)
- Soft gradient background (light purple to light blue)

**Content:**
- Title: "User Onboarding Journey" at top
- 4 vertical stages:
  1. "Sign Up" (Email & Password)
  2. "Profile Setup" (Name, Photo, Preferences)
  3. "Guided Tour" (Feature Highlights)
  4. "First Action" (Create First Project)
- Each stage shows duration estimate

**Layout:**
- Vertical flow top to bottom
- Large rounded rectangle cards for each stage
- Connecting lines with circular progress indicators
- Each card has icon, title, description, time estimate

**Constraints:**
- English text only
- All text fully readable with high contrast
- Friendly, welcoming visual style"""
    },

    # FLOWCHART STYLES (3)
    {
        "name": "Professional Decision Tree",
        "filename": "flowchart-professional.png",
        "prompt": """**Task:** Create a professional flowchart showing feature flag rollout decision logic

**Style:**
- Clean technical diagram with sharp edges
- Color-coded shapes: blue rectangles for processes, yellow diamonds for decisions, green ovals for endpoints
- Sans-serif font (Arial/Helvetica)
- Straight connector lines with arrows

**Output:**
- Vertical portrait orientation (3:4)
- White background

**Content:**
- Title: "Feature Flag Rollout Decision Tree"
- Start: "New Feature Ready"
- Decision 1: "Passed QA Testing?" (Yes/No)
- Decision 2: "Risk Assessment Level?" (Low/Medium/High)
- Endpoints: "Full Rollout", "Gradual Rollout (10%→50%→100%)", "Beta Users Only", "Back to Development"
- 8-10 total nodes

**Layout:**
- Top-down vertical flow
- Diamond shapes for decision points
- Rectangles for process steps
- Ovals for start/end points
- Clear yes/no labels on decision branches

**Constraints:**
- English text only
- All text fully readable
- Standard flowchart conventions"""
    },
    {
        "name": "Hand-Drawn User Flow",
        "filename": "flowchart-handdrawn.png",
        "prompt": """**Task:** Create a hand-drawn flowchart showing mobile app user authentication flow

**Style:**
- Casual sketchy style like napkin drawings
- Black pen on light beige paper texture
- Wobbly hand-drawn shapes and arrows
- Handwritten text with slight irregularity

**Output:**
- Square aspect ratio (1:1)
- Beige/cream paper background

**Content:**
- Title: "Mobile Login Flow" (handwritten at top)
- Start: "Open App"
- Decisions: "Has Account?", "Remember Me?", "Biometric Available?"
- Actions: "Show Login Screen", "Enter Credentials", "Biometric Prompt", "Navigate to Home"
- Endpoints: "Success → Dashboard", "Failed → Retry", "New User → Signup"

**Layout:**
- Mixed vertical and horizontal flow
- Sketchy rectangles, diamonds, and ovals
- Arrows with hand-drawn curves
- Annotations and small notes in margins

**Constraints:**
- English text only
- All text fully readable
- Authentic hand-sketched aesthetic"""
    },
    {
        "name": "Dark Mode System Flowchart",
        "filename": "flowchart-dark.png",
        "prompt": """**Task:** Create a modern dark-themed flowchart showing API error handling logic

**Style:**
- Dark background (#0f172a slate-900)
- Neon accent colors: cyan (#06b6d4) for actions, pink (#ec4899) for errors, green (#10b981) for success
- Modern geometric shapes with rounded corners
- Glowing effect on connectors

**Output:**
- Landscape 16:9 orientation
- Dark slate background

**Content:**
- Title: "API Error Handling Flow" (top, cyan text)
- Start: "API Request Sent"
- Decisions: "Response Code?", "Retry Count < 3?", "Fallback Available?"
- Paths: 200 (Success), 4xx (Client Error), 5xx (Server Error), Timeout
- Actions: "Parse Response", "Log Error", "Retry with Backoff", "Use Cached Data", "Show Error Message"
- Endpoints: "Return Data", "Graceful Degradation", "Alert User"

**Layout:**
- Left-to-right primary flow
- Branching paths for error conditions
- Rounded rectangles with glow effects
- Arrows with subtle neon glow

**Constraints:**
- English text only
- High contrast text on dark background
- Modern developer dashboard aesthetic"""
    },

    # STEPS STYLES (3)
    {
        "name": "Numbered Steps Guide",
        "filename": "steps-numbered.png",
        "prompt": """**Task:** Create a clean numbered steps guide for conducting user interviews

**Style:**
- Minimalist design with large numbers
- Color scheme: deep teal (#0d9488) for numbers, black text on white
- Modern sans-serif font
- Generous white space

**Output:**
- Vertical portrait (3:4)
- White background

**Content:**
- Title: "User Interview Guide: 5 Essential Steps"
- Step 1: "Prepare Research Questions" (3-4 bullet points: Define objectives, Create discussion guide, etc.)
- Step 2: "Recruit Participants" (Screen for target users, Schedule 30-45 min sessions)
- Step 3: "Conduct Interview" (Build rapport, Ask open-ended questions, Take notes)
- Step 4: "Analyze Findings" (Identify patterns, Extract key insights)
- Step 5: "Share Results" (Create summary report, Present to stakeholders)

**Layout:**
- Large circled numbers (1-5) on left side
- Step title and description to the right
- Progressive vertical flow
- Consistent spacing between steps

**Constraints:**
- English text only
- All text fully readable
- Clean, professional appearance"""
    },
    {
        "name": "Illustrated Step-by-Step",
        "filename": "steps-illustrated.png",
        "prompt": """**Task:** Create a colorful illustrated step guide for A/B testing process

**Style:**
- Friendly colorful illustrations
- Warm color palette: orange (#f97316), purple (#a855f7), blue (#3b82f6)
- Playful rounded shapes
- Small icons/illustrations for each step

**Output:**
- Horizontal landscape (16:9)
- Light cream background (#fef3c7)

**Content:**
- Title: "How to Run an A/B Test"
- Step 1: "Define Hypothesis" (icon: lightbulb) - "What are you testing and why?"
- Step 2: "Create Variants" (icon: split path) - "Design version A and B"
- Step 3: "Set Success Metrics" (icon: target) - "Choose KPIs to measure"
- Step 4: "Run Experiment" (icon: play button) - "Launch to 50/50 traffic split"
- Step 5: "Analyze Results" (icon: chart) - "Statistical significance reached?"

**Layout:**
- Horizontal left-to-right flow
- Each step in a rounded card with icon at top
- Arrow connectors between cards
- Number badge in corner of each card

**Constraints:**
- English text only
- All text fully readable
- Friendly, approachable design"""
    },
    {
        "name": "Blueprint Technical Steps",
        "filename": "steps-blueprint.png",
        "prompt": """**Task:** Create a technical blueprint-style steps diagram for API integration process

**Style:**
- Blueprint aesthetic: white/cyan lines on dark blue background
- Technical drawing style with grid overlay
- Monospace font for code snippets
- Precise geometric shapes

**Output:**
- Landscape 16:9
- Dark blue background (#1e3a8a) with grid lines

**Content:**
- Title: "API Integration Steps" (blueprint header style)
- Step 1: "Obtain API Key" (Register account, Generate credentials)
- Step 2: "Configure Endpoint" (Set base URL: api.example.com/v2)
- Step 3: "Authenticate Request" (Add Bearer token to headers)
- Step 4: "Make API Call" (Code snippet: GET /users)
- Step 5: "Handle Response" (Parse JSON, Error handling)
- Step 6: "Test & Deploy" (Validate in staging, Monitor production)

**Layout:**
- Vertical stair-step progression
- Each step in a technical box with annotations
- Connection lines with dimensions/labels
- Blueprint-style corner marks

**Constraints:**
- English text only
- Technical drawing conventions
- Monospace font for code elements"""
    },

    # SEQUENCE STYLES (3)
    {
        "name": "Timeline Sequence",
        "filename": "sequence-timeline.png",
        "prompt": """**Task:** Create a horizontal timeline showing product launch sequence

**Style:**
- Clean modern timeline with milestone markers
- Color scheme: gradient from blue (#3b82f6) to purple (#8b5cf6)
- Sans-serif font with clear hierarchy
- Circular milestone nodes on timeline

**Output:**
- Wide horizontal landscape (16:9)
- White background

**Content:**
- Title: "Product Launch Timeline: Q4 2024"
- 6 milestones on horizontal line:
  * Oct 1: "Feature Freeze" (Lock scope, Begin testing)
  * Oct 15: "Beta Launch" (Limited user group)
  * Nov 1: "Marketing Campaign" (Email, social, PR)
  * Nov 15: "Public Launch" (Full availability)
  * Nov 30: "Monitor & Iterate" (Track metrics)
  * Dec 15: "Retrospective" (Team debrief)

**Layout:**
- Horizontal timeline with date markers
- Milestones as circles on the line
- Content cards above/below alternating
- Progress indicator showing current position

**Constraints:**
- English text only
- All text fully readable
- Professional presentation quality"""
    },
    {
        "name": "Swimlane Sequence Diagram",
        "filename": "sequence-swimlane.png",
        "prompt": """**Task:** Create a swimlane sequence diagram showing checkout flow across systems

**Style:**
- Technical swimlane diagram
- Three lanes with different background colors: light blue, light green, light yellow
- Black text and arrows
- Rectangular message boxes

**Output:**
- Vertical portrait (3:4)
- White background with colored lanes

**Content:**
- Title: "E-commerce Checkout Sequence"
- 3 Swimlanes (vertical columns):
  * User (light blue)
  * Web App (light green)
  * Payment Service (light yellow)
- Sequence (top to bottom):
  1. User: "Click Checkout"
  2. Web App: "Validate Cart"
  3. Web App → Payment Service: "Process Payment"
  4. Payment Service: "Authorize Card"
  5. Payment Service → Web App: "Payment Confirmed"
  6. Web App → User: "Show Success"
  7. Web App: "Send Receipt Email"

**Layout:**
- 3 vertical lanes side by side
- Horizontal arrows between lanes
- Sequential actions flow top to bottom
- Clear actor labels at top of lanes

**Constraints:**
- English text only
- All text fully readable
- Standard UML sequence conventions"""
    },
    {
        "name": "Animated Storyboard Sequence",
        "filename": "sequence-storyboard.png",
        "prompt": """**Task:** Create a storyboard-style sequence showing user journey through app onboarding

**Style:**
- Comic/storyboard panel aesthetic
- Colorful illustrated frames
- Speech bubbles and annotations
- Friendly character illustrations (simple stick figures or avatars)

**Output:**
- Grid layout (2x3 = 6 panels)
- Light background with panel borders

**Content:**
- Title: "First-Time User Journey"
- Panel 1: "Opens App" - User looking at welcome screen (speech bubble: "Let's try this!")
- Panel 2: "Creates Account" - Filling out form (thought bubble: "Quick signup!")
- Panel 3: "Sees Tutorial" - Interactive tips highlighted
- Panel 4: "Explores Features" - User tapping around (annotation: "Discovering tools")
- Panel 5: "Completes First Task" - Success animation (speech: "That was easy!")
- Panel 6: "Shares with Friend" - Sending invite (annotation: "Viral loop activated!")

**Layout:**
- 2 columns × 3 rows of panels
- Each panel like a comic frame
- Sequential flow left-to-right, top-to-bottom
- Numbered panels (1-6)

**Constraints:**
- English text only
- All text fully readable
- Storyboard/comic book style"""
    },

    # JOURNEY-MAP STYLE (1 more needed)
    {
        "name": "Journey Map Dashboard",
        "filename": "journey-map-dashboard.png",
        "prompt": """**Task:** Create a comprehensive customer journey map for SaaS trial-to-paid conversion

**Style:**
- Modern dashboard/infographic aesthetic
- Multi-row layout with different data types
- Color-coded sentiment: green (positive), yellow (neutral), red (pain points)
- Clean data visualization elements

**Output:**
- Wide horizontal landscape (16:9)
- White/light gray background

**Content:**
- Title: "Customer Journey Map: Free Trial → Paid Subscription"
- 5 phases (columns): "Awareness" → "Trial Signup" → "Activation" → "Engagement" → "Conversion"
- 4 rows per phase:
  * User Actions (what they do)
  * Emotions (sentiment icons: happy/neutral/frustrated)
  * Pain Points (red flags where friction occurs)
  * Opportunities (green lightbulbs for improvements)
- Example content:
  * Awareness: Search for solution, Read reviews, Visit website
  * Trial Signup: Create account (Pain: Too many form fields)
  * Activation: First login, Setup workspace (Opportunity: Better onboarding)

**Layout:**
- Horizontal timeline across top
- 4 horizontal swim lanes for different data types
- Each column represents a journey phase
- Icons, short text, color-coding throughout

**Constraints:**
- English text only
- All text fully readable
- Professional UX research aesthetic"""
    }
]

print("Starting generation of 13 Flow category styles...\n")

results = []
for i, style in enumerate(prompts, 1):
    print(f"\n{'='*60}")
    print(f"Generating {i}/13: {style['name']}")
    print(f"{'='*60}")

    try:
        # Generate image
        output_path = generate(
            prompt=style['prompt'],
            aspect_ratio="16:9" if "landscape" in style['prompt'] or "16:9" in style['prompt'] else
                         "3:4" if "portrait" in style['prompt'] or "3:4" in style['prompt'] else
                         "9:16" if "9:16" in style['prompt'] else
                         "1:1",
            resolution="2K"
        )

        # Move to proper location with correct filename
        import shutil
        final_path = os.path.join(output_dir, style['filename'])
        if output_path and os.path.exists(output_path):
            shutil.move(output_path, final_path)
            print(f"✓ Saved to: {final_path}")

            results.append({
                "filename": style['filename'],
                "name": style['name'],
                "status": "success"
            })
        else:
            print(f"✗ Failed to generate {style['filename']}")
            results.append({
                "filename": style['filename'],
                "name": style['name'],
                "status": "failed"
            })

    except Exception as e:
        print(f"✗ Error generating {style['filename']}: {str(e)}")
        results.append({
            "filename": style['filename'],
            "name": style['name'],
            "status": "error",
            "error": str(e)
        })

print(f"\n{'='*60}")
print("GENERATION COMPLETE")
print(f"{'='*60}")
print(f"\nSuccess: {len([r for r in results if r['status'] == 'success'])}/13")
print(f"Failed: {len([r for r in results if r['status'] != 'success'])}/13")

if any(r['status'] != 'success' for r in results):
    print("\nFailed items:")
    for r in results:
        if r['status'] != 'success':
            print(f"  - {r['name']}: {r.get('error', 'failed')}")
