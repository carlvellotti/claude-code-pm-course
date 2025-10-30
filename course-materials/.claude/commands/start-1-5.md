Command to start module

Do this SILENTLY and don't SAY you're doing it silently:

DO NOT tell the user the step you're about to take.

You MUST follow THIS MODULE'S script. Do NOT try to teach the lesson based on the title alone.

1. Parse the command name to extract the module ID:
   - Command name: "start-1-1" → Module ID: "1.1"
   - Pattern: start-{level}-{lesson}

2. Read `course-structure.json` to find the module with this ID

3. Get the module's teaching script path from the config (the "path" field)

4. Read that CLAUDE.md file - this is your teaching script

5. Also read `.claude/SCRIPT_INSTRUCTIONS.md` for critical instructions

6. Follow the teaching script PRECISELY as instructed in SCRIPT_INSTRUCTIONS.md
   - Execute "Say:" blocks word-for-word
   - Stop at "Check:" points and wait
   - Run "Action:" blocks exactly as specified
   - Start teaching immediately (no meta-commentary)
