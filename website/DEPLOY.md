# Deploying to Vercel

The site is ready to deploy! Here are your options:

## Quick Deploy (Recommended)

### Option 1: Deploy via Vercel Dashboard

1. **Push to GitHub** (if you haven't already):
   ```bash
   cd /Users/carl/claude-code-pm-course
   git add website/
   git commit -m "Add Nextra documentation website"
   git push origin main
   ```

2. **Go to Vercel**:
   - Visit https://vercel.com/new
   - Sign in with GitHub
   - Click "Import Project"
   - Select your repository: `carlvellotti/claude-code-pm-course`

3. **Configure Build Settings**:
   - **Root Directory**: `website`
   - **Framework Preset**: Next.js
   - **Build Command**: `npm run build` (default is fine)
   - **Output Directory**: `out`
   - **Install Command**: `npm install` (default is fine)

4. **Deploy**:
   - Click "Deploy"
   - Wait ~2-3 minutes for build
   - Your site will be live at `https://your-project.vercel.app`

5. **Custom Domain** (Optional):
   - In Vercel dashboard, go to Settings → Domains
   - Add your custom domain
   - Follow DNS instructions

## Option 2: Deploy via Vercel CLI

```bash
# Install Vercel CLI globally
npm install -g vercel

# Navigate to website directory
cd /Users/carl/claude-code-pm-course/website

# Login to Vercel (first time only)
vercel login

# Deploy to preview
vercel

# Deploy to production
vercel --prod
```

## What Gets Deployed

Your built site includes:
- ✅ All course content (20 pages)
- ✅ Left sidebar navigation
- ✅ Right-side table of contents
- ✅ Client-side search (Pagefind)
- ✅ Company context section
- ✅ All images
- ✅ Responsive mobile layout
- ✅ Fast static site (no server needed)

## Post-Deployment

After deploying:

1. **Test the site**:
   - Check all navigation links work
   - Test search functionality
   - Verify images load correctly
   - Test on mobile

2. **Update README** with live URL

3. **Share the link**!

## Updating Content

To update the website after deployment:

1. Edit REFERENCE_GUIDE.md files in `/lesson-modules/`
2. Run conversion script:
   ```bash
   cd /Users/carl/claude-code-pm-course/website
   ./convert-content.sh
   ```
3. Build and test locally:
   ```bash
   npm run build
   npm run preview  # Test locally
   ```
4. Commit and push:
   ```bash
   git add .
   git commit -m "Update course content"
   git push
   ```
5. Vercel will automatically rebuild and redeploy!

## Troubleshooting

### Build fails on Vercel
- Check build logs in Vercel dashboard
- Ensure `website/` is set as root directory
- Verify Node.js version (should be 18+)

### Search doesn't work
- Pagefind runs in `postbuild` script
- Check that `/pagefind/` directory exists in build output
- Clear browser cache

### Images not loading
- Images should be in `/public/images/`
- Referenced as `/images/filename.png` in MDX files
- Check browser console for 404 errors

## Environment Variables

None needed! This is a static site with no backend or secrets.

## Cost

**Vercel Free Tier includes:**
- Unlimited deployments
- 100 GB bandwidth/month
- Automatic HTTPS
- Custom domains
- Preview deployments for PRs

Your static documentation site will easily fit in the free tier.

---

**Ready to deploy?** Follow Option 1 above (Vercel Dashboard) - it's the easiest! 🚀

