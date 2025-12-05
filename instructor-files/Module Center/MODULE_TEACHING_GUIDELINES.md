# Module Teaching Guidelines
## Enhanced Best Practices for Claude Code Course Modules

**Purpose:** Ensure all modules follow consistent, beginner-friendly teaching patterns

> **Note:** This document provides tactical rules for **building individual modules** (how to write teaching scripts, structure interactive flow, manage cognitive load). For understanding the overall course architecture, system design, and how modules fit together, see **COURSE_MECHANICS.md**.

> **Important:** All CLAUDE.md teaching scripts reference **`.claude/SCRIPT_INSTRUCTIONS.md`** which contains the critical rules Claude must follow when teaching (no fourth-wall breaking, follow script precisely, etc.). That file is what Claude reads during lessons. THIS file is what YOU read when building modules.

---

## 🎯 Core Principle: First-Time User Focus

Every module should assume the user has:
- Never used Claude Code before (even if later modules)
- Never used a terminal
- No knowledge of file operations

---

## 🚫 Critical Rule: No Fourth-Wall Breaking

### NEVER Say:
- "I've read the teaching script"
- "Perfect! Now let me begin the module"
- "Following the instructions..."
- "Let me check what I'm supposed to do next"
- "I'll read the CLAUDE.md and..."

### ALWAYS:
- Start directly with the content
- Speak as the instructor, not as an AI following a script
- Stay in character as a teacher throughout
- No meta-commentary about what you're doing behind the scenes

### Implementation in /start-X-Y.md files:
- Embed Step 1 content directly in the slash command file
- Put "Internal Instructions" section AFTER the user-facing content
- Use clear separation (horizontal rule) between user content and internal notes

---

## 🎮 Interactive Flow Architecture

### The Gate System
Every major topic is a "gate" that requires user action to pass through.

**BAD (Info-dump):**
```
"Here's everything about TaskFlow: [5 paragraphs of info]
Now let me tell you about the files: [5 more paragraphs]
And here's how the course works: [5 more paragraphs]"
```

**GOOD (User-initiated gates):**
```
"Here's a brief intro to TaskFlow.

When you're ready to learn more, say: 'Tell me about TaskFlow'"

[User asks]

"Great! Here's the TaskFlow info...

When you're ready to see what files we're working with, say: 'Show me the TaskFlow files'"

[User asks]

"Perfect! I'll search for files now..."
```

### Rules:
1. **Major topic transitions = User initiation required**
2. **Within a topic = Can flow naturally**
3. **Always give specific prompt** to say next
4. **Only ONE option** to say (not "Say A or B or C")

---

## 💬 User Prompt Design

### Specific, Not Ambiguous

**BAD:**
- ❌ "Ready to learn more?" (What do they say?)
- ❌ "Would you like to see the files?" (Yes/No ambiguity)
- ❌ "Any questions?" (Dead end if no questions)
- ❌ "Ready?" (Too vague)

**GOOD:**
- ✅ "When you're ready, say: **'Tell me about TaskFlow'**"
- ✅ "Next, I'll show you the files. Just say: **'Show me the files'**"
- ✅ "Do you have any questions? If not, say: **'No questions'** to continue."

### Formatting:
- Use bold for the exact phrase: **'Show me the files'**
- Use imperative ("Say:") not conditional ("You can say:")
- One option only per prompt
- Exception: Explicit choices ("Say A for X, or B for Y")

---

## 🌉 Section Transitions (No Dead Ends)

### Every Section Must End With:
1. What they just learned (brief recap)
2. What's coming next (preview)
3. Explicit next instruction

**BAD (Dead end):**
```
"By the end, you'll have a complete 'Product OS' that saves 20+ hours per week!"

[User sits there wondering: "Okay... now what?"]
```

**GOOD Option A (Auto-flow):**
```
"By the end, you'll have a complete 'Product OS' that saves 20+ hours per week!

Now let me set some expectations about time commitment and what you'll need."

[Continues automatically to expectations section]
```

