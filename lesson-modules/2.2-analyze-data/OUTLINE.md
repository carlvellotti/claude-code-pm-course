# Module 2.2: Data-Driven Feature Development - Ultra Simple Outline

## Files Needed to Start

### `impact-estimation-framework.md` (reference guide)
**Content:** Complete guide to estimating feature impact - the formula (Users × Action Rate × Lift × Value), how to estimate lift, how to calculate value, three-scenario approach, common pitfalls
**Purpose:** Teaching resource students read before doing impact estimation exercise
**Note:** This is a static reference document, not generated

### `taskflow-usage-data-q4.csv` (1000 rows)
**Columns:** `user_id`, `event_type`, `timestamp`, `company_size`, `user_role`, `industry`
**Generated with:** Python/pandas - realistic event sequences (signup, first_task_created, first_task_completed, invite_sent, etc.)
**Story baked in:** Small teams (5-20 people) show higher activation but need examples; enterprise users (100+) get stuck more often despite having clearer use cases

### `activation-funnel-q4.csv` (aggregated funnel data)
**Columns:** `step`, `users_entered`, `users_completed`, `completion_rate`, `median_time_to_complete`
**Generated with:** Python - aggregate the usage data above into funnel steps
**Story baked in:** Biggest drop-off (60%) is between "first task created" and "first task completed" - users create empty tasks but don't know what to put in them

### `user-survey-responses.csv` (800 responses)
**Columns:** `user_id`, `company_size`, `onboarding_rating`, `biggest_confusion`, `feature_request`, `would_recommend`
**Generated with:** Python with curated text snippets for realistic survey responses
**Story baked in:** Top complaints are "didn't know what to create", "needed examples", "felt overwhelmed by blank canvas" - validates the problem from funnel data

### `onboarding-experiment-results.csv` (8K users, post-launch A/B test)
**Columns:** `user_id`, `cohort` (treatment/control), `signup_date`, `company_size`, `user_role`, `completed_first_task`, `time_to_first_task_minutes`, `invited_teammate`, `used_task_template`, `days_active_week_1`, `tasks_completed_week_1`
**Generated with:** Python/numpy with controlled randomization
**Story baked in - NUANCED RESULTS:**
- **Topline modest:** Overall activation 45% → 48% (small improvement, p=0.04, barely stat sig)
- **Segment reveals truth:** Small teams (5-20): 45% → 56% (huge win, p<0.001) vs Enterprise (100+): 45% → 42% (actually worse, guided flow too simple for their needs)
- **Quality over quantity:** Week 1 retention among activated users: 60% → 78% (massive quality improvement, p<0.001)
- **Feature adoption signals:** Treatment users who saw task templates in guided flow use them 3.2x more (35% vs 11%, p<0.001)
- **Viral coefficient:** Invite teammate rate during onboarding: 35% vs 12% in control (p<0.001) - leading indicator of growth
**Teaching moment:** Teaches to dig beyond topline, segment by target customer, focus on quality activations not just quantity, identify leading indicators

## Files Created During Module
- `activation-problem-analysis.md` (data analysis revealing where users get stuck and why)
- `guided-onboarding-impact-estimate.md` (projected impact: activation 45% → 58%, time-to-value 45min → 20min)
- `guided-onboarding-roi-scenarios.md` (pessimistic/realistic/optimistic scenarios with dev costs)
- `onboarding-experiment-readout.md` (statistical analysis with ship/iterate/kill recommendation)

## High-Level Overview
- Real PM scenario at TaskFlow: activation stuck at 45% for 6 months, need to find and fix the problem
- Follow complete product development cycle: discover problem → identify solution → estimate impact → analyze experiment
- PMs get this data from Mixpanel (`taskflow-usage-data-q4.csv`, `activation-funnel-q4.csv`) and Qualtrics (`user-survey-responses.csv`)
- Challenge: data is messy and scattered, leadership wants confident recommendations backed by analysis
- First we need to come up with some ideas
- **PHASE 1 - DISCOVERY:** Analyze `activation-funnel-q4.csv` to find biggest drop-off (60% drop between signup and first task completed)
- **PHASE 1 - DISCOVERY:** Cross-reference with `user-survey-responses.csv` to understand WHY users drop (confused about what to create, need examples)
- **PHASE 1 - DISCOVERY:** Synthesize findings in `activation-problem-analysis.md` and propose solution: Guided Onboarding with sample project
- Now we need to estimate the impact of this idea
- **PHASE 2 - IMPACT ESTIMATION:** Build impact model using `taskflow-usage-data-q4.csv` to project Guided Onboarding effect on activation in `guided-onboarding-impact-estimate.md`
- **PHASE 2 - IMPACT ESTIMATION:** Create ROI scenarios in `guided-onboarding-roi-scenarios.md` (dev cost: 4 eng-months = $100k vs projected ARR lift based on activation improvement)
- Now image we've run the experiment and have messy results
- **PHASE 3 - EXPERIMENT ANALYSIS:** Fast-forward to post-launch, analyze results from `onboarding-experiment-results.csv` (statistical significance, effect size, segment performance)
- **PHASE 3 - EXPERIMENT ANALYSIS:** Write experiment readout in `onboarding-experiment-readout.md` with ship to 100%/iterate/kill decision and supporting data
- Show complete PM workflow: use data to find problems, estimate impact before building, analyze results after shipping

