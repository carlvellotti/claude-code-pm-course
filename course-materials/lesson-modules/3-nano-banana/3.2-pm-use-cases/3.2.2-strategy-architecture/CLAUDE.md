# Module 3.2.2: Strategy & Architecture Visuals

Welcome to Module 3.2.2: Strategy & Architecture Visuals!

Your TaskFlow Mobile pitch was a hit - leadership is excited. But now different stakeholders want deeper dives.

The CTO wants to understand the technical architecture. The CEO wants to see feature prioritization. And the board wants to see the product roadmap.

You need visuals that communicate complex ideas clearly. Let's build them.

STOP: Ready to prep for your stakeholder meetings?

USER: Ready

---

Quick reminder: you can reference styles from `style-library.html` or just describe what you want.

The **Architecture** and **Framework** categories have great options for this module.

STOP: Makes sense?

USER: Yes

---

## Part 1: System Architecture (CTO Meeting)

First up: the CTO meeting.

The CTO wants to understand how TaskFlow Mobile fits into the existing TaskFlow ecosystem. Let's create a system architecture diagram showing:

- **TaskFlow Mobile app** - the new thing we're building
- **TaskFlow Backend API** - the existing backend
- **Database layer** - PostgreSQL for data, Redis for caching
- **Third-party integrations** - push notifications, analytics
- **Data flow** - how information moves between components

This is the kind of diagram that answers "how does it all connect?"

STOP: Ask me to create a system architecture diagram for TaskFlow Mobile.

USER: Create a system architecture diagram / Generate the architecture diagram

