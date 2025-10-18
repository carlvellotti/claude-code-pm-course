import React from 'react'

export default {
  logo: <span style={{ fontWeight: 600 }}>Claude Code for Product Managers</span>,
  project: { 
    link: 'https://github.com/carlvellotti/claude-code-pm-course' 
  },
  docsRepositoryBase: 'https://github.com/carlvellotti/claude-code-pm-course/blob/main/website',
  footer: { 
    text: (
      <span>
        Created by{' '}
        <a 
          href="https://www.linkedin.com/in/carlvellotti/" 
          target="_blank" 
          rel="noopener noreferrer"
        >
          Carl Vellotti
        </a>
        . Check out{' '}
        <a 
          href="https://fullstack-pm.com/subscribe" 
          target="_blank" 
          rel="noopener noreferrer"
        >
          The Full Stack PM
        </a>
        , a community and newsletter for PM Builders
      </span>
    )
  },
  useNextSeoProps() {
    return { titleTemplate: '%s – Claude Code for Product Managers' }
  },
  head: (
    <>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta property="og:title" content="Claude Code for Product Managers" />
      <meta property="og:description" content="A practical reference for using Claude Code on real product work" />
      <meta property="og:image" content="https://claude-code-pm-course.vercel.app/images/claude-code-for-pms.png" />
      <meta property="og:image:width" content="1200" />
      <meta property="og:image:height" content="630" />
      <meta name="twitter:card" content="summary_large_image" />
    </>
  ),
  primaryHue: 220,
  sidebar: {
    defaultMenuCollapseLevel: 1,
    toggleButton: true
  },
  toc: {
    backToTop: true
  }
}

