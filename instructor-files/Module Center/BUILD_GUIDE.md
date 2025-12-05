# Course Building Guide
## How Everything Fits Together

**Last Updated:** October 13, 2025
**Purpose:** Central hub connecting all course development documentation

---

## 🎯 What This Is

This document explains how the various course development documents work together. Read this first to understand the system, then dive into the specific guidelines as needed.

---

## 📚 The Documentation System

### Overview Documents (Read These First)

**[HIGH_LEVEL_COURSE_OVERVIEW.md](HIGH_LEVEL_COURSE_OVERVIEW.md)**
- Complete course structure: all levels, all modules
- Learning objectives and prerequisites for each module
- Use this to understand what each module should teach

**[COURSE_MECHANICS.md](COURSE_MECHANICS.md)**
- How the course system works (slash commands, teaching loop, file organization)
- User journey examples
- Use this to understand the technical architecture

### Building Guidelines (Reference While Building)

**[OUTLINE_PROCESS.md](OUTLINE_PROCESS.md)**
- Quick outline process for planning modules before writing
- High-level overview format (files needed, files created, key concepts)
- Detailed teaching flow format (ACTION/STOP/USER prefixes, student-driven commands)
- Use this to quickly iterate on module structure before building

**[MODULE_TEACHING_GUIDELINES.md](MODULE_TEACHING_GUIDELINES.md)**
- How to write interactive modules (CLAUDE.md files)
- Fourth-wall rules, gate system, user prompts
- Includes complete checklist

**[REFERENCE_GUIDE_GUIDELINES.md](REFERENCE_GUIDE_GUIDELINES.md)**
- How to write reference guides (REFERENCE_GUIDE.md files)
- Required sections, writing style, community resources
- Includes complete checklist

### Supporting Documents

**[COMMUNITY_RESOURCES_TODO.md](COMMUNITY_RESOURCES_TODO.md)**
- What community resources to research and link
- Search terms and quality standards
- Track progress on finding resources

---

## 🏗️ What You're Building

Each module consists of **4 components:**

```
exercises/X.Y-module-name/
├── CLAUDE.md              # Interactive teaching script (follows MODULE_TEACHING_GUIDELINES.md)
├── REFERENCE_GUIDE.md     # Standalone documentation (follows REFERENCE_GUIDE_GUIDELINES.md)
└── [exercise files]       # Files students work with (TaskFlow context)

.claude/commands/
└── start-X-Y.md           # Slash command to launch the module
```

**Important:** All CLAUDE.md files reference `.claude/SCRIPT_INSTRUCTIONS.md` which contains critical rules for Claude during teaching (no fourth-wall breaking, follow script precisely, etc.).

**Two learning tracks:**
1. **Interactive:** Student types `/start-X-Y`, Claude teaches using CLAUDE.md
2. **Self-study:** Student reads REFERENCE_GUIDE.md on website

Both teach the same content, different formats.

---

## 🔄 The Build Process

### 1. Planning & Outlining
- Check **HIGH_LEVEL_COURSE_OVERVIEW.md** for module objectives
- Review **COURSE_MECHANICS.md** for system patterns
- Use **OUTLINE_PROCESS.md** to create a quick outline:
  - Step 1: High-level overview (files needed, files created, key concepts)
  - Step 2: Get alignment on overview before proceeding
  - Step 3: Write detailed teaching flow (ACTION/STOP/USER format)
- This lets you iterate quickly before writing the full CLAUDE.md

### 2. Build CLAUDE.md
- Convert the outline to the full teaching script format
- Follow **MODULE_TEACHING_GUIDELINES.md** (SAY/STOP/CHECK/ACTION structure)
- Use existing modules as templates
- Check against the checklist in that document

### 3. Build REFERENCE_GUIDE.md
- Follow **REFERENCE_GUIDE_GUIDELINES.md**
- Research community resources (use **COMMUNITY_RESOURCES_TODO.md**)
- Check against the checklist in that document

### 4. Create Exercise Files
- Add to `exercises/X.Y-module-name/`
- Use TaskFlow company context
- Make it feel like real PM work

### 5. Create Slash Command
- Create `.claude/commands/start-X-Y.md`
- Use the standard format (see existing commands):
  ```markdown
  DO NOT tell the user the step you about to take.

  Do this SILENTLY: read `exercises/X.Y-module-name/CLAUDE.md`

  Follow the script PRECISELY.
  ```
- Keep it minimal - all content lives in CLAUDE.md

### 6. Test
- Run through `/start-X-Y` as a student would
- Read REFERENCE_GUIDE.md standalone
- Verify against both checklists

### 7. Commit
```bash
git add exercises/X.Y-module-name/ .claude/commands/start-X-Y.md
git commit -m "Add Module X.Y: [Title]"
```

---

## 🎯 Key Relationships

```
HIGH_LEVEL_COURSE_OVERVIEW.md
    ↓ (What to teach)

OUTLINE_PROCESS.md
    ↓ (Quick outline for iteration)

MODULE_TEACHING_GUIDELINES.md ←→ REFERENCE_GUIDE_GUIDELINES.md
    ↓ (How to teach)              ↓ (How to document)

CLAUDE.md                     REFERENCE_GUIDE.md
(Interactive)                 (Standalone)
    ↓                             ↓
Both use: COURSE_MECHANICS.md (system architecture)
Both use: COMMUNITY_RESOURCES_TODO.md (links to include)
Both use: TaskFlow context (company, personas, scenarios)
```

---

## 🚀 Getting Started

**To build a new module:**
1. Open **HIGH_LEVEL_COURSE_OVERVIEW.md** → Find your module's objectives
2. Open **OUTLINE_PROCESS.md** → Create quick outline (high-level overview + detailed flow)
3. Get alignment on outline before proceeding
4. Open **MODULE_TEACHING_GUIDELINES.md** → Convert outline to full CLAUDE.md teaching script
5. Open **REFERENCE_GUIDE_GUIDELINES.md** → Build REFERENCE_GUIDE.md
6. Create the exercise files and slash command
7. Test both tracks (interactive and self-study)
8. Check both checklists
9. Commit

**To continue existing work:**
1. Check `git status` to see what exists
2. Review existing files against guidelines
3. Identify what's missing from checklists
4. Continue building and test as you go

---

## ✨ That's It

The guidelines documents have all the details. This doc just explains how they fit together.

**Go build!** 🚀

---

## 📄 Quick Links

- [HIGH_LEVEL_COURSE_OVERVIEW.md](HIGH_LEVEL_COURSE_OVERVIEW.md) - What each module teaches
- [COURSE_MECHANICS.md](COURSE_MECHANICS.md) - How the system works
- [OUTLINE_PROCESS.md](OUTLINE_PROCESS.md) - Quick outline process for planning modules
- [MODULE_TEACHING_GUIDELINES.md](MODULE_TEACHING_GUIDELINES.md) - Building CLAUDE.md files
- [REFERENCE_GUIDE_GUIDELINES.md](REFERENCE_GUIDE_GUIDELINES.md) - Building REFERENCE_GUIDE.md files
- [COMMUNITY_RESOURCES_TODO.md](COMMUNITY_RESOURCES_TODO.md) - Resources to link
