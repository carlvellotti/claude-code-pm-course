---
pillar: P2 - AI Fluency
supported_tools:
  - Claude Code
  - Cursor
  - Nano Banana
last_updated: 2025-12-04
tags:
  - theme_ai_image
  - theme_ai_tool_nano_banana
---

## Deliverables

- [ ] **In-tool course** - 3 modules for Claude Code / Cursor PM course (see outline below)
- [ ] **Shitpost** - "How to fake anything for job interviews" (and other applications)
- [ ] **Cheatsheet** - Quick reference for image gen settings, prompts, common patterns
- [ ] **Story carousel** - "How Michael Scott would use Gemini Pro"
- [ ] **Free giveaway** - Prompt templates + style database files
- [ ] **PDF lead magnet** - Comprehensive reference combining all docs into one mega-guide (how the model works, settings, techniques, use cases)

---

## Module Outline

### Module 1: Introduction to Image Generation

**1.1 Welcome & First Generation**
- Quick setup: API key from Google AI Studio → `.env` file
- Immediate win: Generate a "ready to learn" image (course mascot, celebration, etc.)
- What you'll learn in this course:
  - Product mockups & wireframes
  - Persona visualizations
  - Architecture diagrams
  - Ad creatives & marketing assets
  - And more...
- How it works (brief): Pre-built module, simple functions, Claude handles the rest
- Pricing context: Cheaper than wrapper apps, pay per generation

**1.2 Understanding the Basics**
- The `generate()` function and what it returns
- Output folder structure
- Available parameters: aspect ratio, resolution, model choice
- Sessions: how iterative editing works

**1.3 Consistency & Style**
- Using reference images
- Multi-image inputs (style ref + content ref)
- Deconstructing existing images to extract their style
- Building a style database (JSON/markdown)
- The meta-skill: building your personal creative toolkit

**1.4 Iteration Strategies**
- Sessions vs reference images for editing:
  - Continuing in a session: Gemini remembers full context, precise edits work
  - Passing same image as reference each time: Errors compound, edits get misinterpreted
- Recommended workflow: generate → refine in session → `revert()` if wrong turn → continue
- When to `new_session()`: Starting a completely different image concept
- Generating variants: Make a few options, pick one, then iterate on that in its session

---

### Module 2: PM Use Cases

**2.1 Users & Product Visuals**
- 2.1a Persona visualizations
- 2.1b User journey mapping / flow visualizations
- 2.1c Hand-drawn → polished wireframes
- 2.1d Product mockups in context (device frames, lifestyle)

**2.2 Strategy & Architecture Visuals**
- 2.2a Architecture / system diagrams
- 2.2b Pitch deck visuals
- 2.2c Strategy framework diagrams / process docs

**2.3 Ad & Marketing Assets**
- 2.3a Ad creative assets
- 2.3b Feature announcement graphics

---

### Module 3: Build Your Own Image Tool

**The Project: Style Transformer**
- Upload an image → choose a style → output in that style
- Core features:
  - Apply existing styles from your database
  - Save new styles manually
  - Auto-deconstruct uploaded style images (advanced)

---

## Notes

- Source material: [[gemini-image-generation-learnings]] from carousel experiment
- Course repo: https://github.com/carlvellotti/claude-code-pm-course
- Lesson format: CLAUDE.md teaching scripts with Say/Check/Action blocks
- Each module section becomes a hands-on exercise in Claude Code

### Open Questions
- ~~How to structure the reusable generation scripts?~~ → Resolved: `image_gen.py` module
- What's the actual hands-on project for Module 2? (generate assets for a fictional product launch?)
- Style database format: JSON vs markdown table?

### Implementation Decisions

**API Key Storage: `.env` file approach**
- Add `.env.example` to course-materials with `GEMINI_API_KEY=your_key_here`
- Module 1.1 teaches: get key from Google AI Studio → copy `.env.example` to `.env` → paste key
- Python scripts use `python-dotenv` to load: `load_dotenv()` then `os.environ.get('GEMINI_API_KEY')`
- Teaching script must guide students through this setup before first generation

**Multi-turn as primary pattern**
- The API is stateless, but SDK's chat feature manages conversation history client-side
- Multi-turn enables natural iteration: "generate this" → "now make it bluer" → "add a shadow"
- Gemini 3 Pro uses "thought signatures" to preserve reasoning context across turns - handled automatically by SDK
- Session persistence: save/restore chat history to `.image_session.json` between Claude Code turns

**Pre-built `image_gen.py` module**
- Single module handles all image generation, session management, output saving
- Claude calls simple functions rather than writing new scripts each time
- Key functions:
  - `generate(prompt, reference_images=None, aspect_ratio="1:1", resolution="2K")` - Generate/refine, auto-continues session
  - `new_session()` - Clear session, start fresh
  - `session_info()` - Show current session status
  - `revert(turns=1)` - Undo last N turns (removes from history)
- Session file stores: conversation history, generated images (base64), thought signatures
- Outputs saved to `outputs/` folder with sequential numbering

**Two interaction modes**
- **Claude decides:** User describes intent ("make a persona card"), Claude picks smart defaults
- **User specifies:** User explicitly requests parameters ("use 16:9 aspect ratio"), Claude honors them
- Module 1 teaches all available parameters so users *can* control them, but don't *have* to

**Available parameters (Gemini 3 Pro):**
- `aspect_ratio`: "1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"
- `resolution`: "1K", "2K", "4K"
- `reference_images`: Up to 14 images (6 objects, 5 humans for consistency)
- `model`: "gemini-2.5-flash-image" (fast) or "gemini-3-pro-image-preview" (advanced)

**Session vs Image Reference Testing (2025-12-05)**
Ran comparison tests: 3 image types (diagram, product photo, ad creative) x 4 turns each x 2 conditions (with session vs image-ref only).

Results:
- **Sessions win for structural edits** - Image-ref made errors (double Redis, wrong connections)
- **Sessions win for precise text changes** - Image-ref added text instead of replacing
- **Sessions win for cumulative edits** - Reflection carried through all turns with session, ignored with image-ref
- **Both handle style/lighting reasonably** - This is where image-ref is acceptable

Conclusion: Sessions are worth the complexity. Thought signature preservation enables accurate iterative editing that image-reference alone cannot match. For the course, we'll use simple linear sessions (no branching/named sessions) to keep complexity manageable.

Test outputs: `session-test/` folder in repo

**Future: Open Source the Module**
Plan to extract `image_gen.py` as a standalone open source package. Useful beyond the course because:
- Handles thought signatures (the hard part)
- Session persistence across script executions
- Simple API works with any AI coding tool (Claude Code, Cursor, etc.)

Potential repo: `gemini-image-gen` or similar. Extract when course is stable.

---

## Swipe File

```dataview
TABLE description, platform
FROM "🎨 Content Creation/📂 Swipe File/Examples"
WHERE contains(tags, this.tags)
LIMIT 10
```
