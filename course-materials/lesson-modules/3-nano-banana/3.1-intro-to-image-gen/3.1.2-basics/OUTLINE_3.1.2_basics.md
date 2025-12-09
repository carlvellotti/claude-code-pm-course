# Module 3.1.2: Understanding the Basics - Ultra Simple Outline

## Files Needed to Start
- `image_gen.py` - Pre-built image generation module (in course root)
- `.env` - Already configured with API key from 3.1.1
- `outputs/output_001_*.png` - The image generated in 3.1.1

## Files Created During Module
- `outputs/output_*.png` - Student's generated images (varies based on what they create)
- `.image_session.json` - Updated with session history

## High-Level Overview
- Recap: You generated your first image in 3.1.1, now let's understand how it works under the hood
- Explain we're hitting the Gemini API - Google's image generation service. The main advantage is that you can use me (Claude Code) when working with the API, but there are other advantages as well. For example API use is slightly more permissive than using Google's own products, allowing you to do things like use real celebrities as reference images.
- Introduce `image_gen.py` - a pre-built Python script that handles the API calls for you
- Show the script in chat and walk through what each part controls (aspect ratio, resolution, model)
- Note: we're using gemini-3-pro-image-preview (aka Nano Banana Pro) - the most powerful model
- Generate a simple image to demonstrate the basics - user can input whatever they want
- Show where the output went (`outputs/` folder)
- Immediately explain iteration: you can refine images by asking for changes
- Demonstrate iteration: ask for a change to the image we just made
- Walk through aspect ratios with examples (16:9 for landscape, 9:16 for portrait)
- Explain resolution options:
  - 1K (1024px): Fastest (~18s), good for iteration and drafts - we'll use this as default for speed
  - 2K (2048px): Slower (~28s) but same cost as 1K - good for final outputs
  - 4K (4096px): Slowest (~42s) and costs more - only for print-quality work
- Tease what's next: the golden rules of prompting, consistency & style

---

## Teaching Flow

- Welcome back! In 3.1.1 you generated your first image - pretty magical, right?
- Now let's understand what's happening under the hood
- STOP: Ready to peek behind the curtain?
- USER: Yes / Ready

---

- When you asked me to generate that image, I was calling Google's Gemini API
- Gemini 3 Pro (aka: Nano Banana Pro) is one of the most powerful image models available
- The cool thing about using the API directly (vs Google's own apps) is it's slightly more permissive
  - For example, you can use real celebrities as reference images
- And you get me (Claude) as your creative partner - I handle the technical stuff while you focus on the creative vision
- STOP: Make sense so far?
- USER: Yes

---

- All the API magic lives in a pre-built script called `image_gen.py`
- ACTION: Read `image_gen.py` and show the key function signature for `generate()`
- Here's what you can control:
  - `prompt` - Your description of what to create
  - `reference_images` - Photos to use as visual input (we'll cover this in 3.1.3)
  - `aspect_ratio` - Shape of the image (1:1 square, 16:9 landscape, 9:16 portrait, etc.)
  - `resolution` - Size/quality (1K, 2K, or 4K)
- You can just work with me, and I'll handle the API calls, parameters, and file saving automatically
- Let's try it - describe any image you'd like to create
- Be descriptive - include subject, setting, lighting, mood. This model is unbelievably good, so really stretch your imagination.
- STOP: What would you like to generate?
- USER: [Describes an image they want]
- ACTION: Generate the image using their description, aspect_ratio="1:1" (unless user asks for something different), resolution="1K"
- [Make a fun comment about image] Your image has been saved to the `outputs/` folder
- STOP: Open the `outputs/` folder in Finder and check it out. What do you think?
- USER: [Responds with their reaction]

---

- Here's something powerful: you don't have to start over if it's not perfect
- I remember our conversation, so you can just ask for changes
- Iterate by refining an image step by step. I will also continue the session with Nano Banana, which means it has all it's thoughts from before, which leads to much better results for editing.
- STOP: Tell me one thing you'd change about your image
- USER: [Describes a change they want]
- ACTION: Generate a refined version based on their feedback (continues the session)
- Check the `outputs/` folder - there's a new version
- STOP: Better? Or want to tweak something else? Or shall we continue?
- USER: [Responds]

---

- Nice! Let's talk about aspect ratios - the shape of your image
- Common options:
  - `1:1` - Square (Instagram posts, profile pics)
  - `16:9` - Landscape (presentations, YouTube thumbnails, desktop wallpapers)
  - `9:16` - Portrait (Instagram/TikTok stories, phone wallpapers)
  - `4:5` - Tall rectangle (Instagram feed posts - fits better than square)
  - `3:2` - Classic photo ratio (similar to 35mm film)
- STOP: Which ratio would you use for a presentation slide?
- USER: Answers
- [Reply based on answer, ie if "landscape": Exactly! The shape should match where you'll use the image]

---

- Now let's talk resolution - how big/detailed the image is
- Three options:
  - **1K** (1024px): Fastest generation (~20 seconds). Great for iterating and drafts
  - **2K** (2048px): Slower (~30 seconds), same cost as 1K. Good for final outputs
  - **4K** (4096px): Slowest (~45 seconds), costs more. Only for print-quality work
- For this course, we default to 1K so you can iterate quickly. There is no difference in the quality of the work itself other than resolution.
- When you're happy with a result, you can regenerate at 2K for a polished final version. 4K is good for something that needs to be physically printed.
- STOP: Makes sense?
- USER: Yes

---

- Quick recap of what you learned:
  - Gemini API powers the image generation (via `image_gen.py`)
  - You can control aspect ratio and resolution
  - Iteration is key - refine images step by step instead of starting over
  - 1K for drafts, 2K for finals
- In the next lesson, we'll cover the **Golden Rules of Prompting** and how to use reference images for consistent style
- STOP: Ready to continue to 3.1.3?
- USER: Yes / Ready
- Run `/start-3-1-3` when you're ready!
- ACTION: End module
