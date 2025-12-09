#!/bin/bash
# Generate all 13 Flow category styles one by one

cd "/Users/carl/Documents/Coding projects/claude-code-pm-course"

python3 -u << 'PYTHON_SCRIPT'
import sys
import os
sys.path.insert(0, '/Users/carl/Documents/Coding projects/claude-code-pm-course')

from image_gen import generate, new_session
import shutil
import json

output_dir = '/Users/carl/Documents/Coding projects/claude-code-pm-course/course-materials/lesson-modules/3-nano-banana/3.1-intro-to-image-gen/3.1.4-style-database/thumbnails'

# Ensure directory exists
os.makedirs(output_dir, exist_ok=True)

# Start fresh
print('Clearing session...', flush=True)
new_session()

styles = []

# ==================================================================
# PROCESS STYLES (3)
# ==================================================================

# 1. Clean Corporate Process Flow
print('\n[1/13] Clean Corporate Process Flow', flush=True)
output = generate('''**Task:** Create a horizontal business process diagram showing a product development workflow

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
- Professional presentation-ready quality''', aspect_ratio='16:9', resolution='2K')

if output and os.path.exists(output):
    shutil.move(output, os.path.join(output_dir, 'process-corporate.png'))
    print('✓ process-corporate.png', flush=True)
    styles.append({"name": "Clean Corporate Process Flow", "category": "Flow", "tags": ["process"], "thumbnail": "thumbnails/process-corporate.png", "exampleUse": "Business processes, operational workflows, SOPs, product development stages"})

# 2. Whiteboard Sketch Process Cycle
print('\n[2/13] Whiteboard Sketch Process Cycle', flush=True)
output = generate('''**Task:** Create a hand-drawn style circular process diagram for agile sprint cycle

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
- Authentic whiteboard marker aesthetic''', aspect_ratio='1:1', resolution='2K')

if output and os.path.exists(output):
    shutil.move(output, os.path.join(output_dir, 'process-whiteboard.png'))
    print('✓ process-whiteboard.png', flush=True)
    styles.append({"name": "Whiteboard Sketch Process Cycle", "category": "Flow", "tags": ["process"], "thumbnail": "thumbnails/process-whiteboard.png", "exampleUse": "Agile sprint cycles, iterative processes, circular workflows, team planning sessions"})

# 3. Colorful Gradient Onboarding Flow
print('\n[3/13] Colorful Gradient Onboarding Flow', flush=True)
output = generate('''**Task:** Create a colorful vertical process diagram for user onboarding flow

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
- Friendly, welcoming visual style''', aspect_ratio='9:16', resolution='2K')

if output and os.path.exists(output):
    shutil.move(output, os.path.join(output_dir, 'process-gradient.png'))
    print('✓ process-gradient.png', flush=True)
    styles.append({"name": "Colorful Gradient Onboarding Flow", "category": "Flow", "tags": ["process"], "thumbnail": "thumbnails/process-gradient.png", "exampleUse": "User onboarding flows, step-by-step guides, mobile app flows, progressive stages"})

# ==================================================================
# FLOWCHART STYLES (3)
# ==================================================================

# 4. Professional Decision Tree
print('\n[4/13] Professional Decision Tree', flush=True)
output = generate('''**Task:** Create a professional flowchart showing feature flag rollout decision logic

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
- Standard flowchart conventions''', aspect_ratio='3:4', resolution='2K')

if output and os.path.exists(output):
    shutil.move(output, os.path.join(output_dir, 'flowchart-professional.png'))
    print('✓ flowchart-professional.png', flush=True)
    styles.append({"name": "Professional Decision Tree", "category": "Flow", "tags": ["flowchart"], "thumbnail": "thumbnails/flowchart-professional.png", "exampleUse": "Decision trees, feature rollout logic, approval workflows, conditional processes"})

# 5. Hand-Drawn User Flow
print('\n[5/13] Hand-Drawn User Flow', flush=True)
output = generate('''**Task:** Create a hand-drawn flowchart showing mobile app user authentication flow

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
- Authentic hand-sketched aesthetic''', aspect_ratio='1:1', resolution='2K')

if output and os.path.exists(output):
    shutil.move(output, os.path.join(output_dir, 'flowchart-handdrawn.png'))
    print('✓ flowchart-handdrawn.png', flush=True)
    styles.append({"name": "Hand-Drawn User Flow", "category": "Flow", "tags": ["flowchart"], "thumbnail": "thumbnails/flowchart-handdrawn.png", "exampleUse": "User flows, authentication logic, mobile app flows, brainstorming sessions"})

# 6. Dark Mode System Flowchart
print('\n[6/13] Dark Mode System Flowchart', flush=True)
output = generate('''**Task:** Create a modern dark-themed flowchart showing API error handling logic

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
- Modern developer dashboard aesthetic''', aspect_ratio='16:9', resolution='2K')

if output and os.path.exists(output):
    shutil.move(output, os.path.join(output_dir, 'flowchart-dark.png'))
    print('✓ flowchart-dark.png', flush=True)
    styles.append({"name": "Dark Mode System Flowchart", "category": "Flow", "tags": ["flowchart"], "thumbnail": "thumbnails/flowchart-dark.png", "exampleUse": "API error handling, system architecture, technical workflows, developer documentation"})

# ==================================================================
# STEPS STYLES (3)
# ==================================================================

