# Module 0.2: Start Claude Code & Clone the Course

**Goal:** Have your first real interaction with Claude Code and let it set up your learning environment.

**The Big Insight:** You're about to learn by doing. Instead of manually cloning a repository or setting up folders, you'll simply tell Claude what you want—and watch it happen.

**Time:** 5 minutes

---

## What You're About to Experience

This is your first taste of the paradigm shift.

**Old way (without Claude Code):**
1. Read documentation about `git clone`
2. Find the repository URL
3. Navigate to the right directory using `cd`
4. Copy-paste the git command
5. Hope you didn't make a typo
6. Manually navigate into the folder

**New way (with Claude Code):**
1. Tell Claude what you want in plain English
2. Claude does all of it for you

Let's go.

---

## Step 1: Start Claude Code

Open your terminal and type:

```bash
claude
```

Press Enter.

**What you'll see:**

```
Welcome to Claude Code

Let's get started.

[Claude Code interface appears]
```

You're now inside Claude Code. Think of this as your AI-powered command center.

---

## Step 2: Your First Conversation

At the bottom of the screen, you'll see a text input area. This is where you talk to Claude.

**Important concept:** You're not writing commands. You're having a conversation.

---

## Step 3: Clone the Course Repository

Here's where it gets interesting. You're going to ask Claude to clone this entire course repository and set it up for you.

**Type this (or something like it in your own words):**

```
Clone the Claude Code PM course repository from
[REPOSITORY_URL] and set it up for me. Put it in a
folder called "claude-code-pm-course" in my Documents folder.
```

**Replace `[REPOSITORY_URL]` with the actual course repository URL.**

*(Note to course creator: Insert your actual GitHub repository URL here)*

Press Enter.

---

## Step 4: Watch Claude Work

Here's what happens next—and this is the "aha!" moment:

**Claude will:**
1. Understand your intent
2. Figure out where your Documents folder is
3. Navigate to that directory
4. Run the `git clone` command with the correct URL
5. Name the folder appropriately
6. Confirm success
7. Navigate into the new directory

**You'll see output like:**

```
I'll help you clone the repository and set it up.

Tool Use: bash
Command: cd ~/Documents && git clone [REPOSITORY_URL] claude-code-pm-course

[Git output showing clone progress]
Cloning into 'claude-code-pm-course'...
remote: Enumerating objects: 234, done.
remote: Counting objects: 100% (234/234), done.
remote: Compressing objects: 100% (156/156), done.
remote: Total 234 (delta 78), reused 234 (delta 78)
Receiving objects: 100% (234/234), done.
Resolving deltas: 100% (78/78), done.

Tool Use: bash
Command: cd ~/Documents/claude-code-pm-course

✓ Successfully cloned the repository to ~/Documents/claude-code-pm-course
✓ Navigated into the course directory

You're all set! The course is now available at:
/Users/[your-username]/Documents/claude-code-pm-course

Would you like me to show you the directory structure?
```

**Take a moment to appreciate what just happened:**
- You stated what you wanted
- Claude figured out the how
- Claude executed multiple commands in sequence
- Claude verified success

**This is the new way of working.**

---

## Step 5: Explore What Claude Created

Let's confirm everything worked. Ask Claude:

```
Show me the folder structure of the course.
```

**Claude will respond with something like:**

```
Tool Use: bash
Command: tree -L 2 claude-code-pm-course

claude-code-pm-course/
├── README.md
├── HIGH_LEVEL_COURSE_OVERVIEW.md
├── lesson-modules/
│   ├── 0.0-introduction/
│   ├── 0.1-installation/
│   ├── 0.2-start-and-clone/
│   ├── 1.1-welcome/
│   ├── 1.2-visualizing-files/
│   ├── 1.3-first-tasks/
│   ├── 1.4-agents/
│   └── [... more modules]
├── TaskFlow-context/
│   ├── company-overview.md
│   ├── user-personas/
│   ├── product-specs/
│   └── user-research/
└── resources/
    ├── templates/
    ├── examples/
    └── cheatsheets/

The course includes:
- 15+ interactive lesson modules
- Complete TaskFlow company context
- Ready-to-use templates
- Reference guides
```

**Success!** You've just cloned an entire course repository without typing a single git command.

---

## What Just Happened? (The Important Part)

Let's break down the magic:

### You said:
> "Clone the repository and set it up for me."

### Claude understood:
- **Intent:** You want the course materials on your computer
- **Where:** Your Documents folder
- **How:** Using git clone
- **Verification:** Navigate into the directory and confirm it worked

### Claude executed:
1. Changed directory to `~/Documents`
2. Ran `git clone [URL] claude-code-pm-course`
3. Navigated into `claude-code-pm-course`
4. Confirmed success
5. Offered to show you the structure

### You learned:
**You are now an orchestrator, not a command typist.**

---

## The Permission System (Important to Understand)

You may have noticed Claude asking for permission to run commands:

```
I'll need to run the following command:
git clone [URL]

May I proceed? (yes/no)
```

**This is a safety feature.** Claude will ask permission before:
- Running terminal commands
- Creating or modifying files
- Installing software
- Making system changes

