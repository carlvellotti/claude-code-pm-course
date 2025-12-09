# Module 3.1.4: Building Your Style Database - Outline

## Files Needed to Start
- `image_gen.py` - Pre-built image generation module (in course root)
- `style_extract.py` - Style extraction module (in course root)
- `.env` - Already configured with API key
- `recursive-painter.jpg` - Complex example image (man painting himself painting himself with CRT TV)
- `style-library.html` - Visual browser for the style library (open in browser)
- `thumbnails/` folder - Preview images for each style

## Files Created During Module
- New entry added to `style-library.html` from our extraction demo
- `thumbnails/90s-analog-snapshot.jpg` - Thumbnail for the extracted style
- `outputs/output_*.png` - Generated images using styles from the library

## High-Level Overview

**Part 1: The Meta-Skill**
- So far we've learned how to generate images and apply the Golden Rules
- But there's a bigger game: building a personal creative toolkit that grows with you over time
- Instead of starting from scratch every time, you build a library of styles you can reuse
- This is the difference between using AI occasionally vs having AI as a creative superpower
- This is also an amazing way to use Claude Code as your partner - it can manage the database for you
- Just say "use style #3" or "add this to my library" and Claude handles the rest - full context, no copy-pasting
- Three ways to grow your library: save as you go, collect from online, extract from any image

**Part 2: Introduce the Style Library**
- Tell user to open `style-library.html` in their browser (give exact path, tell them to find in Finder/Explorer and double-click)
- Clarify: this isn't a real website! It's just a local HTML file - a way to visualize your style collection from your computer
- And here's the cool part: you can always change the design or functionality just by asking Claude! Don't do it now, but in the future you could add new columns, change the layout, add search, etc.
- Explain the library structure: index number, thumbnail, name, category, prompt (click to copy), tags, example uses
- Categories: Framework, Flow, Architecture, Mockup, Persona, Marketing, Artistic (PM-focused + composable!)
- How to use it: tell Claude the index # (e.g., "use style #02") or copy the prompt directly
- Let user try it - pick a style, generate something with it

**Part 3: Growing Your Library - Method 1: Save As You Go**
- Simplest method: when you create something you like, just tell Claude to add it to the library
- Ask user: what image would you like to generate? (any subject, any style)
- Generate their image
- Have them view it, then ask them to tell you to add it to their style library
- Demo the flow: user says "add this to my library" → Claude updates style-library.html

**Part 4: Growing Your Library - Method 2: Collect From Online**
- Find prompts from databases, social media, tutorials
- Example from official Nano Banana account: https://x.com/NanoBanana/status/1998085942201163905
- The prompt: "Make a photo that is perfectly isometric. It is not a miniature, it is a captured photo that just happened to be perfectly isometric. It is a photo of [subject]."
- Ask user: what subject should we use for the isometric photo?
- Generate the image with their subject
- Have them view it, then ask them to tell you to add it to their style library
- Demo the full flow: user says "add this to my library" → Claude updates style-library.html

**Part 5: Growing Your Library - Method 3: Extract From Any Image**
- The power move: Gemini 3 Pro isn't just amazing at creating images - it has the best image understanding of any model
- Show `style_extract.py` - pre-built module that extracts detailed style information using natural language (not JSON)
- Proof of concept with a deliberately HARD image (`recursive-painter.jpg`) - recursive painting with CRT TV and 1990s aesthetic
- Run style extraction, review the detailed output (color palette, lighting, composition, textures, mood, typography, effects)
- Recreate the EXACT same image from pure text description to prove the extraction works
- Compare side-by-side - this is the wow moment
- Ask the user if they want to add the extracted style to `style-library.html`

**Part 6: Wrap-Up**
- Emphasize the meta-skill: building your personal creative toolkit over time
- Any image you love → extract → save → reuse forever
- You now have a complete, advanced understanding of everything you need to use Nano Banana Pro
- In Module 3.2, we'll apply all these learnings to real PM use cases

---

## Teaching Flow

### Part 1: The Meta-Skill

