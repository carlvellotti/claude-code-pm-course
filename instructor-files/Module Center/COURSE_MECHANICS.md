# Claude Code PM Course - How It Works
## Course Mechanics & Structure

**Last Updated:** October 11, 2025

> **Note:** This document explains the high-level course architecture - how the system works, repository structure, and user journey. For tactical guidelines on **how to write individual modules** (teaching patterns, interactive flow, best practices), see **MODULE_TEACHING_GUIDELINES.md**.

---

## 🎯 Core Philosophy

This course is **guided by Claude Code itself**. Users don't read instructions and then execute - instead, Claude Code acts as their instructor, walking them through every step, demonstrating concepts, and providing real-time feedback.

**Think of it as:** An interactive workshop where Claude is your personal instructor, not a traditional course where you read and then try things.

---

## 📁 Repository Structure

```
claude-code-pm-course/
├── README.md (Start here! Explains setup)
├── CLAUDE.md (Root - tells Claude this is a course)
│
├── company-context/
│   ├── COMPANY.md (TaskFlow background story)
│   ├── PRODUCT.md (Product details)
│   ├── PERSONAS.md (User personas)
│   └── COMPETITIVE.md (Market context)
│
├── exercises/
│   ├── 1.1-welcome/
│   │   ├── CLAUDE.md (Module 1.1 teaching script for Claude)
│   │   └── (no files yet - just context)
│   │
│   ├── 1.2-visualization/
│   │   ├── CLAUDE.md (Module 1.2 teaching script)
│   │   └── (guides on opening VS Code/Obsidian)
│   │
│   ├── 1.3-first-tasks/
│   │   ├── CLAUDE.md (Module 1.3 teaching script)
│   │   ├── meeting-notes-raw.txt
│   │   ├── user-interviews.txt
│   │   ├── product-sync-notes.txt
│   │   └── stakeholder-emails.txt
│   │
│   ├── 1.4-agents/
│   │   ├── CLAUDE.md (Module 1.4 teaching script)
│   │   ├── meeting-notes-1.txt (10 files for parallel demo)
│   │   ├── meeting-notes-2.txt
│   │   ├── ... (meeting-notes-3 through 10)
│   │   ├── competitor-brief-1.md (5 competitors)
│   │   └── ... (competitor-brief-2 through 5)
│   │
│   ├── 1.5-commands/
│   │   ├── CLAUDE.md
│   │   └── (exercises for commands)
│   │
│   ├── 1.6-files/
│   │   ├── CLAUDE.md
│   │   ├── competitor-research/ (folder with multiple docs)
│   │   ├── user-feedback.csv
│   │   └── design-mockups/ (images)
│   │
│   ├── 1.7-claude-md/
│   │   ├── CLAUDE.md
│   │   └── (students create their own CLAUDE.md here)
│   │
│   ├── 2.1-planning-mode/
│   ├── 2.2-prds/
│   ├── 2.3-user-stories/
│   ├── 2.4-research/
│   ├── 2.5-communication/
│   └── ... (all other modules)
│
├── reference/
│   ├── COMMANDS.md
│   ├── KEYBOARD_SHORTCUTS.md
│   ├── PROMPTING_LIBRARY.md
│   └── ... (other reference docs)
│
└── .claude/
    └── commands/
        ├── start-1-1.md (slash command to begin Module 1.1)
        ├── start-1-2.md
        ├── start-1-3.md
        └── ... (slash command for each module)
```

---

## 🎓 How Users Progress Through the Course

### Starting a New Module

Users type a slash command to start each module:

```bash
/start-1-1    # Starts Module 1.1
/start-1-2    # Starts Module 1.2
/start-1-3    # Starts Module 1.3
# etc.
```

**What happens when they type `/start-1-1`:**

1. The slash command (`.claude/commands/start-1-1.md`) contains:
   ```markdown
   Read the CLAUDE.md file in exercises/1.1-welcome/ and follow the teaching script.
   You are the instructor guiding the user through Module 1.1.
   ```

2. Claude reads `exercises/1.1-welcome/CLAUDE.md`

3. Claude begins the guided instruction based on that script

---

## 📋 What's in Each Module's CLAUDE.md?

