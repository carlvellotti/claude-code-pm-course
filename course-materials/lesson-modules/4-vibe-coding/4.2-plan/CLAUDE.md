# 4.2 Plan

Before we build, we need to get clear on what we're building.

This is called "requirements" - basically a description of how your quiz should work and look.

STOP: Have you ever given someone vague instructions and gotten something totally different than you expected?

USER: Yes / Definitely

---

That's what happens when you skip requirements. The more detail we figure out now, the better I can build what you actually want.

I'm going to interview you about your quiz. We'll figure out the personality-to-coffee pairings, the style, the questions. Then I'll save it all to a file so we have a clear spec to build from.

STOP: Think of this like briefing a contractor before they start work. The clearer the brief, the better the result. Ready to start?

USER: Yes

---

I'm going to use a tool called AskUserQuestion - it gives you nice buttons to pick from instead of typing. You can ask me to use this anytime you want a cleaner way to make decisions. Just say "ask me" or "give me options."

Let's try it now.

ACTION: Use AskUserQuestion with two questions:
- Q1 Header: "Results" / Question: "How many personality/coffee pairings should your quiz have?" / Options: "3 - Simple and focused", "4 - Good variety (Recommended)", "5 - More distinctions", "6 - Maximum variety"
- Q2 Header: "Question vibe" / Question: "What style of questions do you want?" / Options: "Fun pop culture (Harry Potter, Netflix, etc.)", "Lifestyle & preferences (travel, food, weekends)", "Abstract & quirky (colors, scenarios, hypotheticals)", "Mix of everything"

USER: [Selects options]

Great choices! Now let's pick your actual personality-to-coffee pairings.

---

Remember: the quiz recommends a COFFEE based on personality. So we need to decide which personalities map to which drinks.

Here are 10 pairing ideas. Pick [X] based on how many results you chose earlier. Just type the numbers, like "1, 4, 7":

1. **Bold Adventurer** → Double Espresso - "You live for intensity"
2. **Cozy Classic** → Medium Roast Drip - "Comfort in every cup"
3. **Sweet Enthusiast** → Caramel Latte - "Life's too short for bitter"
4. **Zen Minimalist** → Black Coffee, Single Origin - "Simple. Clean. Perfect."
5. **Social Butterfly** → Cappuccino - "Coffee is better with company"
6. **Night Owl** → Red Eye (coffee + espresso shot) - "Sleep is optional"
7. **Health Nut** → Oat Milk Americano - "Wellness in every sip"
8. **Artisan Snob** → Pour-Over, Single Origin - "You know what you like"
9. **Practical Pragmatist** → Large Drip, Whatever's Fresh - "Just make it work"
10. **Indulgent Treat** → Mocha with Whip - "Coffee is dessert"

STOP: Type the numbers you want (e.g., "1, 3, 5, 8")

USER: [Types numbers]

ACTION: Note their selections for use in REQUIREMENTS.md

---

Perfect! Now we need to figure out the "logic."

Logic is the behind-the-scenes rules for how something works. If users do X, what happens? If they click this, what do they see? It's the "if this, then that" of your product.

Every app, website, or tool has logic. When you're planning something, you always need to think through how it should actually behave. I can help you brainstorm options.

Here's how this quiz will work: each question has answers, and each answer maps to one of your personalities. At the end, we tally up which personality got picked most.

The question is: how do we show the result? Two options:

**Option A: Single recommendation** - "You're a Bold Adventurer! Try our Double Espresso."

**Option B: Show all percentages** - "You're 50% Bold Adventurer, 30% Cozy Classic, 20% Sweet Enthusiast" with all the coffee recommendations.

STOP: Which do you prefer - single recommendation (A) or show percentages (B)?

USER: [Responds A or B]

ACTION: Note their choice for REQUIREMENTS.md

Great choice! So if someone's answers map to "Bold Adventurer" 3 times and "Cozy Classic" 2 times:

[If they chose A]: They get "You're a Bold Adventurer! Your coffee: Double Espresso."

[If they chose B]: They see all their results with percentages and can explore all the coffee recommendations.

The questions just reveal which personality fits them best.

STOP: Make sense?

USER: Yes

---

Now for the fun part - how should it LOOK?

I'm going to generate a few different visual styles as preview pages and open them in your browser.

STOP: Ready to see some style options?

USER: Yes

ACTION: Generate 3-4 HTML style preview files with different aesthetics:
- Style 1: Playful/colorful (bright colors, rounded shapes, fun fonts)
- Style 2: Minimal/clean (lots of whitespace, simple typography)
- Style 3: Bold/dramatic (dark backgrounds, high contrast, strong typography)
- Style 4: Warm/cozy (earth tones, soft gradients, inviting feel)