**GOOD Option B (User-initiated):**
```
"By the end, you'll have a complete 'Product OS' that saves 20+ hours per week!

Next, I'll explain what you'll need to succeed. Just say: **'What do I need?'**"

[Waits for user]
```

### When to Auto-Flow vs User-Initiated:
- **Auto-flow:** Small transitions within the same topic
- **User-initiated:** Major topic changes, or when user might need a break

---

## ⚠️ Command Execution & UI Context

### Permission Prompts (First Time Only)

**Only warn about permissions THE FIRST TIME in a module:**

```
"I'm going to search for the available files in the TaskFlow directory.

**Quick heads-up:** I'll need to run some bash commands to do this. You'll see
permission prompts pop up asking if you want to approve them. Feel free to click
**'Yes and don't ask again'** - this will make things smoother going forward.

Ready? I'll search for the files now."
```

**After first warning:** Never mention permissions again in that module. Users get it.

### UI Context (Always Provide)

**Before every action, explain what the user will see:**

```
Good:
"I'm going to read the company files. You'll see me use the Read tool -
it'll show which file I'm reading and then display the contents."

"Let me create a summary file. You'll see a Write tool call, and then
the file will appear in your editor if you have it open."

"I'll list the directory contents using ls. You'll see a Bash tool
execution with the file listing."
```

**Why:** Users understand what's happening in the UI, not confused by tool calls.

**Rule:**
- Permission warnings: Once per module (first bash command only)
- UI context: Every time before an action the user is learning about

---

## 💻 Command Selection Guidelines

### Use Universal Commands

**For directory/file listing:**
- ✅ `ls -la` or `ls`
- ✅ `find . -maxdepth 2 -type d`
- ❌ `tree` (often not installed, causes errors)

**For file reading:**
- ✅ Read tool
- ❌ `cat` via Bash (use tool instead)

**For file editing:**
- ✅ Edit tool
- ❌ `sed` or `awk` via Bash

**General principle:**
Use the most universally available commands. If a command might not be installed
by default (like `tree`), don't use it in beginner modules.

---

## 🗺️ Global View Principle

### Users Need Context

At every step, answer three questions:
1. **Where am I?** (What stage of the module/course)
2. **Why am I here?** (Purpose of this step)
3. **What's next?** (Where we're going)

**Example:**
```
"Right now you're just seeing file names. Don't worry - in Module 1.2, I'll show
you how to view and edit these files in your own editor (like VS Code or Obsidian).
For now, let's just get oriented!"
```

### Benefits:
- Reduces anxiety ("Am I supposed to understand this?")
- Shows the learning journey
- Helps users see progress
- Connects pieces together

---

## 🧠 Cognitive Load Management

### One Concept Per Section

**BAD:**
```
"Here are the files. BTW files can be viewed in editors which we'll cover later
but also you can use @ to reference them and there are different file types..."
```

**GOOD:**
```
"Here are the files in the TaskFlow directory:
[Shows files]

Next, I'll give you a quick summary of what's in these files. Just say: 'Give me a summary'"

[Later, in different section:]
"Right now you're just seeing file names. In Module 1.2, I'll show you how to
view and edit these files."
```

### Section Structure:
1. Introduce ONE concept
2. Explain it fully
3. Check understanding
4. Bridge to next concept
5. Repeat

---

## 📝 Teaching Script Structure

### Preferred Format (Based on Module 1.5)

All CLAUDE.md teaching scripts should follow this structure with **CAPS control markers**:

