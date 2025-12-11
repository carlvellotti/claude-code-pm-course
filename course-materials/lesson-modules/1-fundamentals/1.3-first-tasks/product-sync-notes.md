product sync - mon oct 7, 2:30pm

attendees: sarah, mike (cto), jordan, alex (mobile pm), jamie (eng lead), me

=== NOTIFICATIONS DISCUSSION ===

me presenting notification redesign proposal

current state is BAD:
- 127 tickets last quarter about notifications
- users either get 50+ notifs/day or turn everything off
- 42 different notification types (way too many!)
- on/off preferences only (not granular enough)
- sync delivery = slow API (200-400ms latency - mike said this)
- enterprise customers complaining in sales calls

my proposal:
3 tiers - urgent/important/fyi
- urgent = immediate (assigned, @mentioned, deadline)
- important = digest eligible (comments, status changes)
- fyi = opt-in only (likes, watchers, general activity)

smart batching - group related notifs
ex: 5 comments on same task = 1 notification not 5

digest mode - daily or twice daily
urgent still immediate tho

timezone aware - respect working hours (9-6 in user tz)
queue stuff outside hours, deliver later

better content - show task title + preview, who did it, action buttons

MIKE'S TECH NOTES:
"need async queue, sync is killing us"
- move to redis (we already use it)
- notification worker processes queue
- 3-4 weeks to implement

db changes needed:
"user_preferences table is 42 boolean columns, doesnt scale"
wants jsonb column instead
showed example schema (urgent/important/fyi with channels, digest settings, quiet hours)

migration = 2 weeks, cant flip switch, need gradual rollout
default existing users to "all = important"

"async will IMPROVE performance, notifs are slowest api ops"

CONCERNS from team:

jordan: UI will be complex
- 3 tiers, channels, digest, quiet hours = lots of settings
- needs progressive disclosure (simple + advanced modes)
- "need to design carefully or users confused"

sarah: how do we educate users about changes?
- announcement needed
- migration guide
- in-app messaging?
also timeline concern - 6 weeks min (eng + design + testing)
"competes with mobile app launch in Q1"

alex: mobile is different than email
- push has char limits
- ios/android handle differently
- needs mobile-specific design

jamie: what if redis goes down?
- notifications disappear?
- need durable queue (sqs?) or persistence
mike: "can use redis AOF or move to sqs, ill spec it"

me: backward compat? legacy mode?
sarah: "no, too complex to maintain 2 systems"

OPEN QUESTIONS:
1. how determine urgent vs important vs fyi? user configurable?
2. slack notifications - follow email rules or always urgent?
3. preferences global or per-project? both?
4. a/b test approach? 10% rollout first?
5. rollback plan if this breaks?

DECISIONS:
✓ moving forward with 3-tier system (unanimous)
✓ async queue (mike to spec redis vs sqs)
⏸ timeline Q1 or Q2? sarah wants detailed plan, decide by eow
⏸ per-project prefs = v2, start with global
⏸ a/b testing needs data team input

ACTION ITEMS:
- me: comprehensive PRD by fri oct 11
- mike: tech spec (arch, db schema, migration) by fri oct 11
- jordan: ux flows + wireframes by mon oct 14
- alex: mobile considerations doc by mon oct 14
- jamie: eng estimate breakdown by tues oct 15
- me: competitive analysis (asana/linear/clickup) by tues oct 15
- sarah: schedule followup meeting wed oct 16 3pm

=== Q1 PRIORITIZATION ===

sarah leading this discussion

5 initiatives competing for Q1:
1. mobile app (committed, non-negotiable)
2. dark mode (highly requested)
3. notification redesign (discussed above)
4. template library (activation play)
5. enterprise features (sso, permissions)

CAPACITY:
12 engineers total
4 on mobile til launch
8 available for web
2 week sprints = 6 sprints in Q1

