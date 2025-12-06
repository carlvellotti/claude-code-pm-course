# Socratic Questioning Framework for PRDs

This framework helps sharpen feature thinking through targeted questions. Use this to help PMs move from vague ideas to clear, well-reasoned feature definitions.

---

## Core Philosophy

**The goal is NOT to challenge the PM, but to help them think more clearly.**

Good Socratic questioning:
- ✅ Helps uncover assumptions
- ✅ Clarifies fuzzy thinking
- ✅ Surfaces potential issues early
- ✅ Strengthens the rationale

Bad Socratic questioning:
- ❌ Feels like an interrogation
- ❌ Makes PM defensive
- ❌ Asks "gotcha" questions
- ❌ Questions just to question

---

## The Five Question Categories

Use 3-5 questions total. Pick the most relevant from each category based on the feature.

### 1. Problem Clarity Questions

**Purpose:** Ensure the problem is real and well-understood

**Questions to ask:**

**"What specific user pain point does this solve?"**
- Look for concrete examples, not abstract statements
- Good: "Users waste 10 minutes finding task context across 5 tools"
- Bad: "Users want better productivity"

**"How do we know this is a real problem?"**
- Push for evidence: user interviews, support tickets, churn reasons, usage data
- Qualitative + quantitative is strongest

**"Who experiences this problem most acutely?"**
- Forces specificity about target users
- Helps prioritize if you can't solve for everyone

**"What's the cost of NOT solving this?"**
- Revenue impact? Churn? Competitive loss? Team productivity?
- Helps establish urgency

---

### 2. Solution Validation Questions

**Purpose:** Ensure the proposed solution actually solves the problem

**Questions to ask:**

**"Why is this the right solution for that problem?"**
- Look for logical connection between problem and solution
- Watch for solutions looking for problems

**"What alternatives did you consider? Why did you reject them?"**
- Shows depth of thinking
- Reveals trade-offs that were considered
- "This is the only way" is a red flag

**"What's the simplest version that solves the core problem?"**
- Helps avoid over-engineering
- Identifies must-have vs nice-to-have

**"How will users discover this feature?"**
- Great solution that no one finds is useless
- Tests whether it fits naturally into user workflows

---

### 3. Success Criteria Questions

**Purpose:** Ensure we can measure if the solution works

**Questions to ask:**

**"How will we know if this feature is successful?"**
- Look for specific, measurable outcomes
- Both quantitative (metrics) and qualitative (feedback) matter

**"What would make you consider this feature a failure?"**
- Helps identify risks and edge cases
- Good teams have clear failure criteria

**"What metric are we trying to move? By how much?"**
- Forces specificity
- "Improve engagement" → "Increase weekly active tasks created by 25%"

**"What's the adoption target?"**
- Not all features need 100% adoption
- Different targets for different user segments

---

### 4. Constraint & Trade-off Questions

**Purpose:** Surface limitations and difficult decisions

**Questions to ask:**

**"What are the technical constraints or risks?"**
- Helps engineering team provide realistic estimates
- Identifies blockers early

**"What are we NOT going to do as part of this?"**
- Scope management is critical
- Clear non-goals prevent scope creep

**"What existing features or workflows does this affect?"**
- Nothing exists in isolation
- Need to think about system impacts

**"If we had half the time/resources, what would we cut?"**
- Reveals true priorities
- Helps identify MVP vs full vision

---

### 5. Strategic Fit Questions

**Purpose:** Ensure feature aligns with company goals and strategy

**Questions to ask:**

**"Why is this the right feature to build RIGHT NOW?"**
- Tests urgency and prioritization
- Helps clarify opportunity cost

**"How does this fit into our broader product strategy?"**
- Feature should ladder up to bigger goals
- Helps tell the strategic narrative

**"What happens if we wait 6 months to build this?"**
- Tests true urgency vs perceived urgency
- Helps prioritize against other opportunities

**"How does this affect our competitive position?"**
- Are we playing catch-up or leading?
- Table-stakes features vs differentiators

---

## Conversation Flow Tips

### Start Broad, Then Narrow

**First question:** Problem clarity
**Middle questions:** Solution validation + success criteria
**Last question:** Strategic fit

This helps PMs start from user needs and work up to business strategy, not the reverse.

### Listen for Red Flags

**Vague language:**
- "Users want better..." → What specifically?
- "This will improve..." → Improve what, by how much?
- "Everyone needs..." → Really? Everyone?

**Solution-first thinking:**
- PM can describe feature but struggles to describe problem
- "Because competitors have it" is not a problem statement

**Lack of evidence:**
- "I think users would like..." → How do we know?
- No data, no user quotes, no examples

**Unclear success:**
- Can't articulate what success looks like
- No metrics, no qualitative indicators

---

## Example Question Sequence

**For AI Voice Chat + To-Do List Feature:**

1. **Problem:** "What specific pain point does voice chat solve that typing doesn't?"
   - Pushes for concrete problem statement

2. **Solution:** "Why voice over other input methods? What alternatives did you consider?"
   - Tests solution validation

3. **Success:** "How will we measure if users actually use the voice feature?"
   - Establishes clear success criteria

4. **Constraints:** "What are we NOT including in V1? What comes later?"
   - Helps scope the MVP

5. **Strategy:** "Why is this the right AI feature to build first, versus other AI opportunities?"
   - Tests strategic thinking

---

## Coaching Notes

**If PM struggles with a question:**
- Don't leave them hanging
- Offer multiple-choice options
- Share examples from other contexts
- This is a learning tool, not a test

**If PM gives weak answer:**
- Ask follow-up: "Can you say more about that?"
- Probe gently: "What evidence supports that?"
- Offer alternative perspective: "Some might argue X, how would you respond?"

**If PM gives great answer:**
- Acknowledge it!
- Build on it with next question
- Show how their answer strengthens the PRD

---

## Output Goal

After Socratic questioning, PM should have:

✅ Clear, specific problem statement with evidence
✅ Rational justification for why THIS solution
✅ Concrete success criteria (quantitative + qualitative)
✅ Explicit scope boundaries (what's in, what's out)
✅ Strategic narrative for why this matters now

These answers form the foundation of a strong PRD.

---

**Remember:** This is not a checklist. Use judgment. Pick the 3-5 most important questions for THIS feature. Quality over quantity.
