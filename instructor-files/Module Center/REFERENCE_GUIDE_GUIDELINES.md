# Reference Guide Writing Guidelines
## Best Practices for Creating Module Reference Guides

**Last Updated:** October 13, 2025
**Purpose:** Ensure all REFERENCE_GUIDE.md files are comprehensive, standalone, and valuable for self-study

> **Note:** This document covers how to write **REFERENCE_GUIDE.md files** (comprehensive, standalone documentation). For guidelines on writing **CLAUDE.md files** (interactive teaching scripts), see **MODULE_TEACHING_GUIDELINES.md**.

---

## 🎯 Core Principles

### 1. **Standalone & Complete**
Reference guides must be fully understandable WITHOUT doing the interactive module. Readers should be able to:
- Learn the concept completely from the guide alone
- Apply what they learned in their own work
- Come back later to refresh their knowledge
- Share with team members who aren't taking the course

### 2. **Comprehensive but Scannable**
Include ALL relevant information, but structure it so readers can:
- Quickly find what they need
- Skim for key points
- Deep-dive into specific sections
- Jump to exactly what's relevant

### 3. **Reference First, Tutorial Second**
Think "handbook chapter" not "step-by-step tutorial". The interactive module handles tutorials. The reference guide is the resource you'd want bookmarked.

---

## 📋 Required Structure

Every REFERENCE_GUIDE.md must include these sections in this order:

### Header Block
```markdown
# Module X.Y: [Title]
## Reference Guide

**Last Updated:** [Date]
**Time to Complete:** [Estimate for interactive module]
**Prerequisites:** [What you need to know/have first]

---
```

**Why:** Sets expectations and helps readers assess if they're ready.

### 1. Overview Section (📖)
```markdown
## 📖 Overview

[2-3 sentences explaining what this module covers]

**Key takeaway:** [Single sentence summarizing the most important insight]
```

**What to include:**
- What problem this solves
- Why it matters
- Main concept in plain language
- ONE key takeaway they should remember

**Length:** 1-2 short paragraphs max

---

### 2. Core Content Sections
The meat of the guide. Structure depends on the topic, but typically includes:

**For Tool/Feature Modules:**
- What it is (concept explanation)
- When to use it (real-world scenarios)
- How it works (mechanics)
- Examples (concrete use cases)
- Best practices
- Limitations/gotchas

**For Workflow Modules:**
- The workflow step-by-step
- Why each step matters
- Variations and alternatives
- Real PM scenarios
- Templates and examples
- Tips for efficiency

