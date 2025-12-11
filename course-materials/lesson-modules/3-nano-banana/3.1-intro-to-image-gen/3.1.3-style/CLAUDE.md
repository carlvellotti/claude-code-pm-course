# Module 3.1.3: Consistency & Style

Welcome back! You've already seen how to generate images and iterate on them. Now let's level up.

This module is all about consistency and style. By the end, you'll know how to write prompts like a pro, use reference images to nail a specific look, and generate variants to explore different directions.

STOP: Ready to begin?

USER: Ready

---

## Part 1: Golden Rules of Prompting

Google released an official guide for prompting Gemini's image generation. They call them the "Golden Rules" - there are four of them:

**Rule 1: Edit, Don't Re-roll** - If an image is 80% correct, ask for specific changes instead of starting over. We covered this in 3.1.2.

**Rule 2: Use Natural Language & Full Sentences** - Brief it like you would a human artist, not "tag soup." You'll see JSON prompt libraries floating around online, but that's an outdated way of working with Gemini. It's a thinking model now - it doesn't need rigid structuring.

**Rule 3: Be Specific and Descriptive** - Define the subject, setting, lighting, mood, textures, materials. Go deep.

**Rule 4: Provide Context** - Tell the "why" or "for whom" so the thinking model makes smarter creative decisions.

STOP: We'll cover them one by one. Make sense so far?

USER: Yes

---

We already covered Rule 1 in the last module - it works because Gemini is a thinking model, and continuing the conversation gives it more context to work with.

Now let's see the other three rules in action. For each one, I'll generate two versions simultaneously so you can see the difference side-by-side.

You'll pick the concepts - I'll show you the technique.

STOP: Ready to see these in action?

USER: Yes

---

### Rule 2: Natural Language vs Tag Soup

Let's start with Rule 2.

"Tag soup" is the style of prompting that became popular with earlier image models like Midjourney and Stable Diffusion - comma-separated keywords jammed together:

```
cat, orange tabby, sitting, window, sunlight, cozy, warm lighting, 8k, hyperrealistic, bokeh, soft focus
```

Natural language is just... writing normally:

```
An orange tabby cat sitting on a windowsill, bathed in warm afternoon sunlight. The scene feels cozy and intimate, with soft focus on the background.
```

Both can work, but Gemini was trained on natural language. Let's see the difference.

STOP: What concept would you like to see this demonstrated with? Give me a subject or scene - anything you want.

USER: [Provides concept]

---

Perfect. I'll show you the difference between tag soup and natural language.

I'm generating both versions right now so we can compare them directly.

ACTION: Generate two images in parallel:
- Tag soup version: comma-separated keywords, no sentences
- Natural language version: full sentences describing the same scene

ACTION: Save both images with descriptive names

Here's what I used for each prompt:
- **Tag soup:** [share the tag soup prompt]
- **Natural language:** [share the natural language prompt]

Check both images in your `outputs/` folder:
- `[concept]_tag_soup.png`
- `[concept]_natural_language.png`

STOP: Take a look at both - what do you notice?

USER: [Describes observations]

---

You might notice they're actually pretty similar. That's kind of the point.

Both approaches can produce good results. But natural language is just... easier. You don't have to memorize special syntax or worry about formatting. Just describe what you want like you're talking to a designer. And remember, I can always help you write these prompts as well.

STOP: Ready for the next rule?

USER: Yes

---

### Rule 3: Be Specific and Descriptive

This one's fun. Rule 3 is about defining the subject, setting, lighting, mood, textures, materials - all of it.

Here's the thing about Gemini: it can handle A LOT of description. Like, way more than you'd think. And it's surprisingly consistent even with very detailed prompts.

Don't hold back. And if you're ever not sure how to add more detail, just ask me - I can help expand your prompts.

STOP: What would you like to create for this demo? Give me a new concept.

USER: [Provides concept]

---

Great choice. I'll show you vague vs detailed.

For the vague version, I'll use a simple one-sentence description. For the detailed version, I'm going all out - lighting, textures, atmosphere, materials, composition, everything.

ACTION: Generate two images in parallel:
- Vague prompt: simple, minimal description
- Detailed prompt: extensive description with lighting, mood, textures, materials, atmosphere, composition

ACTION: Save both images with descriptive names

Here's what I used:
- **Vague:** [share the vague prompt]
- **Detailed:** [share the detailed prompt - show them how crazy detailed you went]

ACTION: View the images yourself and note the differences

Check your `outputs/` folder:
- `[concept]_vague.png`
- `[concept]_detailed.png`

STOP: Compare them - see the difference detail makes?

USER: [Responds]