```markdown
# Module X.Y: [Title]

**Teaching Script for Claude Code**

---

## Your Role

You are teaching Module X.Y of the Claude Code PM Course. [Brief description]

**Teaching style:**
- [Key characteristic 1]
- [Key characteristic 2]
- [Key characteristic 3]

---

## Module Learning Objectives

By the end of this module, students should:
1. [Objective 1]
2. [Objective 2]
3. [Objective 3]

---

## Teaching Flow

**SAY:**

"[Natural conversational dialogue in quotes - this is what Claude speaks to the student.
Can be multiple paragraphs flowing naturally.]"

**STOP: Ask user to say 'Show me the team'**

**CHECK:** Wait for student to request

---

**When student says 'Show me the team', say:**

"[Response dialogue in quotes]"

**ACTION:**

[What Claude does behind the scenes:
- Read files
- Run commands
- Launch agents
- Create files]

**Present it like this:**

"[How to format and show the results to the user]"

**STOP: Ask user to open and read `filename.md`**

**CHECK:** Wait for student to view the file

---

[Continue pattern throughout module...]

---

## Important Notes for Claude (You)

**Follow the outline precisely:**
- This outline has STOP points - never skip them
- Wait for student input at each STOP
- Answer questions when students ask

[Additional implementation details, edge cases, troubleshooting]

---

## Success Criteria

Module X.Y is successful if the student:
- ✅ [Success criterion 1]
- ✅ [Success criterion 2]
- ✅ [Success criterion 3]

---

**Remember: [Key reminder about this module's purpose]**
```

### Key Control Markers (Always Use CAPS):

**SAY:** - Dialogue Claude speaks to the student
- Write naturally in quotes
- Can flow across multiple paragraphs
- Include specific prompts in bold: **'Show me the files'**
- No "Say:" prefix needed - quotes indicate speech

**STOP:** - User-initiated gate (wait for student action)
- Be specific: "Ask user to say 'Show me the team'"
- Not: "Wait for user input" (too vague)
- Always follows directly after SAY block

**CHECK:** - Confirmation that you're waiting
- "Wait for student to request"
- "Wait for student response"
- "Wait for student to give the command"
- Always follows directly after STOP

**ACTION:** - What Claude does (tools, commands, file operations)
- Read/write files
- Run bash commands
- Launch agents
- Process data
- Keep concise and actionable

**Present it like this:** - How to format output
- Shows exact formatting for results
- Specifies what the user should see
- Use quotes to show the actual output

### Pattern Flow:

The typical pattern within a teaching section:

1. **SAY:** (dialogue)
2. **STOP:** (specific instruction)
3. **CHECK:** (wait confirmation)
4. `---` (horizontal rule)
5. **When student [does X], say:** (response dialogue)
6. **ACTION:** (behind the scenes work)
7. **Present it like this:** (output formatting)
8. **STOP:** (next gate)
9. **CHECK:** (next wait)
10. `---` (horizontal rule)

Repeat this pattern throughout the module.

### Horizontal Rules for Major Sections:

Use `---` to separate major teaching beats:
- After each STOP/CHECK cycle
- Between different topics
- Before "Important Notes for Claude"
- Before "Success Criteria"

### Meta-Instructions at the End:

Keep implementation details OUT of the teaching flow:
- "Important Notes for Claude (You)" section at end
- "Success Criteria" checklist at end
- Final bold reminder about module purpose

This keeps the teaching flow clean and conversational.

---

## 🎨 Making It Fun (But Not Overdone)

### Visual Elements - Use Sparingly

**When to use ASCII art, boxes, and diagrams:**
- ✅ Module completion celebrations
- ✅ Complex concepts that benefit from visualization (file trees, workflows)
- ✅ Progress indicators at major milestones
- ✅ Important callouts (tips, warnings)

**When NOT to use:**
- ❌ Every single section
- ❌ Decorating normal text
- ❌ Making it look "busy"

**Principle:** Visual elements should ADD clarity, not distraction.

### Emojis - Occasional, Not Constant

**Good uses:**
- ✅ Section headers occasionally (🎯 Learning Objectives)
- ✅ Achievement moments (🎉 Module complete!)
- ✅ Icon indicators (✓ ✗ ⚠️ 💡)
- ✅ File type indicators in trees (📁 📄)

**Avoid:**
- ❌ Every sentence having emojis
- ❌ Multiple emojis per line
- ❌ Emojis that don't add meaning

**Principle:** Emojis for emphasis and clarity, not decoration.

### Real-World Scenarios - Always Include

**Every exercise should have clear real-world context:**

```
Good:
"**Scenario:** It's 5pm Friday. You've been in back-to-back meetings all day
and have 3 sets of rough meeting notes. Your team is waiting for action items
before the weekend. Let's process these notes in 2 minutes instead of 30."
```