ESTIMATES:
mobile = 4 sprints (in progress)
dark mode = 2 sprints
notifications = 3 sprints
templates = 3 sprints
enterprise = 4 sprints

math: can do ~2 major projects (plus mobile) with 8 engineers

sarah's criteria:
1. okr impact (activation, retention, revenue)
2. customer demand
3. competitive pressure
4. team morale
5. tech dependencies

DISCUSSION:

dark mode:
mike: "team really wants this, morale boost"
jordan: "design mostly done"
alex: "launch on web + mobile simultaneously? branding opp"
sarah: "feels like Q1 candidate"

notifications:
me: "127 tickets, real pain point"
sarah: "blocking new users/revenue or just annoyance?"
me: "both, enterprise mentions in sales calls"
mike: "tech debt too, slowing api"
sarah: "if not Q1, definitely Q2"

templates:
me: "directly addresses activation okr"
jordan: "users stare at blank screen, templates solve that"
jamie: "3 sprints maybe 4 with versioning"
sarah: "move activation 45% to 60%? thats huge jump"
me: "prob not alone, need onboarding + templates"
alex: "mobile needs templates too, adds scope"

enterprise:
sarah: "losing deals without sso/permissions"
mike: "enterprise avg $15k vs smb $5k, 3x!"
me: "but slow sales cycle, wont impact Q1 revenue"
sarah: "building pipeline for Q2/Q3"

SARAH'S STRAWMAN:
Q1: mobile + dark mode + templates
Q2: notifications + enterprise

rationale: dark mode quick/visible/team wants it, templates = okr

PUSHBACK:

mike: "worried about tech debt if we dont fix notifs"
"can we at least do async queue in Q1 even if not full redesign?"
sarah: "split it? infra Q1, ux Q2?"
mike: "yes, buys performance + sets up Q2"

jamie: "templates 3-4 sprints if mobile needs it too"
alex: "mobile launches late Q1, could do web Q1, mobile Q2?"
sarah: "works, web first"

REVISED PLAN:
Q1:
- mobile (4 sprints, 4 eng)
- dark mode (2 sprints, 3 eng, web+mobile)
- templates (3 sprints, 3 eng, web only)
- notif infrastructure (1 sprint, 2 eng, async queue only)

Q2:
- notif ux redesign (2 sprints)
- templates mobile (1 sprint)
- enterprise features (4 sprints)

consensus: feels achievable, sarah will finalize

=== ENTERPRISE FEEDBACK ===

sarah summarizing recent sales calls + customer interviews

common requests:
- advanced sso (saml variants, okta, azure ad)
- detailed audit logs
- data residency (eu/us servers)
- custom contracts
- dedicated support / slas
- admin analytics (usage tracking)

deal blockers:
- no soc2 (we're working on it)
- no eu datacenter
- audit logs dont meet compliance

pipeline:
- 12 enterprise deals (avg $15k each)
- 3 blocked by sso
- 2 blocked by compliance/audit

sarah: "enterprise = longer game, invest Q2/Q3 for Q3/Q4 revenue"

=== SPRINT 23 PREVIEW ===

jamie presenting

sprint starts mon oct 14

planned:
- mobile: polish + bug fixes (close to launch!)
- dark mode: color system refactor (foundation)
- onboarding: a/b test results
- performance: search optimization
- bug fixes: 8 P0s in backlog

team availability:
jamie out oct 21-25 (vacation)
mobile full capacity
web has 2 sprint capacity

goal: "prepare foundation for Q1 priorities"

=== PARKING LOT ===

- api v2 planning (sarah to schedule)
- marketing wants dark mode launch campaign (hold til Q1)
- github integration issue escalated (alex investigating)
- competitor "motion" launched ai features (need to check out)

=== NEXT MEETINGS ===

wed oct 9: design review (dark mode mockups)
thu oct 10: sprint 23 planning
wed oct 16: notification go/no-go
fri oct 18: Q1 roadmap finalization

meeting done 3:32pm
