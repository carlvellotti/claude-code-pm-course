# 4.3 Build & Iterate

This is it. Time to build your quiz.

I'm going to handle all the technical setup. You just watch the magic happen.

STOP: Ready?

USER: Yes

---

First, I need to set up the project structure - this creates all the starter files we need.

ACTION: Run the following command in the quiz-project folder:
```
npx create-next-app@latest . --typescript --tailwind --eslint --app --no-src-dir --import-alias "@/*" --yes
```
(The --yes flag accepts all defaults automatically)

Done! Look at your file explorer - you should see a bunch of new files in the quiz-project folder.

Don't worry about understanding all of them. The `app/` folder is where your quiz will live. Everything else is just configuration.

STOP: Do you see the new files?

USER: Yes

---

Before I build, let me show you something useful: plan mode.

For big tasks, it helps to see what I'm going to do before I do it. Press **Shift+Tab** to switch modes - you should see "Plan mode" as an option.

STOP: Switch to Plan mode and let me know when you're there.

USER: In plan mode

Perfect. Plan mode means I'll show you my plan, you approve it, then I execute. Let's do it.

STOP: Ask me to build the quiz based on the requirements.

USER: Build my quiz based on REQUIREMENTS.md

ACTION: Read REQUIREMENTS.md, then create a plan showing:
- Components to create (quiz page, question component, results page)
- Styling approach based on their chosen style
- Quiz logic implementation (how answers map to results)
- Any images/icons to include

Present the plan clearly with bullet points.

Here's my plan. I'll create the quiz page, the question components, the results page, and style everything according to your preferences.

STOP: Does this look right? Any questions before I start?

USER: Looks good / [Questions]

ACTION: Answer any questions they have, then tell them to switch back to normal mode (Shift+Tab) and you'll execute the plan.

---

Building now. This takes a minute or two. You'll see me creating and editing files. Just let me work.

ACTION: Build the full quiz application based on REQUIREMENTS.md:
1. Create the main quiz page in app/page.tsx
2. Create quiz components (QuizQuestion, Results, etc.)
3. Implement the quiz logic (tracking answers, calculating results)
4. Apply the visual style they chose
5. Add any images/icons based on their preference
6. Make sure the result display matches their choice (single vs percentages)

Take your time and build it properly. This is the core deliverable.

Done! Your quiz is built. Now let's see it in action.

---

I'm going to start your quiz running and open it in your browser.

ACTION: Run `npm run dev` in background in the quiz-project folder

ACTION: Wait a few seconds for the server to start, then bash open http://localhost:3000 in browser

Your quiz should now be open in your browser!

This "localhost" link only works on YOUR computer - it's a temporary local version. We'll make it public later when we deploy.

STOP: Do you see your quiz?

USER: Yes! / [Issues]

ACTION: If they have issues:
- Browser didn't open → Tell them to manually go to http://localhost:3000
- Build errors → Check the terminal output, fix errors
- Blank page → Check for JavaScript errors in browser console

---

Look at that! You have a working quiz!

Take it for a spin - answer the questions and see your result.

STOP: Try the quiz. Does it work? Do you get a result at the end?

USER: Yes it works! / [Something's wrong]

ACTION: If something's wrong, debug together. Common issues:
- Result not showing → Check the logic implementation
- Wrong personality mapping → Review the answer mappings
- Style issues → Can fix in iteration

This is normal - first versions often need fixes. Let's get it working first, then polish.

Amazing! You just built a web app. Let that sink in.

---

The first version is never perfect. Let's iterate - make 2-3 changes until you love it.

Here's a trick: you can take a screenshot, paste it here with **Ctrl+V** (not Cmd+V on Mac!), and tell me what to change.

Circle something, point at it, whatever - just show me what you want different.

This is also a great way to show me bugs. If something looks wrong, screenshot it and paste it here.

If you're not sure what to change, here are some ideas:
- Add confetti or animation when you get your result
- Change the colors or fonts
- Tweak the wording on questions or results
- Add images for each result
- Change the layout or spacing
- Add a progress bar

STOP: Take a screenshot of your quiz, paste it with Ctrl+V, and tell me what you'd like to change.

USER: [Pastes screenshot and describes change]

ACTION: Make the requested change to the code

Done! Refresh your browser to see the update.

STOP: How's that? Want to change anything else?

USER: [More changes / Happy with it]

ACTION: Keep iterating until they're satisfied. 2-3 rounds is typical. Common requests:
- Visual tweaks (colors, spacing, fonts)
- Animation additions
- Wording changes
- Layout adjustments

---

Look at that - it's YOUR quiz, exactly how you want it.

This is the iteration loop: screenshot → describe → change → refresh → repeat.

This is how real product development works. And with AI, each iteration takes seconds instead of days.

STOP: Happy with how it looks?

USER: Yes

---

**What you just learned:** How to go from requirements to working product, then iterate until it's exactly what you want.

**Where else this applies:**
- Building any web project - landing pages, tools, prototypes
- Testing ideas quickly before investing in "real" development
- Working with designers/developers - clear visual feedback speeds everything up

**Next up:** In 4.4, we save your code to GitHub. Right now it only exists on your computer. We're going to put it in the cloud so it's backed up and ready for deployment.

STOP: Ready to save your work? Say "let's do GitHub" or type /start-4-4

USER: Let's do GitHub

---

## Important Notes for Claude

- The `npm run dev` command should run in background so the user can keep talking
- localhost:3000 is the default Next.js port - if something's already using it, Next.js will suggest another port
- When they paste screenshots, actually look at them and make specific changes
- The Ctrl+V note is important - Mac users often try Cmd+V first
- Keep iterations focused - don't suggest too many changes at once
- If the quiz has bugs, fix them before moving to visual polish
- Plan mode (Shift+Tab) is a real Claude Code feature - make sure they actually use it

## Success Criteria

- Next.js project is scaffolded in quiz-project folder
- Quiz is fully built based on REQUIREMENTS.md
- Dev server is running and quiz is viewable at localhost:3000
- User has done at least 1-2 iterations
- User is satisfied with how their quiz looks
- User is ready for GitHub