Each module has a `CLAUDE.md` file that serves as **Claude's teaching script**. This tells Claude:

1. **What to say** to the user
2. **What to demonstrate**
3. **What to ask the user to do**
4. **How to check their understanding**
5. **When to move to the next step**
6. **What real-world context to provide**

### Example: Module 1.3 CLAUDE.md Structure

```markdown
# Module 1.3: Your First PM Tasks

## Your Role as Instructor
You are guiding the user through realistic PM scenarios. Always provide context for
WHY they're doing something and WHEN they'd use this in real work.

## Lesson Flow

### Step 1: Set the Scene

Say to user:
"Welcome to Module 1.3! Here's the scenario: It's 5pm on a Friday. You've been in
back-to-back meetings all day and took rough notes. Now you need to:
- Extract all action items before the weekend
- Figure out what YOU need to do Monday morning
- Send a quick summary to your team

This is where Claude Code shines. Let's process those meeting notes together.

First, let me show you what meeting notes we have. I'm going to list the files
in the exercises/1.3-first-tasks/ folder."

Then execute: ls exercises/1.3-first-tasks/

### Step 2: Demonstrate

Say to user:
"I see we have meeting-notes-raw.txt. Let me read it and show you what I can do."

Then execute: Read @exercises/1.3-first-tasks/meeting-notes-raw.txt

After reading, say:
"I just read the file. Now watch as I create a clean summary with action items
organized by person."

Then create the summary and explain:
"See what just happened? I:
1. Read the entire file (Read tool)
2. Identified all action items
3. Organized them by owner
4. Created a clean format

In about 5 seconds. Manually, this would take 15-20 minutes!"

### Step 3: User's Turn

Say to user:
"Now it's your turn! We have another file called user-interviews.txt.

Try asking me: 'Read the user-interviews.txt file and give me the top 3 pain
points, organized by user type.'

You can use your own words - practice prompting naturally!"

Wait for their input...

### Step 4: Provide Feedback

When they ask:
- Execute the task
- Explain what you did
- Give feedback: "Great job! You prompted clearly and got exactly what you needed.
  Notice how you didn't need to know any technical commands - just plain English."

### Step 5: Real-World Context

Say:
"In your real PM work, you'd get these files by:
- Copying from Otter.ai or Fireflies transcription
- Exporting from Google Docs
- Pasting from Notion
(We'll cover automated imports from Google Drive and Notion in Module 4.1!)

For this course, all files are pre-created so you can focus on learning."

### Step 6: Transition

Say:
"Excellent work! You've completed Module 1.3. You now know how to:
- Have Claude read and analyze files
- Process meeting notes and research
- Get insights from documents quickly

Ready for Module 1.4? That's where things get REALLY interesting - you'll learn
how to clone me and run 10 tasks in parallel!

Type /start-1-4 when you're ready."

## Success Criteria
User has:
- Watched you demonstrate file reading
- Successfully prompted you to analyze a file
- Understood the real-world workflow
- Feels confident with basic file operations

## Troubleshooting

If user seems confused:
- Offer: "Would you like me to show you an example prompt?"
- Provide: "Try typing: 'Analyze the user-interviews file and extract pain points'"

If user asks about file locations:
- Explain: "All course files are in the exercises/ folder. I can see them and
  work with them. You can also open this folder in VS Code or Obsidian to see
  them visually (we covered this in Module 1.2)."
```

---

## 🔄 The Teaching Loop

For every module, Claude follows this pattern:

1. **Set the scene** - Explain the real-world scenario
2. **Demonstrate** - Show the user first
3. **Guide practice** - Have the user try with coaching
4. **Provide context** - Explain when/why they'd use this
5. **Check understanding** - Quick validation
6. **Transition** - Point to next module

This ensures users never feel lost and always understand the "why" behind each feature.

---

## 🎨 Module Types

### Type A: Demonstration Modules
**Example:** Module 1.1, 1.2

Claude shows and explains. User watches and learns.

**CLAUDE.md focus:**
- Clear explanations
- What to demonstrate
- What to show them

### Type B: Guided Practice Modules
**Example:** Module 1.3, 1.4

Claude demonstrates first, then user practices.

**CLAUDE.md focus:**
- Demo script
- Prompts to suggest to user
- Feedback templates
- Success criteria

