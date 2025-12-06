# Outline → Teaching Script

**Purpose:** Final conversion of your outline to CLAUDE.md

By now your outline has the full teaching flow. Expand the dialogue into natural conversational language while keeping all control markers.

---

## Keep the Control Markers

The prefixes from Step 2 stay exactly the same:

- **ACTION:** - What Claude does (read files, run commands, generate images)
- **STOP:** - Wait for student response (questions, confirmations, gates)
- **USER:** - Expected student input

These markers tell Claude when to pause, when to act, and what to expect. Without them, Claude will just keep talking.

---

## Expand the Dialogue

The plain text (no prefix) becomes natural conversation:

**Outline:**
```
- Welcome to Nano Banana!
- I'm going to quote the course creator Carl here: "You aren't going to believe how fucking amazing this is"
- We're going to use Gemini 3 Pro
- STOP: Are you ready to see what it can do?
- USER: Yes / Ready
```

**CLAUDE.md:**
```
Welcome to Nano Banana!

I'm going to quote the course creator Carl here: "You aren't going to believe how fucking amazing this is."

And honestly? He's right. We're going to use Gemini 3 Pro - Google's most advanced image generation model.

STOP: Are you ready to see what it can do?

USER: Yes / Ready
```

The dialogue flows naturally, but the STOP and USER markers remain intact.

---

## Writing Style

- Conversational tone with contractions ("you'll", "let's", "don't")
- Varied sentence length (short punchy + longer flowing)
- Simple language, friend-over-coffee vibe
- Relatable metaphors over jargon
- Direct and confident, not hedging ("I'll show you" not "I can try to show you")

---

## Critical Rules

1. **No fourth-wall breaking** - Never say "I've read the script" or reference instructions
2. **Permission prompts** - Warn once on first bash command, never again
3. **Terminal limits** - Can't display files/images; tell users where to find them

---

## Add to Bottom of Script

- **Important Notes for Claude** - Edge cases, troubleshooting
- **Success Criteria** - What "done" looks like

---

## Create Slash Command

`.claude/commands/start-X-Y.md`:
```
Do this SILENTLY: read `lesson-modules/X.Y-name/CLAUDE.md`
Follow the script PRECISELY.
```

---

## Quick Check

- [ ] Natural conversational flow
- [ ] No fourth-wall breaking
- [ ] Slash command created
