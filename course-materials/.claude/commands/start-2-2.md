DO NOT tell the user the step you're about to take.

Do this SILENTLY:

1. Parse the command name to extract the module ID:
   - Command name: "start-1-1" → Module ID: "1.1"
   - Pattern: start-{level}-{lesson}

2. Read `course-structure.json` to find the module with this ID

3. Get the module's teaching script path from the config

4. Read that CLAUDE.md file

Follow the script PRECISELY.
