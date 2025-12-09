# Module 3.1.3: Consistency & Style - Outline

## Files Needed to Start
- `image_gen.py` - Pre-built image generation module (in course root)
- `.env` - Already configured with API key
- `style-reference``.``jpeg` - Epic basketball landing page for style reference demo
- `Winter 1.JPG`, `Winter 2.jpg`, `Winter 3.jpg` - Photos of Winter (black fluffy cat)
- `Piper 1.jpg`, `Piper 2.jpg` - Photos of Piper (gray/cream fluffy cat)

## Files Created During Module
- `outputs/output_*_[descriptive-name].png` - Generated images with meaningful names

## High-Level Overview

**Part 1: Golden Rules of Prompting**
- Introduce the 4 Golden Rules from Google's official guide:
  1. Edit, Don't Re-roll - if 80% correct, ask for specific changes instead of starting over (we covered this in 3.1.2 - works because Gemini 3 Pro is a thinking model and continuing the conversation gives it more context)
  2. Use Natural Language & Full Sentences - brief like a human artist, not "tag soup". You will see libraries of JSON prompts out there, but that's an outdated way of working with Gemini. Now that it's a powerful thinking model, it doesn't need JSON structuring.
  3. Be Specific and Descriptive - define subject, setting, lighting, mood, textures/materials
  4. Provide Context - tell the "why" or "for whom" so the thinking model makes smarter decisions
- Say we'll demonstrate the remaining 3 rules one by one – for each of these run BOTH at the same time to save time, take a look at them yourself, and tell the user where they are and exactly what they are called, and ask them to review them. Unless we must show existing reference images, ask the users what concepts they want to work with.
- Demo: Natural Language vs Tag Soup (Rule 2) - ask user what they want to make an image about, show bad tag-soup prompt vs natural language, generate both. If they are very similar you can say that realistically both create good results, but it's more natural work with natural language.
- Demo: Specific and Descriptive (Rule 3) - ask user what they next want to create, then generate vague version vs specific detailed prompt, tell user what prompts you are using, and compare results. Go crazy with the amount of detail to really show users what gemini can do. Add that Gemini can handle A LOT of description and is very consistent so don't be afraid to be extremely detailed. Claude can help you with this.
- Demo: Provide Context (Rule 4) - ask user what they want to create, give them some options for the why, then generate both versions, 1 without the why and one with, review them yourself, comment on the differences

**Part 2: Reference Images**
- Demo: Single reference - use `style-reference``.``jpeg` to generate something new in that style
- Demo: Multi-image - combine style-reference.``jpeg + all cat photos (Winter 1-3, Piper 1-2) to create an epic "APEX CAT" cat food landing page featuring Winter and Piper
- Note: Providing multiple reference images of the same subject gives better results - the model can understand the subject from different angles/lighting and represent it more accurately

**Part 3: \****Grids and Variants**
- Demo: Grid generation - ask users to tell you to use Winter photos to generate a 3x3 video game character sprite sheet (9 poses/actions). Great for consistency across different angles/poses.
- Demo: Generating variants - let user pick any concept from earlier demos and generate 2-3 variants of it. Pick the best one, then iterate on that in its session.

---

## Notes for Claude (when running this module)
- Use descriptive names when saving outputs (e.g., `coffee_shop_warm_light.png` not just sequential numbers)
- When generating variants, name them clearly (e.g., `persona_variant_1.png`, `persona_variant_2.png`)

---
## Teaching Flow
 
- Welcome back! You've seen how to generate and iterate on images
- Now let's level up - we're going to learn about consistency and style
- By the end of this module you'll know how to write prompts like a pro, use reference images, and generate variants
- STOP: Ready to begin?
- USER: Ready

---

### Part 1: Golden Rules of Prompting

- Google released an official guide for prompting Gemini's image generation
- They call them the "Golden Rules" - there are four of them
- **Rule 1: Edit, Don't Re-roll** - if 80% correct, ask for specific changes instead of starting over (we covered this in 3.1.2)
- **Rule 2: Use Natural Language & Full Sentences** - brief it like a human artist, not "tag soup." You'll see JSON prompt libraries out there, but that's outdated - Gemini is a thinking model now and doesn't need rigid structuring
- **Rule 3: Be Specific and Descriptive** - define subject, setting, lighting, mood, textures, materials
- **Rule 4: Provide Context** - tell the "why" or "for whom" so the thinking model makes smarter decisions
- STOP: Make sense so far?
- USER: Yes

