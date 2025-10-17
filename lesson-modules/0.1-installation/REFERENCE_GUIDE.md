# Module 0.1: Installation & Prerequisites

**Goal:** Get Claude Code installed and verified on your machine in 15 minutes.

**What you'll accomplish:**
- ✅ Verify you have the prerequisites
- ✅ Install Claude Code CLI
- ✅ Authenticate with your Claude account
- ✅ Run health check to confirm everything works

---

## Prerequisites Checklist

Before you begin, make sure you have:

### 1. Claude Subscription (Required)
- **Claude Pro** ($20/month) OR **Claude Max** (higher tier)
- You CANNOT use Claude Code with the free tier
- Sign up at: https://claude.ai/

### 2. Operating System (Any of these)
- **macOS** (any recent version)
- **Windows** (Windows 10 or later)
- **Linux** (most distributions supported)

### 3. Node.js (We'll help you install if needed)
- Claude Code requires Node.js version 18 or higher
- Don't worry if you don't have it—we'll show you how to install it below

---

## Step 1: Check if Node.js is Installed

Open your terminal:
- **Mac:** Press `Cmd + Space`, type "Terminal", press Enter
- **Windows:** Press `Windows + R`, type "cmd", press Enter
- **Linux:** Press `Ctrl + Alt + T`

Type this command and press Enter:

```bash
node --version
```

**If you see a version number** (like `v18.0.0` or higher):
- ✅ Great! You have Node.js installed. Skip to Step 2.

**If you see "command not found" or an error:**
- ❌ You need to install Node.js. Follow the instructions below.

---

## Installing Node.js (If Needed)

### Option A: Official Installer (Recommended for beginners)

1. Go to: https://nodejs.org/
2. Download the **LTS (Long Term Support)** version
3. Run the installer and follow the prompts
4. After installation, **close and reopen your terminal**
5. Verify by running: `node --version`

### Option B: Using a Package Manager (For advanced users)

**Mac (using Homebrew):**
```bash
brew install node
```

**Windows (using Chocolatey):**
```bash
choco install nodejs
```

**Linux (using apt):**
```bash
sudo apt update
sudo apt install nodejs npm
```

---

## Step 2: Install Claude Code

Now that you have Node.js, installing Claude Code is simple.

Copy and paste this command into your terminal:

**Mac / Linux:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**What this does:**
- Downloads the Claude Code installer
- Installs Claude Code globally on your system
- Sets up the necessary permissions

**What you'll see:**
- Installation progress messages
- A success message: "✅ Claude Code successfully installed!"
- Version information

This should take 1-2 minutes.

---

## Step 3: Verify Installation

After installation completes, verify Claude Code is installed correctly:

```bash
claude --version
```

**You should see:**
- A version number (e.g., `Version: 1.0.93` or similar)
- If you see this, ✅ installation successful!

**If you see "command not found":**
1. Close and reopen your terminal
2. Try again: `claude --version`
3. Still not working? See Troubleshooting section below

---

## Step 4: Authenticate with Your Claude Account

Now let's connect Claude Code to your Claude Pro or Max subscription.

**Run this command:**

```bash
claude
```

**What happens next:**
1. Claude Code will start for the first time
2. You'll see a welcome screen
3. It will ask you to choose a login method:
   - **Option 1:** Claude account with subscription (← Choose this)
   - **Option 2:** Anthropic Console account (for API usage billing)

**Choose Option 1** and follow the authentication flow:
- A browser window will open
- Log in with your Claude Pro/Max credentials
- Authorize Claude Code
- Return to your terminal

**Success looks like this:**
```
Welcome to Claude Code

Let's get started.

Choose the text style that looks best with your terminal:
[Selection menu appears]
```

Choose your preferred text style (I recommend Dark mode or Light mode depending on your terminal theme).

---

## Step 5: Run Health Check

Let's make sure everything is working properly.

**Type this command in Claude Code (you should already be in Claude Code from Step 4):**

```
/doctor
```

**What `/doctor` does:**
- Checks your Claude Code installation
- Verifies your subscription is active
- Tests your system configuration
- Checks for common issues

**Healthy output looks like:**
```
✅ Installation complete!
✅ Subscription active
✅ System configuration valid
✅ All checks passed
```

**If you see any ❌ red X marks:**
- Read the error message carefully
- See Troubleshooting section below
- Or proceed to the next module—most issues resolve themselves

---

## Success Criteria

You're ready for Module 0.2 when you can:

✅ Run `claude --version` and see a version number
✅ Type `claude` in your terminal and see the welcome screen
✅ Run `/doctor` and get green checkmarks
✅ Feel confident opening your terminal (even if it feels new!)

---

## Troubleshooting Common Issues

### "Command not found: claude"

**Fix:**
1. Close your terminal completely
2. Open a new terminal window
3. Try again: `claude --version`

**Still not working?**
- Your PATH variable may not be updated
- **Mac/Linux:** Add this to `~/.bashrc` or `~/.zshrc`:
  ```bash
  export PATH="$HOME/.local/bin:$PATH"
  ```
- **Windows:** The installer usually handles this automatically. Try restarting your computer.

### "Subscription required"

**Fix:**
- Make sure you have an active Claude Pro or Max subscription
- Go to: https://claude.ai/ and verify your subscription status
- Try logging out and logging back in

### "Node version too old"

**Fix:**
- Update Node.js to version 18 or higher
- Run: `node --version` to check your current version
- Download the latest LTS from: https://nodejs.org/

### "Permission denied" errors

**Mac/Linux Fix:**
```bash
sudo curl -fsSL https://claude.ai/install.sh | bash
```

**Windows Fix:**
- Run PowerShell as Administrator
- Right-click PowerShell icon → "Run as Administrator"
- Run the install command again

### Still stuck?

**Get help:**
- Official docs: https://docs.claude.com/en/docs/claude-code
- GitHub issues: https://github.com/anthropics/claude-code/issues
- Claude Code community forums

---

## What You Just Did

Congratulations! You've just:

1. ✅ Installed a powerful AI tool that most PMs don't even know exists
2. ✅ Set up your terminal environment (no longer intimidating!)
3. ✅ Authenticated with Claude
4. ✅ Verified everything works with `/doctor`

**Time invested:** 15 minutes
**ROI:** Infinite (you'll save hours per week for the rest of your career)

---

## What's Next

**Module 0.2: Start Claude Code & Clone the Course**

In the next module, you'll:
- Have your first real conversation with Claude Code
- Watch Claude clone this entire course repository for you
- See the "aha!" moment: Claude does the work while you state the intent

**Pro tip before you continue:**
- Keep your terminal open
- Don't worry about understanding every detail
- You'll learn by doing in the next modules

---

## Quick Reference: Commands You Learned

| Command | What it does |
|---------|-------------|
| `node --version` | Check if Node.js is installed |
| `claude` | Start Claude Code |
| `claude --version` | Check Claude Code version |
| `/doctor` | Run health check inside Claude Code |
| `/help` | Get help inside Claude Code |

---

**Ready? Let's move to Module 0.2 and start using Claude Code.**