ACTION: Generate system architecture diagram
- TaskFlow Mobile connecting to TaskFlow Backend API
- Backend connecting to PostgreSQL database and Redis cache
- Third-party services: push notifications (Firebase), analytics (Mixpanel)
- Show data flow arrows between components
- Clean, technical style suitable for engineering review (style #34 or similar)
- 16:9 aspect ratio
- Save to outputs folder with descriptive name

ACTION: Provide the path to the output image so user can view it.

Check the `outputs/` folder for your architecture diagram.

STOP: Does this clearly show how the pieces connect?

USER: Response

ACTION: If user wants changes, iterate on the diagram. If satisfied, continue.

The CTO can now see exactly how TaskFlow Mobile integrates with the existing system.

This same approach works for ANY diagram you need - system architecture, data flows, org charts, network topology, whatever. Just describe your components and how they connect.

STOP: Ready for the CEO meeting?

USER: Yes

---

## Part 2: Strategy Framework (CEO Meeting)

Next: the CEO meeting.

The CEO wants to see how you're prioritizing features - what gets built first and why. A 2x2 matrix is perfect for this: **Impact vs Effort**.

Let's map out the key features for TaskFlow Mobile:

- **Quick Wins** (High Impact, Low Effort): Push notifications for task updates, offline task viewing
- **Major Projects** (High Impact, High Effort): Real-time sync across devices, team chat integration
- **Fill-ins** (Low Impact, Low Effort): Custom themes, widget support
- **Avoid** (Low Impact, High Effort): Voice command support, AR task visualization

STOP: Ask me to create a 2x2 prioritization matrix for TaskFlow Mobile features.

USER: Create a prioritization matrix / Generate the 2x2 matrix

ACTION: Generate 2x2 prioritization matrix
- X-axis: Effort (Low → High)
- Y-axis: Impact (Low → High)
- Four quadrants labeled: Quick Wins, Major Projects, Fill-ins, Avoid
- Plot the features mentioned above in appropriate quadrants
- Clean corporate style suitable for executive presentation (style #5 or similar)
- 1:1 or 16:9 aspect ratio
- Save to outputs folder with descriptive name

ACTION: Provide the path to the output image so user can view it.

Check the `outputs/` folder for your prioritization matrix.

STOP: See how the matrix makes the prioritization logic visual and clear?

USER: Response

ACTION: If user wants changes, iterate on the matrix. If satisfied, continue.

Now the CEO can see at a glance what you're building first and why.

And this works for ANY framework you can imagine - 2x2 matrices, pyramids, Venn diagrams, canvases, funnels, whatever. Same process: describe the structure, list what goes where, specify the style. You can reference the style library or describe what you want from scratch.

STOP: Ready for the board meeting?

USER: Yes

---

## Part 3: Product Roadmap (Board Meeting)

Finally: the board meeting.

The board wants to see the big picture - when does this ship and what's the phased rollout?

Let's create a roadmap showing TaskFlow Mobile over 3 quarters:

- **Q1: MVP Launch** - Core task management, push notifications, offline viewing
- **Q2: Team Features** - Real-time sync, team chat integration, shared task lists
- **Q3: Enterprise** - Admin controls, SSO integration, advanced analytics

This shows a clear path from MVP to enterprise-ready.

STOP: Ask me to create a product roadmap for TaskFlow Mobile.

USER: Create a product roadmap / Generate the roadmap

ACTION: Generate product roadmap visualization
- Timeline showing Q1, Q2, Q3
- Each quarter with key milestones/features
- Q1: MVP (core features)
- Q2: Team features (collaboration)
- Q3: Enterprise (admin/security)
- Clean, modern style suitable for board presentation (style #88 or similar)
- 16:9 aspect ratio
- Save to outputs folder with descriptive name

ACTION: Provide the path to the output image so user can view it.

Check the `outputs/` folder for your roadmap.

STOP: Does this tell a clear story of how the product evolves?

USER: Response

ACTION: If user wants changes, iterate on the roadmap. If satisfied, continue.

The board can now see the strategic vision laid out over time.

This works for ANY timeline or sequence you need - roadmaps, Gantt charts, release plans, migration schedules. Define your time periods, list what goes in each, describe the style. Same process every time.

STOP: One more thing before we wrap up.

USER: Yes

---

## Growing Your Style Library

Remember: you can always add your own styles to the style database.

Found a diagram style you love online? Extract it and save it. Created something in this module that worked really well? Add it to your library.

A great source for framework and diagram inspiration is **https://slidemodel.com/** - find a style you like, screenshot it, and use style extraction to clone it for your own purposes.

Over time, you'll build a collection of go-to styles for every situation.

If you need a refresher on how to add styles, revisit Module 3.1.4.

STOP: Makes sense?

USER: Yes

---

## Wrap-Up

Let's recap what you just built:

1. **A system architecture diagram** for the CTO
2. **A 2x2 prioritization matrix** for the CEO
3. **A product roadmap** for the board

Three different stakeholders, three different visual needs - all handled.

These techniques work for any strategic or technical communication:
- Architecture reviews
- Strategy presentations
- Planning sessions
- Board updates

STOP: Any questions before we move on?

USER: Questions or ready to continue

---

In the next module, we'll tackle marketing and announcement visuals - ads, feature graphics, and launch assets.

Type `/start-3-2-3` to continue.

---

## Important Notes for Claude

- **File paths:** Always provide absolute paths when telling users where to find files.
- **Image generation:** Use the `image_gen.py` module via Python. Start a new session at the beginning of each major generation to keep sessions clean.
- **Style library:** If user references a style number, look up the prompt in `style-library.html` (in the 3.1.4 module folder).
- **Iteration:** If any image doesn't turn out well, offer to regenerate or refine it. Use the session to iterate.
- **Output naming:** Use descriptive names like `taskflow_system_architecture.png`, `feature_prioritization_matrix.png`, `product_roadmap_q1_q3.png`.
- **Technical accuracy:** For the architecture diagram, ensure the components and connections make logical sense for a mobile app backend.
- **Opening images:** If a user is having trouble finding an image, offer to open it for them using `open [path]` (Mac) or `start [path]` (Windows).

## Success Criteria

The module is complete when the user has:
- [ ] Generated a system architecture diagram showing TaskFlow Mobile's technical stack
- [ ] Generated a 2x2 prioritization matrix with features plotted by impact/effort
- [ ] Generated a product roadmap showing 3-quarter phased rollout
- [ ] Understands they can add custom styles to their library (callback to 3.1.4)
- [ ] Understands these techniques apply to any strategic/technical visual need
