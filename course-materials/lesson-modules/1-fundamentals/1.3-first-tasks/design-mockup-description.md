DESIGN MOCKUP: TASKFLOW DARK MODE
Designer: Jordan Kim
Version: v3 (Final for review)
Date: October 8, 2024
Figma Link: [figma.com/taskflow-dark-mode-v3]

═══════════════════════════════════════════════════════════════════

OVERVIEW:

Jordan presented the final dark mode mockups for TaskFlow. This is version 3 after incorporating feedback from engineering and product teams. The design covers the main application screens: project board, task detail view, navigation, and settings.

═══════════════════════════════════════════════════════════════════

COLOR PALETTE:

Background Colors:
- Primary background: #1a1a1a (very dark gray, not pure black)
- Secondary background: #242424 (slightly lighter for cards/panels)
- Tertiary background: #2e2e2e (for hover states)

Text Colors:
- Primary text: #f0f0f0 (off-white, not pure white - reduces eye strain)
- Secondary text: #b0b0b0 (gray for less important text)
- Disabled text: #666666 (darker gray)

Accent Colors:
- Primary brand (blue): #4d9fff (lighter than light mode #2563eb)
- Success (green): #4ade80 (lighter than light mode)
- Warning (yellow): #fbbf24 (same as light mode, already bright)
- Error (red): #f87171 (lighter than light mode)
- Links: #60a5fa (lighter blue, distinct from primary brand)

Borders/Dividers:
- Subtle borders: #333333 (barely visible, just enough to separate)
- Strong borders: #444444 (for emphasized separation)

═══════════════════════════════════════════════════════════════════

KEY SCREENS SHOWN:

1. PROJECT BOARD VIEW:
- Left sidebar navigation with dark #1a1a1a background
- Main content area #242424 background
- Task cards with #2e2e2e background
- Column headers (To Do, In Progress, Done) with subtle #333333 borders
- Task cards have rounded corners (8px) and subtle shadow
- Hover state: task card background lightens to #363636

