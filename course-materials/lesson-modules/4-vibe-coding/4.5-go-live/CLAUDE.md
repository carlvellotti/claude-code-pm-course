# 4.5 Go Live

This is it. The final step.

Your quiz is built, polished, and saved to GitHub. Now we put it on the internet so anyone can visit it.

Developers call this "deploying" - you're deploying your app to the web. You'll hear that word a lot.

STOP: Ready to go live?

USER: Yes

---

Vercel is a free service that puts your code on the internet.

It's basically the home base of vibecoding.

You give it your GitHub project, and it turns it into a real website with a real URL.

It's made by the same people who make Next.js (the framework we used), so they work together perfectly.

STOP: Sound good?

USER: Yes

---

First, you need a Vercel account.

STOP: Want me to open vercel.com for you? I recommend signing up with your GitHub account - it makes everything connect automatically.

USER: Yes / I'll do it myself

ACTION: If they want it opened, run: `open https://vercel.com`

STOP: Let me know when you've created an account. Make sure to sign up with GitHub!

USER: Done

---

Just like with GitHub, I'm going to download tools that let me work with Vercel directly.

This will open your browser to log in - just follow the prompts.

ACTION: Set up Vercel CLI:

1. Check if already installed:
```
vercel --version
```

2. If NOT installed:
```
npm i -g vercel
```

3. Once installed, authenticate (run in background to avoid blocking):
```bash
vercel login > /tmp/vercel-auth.log 2>&1 &
sleep 3
cat /tmp/vercel-auth.log
```

4. Read the output to get the device URL with code, then open it:
```bash
open "https://vercel.com/oauth/device?user_code=[CODE FROM OUTPUT]"
```

5. Tell user: "I just opened Vercel in your browser. Click Authorize, then let me know when you're done."

STOP: Let me know when you've authorized it.

USER: Done

ACTION: Verify authentication worked:
```bash
vercel whoami
```

If successful, continue. If not authenticated, troubleshoot:
- They may not have completed the browser flow - ask them to try again
- The background process may have timed out - run the login command again

---

Now let's put your quiz on the internet.

ACTION: Deploy to Vercel:

1. Navigate to the quiz-project folder:
```
cd [path to quiz-project]
```

2. Deploy to production:
```
vercel --prod --yes
```

The `--yes` flag accepts all the defaults so you don't have to answer questions. The `--prod` flag means it goes live immediately.

Wait for the deploy to complete - it takes about a minute. Watch for the URL in the output.

Vercel is building your quiz and putting it on the internet now...

Done! Look for the URL in the output - it'll look something like `quiz-project-abc123.vercel.app`.

---

Your URL is: [Copy the URL from the deploy output]

That's YOUR website. On the real internet. Anyone can visit it.

Let me open it for you.

ACTION: Open the deployed URL in the browser using bash open

STOP: Do you see your quiz live on the internet?

USER: Yes!

---

Open that URL on your phone. It should work there too - same quiz, any device.

STOP: Does it work on your phone?

USER: Yes!

---

Now for the real test: send that link to a friend. Text it to someone right now. When they react, that's the feeling of shipping something real.

Let's acknowledge what just happened.

You built a real web application. You put it on the internet. You have a URL that works on any device. You did this without writing a single line of code yourself.

That's vibecoding. That's the future.

STOP: How does that feel?

USER: [Response]

---

Here's what you now know:

**Plan** → Get clear on what you're building
**Build** → Let AI create it
**Iterate** → Refine until it's right
**Save** → Back it up to GitHub
**Go Live** → Put it on the internet (deploy)

This is the loop. You can build anything with this loop.

STOP: Make sense?

USER: Yes

---

One more thing: what if you want to update your quiz later?

Here's the flow: make changes on your computer, ask me to "push to GitHub," and Vercel will automatically update your live website.

That's it. Vercel watches your GitHub and auto-deploys whenever you push changes. Magic.

STOP: Pretty cool, right?

USER: Yes

---

What if you wanted to collect emails from people who take the quiz? You'd need a database to save them. That's a future module.

What if you wanted to make sure it doesn't break? You'd need testing. Also a future module.

What if you wanted a custom domain like yourquiz.com? Totally doable - Vercel makes it easy.

The point is: you now have the foundation. Everything else builds on this.

STOP: Feeling empowered?

USER: Yes

---

Want to build something else? Start a new project folder and follow this same process.

The main things to tell Claude: you want to deploy on Vercel, and that it has Vercel CLI access. It'll know what to do.

STOP: Any ideas brewing?

USER: [Response]

---

## Quick Plugs

**To catch future modules:** Subscribe to the Claude Code for PMs newsletter at ccforpms.com. That's also where you'll find in-depth guides and a community of PMs using Claude Code.

STOP: Want me to open that site so you can subscribe?

USER: Yes / No

ACTION: If yes, open https://ccforpms.com in browser

This course was created by Carl Vellotti. If you have feedback, questions, or just want to say hi, he's always happy to hear from you: [X](https://x.com/carlvellotti) / [LinkedIn](https://www.linkedin.com/in/carlvellotti/)

If you enjoyed this, share it with friends and coworkers who could use these skills!

---

**Module 4 Complete!**

You went from zero to deployed web app. You learned planning, building, iteration, GitHub, and going live.

This is vibecoding. This is your new superpower.

**What's next:** Future modules will cover databases, APIs, more complex apps, and connecting Claude to everything. But you now have the core skill - you can build and ship things.

In the meantime, try building something for yourself. The best way to learn is to make something you actually want.

STOP: Thanks for building with me. Now go make something cool.

USER: (exits or explores)

---

## Important Notes for Claude

- The `vercel --prod --yes` flags are critical - `--yes` skips all interactive prompts, `--prod` deploys to production immediately
- Vercel auto-connects to the GitHub repo they created in 4.4 - this is why signing up with GitHub was important
- The URL format is usually `[project-name]-[random].vercel.app`
- Auto-deploy is set up automatically when they link GitHub during Vercel signup
- If deploy fails, common issues:
  - Build errors → Check the Vercel dashboard for logs
  - Not in the right directory → Make sure you're in quiz-project
- The celebration moment (sending to a friend) is crucial - let it breathe, don't rush past it

## Success Criteria

- User has a Vercel account (connected to GitHub)
- Vercel CLI is installed and authenticated
- Quiz is deployed and live on the internet
- User can access the quiz from their phone
- User has sent the link to at least one other person
- User understands the Plan → Build → Iterate → Save → Go Live loop
- User knows how to update: make changes → push to GitHub → auto-deploys
- User feels empowered to build more things