---

The detailed version gives Gemini so much more to work with. And here's what's cool - it actually follows through on all those details. The lighting you specified? It's there. The textures? There.

Don't be afraid to be extremely specific. If you're ever stuck, just ask me to help expand your prompt.

STOP: Ready for the last rule?

USER: Yes

---

### Rule 4: Provide Context

This one is about telling Gemini the "why" or "for whom."

Context helps the model understand the purpose and make appropriate creative choices. A portrait "for a children's book" looks very different from a portrait "for a luxury brand advertisement."

STOP: What would you like to create? I'll give you some context options we can add.

USER: [Provides concept]

---

Nice. Here are some context options that would work well with that:

ACTION: Generate context options dynamically based on what makes sense for the user's concept (e.g., "for a children's book illustration", "for a luxury brand advertisement", "for a tech startup landing page", "for a vintage poster design")

STOP: Pick one of these, or suggest your own context.

USER: [Picks context]

---

I'll generate one without context and one with your chosen context.

ACTION: Generate two images in parallel:
- No context: just the subject description
- With context: same subject plus the "why" / "for whom"

ACTION: Save both images with descriptive names

ACTION: Review both images and identify specific differences

Here's what I noticed: [share observations about how context influenced the result - be specific about what changed]

Check your `outputs/` folder:
- `[concept]_no_context.png`
- `[concept]_with_context.png`

STOP: See how the context changed the creative direction?

USER: [Responds]

---

That wraps up the Golden Rules:
1. **Edit, don't re-roll** - iterate on what's working
2. **Use natural language** - talk to it like a designer
3. **Be specific and descriptive** - Gemini can handle the detail
4. **Provide context** - tell it the "why"

Keep these in mind for all your image generation work. They'll make a real difference.

STOP: Ready to move on to reference images?

USER: Yes

---

## Part 2: Reference Images

Now we're getting into the really powerful stuff.

You can provide Gemini with reference images to guide the style or subject. This is huge for brand consistency, recreating specific looks, or getting characters to look right.

Let's start with a single style reference.

ACTION: Read the `style-reference.jpeg` file to understand its visual style

ACTION: Tell user where to find `style-reference.jpeg` so they can view it

This is an epic basketball landing page - bold, dynamic, high-energy design. Great visual style.

STOP: What would you like me to create in this style? Give me a completely different subject.

USER: [Provides subject]

---

ACTION: Generate an image using `style-reference.jpeg` as a style reference with the user's subject

ACTION: Save with descriptive name

Check `outputs/` for your styled image.

STOP: Take a look - see how it captured that bold, dynamic visual style but with your subject?

USER: [Responds]

---

This is incredibly useful for brand consistency. Got a style you love? Just feed it in as a reference.

Now let's try something more advanced - multiple reference images.

We're going to create an epic cat food landing page called "APEX CAT" featuring Carl's cats Winter and Piper.

ACTION: Tell users where they can find the cat images (Winter 1-3, Piper 1-2)

STOP: Did you find Winter and Piper?

USER: [Confirms]

---

I'll combine:
- The `style-reference.jpeg` for that bold, dynamic visual style
- Photos of Winter (the black fluffy cat) - all 3 reference photos
- Photos of Piper (the gray/cream fluffy cat) - both reference photos

Pro tip: providing multiple reference photos of the same subject gives much better results. The model can understand the subject from different angles and lighting conditions, which helps it represent them more accurately.

ACTION: Generate an "APEX CAT" landing page combining style reference + all 5 cat photos

ACTION: Save with descriptive name like `apex_cat_landing_page.png`

Check your `outputs/` folder for the result.

STOP: What do you think? See how it captured both cats' likeness in that landing page style?

USER: [Responds]

---

That's the power of reference images:
- **Single reference** for style
- **Multiple references** for better subject accuracy
- **Mix and match** - style from one image, subjects from others

STOP: Ready for Part 3 - grids and variants?

USER: Yes

---

## Part 3: Grids and Variants

Sometimes you need multiple views or variations of the same subject. Grids are perfect for this - character sheets, sprite sheets, product angles, you name it.

Let's create a 3x3 video game character sprite sheet using Winter.

STOP: Go ahead and ask me to generate a character sprite sheet using the Winter photos.

USER: Generate a character sprite sheet using the Winter photos

---

ACTION: Generate a 3x3 grid sprite sheet using Winter reference photos
- 9 different poses/actions of Winter as a video game character
- Consistent style across all 9 cells

ACTION: Save as `winter_sprite_sheet.png`

Check your `outputs/` folder for the sprite sheet.

This is great for consistency - same character, different angles and poses, all matching the same design language.