**Why it works:**
- Clear time pressure (5pm Friday)
- Relatable situation (back-to-back meetings)
- Concrete outcome (action items)
- Shows value (2 min vs 30 min)

**Template for scenarios:**
1. **When:** Time of day, day of week
2. **Context:** What led to this situation
3. **Problem:** What needs to be solved
4. **Stakes:** Why it matters
5. **Outcome:** What success looks like

### Storytelling - Make TaskFlow Real

**Treat TaskFlow like a real company:**
- Reference specific team members by name
- Mention actual features they're building
- Include realistic constraints (timeline, resources)
- Add business context (why this feature matters)

```
Good:
"You're working on the dark mode feature for TaskFlow. Your CEO Sarah mentioned
in this morning's standup that 3 enterprise customers are blocked on this -
it's a deal-breaker for their security teams. Engineering says it's 2 sprints,
but marketing wants to announce it at the conference in 3 weeks..."
```

---

## 🎬 Slash Command Creation

Every module needs a slash command to start it. Create `.claude/commands/start-X-Y.md` with this simple format:

```markdown
Command to start Module X Lesson Y

DO NOT tell the user the step you're about to take.

Do this SILENTLY: read `lesson-modules/X.Y-module-name/CLAUDE.md`

Follow the script PRECISELY.
```

**That's it.** All content lives in CLAUDE.md. The slash command just tells Claude to read it silently and start teaching.

---

## ✅ Module Completion Checklist

Before shipping any module, verify:

- [ ] No fourth-wall breaking in any step
- [ ] All major transitions are user-initiated
- [ ] Every prompt is specific (bold exact phrase to say)
- [ ] No dead-end sections (all have transitions)
- [ ] Permission warning on FIRST bash command only (not every time)
- [ ] UI context provided before each action
- [ ] Only universal commands used (no `tree`, etc.)
- [ ] Global context provided ("You're seeing X now, you'll learn Y later")
- [ ] One concept per section (no info overload)
- [ ] ZERO assumptions about user knowledge
- [ ] Teaching script has clear Check/Say/Action/Present structure
- [ ] Real-world scenario clearly stated for each exercise
- [ ] Visual elements used sparingly and purposefully
- [ ] Emojis occasional, not constant
- [ ] No gamification (XP, badges, scores)

---

## 🎯 Example: Perfect Module Opening

**❌ BAD:**
```
⏺ Read(exercises/1.1-welcome/CLAUDE.md)
  ⎿  Read 300 lines

⏺ Perfect! I've read the teaching script. Now let me begin Module 1.1.

Welcome to the Claude Code PM Course! Here's everything you need to know about
TaskFlow, the files we have, how the course works, and what you'll learn...
[info dump continues]
```

**✅ GOOD:**
```
Welcome to the Claude Code PM Course! 🎉

I'm Claude, and I'll be your instructor throughout this course. We're going to
learn Claude Code together - a powerful AI tool that can save you 10-20 hours
per week as a Product Manager.

Throughout this course, you'll work for a fictional company called **TaskFlow** -
imagine Asana meets Jira, but built specifically for remote teams. It's a project
management SaaS that's growing fast.

Here's what makes this course different: all the files, documents, and context are
already created for you. You're stepping into a real (fictional) PM role with
active projects, real user personas, and actual work to do!

When you're ready to learn more about TaskFlow, just say: **'Tell me about TaskFlow'**
```

---

## 📚 References

Apply these guidelines alongside:
- **COURSE_MECHANICS.md** - Overall teaching approach
- **HIGH_LEVEL_COURSE_OVERVIEW.md** - Course structure
- **COURSE_OUTLINE.md** - Module content details

These guidelines ENHANCE those documents with specific tactical best practices
learned from building Module 1.1.

---

**Remember:** We're teaching people who have NEVER used Claude Code before. Every
detail matters. Every transition matters. Every prompt matters. Make it so smooth
they don't even notice they're learning - they just feel guided and confident.
