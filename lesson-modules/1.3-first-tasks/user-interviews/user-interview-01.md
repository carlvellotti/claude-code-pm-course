# User Interview #1: Enterprise Admin Persona

**Participant:** Rachel Kim
**Role:** Director of IT Operations
**Company:** FinanceTech Solutions (650 employees, Series C)
**TaskFlow Plan:** Enterprise (pilot with 100 users)
**Date:** October 5, 2024
**Interviewer:** Senior PM
**Duration:** 35 minutes

---

## Background

Rachel has been at FinanceTech for 4 years, leading IT operations. Her team manages 30+ tools across the organization. They're currently piloting TaskFlow with their product and engineering teams (100 users). Evaluating whether to roll out company-wide.

---

## Interview

**Q: Tell me about your current project management setup before TaskFlow.**

Rachel: "Oh boy. It's a mess, honestly. Engineering uses Linear, product team was on Asana, marketing uses Monday.com, and sales has their own thing in Salesforce. Everyone wanted something different. My team spends so much time just managing access and trying to get visibility into what's actually happening."

**Q: What made you consider TaskFlow?**

Rachel: "We needed to consolidate. Too many tools, too many logins, too much chaos. When someone leaves the company, we have to remember to revoke access in like 15 different places. It's a nightmare. TaskFlow's SSO integration was the main draw - we can provision and deprovision from our identity provider."

**Q: How's the pilot going so far?**

Rachel: "Pretty good! The product and engineering teams are happy with it. They like the interface - it's clean, fast. But I need more from the admin side. The audit logs are basic - I need more detail. Like, who exported data? Who changed permissions? That kind of thing. Compliance team asks for this stuff."

**Q: What would make you roll this out company-wide?**

Rachel: "Better admin controls. Right now I can see high-level usage, but I want to see exactly who's using it, who's not, what features they're using. Cost allocation too - we charge back to departments, so I need to know which team is using how much. Also, the permission system is good but we need more granularity. Like, read-only access for certain projects, or limit who can invite external users."

**Q: Any features you wish TaskFlow had?**

Rachel: "Dark mode. Sounds silly, but our engineering team asks about it constantly. They work late, they want dark mode. Also, better mobile app - the mobile web version is okay but not great. Our field teams would use this if the mobile experience was better."

**Q: What about the onboarding experience?**

Rachel: "Honestly? It's fine for power users but confusing for casual users. We had to create our own onboarding guide. Some kind of template library would help - like 'here's a pre-built project, start with this.' People stare at a blank screen and don't know what to do. We need to hold their hand more at the beginning."

**Q: How does TaskFlow compare to your previous tools?**

Rachel: "Pricing is better than Asana - we're saving like 40%. Performance is way better than Monday.com - that thing is so slow. The SSO integration is easier than most tools. But enterprise features are still catching up. We need things like data residency options, more compliance certifications, custom contract terms. You're not quite ready for a Fortune 500 deployment yet."

**Q: Anything else we should know?**

Rachel: "The support team is responsive, that's great. The product updates frequently - that's good but also a little concerning. We need stability. Maybe a slower release cycle for enterprise customers? Or an LTS version? Also, documentation for admins could be better. I had to figure out a lot through trial and error."

---

## Key Insights
- SSO was primary driver for adoption
- Needs more detailed audit logs for compliance
- Permission system needs more granularity
- Cost allocation/usage tracking important for enterprise
- Dark mode highly requested by engineering team
- Onboarding needs help (template library suggestion)
- Mobile web experience not good enough
- Enterprise customers need stability over rapid updates
