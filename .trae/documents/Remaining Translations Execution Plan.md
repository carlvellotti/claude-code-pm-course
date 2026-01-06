# Translation Execution Plan

Based on the `repo-translation-plan.md` and current repository status, here is the plan to complete the remaining translations.

## Current Status
- **Completed:** Most of `course-materials/lesson-modules/1-fundamentals` and some root files.
- **Pending:** `course-materials` (Modules 2 & 3, .claude), `website` content, `docs/`, and root documentation.

## Phases

### Phase 1: Course Materials (High Priority)
Translate remaining student-facing materials.
- **Targets:**
  - `course-materials/lesson-modules/2-advanced-pm-work/**` (Markdown files)
  - `course-materials/lesson-modules/3-nano-banana/**` (Markdown files)
  - `course-materials/.claude/**` (Agents, Commands, Skills)

### Phase 2: Website Content
Translate website pages for the documentation site.
- **Targets:**
  - `website/pages/**/*.mdx` (Create `*.zh.mdx`)
  - `website/DEPLOY.md`, `website/VERCEL_SETTINGS.md`

### Phase 3: Root & Project Documentation
Translate high-level project documentation.
- **Targets:**
  - `README.md`, `CLAUDE.md`, `TEST_COMMANDS.md`
  - `docs/SEO_IMPLEMENTATION_SPEC.md`, `docs/GITHUB_RELEASES_PLAN.md`

### Phase 4: Code Comments
Translate code comments and log strings (in-place).
- **Targets:**
  - `website/components/EmailPopup.jsx`
  - `website/fix-frontmatter.py`
  - `course-materials/lesson-modules/3-nano-banana/**/*.py`
  - `scripts/*.sh`

## Execution Strategy
1.  I will create a comprehensive **Todo List** to track these files.
2.  I will process files in **batches**, reading the source, translating the content (preserving frontmatter/code), and writing the new `*.zh.md` or `*.zh.mdx` file.
3.  For code files, I will edit them **in-place** to translate comments/logs.
