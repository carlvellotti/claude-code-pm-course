# Claude Code PM 课程 SEO 实施规范

## 执行摘要

本规范概述了 ccforpms.com 的战术性 SEO 改进，以提高围绕“Claude Code for product managers”及相关术语的利基搜索查询的可发现性。鉴于搜索量较低但竞争极小，基本的技术 SEO 将产生巨大的影响。

**预期成果：** 在 2-3 个月内，“claude code for product managers”排名第一页，通过丰富网页摘要将搜索点击率提高 30-40%。

---

## 1. 当前状态分析

### 有效方面
- ✅ 干净的 URL 结构 (Next.js 静态导出)
- ✅ 用于社交分享的基本 Open Graph 标签
- ✅ 响应式设计（移动友好）
- ✅ 通过 frontmatter 实现页面级元描述
- ✅ 快速性能（静态站点）
- ✅ 内部导航结构

### 关键差距
- ❌ **无 sitemap.xml** - 搜索引擎无法有效发现所有 19 个页面
- ❌ **无 robots.txt** - 没有针对机器人的抓取指南
- ❌ **通用元描述** - 首页仅显示 "Claude Code for Product Managers"
- ❌ **无结构化数据** - 缺少 Course schema 标记（巨大的错失良机）
- ❌ **无规范 URL** - 重复内容的风险
- ❌ **不一致的 OG 标签** - 硬编码为 vercel.app 域，而不是 ccforpms.com
- ❌ **缺少 alt 文本** - 图像缺少描述性 alt 属性

### URL 结构（共 19 页）
```
/                                    # 首页
/getting-started/introduction        # 模块 0.0
/getting-started/installation        # 模块 0.1
/getting-started/start-and-clone     # 模块 0.2
/fundamentals/welcome                # 模块 1.1
/fundamentals/visualizing-files      # 模块 1.2
/fundamentals/first-tasks            # 模块 1.3
/fundamentals/agents                 # 模块 1.4
/fundamentals/custom-subagents       # 模块 1.5
/fundamentals/project-memory         # 模块 1.6
/fundamentals/claude-code-navigation # 模块 1.7
/advanced/write-prd                  # 模块 2.1
/advanced/analyze-data               # 模块 2.2
/advanced/product-strategy           # 模块 2.3
/company-context/overview            # 参考
/company-context/product             # 参考
/company-context/personas            # 参考
/company-context/competitive         # 参考
/search                              # 搜索页面
```

---

## 2. 建议的变更（按优先级排序）

### 优先级 1：站点地图生成

**原因：** 对搜索引擎发现至关重要。没有站点地图，Google 可能会错过页面。

**实施：**
- 安装 `next-sitemap` 包
- 配置为在 postbuild 中运行
- 构建后在 `/out` 目录中生成 sitemap.xml
- 自动生成 robots.txt

**技术细节：**

1. 安装依赖项：
   ```bash
   npm install --save-dev next-sitemap
   ```

2. 创建 `next-sitemap.config.js`:
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

3. 更新 `package.json`:
   ```json
   "postbuild": "next-sitemap --config next-sitemap.config.js"
   ```

---

### 优先级 2：增强元标签

**原因：** 元描述是搜索结果点击率的第一大因素。

**实施：**

更新 `theme.config.tsx` 以使用动态、特定于页面的元标签：

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

**关键页面的优化描述：**

| 页面 | 描述 (150-160 字符) |
|------|--------------------------|
| `/` | "通过互动教程学习 Claude Code 进行 PM 工作。掌握 AI 智能体、文件操作和产品经理的自动化工作流。" |
| `/getting-started/introduction` | "Claude Code for PMs 简介：了解 AI 文件操作、并行智能体和项目记忆如何改变产品管理工作流。" |
| `/getting-started/installation` | "在 15 分钟内安装 Claude Code。针对产品经理的 Mac、Windows、Linux 分步指南，包含前提条件和故障排除。" |
| `/fundamentals/agents` | "掌握 Claude Code 并行智能体以同时处理 10 个文件。学习运行多个 AI 实例以进行批量 PM 工作流和分析。" |
| `/advanced/write-prd` | "使用 Claude Code AI 智能体撰写更好的 PRD。使用苏格拉底式提问、并行方法和多角度审查来编写需求文档。" |