# 7. Numbered Steps Guide
print('\n[7/13] Numbered Steps Guide', flush=True)
output = generate('''**Task:** Create a clean numbered steps guide for conducting user interviews

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
- Clean, professional appearance''', aspect_ratio='3:4', resolution='2K')

if output and os.path.exists(output):
    shutil.move(output, os.path.join(output_dir, 'steps-numbered.png'))
    print('✓ steps-numbered.png', flush=True)
    styles.append({"name": "Numbered Steps Guide", "category": "Flow", "tags": ["steps"], "thumbnail": "thumbnails/steps-numbered.png", "exampleUse": "User interview guides, research protocols, step-by-step instructions, procedural documentation"})

# 8. Illustrated Step-by-Step
print('\n[8/13] Illustrated Step-by-Step', flush=True)
output = generate('''**Task:** Create a colorful illustrated step guide for A/B testing process

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
- Friendly, approachable design''', aspect_ratio='16:9', resolution='2K')

if output and os.path.exists(output):
    shutil.move(output, os.path.join(output_dir, 'steps-illustrated.png'))
    print('✓ steps-illustrated.png', flush=True)
    styles.append({"name": "Illustrated Step-by-Step", "category": "Flow", "tags": ["steps"], "thumbnail": "thumbnails/steps-illustrated.png", "exampleUse": "A/B testing processes, experiment workflows, how-to guides, team tutorials"})

# 9. Blueprint Technical Steps
print('\n[9/13] Blueprint Technical Steps', flush=True)
output = generate('''**Task:** Create a technical blueprint-style steps diagram for API integration process

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
- Monospace font for code elements''', aspect_ratio='16:9', resolution='2K')

if output and os.path.exists(output):
    shutil.move(output, os.path.join(output_dir, 'steps-blueprint.png'))
    print('✓ steps-blueprint.png', flush=True)
    styles.append({"name": "Blueprint Technical Steps", "category": "Flow", "tags": ["steps"], "thumbnail": "thumbnails/steps-blueprint.png", "exampleUse": "API integration guides, technical setup procedures, developer documentation, system configuration"})

# ==================================================================
# SEQUENCE STYLES (3)
# ==================================================================

# 10. Timeline Sequence
print('\n[10/13] Timeline Sequence', flush=True)
output = generate('''**Task:** Create a horizontal timeline showing product launch sequence

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
- Professional presentation quality''', aspect_ratio='16:9', resolution='2K')

if output and os.path.exists(output):
    shutil.move(output, os.path.join(output_dir, 'sequence-timeline.png'))
    print('✓ sequence-timeline.png', flush=True)
    styles.append({"name": "Timeline Sequence", "category": "Flow", "tags": ["sequence"], "thumbnail": "thumbnails/sequence-timeline.png", "exampleUse": "Product launch timelines, project milestones, release schedules, roadmap visualization"})

# 11. Swimlane Sequence Diagram
print('\n[11/13] Swimlane Sequence Diagram', flush=True)
output = generate('''**Task:** Create a swimlane sequence diagram showing checkout flow across systems

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
- Standard UML sequence conventions''', aspect_ratio='3:4', resolution='2K')

if output and os.path.exists(output):
    shutil.move(output, os.path.join(output_dir, 'sequence-swimlane.png'))
    print('✓ sequence-swimlane.png', flush=True)
    styles.append({"name": "Swimlane Sequence Diagram", "category": "Flow", "tags": ["sequence"], "thumbnail": "thumbnails/sequence-swimlane.png", "exampleUse": "System interactions, checkout flows, cross-functional processes, service communication"})

# 12. Animated Storyboard Sequence
print('\n[12/13] Animated Storyboard Sequence', flush=True)
output = generate('''**Task:** Create a storyboard-style sequence showing user journey through app onboarding

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
- Storyboard/comic book style''', aspect_ratio='16:9', resolution='2K')

if output and os.path.exists(output):
    shutil.move(output, os.path.join(output_dir, 'sequence-storyboard.png'))
    print('✓ sequence-storyboard.png', flush=True)
    styles.append({"name": "Animated Storyboard Sequence", "category": "Flow", "tags": ["sequence"], "thumbnail": "thumbnails/sequence-storyboard.png", "exampleUse": "User journey flows, onboarding sequences, narrative scenarios, customer experience mapping"})

# ==================================================================
# JOURNEY-MAP STYLE (1)
# ==================================================================

# 13. Journey Map Dashboard
print('\n[13/13] Journey Map Dashboard', flush=True)
output = generate('''**Task:** Create a comprehensive customer journey map for SaaS trial-to-paid conversion

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
- Professional UX research aesthetic''', aspect_ratio='16:9', resolution='2K')

if output and os.path.exists(output):
    shutil.move(output, os.path.join(output_dir, 'journey-map-dashboard.png'))
    print('✓ journey-map-dashboard.png', flush=True)
    styles.append({"name": "Journey Map Dashboard", "category": "Flow", "tags": ["journey-map"], "thumbnail": "thumbnails/journey-map-dashboard.png", "exampleUse": "Customer journey mapping, UX research, trial-to-paid conversion analysis, multi-touchpoint experiences"})

print(f'\n\n{"="*70}')
print(f'GENERATION COMPLETE: {len(styles)}/13 styles')
print(f'{"="*70}')

# Save JSON output
json_path = os.path.join(output_dir, '../flow-styles.json')
with open(json_path, 'w') as f:
    json.dump(styles, f, indent=2)
print(f'\nSaved results to: {json_path}')

PYTHON_SCRIPT
