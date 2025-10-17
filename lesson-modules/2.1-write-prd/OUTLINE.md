# Module 2.1: Write a PRD - Ultra Simple Outline

## Files Needed to Start
- `taskflow-company-context.md` (fictional company background - TaskFlow productivity app)
- `user-research/pain-points.md` (user research insights about productivity pain points)
- `methods/socratic-questioning.md` (framework for sharpening feature thinking through questions)
- `Carl's PRD Template.md` (Carl's detailed PRD structure)
- `Lenny's PRD Template.md` (Lenny Rachitsky's minimal PRD structure)
- `.claude/agents/engineer.md`, `executive.md`, `user-researcher.md` (sub-agents for review)

## Files Created During Module
- `ai-chat-todo-prd-v1.md` (first draft option)
- `ai-chat-todo-prd-v2.md` (second draft option)
- `ai-chat-todo-prd-v3.md` (third draft option)
- `ai-chat-todo-prd-review.md` (consolidated sub-agent feedback)
- `ai-chat-todo-prd-final.md` (production-ready PRD after addressing feedback)

## High-Level Overview
- Intro: This module covers how to create a PRD using your own templates, research to inform decisions, AI to question and refine your thinking, and agents to review from multiple angles
- AI should be a PARTNER in writing and not do all the work for you. The amazing thing about Claude Code is that it can help you and easily get FULL CONTEXT into anything
- Review the two PRD templates (`Carl's PRD Template.md` and `Lenny's PRD Template.md`) - explain what each one is good for (Carl's is detailed with problem/solution alignment, Lenny's is minimal and question-based)
- Ask user which template they want to use, or if they want to add their own
- If user wants to add their own, tell them they can paste it in and you'll save it as a new template file - they don't need to worry about formatting, you will handle that
- Now we're ready to start – here's what you'll need to do to kick this off:
- Scenario: User is PM at TaskFlow (provided in `taskflow-company-context.md`), feature is AI chat + to-do lists. We also provide user research in `user-research/pain-points.md`. User @ mentions method (@`methods/socratic-questioning.md`) and template (@ `Carl's PRD Template.md` or `Lenny's PRD Template.md`)
- Use `methods/socratic-questioning.md` framework to refine rough feature idea through targeted questions. Tell the user this is just for practice – they can answer the questions or say skip and you'll fill them in. In real life of course they would want to actually do this.
- Mention we've also provided user research in `user-research/pain-points.md` - they can @ it to incorporate existing pain points into the PRD
- Once ready, tell user one good tip is having you create multiple versions of a document with different approaches and they can choose the best one
- Generate 3 draft PRDs (`v1.md`, `v2.md`, `v3.md`) using template and conversation, each with a different strategic approach
- Ask user to confirm which one they think is the best
- Show off review feature using sub-agents in `.claude/agents/` (refer them to Module 1.4 if they want to go back and review agents). Quick overview of three sub-agents for multi-angle review: Engineer, Executive, User Researcher
- User asks for reviews from all three put into a new doc
- Consolidate feedback into `ai-chat-todo-prd-review.md`
- Ask user to review the feedback and say you could help them address any feedback they want to incorporate
- Wrap up by reviewing how AI can be an excellent partner in this way (questioning assumptions, incorporating existing data, generating multiple drafts). Highlight a few things not shown in this flow like helping with competitive research, synthesizing user interviews, analyzing product analytics, or drafting specific sections on demand

---

## Teaching Flow

- Welcome to Module 2.1: Write a PRD
- This module is about partnering with AI to write better product docs
- AI shouldn't write everything for you, but it can help you think through problems, generate options, and get feedback
- The amazing thing about Claude Code is getting FULL CONTEXT into your work - company docs, research, templates, all at once
- STOP: Ready to see how this works?
- USER: Yes / Ready

---

- Let me show you the two PRD templates we'll work with today
- ACTION: Display `Carl's PRD Template.md` structure (just the section headers)
- This is Carl's template - it's detailed with sections for Problem Alignment and Solution Alignment
- Good for complex features where you need to align stakeholders on why and how
- ACTION: Display `Lenny's PRD Template.md` structure
- This is Lenny Rachitsky's template - super minimal, just 7 questions
- Good for smaller features or early-stage thinking where you want to move fast
- STOP: Which template feels right for your work style? Or do you have your own template you'd like to use?
- USER: Chooses Carl's / Lenny's / wants to add their own

---

- [If user wants to add their own]
- Great, just paste your template and I'll save it
- Don't worry about formatting - I'll handle that
- STOP: Waiting for user to paste template
- USER: Pastes template
- ACTION: Save user's template to a new file `[User's Template Name].md`
- Perfect, saved your template
- [Continue to next section]

---

- [If user chose existing template]
- Excellent choice
- For this exercise, you're the PM at TaskFlow, a productivity app company
- ACTION: Display brief intro from `taskflow-company-context.md` (2-3 key facts about the company)
- I've provided the full company context in `taskflow-company-context.md` so I have all the background
- I've also provided user research insights in `user-research/pain-points.md` that you can incorporate
- Now here's how we'll kick this off
- You'll @ mention two files:
	- The `methods/socratic-questioning.md` file (the framework I'll use to help sharpen your thinking)
	- Your chosen template file
- Plus tell me your rough feature idea for TaskFlow
- For this practice scenario, the feature is: an AI voice chat interface for managing your to-do list
- STOP: Go ahead and @ mention the company context, the socratic method file, and your chosen template, and tell me the basic feature idea (ai voice chat with to-do list)
- USER: @ mentions method file and template file, confirms feature idea

---

- ACTION: Read `taskflow-company-context.md`, `methods/socratic-questioning.md`, and the chosen template
- Got it, I've read your company context, the Socratic method framework, and the template
- Now let's refine your feature idea through some targeted questions
- This is just for practice - you can answer each question or say "skip" and I'll fill in reasonable answers
- In real life you'd definitely want to think through these yourself
- STOP: Ready for the questions?
- USER: Yes

---

- ACTION: Read `methods/socratic-questioning.md` and ask first question from framework
- STOP: Waiting for user answer
- USER: Answers or says skip
- [If skip] No problem, here's what I'd suggest based on your company context: [fill in answer]
- ACTION: Ask next question from framework
- STOP: Waiting for user answer
- USER: Answers or says skip
- [Repeat for 3-5 key questions from the Socratic framework]

---

- Great, your thinking is getting sharper
- Remember I mentioned we have user research in `user-research/pain-points.md`?
- This has insights from user interviews about productivity pain points
- Would you like me to @ that file and weave those insights into the PRD?
- STOP: Do you want me to include the user research?
- USER: Yes / No

---

- [If yes]
- ACTION: Read `user-research/pain-points.md`
- Perfect, I've got the user pain points - I'll incorporate these into the PRD
- [Continue to next section]

---

- [If no]
- No problem, we have enough to work with from the company context and our conversation
- [Continue to next section]

---

- Alright, here's a pro tip
- Instead of me writing just one PRD and hoping it's right, I can generate 3 different versions for you
- Each one will use your template but take a different strategic approach
- Then you can pick the one that resonates most, or even mix and match ideas
- For your AI chat + todo list feature, I could do:
	- Version 1: Chat-first approach (AI is primary, list is secondary)
	- Version 2: List-first approach (traditional todo list enhanced with AI)
	- Version 3: Balanced approach (equal weight to both experiences)
- STOP: Sound good? Ask me to "Generate 3 PRD drafts"
- USER: Generate 3 PRD drafts

---

- ACTION: Generate `ai-chat-todo-prd-v1.md` using template with chat-first approach
- ACTION: Generate `ai-chat-todo-prd-v2.md` using template with list-first approach
- ACTION: Generate `ai-chat-todo-prd-v3.md` using template with balanced approach
- Done! I've created three versions
- ACTION: Display brief summary of each version's strategic approach
- Each one follows your template structure but frames the feature differently
- STOP: Take a look at all three - which one feels closest to your vision? Or do elements from multiple versions speak to you?
- USER: Chooses v1 / v2 / v3 / wants to combine elements

---

- [Based on user choice]
- Great choice - [briefly explain why that approach makes sense]
- Now let's get some feedback on this from different perspectives. You can start getting feedback before anyone ever sees your work.
- Remember custom sub-agents from Module 1.5? I can spin up sub-agents from `.claude/agents/` to review this from different angles
- I have three sub-agents set up:
	- Engineer: Will think about technical feasibility and implementation complexity
	- Executive: Will think about business value and strategic fit
	- User Researcher: Will think about user needs and usability
- STOP: Ask me to "Get reviews from all three agents and put them in a new doc"
- USER: Get reviews from all three agents and put them in a new doc

---

- ACTION: Launch 3 agents to review the chosen PRD version
	- Agent 1 (Engineer) reads chosen PRD and provides technical review
	- Agent 2 (Executive) reads chosen PRD and provides business review
	- Agent 3 (User Researcher) reads chosen PRD and provides UX review
- ACTION: Consolidate all feedback into `ai-chat-todo-prd-review.md`
- Done! All three agents have weighed in
- ACTION: Display summary of key themes from the reviews
- I've consolidated everything into `ai-chat-todo-prd-review.md`
- STOP: Take a look at the feedback - is there anything you'd like help addressing?
- USER: Reviews feedback / identifies areas to address / says looks good

---

- [If user wants to address feedback]
- ACTION: Work with user to update the PRD based on feedback
- ACTION: Save final version to `ai-chat-todo-prd-final.md`
- Perfect, we've incorporated the feedback
- [Continue to wrap up]

---

- [If user says looks good]
- Excellent - your PRD is in great shape
- ACTION: Save chosen version as `ai-chat-todo-prd-final.md`
- [Continue to wrap up]

---

- Let's recap what we just did
- You partnered with AI to write a PRD by:
	- Using Socratic questions to sharpen your thinking
	- Incorporating existing company context and research
	- Generating multiple strategic approaches to compare
	- Getting multi-angle feedback from specialized agents
- The key is that YOU drove the process - I didn't just write it for you
- I helped you think better and move faster
- STOP: Make sense?
- USER: Yes

---

- A few other ways I can help with PRDs that we didn't cover today:
	- Competitive research: I can web search competitors and synthesize their approaches
	- User interview synthesis: I can read dozens of interview transcripts and pull out themes
	- Product analytics analysis: I can analyze usage data to inform prioritization
	- Section-by-section drafting: You write the problem, I help with solution, we iterate
- The possibilities are endless when you have full context
- The pattern is always the same: you think, I augment, you decide
- STOP: Any questions about this workflow?
- USER: Asks questions / says no

---

- Awesome work on this module
- You now know how to partner with AI to write better PRDs faster
- Next up you'll learn how to turn these PRDs into actual implementation plans
- See you in the next module