# Module 1.6: Project Memory - CLAUDE.md
## Reference Guide

**Last Updated:** October 13, 2025
**Time to Complete:** 20-25 minutes
**Prerequisites:** Modules 1.1-1.5 complete

---

## 📖 Overview

Every time you start a new conversation with an AI tool, you have to re-explain everything from scratch. What your product does. Who your users are. Your writing preferences. Your company's terminology. It's exhausting and wastes 5-10 minutes every single session.

**CLAUDE.md changes that forever.**

CLAUDE.md is Claude's permanent memory for your project. You write it once, and Claude knows your product context in every conversation. No re-explaining. Ever.

**Key takeaway:** CLAUDE.md is your project's constitution - immutable rules that override temporary prompts. While prompts are like legislation (flexible requests), CLAUDE.md establishes the supreme law of your project.

---

## 🏛️ What Is CLAUDE.md?

### The Core Concept

CLAUDE.md is a markdown file that lives in your project directory and contains permanent context about your product, team, and preferences. When you start a Claude Code session in that directory, Claude automatically reads this file and applies everything in it.

Think of it as Claude's onboarding document for your project.

### What Makes It Special

**Automatic loading:** You never have to say "read my CLAUDE.md" - Claude reads it at session start automatically.

**Persistent memory:** Information in CLAUDE.md carries across ALL conversations in that project directory.

**Team-shareable:** Commit CLAUDE.md to git, and your entire team gets the same product context.

**Hierarchical:** Multiple CLAUDE.md files can exist at different levels (global, project, directory).

### The Power of Permanence

Without CLAUDE.md:
```
Session 1: "Remember, we call it Workspace not Project..."
Session 2: "Remember, we call it Workspace not Project..."
Session 3: "Remember, we call it Workspace not Project..."
[Repeat forever]
```

With CLAUDE.md:
```
CLAUDE.md: "Use 'Workspace' not 'Project'"
Session 1: Claude uses "Workspace" ✓
Session 2: Claude uses "Workspace" ✓
Session 3: Claude uses "Workspace" ✓
[Works forever, automatically]
```

---

## ⚖️ The Constitution Metaphor

### CLAUDE.md = Constitution, Prompts = Legislation

This is the most important concept to understand:

**CLAUDE.md is your project's constitution** - the supreme law that cannot be overridden.

**User prompts are legislation** - flexible requests that must comply with the constitution.

### The Hierarchy in Action

**If there's a conflict, CLAUDE.md ALWAYS wins.**

**Example 1: Terminology Override**

Your CLAUDE.md says:
```markdown
Always use "Workspace" not "Project" in TaskFlow documentation.
```

You prompt Claude:
```
Write a PRD for the new Project dashboard feature
```

What Claude does:
```
Writes the PRD using "Workspace dashboard" because CLAUDE.md overrides
your casual prompt wording
```

**Example 2: Writing Style Enforcement**

Your CLAUDE.md says:
```markdown
Always use Oxford commas in all documentation.
```

You prompt Claude:
```
Write this without Oxford commas: "Features include tasks, projects and reports"
```

What Claude does:
```
"Features include tasks, projects, and reports"
(Still uses Oxford commas because CLAUDE.md is the constitution)
```

### Why This Hierarchy Matters

**Consistency:** Your core product rules don't change based on how someone phrases a prompt.

**Quality control:** Writing standards and best practices are enforced automatically.

**Onboarding:** New team members can write casual prompts and Claude still produces on-brand content.

**Trust:** You know Claude will ALWAYS follow your product's fundamental rules.

### Constitution vs Legislation Table

| Aspect | CLAUDE.md (Constitution) | User Prompts (Legislation) |
|--------|--------------------------|----------------------------|
| **Priority** | Supreme - always wins | Secondary - must comply |
| **Permanence** | Stays forever | Temporary per request |
| **Scope** | Applies to all sessions | Applies to current task |
| **Purpose** | Immutable project rules | Flexible specific requests |
| **Example** | "Always call it Workspace" | "Create a PRD for dark mode" |