**You can:**
- Type `yes` to approve
- Type `no` to decline
- Type `yes and don't ask again` to trust Claude for this session

**For learning purposes, it's fine to use "yes and don't ask again" in this course environment.**

---

## Common Questions

### "Do I need to understand git?"

**No.** That's the point. You stated what you wanted, Claude handled the implementation.

### "What if I don't have git installed?"

Claude will detect this and help you install it. Just follow the prompts.

### "Can I do this with other repositories?"

**Absolutely.** This same pattern works for any git repository:
- Clone your company's internal docs
- Clone open-source projects
- Clone your own projects from GitHub

Just tell Claude what you want.

### "What if something goes wrong?"

Claude will tell you what went wrong and suggest fixes. You can ask:
- "What went wrong?"
- "How do I fix this?"
- "Try again with a different approach"

---

## Try It Yourself: Navigate the Course

Now that the course is cloned, practice giving Claude instructions:

**Try these prompts:**

```
Show me all the Level 1 modules.
```

```
Open the README file and summarize what this course teaches.
```

```
What are the learning objectives for Module 1.3?
```

```
List all the TaskFlow user personas available in the context folder.
```

**Observe how Claude:**
- Interprets your request
- Finds the right files
- Reads them
- Gives you a clear answer

**This is your new workflow.**

---

## Success Criteria

You're ready for Module 1.1 when you:

✅ Successfully cloned the course repository
✅ Can see the folder structure in your Documents folder
✅ Understand the conversation model (not command-typing)
✅ Feel comfortable asking Claude to do things for you
✅ Appreciate that you just completed a technical task without knowing git

---

## The Mindset Shift

Let's revisit the insight from Module 0.0:

**Old mindset:**
> "I need to learn git commands to clone a repository."

**New mindset:**
> "I need the course materials on my computer."

**See the difference?**

You think in **outcomes**. Claude handles **execution**.

This mindset shift applies to everything you'll do in this course:

- "I need a PRD for dark mode" → Claude writes it
- "Organize my meeting notes from last week" → Claude organizes them
- "Analyze 500 customer feedback responses" → Claude analyzes them
- "Create a competitive landscape matrix" → Claude creates it

**You state the what. Claude figures out the how.**

---

## What You Just Learned

In 5 minutes, you:

1. ✅ Started Claude Code
2. ✅ Had your first conversation with AI that actually executes
3. ✅ Cloned an entire course repository without knowing git
4. ✅ Explored the course structure
5. ✅ Understood the permission system
6. ✅ Experienced the paradigm shift firsthand

**This is just the beginning.**

---

## What's Next

You're now ready to start the real course.

**Module 1.1: Welcome to TaskFlow**

In Module 1.1, you'll:
- Meet TaskFlow, your learning company (a fictional PM tool like Asana meets Linear)
- See how the interactive course works
- Learn the @-symbol for referencing files
- Complete your first real PM task with Claude Code

**Important setup note:**

Before you continue to Module 1.1, consider setting up a file visualization tool like Obsidian (covered in Module 1.2). This lets you see the files Claude creates in real-time, which makes learning much easier.

**But you don't have to.** You can jump straight to Module 1.1 and come back to visualization later.

---

## Quick Reference: What You Used

| Concept | What it means |
|---------|---------------|
| `claude` | Start Claude Code from terminal |
| Natural language instructions | Tell Claude what you want in plain English |
| Permission prompts | Claude asks before running commands (for safety) |
| "Yes and don't ask again" | Trust Claude for the current session |
| Tool Use: bash | Claude showing you what command it's running |
| Git clone | Downloading a repository (you don't need to know this!) |

---

## Pro Tips

**Tip 1: Be specific but natural**
```
❌ "git clone [URL]"  (You're thinking in commands)
✅ "Clone this repository and put it in my Documents folder"  (You're thinking in outcomes)
```

**Tip 2: Claude remembers context**
```
You: "Clone the course repository."
Claude: [Clones it]
You: "Show me the structure."  ← Claude knows you mean the course you just cloned
```

**Tip 3: You can always ask "why" or "how"**
```
You: "Why did you use that command?"
You: "How does git clone work?"
You: "What would happen if I ran this myself?"
```

**Tip 4: Experiment fearlessly**
- You're in a learning environment
- You can always re-clone the repository
- Claude will help you fix mistakes
- The worst that happens: you learn something

---

## Troubleshooting

### "Git is not installed"

**Claude will likely detect this and offer to help you install git.**

If not, you can say:
```
Help me install git.
```

Claude will guide you through the installation for your operating system.

### "Permission denied"

This usually means you need authentication for a private repository.

**Solution:**
```
Help me set up GitHub authentication.
```

Claude will walk you through it.

### "The directory already exists"

If you've already cloned the repository:

```
Delete the existing course folder and clone a fresh copy.
```

Claude will handle it.

---

## Final Thought

You just completed your first real task with Claude Code.

You didn't learn git. You didn't memorize commands. You didn't worry about syntax.

**You stated what you wanted, and it happened.**

This is how you'll work for the rest of the course—and the rest of your PM career.

**Welcome to the future of PM work.**

---

**Ready to dive in? Head to Module 1.1: Welcome to TaskFlow.**
