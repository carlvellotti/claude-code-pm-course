# Module 1.4 Simple Flow Outline

## Starting Files (Must Exist)
- `meeting-notes/meeting-notes-1.md` through `meeting-notes-10.md` (10 messy meeting notes)
- `competitor-research/competitor-asana.md` through `competitor-jira.md` (5 competitor briefs)
- `mobile-research/user-interviews/interview-01.md` through `interview-05.md` (5 user interviews about mobile needs)
- `mobile-research/survey-results.csv` (survey data from 200 users about mobile)
- `mobile-research/support-tickets/ticket-01.md` through `ticket-10.md` (10 support tickets requesting mobile)
- `mobile-research/sales-notes.md` (sales team notes about lost deals due to no mobile app)

---

## Introduction

### Setup
- Welcome to Module 1.4: Agents
- This is the game-changer module
- Scenario: Monday morning, 10 meeting notes from last week need processing
- Normally = 2-3 hours sequentially, with agents = minutes in parallel
- **STOP:** Ask use if they are ready
- **USER INPUT:** Confirms

### Show the Problem
- Run `ls meeting-notes/`
- List the 10 files
- Say "10 files, each needs processing - normally you'd do one by one, but agents allows parallel processing"
- **STOP:** "Say 'Show me agents!' when ready"
- **USER INPUT:** "Show me agents"

## The Big Reveal: Agents in Action

### Demonstrate Agents
- Say "I'm going to spin up 10 independent agents, each processing one meeting note simultaneously"
- Say "Watch what happens - multiple agents working concurrently"
- Launch 10 agents to process meeting notes meaning they organize them and append summaries including action items & owners
- Say done
- **STOP:** Go view the files
- **USER INPUT:** I viewed the files
- **STOP:** "Say 'Explain agents to me'"
- **USER INPUT:** "Explain agents to me"

---

## Decision Point: When to Use Agents

### Quick Check
- Ask: "Which scenario benefits most from agents?"
  - A) Writing a single PRD
  - B) Analyzing 15 user interview transcripts
  - C) Editing one sentence
  - D) Having a strategy conversation
- **STOP:** Wait for answer
- **USER INPUT:** [A/B/C/D or "skip"]
- Respond based on answer:
  - If B: "Exactly! 15 similar tasks in parallel = perfect for agents!"
  - If not B: "Actually B - 15 interviews. Multiple similar independent tasks = agents. Single tasks = regular Claude."
  - If skip: "Answer is B - 15 interviews. Agents excel at parallel batch work!"

---

## What Are Agents? (The "Aha!" Moment)

### Explanation
- Say "Agents = independent instances of Claude working simultaneously"
- Regular Claude = sequential (one thing at a time)
- Agents = parallel (10 things at same time)
- Like cloning yourself
- Agents are NOT specialized tools - they're complete Claude instances

### When to Use Agents
- Perfect scenarios:
  - Batch processing (10 meeting notes → 10 agents)
  - Multi-source research (5 competitors → 5 agents)
  - Different data sources (interviews + surveys + tickets + notes → 4 agents)
- When NOT to use:
  - Single tasks
  - Sequential work (Task 2 depends on Task 1)
  - Simple quick tasks
- **STOP:** "Say 'Show me competitive research'"
- **USER INPUT:** "Show me competitive research"

---

## Competitive Research with Agents

### Setup
- Scenario: CEO wants competitive landscape update
- Have 5 competitor briefs to analyze
- Run `ls competitor-research/`
- List 5 files
- **STOP:** Ask user if ready
- **USER INPUT:** Ready

### Demonstrate
- Say "Analyzing all 5 would take 60+ minutes manually"
- Mention that while we haven't covered it Claude Code can search the web
- Launch 5 agents, each analyzing one competitor
- Put all into a single file
- **CREATED FILE:** `competitive-landscape-matrix.md` (feature comparison, pricing, positioning, gaps)
- Say done, show insights and point ot file
- **STOP:** "Say 'Show me multi-source research'"
- **USER INPUT:** "Show me multi-source research"

