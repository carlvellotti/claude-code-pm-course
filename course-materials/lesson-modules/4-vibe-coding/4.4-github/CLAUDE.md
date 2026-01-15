# 4.4 GitHub

Right now, your quiz only exists on your computer.

If your laptop stops working or you delete the files, it's gone. And we can't put it on the internet yet.

We need to save it to the cloud first. That's what GitHub is for.

STOP: Have you used GitHub before?

USER: Yes / No / A little

---

GitHub is like Google Drive, but for code.

It saves your code to the cloud, keeps a history of every change, and lets you undo mistakes.

It's also how we'll get your quiz onto the internet - the service we use needs to grab your code from somewhere.

Your project on GitHub is called a "repository" (or "repo" for short). You'll hear developers use that word a lot.

STOP: Make sense?

USER: Yes

---

First, you need a GitHub account.

STOP: Do you have a GitHub account? If not, I can open the signup page for you.

USER: I have one / Open it for me / I'll do it myself

ACTION: If they want it opened, run: `open https://github.com` (or bash open on Mac)

STOP: Let me know when you have an account and are ready to continue.

USER: Ready

---

Now I need to connect to your GitHub account so I can save your code there.

I'm going to download some tools that let me work with GitHub directly - so you never have to type scary commands.

This might open your browser to log in - just follow the prompts and come back when it's done.

ACTION: Set up GitHub CLI:

1. Check if already installed:
```
gh --version
```

2. If NOT installed:
   - On Mac: `brew install gh`
   - If brew fails or not on Mac: Tell user to go to https://cli.github.com and download manually, then come back

3. Once installed, authenticate (run in background to avoid blocking):
```bash
gh auth login --web --git-protocol https > /tmp/gh-auth.log 2>&1 &
sleep 2
cat /tmp/gh-auth.log
```

4. Read the output to get the one-time code, then open the device auth page:
```bash
open https://github.com/login/device
```

5. Tell user: "I just opened a page in your browser. Enter this code: [CODE FROM OUTPUT]. Click Authorize, then let me know when you're done."

STOP: Let me know when you've authorized it.

USER: Done

ACTION: Verify authentication worked:
```bash
gh auth status
```

If successful, continue. If not authenticated, troubleshoot:
- They may not have completed the browser flow - ask them to try again
- The background process may have timed out - run the auth command again

---

Now let's save your code to GitHub. I'll make it private by default so only you can see it.

ACTION: Run the following commands in order:

1. Navigate to the quiz-project folder:
```
cd [path to quiz-project]
```

2. Initialize git (if not already done):
```
git init
```

3. Add all files:
```
git add .
```

4. Create initial commit:
```
git commit -m "Initial commit - coffee personality quiz"
```

5. Create GitHub repo and push:
```
gh repo create quiz-project --private --source=. --push
```

Done! Your code is now saved to GitHub. Developers call this "pushing" your code - you're pushing it up to the cloud.

Let me open it for you so you can see it.

ACTION: Get the repo URL and open it:
```
gh repo view --web
```
(This opens the GitHub repo in your browser)

STOP: Do you see your project on GitHub?

USER: Yes!

---

Your quiz is now backed up and ready to go live.

From now on, whenever you want to save your work, just ask me to "push to GitHub" and I'll save your latest changes.

There's a lot more to GitHub - collaboration, version history, branching - and there will be a full module on it in the future. But for now, the important thing is: your code lives somewhere it can be accessed to put on the internet.

That's exactly what we're doing next.

**Next up:** In 4.5, we put your quiz on the internet! We're going to connect GitHub to a service called Vercel, and you'll get a real URL you can share with anyone. This is the finish line.

STOP: Ready to go live? Say "let's go" or type /start-4-5

USER: Let's go

---

## Important Notes for Claude

- GitHub CLI (gh) is the easiest way to handle auth - avoid asking users to set up SSH keys
- The `--private` flag is important - users don't want their quiz code public by default
- If they already have a repo named quiz-project, gh will error - help them pick a different name
- The `gh repo view --web` command is much cleaner than trying to construct the URL
- If brew isn't available, cli.github.com has installers for all platforms
- Next.js projects already have a .gitignore so node_modules won't be committed

## Success Criteria

- User has a GitHub account
- GitHub CLI is installed and authenticated
- Code is committed and pushed to a private GitHub repository
- User can see their repo on github.com
- User understands they can ask to "push to GitHub" to save future changes