---

## Teaching Flow

- Welcome to Module 2.2: Data-Driven Feature Development
- This module teaches the complete PM workflow from problem discovery through experiment analysis
- Real scenario: TaskFlow's activation rate has been stuck at 45% for 6 months
- Leadership is frustrated, asking what you're going to do about it
- STOP: Ready to dig into the data and figure this out?
- USER: Yes / Ready

---

### PHASE 1: DISCOVERY - Finding the Problem

- First step: analyze the data to find WHERE users are getting stuck
- We have activation funnel data exported from Mixpanel in `activation-funnel-q4.csv`
- STOP: Ask user to say "Analyze the activation funnel"
- USER: Analyze the activation funnel
- ACTION: Read `activation-funnel-q4.csv` and analyze the funnel steps
	- Show funnel: Signup → First Task Created → First Task Completed → Invite Sent
	- Calculate drop-off rates at each step
	- Identify biggest drop-off: 60% between "First Task Created" and "First Task Completed"
- Found it! 60% of users who create a task never complete it
- STOP: Why do you think users are abandoning tasks they just created?
- USER: Various responses (don't know what to put, confused, etc.)

---

- Good instinct, let's validate with data
- We have user survey responses in `user-survey-responses.csv` - 800 responses from recent signups, go check it out
- STOP: Ask user to say "Analyze the survey data to understand why users drop off"
- USER: Analyze the survey data to understand why users drop off
- ACTION: Read `user-survey-responses.csv` and analyze responses
	- Extract top complaints from `biggest_confusion` field
	- Count frequency of themes: "didn't know what to create" (35%), "needed examples" (28%), "felt overwhelmed" (22%)
	- Cross-reference with `company_size` to see if patterns differ
- Survey confirms it! Users feel overwhelmed by the blank canvas and need examples
- Small teams especially struggle - they don't have established workflows yet
- STOP: Based on this data, what feature would you propose?
- USER: Various ideas (templates, examples, guided onboarding, etc.)

---

- Great ideas! Let's synthesize our findings into a proper analysis
- For now we'll just move forward with this idea: Guided Onboarding
- We need to document: the problem, supporting data, and proposed solution
- STOP: Ask user to say "Create the problem analysis document"
- USER: Create the problem analysis document
- ACTION: Create `activation-problem-analysis.md` with:
	- Problem statement: 60% drop-off between task creation and completion
	- Quantitative evidence: funnel data showing the drop-off
	- Qualitative evidence: survey quotes and themes
	- Segmentation insight: especially bad for small teams (our target market!)
	- Proposed solution: Guided Onboarding with sample project pre-populated with example tasks
- Perfect! We've identified the problem and proposed a solution: Guided Onboarding
- STOP: Make sense so far? Any questions before we move to impact estimation?
- USER: Makes sense / Questions

---

### PHASE 2: IMPACT ESTIMATION - Is It Worth Building?

- Now we need to convince leadership this is worth building
- Engineering estimates 4 months of work = $100k in dev costs
- We need to project the business impact to justify that investment
- STOP: What metrics do you think we should try to improve with Guided Onboarding?
- USER: Various responses (activation, time to value, retention, etc.)

---

- Great thinking! Let's focus on activation rate and time-to-value
- Before we dive in, let me show you the framework for impact estimation
- STOP: Ask user to say "Show me the impact estimation framework"
- USER: Show me the impact estimation framework
- ACTION: Read and present `impact-estimation-framework.md`
	- Show the formula: Impact = Users Affected × Current Action Rate × Expected Lift × Value per Action
	- Explain each component with examples
	- Emphasize the three-scenario approach (pessimistic/realistic/optimistic)
- Now let's apply this framework to Guided Onboarding
- We have detailed usage data in `taskflow-usage-data-q4.csv` to build our model
- STOP: Ask user to say "Build the impact estimation model"
- USER: Build the impact estimation model
- ACTION: Read `taskflow-usage-data-q4.csv` and analyze usage patterns
	- Segment users by company size and calculate activation rates
	- Calculate current time-to-value (median: 45 minutes)
	- Estimate improvement based on similar features at competitors (from survey data)
	- Project activation improvement: 45% → 58% (conservative based on removing the 60% drop-off)
	- Project time-to-value improvement: 45 min → 20 min (users start with pre-filled tasks)
- ACTION: Create `guided-onboarding-impact-estimate.md` with projections
	- Current state: 45% activation, 45 min time-to-value
	- Projected state: 58% activation, 20 min time-to-value
	- Business impact: +13 percentage points activation = +650 activated users/month
	- Revenue impact: 650 users × $12/user/month × 60% conversion = +$4,680 MRR = +$56k ARR
- Looking good! $100k investment for $56k ARR in year 1
- STOP: Does that ROI seem worth it to you?
- USER: Maybe not / seems low / depends

---

- Let's model different scenarios
- Our estimate assumed certain adoption rates and effectiveness
- What if our assumptions are wrong? Let's build pessimistic and optimistic scenarios
- STOP: Ask user to say "Create ROI scenarios"
- USER: Create ROI scenarios
- ACTION: Create `guided-onboarding-roi-scenarios.md` with three scenarios
	- **Pessimistic:** Only 30% of users see guided onboarding (slow rollout), activation 45% → 50%, ARR +$21k, ROI: 0.21x (not great)
	- **Realistic:** 70% adoption, activation 45% → 58%, ARR +$56k, ROI: 0.56x in year 1, 1.7x over 3 years (good!)
	- **Optimistic:** 90% adoption + retention improvements, activation 45% → 62%, ARR +$89k, ROI: 0.89x in year 1
	- Include retention multiplier: activated users stay 3x longer (LTV impact)
- Much better! When you factor in retention, the realistic case is 1.7x ROI over 3 years
- Plus this unblocks growth - we can't scale if activation stays at 45%
- STOP: Would you pitch this to leadership now?
- USER: Yes / Need more data

---

- Great! In the real world, you'd present this to leadership and get buy-in to build it
- They'd probably approve it given the data and strategic importance
- Let's fast-forward: your team built Guided Onboarding and launched it as an A/B test
- STOP: Ready to analyze the experiment results?
- USER: Yes / Ready

---

### PHASE 3: EXPERIMENT ANALYSIS - Did It Work?

- Fast-forward 4 weeks: experiment ran with 8,000 users (4,000 treatment, 4,000 control)
- You exported the results from LaunchDarkly into `onboarding-experiment-results.csv`
- Time to see if our bet paid off
- Leadership wants to know: ship to 100%, iterate, or kill?
- STOP: Ask user to say "Analyze the experiment results"
- USER: Analyze the experiment results
- ACTION: Read `onboarding-experiment-results.csv` and start analysis
	- Calculate topline activation: Control 45.2%, Treatment 47.8% (+2.6 percentage points)
	- Run statistical test: p-value = 0.04 (barely significant at p<0.05 threshold)
	- Calculate confidence interval: [0.1%, 5.1%] - wide range, could be small or moderate effect
- Hmm, the topline looks underwhelming
- We projected 58% but only got 48%
- STOP: What would you recommend based on these results? Ship, iterate, or kill?
- USER: Various responses (probably kill or iterate)

---

- Hold on! Don't give up yet - we need to segment the data
- Remember our target market is small teams (5-20 people), not enterprise
- Let's see if the feature works for our target segment even if topline is modest
- STOP: Ask user to say "Segment the results by company size"
- USER: Segment the results by company size
- ACTION: Segment analysis by company_size
	- **Small teams (5-20):** Control 44.8%, Treatment 56.2% (+11.4pp, p<0.001) - HUGE WIN!
	- **Mid-size (21-99):** Control 45.5%, Treatment 47.1% (+1.6pp, p=0.23) - no real effect
	- **Enterprise (100+):** Control 45.6%, Treatment 42.1% (-3.5pp, p=0.08) - actually worse!
- Aha! The feature crushes for small teams but hurts for enterprise
- This makes sense: guided onboarding is too simple for complex enterprise workflows
- STOP: Does this change your recommendation?
- USER: Yes / More confident / Ship to small teams only

---

- Exactly! But let's check one more thing: quality over quantity
- Did we activate more users or better users? Let's look at retention
- STOP: Ask user to say "Analyze retention among activated users"
- USER: Analyze retention among activated users
- ACTION: Filter to activated users only, calculate week 1 retention (days_active_week_1 >= 3)
	- Control activated users: 60.1% week 1 retention
	- Treatment activated users: 78.4% week 1 retention (+18.3pp, p<0.001)
	- Treatment users completed 2.3x more tasks in week 1 (6.8 vs 2.9, p<0.001)
- Wow! Not only did we activate more small teams, but those activations are MUCH higher quality
- 78% retention vs 60% - that's a massive improvement in user quality
- STOP: Any other metrics we should check before making our final recommendation?
- USER: Feature adoption / invite rate / other ideas

---

- Let's check the leading indicators: template usage and invite rate
- These predict long-term retention and viral growth
- STOP: Ask user to say "Analyze feature adoption metrics"
- USER: Analyze feature adoption metrics
- ACTION: Analyze `used_task_template` and `invited_teammate` columns
	- Template usage: Treatment 35.2% vs Control 10.9% (3.2x higher, p<0.001)
	- Invite teammate during onboarding: Treatment 34.8% vs Control 12.1% (2.9x higher, p<0.001)
	- Users who used templates completed 4.1x more tasks in week 1
	- Users who invited teammates have 2.8x higher 30-day retention (historical data)
- Perfect! These leading indicators suggest long-term success
- Template usage shows feature is sticky, invite rate predicts viral growth
- STOP: Ready to write up the final experiment readout?
- USER: Yes / Ready

---

- Time to synthesize everything into a clear recommendation for leadership
- This is what PMs call an "experiment readout" - your final analysis and recommendation
- STOP: Ask user to say "Create the experiment readout"
- USER: Create the experiment readout
- ACTION: Create `onboarding-experiment-readout.md` with:
	- **Executive Summary:** Ship to small teams (5-20 people), exclude enterprise
	- **Topline Results:** Modest overall lift (45% → 48%, p=0.04) but deceiving
	- **Segment Analysis:** Small teams +11.4pp (p<0.001), Enterprise -3.5pp (p=0.08)
	- **Quality Metrics:** Week 1 retention +18.3pp (60% → 78%, p<0.001) - massive quality improvement
	- **Leading Indicators:** Template usage 3.2x higher, invite rate 2.9x higher - predicts long-term success
	- **Recommendation:** Ship to 100% for small teams, build separate enterprise onboarding later
	- **Expected Impact:** +450 high-quality activated users/month (small teams only), +$32k ARR, 1.9x ROI when factoring retention
	- **Next Steps:** Ship this week, monitor for 2 weeks, start enterprise onboarding discovery
- Excellent work! You've turned messy experiment data into a clear, confident recommendation
- STOP: See how we went from "topline looks bad" to "ship it" by digging deeper?
- USER: Yes / Makes sense

---

### Wrap-Up

- Let's recap what you just learned - the complete PM workflow:
- **Phase 1 - Discovery:** Used funnel and survey data to identify WHERE and WHY users drop off
	- Found 60% drop-off between task creation and completion
	- Survey revealed users need examples and feel overwhelmed
	- Proposed Guided Onboarding as solution
- **Phase 2 - Impact Estimation:** Built ROI model to justify $100k dev investment
	- Projected activation improvement and revenue impact
	- Created pessimistic/realistic/optimistic scenarios
	- Showed 1.7x ROI over 3 years in realistic case
- **Phase 3 - Experiment Analysis:** Analyzed messy results to find the real story
	- Topline looked modest but segment analysis revealed huge win for target market
	- Quality metrics showed we activated BETTER users, not just more users
	- Leading indicators predicted long-term success
- STOP: Which phase was most valuable for you to learn?
- USER: Various responses

---

- The key lesson: don't stop at topline metrics!
- Always segment by your target customer
- Look at quality metrics (retention) not just quantity (activation rate)
- Check leading indicators that predict long-term success
- This is how great PMs make data-driven decisions
- STOP: Any questions about this workflow?
- USER: Questions / No questions

---

- Fantastic! You now know how to:
	- Analyze data to discover problems (funnel + survey analysis)
	- Estimate impact before building (ROI modeling with scenarios)
	- Analyze experiments after shipping (statistical analysis with segmentation)
- This is the workflow you'll use constantly as a PM
- Every major feature should follow this pattern: discover → estimate → build → analyze
- STOP: Ready to move to the next module?
- USER: Yes / Want to practice more

---

**[MODULE COMPLETE]**