---

- We already covered Rule 1 in the last module - it works because Gemini is a thinking model and continuing the conversation gives it more context
- Now let's see the other three rules in action with side-by-side comparisons
- For each rule, I'll generate two versions simultaneously so you can see the difference
- You'll pick the concepts - I'll show you the technique
- STOP: Ready to see these in action?
- USER: Yes

---

- Let's start with **Rule 2: Natural Language vs Tag Soup**
- STOP: What concept would you like to see this demonstrated with? Give me a subject or scene.
- USER: [Provides concept]
 
---
 
- Perfect, I'll show you the difference between tag soup and natural language
- I'm going to generate both versions simultaneously so we can compare
- ACTION: Generate two images in parallel:
  - Tag soup version: comma-separated keywords, no sentences
  - Natural language version: full sentences describing the same scene
- ACTION: Save both images with descriptive names
- Tell users what prompts you used
- Check both images in your `outputs/` folder:
  - `[concept]_tag_soup.png`
  - `[concept]_natural_language.png`
- STOP: Take a look - what do you notice?
- USER: [Describes observations]
 
---
 
- You might notice they're actually pretty similar
- Realistically, both approaches can produce good results
- But natural language is just... easier to work with
- You don't have to memorize special syntax or formatting
- Just describe what you want like you're talking to a designer
- STOP: Ready for the next rule?
- USER: Yes
 
---
 
- **Rule 3: Be Specific and Descriptive**
- Define the subject, setting, lighting, mood, textures, materials
- Gemini can handle A LOT of description - don't hold back
- It's surprisingly consistent even with very detailed prompts
- Claude can help you craft these detailed descriptions
- STOP: What would you like to create for this demo? Give me a new concept.
- USER: [Provides concept]
 
---
 
- Great choice. I'll show you vague vs detailed prompts
- For the vague version, I'll use a simple one-sentence description
- For the detailed version, I'm going to go all out - we're talking lighting, textures, atmosphere, materials, everything
- ACTION: Generate two images in parallel:
  - Vague prompt: simple, minimal description
  - Detailed prompt: extensive description with lighting, mood, textures, materials, atmosphere, composition
- ACTION: Save both images with descriptive names
- Here's what I used for each prompt: [share the prompts]
- Check your `outputs/` folder:
  - `[concept]_vague.png`
  - `[concept]_detailed.png`
- ACTION: View the images yourself
- STOP: Compare them - see the difference detail makes?
- USER: [Responds]
 
---
 
- The detailed version gives Gemini so much more to work with
- And here's the thing - it actually follows through on all those details
- Don't be afraid to be extremely specific
- If you're not sure how to be more detailed, just ask Claude to help expand your prompt
- STOP: Ready for the last rule?
- USER: Yes
 
---
 
- **Rule 4: Provide Context**
- Tell the "why" or "for whom" so the thinking model makes smarter decisions
- Context helps Gemini understand the purpose and make appropriate creative choices
- STOP: What would you like to create? I'll give you some options for context we can add.
- USER: [Provides concept]
 
---
 
- Nice. Here are some context options we could add [generate these dynamically based on what would make sense for the user]:
  - "For a children's book illustration"
  - "For a luxury brand advertisement"
  - "For a tech startup landing page"
  - "For a vintage poster design"
- STOP: Pick one, or suggest your own context
- USER: [Picks context]
 
---
 
- I'll generate one without context and one with your chosen context
- ACTION: Generate two images in parallel:
  - No context: just the subject description
  - With context: same subject plus the "why" / "for whom"
- ACTION: Save both images with descriptive names
- ACTION: Review both images and identify specific differences
- Here's what I noticed: [share observations about how context influenced the result]
- Check your `outputs/` folder:
  - `[concept]_no_context.png`
  - `[concept]_with_context.png`
- STOP: See how the context changed the creative direction?
- USER: [Responds]
 
---
 
- That wraps up the Golden Rules:
  - Edit, don't re-roll
  - Use natural language
  - Be specific and descriptive
  - Provide context
- Keep these in mind for all your image generation work
- STOP: Ready to move on to reference images?
- USER: Yes
 
---
 
### Part 2: Reference Images
 
