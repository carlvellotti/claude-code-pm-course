# Module 3.1.1: Welcome & First Generation

**Teaching Script for Claude Code**

---

## Teaching Flow

Welcome to Nano Banana!

I'm going to quote the course creator Carl here: "You aren't going to believe how fucking amazing this is."

He's right. We're going to use Gemini 3 Pro - also known as Nano Banana Pro - Google's most advanced image generation model. It can create photorealistic images, transform reference photos, generate text overlays, and so much more.

STOP: Are you ready to see what it can do?

USER: Yes / Ready

---

Before we generate anything, we need to set up your API key. This takes about 2-3 minutes and you only do it once.

First, go to Google AI Studio:

**https://aistudio.google.com/**

STOP: Open that link in your browser and let me know when you're there.

USER: I'm there

---

If this is your first time, accept the Terms of Service.

Then click **"Get API Key"** in the left sidebar. You'll see your projects - click **"Create API key"** to generate a new key.

Copy the key that appears - it starts with "AIza..."

STOP: Do you have your API key copied?

USER: Yes

---

Important: You also need to set up billing for Gemini 3 Pro to work.

Don't worry about cost - it's about $0.10 per image, and this whole course will cost less than $5 total. (This goes to Google, not to Carl... unfortunately.)

In Google AI Studio, go to **Settings** (bottom of the left sidebar) → **Plan information** → click **"Set up Billing"** next to your project.

This will redirect you to Google Cloud Console to link a billing account. Follow the on-screen instructions to add a payment method.

STOP: Is your billing set up?

USER: Yes / Done

---

Now let's add your API key to this project.

ACTION: Read `.env.example` and show the contents

Here's what the `.env.example` file looks like - you need to copy this to `.env` and paste in your API key.

STOP: Say "Create my .env file with my API key"

USER: Create my .env file with my API key

---

ACTION: Copy `.env.example` to `.env`

I've created the `.env` file for you. Now paste your API key after the equals sign where it says `your_key_here`.

STOP: Let me know when you've pasted your key.

USER: Done

---

Perfect! You're all set up.

Now for the fun part - let's generate your first image.

I have a reference photo of Carl, the course creator. You can find it at `lesson-modules/3-nano-banana/3.1-intro-to-image-gen/3.1.1-welcome/carl-reference.JPG` if you want to see what you're working with. We're going to put him in a banana suit to welcome you to the course.

STOP: Say "Generate Carl in a banana suit welcoming me to Nano Banana"

USER: Generate Carl in a banana suit welcoming me to Nano Banana

---
This will take about 10-15 seconds

ACTION: Run generate() with reference image `carl-reference.JPG` and prompt: "Carl in a bright yellow banana suit, standing confidently with arms crossed, big friendly smile, ready to teach. Text overlay says 'Welcome to Nano Banana!' Professional course instructor vibe but fun and playful."

Your image has been saved to the `outputs/` folder - open it to see the result!

STOP: What do you think?

USER: Response about the image

---

Pretty incredible, right?

That's Gemini 3 Pro. It can take a reference photo and transform it while keeping the person recognizable. And because we're doing this in Claude Code, I handle all the complexity for you:

- API calls
- Session management
- Saving outputs
- Picking smart parameters

Through this course, you'll build your own system of prompts, reference images, and styles. We'll start by covering general use and then move onto PM use cases in the next module.

STOP: Want to hear what's coming next in this module?

USER: Yes

---

Here's what we'll cover in Module 3.1:

- **Understanding the Basics** - how the generate() function works, available parameters, output structure
- **Consistency & Style** - using reference images, building a style database, extracting styles from existing images
- **Iteration Strategies** - sessions, refining images step by step, reverting when needed

Once you've got the fundamentals down, Module 3.2 will show you PM-specific use cases like mockups, personas, and diagrams.

STOP: Ready to continue to the next lesson?

USER: Yes / Ready

---

Great! In the next lesson, you'll learn how the `generate()` function works and all the options available to you.

Run `/start-3-1-2` when you're ready to continue.

ACTION: End module

---

## Important Notes for Claude

**File operations in this module:**
- Read `.env.example` to show the student the template
- Copy `.env.example` to `.env` when student requests
- The student manually pastes their API key - don't try to insert it for them

**For the image generation:**
- Use the `generate()` function from `image_gen.py`
- Pass the reference image path and the exact prompt specified
- The output will be saved automatically to `outputs/`

**If something goes wrong:**
- API key errors: Have them double-check the key is pasted correctly in `.env`
- Billing errors: Confirm billing is set up in Google AI Studio settings
- Generation fails: Check the error message and troubleshoot accordingly

---

## Success Criteria

Module 3.1.1 is successful if the student:

- ✅ Has their Gemini API key set up in `.env`
- ✅ Has billing configured in Google AI Studio
- ✅ Generated their first image (Carl in banana suit)
- ✅ Understands what they'll learn in this module
- ✅ Knows how to continue to the next lesson

---

**Remember: This is the student's first taste of image generation. Make it magical. The "wow" moment with that first generated image sets the tone for the entire module.**
