# Impact Estimation Framework

**A Product Manager's Guide to Estimating Feature Impact**

---

## The Formula

Impact estimation follows this basic formula:

```
Impact = Users Affected × Current Action Rate × Expected Lift × Value per Action
```

Let's break down each component:

---

## 1. Users Affected

**Question:** How many users will be exposed to this feature?

**Examples:**
- **All new signups:** 5,000 users/month
- **Existing users who see onboarding:** 70% of signups = 3,500 users/month
- **Enterprise customers only:** 500 users/month

**Key considerations:**
- Will this be a gradual rollout or 100% launch?
- Are we targeting specific segments?
- What's the adoption curve? (not everyone uses a feature immediately)

---

## 2. Current Action Rate

**Question:** What percentage of users currently take the desired action?

**Examples:**
- **Activation rate:** 45% of signups complete first task
- **Invite rate:** 12% of users invite a teammate
- **Feature adoption:** 23% of users use advanced filters

**How to find this:**
- Query your analytics tool (Mixpanel, Amplitude)
- Export usage data and calculate the baseline
- Segment by user type if relevant (small teams vs enterprise)

---

## 3. Expected Lift

**Question:** How much will this feature improve the action rate?

**This is the hardest part!** You need to make educated assumptions based on:

**Sources of lift estimates:**
1. **Similar features you've shipped:** "Last time we improved onboarding, we saw +8pp lift"
2. **Competitor benchmarks:** "Linear's activation is 65%, we're at 45%, so there's 20pp of room"
3. **User research:** "Survey shows 60% of drop-offs are due to X, so fixing X could recover 60% of that drop-off"
4. **A/B test results from similar features:** Historical data from your company
5. **Expert judgment:** Engineering/Design/PM estimates based on the scope of change

**Example calculation:**
- Current: 45% activation (4,500 out of 10,000 signups complete first task)
- Problem: 60% drop-off between "create task" and "complete task"
- Root cause: Users don't know what to put in tasks (from survey)
- Solution: Guided onboarding with pre-filled example tasks
- Estimate: If 60% drop because of confusion, and we eliminate that confusion, we could recover ~50% of that drop-off (being conservative)
- Math: 60% drop = 6,000 users lost. Recover 50% = +3,000 users. New rate: 7,500/10,000 = 75%... but that seems too optimistic
- Conservative estimate: Recover 30% of drop-off = +1,800 users = 63% activation
- Really conservative: Recover 20% = +1,200 users = 58% activation ← Use this

**Pro tip:** Create three scenarios (pessimistic, realistic, optimistic) to bound your estimate.

---

## 4. Value per Action

**Question:** What is each incremental action worth to the business?

**For activation improvements:**
- Activated user → Paying customer conversion rate: 60%
- Average revenue per user: $12/month
- Average customer lifetime: 24 months
- **Value per activated user:** $12 × 60% × 24 months = $172.80 LTV

**For retention improvements:**
- Each percentage point of retention = X users stay longer
- Extended LTV = retention improvement × ARPU × extended months

**For viral/invite features:**
- Each invite → 40% acceptance rate
- Each accepted invite → 60% activation → 60% conversion
- **Value per invite:** 40% × 60% × 60% × $172.80 LTV = $41.47

---

## Putting It All Together

**Example: Guided Onboarding for TaskFlow**

### Current State:
- **Users affected:** 5,000 new signups/month (post-launch, assume 70% see it = 3,500/month)
- **Current action rate:** 45% activation
- **Current activated users:** 2,250/month
- **Value per activation:** $172.80 LTV ($12/mo × 60% conversion × 24 months)

### Projected Impact (Realistic Scenario):
- **Expected lift:** 45% → 58% activation (+13 percentage points)
- **New activated users:** 2,030/month (58% of 3,500)
- **Incremental activated users:** +130/month (2,030 - 1,900)
- **Annual value:** 130 × 12 months × $172.80 = $269,856 in LTV
- **Year 1 revenue impact:** 130 × 12 × $12 × 60% = $11,232 MRR = $134,784 ARR

### Cost:
- **Engineering:** 4 engineers × 1 month = $100,000

### ROI:
- **Year 1:** $134,784 revenue / $100,000 cost = 1.35x ROI
- **3-year LTV:** $269,856 / $100,000 = 2.7x ROI

---

## Three Scenarios Approach

Always create three scenarios to acknowledge uncertainty:

### Pessimistic Scenario (20th percentile):
- Lower adoption (30% instead of 70%)
- Lower lift (45% → 50% instead of 58%)
- Calculate minimum expected impact

### Realistic Scenario (50th percentile):
- Expected adoption (70%)
- Conservative lift based on data (45% → 58%)
- Your "most likely" case

### Optimistic Scenario (80th percentile):
- High adoption (90%)
- Strong lift plus secondary effects (45% → 62% + retention improvements)
- Best-case scenario if everything works

**Present all three to leadership** so they understand the range of outcomes.

---

## Common Pitfalls

❌ **Don't:**
- Assume 100% of users will use the feature
- Take the most optimistic benchmark ("Notion has 80% activation!")
- Forget to account for conversion rates in your value calculation
- Include every possible secondary effect (keep it simple)
- Present a single number without uncertainty bounds

✅ **Do:**
- Use historical data from your company when possible
- Be conservative with lift estimates (better to under-promise)
- Show your work (make assumptions explicit)
- Create multiple scenarios
- Validate assumptions with data where possible

---

## Template for Impact Estimates

```markdown
## Feature: [Name]

### Current State
- Users affected: [number]/month
- Current action rate: [%]
- Current performance: [number] users taking action
- Value per action: $[amount]

### Projected Impact (Realistic Scenario)
- Expected lift: [current%] → [new%] (+[difference]pp)
- New users taking action: [number]/month
- Incremental impact: +[number]/month
- Annual value: [calculation]
- Year 1 revenue: [calculation]

### Investment Required
- Engineering: [cost]
- Design: [cost]
- Other: [cost]
- **Total:** $[total]

### ROI
- Year 1: [revenue] / [cost] = [X]x ROI
- 3-year LTV: [LTV value] / [cost] = [X]x ROI

### Assumptions & Risk
- Assumption 1: [state assumption]
- Assumption 2: [state assumption]
- Risk: [what could go wrong]
- Mitigation: [how to reduce risk]
```

---

**Remember:** Impact estimates are not predictions—they're informed hypotheses. The goal is to make better decisions, not to be perfectly accurate. Show your work, state your assumptions, and update your estimates as you learn more.