### Type C: Independent Work Modules
**Example:** Advanced modules (3.x, 4.x)

User does the work with Claude as a reference.

**CLAUDE.md focus:**
- Scenario description
- Success criteria
- Where to get help
- Less hand-holding

---

## 📚 Reference Materials

Users can access reference materials anytime:

```bash
# View command reference
Open reference/COMMANDS.md

# View keyboard shortcuts
Open reference/KEYBOARD_SHORTCUTS.md

# View prompting library
Open reference/PROMPTING_LIBRARY.md
```

These are separate from the guided course - they're for lookup when needed.

---

## 🔀 Non-Linear Navigation

While the course is designed to be followed sequentially, users can:

1. **Jump to any module:** `/start-2-3` to skip ahead
2. **Return to previous modules:** `/start-1-2` to review
3. **Access reference anytime:** Open reference docs
4. **Work on real projects:** Use course context as template

**Root CLAUDE.md handles this:**
```markdown
If user jumps to advanced module without basics:
"I notice you're starting Module 4.2 (MCPs). This assumes you know:
- Modules 1.1-1.4 (basics)
- Module 2.1 (planning mode)

Have you completed those? If not, I recommend starting with /start-1-1.
But if you want to proceed anyway, I'll guide you through!"
```

---

## 🎯 Root CLAUDE.md - The Orchestrator

The root `CLAUDE.md` file tells Claude about the entire course:

```markdown
# Claude Code PM Course - Root Context

## What This Is
You are teaching a comprehensive Claude Code course for Product Managers using
the TaskFlow fictional company. This is an interactive, guided course where YOU
are the instructor.

## Course Structure
- Level 0: Setup (2 modules)
- Level 1: Foundation (7 modules)
- Level 2: Practitioner (6 modules)
- Level 3: Power User (3 modules)
- Level 4: Expert (2 modules)
- Level 5: Master (3 modules)

## Your Teaching Style
- Proactive and encouraging
- Always explain WHY and WHEN
- Demonstrate first, then have them practice
- Provide real-world context for every concept
- Use TaskFlow examples throughout
- Never assume they know terminal commands

## How Modules Work
When user types /start-X-Y:
1. Read exercises/X.Y-module-name/CLAUDE.md
2. Follow that module's teaching script
3. Guide them step-by-step
4. Transition to next module when complete

## Module-Specific Instructions
Each module has detailed teaching scripts in its CLAUDE.md file.

## Non-Linear Learning
Users can jump around. If they skip prerequisites:
- Gently suggest going back
- But allow them to proceed if they insist
- Provide extra context for skipped concepts

## TaskFlow Context
TaskFlow is a fictional PM tool (like Asana meets Linear).
All documents (PRDs, meeting notes, research) are pre-created.
Details in company-context/ folder.

## Getting Help
If user is stuck: Be patient, provide examples, offer to demonstrate.
If technical issues: Point to reference/TROUBLESHOOTING.md

## Your Goal
By the end of this course, users should be able to build their own
"Product OS" - a complete PM automation system using Claude Code.
```

---

## 🎬 Example User Journey

Let's walk through what a user experiences:

### Module 0.2: Setup
```
User: claude
Claude: Hi! I'm Claude Code. I'm ready to help.

User: Clone the course repository from github.com/example/claude-pm-course

Claude: I'll clone the course repository for you.
[Executes: git clone ...]
[Executes: cd claude-pm-course]

Done! I've cloned the course and we're now in the course directory.

I can see this is the Claude Code PM Course! Ready to start learning?

Type /start-1-1 to begin Module 1.1: Welcome to TaskFlow
```

### Module 1.1: Welcome
```
User: /start-1-1

Claude: [Reads exercises/1.1-welcome/CLAUDE.md]

Welcome to Module 1.1!

You're about to learn Claude Code through TaskFlow, a fictional project
management SaaS company (think Asana meets Linear). You're the Product Manager.

Throughout this course, you'll work with real documents from TaskFlow's
product team - meeting notes, PRDs, user research, competitive analysis,
and more. Everything is pre-created, so you can focus on learning.

Let me show you what files we're working with. I'll list the files in our
company-context folder:

[Executes: ls company-context/]

We have:
- COMPANY.md - TaskFlow's background story
- PRODUCT.md - Product details and features
- PERSONAS.md - Our target users
- COMPETITIVE.md - Market landscape

Let me give you a quick overview by reading the COMPANY.md file...

[Continues with guided instruction...]

Great! Now you understand TaskFlow. In the next module, I'll show you how
to visualize all these files so you can see what I'm creating and editing.

Ready? Type /start-1-2 for Module 1.2: Visualizing Your Files
```

