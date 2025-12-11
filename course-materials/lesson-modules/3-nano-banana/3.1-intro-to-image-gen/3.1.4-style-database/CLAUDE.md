# Module 3.1.4: Building Your Style Database

Welcome to Module 3.1.4: Building Your Style Database.

So far we've learned how to generate images and apply the Golden Rules. But there's a bigger game here - one that separates casual users from power users.

The meta-skill is this: building a personal creative toolkit that grows with you over time. Instead of starting from scratch every time, you build a library of styles you can reuse.

Think about it - every great image you create, every prompt that works perfectly, every style you discover... it all becomes part of your toolkit. This is the difference between using AI occasionally versus having AI as a creative superpower.

STOP: Make sense so far?

USER: Yes

---

Here's where Claude Code becomes your perfect partner. I can manage your entire style database for you. Just say "use style #3" or "add this to my library" and I'll handle everything - full context, no copy-pasting, no hunting through old chats.

There are three ways to grow your library:
- **Save prompts as you go** - when you make something you like
- **Collect prompts from online** - databases, social media, tutorials
- **Extract styles from any image** - the power move

We'll try all three today.

I've set up a starter style library for you. Let me open it in your browser automatically.

ACTION: Open the style library in the user's browser:
- Mac: `open [absolute path to style-library.html]`
- Windows: `start [absolute path to style-library.html]`

It should have just opened in your browser.

STOP: Take a look at the style library. Let me know when you've had a chance to browse through it.

USER: It's open

---

## Part 2: Introduce the Style Library

Now, important clarification: this isn't a real website! It's just a local HTML file - a way to visualize your style collection right from your computer.

And here's the cool part: you can always change the design or functionality just by asking me. Don't do it now, but in the future you could ask me to add new columns, change the layout, add search functionality - whatever you want. It's YOUR toolkit. Make it work for you.

STOP: Pretty cool, right?

USER: Yes

---

Let me walk you through the structure. Each style has:
- **Index number** - so you can just say "use style #02"
- **Thumbnail preview** - hover to enlarge
- **Name and tags** - for quick scanning
- **Category** - for filtering
- **The full prompt** - hover to expand, click to copy
- **Example uses** - so you know when to reach for it

Try the filter buttons at the top to see different categories.

STOP: Take a minute to browse. Which style catches your eye?

USER: [Picks a style]

---

Great choice! Let's try it out.

STOP: What subject do you want to generate using that style? Tell me the style number and your subject.

USER: [Style number and subject]

ACTION: Run `python3 get_style.py [number]` to get the style prompt. Then generate an image using that prompt combined with their subject.

Your image is ready!

ACTION: Provide the exact path to the output image file

Open the outputs folder to see it.

STOP: What do you think?

USER: [Response]

---

## Part 3: Growing Your Library - Method 1: Save As You Go

That's the first method of using your library - picking existing styles. Now let's talk about GROWING it.

Method 1 is the simplest: save as you go. Whenever you create something you like, just tell me to add it to your library.

Let's try it. I want you to generate any image you want.

STOP: What would you like to create? Any subject, any style - describe it however you want.

USER: [Describes their image]

---

ACTION: Generate the image based on their description using image_gen.py

Done! Check the outputs folder to see your image.

ACTION: Provide the exact path to the output image file

STOP: Take a look - do you like the style?

USER: [Response]

---

If you like it, you can save this style to your library for future use.

STOP: Try it - tell me to add this style to your library.

USER: Add this to my library / Add this style to my library

ACTION: Update style-library.html with the new style entry:
- Find the next available ID number
- Extract a descriptive name from the prompt
- Choose an appropriate category from: Illustration, Photo - Portrait, Photo - Product, Photo - Environment, Diagram, UI/Mockup, 3D/Isometric, Presentation, Marketing, Artistic
- Add 3-5 relevant tags
- Copy the output image to the thumbnails/ folder with a descriptive filename
- Add the entry to the styles array in the JavaScript section
- Write a brief "exampleUse" description

Done! Refresh your style library in the browser.

STOP: Do you see your new style?

USER: Yes

---

That's Method 1 - save as you go. Every time you create something you love, just tell me to save it. Over time your library becomes a goldmine of proven styles.

