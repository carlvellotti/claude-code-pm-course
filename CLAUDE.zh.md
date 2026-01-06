# CLAUDE.zh.md

此文件为 Claude Code (claude.ai/code) 在处理此仓库中的代码时提供指导。

## 仓库概览

这是一个用于“Claude Code 产品经理课程”的双重用途仓库：

1. **course-materials/** - 面向学生的互动课程内容（通过 GitHub Releases 作为 zip 分发）
2. **website/** - Next.js 文档站点（部署到 Vercel 的 ccforpms.com）

学生下载 course-materials/ zip 包，解压，从该文件夹运行 `claude`，并输入 `/start-1-1` 开始学习。

## 课程架构：配置驱动系统

**本课程使用配置驱动架构，以便在添加/重新排序模块时实现最大的灵活性。**

### 单一事实来源：course-structure.json

所有模块定义都位于 `course-materials/course-structure.json` 中。此文件控制：
- 课程结构和模块顺序
- 斜杠命令路由（所有斜杠命令都是相同的 - 它们读取配置以知道加载哪个教学脚本）
- 网站导航（在构建时根据配置生成）
- 教学脚本导航（模块读取配置以知道下一步是什么）

### 工作原理

**斜杠命令：**
- 所有 10 个斜杠命令（`/start-1-1` 到 `/start-2-3`）都是相同的
- 它们解析自己的命令名称（例如，"start-1-2" → 模块 "1.2"）
- 它们读取 `course-structure.json` 以找到模块的教学脚本路径
- 它们加载并执行该教学脚本

**教学脚本：**
- 在每个模块结束时，脚本读取 `course-structure.json`
- 它们动态确定下一步是什么
- 它们告诉学生下一个模块的正确斜杠命令

**网站导航：**
- `website/pages/fundamentals/_meta.ts` 和 `website/pages/advanced/_meta.ts` 导入配置
- 导航是在构建时根据 `course-structure.json` 生成的

### 添加或重新排序模块

要添加新模块或重新排序现有模块：

1. **编辑 `course-materials/course-structure.json`** - 添加/移动模块定义
2. **创建新模块文件夹和文件**（如果添加新模块）
3. **完成！** 其他所有内容都会自动更新：
   - 斜杠命令正确路由（它们都是相同的）
   - 教学脚本引用正确的“下一个”模块（它们读取配置）
   - 网站导航更新（在构建时根据配置生成）

**不需要：**
- ❌ 重命名文件夹
- ❌ 更新单个斜杠命令文件
- ❌ 编辑现有教学脚本
- ❌ 手动更新网站 `_meta.ts` 文件

**示例：在当前 1.3 和 1.4 之间插入模块 1.4：**

只需编辑 `course-structure.json` 添加新模块定义，一切都会自动级联。旧 1.4（智能体）的文件夹可以保持名为 `1.4-agents` - 配置将逻辑 ID (1.5) 映射到物理路径 (1.4-agents)。

### 好处

- ✅ 无需触及现有文件即可添加模块
- ✅ 通过编辑一个 JSON 文件重新排序模块
- ✅ 网站和课程材料自动保持同步
- ✅ 课程结构的单一事实来源
- ✅ 课程演变的最大灵活性

## 关键：打开此仓库时

**除非明确要求，否则当用户首次打开此仓库时，切勿主动设置、构建或安装任何内容。** README.zh.md 包含对此的特定警告：

- ❌ 请勿运行 `npm install`
- ❌ 请勿运行 `npm run build`
- ❌ 请勿进行设置更改
- ✅ 等待明确的用户指示

这是一个互动课程仓库。用户（或学生）将指导需要做什么。

## 常用命令

### 发布管理工作流

**当您更新课程内容时：**

1. **更改** course-materials/ 中的文件
   - 编辑 `course-materials/lesson-modules/` 中的模块
   - 更新 `course-materials/company-context/` 中的公司背景
   - 修改 `course-materials/.claude/agents/` 中的智能体
   - 等等。

2. **提交并推送到 main：**
   ```bash
   git add -A
   git commit -m "Update Module 1.3 with new examples"
   git push origin main
   ```

3. **创建新版本：**
   ```bash
   # 运行发布脚本并指定新版本号
   ./scripts/create-release.sh v1.0.1

   # 使用新 zip 创建 GitHub 版本
   gh release create v1.0.1 releases/complete-course.zip \
     --title "v1.0.1 - Updated Module 1.3" \
     --notes "- Fixed typos in Module 1.3\n- Added new examples to Module 2.1"
   ```

4. **更新网站（如果需要）：**
   - 首页显示 "Latest: v1.0.0"
   - 在 `website/pages/index.mdx` 第 128 行更新此内容：
   ```markdown
   **👉 [Download Course Materials](...latest/download/complete-course.zip)** - Get the complete course (Latest: v1.0.1)
   ```

**GitHub Releases 工作原理：**
- `/releases/latest/download/complete-course.zip` - 始终指向最新版本
- 使用此 URL 的学生将自动获得最新版本
- 您可以创建任意数量的版本（v1.0.1, v1.0.2, v1.1.0 等）
- 旧版本保留在其特定版本 URL 处

**语义化版本控制指南：**
- `v1.0.X` (Patch) - 错误修复、拼写错误、现有内容的次要更新
- `v1.X.0` (Minor) - 新模块、新功能、重要内容添加
- `vX.0.0` (Major) - 完全重组、破坏性更改

**快速参考命令：**
```bash
# 1. 更新内容、提交、推送
git add -A && git commit -m "..." && git push origin main

# 2. 创建新发布 zip
./scripts/create-release.sh v1.0.1

# 3. 发布到 GitHub
gh release create v1.0.1 releases/complete-course.zip \
  --title "v1.0.1 - Description" \
  --notes "What changed"
```

就是这样！您网站中的 `/releases/latest/` URL 将自动指向最新版本。

### 网站开发

**本地开发：**
```bash
cd website
npm install
npm run dev
```

**生产构建：**
```bash
cd website
npm run build
```

构建过程：
1. `next build` - 在 website/out/ 中创建静态导出
2. `next-sitemap` - 生成 sitemap.xml 和 robots.txt
3. `pagefind` - 为静态站点构建搜索索引

**预览生产构建：**
```bash
cd website
npm run preview
```

### 部署

网站会在推送到 main 分支时自动部署到 Vercel (ccforpms.com)。无需手动部署。

### 分析

**Google Analytics:**
- 测量 ID: `G-XBF1JD68VY`
- 实现位置: `website/theme.config.tsx` (第 44-55 行)
- 跟踪: 页面浏览量、访客、流量来源、地理数据、设备类型、滚动深度、出站点击
- 验证: 访问站点 → 检查 Google Analytics 实时仪表板

**下载跟踪：**
- 课程材料下载（通过模块 0.2 中的 `curl`）由 GitHub 的内置发布下载统计跟踪
- 检查下载计数: GitHub 仓库 → Releases 选项卡，或通过 `gh api repos/carlvellotti/claude-code-pm-course/releases`
- Google Analytics 不跟踪这些下载（它们完全绕过网站）

## 仓库架构

### 课程材料 (course-materials/)

**结构：**
- `lesson-modules/` - 模块 1 和模块 2 互动课程
- `company-context/` - 练习中使用的 TaskFlow 公司参考资料
- `.claude/` - 为课程提供动力的斜杠命令、智能体和教学脚本

**斜杠命令：**
位于 `course-materials/.claude/commands/`，这些是引导学生通过模块的教学脚本：
- `/start-1-1`, `/start-1-2` 等用于模块 1 课程
- `/start-2-1`, `/start-2-2` 等用于模块 2 课程

**教学脚本行为：**
当用户在 course-materials/ 文件夹中输入斜杠命令时，阅读 `course-materials/.claude/SCRIPT_INSTRUCTIONS.zh.md` 了解有关如何执行教学脚本的关键规则。要点：
- 教学脚本必须逐字逐句遵循（对于 "Say:" 块）
- "Check:" 点是关卡 - 停止并等待学生响应
- "Action:" 块包含要执行的确切命令
- 切勿打破第四面墙或说“我已经阅读了脚本” - 立即开始教学
- 所有示例文件使用 .md 文件扩展名（而不是 .txt），以便它们与 markdown 编辑器（Nimbalyst, Obsidian 等）配合使用

### 网站 (website/)

**技术栈：**
- Next.js 14 静态导出 (`output: 'export'`)
- Nextra (文档主题)
- Pagefind (静态搜索)
- Vercel (托管)

**页面结构：**
```
website/pages/
  getting-started/     - 模块 0 内容（安装、设置）
  fundamentals/        - 模块 1 内容
  advanced/           - 模块 2 内容
  company-context/    - TaskFlow 参考（从站点地图中排除）
  index.mdx           - 落地页
  _meta.ts            - 导航结构
```

**关键文件：**
- `theme.config.tsx` - Nextra 主题配置（徽标、页脚、SEO、导航）
- `next.config.mjs` - Next.js 配置（静态导出、图像优化）
- `next-sitemap.config.js` - 站点地图生成（排除 /company-context/*）

**SEO 配置：**
该站点在 theme.config.tsx 中具有全面的 SEO：
- Open Graph 标签
- Twitter 卡片
- Google 站点验证
- 通过 frontMatter 的每页自定义元数据
- 结构化数据支持

### 讲师文件 (instructor-files/) - 私有子模块

`instructor-files/` 文件夹是一个指向私有仓库 (`claude-code-pm-instructor`) 的 **git 子模块**。这将讲师专用材料（大纲、构建指南、参考文档）与公共课程分开。

**工作原理：**
- 公共用户看到文件夹存在，但无法访问（私有仓库 404）
- 您（有权限）可以正常查看和编辑文件
- 更改在单独的私有仓库中跟踪

**更新讲师文件的工作流：**
```bash
# 1. 在 instructor-files/ 中进行更改
cd instructor-files

# 2. 提交并推送到私有仓库
git add -A
git commit -m "Update build guide"
git push

# 3. 回到主仓库，更新子模块引用
cd ..
git add instructor-files
git commit -m "Update instructor submodule"
git push
```

**克隆后（为您自己）：**
```bash
git submodule update --init --recursive
```

**注意：** 子模块不会包含在学生课程材料 zip 包中（他们通过 GitHub Releases 下载，默认情况下排除子模块）。

### 内部文档 (docs/)

未包含在面向学生的材料中的规划文档：
- `GITHUB_RELEASES_PLAN.md` - 发布策略文档
- `SEO_IMPLEMENTATION_SPEC.md` - SEO 规范

## 文件扩展名约定

所有课程示例文件必须使用 `.md` 扩展名（而不是 `.txt`），因为：
- 学生使用 markdown 编辑器（Nimbalyst, Obsidian, VS Code）可视化课程文件（在模块 1.2 中教授）
- 大多数 markdown 编辑器无法正确显示 .txt 文件
- 这在 SCRIPT_INSTRUCTIONS.md 中强制执行

## Git 工作流

**忽略的文件 (.gitignore):**
- Obsidian 工作区文件（个人设置）
- 发布工件 (releases/, *.zip)
- 构建输出 (node_modules/)
- 大多数 .json 文件（除了 package.json, tsconfig.json）
- 大多数 .png 文件（除了 website/public/**/*.png）

**分支：**
主分支是 `main` - 用于拉取请求。

## 网站主题自定义

该站点使用青色配色方案 (`primaryHue: 169`)，默认为深色主题。页脚包括 CC BY-NC-ND 4.0 许可归属。

## 课程理念

本课程教导产品经理通过动手实践使用 Claude Code。课程内容本身由 Claude Code 提供，创造了一种元学习体验，学生通过使用工具来学习工具。
