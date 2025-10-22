---
name: pptx
description: Create PowerPoint presentations from markdown documents. Use this skill when users need to transform strategy documents, PRDs, or analysis into professional slide decks for stakeholder presentations.
---

# PowerPoint Presentation Creation Skill

You can create professional PowerPoint presentations (.pptx files) from markdown documents. This skill is designed to help Product Managers transform their written work into executive-ready slide decks.

## Capabilities

- Convert markdown documents into PowerPoint presentations
- Create appropriate slide layouts based on content structure
- Apply professional formatting and design
- Generate title slides, content slides, and summary slides
- Support for strategy presentations, PRDs, and analysis documents

## When to Use This Skill

Use this skill when users need to:
- Create executive presentations from strategy documents
- Transform written analysis into slide decks
- Present PRDs or feature specs to stakeholders
- Generate professional slides for leadership reviews

## How to Create Presentations

When creating a presentation, follow this workflow:

### 1. Analyze the Source Document

Read the markdown document and identify:
- Main sections that should become slides
- Key points and supporting details
- Visual hierarchy and flow
- Executive summary content

### 2. Design the Slide Structure

Plan the presentation structure:
- **Title Slide**: Document title, date, context
- **Executive Summary**: Key takeaways (1-2 slides)
- **Main Content Slides**: One slide per major section
- **Details Slides**: Supporting information, broken down for readability
- **Closing Slides**: Summary, next steps, or calls to action

### 3. Create the Presentation

Use Python with the `python-pptx` library to generate the .pptx file:

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

# Create presentation object
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# Define reusable layouts
def add_title_slide(prs, title, subtitle):
    slide = prs.slides.add_slide(prs.slide_layouts[0])  # Title layout
    slide.shapes.title.text = title
    slide.placeholders[1].text = subtitle
    return slide

def add_content_slide(prs, title, content_items):
    slide = prs.slides.add_slide(prs.slide_layouts[1])  # Title and Content layout
    slide.shapes.title.text = title

    # Add content as bullet points
    body = slide.placeholders[1].text_frame
    for item in content_items:
        p = body.add_paragraph()
        p.text = item
        p.level = 0
    return slide

def add_section_slide(prs, section_title):
    slide = prs.slides.add_slide(prs.slide_layouts[2])  # Section header layout
    slide.shapes.title.text = section_title
    return slide

# Example: Create slides
add_title_slide(prs, "Strategy Title", "Presentation Date")
add_section_slide(prs, "Section 1: Diagnosis")
add_content_slide(prs, "Key Findings", [
    "Finding 1: Description here",
    "Finding 2: Description here",
    "Finding 3: Description here"
])

# Save presentation
prs.save('output.pptx')
```

### 4. Format Guidelines

Apply professional formatting:

**Typography:**
- Title fonts: 44pt for slide titles, 54pt for section headers
- Body text: 18-24pt for main content, 16pt for details
- Use sans-serif fonts (Calibri, Arial, or Helvetica)

**Layout:**
- Maximum 3-5 bullet points per slide
- Use 2-column layouts for comparisons
- Break dense content across multiple slides
- Leave whitespace for readability

**Content Principles:**
- One key idea per slide
- Use active, concise language
- Bullets should be parallel in structure
- Include slide numbers for reference

**Special Slide Types:**

*Strategy Slides:*
- Diagnosis → Guiding Policy → Actions structure
- Use visual hierarchy to show relationships
- Highlight tradeoffs and key decisions

*Roadmap Slides:*
- Timeline view with quarters/months
- Group related initiatives
- Call out dependencies

*Metrics Slides:*
- Current vs. target performance
- Use simple tables or charts (describe verbally, implement as formatted text)
- Include success criteria

## Output

After creating the presentation:
1. Save the .pptx file with a descriptive name
2. Confirm the file location to the user
3. Summarize the slide structure (number of slides and key sections)
4. Note any content that was simplified or restructured for presentation format

## Dependencies

This skill requires the `python-pptx` library. If not installed, guide the user to install it:

```bash
pip install python-pptx
```

## Best Practices

- **Executive-first**: Start with summary slides that executives can read in 2 minutes
- **Scannable**: Each slide should be understandable in 10 seconds
- **Actionable**: End with clear next steps or decisions needed
- **Professional**: Use consistent formatting throughout
- **Context-aware**: Adjust formality and detail based on the audience

## Example Usage

**User request**: "Create a slide deck from my strategy document"

**Your workflow**:
1. Read the strategy document
2. Identify key sections (Diagnosis, Guiding Policy, Actions, etc.)
3. Plan ~12-15 slides covering the strategy
4. Generate Python code using python-pptx
5. Create the .pptx file
6. Confirm creation and summarize structure

## Notes

- For this course, presentations are used to transform PM documents (strategies, PRDs, analyses) into stakeholder-ready formats
- Focus on clarity and professionalism over visual design complexity
- When in doubt, use simple layouts with clear hierarchy
- The goal is to make written work presentation-ready, not to create marketing materials