### Module 1.3: First PM Task
```
User: /start-1-3

Claude: [Reads exercises/1.3-first-tasks/CLAUDE.md]

Welcome to Module 1.3!

Here's the scenario: It's 5pm on a Friday. You've been in back-to-back
meetings all day - a product sync, stakeholder check-in, and planning
session. You took rough notes during each meeting.

Now you need to:
- Extract all action items before the weekend
- Figure out what YOU need to do Monday morning
- Send a quick summary to your team

This is where Claude Code shines. Let's process those meeting notes.

First, let me show you what files we have:
[Executes: ls exercises/1.3-first-tasks/]

I see we have meeting-notes-raw.txt. Let me read it and show you what I can do.
[Executes: Read @exercises/1.3-first-tasks/meeting-notes-raw.txt]

I just read the file. Now watch as I create a clean summary with action items...

[Creates beautiful formatted summary]

See what just happened? In about 5 seconds, I:
1. Read the entire file (Read tool)
2. Identified all action items
3. Organized them by owner
4. Created a clean format you can copy into Slack

Manually, this would take 15-20 minutes. You just saved yourself time and
can actually enjoy your Friday evening!

Now it's your turn! We have another file called user-interviews.txt.

Try asking me: "Read the user-interviews.txt file and give me the top 3
pain points, organized by user type."

You can use your own words - practice prompting naturally!

User: Read the user-interviews.txt file and give me the top 3 pain points

Claude: [Executes task]

Great job! You prompted clearly and got exactly what you needed.

[Provides analysis...]

Notice how you didn't need to know any technical commands - just plain English.

[Continues with more scenarios...]

Excellent work! Ready for Module 1.4? That's where things get REALLY
interesting - you'll learn how to clone me and run 10 tasks in parallel!

Type /start-1-4 when you're ready.
```

### Module 1.4: Agents (The "Wow" Moment)
```
User: /start-1-4

Claude: [Reads exercises/1.4-agents/CLAUDE.md]

Welcome to Module 1.4 - this is where things get WILD! 🤯

Here's a question: What if you had 10 meeting note files to summarize?
Or 5 competitors to research?

You COULD ask me to do them one by one... or...

You could clone me and have 10 versions of me work in parallel!

Let me show you. I'm going to list the meeting notes in this folder:
[Executes: ls exercises/1.4-agents/]

I see 10 meeting note files: meeting-notes-1.txt through meeting-notes-10.txt

Now watch this. I'm going to spin up 10 agents (clones of myself) and have
each one summarize a different file simultaneously:

[Executes: Launches 10 agents in parallel]

Agent 1: Processing meeting-notes-1.txt ✓
Agent 2: Processing meeting-notes-2.txt ✓
Agent 3: Processing meeting-notes-3.txt ✓
... (all 10 running at the same time!)

Done! All 10 summaries complete in about 30 seconds.

If I did these sequentially, it would take 5 minutes.
If YOU did them manually, it would take 2+ hours.

**This is what makes Claude Code WAY more powerful than a chatbot.**

Think about it:
- 5 competitors to research? 5 agents.
- 20 user interviews to analyze? 20 agents.
- Multiple data sources to synthesize? Multiple agents.

You're not limited to one task at a time. You can clone me as many times
as you need!

Ready to try? We have 5 competitor briefs in this folder...

[Continues guiding them through hands-on agent practice...]
```

---

## 🎓 Progression & Pacing

### Self-Paced Learning
- Users control when to move to next module
- No time limits or deadlines
- Can take breaks and return anytime
- Claude remembers progress (via CLAUDE.md context)

