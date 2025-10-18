# Vercel Deployment Settings

## Exact Settings to Use in Vercel Dashboard

When importing the project on Vercel, use these EXACT settings:

### Project Settings
```
Project Name: claude-code-pm-course (or whatever you prefer)
```

### Build & Development Settings
```
Framework Preset:     Next.js
Root Directory:       website
Build Command:        npm run build
Output Directory:     out  
Install Command:      npm install
```

### Important Notes

1. **Root Directory MUST be `website`** - This is critical!
2. All other settings should auto-detect correctly
3. Don't add a custom `vercel.json` file
4. Node.js version: 18.x or higher (should auto-detect)

## If Build Still Fails

Look for the error in the build logs. Common issues:

### Error: "Cannot find module" or "Module not found"
- Check that all files committed to git
- Verify `node_modules` is in `.gitignore`

### Error: "_meta.json not supported"
- Already fixed - make sure you pulled latest from main
- Should only have `_meta.ts` files, no `_meta.json`

### Error: "YAML parsing error" in frontmatter
- Already fixed - all frontmatter uses single quotes
- Check for any `<` or `>` symbols outside code blocks

### Build succeeds but site is blank
- Check Output Directory is set to `out`
- Verify `/out` directory contains HTML files after build

## Testing Locally

To test the exact build Vercel will run:

```bash
cd /Users/carl/claude-code-pm-course/website
rm -rf .next out node_modules
npm install
npm run build

# Check that out/ directory has content:
ls -la out/
```

If that works locally, it should work on Vercel.

## Share the Error

If still failing, share:
1. Screenshot of Vercel build settings
2. Copy/paste the error from build logs
3. I'll fix it immediately!

