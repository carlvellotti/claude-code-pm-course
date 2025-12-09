# Module Outline Process - Step 1

This document defines **Step 1** of the module outline process for the Claude Code PM Course.

## File Naming Convention

Outline files use this format: `OUTLINE_[module-id]_[lesson-name].md`

Examples:
- `OUTLINE_3.1.1_welcome.md`
- `OUTLINE_3.1.3_style.md`
- `OUTLINE_1.4_agents.md`

This file contains both Step 1 (high-level overview) and Step 2 (teaching flow). Step 3 creates the final `CLAUDE.md` script.

---

## Step 1: Create High-Level Overview

Before writing the detailed teaching flow, create a simple high-level overview with:

1. **Files Needed to Start** - List all files that must exist before the module begins
2. **Files Created During Module** - List all files that will be created during the lesson
3. **High-Level Overview** - Single bulleted list of key concepts (no nested bullets, very simple)
   - **Important:** Explicitly mention files/folders when they're used (e.g., "review `feature-spec.md`" or "in `.claude/agents/`")

**Example:**
```markdown
# Module 1.4: Agents - Outline

## Files Needed to Start
- `meeting-notes/meeting-notes-1.md` through `meeting-notes-10.md` (10 messy meeting notes)

## Files Created During Module
- All 10 meeting notes edited (summaries appended to each)
- `competitive-landscape-matrix.md` (synthesis of all 5 competitor analyses)

## High-Level Overview
- Introduce the concept of agents (cloning Claude to work in parallel)
- Demonstrate parallel processing with 10 files in `meeting-notes/` processed simultaneously
- Explain what agents are (independent Claude instances)
- Demonstrate competitive research with 5 agents analyzing 5 competitors via web search
- Show advanced orchestration with 4 specialized agents on `user-interviews/`, `survey-results.csv`, `support-tickets/`, and `sales-notes.md`
- Explain when to use agents vs regular sequential work

---

## Teaching Flow

[Step 2 content goes here after approval...]
```

**Key point:** Get alignment on this high-level overview BEFORE writing the detailed teaching flow (Step 2) in the same file.