---

### 优先级 3：结构化数据 (Schema.org 标记)

**原因：** 使您的课程在 Google 搜索中显示为带有丰富网页摘要的正确“课程”。

**实施：**

将 Course schema 添加到首页以获得丰富的搜索结果。

**文件：`website/pages/index.mdx`**

添加 frontmatter：
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

**文件：`website/theme.config.tsx`**

在 head 中添加 schema 注入：
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

### 优先级 4：图像 Alt 文本

**原因：** Alt 文本有助于可访问性和 SEO。Google 单独索引图像。

**实施：**

使用描述性 alt 文本更新关键图像：

**首页：**
```markdown
![Claude Code for Product Managers course homepage showing terminal interface and AI agent workflows](/images/better-graphic.png)
```

**所有其他图像：**
遵循模式：`![带有上下文和关键字的描述性文本](/path/to/image.png)`

---

## 3. 实施计划

### 阶段 1：基础（1-2 小时）
1. 安装 next-sitemap
2. 创建 next-sitemap.config.js
3. 更新 package.json postbuild 脚本
4. 构建并验证 sitemap.xml 生成

**修改的文件：**
- `website/package.json`
- `website/next-sitemap.config.js` (新)

---

### 阶段 2：元标签大修（2-3 小时）
1. 使用动态 head 更新 `theme.config.tsx`
2. 更新所有 19 个页面的 frontmatter 描述
3. 修复 OG 图像 URL (vercel.app → ccforpms.com)

**修改的文件：**
- `website/theme.config.tsx`
- 所有 19 个 `.mdx` 文件 (frontmatter)

---

### 阶段 3：结构化数据（1 小时）
1. 将 Course schema 添加到首页 frontmatter
2. 更新 theme.config.tsx 以注入 schema
3. 使用 Google Rich Results Test 进行测试

**修改的文件：**
- `website/theme.config.tsx`
- `website/pages/index.mdx`

---

### 阶段 4：图像优化（1 小时）
1. 更新首页英雄图像 alt 文本
2. 审核并更新其他图像的 alt 文本

**修改的文件：**
- 包含图像的各种 `.mdx` 文件

---

## 4. 测试与验证

### 部署前清单
- [ ] 本地构建成功 (`npm run build`)
- [ ] Sitemap.xml 在 `/out` 中生成
- [ ] Robots.txt 在 `/out` 中生成
- [ ] 所有页面都有唯一的元描述
- [ ] Schema 在 Rich Results Test 中验证通过
- [ ] 无控制台错误

### 部署后验证
- [ ] Google Search Console：提交 sitemap
- [ ] 检查 `site:ccforpms.com` 显示所有页面
- [ ] OpenGraph 验证通过
- [ ] Lighthouse SEO 得分 95+

---

## 5. 预期成果

### 短期（1-4 周）
- Google 通过 sitemap 发现所有 19 个页面
- 搜索结果中出现丰富网页摘要
- 搜索点击率提高 30-40%
- Lighthouse SEO 得分：95+

### 中期（1-3 个月）
- “claude code for product managers”排名第一页
- 索引页面：19/19
- 品牌词平均位置：<5

### 长期（6+ 个月）
- 通过分享积累反向链接
- 更广泛的 PM 自动化术语排名
- 精选摘要潜力

---

## 6. 做出的决定

1. **站点地图排除：** 排除 `/company-context/*` - 仅供参考材料
2. **域名：** 使用 `ccforpms.com` (无 www)
3. **Schema 范围：** 仅在首页使用 Course schema（保持简单）
4. **关键字元数据：** 包括 Bing 兼容性
5. **描述：** 更新所有 19 个页面的优化描述

---

## 7. 成本与工作量摘要

| 阶段 | 时间 | 优先级 |
|-------|------|----------|
| 站点地图生成 | 1-2 小时 | P1 |
| 元标签大修 | 2-3 小时 | P2 |
| 结构化数据 | 1 小时 | P3 |
| 图像优化 | 1 小时 | P4 |
| **总计** | **5-7 小时** | - |

所有工作都是代码更改。不需要付费工具。

---

## 实施分支

所有工作将在分支：`seo-improvements` 中完成

完成后，创建 PR 以供审查，然后合并到 main。
