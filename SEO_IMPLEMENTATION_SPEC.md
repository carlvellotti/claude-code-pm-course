# SEO Implementation Spec for Claude Code PM Course

## Executive Summary

This spec outlines tactical SEO improvements for ccforpms.com to improve discoverability for niche search queries around "Claude Code for product managers" and related terms. Given low search volume but minimal competition, basic technical SEO will have outsized impact.

**Expected Outcome:** Rank on page 1 for "claude code for product managers" within 2-3 months, improve CTR from search by 30-40% through rich snippets.

---

## 1. Current State Analysis

### What's Working
- ✅ Clean URL structure (Next.js static export)
- ✅ Basic Open Graph tags for social sharing
- ✅ Responsive design (mobile-friendly)
- ✅ Page-level meta descriptions via frontmatter
- ✅ Fast performance (static site)
- ✅ Internal navigation structure

### Critical Gaps
- ❌ **No sitemap.xml** - Search engines can't efficiently discover all 19 pages
- ❌ **No robots.txt** - No crawl guidance for bots
- ❌ **Generic meta descriptions** - Homepage says just "Claude Code for Product Managers"
- ❌ **No structured data** - Missing Course schema markup (huge missed opportunity)
- ❌ **No canonical URLs** - Risk of duplicate content
- ❌ **Inconsistent OG tags** - Hardcoded to vercel.app domain, not ccforpms.com
- ❌ **Missing alt text** - Images lack descriptive alt attributes

### URL Structure (19 pages total)
```
/                                    # Homepage
/getting-started/introduction        # Module 0.0
/getting-started/installation        # Module 0.1
/getting-started/start-and-clone     # Module 0.2
/fundamentals/welcome                # Module 1.1
/fundamentals/visualizing-files      # Module 1.2
/fundamentals/first-tasks            # Module 1.3
/fundamentals/agents                 # Module 1.4
/fundamentals/custom-subagents       # Module 1.5
/fundamentals/project-memory         # Module 1.6
/fundamentals/claude-code-navigation # Module 1.7
/advanced/write-prd                  # Module 2.1
/advanced/analyze-data               # Module 2.2
/advanced/product-strategy           # Module 2.3
/company-context/overview            # Reference
/company-context/product             # Reference
/company-context/personas            # Reference
/company-context/competitive         # Reference
/search                              # Search page
```

---

## 2. Proposed Changes (Priority Ordered)

### PRIORITY 1: Sitemap Generation

**Why:** Critical for search engine discovery. Without a sitemap, Google may miss pages.

**Implementation:**
- Install `next-sitemap` package
- Configure to run in postbuild
- Generates sitemap.xml in `/out` directory after build
- Auto-generates robots.txt

**Technical Details:**

1. Install dependency:
   ```bash
   npm install --save-dev next-sitemap
   ```

2. Create `next-sitemap.config.js`:
   ```js
   /** @type {import('next-sitemap').IConfig} */
   module.exports = {
     siteUrl: 'https://ccforpms.com',
     generateRobotsTxt: true,
     generateIndexSitemap: false,
     exclude: ['/company-context/*'],
     robotsTxtOptions: {
       policies: [
         {
           userAgent: '*',
           allow: '/',
           disallow: ['/api/*', '/_next/*'],
         },
       ],
     },
   }
   ```

3. Update `package.json`:
   ```json
   "postbuild": "next-sitemap --config next-sitemap.config.js"
   ```

---

### PRIORITY 2: Enhanced Meta Tags

**Why:** Meta descriptions are the #1 factor for click-through rate from search results.

**Implementation:**

Update `theme.config.tsx` to use dynamic, page-specific meta tags:

```tsx
head: ({ title, frontMatter }) => {
  const siteUrl = 'https://ccforpms.com'
  const pageTitle = title ? `${title} – Claude Code for Product Managers` : 'Claude Code for Product Managers'
  const description = frontMatter.description || 'Learn Claude Code for PM work - an interactive course teaching file operations, agents, and AI-powered product management workflows.'
  const ogImage = frontMatter.ogImage || `${siteUrl}/images/better-graphic.png`
  const canonical = `${siteUrl}${frontMatter.canonical || ''}`

  return (
    <>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta name="description" content={description} />
      <link rel="canonical" href={canonical} />

      {/* Open Graph */}
      <meta property="og:url" content={canonical} />
      <meta property="og:type" content="website" />
      <meta property="og:site_name" content="Claude Code for Product Managers" />
      <meta property="og:title" content={pageTitle} />
      <meta property="og:description" content={description} />
      <meta property="og:image" content={ogImage} />
      <meta property="og:image:width" content="1200" />
      <meta property="og:image:height" content="630" />

      {/* Twitter */}
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content={pageTitle} />
      <meta name="twitter:description" content={description} />
      <meta name="twitter:image" content={ogImage} />

      {/* Additional SEO */}
      {frontMatter.keywords && (
        <meta name="keywords" content={frontMatter.keywords} />
      )}
    </>
  )
}
```

**Optimized Descriptions for Key Pages:**

| Page | Description (150-160 chars) |
|------|--------------------------|
| `/` | "Learn Claude Code for PM work through interactive tutorials. Master AI agents, file operations, and automated workflows for product managers." |
| `/getting-started/introduction` | "Introduction to Claude Code for PMs: Learn how AI file operations, parallel agents, and project memory transform product management workflows." |
| `/getting-started/installation` | "Install Claude Code in 15 minutes. Step-by-step guide for Mac, Windows, Linux with prerequisites and troubleshooting for product managers." |
| `/fundamentals/agents` | "Master Claude Code parallel agents to process 10 files simultaneously. Learn to run multiple AI instances for batch PM workflows and analysis." |
| `/advanced/write-prd` | "Write better PRDs with Claude Code AI agents. Use Socratic questioning, parallel approaches, and multi-perspective reviews for requirements docs." |