STOP: Ready for Method 2?

USER: Yes

---

## Part 4: Growing Your Library - Method 2: Collect From Online

Method 2: collect prompts from online. There are amazing prompts floating around on social media, prompt databases, and tutorials. When you find one you like, test it, then add it to your library.

Here's a great example from the official Nano Banana account: https://x.com/NanoBanana/status/1998085942201163905

The prompt is: "Make a photo that is perfectly isometric. It is not a miniature, it is a captured photo that just happened to be perfectly isometric. It is a photo of [subject]."

STOP: What subject should we use for the isometric photo?

USER: [Their subject]

---

ACTION: Generate an isometric image with their subject using the prompt: "Make a photo that is perfectly isometric. It is not a miniature, it is a captured photo that just happened to be perfectly isometric. It is a photo of [their subject]."

Check out your isometric photo!

ACTION: Provide the exact path to the output image file

Open the outputs folder to see it.

STOP: Pretty cool effect, right? Do you want to add this style to your library?

USER: Yes / Add this to my library

ACTION: Update style-library.html with the isometric style:
- Name: "Perfect Isometric Photo"
- Category: "3D/Isometric"
- Tags: ["isometric", "photography", "geometric", "perspective"]
- Prompt: "Make a photo that is perfectly isometric. It is not a miniature, it is a captured photo that just happened to be perfectly isometric. It is a photo of [subject]."
- Copy the output image to thumbnails/
- Add entry to styles array

Done! Refresh your browser to see it.

STOP: Two styles added! Ready for the power move?

USER: Yes

---

## Part 5: Growing Your Library - Method 3: Extract From Any Image

Method 3 is the power move.

Gemini 3 Pro isn't just amazing at creating images - it has the best image understanding of any model. That means we can extract the style from ANY image and recreate it.

See an image you love on Pinterest? Instagram? A magazine? Extract the style, save it forever.

I've built a style extraction module to do exactly this.

STOP: Want to see it in action?

USER: Yes

---

ACTION: Confirm the style_extract.py file exists in the lesson-modules/3-nano-banana/ directory

The `style_extract.py` module analyzes any image and extracts detailed style information. Not as JSON or structured data - as natural language that Gemini can use directly.

It captures: color palette, lighting, composition, textures, mood, artistic style, typography, special effects - everything that makes the image look the way it looks.

Let's test it on a deliberately HARD image.

ACTION: Get the exact path to recursive-painter.jpg in this module folder

Open this file to see it: [provide exact path]

STOP: Do you see it? It's a man painting himself painting himself, with a CRT TV showing the same scene - 1990s aesthetic with a datestamp.

USER: Yes, I see it

Recursive, complex, layered. If we can extract THIS style, we can extract anything.

STOP: Ready to run the extraction?

USER: Yes

---

ACTION: Run the style extraction on recursive-painter.jpg by executing:
```python
import sys
sys.path.insert(0, '[course root path]')
from style_extract import extract_style
result = extract_style('[path to recursive-painter.jpg]')
print(result)
```

Here's what the extraction found:

ACTION: Display the extracted style description to the user

[Explictly show the output]

Look at all that detail - the color palette, the lighting quality, the composition notes, the texture descriptions.

Now here's the real test: can we recreate the EXACT same image from just this text description?

STOP: Tell me to recreate the image using the extracted style.

USER: Recreate the image / Generate it

---

ACTION: Generate an image using the extracted style description. The prompt should recreate the recursive painter scene - a man in an art studio painting himself painting himself, with a CRT TV showing the same recursive scene, 1990s analog snapshot aesthetic with datestamp.

ACTION: Provide the exact path to the output image file

Open the output and compare it side-by-side with the original.

STOP: What do you think? Can you see the same style captured?

USER: [Response - should be impressed]

---

This is the wow moment.

We took a complex, layered, recursive image and extracted its essence as pure text. Then recreated it from scratch.

Now imagine doing this with any image you love - any style you want to capture. Pinterest inspiration → extract → save → yours forever.

STOP: Want to add this extracted style to your library?

USER: Yes / Add it

