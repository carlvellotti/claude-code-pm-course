import React from 'react'
import { useConfig } from 'nextra-theme-docs'
import { useRouter } from 'next/router'

const SITE_NAME = {
  en: 'Claude Code for Product Managers',
  zh: 'Claude Code 产品经理课程'
}

const FEEDBACK_CONTENT = {
  en: 'Give Carl feedback →',
  zh: '反馈给 Carl →'
}

const SEARCH_PLACEHOLDER = {
  en: 'Search documentation...',
  zh: '搜索文档...'
}

const HEAD_DESCRIPTION = {
  en: 'Learn Claude Code for PM work - an interactive course teaching file operations, agents, and AI-powered product management workflows.',
  zh: '学习用于产品经理工作的 Claude Code —— 这是一个交互式课程，教授文件操作、智能体和 AI 驱动的产品管理工作流。'
}

const HEAD_TITLE_HOME = {
  en: 'Learn Claude Code IN Claude Code! – Claude Code for Product Managers',
  zh: '在 Claude Code 中学习 Claude Code！– Claude Code 产品经理课程'
}

// Helper to get locale from path since we're not using Next.js i18n routing
const useLocale = () => {
  const { asPath } = useRouter()
  return asPath.startsWith('/zh') ? 'zh' : 'en'
}

const LanguageSwitch = () => {
  const { asPath } = useRouter()
  const locale = useLocale()
  
  // Calculate target path
  let targetPath = ''
  if (locale === 'zh') {
    // Remove /zh prefix
    targetPath = asPath.replace(/^\/zh/, '') || '/'
  } else {
    // Add /zh prefix
    // Handle root / correctly
    targetPath = asPath === '/' ? '/zh' : `/zh${asPath}`
  }
  
  return (
    <a 
      href={targetPath} 
      suppressHydrationWarning
      style={{ 
        padding: '0.5rem', 
        fontSize: '0.875rem', 
        fontWeight: 600,
        textDecoration: 'none',
        color: 'currentColor',
        marginLeft: '0.5rem'
      }}
    >
      {locale === 'en' ? '中文' : 'English'}
    </a>
  )
}

export default {
  logo: function Logo() {
    const locale = useLocale()
    return <span style={{ fontWeight: 600 }}>{SITE_NAME[locale]}</span>
  },
  project: {
    link: 'https://github.com/carlvellotti/claude-code-pm-course'
  },
  docsRepositoryBase: 'https://github.com/carlvellotti/claude-code-pm-course/blob/main/website',
  feedback: {
    content: function Feedback() {
      const locale = useLocale()
      return <>{FEEDBACK_CONTENT[locale]}</>
    },
    labels: 'feedback'
  },
  editLink: {
    component: null
  },
  navbar: {
    extraContent: <LanguageSwitch />
  },
  footer: {
    content: function Footer() {
      const locale = useLocale()
      return (
        <span>
          © {new Date().getFullYear()} Carl Vellotti. {locale === 'zh' ? '保留所有权利。' : 'Licensed under'}{' '}
          <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/" target="_blank" rel="noopener noreferrer">
            CC BY-NC-ND 4.0
          </a>
          .
        </span>
      )
    }
  },
  useNextSeoProps() {
    const locale = useLocale()
    return { titleTemplate: `%s – ${SITE_NAME[locale]}` }
  },
  theme: 'dark',
  search: {
    placeholder: function Placeholder() {
      const locale = useLocale()
      return SEARCH_PLACEHOLDER[locale]
    }
  },
  head: function Head() {
    const { frontMatter, title } = useConfig()
    const { asPath } = useRouter()
    const locale = useLocale()
    const siteUrl = 'https://ccforpms.com'
    // Simple home check - could be improved
    const isHome = asPath === '/' || asPath === '/zh' || asPath === '/en'
    const pageTitle = isHome
      ? HEAD_TITLE_HOME[locale]
      : (title ? `${title} – ${SITE_NAME[locale]}` : SITE_NAME[locale])
    const description = frontMatter?.description || HEAD_DESCRIPTION[locale]
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
        <meta property="og:site_name" content={SITE_NAME[locale]} />
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