---

### PRIORITY 3: Structured Data (Schema.org Markup)

**Why:** Makes your course appear as a proper "Course" in Google Search with rich snippets.

**Implementation:**

Add Course schema to homepage for rich search results.

**File: `website/pages/index.mdx`**

Add frontmatter:
```yaml
---
title: 'Claude Code for Product Managers'
description: 'Learn Claude Code for PM work through interactive tutorials. Master AI agents, file operations, and automated workflows for product managers.'
schema:
  "@context": "https://schema.org"
  "@type": "Course"
  name: "Claude Code for Product Managers"
  description: "Learn Claude Code for PM work through interactive tutorials covering AI agents, file operations, and automated workflows."
  provider:
    "@type": "Person"
    name: "Carl Vellotti"
    url: "https://www.linkedin.com/in/carlvellotti/"
  educationalLevel: "Intermediate"
  timeRequired: "PT12H"
  inLanguage: "en"
  isAccessibleForFree: true
  hasCourseInstance:
    "@type": "CourseInstance"
    courseMode: "online"
    courseWorkload: "PT12H"
  teaches:
    - "Claude Code file operations"
    - "AI agent workflows"
    - "Parallel processing"
    - "Custom sub-agents"
    - "Project memory management"
---
```

**File: `website/theme.config.tsx`**

Add schema injection in head:
```tsx
{/* Structured Data */}
{frontMatter.schema && (
  <script
    type="application/ld+json"
    dangerouslySetInnerHTML={{
      __html: JSON.stringify(frontMatter.schema)
    }}
  />
)}
```

---

### PRIORITY 4: Image Alt Text

**Why:** Alt text helps accessibility AND SEO. Google indexes images separately.

**Implementation:**

Update key images with descriptive alt text:

**Homepage:**
```markdown
![Claude Code for Product Managers course homepage showing terminal interface and AI agent workflows](/images/better-graphic.png)
```

**All other images:**
Follow pattern: `![Descriptive text with context and keywords](/path/to/image.png)`

---

## 3. Implementation Plan

### Phase 1: Foundation (1-2 hours)
1. Install next-sitemap
2. Create next-sitemap.config.js
3. Update package.json postbuild script
4. Build and verify sitemap.xml generation

**Files Modified:**
- `website/package.json`
- `website/next-sitemap.config.js` (new)

---

### Phase 2: Meta Tag Overhaul (2-3 hours)
1. Update `theme.config.tsx` with dynamic head
2. Update frontmatter descriptions for all 19 pages
3. Fix OG image URL (vercel.app → ccforpms.com)

**Files Modified:**
- `website/theme.config.tsx`
- All 19 `.mdx` files (frontmatter)

---

### Phase 3: Structured Data (1 hour)
1. Add Course schema to homepage frontmatter
2. Update theme.config.tsx to inject schema
3. Test with Google Rich Results Test

**Files Modified:**
- `website/theme.config.tsx`
- `website/pages/index.mdx`

---

### Phase 4: Image Optimization (1 hour)
1. Update homepage hero image alt text
2. Audit and update alt text for other images

**Files Modified:**
- Various `.mdx` files with images

---

## 4. Testing & Verification

### Pre-Deployment Checklist
- [ ] Build succeeds locally (`npm run build`)
- [ ] Sitemap.xml generated in `/out`
- [ ] Robots.txt generated in `/out`
- [ ] All pages have unique meta descriptions
- [ ] Schema validates in Rich Results Test
- [ ] No console errors

### Post-Deployment Verification
- [ ] Google Search Console: Submit sitemap
- [ ] Check `site:ccforpms.com` shows all pages
- [ ] OpenGraph validation passes
- [ ] Lighthouse SEO score 95+

---

## 5. Expected Outcomes

### Short-term (1-4 weeks)
- Google discovers all 19 pages via sitemap
- Rich snippets appear in search results
- CTR from search improves 30-40%
- Lighthouse SEO score: 95+

### Medium-term (1-3 months)
- Rank page 1 for "claude code for product managers"
- Indexed pages: 19/19
- Average position for branded terms: <5

### Long-term (6+ months)
- Accumulate backlinks from shares
- Rank for broader PM automation terms
- Featured snippet potential

---

## 6. Decisions Made

1. **Sitemap Exclusions:** Exclude `/company-context/*` - reference material only
2. **Domain:** Use `ccforpms.com` (no www)
3. **Schema Scope:** Course schema on homepage only (keep it simple)
4. **Keywords Meta:** Include for Bing compatibility
5. **Descriptions:** Update all 19 pages with optimized descriptions

---

## 7. Cost & Effort Summary

| Phase | Time | Priority |
|-------|------|----------|
| Sitemap generation | 1-2 hours | P1 |
| Meta tag overhaul | 2-3 hours | P2 |
| Structured data | 1 hour | P3 |
| Image optimization | 1 hour | P4 |
| **Total** | **5-7 hours** | - |

All work is code changes. No paid tools required.

---

## Implementation Branch

All work will be done in branch: `seo-improvements`

Upon completion, create PR for review before merging to main.
