import React from 'react'

export default {
  logo: <span style={{ fontWeight: 600 }}>Claude Code for PMs</span>,
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
    return { titleTemplate: '%s – Claude Code for PMs' }
  },
  head: (
    <>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta property="og:title" content="Claude Code for PMs" />
      <meta property="og:description" content="A practical reference for using Claude Code on real product work" />
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