STOP: See how all 9 poses maintain the same character design?

USER: [Responds]

---

Let's try one more grid - and this one's a bit meta.

We just learned the Golden Rules of prompting. What if we used image generation to create teaching slides about those very rules?

STOP: Ask me to generate an 8-slide presentation about the Golden Rules.

USER: Generate an 8-slide presentation about the Golden Rules

---

ACTION: Generate a 2x4 grid (8 slides) teaching the Golden Rules of prompting
- Slide 1: Title slide - "Golden Rules of Image Prompting"
- Slide 2: Overview - the 4 rules at a glance
- Slides 3-6: One slide per rule with visual example
- Slide 7: Quick reference cheat sheet
- Slide 8: "Now go create!" closing slide
- Consistent visual style across all slides

ACTION: Save as `golden_rules_slides.png`

Check your `outputs/` folder for the slides.

See what we did there? We used the tool to create teaching content about the tool. Grids are incredibly useful for presentations, tutorials, or any content that needs visual consistency.

STOP: Pretty meta, right? Ready to move on to variants?

USER: [Responds]

---

Now let's talk about variants.

Here's something important: anything with LLMs has inherent randomness, and this is espeically true with image generation. Even with the exact same prompt, you'll get different results each time.

You can treat this as a feature, not a bug.

Instead of generating one image and hoping it's right, generate 2-3 variants with the same prompt. Then pick your favorite and iterate on that one.

STOP: Pick any concept from our earlier demos that you'd like to explore further. You can check the `outputs/` folder if you need a reminder.

USER: [Picks concept]

---

ACTION: Generate 3 variants of the user's chosen concept using the SAME prompt each time
- Call new_session() before each generation to ensure fresh results
- Use identical prompts to demonstrate the natural variation

ACTION: Save as `[concept]_variant_1.png`, `[concept]_variant_2.png`, `[concept]_variant_3.png`

Check your `outputs/` folder - you should see three different versions from the same prompt.

STOP: Which variant do you like best?

USER: [Picks favorite]

---

Great choice. Now we can iterate on that specific direction.

This is the workflow: generate variants, pick the best, then refine.

STOP: What would you like to change or enhance about your chosen variant?

USER: [Provides feedback]

---

ACTION: Continue the session to refine the chosen variant based on user feedback

ACTION: Save the refined version

This is the full creative workflow:
1. **Generate variants** to explore directions
2. **Pick your favorite**
3. **Iterate with specific feedback**

STOP: See how that workflow gives you more control over the creative direction?

USER: [Responds]

---

## Wrap-Up

Excellent work! Let's recap what you learned:

**Golden Rules:**
- Edit, don't re-roll
- Use natural language
- Be specific and descriptive
- Provide context

**Reference Images:**
- Single reference for style
- Multiple references for better subject accuracy
- Mix and match style and subject references

**Grids and Variants:**
- Grids for consistency across poses/angles
- Variants to explore directions, then iterate on the best

STOP: Any questions before we move on?

USER: [Questions or ready to continue]

---

In the next module, we'll build a style database so you can save and reuse your favorite styles. You'll learn how to deconstruct existing images and build your own creative toolkit.

STOP: Tell me when you're ready for Module 3.1.4

USER: Ready

Run `/start-3-1-4` to continue.

---

## Important Notes for Claude

When running this module:

1. **Descriptive file names** - Always use meaningful names when saving outputs (e.g., `coffee_shop_warm_light.png` not just sequential numbers)

2. **Share your prompts** - When generating comparison images, always show the user what prompts you used so they can learn from the technique

3. **View images yourself** - For demos where you need to comment on differences, actually look at the generated images and provide specific observations

4. **Dynamic context options** - When offering context options for Rule 4, generate options that make sense for the user's specific concept

5. **Cat photo locations** - The cat photos (Winter 1-3, Piper 1-2) and style-reference.jpeg are in the module folder. Tell users the exact path.

6. **Variants workflow** - When generating variants, use the same prompt each time to demonstrate natural randomness

7. **Opening images** - If a user is having trouble finding an image, offer to open it for them using `open [path]` (Mac) or `start [path]` (Windows)

## Success Criteria

Module is complete when:
- [ ] User has seen all 4 Golden Rules explained
- [ ] User has completed 3 comparison demos (tag soup vs natural language, vague vs detailed, no context vs with context)
- [ ] User has used a single style reference
- [ ] User has seen the multi-image APEX CAT demo
- [ ] User has generated a grid/sprite sheet
- [ ] User has generated variants and iterated on their favorite
- [ ] User is directed to `/start-3-1-4`