**Formatting rules:**
- Use H3 (###) for major topics
- Use H4 (####) for subtopics
- Use emoji headers sparingly (for major sections only)
- Include code blocks, file trees, examples liberally
- Break up text with lists, callouts, diagrams

---

### 3. Setup/Configuration Section (if applicable)
For modules that require setup (Obsidian, MCP servers, integrations):

```markdown
## 🚀 Setup Guide

### Step 1: [First thing to do]
[Detailed instructions]

### Step 2: [Next thing]
[Detailed instructions]
```

**Requirements:**
- Step-by-step instructions
- Platform-specific guidance (Mac/Windows/Linux)
- Screenshots or ASCII diagrams where helpful
- Troubleshooting for common issues
- Links to official documentation

---

### 4. Examples & Use Cases
```markdown
## 💼 Real-World Examples

### Example 1: [Scenario name]
**Scenario:** [Realistic PM situation]

**How to approach:**
[Step-by-step or explanation]

**Outcome:**
[What you achieve]
```

**Best practices:**
- Use TaskFlow company context
- Reference specific personas (Sarah, Mike, Alex)
- Include before/after comparisons
- Show actual commands/prompts
- Explain the "why" not just the "how"

---

### 5. Best Practices Section
```markdown
## 💡 Best Practices

### Do:
- ✅ [Specific action to take]
- ✅ [Another good practice]

### Don't:
- ❌ [Common mistake to avoid]
- ❌ [Anti-pattern]

### Pro Tips:
1. **[Tip title]** - [Explanation]
2. **[Another tip]** - [Explanation]
```

**Include:**
- Dos and don'ts
- Pro tips for power users
- Common mistakes and how to avoid them
- Efficiency shortcuts
- When to use vs. when not to use

---

### 6. Troubleshooting Section
```markdown
## 🐛 Troubleshooting

### "[Error message or problem]"

**Likely cause:** [Why this happens]

**Fix:**
1. [Step to resolve]
2. [Another step]
3. [Final verification]

### "[Another common issue]"
...
```

**Requirements:**
- Address actual common issues
- Include error messages users will see
- Provide clear, actionable fixes
- Link to additional resources if needed
- Cover platform-specific problems (Mac/Windows)

---

### 7. Community Resources & Further Reading
```markdown
## 📚 Community Resources

**Official Documentation:**
- [Link] - [What you'll find here]
- [Link] - [What you'll find here]

**Community Examples:**
- [GitHub repo] - [Description of what's available]
- [Forum thread] - [Topic covered]

**Related Tools & Plugins:**
- [Tool name] - [How it extends this capability]

**Further Reading:**
- [Blog post] - [Topic]
- [Video tutorial] - [What it covers]
```

**IMPORTANT:** This section should include:
- Official docs from Anthropic/Claude Code
- Community GitHub repos with examples
- For agent modules: repos with pre-built agents
- For MCP modules: MCP server registries
- For tools: related plugins and extensions
- Blog posts and tutorials from the community
- Relevant forum discussions or Reddit threads

**Quality standards:**
- Only link to maintained, quality resources
- Provide context for each link (don't just list URLs)
- Organize by category (Official, Community, Tools, etc.)
- Keep links up-to-date (review quarterly)

---

### 8. What's Next Section
```markdown
## 🚀 What's Next?

### After Module X.Y

You now understand:
- ✅ [Key learning 1]
- ✅ [Key learning 2]
- ✅ [Key learning 3]

**Ready for Module X.Z?**

[Brief preview of next module - what they'll learn and why it matters]

**[Go to Module X.Z Reference →](../X.Z-module-name/REFERENCE_GUIDE.md)**

Or, if you're doing the interactive track:
```
Type: /start-X-Z
```
```

**Purpose:**
- Summarize key learnings
- Preview next module
- Provide clear navigation
- Maintain momentum

---

## ✍️ Writing Style

### Tone
- **Professional but approachable** (like a knowledgeable colleague, not a textbook)
- **Clear and direct** (no fluff, but not robotic)
- **Encouraging** (build confidence without being condescending)
- **Practical** (focus on real PM work, not abstract concepts)

### Language
- **Active voice:** "You'll learn how to..." not "How to learn will be..."
- **Second person:** Use "you" and "your" throughout
- **Present tense:** "Claude reads the file" not "Claude will read the file"
- **Plain English:** Avoid jargon, or define it when necessary

### Formatting
- **Bold** for emphasis and key terms
- **Code blocks** for commands, file paths, examples
- **Lists** for steps, features, tips (easier to scan than paragraphs)
- **Tables** for comparisons or feature matrices
- **Callouts** (using blockquotes with emoji) for important notes

**Example callout:**
```markdown
> ⚠️ **Important:** Hidden folders starting with `.` won't show in Obsidian. Use Finder/Explorer instead.
```

---

## 🎨 Visual Elements

### When to Use

**ASCII diagrams - Use for:**
- File structure trees
- Workflow visualizations
- Before/after comparisons
- System architecture

**Example:**
```
┌─────────────────────┬─────────────────────┐
│   Terminal          │   Obsidian          │
│   (Claude Code)     │   (File Viewer)     │
└─────────────────────┴─────────────────────┘
```

**Code blocks - Use for:**
- Commands to run
- File contents
- Example prompts
- Configuration snippets

**Tables - Use for:**
- Feature comparisons
- Keyboard shortcuts
- Parameter documentation
- Before/after scenarios

### When NOT to Use
- ❌ Decorative ASCII art that doesn't add clarity
- ❌ Excessive emoji (1-2 per section header is enough)
- ❌ Complex tables that are hard to read in markdown
- ❌ Images (use ASCII representations instead for portability)

---

## 📊 Content Depth

### The Right Amount

**Too shallow:**
```markdown
## Agents
Agents let you run tasks in parallel. Use them for multiple tasks.
```

**Too deep:**
```markdown
## Agents
[5000 words explaining the technical implementation, token management,
parallel processing architecture, edge cases, theoretical computer
science concepts...]
```

**Just right:**
```markdown
## Agents - Clone Yourself for Parallel Work

### What Are Agents?
Agents are independent instances of Claude that run in parallel. Think of
them as clones of yourself working on different tasks simultaneously.

### When to Use Agents
- **Multiple similar tasks:** Processing 10 meeting notes, researching 5 competitors
- **Time-sensitive work:** Need results fast, can parallelize
- **Independent work:** Tasks don't depend on each other

[Continues with examples, best practices, real scenarios...]
```

### Balance Guidelines
- **Concept explanation:** 2-3 paragraphs
- **How-to sections:** Step-by-step with context
- **Examples:** 2-3 concrete scenarios
- **Best practices:** 5-7 key points
- **Troubleshooting:** 3-5 common issues

**Total length:**
- Simple modules: 800-1,200 words
- Standard modules: 1,500-2,500 words
- Complex modules: 3,000-4,000 words

---

## 🔗 Linking Strategy

### Internal Links (Within Course)
- Link to other module reference guides
- Link to level overview pages
- Use relative paths: `../1.2-module/REFERENCE_GUIDE.md`
- Provide context: "See [Module 1.4: Agents](../1.4-agents/REFERENCE_GUIDE.md) for parallel processing"

### External Links (To Community Resources)
- **Always** link to official Anthropic/Claude Code docs
- Link to maintained GitHub repos with examples
- Link to active community forums/discussions
- Include publication date or "last updated" when possible

**Format:**
```markdown
**Official Docs:**
- [Claude Code Documentation](URL) - Getting started guide

**Community Examples:**
- [awesome-claude-agents](https://github.com/example/awesome-claude-agents) - Collection of 50+ pre-built agents for various tasks
- [claude-code-mcp-servers](https://github.com/example/mcp-servers) - Community MCP server implementations

**Pro Tips:**
- [Building Better Sub-Agents](URL) - Blog post by [Author]
```

### Link Quality Standards
- ✅ Test all links before publishing
- ✅ Use HTTPS (not HTTP)
- ✅ Link to specific sections when possible (#heading-anchor)
- ✅ Provide context (what's at the link)
- ❌ Don't link to paywalled content without noting it
- ❌ Don't link to outdated or unmaintained resources

---

## ✅ Pre-Publish Checklist

Before marking a reference guide as complete, verify:

### Structure
- [ ] Header block with date, time estimate, prerequisites
- [ ] Overview section with key takeaway
- [ ] Core content organized with clear hierarchy
- [ ] Examples section with 2-3 real scenarios
- [ ] Best practices section
- [ ] Troubleshooting section (if applicable)
- [ ] Community resources & further reading section
- [ ] What's next section with navigation

### Content Quality
- [ ] Standalone (can be understood without interactive module)
- [ ] Comprehensive (covers all important aspects)
- [ ] Practical (includes real PM use cases)
- [ ] Accurate (all commands/examples tested)
- [ ] Complete (no TODO sections or placeholders)

### Writing Quality
- [ ] Professional but approachable tone
- [ ] Active voice, second person ("you")
- [ ] Plain English (jargon defined)
- [ ] Scannable (good use of lists, headings, formatting)
- [ ] Free of typos and grammatical errors

### Links & Resources
- [ ] All internal links tested and working
- [ ] All external links tested and working
- [ ] Official documentation linked
- [ ] Community resources included
- [ ] Link context provided (not just naked URLs)

### Formatting
- [ ] Consistent emoji usage (not overdone)
- [ ] Code blocks properly formatted
- [ ] File paths use backticks
- [ ] Lists formatted consistently
- [ ] Headings follow hierarchy (no skipped levels)

### Technical Accuracy
- [ ] All commands tested on Mac
- [ ] Windows-specific guidance included where different
- [ ] File paths are correct
- [ ] Version-specific info noted if applicable
- [ ] Edge cases and limitations mentioned

---

## 🚫 Common Mistakes to Avoid

### 1. Assuming Context from Interactive Module
**Bad:** "As we covered earlier with the files..."
**Good:** "When working with files in Claude Code, you can..."

### 2. Tutorial Step-by-Step When Reference is Better
**Bad:** "First, type this. Then type that. Now do this..."
**Good:** "To process meeting notes, use the following pattern: [explanation with example]"

### 3. Missing Community Resources
**Bad:** Ending guide with no external links
**Good:** Comprehensive section with repos, docs, forums, examples

### 4. Too Much "We'll Cover This Later"
**Bad:** "We'll learn more about this in Module X.Y"
**Good:** "This feature is covered in-depth in [Module X.Y](link), including [brief preview of what's there]"

### 5. No Real-World Context
**Bad:** "Here's how agents work [technical explanation]"
**Good:** "Scenario: It's Monday morning and you have 10 meeting recordings from last week to process before your 10am standup..."

### 6. Outdated Information
**Bad:** Links to deprecated tools, old syntax, removed features
**Good:** Regularly updated content with "Last Updated" dates

---

## 💡 Examples of Great Reference Guides

### Within This Course
- **Module 1.1 Reference:** Great structure, clear overview, comprehensive Q&A
- **Module 1.2 Reference:** Excellent setup guide, platform-specific instructions

### External Inspiration
- Stripe API documentation (clarity and examples)
- MDN Web Docs (comprehensive but scannable)
- Figma Help Center (practical use cases)

---

## 🤝 How Reference Guides Relate to Other Docs

```
Reference Guides (REFERENCE_GUIDE.md)
├── Complement: CLAUDE.md (teaching scripts) - Reference is comprehensive, CLAUDE is interactive
├── Reference: MODULE_TEACHING_GUIDELINES.md - Guidelines for interactive modules
├── Align with: HIGH_LEVEL_COURSE_OVERVIEW.md - Overall course structure
└── Support: Community resources - Link to external examples and tools
```

**Key relationship:**
- CLAUDE.md = Learn by doing (interactive)
- REFERENCE_GUIDE.md = Learn by reading (comprehensive)
- Both cover the same content, different formats

---

## ✨ Final Thoughts

**A great reference guide is:**
- The resource you bookmark and return to months later
- Something you'd share with a colleague who didn't take the course
- Comprehensive enough to stand alone
- Practical enough to apply immediately
- Clear enough to skim, deep enough to study

**Your goal:** Write the guide you wish existed when you were learning.

---

**Related Documents:**
- [MODULE_TEACHING_GUIDELINES.md](MODULE_TEACHING_GUIDELINES.md) - Guidelines for interactive modules
- [COURSE_MECHANICS.md](COURSE_MECHANICS.md) - How the course system works
- [HIGH_LEVEL_COURSE_OVERVIEW.md](HIGH_LEVEL_COURSE_OVERVIEW.md) - Course structure