Each preview should show a sample quiz card with a question and answer options. Save them to the quiz-project folder as style-preview-1.html, style-preview-2.html, etc.

ACTION: Open all preview files in the browser using bash open commands

Take a look at those previews in your browser. Each tab is a different style.

STOP: Which style do you like best? You can pick one, or tell me what to mix - like "I like the colors from #2 but the layout from #3"

USER: [Responds with preference]

ACTION: Note their style preference. If they want to mix elements, clarify what specifically they want combined.

---

One more visual question: do you want images in your quiz?

You could have a picture for each coffee result - like a photo of espresso for "Bold Adventurer."

I can search the web and download images for you - but heads up, it takes a bit of time since I have to search, find good ones, and download them.

Alternatively, we can skip images for now and add them later once the quiz is working.

STOP: What do you prefer - images (takes longer) or skip for now?

USER: [Responds]

ACTION: Based on their choice:

If they want IMAGES:
- Ask what images they want for each result (e.g., "espresso shot", "cozy latte", "iced coffee")
- For each image:
  1. Web search for the image (e.g., "espresso shot unsplash")
  2. Fetch a result page to find direct image URLs
  3. Download using curl to public/ folder in quiz-project
- Note: Unsplash is best for stock photos (free, high quality).

If they want to SKIP:
- Move on - can always add images later during iteration

---

One more thing: do you want icons next to each answer option? Like a little sword icon for "Gryffindor" or a moon for "Night vision"?

Icons make the quiz feel more polished and visual, but we can also keep it text-only if you prefer a cleaner look.

STOP: Icons or no icons?

USER: [Responds]

ACTION: Note their choice for REQUIREMENTS.md

---

Last part - the actual questions people will answer.

You chose "[their vibe choice from earlier]" style questions, so I'll generate 5-7 questions that match that vibe. Each question will have answers that map to your different personalities.

Of course, you can always come up with your own questions too - just tell me what you want and I'll make it happen.

ACTION: Generate 5-7 quiz questions matching their vibe choice:
- If "Fun pop culture": Harry Potter houses, Netflix shows, fictional characters, movie genres, etc.
- If "Lifestyle & preferences": weekend activities, travel styles, food choices, social preferences, etc.
- If "Abstract & quirky": colors, hypothetical scenarios, random objects, desert island choices, etc.
- If "Mix of everything": 2-3 from each category

Each question should have answers that clearly map to the personalities they selected. For example, if they picked Bold Adventurer and Cozy Classic, answers should lean toward intensity vs. comfort.

Here are my suggestions. Take a look - each answer is designed to map to one of your personalities.

STOP: What do you think? Good as-is, want changes, or want to write your own?

USER: [Approves or suggests changes]

ACTION: Adjust questions based on feedback. If they want to write their own, help them map answers to personalities.

---

Perfect! We've got everything we need. Let me save all of this to a requirements file.

ACTION: Create REQUIREMENTS.md in the quiz-project folder with:
- Personality→Coffee pairings (all selected ones with taglines)
- Result display style (single or percentages)
- Visual style description
- Image/icon decision
- All quiz questions with answer-to-personality mappings

Done! Open REQUIREMENTS.md and take a look. This is the spec I'll build from.

STOP: Does everything look right?

USER: Yes / [Corrections]

ACTION: Make any corrections if needed

---

**What you just learned:** How to define clear requirements before building - specifically for a recommendation engine.

**Where else this applies:**
- Briefing a designer or developer on any project
- Writing a product spec or PRD
- Planning any creative project - the clearer the vision, the better the result
- Working with AI tools - the more specific you are, the better the output

**Next up:** In 4.3, we actually BUILD this thing. You'll watch me create your quiz from scratch based on these requirements. This is where the magic happens.

STOP: Ready for 4.3? Say "let's build" or type /start-4-3

USER: Let's build

---

## Important Notes for Claude

- The AskUserQuestion tool should be used for the initial batched questions ONLY - after that, use regular conversation
- When generating style previews, make them actually visually distinct - don't just change colors slightly
- For images: Unsplash works great for stock photos, but always check the URL actually returns an image before downloading
- The REQUIREMENTS.md file is crucial - it's the spec for 4.3. Make sure it's complete and clear.
- If users want to mix styles, get specific about what elements from each
- Adjust the number of questions based on their pairing count (more pairings = more questions needed to differentiate)

## Success Criteria

- User has selected their personality→coffee pairings
- User has chosen result display style (single vs percentages)
- User has selected a visual style
- User has made a decision on images/icons/skip
- User has approved quiz questions
- REQUIREMENTS.md exists with all the above documented
- User is excited to build
