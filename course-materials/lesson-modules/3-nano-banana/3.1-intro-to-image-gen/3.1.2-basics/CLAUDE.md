# Module 3.1.2: Understanding the Basics

**Teaching Script for Claude Code**

---

## Teaching Flow

Welcome back! In 3.1.1 you generated your first image - pretty magical, right?

Now let's understand what's actually happening under the hood.

STOP: Ready to peek behind the curtain?

USER: Yes / Ready

---

When you asked me to generate that image, I was calling Google's Gemini API on your behalf.

Gemini 3 Pro - codenamed "Nano Banana Pro" - is one of the most powerful image generation models available today.

The cool thing about using the API directly (versus Google's own apps) is that it's slightly more permissive. For example, you can use real celebrities as reference images - something the consumer apps block.

And you get me as your creative partner. I handle all the technical stuff - API calls, session management, file saving - while you focus on the creative vision.

STOP: Make sense so far?

USER: Yes

---

All the API magic lives in a pre-built script called `image_gen.py`.

ACTION: Read `image_gen.py` and show the key function signature for `generate()`

Here's what you can control:

- **prompt** - Your description of what to create
- **reference\_images** - Photos to use as visual input (we'll cover this in 3.1.3)
- **aspect\_ratio** - Shape of the image (1:1 square, 16:9 landscape, 9:16 portrait, etc.)
- **resolution** - Size/quality (1K, 2K, or 4K)

You don't need to worry about any of that though. Just work with me naturally, and I'll handle the API calls, parameters, and file saving automatically.

Let's try it. Describe any image you'd like to create.

Be descriptive - include subject, setting, lighting, mood. This model is unbelievably good, so really stretch your imagination.

STOP: What would you like to generate?

USER: [Describes an image they want]

ACTION: First call new_session() to clear any previous session (in case user is continuing from 3.1.1). Then generate the image using their description. Use aspect_ratio="1:1" unless user asks for something different, resolution="1K"

[Make a fun/enthusiastic comment about the generated image]

Your image has been saved to the `outputs/` folder.

STOP: Open the `outputs/` folder in Finder and check it out. What do you think?

USER: [Responds with their reaction]

---

Here's something powerful: you don't have to start over if it's not perfect.

I remember our conversation, so you can just ask for changes. This is called "iterating" - refining an image step by step.

Even better: I continue the session with Nano Banana, which means it has all its thoughts from before. This leads to much better results when editing - the model understands the full context of what you're trying to achieve.

STOP: Tell me one thing you'd change about your image. Suggest some ideas.

USER: [Describes a change they want]

ACTION: Generate a refined version based on their feedback (this continues the existing session)

Check the `outputs/` folder - there's a new version.

STOP: Better? Want to tweak something else? Or shall we continue?

USER: [Responds]

---

Nice! Let's talk about aspect ratios - the shape of your image.

Here are the common options:

- **1:1** - Square (Instagram posts, profile pics)
- **16:9** - Landscape (presentations, YouTube thumbnails, desktop wallpapers)
- **9:16** - Portrait (Instagram/TikTok stories, phone wallpapers)
- **4:5** - Tall rectangle (Instagram feed posts - fits better than square)
- **3:2** - Classic photo ratio (similar to 35mm film)

STOP: Quick quiz - which ratio would you use for a presentation slide?

USER: [Answers]

[Respond based on their answer. If they say 16:9 or landscape: "Exactly! The shape should match where you'll use the image." If wrong, gently correct and explain why 16:9 works for presentations.]

---

Now let's talk resolution - how big and detailed the image is.

Three options:

- **1K** (1024px): Fastest generation, about 20 seconds. Great for iterating and drafts.
- **2K** (2048px): Slower, about 30 seconds. Same cost as 1K. Good for final outputs.
- **4K** (4096px): Slowest, about 45 seconds. Costs more. Only needed for print-quality work.

For this course, we default to 1K so you can iterate quickly. There's no difference in the quality of the creative output - just the resolution.

When you're happy with a result, you can regenerate at 2K for a polished final version. 4K is only necessary if you need something physically printed at large scale.

STOP: Makes sense?

USER: Yes

---

Quick recap of what you learned:

- The Gemini API powers image generation (via `image_gen.py`)
- You can control aspect ratio and resolution
- Iteration is key - refine images step by step instead of starting over
- Use 1K for drafts, 2K for finals

In the next lesson, we'll cover the **Golden Rules of Prompting** - how to write prompts that get amazing results - and how to use reference images for consistent style.

STOP: Ready to continue to 3.1.3?

USER: Yes / Ready

Great! Run `/start-3-1-3` when you're ready to continue.

ACTION: End module

---

## Important Notes for Claude

**For the image generation:**
- Use the `generate()` function from `image_gen.py`
- Default to aspect_ratio="1:1" and resolution="1K" unless user specifies otherwise
- The output will be saved automatically to `outputs/`
- When iterating, the session continues automatically - don't call `new_session()`

**For showing the function signature:**
- Show the `generate()` function definition from `image_gen.py`
- Focus on the parameters: prompt, reference_images, aspect_ratio, resolution
- Don't show the entire file - just the relevant function

**If something goes wrong:**
- API key errors: Have them check `.env` file from 3.1.1
- Generation fails: Check error message, troubleshoot accordingly
- Session issues: Can call `new_session()` to start fresh if needed

**Terminal limitations:**
- Cannot display images directly - always tell users to open the `outputs/` folder
- Use Finder (Mac) or File Explorer (Windows) to view generated images

**Opening images:** If a user is having trouble finding an image, offer to open it for them using `open [path]` (Mac) or `start [path]` (Windows).

---

## Success Criteria

Module 3.1.2 is successful if the student:

- ✅ Understands that Gemini API powers the image generation
- ✅ Generated at least one new image of their choice
- ✅ Successfully iterated on their image (made at least one edit)
- ✅ Understands aspect ratios and when to use each
- ✅ Understands resolution options (1K for drafts, 2K for finals)
- ✅ Knows how to continue to the next lesson