---

## # The Power of the # Symbol

### Dynamic Session Rules

You can add temporary rules to your current session using the **#** symbol at the start of a line:

```
# Always use bullet points instead of numbered lists in this session
```

When you send this, Claude treats it as a rule for the rest of your conversation.

### How # Works

**The # symbol means:** "This is a rule for this conversation."

After you state a # rule, Claude will follow it for the remainder of the session, but it won't persist to future sessions.

### # vs CLAUDE.md

| Feature | # Symbol | CLAUDE.md |
|---------|----------|-----------|
| **Duration** | Current session only | Forever |
| **Scope** | This conversation | All conversations |
| **Use case** | Experimenting with preferences | Permanent project rules |
| **Location** | In chat message | In CLAUDE.md file |

### When to Use #

**Use # when you:**
- Discover a preference during work ("Oh, I want bullet points for this!")
- Want to experiment before making it permanent
- Have a temporary constraint for this session only
- Need to override CLAUDE.md for this one conversation

**Use CLAUDE.md when you:**
- Know the rule is permanent
- Want it to apply across ALL sessions
- Want your whole team to follow the same rule
- Need consistency across conversations

### Real-World Workflow

During a session:
```
# When writing user stories, always include a "User Impact" section
```

You like the results, so later you add to CLAUDE.md permanently:
```markdown
## User Story Standards

When writing user stories, ALWAYS include:
- Given/When/Then acceptance criteria
- User Impact section explaining why it matters
- Link to research or supporting data
```

Now it's enforced forever across all sessions!

---

## 📝 What to Put in CLAUDE.md

### ✅ GOOD for CLAUDE.md

#### 1. Product Context

**What your product is and does:**
```markdown
## Product Overview

TaskFlow is a project management SaaS for remote-first teams.
Think Asana meets Jira, built for async collaboration.

Stage: Series B ($20M raised, 50 employees)
Revenue: $2.5M ARR, 10,000 active users
```

**Why include this:** Claude understands your product domain and can make intelligent suggestions.

#### 2. User Personas

**Who your users are with specific details:**
```markdown
## User Personas

### Sarah - Enterprise Admin
- Role: IT Administrator at 500+ person company
- Pain points: Needs SSO, audit logs, compliance, security
- Quote: "I need to prove this meets our security standards"

### Mike - IC Engineer
- Role: Individual contributor at startup
- Pain points: Wants speed, keyboard shortcuts, GitHub integration
- Quote: "If I have to use my mouse, the tool is too slow"
```

**Why include this:** Claude can reference personas when writing PRDs, user stories, and making product decisions.

#### 3. Writing Style & Preferences

**How you want documentation to sound:**
```markdown
## Writing Style

- Use active voice (not passive)
- Use Oxford commas in all lists
- Maximum 2-sentence paragraphs for readability
- Use "we" not "I" in documentation
- Avoid jargon unless necessary, then define it inline
- Lead with key information (busy readers first)
```

**Why include this:** Consistency across all documents Claude generates.

#### 4. Product Terminology

**Specific terms your product uses:**
```markdown
## Product Terminology

ALWAYS use these terms (NEVER use alternatives):
- "Workspace" not "Project" - Our top-level container
- "Task" not "Todo" or "Issue" - Individual work items
- "Epic" not "Initiative" or "Theme" - Large multi-sprint features
- "PM" means Product Manager (not Project Manager)
- "Activation" means completing onboarding and creating first workspace
```

**Why include this:** Prevents terminology confusion and ensures brand consistency.

#### 5. Team Structure

**Who's on your team:**
```markdown
## Team Reference

- Sarah - CEO, founder, vision and fundraising
- Mike - CTO, technical architecture and engineering
- Alex - Head of Design, owns all UX and visual design
- You - Senior PM, activation & onboarding

Extended team: 20 engineers (4 teams), 3 designers, 5 GTM
```

**Why include this:** Claude knows who to reference in updates and can model communication for different audiences.

#### 6. Immutable Rules

