# Update Links to Translated Documents

I will update all translated Markdown (`.zh.md`) and MDX (`.zh.mdx`) files to reference their Chinese counterparts instead of the English files.

## Plan
1.  **Create a Python Script**: I will create a script `scripts/update_links_to_zh.py` that:
    -   Scans all `*.zh.md` and `*.zh.mdx` files in the repository.
    -   Identifies file paths ending in `.md` or `.mdx` within the content.
    -   Checks if a corresponding `.zh.md` or `.zh.mdx` file exists (handling relative paths and the `course-materials` root context).
    -   Updates the reference only if the Chinese file exists.
2.  **Execute the Script**: Run the script to perform the batch update.
3.  **Verify**: Check a few key files (e.g., `CLAUDE.zh.md`, `README.zh.md`) to ensure links are correctly updated.
4.  **Cleanup**: Remove the temporary script.

This ensures that all internal links in the Chinese documentation point to the Chinese versions of the files, providing a seamless experience.
