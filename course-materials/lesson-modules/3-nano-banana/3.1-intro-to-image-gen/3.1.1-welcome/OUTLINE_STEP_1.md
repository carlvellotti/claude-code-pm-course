# Module 3.1.1: Welcome & First Generation - Ultra Simple Outline

## Files Needed to Start
- `image_gen.py` - Pre-built image generation module (in course root)
- `.env.example` - Template showing required environment variable
- `carl-reference.JPG` - Photo of Carl for reference image demo

## Files Created During Module
- `.env` - Created by copying `.env.example` and adding API key
- `outputs/output_001_HHMMSS.png` - First generated image (Carl in banana suit)
- `.image_session.json` - Session state file (created automatically)

## High-Level Overview
- Welcome to Nano Banana and quote Carl: "You aren't going to believe how fucking amazing this is"
- Explain Gemini 3 Pro (Nano Banana Pro) is Google's most advanced image generation model
- Emphasize Claude Code benefits: automatic API calls, session management, smart parameters
- Mention you'll build your own system of prompts, reference images, and styles through this course
- Walk through getting API key from Google AI Studio (free account, 2-3 min)
- Walk through setting up billing via Settings → Plan information → Set up Billing (required for Gemini 3 Pro) – Images are about $0.10 each. But you'll see that it's worth it and this whole course will not cost more than $5 absolute max.
- Set up `.env` file by copying `.env.example` and pasting API key
- Generate first image using `carl-reference.JPG` with prompt: "Carl in a bright yellow banana suit, standing confidently with arms crossed, big friendly smile, ready to teach. Text overlay says 'Welcome to Nano Banana!' Professional course instructor vibe but fun and playful."
- View the generated image in `outputs/` folder
- Quick overview of what you'll learn: mockups, personas, diagrams, ad creatives
- Tease what's next: understanding the basics and available options

---

## Teaching Flow

- Welcome to Nano Banana!
- I'm going to quote the course creator Carl here: "You aren't going to believe how fucking amazing this is"
- We're going to use Gemini 3 Pro, also known as Nano Banana Pro - Google's most advanced image generation model
- STOP: Are you ready to see what it can do?
- USER: Yes / Ready

---

- Before we generate anything, we need to set up your API key
- This takes about 2-3 minutes and you only do it once
- First, go to Google AI Studio: https://aistudio.google.com/
- ACTION: Display the URL for user to click/copy
- STOP: Open that link in your browser and let me know when you're there
- USER: I'm there

---

- If this is your first time, accept the Terms of Service
- Click "Get API Key" in the left sidebar
- You'll see your projects - click "Create API key" to generate a new key
- Copy the key that appears - it starts with "AIza..."
- STOP: Do you have your API key copied?
- USER: Yes

---

- Important: You also need to set up billing for Gemini 3 Pro to work
- Don't worry about cost - Gemini 3 Pro is about $0.10 per image, and this whole course will cost less than $5 total. This of course goes to Google and not to Carl (unfortunately).
- In Google AI Studio, go to Settings (bottom of the left sidebar) → Plan information
- Click "Set up Billing" next to your project
- This will redirect you to Google Cloud Console to link a billing account
- ACTION: Display the billing setup path: Settings → Plan information → Set up Billing
- Follow the on-screen instructions to add a payment method
- STOP: Is your billing set up?
- USER: Yes / Done

---

- Now let's add your API key to this project
- ACTION: Read `.env.example` and display its contents
- You need to copy this file to `.env` and paste in your API key
- STOP: Ask user to say: "Create my .env file with my API key"
- USER: Create my .env file with my API key
- ACTION: Copy `.env.example` to `.env`
- Now paste your API key after the equals sign
- ACTION: Open `.env` for editing and show where to paste the key
- STOP: Paste your API key and let me know when done
- USER: Done

---

- Perfect! You're all set up
- Now for the fun part - let's generate your first image
- I have a reference photo of Carl, the course creator
- We're going to put him in a banana suit to welcome you to the course
- You can find Carl's reference photo at `carl-reference.JPG` in this folder if you want to see who you're working with
- STOP: Ready to see the magic?
- USER: Yes / Ready

---

- STOP: Ask user to say: "Generate Carl in a banana suit welcoming me to Nano Banana"
- USER: Generate Carl in a banana suit welcoming me to Nano Banana
- ACTION: Run generate() with the reference image and prompt: "Carl in a bright yellow banana suit, standing confidently with arms crossed, big friendly smile, ready to teach. Text overlay says 'Welcome to Nano Banana!' Professional course instructor vibe but fun and playful."
	- Reference image: `carl-reference.JPG`
	- This takes about 10-15 seconds
- Your image has been saved to the `outputs/` folder - open it to see the result!
- STOP: What do you think?
- USER: Response about the image

---

- Pretty incredible, right?
- That's Gemini 3 Pro - it can take a reference photo and transform it while keeping the person recognizable
- And because we're doing this in Claude Code, I handle all the complexity for you
	- API calls
	- Session management
	- Saving outputs
	- Picking smart parameters
- Through this course, you'll build your own system of prompts, reference images, and styles
- We'll start by covering general use and then move onto PM use cases in the next module.
- STOP: Want to hear what you'll learn to create?
- USER: Yes

---

- Here's what's coming in this module:
- Product mockups and wireframes - turn sketches into polished designs
- Persona visualizations - bring your user personas to life
- Architecture diagrams - professional system diagrams from descriptions
- Ad creatives and marketing assets - social media graphics, announcements, more
- And you'll learn iteration strategies - how to refine images until they're exactly right
- STOP: Ready to continue to the next lesson where we dive into the basics?
- USER: Yes / Ready

---

- Great! In the next module, you'll learn how the `generate()` function works and all the options available to you
- Run `/start-3-1-2` when you're ready to continue
- ACTION: End module