**Rules that must ALWAYS be followed:**
```markdown
## Immutable Rules

These rules override any prompt that conflicts:

1. ALWAYS include acceptance criteria in user stories
   - Use Given/When/Then format
   - Make them specific and testable

2. NEVER write PRDs without user research references
   - Link to interviews, surveys, or support tickets
   - Include direct user quotes when possible

3. ALWAYS consider accessibility in feature specs
   - Mention keyboard navigation
   - Consider screen reader compatibility
```

**Why include this:** Non-negotiable quality standards are enforced automatically.

#### 7. Documentation Structure

**Where things live:**
```markdown
## Documentation Structure

- `/docs/prds/` - Product requirement documents
- `/docs/user-stories/` - User story backlogs
- `/research/interviews/` - User interview transcripts
- `/research/surveys/` - Survey data and analysis
- `/competitive/` - Competitive research
- `/meetings/` - Meeting notes and syncs
```

**Why include this:** Claude knows where to create files and can reference existing documents.

#### 8. Success Metrics

**What you measure:**
```markdown
## Key Metrics

- Activation Rate: % of signups who create first workspace (current: 42%)
- Time to First Workspace: Median time from signup (current: 4 mins)
- Weekly Active Users: Users active in last 7 days (current: 6,800)
- Net Revenue Retention: Including expansion (current: 115%)
```

**Why include this:** Claude can reference metrics in PRDs and frame features around impact.

### ❌ DON'T Put in CLAUDE.md

#### 1. Temporary Instructions

**BAD:**
```markdown
Today's meeting notes are in meeting-2025-10-13.txt
We're working on dark mode this sprint
The staging environment is down right now
```

**Why bad:** These change constantly. Use prompts instead.

#### 2. Frequently Changing Requirements

**BAD:**
```markdown
Current sprint goal: Implement SSO
Q4 OKR: Increase activation to 55%
This week's focus: Bug fixes
```

**Why bad:** If it changes weekly or monthly, it doesn't belong in "permanent memory."

#### 3. Specific Task Instructions

**BAD:**
```markdown
When I ask you to create a PRD, first ask me 5 clarifying questions
Always suggest 3 alternatives before implementing
End every response with "What else do you need?"
```

**Why bad:** These are personal preferences. Put them in CLAUDE.local.md instead (covered next).

#### 4. Sensitive Information

**BAD:**
```markdown
Our revenue is actually declining (don't tell the board)
We're planning layoffs next quarter
API keys: sk-proj-xxxxx
Database password: admin123
```

**Why bad:** CLAUDE.md is often committed to git and shared with teams. Keep sensitive info out.

### The Test

**If you'd want Claude to know this in 6 months, put it in CLAUDE.md.**

**If it might change next week, use prompts instead.**

---

## 🏗️ CLAUDE.md Hierarchy

### Four Levels of CLAUDE.md Files

You can have multiple CLAUDE.md files at different locations:

```
~/.claude/CLAUDE.md              # 1. Global (all your projects)
/project-root/CLAUDE.md          # 2. Project-specific
/project-root/frontend/CLAUDE.md # 3. Directory-specific
/project-root/CLAUDE.local.md    # 4. Personal (gitignored)
```

### Priority Order (What Wins)

**Most specific wins:**

1. **Directory-level** (e.g., `/frontend/CLAUDE.md`)
2. **Project-level** (e.g., `/project-root/CLAUDE.md`)
3. **Global** (e.g., `~/.claude/CLAUDE.md`)
4. **User prompts** (least priority)

### How They Stack