---

## Advanced Agent Orchestration

### Setup
- Scenario: Researching whether to add mobile app
- 4 different data sources (different formats, different insights):
  - User interviews (5 transcripts in `mobile-research/user-interviews/`)
  - Survey data (CSV with 50 responses in `mobile-research/survey-results.csv`)
  - Support tickets (10 tickets in `mobile-research/support-tickets/`)
  - Sales notes (lost deals in `mobile-research/sales-notes.md`)
- Key difference: Not just parallel processing - SPECIALIZED agents for different data types
- **STOP:** Ask user to check out files and let you know when ready if ready
- **USER INPUT:** Ready

### Demonstrate Specialized Agents
- Say "Instead of 4 identical processes, we're launching 4 SPECIALIZED agents. That means...."
- Say "Each agent has different expertise for their data type"
- Launch 4 specialized agents:
  - **Agent 1: Interview Analyst** - Reads all 5 files in `user-interviews/`, extracts mobile pain points and quotes
  - **Agent 2: Survey Analyst** - Analyzes `survey-results.csv`, calculates percentages and segments by user role
  - **Agent 3: Support Analyst** - Reviews all 10 files in `support-tickets/`, categorizes mobile requests by use case
  - **Agent 4: Sales Analyst** - Reads `sales-notes.md`, identifies lost deals and revenue impact
- Say "All 4 working simultaneously on different tasks"
- Create synthesis combining all 4 sources
- **CREATED FILE:** `mobile-app-research-synthesis.md` (comprehensive analysis with pain points, demand data, use cases, revenue impact, recommendation)
- Say done, show key insights from synthesis
- Point out: "This is advanced orchestration - different agents, different specializations, unified output"
- **STOP:** Ready for the recap
- **USER INPUT:** Ready

---

## Agent Workflows - Repeatable Patterns

### Explain Workflows
- Workflows = repeatable patterns for common PM tasks
- Workflow 1: Weekly Meeting Processing
- Workflow 2: Sprint User Story Creation
- Workflow 3: Multi-Channel User Research
- Workflow 4: Competitive Intelligence

### How to Think About Agents
- Question 1: Can this be broken into independent parallel tasks?
- Question 2: How many independent tasks? (That's how many agents)
- Question 3: Are tasks similar or different? (Generic vs specialized agents)
- Question 4: Will outputs need combining? (Plan synthesis step)
- **STOP:** "Say 'What's next?'"
- **USER INPUT:** "What's next?"

---

## Agents vs Custom Sub-Agents (Preview) + Wrap-Up

### Recap
- Module 1.4 complete!
- You understand:
  - What agents are (independent parallel Claude instances)
  - Power of parallel processing (10x speed)
  - When to use agents (batch work, multi-source research)
  - Agent orchestration (specialized agents with different focuses)
  - Agent workflows (repeatable patterns)
  - The aha! moment (way more powerful than chatbot)

### Distinction: Agents vs Custom Sub-Agents
- Agents (Module 1.4):
  - Ad-hoc, created on the fly
  - Temporary, for immediate parallel work
  - Generic capabilities
- Custom Sub-Agents (Module 1.5):
  - Pre-configured personas you create once
  - Permanent team members
  - Call them by name
- Think: Agents = temp contractors, Sub-Agents = permanent employees

### Preview Module 1.5
- Build your dream PM team
- Specialized personas with colors and emojis
- Engineer, Executive, User Researcher, etc.
- **STOP:** "When ready: /start-1-5"

---

## Files Created During Module
1. Meeting notes edited in place (summaries appended to each of the 10 files)
2. `competitive-landscape-matrix.md` (5 competitor analysis synthesized)
3. `mobile-app-research-synthesis.md` (4-source research synthesis)
