# 面向产品经理 - 文档网站

这是一个基于 Next.js 的文档网站,用于 Claude Code 面向产品经理课程。

## 开发

```bash
# 安装依赖
npm install
# 运行开发服务器
npm run dev
# 打开 http://localhost:3000
```

## 构建

```bash
# 构建静态站点
npm run build
# 构建输出将在 `out/` 目录中
# Pagefind 会在构建后自动索引内容
```

## 部署到 Vercel

### 选项 1: 通过 Vercel 部署板部署

1. 前往 [vercel.com](https://vercel.com) 并登录
2. 点击 "Add New Project"
3. 导入 GitHub 仓库:`carlvellotti/claude-code-pm-course`
4. 设置根目录为 `website`
5. 框架预设:Next.js
6. 构建命令:`npm run build`(默认即可)
7. 输出目录:`out`
8. 部署!

### 选项 2: 通过 Vercel CLI 部署

```bash
# 安装 Vercel CLI
npm i -g vercel
# 导航到网站目录
cd /Users/carl/claude-code-pm-course/website
# 登录(首次仅)
vercel login
# 部署到预览环境
vercel
# 用于生产环境
vercel --prod
```

## 项目结构

```
website/
├── pages/               # 所有内容页面(MDX)
│   ├── company-context/ # TaskFlow 公司信息
│   ├── getting-started/ # 模块 0.0-0.2
│   ├── fundamentals/    # 模块 1.1-1.7
│   ├── advanced/        # 模块 2.1-2.3
│   ├── _app.jsx         # Next.js 应用包装器
│   ├── _meta.ts         # 导航配置
│   ├── index.mdx        # 首页
│   └── search.mdx       # 搜索页面,含 Pagefind
├── public/
│   └── images/          # 课程图片
├── next.config.mjs      # Next.js 配置
├── theme.config.tsx     # Nextra 主题配置
└── package.json         # 依赖项
```

## 内容更新

内容会自动从主课程 `lesson-modules/` 目录转换。如需更新:
1. 编辑 `/lesson-modules/` 中的 REFERENCE_GUIDE.md 文件
2. 运行转换脚本:`./convert-content.sh`
3. 构建并部署

```bash
cd /Users/carl/claude-code-pm-course/website
./convert-content.sh
npm run build
npm run preview # 本地测试
```

## 技术栈

- **Next.js 14** - 静态站点生成
- **Nextra 3** - 文档主题
- **Pagefind** - 客户端搜索

## 链接

- **实时站点:** TBD(将部署到 Vercel)
- **课程仓库:** https://github.com/carlvellotti/claude-code-pm-course
- **Nextra 文档:** https://nextra.site
- **Pagefind 文档:** https://pagefind.app

## 项目包含

您构建的站点包含:
- ✅ 所有课程内容(20 个页面)
- ✅ 左侧边栏导航
- ✅ 右侧边栏内容表(含 Pagefind)
- ✅ 客户端搜索
- ✅ 公司上下文部分
- ✅ 所有图片
- ✅ 响应式移动布局
- ✅ 快速静态站点(无需服务器)
- ✅ 开源 HTTPS 和自定义域名(如有需要)
- ✅ Nextra 文档站点自动转换 MDX 内容