### Suggested Pacing
- **Level 0 (Setup):** 15-30 minutes
- **Level 1 (Foundation):** 3-4 hours (can split over multiple sessions)
- **Level 2 (Practitioner):** 4-5 hours
- **Level 3 (Power User):** 3-4 hours
- **Level 4 (Expert):** 3-4 hours
- **Level 5 (Master):** 2-3 hours

**Total:** ~20 hours for complete course

### Module Length
- Short modules: 15-20 minutes (1.1, 1.2)
- Medium modules: 30-45 minutes (1.3, 1.4, 1.5)
- Long modules: 60-90 minutes (2.2 PRDs, 4.1 MCPs)

---

## 🔧 Technical Implementation

### Slash Commands (`.claude/commands/`)

Each module has a corresponding slash command:

**File: `.claude/commands/start-1-3.md`**
```markdown
Read and follow the teaching script in exercises/1.3-first-tasks/CLAUDE.md

You are the instructor for Module 1.3: Your First PM Tasks.

Guide the user through the lesson step-by-step as described in the CLAUDE.md file.
Be encouraging, provide context, and check their understanding.

When they complete the module, guide them to /start-1-4 for the next lesson.
```

### Nested CLAUDE.md Files

The course uses **nested CLAUDE.md files** for context hierarchy:

```
Root CLAUDE.md (course-level context)
    ↓
exercises/1.3-first-tasks/CLAUDE.md (module-specific teaching script)
```

When Claude reads the module's CLAUDE.md, it has:
1. Root course context (always loaded)
2. Module-specific instructions (loaded on demand)

### File Organization

**Pre-created files for exercises:**
- All meeting notes, PRDs, research docs are included
- Users NEVER need to create their own example content
- Focus is on learning Claude Code, not creating fake data

**User-generated files:**
- Some modules have users create their own CLAUDE.md
- Some exercises result in new files (summaries, PRDs, etc.)
- These stay in their folders for reference

---

## 📊 Progress Tracking

### How Users Know Where They Are

**Option 1: Ask Claude**
```
User: What module am I on?

Claude: Based on our conversation, you've completed:
- Module 1.1: Welcome to TaskFlow ✓
- Module 1.2: Visualizing Files ✓
- Module 1.3: First PM Tasks ✓

You're currently in Module 1.4: Agents

Next up: Module 1.5: Essential Commands (/start-1-5)
```

**Option 2: Progress Command**
```
User: /progress

Claude: [Checks completed modules based on session history]

Your Progress:
Level 1: Foundation
- 1.1 Welcome ✓
- 1.2 Visualization ✓
- 1.3 First Tasks ✓
- 1.4 Agents ← (current)
- 1.5 Commands (not started)
...
```

---

## 🎯 Design Principles

### 1. **Zero Terminal Knowledge Required**
Users never need to learn terminal commands. Claude executes everything.

### 2. **Context-First**
Every exercise starts with "Here's the real-world scenario..."

### 3. **Show, Then Do**
Claude demonstrates first, then user practices.

### 4. **Immediate Feedback**
Claude provides feedback after every user action.

### 5. **Always Explain Why**
Every feature includes "When would you use this in real PM work?"

### 6. **Progressive Complexity**
Start simple (read a file), build to advanced (orchestrate 10 agents with MCPs).

### 7. **Pre-Created Context**
Everything is ready to go - no "imagine you have..." needed.

### 8. **Meta-Learning**
Learning Claude Code BY USING Claude Code.

---

## 🚀 Getting Started (User Experience)

**Step 1:** Install Claude Code (Module 0.1)
**Step 2:** Type `claude` and tell it to clone the course repo (Module 0.2)
**Step 3:** Type `/start-1-1` and let Claude guide you
**Step 4:** Follow Claude's instructions, practice, and learn!

That's it. The entire course is guided by Claude from that point forward.

---

## 📝 Summary

This course is **fundamentally different** from traditional courses:

❌ **NOT a traditional course:**
- Read instructions
- Try to execute
- Get stuck
- Re-read instructions
- Maybe figure it out

✅ **Claude Code guided course:**
- Claude tells you what to do
- Claude demonstrates
- You practice with coaching
- Claude provides feedback
- You learn by doing, with an expert instructor

**The user experience is:**
"I'm learning Claude Code FROM Claude Code, with Claude as my personal instructor who never gets tired and always explains why."

That's the magic. 🎩✨