- Welcome to Module 3.1.4: Building Your Style Database
- So far we've learned how to generate images and apply the Golden Rules
- But there's a bigger game here - one that separates casual users from power users
- The meta-skill is this: building a personal creative toolkit that grows with you over time
- Instead of starting from scratch every time, you build a library of styles you can reuse
- Every great image you create, every prompt that works perfectly, every style you discover... it all becomes part of your toolkit
- This is the difference between using AI occasionally vs having AI as a creative superpower
- STOP: Make sense so far?
- USER: Yes

---

- Here's where Claude Code becomes your perfect partner
- Claude can manage your entire style database for you
- Just say "use style #3" or "add this to my library" and Claude handles everything
- Full context, no copy-pasting, no hunting through old chats
- There are three ways to grow your library:
	- Save prompts as you go (when you make something you like)
	- Collect prompts from online (databases, social media, tutorials)
	- Extract styles from any image (the power move)
- We'll try all three today
- ACTION: Get the absolute path to style-library.html in this module folder
- I've set up a style library for you - open this file in your browser: [provide exact path]
- Find it in Finder (Mac) or Explorer (Windows) and double-click to open
- STOP: Let me know when you have it open
- USER: It's open

---

### Part 2: Introduce the Style Library

- Now, important clarification: this isn't a real website!
- It's just a local HTML file - a way to visualize your style collection right from your computer
- And here's the cool part: you can always change the design or functionality just by asking me
- Don't do it now, but in the future you could ask me to add new columns, change the layout, add search functionality, whatever you want
- It's YOUR toolkit - make it work for you
- STOP: Pretty cool, right?
- USER: Yes

---

- Let me walk you through the structure
- Each style has:
	- Index number (so you can just say "use style #02")
	- Thumbnail preview (hover to enlarge)
	- Name and tags for quick scanning
	- Category for filtering
	- The full prompt (hover to expand, click to copy)
	- Example uses so you know when to reach for it
- Try the filter buttons at the top to see different categories
- STOP: Take a minute to browse. Which style catches your eye?
- USER: [Picks a style]

---

- Great choice! Let's try it out
- STOP: What subject do you want to generate using that style? Tell me the style number and your subject
- USER: [Style number and subject]
- ACTION: Generate image using the selected style prompt with their subject
- Your image is ready - open the outputs folder to see it
- ACTION: Provide the path to the output image
- STOP: What do you think?
- USER: [Response]

---

### Part 3: Growing Your Library - Method 1: Save As You Go

- That's the first method of using your library - picking existing styles
- Now let's talk about GROWING it
- Method 1 is the simplest: save as you go
- Whenever you create something you like, just tell me to add it to your library
- Let's try it - I want you to generate any image you want
- STOP: What would you like to create? Any subject, any style - describe it however you want
- USER: [Describes their image]

---

- ACTION: Generate the image based on their description
- Done! Check the outputs folder to see your image
- ACTION: Provide the path to the output image
- STOP: Take a look - do you like the style?
- USER: [Response]

---

- If you like it, you can save this style to your library for future use
- STOP: Try it - tell me to add this style to your library
- USER: Add this to my library / Add this style to my library
- ACTION: Update style-library.html with the new style entry
	- Extract a name and category from the prompt
	- Add appropriate tags
	- Save the output image as a thumbnail
	- Add entry to the styles array in the HTML file
- Done! Refresh your style library in the browser
- STOP: Do you see your new style?
- USER: Yes

---

- That's Method 1 - save as you go
- Every time you create something you love, just tell me to save it
- Over time your library becomes a goldmine of proven styles
- STOP: Ready for Method 2?
- USER: Yes

---

### Part 4: Growing Your Library - Method 2: Collect From Online

- Method 2: collect prompts from online
- There are amazing prompts floating around on social media, prompt databases, tutorials
- When you find one you like, test it, then add it to your library
- Here's a great example from the official Nano Banana account
- ACTION: Show the Twitter/X link: https://x.com/NanoBanana/status/1998085942201163905
- The prompt is: "Make a photo that is perfectly isometric. It is not a miniature, it is a captured photo that just happened to be perfectly isometric. It is a photo of [subject]."
- STOP: What subject should we use for the isometric photo?
- USER: [Their subject]

