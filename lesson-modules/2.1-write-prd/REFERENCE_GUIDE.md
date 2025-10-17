# Module 2.1: Write a PRD
## Reference Guide

**Time to Complete:** 45-60 minutes
**Prerequisites:**
- Module 1.4: Agents (understanding parallel processing)
- Module 1.5: Custom Sub-Agents (for multi-perspective feedback)

---

> **📘 About Module 2:** Module 2 takes everything you learned in Module 1 (the Claude Code fundamentals) and applies it to realistic, advanced PM scenarios. Instead of learning individual features in isolation, you'll tackle real product management challenges using multiple Claude Code capabilities together. This is where theory meets practice.

---

## 📖 Overview

This module teaches you how to partner with AI to write better Product Requirements Documents (PRDs) faster. You'll learn to use Claude Code as a thinking partner—not just a writing tool—by incorporating templates, company context, and user research via @-mentions, generating multiple strategic approaches, and getting multi-perspective feedback before anyone sees your work.

**Key takeaway:** AI is most valuable when it helps YOU think better, not when it does all the thinking for you. The best PRDs come from human judgment augmented by AI's ability to process full context, generate options, and provide diverse perspectives.

---

## 🎯 The AI Partnership Model for PRDs

### What Makes This Different

Traditional approach:
1. Open blank document
2. Stare at cursor
3. Write PRD alone
4. Share with team
5. Get feedback
6. Revise
7. Repeat

AI partnership approach:
1. Provide full context via @-mentions (company, research, templates)
2. Use Socratic questioning to clarify your thinking
3. Generate multiple strategic approaches in parallel
4. Compare and choose the best direction
5. Get feedback from AI sub-agents (Engineer, Executive, UX)
6. Refine before anyone sees it
7. Share stronger first draft

The difference: **You're never starting from scratch, and you've already addressed potential issues before your first review.**

---

## 🔧 The Four Core Techniques

### 1. Full Context via @-Mentions

**The problem:** Writing in isolation means missing critical context. You can't remember every detail from company docs, user research, and strategic priorities.

**The solution:** Use @-mentions to give Claude full context at once.

**What to @-mention:**
- **Company context** - Product strategy, customer insights, business metrics
- **User research** - Interview transcripts, survey results, pain points
- **Templates** - Your preferred PRD structure
- **Methods** - Frameworks like Socratic questioning to guide thinking
- **Related docs** - Previous PRDs, competitive analysis, roadmap docs

**Example prompt:**
```
Help me write a PRD for [feature] using:
@company-context.md - full context on our product and customers
@user-research/pain-points.md - insights from 20 user interviews
@prd-template.md - our standard PRD structure
@methods/socratic-questioning.md - help me think through this clearly
```

**Why this works:** Claude can now reason about your feature with all relevant information—just like a great PM would.

---

### 2. Socratic Questioning for Clarity

**The problem:** Initial feature ideas are often fuzzy. "We should add AI" or "Users want better mobile experience" aren't specific enough to build.

**The solution:** Use structured questioning to sharpen your thinking before writing.

**Key question categories:**

**Problem Clarity:**
- What specific user pain point does this solve?
- How do we know this is a real problem?
- Who experiences this problem most acutely?
- What's the cost of NOT solving this?

**Solution Validation:**
- Why is this the right solution for that problem?
- What alternatives did you consider? Why did you reject them?
- What's the simplest version that solves the core problem?
- How will users discover this feature?

**Success Criteria:**
- How will we know if this feature is successful?
- What would make you consider this a failure?
- What metric are we trying to move? By how much?
- What's the adoption target?

**Constraints & Trade-offs:**
- What are the technical constraints or risks?
- What are we NOT going to do as part of this?
- If we had half the time/resources, what would we cut?

**Strategic Fit:**
- Why is this the right feature to build RIGHT NOW?
- How does this fit into our broader product strategy?
- How does this affect our competitive position?

**Pro tip:** You don't need all questions—pick 3-5 most relevant to your feature. Quality over quantity.

---

### 3. Generate Multiple Strategic Approaches