The levels **combine** (they don't replace each other). Rules from all levels apply simultaneously, with more specific levels overriding less specific ones when there's a conflict.

**Example Scenario:**

**Global CLAUDE.md** (`~/.claude/CLAUDE.md`):
```markdown
# My universal preferences
Always use active voice in writing
Use Oxford commas
```

**Project CLAUDE.md** (`/taskflow/CLAUDE.md`):
```markdown
# TaskFlow-specific rules
Use "Workspace" not "Project"
All user stories need acceptance criteria
Reference personas: Sarah, Mike, or Alex
```

**Frontend Directory CLAUDE.md** (`/taskflow/frontend/CLAUDE.md`):
```markdown
# Frontend-specific rules
When discussing frontend, always consider mobile responsiveness
Mention accessibility requirements
```

**What happens when working in `/taskflow/frontend/`:**

Claude follows ALL THREE layers:
- Active voice and Oxford commas (global)
- "Workspace" terminology and persona references (project)
- Mobile responsiveness and accessibility (directory)

### When to Use Each Level

#### Global (~/.claude/CLAUDE.md)

**Use for:** Personal preferences that apply to ALL your work

**Examples:**
```markdown
# Global preferences
I prefer brief summaries, maximum 3 bullet points
When generating documentation, ask clarifying questions first
Use TODO tags when something needs my input
```

#### Project (/project-root/CLAUDE.md)

**Use for:** Product-specific context that everyone on the team needs

**Examples:**
```markdown
# TaskFlow project
Product overview and positioning
User personas
Writing style and terminology
Team structure and tools
```

#### Directory (/project-root/subfolder/CLAUDE.md)

**Use for:** Rules specific to a subsection of your project

**Examples:**
```markdown
# Frontend-specific rules
Consider mobile breakpoints in all features
Reference design system components
Mention loading states and error handling

# Backend-specific rules
Include database migration notes
Consider API rate limiting
Document authentication requirements
```

#### Personal (CLAUDE.local.md)

**Use for:** Your own preferences that you DON'T want to share with team

**Examples:**
```markdown
# My personal preferences (not shared with team)
I prefer brief responses unless I ask for detail
Always format PRDs in a specific template I use
When creating meeting notes, tag action items with @name
```

**Important:** Add `CLAUDE.local.md` to your `.gitignore` so it stays personal:
```
# .gitignore
CLAUDE.local.md
```

---

## 🚀 Creating Your First CLAUDE.md

### Step-by-Step Guide

#### Step 1: Start with Product Context

Open a new file called `CLAUDE.md` in your project root and start with basics:

```markdown
# [Your Product Name] Product Context

This file provides permanent context about [Product] for Claude Code.

---

## What [Product] Is

[Product] is a [type of product] for [target users]. Think [comparison].

**Company Details:**
- Founded: [year]
- Stage: [stage and funding]
- Team: [size]
- Revenue: [ARR and users]
```

#### Step 2: Add User Personas

```markdown
## User Personas

### [Persona 1 Name] - [Role]
- Role: [job title and context]
- Pain points: [what frustrates them]
- Priorities: [what matters most]
- Quote: "[memorable quote]"

[Repeat for other personas]
```

#### Step 3: Define Writing Style

```markdown
## Writing Style & Standards

- Voice: [active/passive, formal/casual]
- Paragraph length: [preference]
- Tone: [how should it sound]
- Formatting: [lists, headers, etc.]
```

#### Step 4: Set Product Terminology

```markdown
## Product Terminology

ALWAYS use these terms (NEVER use alternatives):
- "[Term]" not "[alternative]" - [why]
- "[Term]" not "[alternative]" - [why]
```

#### Step 5: Add Immutable Rules

```markdown
## Immutable Rules

These rules override any prompt that conflicts:

1. ALWAYS [rule]
   - [details]

2. NEVER [rule]
   - [details]
```

#### Step 6: Include Team Context

```markdown
## Team Reference

- [Name] - [Role], [focus area]
- [Name] - [Role], [focus area]
```

#### Step 7: Document Structure (Optional)

```markdown
## Documentation Structure

- `/path/` - [what lives here]
- `/path/` - [what lives here]
```

### Complete Example: TaskFlow CLAUDE.md

Here's the real CLAUDE.md created for the TaskFlow course (see `EXAMPLE_TASKFLOW_CLAUDE.md` in this module directory for the full version):

```markdown
# TaskFlow Product Context

This file provides permanent context about TaskFlow for Claude Code.

---

## What TaskFlow Is

TaskFlow is a project management SaaS for remote-first teams. Think Asana
meets Jira, but built specifically for async collaboration.

**Company Details:**
- Founded: 2021
- Stage: Series B ($20M raised)
- Team: 50 employees
- Revenue: $2.5M ARR
- Users: 10,000 active users, growing fast

**Your Role:**
- Position: Senior Product Manager
- Focus: Activation & Onboarding
- Reporting: To Sarah (CEO)

---

## User Personas

### Sarah - Enterprise Admin
- Role: IT Administrator at 500+ person company
- Pain points: Needs security, SSO, audit logs, compliance
- Quote: "I need to prove to leadership that TaskFlow meets our
security standards"

### Mike - IC Engineer
- Role: Individual contributor software engineer at startup
- Pain points: Wants speed, keyboard shortcuts, GitHub integration
- Quote: "If I have to use my mouse, the tool is too slow"

### Alex - Team Lead
- Role: Engineering manager of 8-person team
- Pain points: Needs team visibility, workload balance, reporting
- Quote: "I need to see who's overloaded before they burn out"

---

## Writing Style & Standards

- Use active voice (not passive)
- Use Oxford commas in all lists
- Maximum 2-sentence paragraphs for readability
- Use "we" not "I" in documentation
- Avoid jargon unless necessary, then define it inline

---

## Product Terminology

ALWAYS use these terms consistently:
- "Workspace" not "Project" - Our top-level container
- "Task" not "Todo" or "Issue" - Individual work items
- "Epic" not "Initiative" - Large multi-sprint features
- "PM" means Product Manager (not Project Manager)

---

## Immutable Rules

1. ALWAYS include acceptance criteria in user stories
   - Use Given/When/Then format
   - Make them specific and testable

2. NEVER write PRDs without user research references
   - Link to interviews, surveys, or support tickets
   - Include direct user quotes when possible

3. ALWAYS consider accessibility in feature specs
   - Mention keyboard navigation
   - Consider screen reader compatibility

---

## Team Reference

- Sarah - CEO, founder, focus on vision and fundraising
- Mike - CTO, technical architecture and engineering
- Alex - Head of Design, owns all UX and visual design
- You - Senior PM, activation & onboarding
```

---

## 💼 Real-World Examples

### PM CLAUDE.md for TaskFlow

See `EXAMPLE_TASKFLOW_CLAUDE.md` in this module directory for the complete example created during the course. It demonstrates:

- Comprehensive product context
- Detailed user personas
- Writing style enforcement
- Product terminology standards
- Immutable quality rules
- Team reference information

### Other Product Types

#### Early-Stage Startup

```markdown
# [Startup Name] - Pre-Product Market Fit

## Current Stage
- Pre-seed, bootstrapped
- 3 person team (2 eng, 1 PM/founder)
- Building MVP for [market]

## Target User (Hypothesis)
[Description - we're still validating!]

## Experiment Tracking
Document all experiments in /experiments/ with:
- Hypothesis
- Method
- Results
- Learning
```

**Why different:** Emphasizes experimentation and acknowledges uncertainty.

#### Enterprise Product

```markdown
# [Product] - Enterprise SaaS

## Compliance Requirements
ALWAYS consider in feature specs:
- SOC 2 compliance
- GDPR data handling
- HIPAA requirements (healthcare customers)

## Enterprise Personas
Focus on economic buyer vs. end user distinction

## Sales Engineering Context
[Enterprise context that PMs need to know]
```

**Why different:** Emphasizes compliance, enterprise complexity, buying committees.

#### Developer Tools

```markdown
# [Tool] - Developer Platform

## Target Users
- Backend engineers (primary)
- DevOps engineers (secondary)

## Technical Depth
- Assume users are technical
- Code examples required in all docs
- CLI-first, UI-second approach

## Integration Ecosystem
[List of tools your product integrates with]
```

**Why different:** More technical, assumes engineering audience.

---

## 🎯 Best Practices

### Writing Style

**Be specific, not vague:**

❌ **Bad:**
```markdown
Users like simple interfaces
```

✅ **Good:**
```markdown
User research (8/10 interviews, June 2025) showed users abandon features
with more than 3 required fields. Keep forms minimal.
```

**Use imperative language for rules:**

❌ **Bad:**
```markdown
It would be nice if user stories had acceptance criteria
```

✅ **Good:**
```markdown
ALWAYS include acceptance criteria in user stories
```

**Provide context for why:**

❌ **Bad:**
```markdown
Use "Workspace" not "Project"
```

✅ **Good:**
```markdown
Use "Workspace" not "Project" - We differentiate from traditional project
management tools. "Workspace" signals collaboration space.
```

### Organization

**Use clear headers:**
```markdown
## Product Context
## User Personas
## Writing Style
## Terminology
## Immutable Rules
```

**Group related information:**
```markdown
## Tools We Use

**Development:**
- GitHub for code
- Linear for engineering tasks

**Product:**
- Figma for design
- Amplitude for analytics
```

**Keep it scannable:**
- Use bullet points liberally
- Short paragraphs (1-2 sentences)
- Bold key terms
- Add spacing between sections

### Maintenance

**Review quarterly:**
- Are personas still accurate?
- Has terminology evolved?
- Do metrics need updating?
- Are rules still relevant?

**Version control:**
- Commit CLAUDE.md to git
- Document major changes in commit messages
- Review changes in PRs (important context updates)

**Team alignment:**
- Share when CLAUDE.md is created/updated
- Get feedback from team members
- Ensure everyone agrees on terminology and rules

**Keep it current:**
```markdown
## Notes

- This CLAUDE.md reflects TaskFlow as of Q2 2025
- Update strategic focus quarterly
- Personas based on research (see /research/personas/)
- Metrics updated monthly
```

---

## 🔧 Troubleshooting

### Problem: Rules Are Being Ignored

**Symptom:** Claude doesn't follow a rule in CLAUDE.md

**Possible causes:**

1. **Conflicting rules across hierarchy levels**
   - Check if a more specific CLAUDE.md contradicts the rule
   - Directory > Project > Global (most specific wins)

2. **Rule is too vague**
   - ❌ "Keep things simple"
   - ✅ "Limit forms to maximum 3 required fields"

3. **Rule conflicts with itself**
   - Example: "Use active voice" and "Use passive voice" in same file
   - Remove contradiction

**Solution:**
- Make rules explicit and specific
- Use ALWAYS/NEVER for non-negotiable rules
- Check for conflicts across hierarchy

### Problem: CLAUDE.md Not Loading

**Symptom:** Claude doesn't seem to know project context

**Possible causes:**

1. **Wrong file location**
   - Must be named exactly `CLAUDE.md` (case-sensitive on some systems)
   - Must be in project root or directory where you run `claude`

2. **File permissions**
   - Make sure Claude Code can read the file
   - Check: `ls -la CLAUDE.md` (should show read permissions)

3. **Syntax errors**
   - CLAUDE.md should be valid markdown
   - No broken formatting that prevents parsing

**Solution:**
- Verify file exists: `ls CLAUDE.md`
- Verify location: `pwd` to check current directory
- Test: Start new session and ask "What does my CLAUDE.md say?"

### Problem: Too Many CLAUDE.md Files

**Symptom:** Unclear which rules apply, confusion about precedence

**Possible causes:**
- CLAUDE.md files scattered throughout project
- Rules conflict across different levels
- Team members created their own without coordination

**Solution:**
- Audit all CLAUDE.md files: `find . -name "CLAUDE.md"`
- Document the hierarchy (add to README)
- Consolidate when possible
- Use CLAUDE.local.md for personal preferences

### Problem: CLAUDE.md Is Too Long

**Symptom:** File is hundreds of lines, hard to maintain

**Possible causes:**
- Including too much detail
- Mixing permanent and temporary information
- Not removing outdated sections

**Solution:**
- Aim for 50-200 lines (sweet spot)
- Move detailed context to separate reference docs
- Link to those docs from CLAUDE.md
- Remove or archive outdated information

**Example refactor:**
```markdown
## User Personas

For detailed persona information, see `/docs/personas/`.

Quick reference:
- Sarah: Enterprise Admin, needs security/compliance
- Mike: IC Engineer, needs speed/integrations
- Alex: Team Lead, needs visibility/reporting
```

---

## 📚 Community Resources

### Official Documentation

**Claude Code Documentation:**
- Project memory: [Link to official docs when available]
- Slash commands and CLAUDE.md interaction
- Hierarchy and precedence rules

### CLAUDE.md Templates

**Starter Templates:**

1. **Basic Product Template**
```markdown
# [Product] Context

## What [Product] Is
[Description]

## User Personas
[Personas]

## Writing Style
[Preferences]

## Terminology
[Key terms]
```

2. **PM-Specific Template**
```markdown
# [Product] PM Context

## Product Overview
## User Personas
## Writing Style & Standards
## Product Terminology
## Documentation Structure
## Immutable Rules
## Success Metrics
## Team Reference
```

3. **Enterprise Product Template**
```markdown
# [Product] Enterprise Context

## Product Overview
## Enterprise Personas (Economic Buyer vs End User)
## Compliance Requirements
## Security Standards
## Procurement Process Context
## Enterprise Writing Style
```

### Example Projects Using CLAUDE.md

**Public repositories:**
- [Coming soon: As community adopts, examples will be shared]

**Where to find examples:**
- GitHub search: `filename:CLAUDE.md`
- Community forums
- Claude Code examples repository

### Community Forums

**Where to discuss:**
- Claude Code Discord/Slack (when available)
- Product management communities using Claude Code
- GitHub discussions on Claude Code repos

**Topics:**
- Share your CLAUDE.md structure
- Get feedback on rules
- Discuss hierarchy strategies
- Troubleshoot issues

---

## 🎉 Module 1.6 Complete!

### You Did It!

Congratulations! You've completed Module 1.6: Project Memory!

CLAUDE.md is one of the most powerful features you'll use. Permanent project memory means never having to re-explain your product context, personas, or writing style.

### What You've Mastered So Far

**Module 1.1: Welcome to TaskFlow**
- Met TaskFlow and understood the course structure
- Got comfortable with Claude Code basics

**Module 1.2: Visualizing Files**
- Set up Obsidian for visual file management
- Created split-screen workflow

**Module 1.3: Your First PM Tasks**
- Processed real PM documents
- Learned file operations

**Module 1.4: Agents - Clone Yourself**
- Discovered parallel agent orchestration
- Saved hours with simultaneous work

**Module 1.5: Custom Sub-Agents**
- Created specialized AI team members
- Built reusable personas

**Module 1.6: Project Memory** (This Module!)
- Understood CLAUDE.md as project constitution
- Created permanent product memory
- Mastered the # symbol and hierarchy

### What You Can Do Now

With Module 1.6 complete, you can:

✅ **Work with files** - Read, write, edit, and reference documents

✅ **Visualize your work** - See everything in Obsidian in real-time

✅ **Process PM documents** - Meeting notes, research, feedback

✅ **Clone yourself** - Use agents for parallel work

✅ **Build a team** - Create specialized sub-agents

✅ **Make Claude remember** - Set permanent project context with CLAUDE.md

**These skills alone will save you 5-10 hours per week.**

---

## 🚀 What's Next: Module 1.7 - Planning Mode

One more module to complete Level 1: Foundation!

### Module 1.7: Final Navigation Skills
- Master the three input modes (edit, auto-accept, plan)
- Use planning mode for complex multi-step workflows
- Learn think control keywords (think/think harder/ultrathink)
- Understand --dangerously-skip-permissions workflow acceleration
- Complete Level 1: Foundation with full navigation mastery!

### Then: Level 2 - Practitioner

After Module 1.7, you'll move to Level 2 which teaches daily PM workflows:

### Module 2.1: Write a PRD
- Transform rough ideas into complete PRDs
- Use research agents and Socratic refinement
- Generate production-ready documentation

### Module 2.2: Analyze Product Data & Build Dashboards
- Handle large datasets (CSV files, surveys)
- Multi-source research synthesis
- Create visual dashboards

### Module 2.3: Build Product Strategy & Roadmap
- Competitive research at scale
- Strategic synthesis and SWOT analysis
- 6-month roadmap creation

### Module 2.4: Understand a Technical Codebase
- Explore codebases as a non-technical PM
- Generate technical glossaries
- Review PRs from PM perspective

### Module 2.5: Create PM Artifacts
- Transform PRDs into exec summaries
- Generate release notes for multiple audiences
- Create meeting prep packages

---

## 🎯 Before Starting Module 1.7

### Recommended Actions

**1. Try CLAUDE.md in your real work:**
- Create a CLAUDE.md for your actual product
- Include product context, personas, writing style
- Experience the magic of permanent memory

**2. Review what you've learned:**
- Look at files created in lesson-modules/
- Read through the TaskFlow CLAUDE.md example
- Review your custom sub-agents

**3. Take a quick break!**
You've learned a lot. Let it sink in before the final Level 1 module.

### When You're Ready

To start Module 1.7 (final module in Level 1):
```
/start-1-7
```

---

## ❓ Common Questions

### "Do I have to create CLAUDE.md for every project?"

No! You can start with a global CLAUDE.md (`~/.claude/CLAUDE.md`) with your general preferences. Then add project-specific ones when helpful. Many people use Claude Code without any CLAUDE.md files - it just makes it more powerful when you have consistent projects.

### "What if I put the wrong thing in CLAUDE.md?"

Just edit it! CLAUDE.md is a regular markdown file. Open it in your editor, change whatever you want, and save. Changes apply to new sessions. Think of it like updating a constitution - you can amend it anytime.

### "Will CLAUDE.md slow down Claude?"

Not noticeably! Claude reads CLAUDE.md at session start, but it's typically 50-200 lines - takes milliseconds. The benefit of having context far outweighs any minimal load time.

### "Can I share CLAUDE.md with my team?"

Yes! That's the point of putting it in your project root. When you commit it to git, your whole team gets the same product context and rules. For personal preferences, use CLAUDE.local.md instead (gitignored).

### "How is this different from custom instructions in ChatGPT?"

Three key differences:

1. **Hierarchy** - CLAUDE.md OVERRIDES prompts (not just suggestions)
2. **Project-specific** - Different CLAUDE.md per project, not just global
3. **Team shareable** - Commit to git, whole team uses same rules

### "What happens if CLAUDE.md conflicts with itself?"

The most specific rule wins. Directory > Project > Global. Within a file, later rules override earlier ones. But try to avoid conflicts - keep rules clear and non-overlapping.

### "Should I commit CLAUDE.md to git?"

**Project CLAUDE.md:** Yes! Share with team.

**CLAUDE.local.md:** No! Add to .gitignore (personal preferences).

**Global CLAUDE.md:** Not in project repo (lives in `~/.claude/`).

---

## ✨ Final Thoughts

You started Module 1.1 with zero knowledge of Claude Code.

Now you have:
- File operation mastery
- Visual workspace setup
- Agent orchestration skills
- Custom sub-agent team members
- **Permanent project memory with CLAUDE.md**

**That's HUGE progress!**

Level 1 gives you the foundation to use Claude Code daily. Level 2 will make you a practitioner who automates real PM workflows and saves 20+ hours per week.

**Celebrate this achievement!** You've earned it.

When you're ready to continue your journey to becoming a Claude Code master, Level 2 awaits.

---

**Next Module:** [Module 1.7: Final Navigation Skills →](../1.7-planning-mode/REFERENCE_GUIDE.md)

Or in Claude Code:
```
/start-1-7
```

**One more module to complete Level 1: Foundation!** 🎓