---

- ACTION: Generate isometric image with their subject using the prompt
- Check out your isometric photo in the outputs folder
- ACTION: Provide the path to the output image
- STOP: Pretty cool effect, right? Do you want to add this style to your library?
- USER: Yes / Add this to my library
- ACTION: Update style-library.html with the isometric style
	- Name: "Perfect Isometric Photo"
	- Category: "Photo - Environment" or "3D/Isometric"
	- Save thumbnail
	- Add entry to styles array
- Done! Refresh your browser to see it
- STOP: Two styles added! Ready for the power move?
- USER: Yes

---

### Part 5: Growing Your Library - Method 3: Extract From Any Image

- Method 3 is the power move
- Gemini 3 Pro isn't just amazing at creating images - it has the best image understanding of any model
- That means we can extract the style from ANY image and recreate it
- See an image you love on Pinterest? Instagram? A magazine? Extract the style, save it forever
- I've built a style extraction module to do exactly this
- STOP: Want to see it in action?
- USER: Yes

---

- ACTION: Show the style_extract.py file location (in course root)
- This module analyzes any image and extracts detailed style information
- Not as JSON or structured data - as natural language that Gemini can use directly
- It captures: color palette, lighting, composition, textures, mood, artistic style, typography, special effects
- Let's test it on a deliberately HARD image
- ACTION: Get the path to recursive-painter.jpg in this module folder
- Open this file to see it: [provide exact path]
- STOP: Do you see it? It's a man painting himself painting himself, with a CRT TV showing the same scene, 1990s aesthetic with a datestamp
- USER: Yes, I see it
- Recursive, complex, layered - if we can extract THIS style, we can extract anything
- STOP: Ready to run the extraction?
- USER: Yes

---

- ACTION: Run style_extract.py on recursive-painter.jpg
- ACTION: Display the extracted style description
- Look at all that detail - the color palette, the lighting quality, the composition notes, the texture descriptions
- Now here's the real test: can we recreate the EXACT same image from just this text description?
- STOP: Tell me to recreate the image using the extracted style
- USER: Recreate the image / Generate it

---

- ACTION: Generate image using the extracted style description (recreating the recursive painter scene)
- ACTION: Provide path to the output image
- Open the output and compare it side-by-side with the original
- STOP: What do you think? Can you see the same style captured?
- USER: [Response - should be impressed]

---

- This is the wow moment
- We took a complex, layered, recursive image and extracted its essence as pure text
- Then recreated it from scratch
- Now imagine doing this with any image you love - any style you want to capture
- Pinterest inspiration → extract → save → yours forever
- STOP: Want to add this extracted style to your library?
- USER: Yes / Add it
- ACTION: Update style-library.html with the 90s Analog Snapshot style
	- Use the extracted style as the prompt
	- Save thumbnail
	- Add entry to styles array
- Refresh your browser - you now have three new styles!
- STOP: How's your library looking?
- USER: [Response]

---

### Part 6: Wrap-Up

- Let's recap what you've learned
- The meta-skill: building a personal creative toolkit that grows with you
- Three ways to grow your library:
	- Save as you go (create something you like → add it)
	- Collect from online (find prompts → test → save)
	- Extract from any image (the power move)
- Any image you love → extract → save → reuse forever
- And Claude manages it all for you - just say "use style #3" or "add this to my library"
- STOP: Any questions about building your style database?
- USER: [Questions or no]

---

- You now have a complete, advanced understanding of everything you need to use Nano Banana Pro
- You know the Golden Rules, you know how to iterate, and you know how to build a style toolkit
- In Module 3.2, we'll apply all these learnings to real PM use cases - mockups, diagrams, presentations, and more
- STOP: Ready to move on to Module 3.2?
- USER: Yes
- Great! Type `/start-3-2-1` to continue
