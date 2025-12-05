# Module Outline Process - Step 2

This document defines **Step 2** of the module outline process for the Claude Code PM Course.

## Step 2: Write the Detailed Teaching Flow

After the `---` divider, write the detailed teaching flow using these standards:

### The Three Prefixes

**For Claude's actions:**
- **ACTION:** Tasks Claude performs (read/create/edit files, run commands, launch agents, present/display information)

**For flow control:**
- **STOP:** Wait for student response (includes questions, checks, conditionals)
- **USER:** Expected student input/action

**Default (no prefix):** Text Claude should speak to the student

### Writing Style Guidelines

**DO:**
- ✅ Write natural conversational dialogue without quotes (assume it's spoken)
- ✅ Use ACTION for any doing (files, commands, agents, displays)
- ✅ Use STOP whenever waiting for student (questions, confirmations, choices)
- ✅ Use USER to document expected student responses
- ✅ **Keep to ONE bullet level deep maximum** (use TABS for sub-bullets, never spaces)
- ✅ Write as a single continuous list from start to finish
- ✅ **Add STOP points frequently to avoid info-dumps** (break up explanations into chunks)
- ✅ **Use section breaks (`---`) to separate major topics** (helps visualize natural pauses)
- ✅ **Have students give commands themselves** - explain the capability, then ask them to request it with the exact command
- ✅ **Give direct actions when teaching NEW mechanics** - prescriptive instructions ("Type this", "Click here") keep students on rails
- ✅ **Use closed validation questions** - "Do you see X?" over "What do you see?" to confirm they're in the right place
- ✅ **Explain BEFORE asking** - tell students what will happen, THEN have them do it (not do it → describe what happened)

**DON'T:**
- ❌ Never write "Say" before dialogue - if there's no prefix, it's assumed to be spoken
- ❌ Never use quotes around dialogue - it's assumed to be spoken text
- ❌ Never nest bullets more than one level deep (bullet → tab-indented sub-bullet only)
- ❌ **Never give more than 3-5 bullets of explanation before a STOP** (too much info at once)
- ❌ **Never skip user gates between major topic changes** (always require user initiation)
- ❌ **Never use "I'm going to do X, ready? *does X*"** - instead teach the capability and have them ask
- ❌ **Never ask "What happened?" or "Describe what you see"** unless exploring (use closed questions: "Do you see the file pill?")

### Student-Driven Commands (Important!)

**BAD - Claude just does it:**
```
- I'm going to process these 10 meeting notes with agents
- STOP: Ready?
- USER: Ready
- ACTION: Launch 10 agents
```

**GOOD - Student requests it:**
```
- I can spin up 10 independent agents to process all these notes simultaneously
- Each agent will read one file and extract action items
- STOP: Ask user to say: "Process all 10 meeting notes with agents"
- USER: Process all 10 meeting notes with agents
- ACTION: Launch 10 agents
	- Agent 1 processes meeting-notes-1.md
	- Agent 2 processes meeting-notes-2.md
	- Etc.
```

**Why this matters:** Students learn by doing, not watching. They need to practice requesting the capability.

### Example Teaching Flow Structure

```markdown
## Teaching Flow

- Welcome to Module 1.4: Agents
- Prepare to be amazed - this is a game-changer
- Scenario: Monday morning, 10 meeting notes from last week need processing
- Normally this takes 2-3 hours sequentially, with agents it takes minutes in parallel
- ACTION: List files in meeting-notes/ folder
- STOP: Ask user to say "Show me the files"
- USER: Show me the files

---

- I can spin up 10 independent agents, each processing one meeting note simultaneously
- Each agent will read a file, extract action items/decisions/next steps, append summary
- STOP: Ask user to say: "Process all the meeting notes with agents"
- USER: Process all the meeting notes with agents
- ACTION: Launch 10 agents to process meeting notes
	- Each agent reads one file, extracts action items/decisions/next steps, appends summary to that file
- Done! All 10 meeting notes processed simultaneously
- STOP: Ask user to view the edited files
- USER: Viewed files

---

- Pretty cool, right? Let me explain what just happened
- STOP: Quick check question (multiple choice about when to use agents)
- USER: Answers
- Respond based on answer
- Explain what agents are
	- Agents = independent instances of Claude working simultaneously
	- Regular Claude = sequential (one thing at a time)
	- Agents = parallel (10 things at same time)
	- Like cloning itself
- STOP: Does that make sense?
- USER: Yes / needs clarification

---

- Now let's try something more advanced: competitive research
- [Continue to next demonstration...]
```

**Notice the breaks:**
- `---` separates major topic shifts (intro → demo → explanation → next topic)
- Never more than 4-5 bullets of dialogue before a STOP
- Each section ends with user gate before moving forward
- Keeps cognitive load manageable

### Formatting Notes

1. **Tabs vs Spaces:** Sub-bullets MUST use tabs, not spaces
2. **One Level Deep:** Never go deeper than bullet → sub-bullet
3. **No "Say":** Just write the dialogue naturally without "Say:" prefix
4. **No Quotes:** Don't wrap dialogue in quotes - it's assumed to be spoken
5. **Continuous Flow:** Single list from beginning to end of module
6. **Keyboard Shortcuts:** Use "Cmd/Ctrl+B" format, not "Cmd+B (or Ctrl+B on Windows)" - keeps it concise

---

## Summary

**Step 1:** Create high-level overview (files needed, files created, bullet overview)
**Step 2:** Get alignment on overview before proceeding
**Step 3:** Write detailed teaching flow using prefix standards (ACTION/STOP/USER, no "Say", tabs for sub-bullets, one level deep)