**The problem:** The first idea is rarely the best idea. But generating alternatives is mentally taxing.

**The solution:** Have Claude generate 3 different strategic approaches to the same feature. Compare, contrast, choose the best (or combine elements).

**Example approaches for "AI voice chat + to-do list":**

**Version 1: Chat-First**
- AI conversation is primary interface
- To-do list is secondary view
- Use case: Quick capture while mobile
- Success metric: % of tasks created via voice

**Version 2: List-First**
- Traditional to-do list is primary
- AI voice is enhancement feature
- Use case: Hands-free updates to existing workflow
- Success metric: Daily active users of voice feature

**Version 3: Balanced**
- Equal weight to both experiences
- Different entry points for different scenarios
- Use case: Flexible based on context
- Success metric: User satisfaction + voice adoption

**Why this works:** Seeing multiple strategic angles helps you make better decisions. You're choosing consciously, not just going with your first instinct.

**How to request:**
```
Generate 3 different PRD versions using my template:
1. Chat-first approach
2. List-first approach
3. Balanced approach

Each should frame the problem, solution, and success differently.
```

**Using agents for parallel generation:**
This is a perfect use case for agents! You can spin up 3 parallel agents to generate all three versions simultaneously:

```
Spin up 3 agents to generate 3 PRD drafts in parallel:
- Agent 1: Chat-first approach
- Agent 2: List-first approach
- Agent 3: Balanced approach
```

This saves time and demonstrates the power of parallel processing for PM work.

---

### 4. Multi-Perspective Feedback via Sub-Agents

**The problem:** You want feedback from engineering, leadership, and UX—but they're not available (or you're not ready to share yet).

**The solution:** Use custom sub-agents to get feedback from different perspectives before sharing with your actual team.

**Three key perspectives:**

**🔧 Engineering Perspective:**
- Technical feasibility
- Implementation complexity
- Potential technical risks
- Dependencies and prerequisites
- Realistic timeline estimates

**💼 Executive Perspective:**
- Business value and strategic fit
- Resource allocation justification
- Competitive positioning
- Revenue/retention impact
- Opportunity cost

**👥 User Research Perspective:**
- User needs alignment
- Usability concerns
- Edge cases and scenarios
- Adoption barriers
- Success metric validity

**How to request:**
```
Get reviews from all three sub-agents in .claude/agents/ and consolidate
feedback into a single document:
- @.claude/agents/engineer.md - technical review
- @.claude/agents/executive.md - business review
- @.claude/agents/user-researcher.md - UX review
```

**Why this works:** You get diverse feedback early, when it's cheap to iterate. By the time you share with your actual team, you've already addressed obvious issues.

---

## 💡 Best Practices

### Do:
- ✅ **Start with context** - Always @-mention company docs, research, templates before writing
- ✅ **Question your assumptions** - Use Socratic framework to clarify fuzzy thinking
- ✅ **Generate options** - Create 2-3 strategic approaches, don't go with first idea
- ✅ **Get early feedback** - Use sub-agents before sharing with real team
- ✅ **Drive the process** - You make decisions, AI provides options and perspectives
- ✅ **Incorporate research** - Use actual user quotes and data, not just intuition
- ✅ **Think in parallel** - Use agents to generate multiple versions simultaneously

### Don't:
- ❌ **Let AI write for you** - You're partnering, not outsourcing
- ❌ **Skip the thinking** - Socratic questions exist to sharpen YOUR judgment
- ❌ **Accept first draft** - Always generate alternatives to compare
- ❌ **Ignore feedback** - Sub-agent reviews often catch important issues
- ❌ **Forget constraints** - Technical, resource, and timeline realities matter
- ❌ **Work in isolation** - Use full context (company + research + templates)

### Pro Tips:

1. **Create a methods library** - Build a collection of frameworks (Socratic questioning, Jobs-to-be-Done, RICE prioritization) you can @-mention for any PRD
2. **Maintain template library** - Keep multiple PRD templates for different use cases (new feature, redesign, technical project, experiment)
3. **Save great agent prompts** - When a sub-agent gives especially valuable feedback, save that persona/prompt for reuse
4. **Iterate on context docs** - Your company-context.md should evolve as strategy changes. Keep it current.
5. **Use checkpoints** - Save each version (v1, v2, v3) so you can reference alternative approaches later
6. **Combine approaches** - Don't feel locked into one version. Often the best PRD combines elements from multiple approaches.
7. **Document your reasoning** - In the PRD, note WHY you chose this approach over alternatives. Shows thoughtful decision-making.

---

## 🐛 Troubleshooting

### "AI-generated PRDs feel generic"

**Likely cause:** Insufficient context or too much AI autonomy

**Fix:**
1. Provide more specific company context (@-mention docs with strategy, customer insights, constraints)
2. Use Socratic questioning to inject YOUR specific thinking
3. Don't ask "write me a PRD" - ask "help me think through this PRD"
4. Add specific examples and user quotes from research
5. Review and add your own insights/context throughout
### "Sub-agent feedback is too surface-level"

**Likely cause:** Agent personas aren't specific enough, or PRD lacks depth

**Fix:**
1. Enhance sub-agent personas with specific concerns (e.g., engineer cares about API rate limits, scalability)
2. Provide agents with more context (@-mention technical docs, strategy docs)
3. Ask for specific types of feedback: "Focus on technical risks" or "Evaluate against Q1 goals"
4. Make sure your PRD draft has enough detail to review
5. Use different agent types for different stages (early: strategic review, later: implementation review)

### "Process takes too long"

**Likely cause:** Doing too many steps, or not using parallelization

**Fix:**
1. You don't need all three strategic approaches every time - sometimes one is enough
2. Use agents to generate drafts in parallel (not sequentially)
3. Skip Socratic questions if you already have clarity
4. Not every PRD needs sub-agent review - use for high-stakes features
5. Save time by reusing context docs and templates across PRDs

### "Hard to track which version is current"

**Likely cause:** Poor file naming or version management

**Fix:**
1. Use clear naming: `feature-name-prd-v1.md`, `feature-name-prd-v2-chat-first.md`, `feature-name-prd-final.md`
2. Add dates to filenames if working over time: `feature-name-prd-2025-01-15.md`
3. Keep a changelog section in your PRD documenting major revisions
4. Use git commits to track evolution
5. Archive old versions in a `drafts/` folder once finalized

---

## 📚 Community Resources

### Official Documentation

- **[Claude Code Overview](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)** - Official Claude Code documentation from Anthropic

### Prompt Engineering

- **[Anthropic's Prompt Engineering Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)** - Official interactive tutorial for writing effective prompts
- **[Awesome Claude Prompts](https://github.com/langgptai/awesome-claude-prompts)** - Community collection of prompt examples

### PM Resources

- **[Lenny's Newsletter](https://www.lennysnewsletter.com/)** - Weekly product management and growth advice from Lenny Rachitsky
- **[Reforge](https://www.reforge.com/)** - Advanced courses on product strategy, growth, and data-driven decision making

---

## 🚀 What's Next?

### After Module 2.1

You now understand:
- ✅ How to partner with AI (not just use it as a tool)
- ✅ Using @-mentions to provide full context
- ✅ Socratic questioning to clarify fuzzy thinking
- ✅ Generating multiple strategic approaches with agents
- ✅ Getting multi-perspective feedback via sub-agents
- ✅ Producing stronger first drafts before team review

**Ready for Module 2.2: Data-Driven Decisions?**

In the next module, you'll learn how to use data to drive product decisions - from discovering problems in your funnel, to estimating feature impact, to analyzing A/B test results like a pro. You'll see how to combine quantitative analysis with AI to find insights faster and make better decisions.

**[Go to Module 2.2 Reference →](../2.2-data-driven-decisions/REFERENCE_GUIDE.md)**

Or, if you're doing the interactive track:
```
Type: /start-2-2
```

---

**Remember:** The best PRDs come from clear thinking, full context, and diverse perspectives. AI doesn't replace your judgment—it amplifies it by helping you think through more angles, faster. Use these techniques not just for PRDs, but for any strategic document where clarity and thoroughness matter.
