import React from 'react'
import { useConfig } from 'nextra-theme-docs'
import { useRouter } from 'next/router'

export default {
  logo: <span style={{ fontWeight: 600 }}>Claude Code for Product Managers</span>,
  project: {
    link: 'https://github.com/carlvellotti/claude-code-pm-course'
  },
  docsRepositoryBase: 'https://github.com/carlvellotti/claude-code-pm-course/blob/main/website',
  feedback: {
    content: 'Give Carl feedback →',
    labels: 'feedback'
  },
  editLink: {
    component: null
  },
  footer: {
    content: (
      <span>
        © {new Date().getFullYear()} Carl Vellotti. Licensed under{' '}
        <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/" target="_blank" rel="noopener noreferrer">
          CC BY-NC-ND 4.0
        </a>
        .
      </span>
    )
  },
  useNextSeoProps() {
    return { titleTemplate: '%s – Claude Code for Product Managers' }
  },
  theme: 'dark',
  head: function Head() {
    const { frontMatter, title } = useConfig()
    const { asPath } = useRouter()
    const siteUrl = 'https://ccforpms.com'
    const isHome = asPath === '/'
    const pageTitle = isHome
      ? 'Claude Code Course for Product Managers | Free Interactive Tutorial'
      : (title ? `${title} – Claude Code for Product Managers` : 'Claude Code for Product Managers')
    const description = frontMatter?.description || 'Learn Claude Code IN Claude Code! Free Claude Code course for Product Managers - master AI agents, file operations, and PM workflows. No videos, just doing.'
    const ogImage = frontMatter?.ogImage || `${siteUrl}/images/better-graphic.png`
    const url = `${siteUrl}${asPath}`

    return (
      <>
        <title>{pageTitle}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="description" content={description} />
        <meta name="google-site-verification" content="Oenxq7BatQp09RlIUs43VkDpdoOQUWlUhqwxYxw49xQ" />

        {/* Favicon */}
        <link rel="icon" type="image/png" href="/favicon.png" />
        <link rel="apple-touch-icon" href="/favicon.png" />

        {/* Google Analytics */}
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-XBF1JD68VY"></script>
        <script
          dangerouslySetInnerHTML={{
            __html: `
              window.dataLayer = window.dataLayer || [];
              function gtag(){dataLayer.push(arguments);}
              gtag('js', new Date());
              gtag('config', 'G-XBF1JD68VY');
            `
          }}
        />

        {/* Open Graph */}
        <meta property="og:type" content="website" />
        <meta property="og:url" content={url} />
        <meta property="og:site_name" content="Learn Claude Code IN Claude Code!" />
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
        {frontMatter?.keywords && (
          <meta name="keywords" content={frontMatter.keywords} />
        )}

        {/* Structured Data */}
        {frontMatter?.schema && (
          <script
            type="application/ld+json"
            dangerouslySetInnerHTML={{
              __html: JSON.stringify(frontMatter.schema)
            }}
          />
        )}
      </>
    )
  },
  primaryHue: 169,
  sidebar: {
    defaultMenuCollapseLevel: 1,
    toggleButton: true
  },
  toc: {
    backToTop: true
  }
}