- Now we're getting into the really powerful stuff
- You can provide Gemini with reference images to guide the style or subject
- Let's start with a single style reference
- ACTION: Read the `style-reference.jpeg` file to understand its visual style
- Tell user where to find it
- This is an epic basketball landing page - bold, dynamic, high-energy design
- STOP: What would you like me to create in this style? Give me a different subject.
- USER: [Provides subject]
 
---
 
- ACTION: Generate an image using `style-reference.jpeg` as a style reference with the user's subject
- ACTION: Save with descriptive name
- Check `outputs/` for your styled image
- STOP: Take a look - see how it captured the visual style but with your subject?
- USER: [Responds]
 
---
 
- This is incredibly useful for brand consistency
- Got a style you love? Just feed it in as a reference
- Now let's try something more advanced - multiple reference images
- We're going to create an epic cat food landing page called "APEX CAT" Carl's cats Winter and Piper
- ACTION: Tell users where they can see the cat images.
- STOP: Did you find Winter and Piper?
- USER: [Confirms]
- I'll combine:
	- The `style-reference.jpeg` for the bold, dynamic visual style
	- Photos of Winter (the black fluffy cat) - 3 reference photos
	- Photos of Piper (the gray/cream fluffy cat) - 2 reference photos
- Pro tip: providing multiple reference photos of the same subject gives much better results - the model can understand the subject from different angles and lighting
- ACTION: Generate an "APEX CAT" landing page combining style reference + all 5 cat photos
- ACTION: Save with descriptive name like `apex_cat_landing_page.png`
- Check your `outputs/` folder for the result
- STOP: What do you think? See how it captured both cats' likeness in the landing page style?
- USER: [Responds]
 
---
 
- That's the power of reference images
- Single reference for style, multiple references for better subject accuracy
- You can mix and match - style from one image, subjects from others
- STOP: Ready for Part 3 - grids and variants?
- USER: Yes
 
---
 
### Part 3: Grids and Variants
 
- Sometimes you need multiple views or variations of the same subject
- Grids are perfect for this - character sheets, sprite sheets, product angles
- Let's create a 3x3 video game character sprite sheet using Winter
- STOP: Ask me to generate a character sprite sheet using the Winter photos
- USER: Generate a character sprite sheet using the Winter photos
 
---
 
- ACTION: Generate a 3x3 grid sprite sheet using Winter reference photos
  - 9 different poses/actions of Winter as a video game character
  - Consistent style across all 9 cells
- ACTION: Save as `winter_sprite_sheet.png`
- Check your `outputs/` folder for the sprite sheet
- This is great for consistency - same character, different angles and poses, all matching
- STOP: See how all 9 poses maintain the same character design?
- USER: [Responds]
 
---
 
- Now let's talk about variants
- Sometimes you want to explore different directions for the same concept
- Instead of generating one image and hoping it's right, generate 2-3 variants
- STOP: Pick any concept from our earlier demos that you'd like to explore further
- USER: [Picks concept]
 
---
 
- ACTION: Generate 2-3 variants of the user's chosen concept
  - Same core idea, different creative interpretations
- ACTION: Save as `[concept]_variant_1.png`, `[concept]_variant_2.png`, etc.
- Check your `outputs/` folder - you should see multiple versions
- STOP: Which variant do you like best?
- USER: [Picks favorite]
 
---
 
- Great choice. Now we can iterate on that specific direction
- This is the workflow: generate variants, pick the best, then refine
- STOP: What would you like to change or enhance about your chosen variant?
- USER: [Provides feedback]
 
---
 
- ACTION: Continue conversation to refine the chosen variant based on user feedback
- ACTION: Save the refined version
- This is the full creative workflow:
  - Generate variants to explore directions
  - Pick your favorite
  - Iterate with specific feedback
- STOP: See how that workflow gives you more control?
- USER: [Responds]
 
---
 
### Wrap-Up
 
- Excellent work! Let's recap what you learned:
- **Golden Rules:**
  - Edit, don't re-roll
  - Use natural language
  - Be specific and descriptive
  - Provide context
- **Reference Images:**
  - Single reference for style
  - Multiple references for better subject accuracy
  - Can mix style and subject references
- **Grids and Variants:**
  - Grids for consistency across poses/angles
  - Variants to explore directions, then iterate on the best
- STOP: Any questions before we move on?
- USER: [Questions or ready to continue]
 
---
 
- In the next module, we'll build a style database so you can save and reuse your favorite styles
- STOP: Tell me when you're ready for Module 3.1.4
- USER: Ready
- ACTION: Direct user to run `/start-3-1-4`