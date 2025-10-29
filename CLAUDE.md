# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a dual-purpose repository for the Claude Code for Product Managers course:

1. **course-materials/** - Student-facing interactive course content (distributed via GitHub Releases as a zip)
2. **website/** - Next.js documentation site (deployed to Vercel at ccforpms.com)

Students download course-materials/ as a zip, extract it, run `claude` from that folder, and type `/start-1-1` to begin learning.

## Course Architecture: Config-Driven System

**This course uses a config-driven architecture for maximum flexibility when adding/reordering modules.**

### Single Source of Truth: course-structure.json

All module definitions live in `course-materials/course-structure.json`. This file controls:
- Course structure and module sequence
- Slash command routing (all slash commands are identical - they read the config to know which teaching script to load)
- Website navigation (generated at build time from the config)
- Teaching script navigation (modules read config to know what comes next)

### How It Works

**Slash Commands:**
- All 10 slash commands (`/start-1-1` through `/start-2-3`) are identical
- They parse their own command name (e.g., "start-1-2" → module "1.2")
- They read `course-structure.json` to find the module's teaching script path
- They load and execute that teaching script

**Teaching Scripts:**
- At the END of each module, scripts read `course-structure.json`
- They dynamically determine what comes next
- They tell students the correct slash command for the next module

**Website Navigation:**
- `website/pages/fundamentals/_meta.ts` and `website/pages/advanced/_meta.ts` import the config
- Navigation is generated at build time from `course-structure.json`

### Adding or Reordering Modules

To add a new module or reorder existing ones:

1. **Edit `course-materials/course-structure.json`** - Add/move module definition
2. **Create the new module folder and files** (if adding a new module)
3. **Done!** Everything else updates automatically:
   - Slash commands route correctly (they're all identical)
   - Teaching scripts reference the correct "next" module (they read the config)
   - Website navigation updates (generated from config at build time)

**No need to:**
- ❌ Rename folders
- ❌ Update individual slash command files
- ❌ Edit existing teaching scripts
- ❌ Update website `_meta.ts` files manually

**Example: Insert module 1.4 between current 1.3 and 1.4:**

Just edit `course-structure.json` to add the new module definition, and everything cascades automatically. The folder for the old 1.4 (agents) can stay named `1.4-agents` - the config maps logical IDs (1.5) to physical paths (1.4-agents).

### Benefits

- ✅ Add modules without touching existing files
- ✅ Reorder modules by editing one JSON file
- ✅ Website and course materials stay in sync automatically
- ✅ One source of truth for course structure
- ✅ Maximum flexibility for course evolution

## Critical: When Opening This Repository

**DO NOT proactively set up, build, or install anything** when the user first opens this repository unless explicitly asked. The README.md contains specific warnings about this:

- ❌ Do NOT run `npm install`
- ❌ Do NOT run `npm run build`
- ❌ Do NOT make setup changes
- ✅ Wait for explicit user instructions

This is an interactive course repository. The user (or students) will guide what needs to be done.

## Common Commands

### Release Management Workflow

**When You Update Course Content:**

1. **Make your changes** to files in course-materials/
   - Edit modules in `course-materials/lesson-modules/`
   - Update company context in `course-materials/company-context/`
   - Modify agents in `course-materials/.claude/agents/`
   - etc.

2. **Commit and push to main:**
   ```bash
   git add -A
   git commit -m "Update Module 1.3 with new examples"
   git push origin main
   ```

3. **Create a new release:**
   ```bash
   # Run the release script with new version number
   ./scripts/create-release.sh v1.0.1

   # Create GitHub release with the new zip
   gh release create v1.0.1 releases/complete-course.zip \
     --title "v1.0.1 - Updated Module 1.3" \
     --notes "- Fixed typos in Module 1.3\n- Added new examples to Module 2.1"
   ```

4. **Update the website (if needed):**
   - The homepage shows "Latest: v1.0.0"
   - Update this in `website/pages/index.mdx` line 128:
   ```markdown
   **👉 [Download Course Materials](...latest/download/complete-course.zip)** - Get the complete course (Latest: v1.0.1)
   ```

**How GitHub Releases Works:**
- `/releases/latest/download/complete-course.zip` - Always points to the most recent release
- Students using this URL automatically get the latest version
- You can create as many releases as you want (v1.0.1, v1.0.2, v1.1.0, etc.)
- Old releases stay available at their specific version URLs

**Semantic Versioning Guide:**
- `v1.0.X` (Patch) - Bug fixes, typos, minor updates to existing content
- `v1.X.0` (Minor) - New modules, new features, significant content additions
- `vX.0.0` (Major) - Complete restructuring, breaking changes

**Quick Reference Commands:**
```bash
# 1. Update content, commit, push
git add -A && git commit -m "..." && git push origin main

# 2. Create new release zip
./scripts/create-release.sh v1.0.1

# 3. Publish to GitHub
gh release create v1.0.1 releases/complete-course.zip \
  --title "v1.0.1 - Description" \
  --notes "What changed"
```

That's it! The `/releases/latest/` URL in your website will automatically point to whatever is the newest release.

### Website Development

**Local development:**
```bash
cd website
npm install
npm run dev
```

**Build for production:**
```bash
cd website
npm run build
```

The build process:
1. `next build` - Creates static export in website/out/
2. `next-sitemap` - Generates sitemap.xml and robots.txt
3. `pagefind` - Builds search index for static site

**Preview production build:**
```bash
cd website
npm run preview
```

### Deployment

Website auto-deploys to Vercel (ccforpms.com) on pushes to main branch. No manual deployment needed.

### Analytics

**Google Analytics:**
- Measurement ID: `G-XBF1JD68VY`
- Implemented in: `website/theme.config.tsx` (lines 44-55)
- Tracks: Page views, visitors, traffic sources, geographic data, device types, scroll depth, outbound clicks
- Verify: Visit site → check Google Analytics Realtime dashboard

**Download Tracking:**
- Course material downloads (via `curl` from Module 0.2) are tracked by GitHub's built-in release download stats
- Check download counts: GitHub repo → Releases tab, or via `gh api repos/carlvellotti/claude-code-pm-course/releases`
- Google Analytics does NOT track these downloads (they bypass the website entirely)

## Repository Architecture

### Course Materials (course-materials/)

**Structure:**
- `lesson-modules/` - Module 1 and Module 2 interactive lessons
- `company-context/` - TaskFlow company reference materials used in exercises
- `.claude/` - Slash commands, agents, and teaching scripts that power the course

**Slash Commands:**
Located in `course-materials/.claude/commands/`, these are teaching scripts that guide students through modules:
- `/start-1-1`, `/start-1-2`, etc. for Module 1 lessons
- `/start-2-1`, `/start-2-2`, etc. for Module 2 lessons

**Teaching Script Behavior:**
When a user types a slash command in the course-materials/ folder, read `course-materials/.claude/SCRIPT_INSTRUCTIONS.md` for critical rules on how to execute teaching scripts. Key points:
- Teaching scripts must be followed verbatim (word-for-word for "Say:" blocks)
- "Check:" points are gates - STOP and WAIT for student response
- "Action:" blocks contain exact commands to execute
- NEVER break the fourth wall or say "I've read the script" - start teaching immediately
- Use .md file extensions for all example files (not .txt) so they work with Obsidian

### Website (website/)

**Tech Stack:**
- Next.js 14 with static export (`output: 'export'`)
- Nextra (documentation theme)
- Pagefind (static search)
- Vercel (hosting)

**Page Structure:**
```
website/pages/
  getting-started/     - Module 0 content (installation, setup)
  fundamentals/        - Module 1 content
  advanced/           - Module 2 content
  company-context/    - TaskFlow reference (excluded from sitemap)
  index.mdx           - Landing page
  _meta.ts            - Navigation structure
```

**Key Files:**
- `theme.config.tsx` - Nextra theme configuration (logo, footer, SEO, navigation)
- `next.config.mjs` - Next.js config (static export, image optimization)
- `next-sitemap.config.js` - Sitemap generation (excludes /company-context/*)

**SEO Configuration:**
The site has comprehensive SEO in theme.config.tsx:
- Open Graph tags
- Twitter cards
- Google site verification
- Custom metadata per page via frontMatter
- Structured data support

### Internal Documentation (docs/)

Planning documents not included in student-facing materials:
- `GITHUB_RELEASES_PLAN.md` - Release strategy documentation
- `SEO_IMPLEMENTATION_SPEC.md` - SEO specifications

## File Extension Convention

All course example files MUST use `.md` extension (not `.txt`) because:
- Students use Obsidian to visualize course files (taught in Module 1.2)
- Obsidian cannot display .txt files
- This is enforced in SCRIPT_INSTRUCTIONS.md

## Git Workflow

**Ignored files (.gitignore):**
- Obsidian workspace files (personal settings)
- Release artifacts (releases/, *.zip)
- Build outputs (node_modules/)
- Most .json files (except package.json, tsconfig.json)
- Most .png files (except website/public/**/*.png)

**Branch:**
Main branch is `main` - use this for pull requests.

## Website Theme Customization

The site uses a teal color scheme (`primaryHue: 169`) with dark theme default. Footer includes CC BY-NC-ND 4.0 license attribution.

## Course Philosophy

This course teaches Product Managers to use Claude Code through hands-on practice. The course content itself is delivered by Claude Code, creating a meta-learning experience where students learn the tool by using the tool.