ACTION: Update style-library.html with the 90s Analog Snapshot style:
- Name: "90s Analog Snapshot"
- Category: "Photo - Portrait"
- Tags: ["vintage", "film grain", "flash", "nostalgic", "datestamp"]
- Prompt: Use the extracted style description
- Copy the generated output image to thumbnails/
- Add entry to styles array

Refresh your browser - you now have three new styles!

STOP: How's your library looking?

USER: [Response]

---

## Part 6: Wrap-Up

Let's recap what you've learned.

The meta-skill: building a personal creative toolkit that grows with you. Three ways to grow your library:
- **Save as you go** - create something you like → add it
- **Collect from online** - find prompts → test → save
- **Extract from any image** - the power move

Any image you love → extract → save → reuse forever. And I manage it all for you - just say "use style #3" or "add this to my library."

STOP: Any questions about building your style database?

USER: [Questions or no]

---

You now have a complete, advanced understanding of everything you need to use Nano Banana Pro. You know the Golden Rules, you know how to iterate, and you know how to build a style toolkit.

In Module 3.2, we'll apply all these learnings to real PM use cases - mockups, diagrams, presentations, and more.

STOP: Ready to move on to Module 3.2?

USER: Yes

Great! Type `/start-3-2-1` to continue.

---

## Important Notes for Claude

### File Paths
- `style-library.html` is in this module folder: `lesson-modules/3-nano-banana/3.1-intro-to-image-gen/3.1.4-style-database/`
- `recursive-painter.jpg` is also in this module folder
- `style_extract.py` and `image_gen.py` are in `lesson-modules/3-nano-banana/`
- Output images go to `lesson-modules/3-nano-banana/outputs/`
- Thumbnails go to the `thumbnails/` folder in this module folder

### When Adding Styles to the Library
1. Read the current style-library.html to find the styles array AND the CANONICAL_TAGS object
2. Determine the next ID number
3. Create a descriptive name
4. Choose a category from the CATEGORIES array (see below)
5. Choose 2-4 tags ONLY from the CANONICAL_TAGS for that category
6. Copy the output image to thumbnails/ with a kebab-case filename
7. Add the new entry to the styles array in the HTML file
8. Update the thumbnail path to point to the new file

### Categories and Canonical Tags
The style-library.html contains CATEGORIES and CANONICAL_TAGS objects. You MUST use these exactly:

**Categories:** Framework, Flow, Architecture, Mockup, Persona, Marketing, Artistic

**Canonical Tags by Category:**
- **Framework:** 2x2-matrix, pyramid, venn, canvas, concentric, triangle
- **Flow:** process, journey-map, flowchart, steps, sequence
- **Architecture:** hierarchy, hub-spoke, system-diagram, org-chart, tree
- **Mockup:** wireframe, device-frame, ui-concept, landing-page, mobile, desktop
- **Persona:** portrait, lifestyle, headshot, context, illustrated, scene
- **Marketing:** ad, social, announcement, banner, hero
- **Artistic:** flat-illustration, hand-drawn, watercolor, photography, retro, minimalist, bold-graphic, 3d-render

Do NOT invent new tags or categories. Always reference the CANONICAL_TAGS in the HTML file.

**Note:** Users can combine styles from different categories (e.g., "use the retro style from Artistic with a scene-style Persona") to create composable results.

### Running Style Extraction
Use the extract_style() function from style_extract.py. It takes an image path and returns a detailed natural language description of the visual style.

### Terminal Limitations
- Cannot display images directly - always provide file paths for users to open
- Use closed validation questions ("Do you see it?") not open-ended ones
- **Opening images:** If a user is having trouble finding an image, offer to open it for them using `open [path]` (Mac) or `start [path]` (Windows)

## Success Criteria

The module is complete when:
- [ ] User has opened and explored the style library HTML
- [ ] User has generated an image using an existing style from the library
- [ ] User has added at least one custom style using Method 1 (save as you go)
- [ ] User has added the isometric style using Method 2 (collect from online)
- [ ] User has seen the style extraction in action on recursive-painter.jpg
- [ ] User has seen the recreated image compared to the original
- [ ] User has been offered to add the extracted style to their library
- [ ] User is directed to Module 3.2 with `/start-3-2-1`
