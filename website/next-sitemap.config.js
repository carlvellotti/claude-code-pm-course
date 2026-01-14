/** @type {import('next-sitemap').IConfig} */
module.exports = {
  siteUrl: 'https://ccforpms.com',
  generateRobotsTxt: true,
  generateIndexSitemap: false, // Don't need index for <50k URLs
  exclude: ['/company-context/*'], // Exclude reference pages from sitemap
  robotsTxtOptions: {
    policies: [
      {
        userAgent: '*',
        allow: '/',
        disallow: ['/api/*', '/_next/*'],
      },
    ],
  },
  transform: async (config, path) => {
    // Set homepage to highest priority
    if (path === '/') {
      return {
        loc: path,
        changefreq: 'weekly',
        priority: 1.0,
        lastmod: new Date().toISOString(),
      }
    }
    return {
      loc: path,
      changefreq: 'weekly',
      priority: 0.7,
      lastmod: new Date().toISOString(),
    }
  },
}