2. TASK DETAIL VIEW:
- Right-side slide-out panel
- Panel background: #242424
- Task title in large #f0f0f0 text
- Task description with markdown rendering (code blocks have #1a1a1a background)
- Comments section at bottom with threaded replies
- Attachment previews with thumbnail borders
- Action buttons (Edit, Complete, Delete) with appropriate accent colors

3. TOP NAVIGATION:
- Fixed header, #1a1a1a background
- Search bar with #2e2e2e background, #333333 border
- User avatar and settings icons in #f0f0f0
- Notification bell with badge (red #f87171 if unread)

4. SETTINGS MODAL:
- Modal overlay with 60% opacity black (#000000 at 0.6)
- Modal content: #242424 background, rounded corners (12px)
- Form inputs with #2e2e2e background
- Toggle switches for dark mode setting (on/off/auto based on system)

═══════════════════════════════════════════════════════════════════

NOTABLE DESIGN DECISIONS:

Contrast Ratios:
Jordan verified all text meets WCAG AA standards (4.5:1 for normal text, 3:1 for large text). Primary text (#f0f0f0 on #1a1a1a) has 11.5:1 ratio. Secondary text (#b0b0b0 on #1a1a1a) has 6.2:1 ratio.

Not Pure Black:
"I'm using #1a1a1a instead of #000000 because pure black on OLED screens can cause eye strain with pure white text. Slightly lighter black is easier on the eyes."

Syntax Highlighting:
Code blocks in task descriptions use a dark syntax theme (similar to VS Code's Dark+ theme). Jordan included examples with JavaScript, Python, and JSON.

User-Uploaded Images:
Images in task attachments have a subtle #333333 border to separate them from the background. Jordan noted: "If users upload screenshots with white backgrounds, they'll look weird. The border helps."

Icons:
All icons are #f0f0f0 or #b0b0b0 depending on importance. Jordan adjusted several icons that were too thin (looked faint in dark mode) - made them slightly bolder.

═══════════════════════════════════════════════════════════════════

INTERACTION STATES:

Hover States:
- Buttons: background lightens by ~10%
- Task cards: background goes from #2e2e2e to #363636
- Links: underline appears

Focus States:
- Blue outline (#4d9fff) for keyboard navigation
- 2px solid outline, 4px offset
- Ensures accessibility for keyboard users

Active/Pressed States:
- Buttons: background darkens slightly, scale down to 98%
- Creates tactile feedback

Disabled States:
- Reduced opacity (50%)
- Cursor changes to not-allowed
- Text color shifts to #666666

═══════════════════════════════════════════════════════════════════

WHAT'S WORKING WELL:

✓ Contrast is excellent - very readable
✓ Accent colors pop without being harsh
✓ Consistent spacing and hierarchy
✓ Smooth transitions between light/dark (Jordan showed animation)
✓ Brand identity maintained (still feels like TaskFlow)
✓ Code blocks look great (important for engineer users)

═══════════════════════════════════════════════════════════════════

CONCERNS / QUESTIONS FROM REVIEW:

1. USER-UPLOADED IMAGES:
Issue: Screenshots with white backgrounds will look jarring
Jordan's solution: Add border, but might not be enough
Alternative: Add background pattern behind images (like Slack does?)
DECISION NEEDED: How to handle this? Test with real content?

2. CHART/GRAPH COLORS:
Issue: Reports page has charts (velocity, burndown). Jordan showed examples but colors might need adjustment.
Concern: Chart libraries (we use Recharts) have default colors that won't work in dark mode.
ACTION: Engineering needs to test chart library dark mode support

3. THIRD-PARTY EMBEDS:
Issue: Figma embeds, Google Doc embeds - we don't control their appearance
Jordan: "If someone embeds a Figma mockup, it'll be light mode. We can't change that."
DECISION NEEDED: Accept that embedded content won't match theme? Or hide embeds in dark mode?

4. MOBILE APP:
Issue: Jordan designed this for web. Mobile needs separate consideration.
Question: Does mobile launch with dark mode? Or ship mobile without dark mode initially?
Alex (mobile PM) needs to weigh in.

5. MARKETING SITE:
Issue: Should our marketing site (taskflow.com) have dark mode too?
Or just the app?
Jordan: "That's extra scope. Marketing site is separate codebase."
DECISION NEEDED: App only or app + marketing site?

6. DEFAULT MODE:
Issue: Should dark mode be opt-in or opt-out?
Options:
  a) Default to light mode (current behavior)
  b) Default to system preference (auto-detect OS theme)
  c) Default to dark mode (force everyone to dark)
Jordan suggests option B (system preference)
DECISION NEEDED: Product and engineering to decide

═══════════════════════════════════════════════════════════════════

TECHNICAL IMPLEMENTATION NOTES:

Jordan worked with Jamie (eng lead) on implementation approach:

CSS Variables:
Use CSS custom properties for colors:
--background-primary: #1a1a1a;
--text-primary: #f0f0f0;
etc.

Toggle switches between light/dark by changing root CSS variables.

Persistence:
User preference stored in database (user settings)
Also stored in localStorage for instant load

Animation:
Smooth transition when toggling (0.2s ease)
Jordan: "No jarring flashing between modes"

System Preference Detection:
Use prefers-color-scheme media query
Respects OS-level dark mode setting

Per-Component Overrides:
Some components might need special handling (charts, embeds)
Engineering to identify edge cases during implementation

═══════════════════════════════════════════════════════════════════

ROLLOUT STRATEGY:

Jordan suggests:
1. Beta test with internal team first (dogfood)
2. Invite 100 power users to test (opt-in beta)
3. Gather feedback, fix issues
4. Public launch with announcement

Marketing opportunity:
- Blog post: "TaskFlow Dark Mode is Here"
- Social media campaign
- Email to all users
- In-app banner announcement

═══════════════════════════════════════════════════════════════════

NEXT STEPS:

[ ] Product (me): Decision on user-uploaded images, embeds, default mode
[ ] Engineering (Jamie): Investigate chart library dark mode support
[ ] Mobile (Alex): Decide if mobile launches with dark mode
[ ] Marketing: Plan launch campaign (if going forward)
[ ] Design (Jordan): Address feedback, finalize specs for engineering

═══════════════════════════════════════════════════════════════════

PERSONAL NOTES:

This looks really polished. Jordan clearly put a lot of thought into contrast, accessibility, and edge cases. The design feels modern and premium - definitely something that will delight our engineering users.

Main concerns are the edge cases (user-uploaded content, embeds, charts). We need to test with real messy data, not just pristine mockups.

Overall: Strong yes to move forward. This will be a big win for user satisfaction and team morale.
