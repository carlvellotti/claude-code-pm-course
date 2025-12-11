# Devil's Advocate: Stress-Testing Product Strategy

## What Is This Method?

Devil's advocate is a **critical thinking technique** where you deliberately challenge your own strategy to find holes, weaknesses, and faulty assumptions. It's the strategic equivalent of "red team" testing in security.

The goal is to **kill your bad ideas before you waste months building them.**

---

## Why This Matters

### The Problem: Confirmation Bias

When you've developed a strategy, you naturally:
- Look for evidence that supports it
- Downplay evidence against it
- Rationalize away concerns
- Get emotionally attached to your idea

This leads to expensive mistakes.

### The Solution: Structured Criticism

By systematically attacking your own strategy, you:
- Find weaknesses early (when they're cheap to fix)
- Validate critical assumptions
- Strengthen your strategy before presenting it
- Build credibility (stakeholders see you've thought through objections)

---

## How to Use This Method

### Step 1: State Your Strategy Clearly

Write out your strategy in one paragraph using Rumelt's Kernel:
- **Diagnosis:** The challenge/opportunity
- **Guiding Policy:** Your approach
- **Coherent Actions:** Key initiatives

**Example:**
"TaskFlow's activation has improved but we need sustainable growth. Our strategy is to become the AI-native productivity tool for founder-led companies (5-20 people), differentiating through deep workflow integration that larger competitors can't match. We'll execute this through: (1) AI voice interface for hands-free task management, (2) AI-powered workflow suggestions based on usage patterns, (3) community-led growth to offset limited marketing budget."

### Step 2: Challenge Every Assumption

Go through each part of your strategy and ask devil's advocate questions.

---

## Devil's Advocate Questions

### DIAGNOSIS CHALLENGES

**"Are we solving the right problem?"**
- What if the problem isn't as important as we think?
- What evidence do we have that this is actually THE constraint?
- Could we be solving a symptom instead of the root cause?

**"Is our timing right?"**
- What if the market isn't ready for this yet?
- What if we're too late and the window has closed?
- What needs to be true about market timing?

**"Do we really understand the customer?"**
- What if our customer research is biased or unrepresentative?
- What if we're listening to the loudest customers, not the majority?
- What if stated preferences don't match actual behavior?

---

### GUIDING POLICY CHALLENGES

**"Why will customers choose us?"**
- What if customers don't actually care about our differentiation?
- What if our "unique value prop" isn't unique at all?
- What's our honest answer to "why not just use [competitor]?"

**"Why can't competitors copy this?"**
- What prevents a larger, better-funded competitor from copying this in 6 months?
- What if our "moat" is actually just a speed bump?
- Which parts are truly defensible vs. just execution?

**"What are we giving up?"**
- What customer segments are we explicitly NOT serving?
- What features/opportunities are we saying NO to?
- What if the thing we're deprioritizing is actually more valuable?

**"Do we have the right to win?"**
- What gives us an unfair advantage here?
- What if we're not uniquely positioned to execute this?
- Why us, why now?

---

### COHERENT ACTIONS CHALLENGES

**"Can we actually execute this?"**
- What if we don't have the technical capability?
- What if we're underestimating how long this takes?
- What resources/skills are we assuming we have?

**"Are these actions truly coherent?"**
- Do these initiatives reinforce each other, or are they independent?
- What if we're spreading ourselves too thin?
- Could we cut half of these and still execute the strategy?

**"What could kill this?"**
- What's the single point of failure?
- What external event would make this strategy obsolete?
- What if our key assumption is wrong?

**"What's the opportunity cost?"**
- What are we NOT doing because we're doing this?
- What if the path not taken was actually better?
- How do we know this is the highest-leverage use of our resources?

---

## Specific Question Sets

### For AI/Technology Strategies

**"What if the technology doesn't work as expected?"**
- What if AI accuracy isn't good enough?
- What if infrastructure costs are prohibitive?
- What if users don't trust AI for this use case?

**"What if the technology becomes commoditized?"**
- OpenAI/Google release this as an API tomorrow - then what?
- What if our "AI moat" disappears in 6 months?
- What's the strategy if the tech becomes table stakes?

### For Market Positioning Strategies

**"What if we're targeting the wrong segment?"**
- What if founder-led companies don't have budget?
- What if they churn faster than enterprise?
- What if this segment is actually too small to build a business?

**"What if the positioning doesn't resonate?"**
- What if "AI-native" is just buzzword bingo?
- What if customers just want "better Notion" not something new?
- How do we test positioning before betting everything on it?

### For Growth Strategies

**"What if our growth assumptions are wrong?"**
- What if virality doesn't work in this market?
- What if our conversion rate is half what we projected?
- What if CAC is 3x higher than expected?

**"What if we can't reach our target customers?"**
- What if founder-led companies don't hang out where we think?
- What if our community strategy takes 2 years to work?
- What's our backup plan for distribution?

---

## The "Needs to be True" Framework

For every major assumption, ask: **"What needs to be true for this to work?"**

Then validate each one.

### Example: TaskFlow AI Strategy

**Strategic Bet:** "Build AI voice interface for task management"

**What needs to be true:**
1. Voice accuracy must be >95% in noisy environments
   - **Validation:** Run test with 50 users in real settings

2. Users must prefer voice over typing (speed/convenience)
   - **Validation:** Time study + user testing

3. AI costs must be <$2/user/month to maintain margins
   - **Validation:** Build prototype, measure actual costs

4. Voice interface must work on web (our only platform)
   - **Validation:** Technical spike to test feasibility

5. Users must use it regularly (not just try once)
   - **Validation:** Measure retention in beta

**Red flag:** If you can't test these assumptions, you're betting blind.

---

## Pre-Mortem Technique

**Setup:** Imagine it's 12 months from now. Your strategy failed completely. Why?

**Instructions:** Write the postmortem explaining what went wrong.

### Example Pre-Mortem: TaskFlow AI Strategy

**"It's Q4 2026. Our AI voice strategy failed. Here's why:**

The voice interface worked technically, but users didn't adopt it. Turns out people are self-conscious talking to their computer in coffee shops and open offices. The use cases were too narrow (mostly in car or at home), which wasn't enough to justify the development cost.

We also underestimated competitors. Notion shipped a similar feature 3 months after us with better integrations. We couldn't differentiate enough to retain users.

Finally, AI infrastructure costs were 4x our projections. We had to charge $20/month instead of $12, which killed conversion. SMBs went with cheaper alternatives.

The real mistake: we built what was cool, not what users actually needed. Voice was a solution looking for a problem."

**Value:** This forces you to confront likely failure modes BEFORE you start building.

---

## How to Do This With AI (Claude)

### The Workflow

1. **Present your strategy to Claude**
   "Here's my product strategy: [explain your diagnosis, guiding policy, coherent actions]"

2. **Ask Claude to play devil's advocate**
   "Challenge this strategy. What are the holes? What assumptions am I making? What could go wrong?"

3. **Go deep on specific concerns**
   "The biggest concern is [X]. Help me think through scenarios where this fails."

4. **Validate assumptions**
   "What needs to be true for this to work? How can I test each assumption?"

5. **Refine your strategy**
   Based on challenges, strengthen weak points or pivot.

### What Makes This Effective

- **AI doesn't have emotional attachment** - Will point out flaws you're blind to
- **AI can think through scenarios quickly** - Explores failure modes systematically
- **AI knows competitive landscape** - Can reference what worked/failed for others
- **AI asks uncomfortable questions** - The ones you're avoiding

### Example Prompt

"I'm developing a product strategy and need you to play devil's advocate. Here's my strategy:

[Your strategy]

Please challenge this aggressively:
1. What assumptions am I making that might be wrong?
2. What could kill this strategy?
3. Why might customers not care about this?
4. How could competitors neutralize our advantage?
5. What am I not seeing?

Don't hold back - I need the harshest criticism to make this better."

---

## Red Flags in Strategy

If you hear yourself saying these things, you're not thinking critically:

❌ **"We'll just execute better than competitors"**
- That's not a strategy, that's wishful thinking

❌ **"This is obviously a good idea"**
- If it's obvious, why isn't someone else doing it successfully?

❌ **"Customers will love this"**
- Based on what evidence? Real validation or your intuition?

❌ **"We'll be first to market"**
- First-mover advantage is rare. Why do you think you'll be the exception?

❌ **"It's a big market"**
- Doesn't mean YOU can capture any of it

❌ **"We don't have direct competitors"**
- You have substitute competitors (what people do today instead)

❌ **"This is just like [successful company]"**
- Context is different. What's different about YOUR situation?

---

## Strengthening Your Strategy

After devil's advocate, your strategy should have:

### Clear Answers to Hard Questions

**Question:** "Why can't Notion copy this?"
**Weak answer:** "We'll move fast"
**Strong answer:** "We're building on proprietary usage data from 10k small teams. Notion targets enterprise and doesn't have these workflows mapped. It would take them 18 months to collect this data and rebuild for a different segment - by then we'll have network effects."

### Validated Assumptions

**Assumption:** "Users want voice interface"
**Validation:** "Ran prototype with 50 users. 65% used it >3x/week. Time-to-complete tasks was 40% faster vs typing. BUT only 20% used in office setting (noise/self-consciousness). Need to test in-office adoption more."

### Realistic Risk Assessment

"Our biggest risk is AI costs. At current volume, we're at $3.50/user/month, which breaks our margins. We need 10x volume to get to $1.50/user/month through scale. If we can't get there in 6 months, we'll need to pivot to a hybrid approach (AI for premium tier only)."

### Coherent Mitigation Plans

"To reduce execution risk, we're building mobile-first (harder to copy) and focusing on workflows competitors don't serve (agencies/consultants). If competitors copy the AI voice interface, we still win on workflow depth."

---

## When to Kill Your Strategy

After devil's advocate, you should kill your strategy if:

1. **Critical assumptions can't be validated** - Too risky
2. **No clear differentiation** - Competitors will copy immediately
3. **Opportunity cost is too high** - Other options are better
4. **Team doesn't have capability** - Can't execute
5. **Economics don't work** - Won't be profitable

**It's better to kill a bad strategy in planning than after 6 months of development.**

---

## Quick Reference: Devil's Advocate Checklist

When stress-testing your strategy, ask:

**DIAGNOSIS**
- [ ] Are we solving the right problem? What's our evidence?
- [ ] Is our timing right? What needs to be true about the market?
- [ ] Do we really understand customers? How have we validated?

**GUIDING POLICY**
- [ ] Why will customers choose us over alternatives?
- [ ] What prevents competitors from copying this?
- [ ] What are we explicitly saying NO to?
- [ ] Do we have the right to win here?

**COHERENT ACTIONS**
- [ ] Can we actually execute this with our resources?
- [ ] Are these actions truly reinforcing each other?
- [ ] What's the single point of failure?
- [ ] What's the opportunity cost?

**VALIDATION**
- [ ] What needs to be true for this to work?
- [ ] How can we test each critical assumption?
- [ ] What would a pre-mortem say about why this failed?
- [ ] What's our plan B if key assumptions are wrong?

**If you can't answer these confidently, keep refining.**

---

## Remember

**The goal isn't to kill your strategy - it's to make it stronger.**

Good strategies survive devil's advocate questioning because they're grounded in:
- Real customer insights
- Honest assessment of capabilities
- Clear differentiation
- Validated assumptions
- Realistic execution plans

**Embrace criticism early. It's cheaper than failure later.**

Use AI as your devil's advocate - it will ask the uncomfortable questions that help you develop an airtight strategy.
