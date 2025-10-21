import React from 'react'

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
  head: (
    <>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta property="og:title" content="Learn Claude Code IN Claude Code!" />
      <meta property="og:description" content="Claude Code for Product Managers" />
      <meta property="og:image" content="https://claude-code-pm-course.vercel.app/images/better-graphic.png" />
      <meta property="og:image:width" content="1200" />
      <meta property="og:image:height" content="630" />
      <meta name="twitter:card" content="summary_large_image" />
    </>
  ),
  primaryHue: 169,
  sidebar: {
    defaultMenuCollapseLevel: 1,
    toggleButton: true
  },
  toc: {
    backToTop: true
  }
}

