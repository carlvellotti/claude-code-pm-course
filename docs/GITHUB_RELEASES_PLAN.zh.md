# GitHub Releases 分发计划

## 执行摘要

实施 GitHub Releases 作为课程材料的分发机制。这允许版本化的课程下载，将营销网站与课程内容清晰分离，并采用标准的开源分发实践。

**关键决定：** 将仓库设为 PUBLIC，以通过 GitHub Releases 实现简单、无需身份验证的下载。

---

## 当前状态

```
claude-code-pm-course/          # 私有 GitHub 仓库
├── website/                    # Nextra 文档站点（部署到 ccforpms.com）
│   ├── pages/
│   ├── public/
│   ├── theme.config.tsx
│   └── package.json
├── lesson-modules/             # 互动课程模块（在根目录）
│   ├── module-0-0.md
│   ├── module-1-1.md
│   └── ...
├── company-context/            # TaskFlow 参考资料
│   ├── overview.md
│   ├── product.md
│   └── ...
├── .claude/                    # 课程的斜杠命令
│   └── commands/
└── README.zh.md
```

**问题：**
- 课程材料分散在根目录中
- 没有明确的学生分发机制
- 仓库是私有的（限制了可发现性和信任）

---

## 建议的结构

### 文件组织

```
claude-code-pm-course/          # 公共 GitHub 仓库
├── website/                    # Nextra 文档站点 → ccforpms.com
│   ├── pages/
│   ├── public/
│   │   ├── images/
│   │   ├── sitemap.xml
│   │   └── robots.txt
│   ├── theme.config.tsx
│   └── package.json
├── course-materials/           # ← 新：学生需要的一切
│   ├── lesson-modules/         # 从根目录移动
│   │   ├── module-0-0.md
│   │   ├── module-1-1.md
│   │   └── ...
│   ├── company-context/        # 从根目录移动
│   │   ├── overview.md
│   │   ├── product.md
│   │   └── ...
│   ├── .claude/                # 从根目录移动
│   │   └── commands/
│   └── README.zh.md               # 学生说明
├── docs/                       # 内部文档
│   ├── SEO_IMPLEMENTATION_SPEC.zh.md
│   └── GITHUB_RELEASES_PLAN.zh.md
├── .gitignore
├── LICENSE                     # CC BY-NC-ND 4.0
└── README.zh.md                   # 仓库 README（针对开发人员/贡献者）
```

---

## GitHub Releases 策略

### 发布结构

**v1.0.0 - 课程启动**
```
Release Assets:
├── complete-course.zip         # 所有模块 (0-2) + 上下文 + .claude
├── module-0-getting-started.zip    # 仅模块 0 + 共享文件
├── module-1-fundamentals.zip       # 仅模块 1 + 共享文件
└── module-2-advanced.zip           # 仅模块 2 + 共享文件
```

### 压缩包内容

**complete-course.zip:**
```
course-materials/
├── lesson-modules/
├── company-context/
├── .claude/
└── README.zh.md
```

**module-0-getting-started.zip:**
```
module-0/
├── lesson-modules/module-0-*.md
├── company-context/            # 跨所有模块共享
├── .claude/                    # 跨所有模块共享
└── README.zh.md
```

**module-1-fundamentals.zip:**
```
module-1/
├── lesson-modules/module-1-*.md
├── company-context/
├── .claude/
└── README.zh.md
```

---

## 实施计划

### 阶段 1：重组仓库（1 小时）

**任务：**
1. 创建 `course-materials/` 目录
2. 移动 `lesson-modules/` → `course-materials/lesson-modules/`
3. 移动 `company-context/` → `course-materials/company-context/`
4. 移动 `.claude/` → `course-materials/.claude/`
5. 创建 `course-materials/README.zh.md` 包含学生说明
6. 如果需要，更新根目录 `.gitignore`
7. 测试网站是否仍然构建（在 website/ 中运行 `npm run build`）

**命令：**
```bash
mkdir course-materials
mv lesson-modules course-materials/
mv company-context course-materials/
mv .claude course-materials/
```

**要更新的文件：**
- 任何对旧路径的引用（可能没有，但请验证）
- 模块 0.2 说明（在未来的提交中更新）

---

### 阶段 2：创建发布脚本（30 分钟）

创建 `scripts/create-release.sh`:

```bash
#!/bin/bash
# 为 GitHub Release 创建课程材料 zip 包

VERSION=$1

if [ -z "$VERSION" ]; then
  echo "Usage: ./scripts/create-release.sh v1.0.0"
  exit 1
fi

echo "Creating release zips for $VERSION..."

# Create temp directory
mkdir -p releases

# Create complete course zip
cd course-materials
zip -r ../releases/complete-course.zip . -x "*.DS_Store"
cd ..

# Create module-specific zips
# Module 0
mkdir -p releases/module-0
cp -r course-materials/company-context releases/module-0/
cp -r course-materials/.claude releases/module-0/
mkdir releases/module-0/lesson-modules
cp course-materials/lesson-modules/module-0-*.md releases/module-0/lesson-modules/
cp course-materials/README.zh.md releases/module-0/
cd releases/module-0
zip -r ../module-0-getting-started.zip . -x "*.DS_Store"
cd ../..

# Module 1
mkdir -p releases/module-1
cp -r course-materials/company-context releases/module-1/
cp -r course-materials/.claude releases/module-1/
mkdir releases/module-1/lesson-modules
cp course-materials/lesson-modules/module-1-*.md releases/module-1/lesson-modules/
cp course-materials/README.zh.md releases/module-1/
cd releases/module-1
zip -r ../module-1-fundamentals.zip . -x "*.DS_Store"
cd ../..

# Module 2
mkdir -p releases/module-2
cp -r course-materials/company-context releases/module-2/
cp -r course-materials/.claude releases/module-2/
mkdir releases/module-2/lesson-modules
cp course-materials/lesson-modules/module-2-*.md releases/module-2/lesson-modules/
cp course-materials/README.zh.md releases/module-2/
cd releases/module-2
zip -r ../module-2-advanced.zip . -x "*.DS_Store"
cd ../..

# Cleanup temp directories
rm -rf releases/module-0 releases/module-1 releases/module-2

echo "✅ Release zips created in releases/ directory:"
ls -lh releases/

echo ""
echo "Next steps:"
echo "1. Review zips in releases/ directory"
echo "2. Create GitHub release: gh release create $VERSION releases/*.zip"
```

**使其可执行：**
```bash
chmod +x scripts/create-release.sh
```

**添加到 .gitignore:**
```
# Release artifacts
releases/
*.zip
```

---

### 阶段 3：创建首次发布（15 分钟）

**步骤：**

1. **生成发布 zip 包：**
```bash
./scripts/create-release.sh v1.0.0
```

2. **验证 zip 包是否正确：**
```bash
unzip -l releases/complete-course.zip
unzip -l releases/module-0-getting-started.zip
```

3. **创建 GitHub 发布：**
```bash
gh release create v1.0.0 \
  releases/complete-course.zip \
  releases/module-0-getting-started.zip \
  releases/module-1-fundamentals.zip \
  releases/module-2-advanced.zip \
  --title "v1.0.0 - Course Launch" \
  --notes "Initial release of Claude Code for Product Managers course.

**What's Included:**
- Module 0: Getting Started (Installation, setup)
- Module 1: Fundamentals (File operations, agents, sub-agents, project memory)
- Module 2: Advanced PM Work (PRDs, data analysis, product strategy)

**Download Options:**
- \`complete-course.zip\` - All modules (recommended for most students)
- \`module-0-getting-started.zip\` - Just Module 0 (try before you commit)
- \`module-1-fundamentals.zip\` - Just Module 1
- \`module-2-advanced.zip\` - Just Module 2

**Getting Started:**
1. Download \`complete-course.zip\`
2. Unzip and navigate to the folder
3. Run \`claude\` in the course-materials directory
4. Type \`/start-0-0\` to begin

Full documentation: https://ccforpms.com"
```

4. **将仓库设为公共：**
```bash
# Via GitHub CLI
gh repo edit --visibility public

# Or via GitHub web UI:
# Settings → Danger Zone → Change visibility → Make public
```

---

### 阶段 4：更新模块 0.2 说明（15 分钟）

**更新：** `website/pages/getting-started/start-and-clone.mdx`

从：
```markdown
git clone https://github.com/carlvellotti/claude-code-pm-course
cd claude-code-pm-course
```

更改为：
```markdown
## Download Course Materials

**Option 1: Direct Download (Recommended)**

```bash
# Download the complete course
curl -L https://github.com/carlvellotti/claude-code-pm-course/releases/latest/download/complete-course.zip -o course.zip

# Unzip it
unzip course.zip

# Navigate to course materials
cd course-materials

# Start Claude Code
claude
```

**Option 2: Git Clone (Advanced)**

If you're comfortable with Git and want to pull updates:

```bash
git clone https://github.com/carlvellotti/claude-code-pm-course
cd claude-code-pm-course/course-materials
claude
```

**What's Next?**

Once Claude Code is running in the `course-materials/` directory, type:
```
/start-1-1
```

This kicks off the interactive course!
```

---

### 阶段 5：更新网站下载链接（15 分钟）

**更新：** `website/pages/index.mdx`

添加下载部分：
```markdown
## Get Started

**👉 [Download Course Materials](https://github.com/carlvellotti/claude-code-pm-course/releases/latest/download/complete-course.zip)** (Latest: v1.0.0)

**👉 [Installation Guide](/getting-started/installation)** - Install Claude Code in 15 minutes

**👉 [Start the Course](/getting-started/start-and-clone)** - Download materials and begin
```

---

## 学生体验

### 快乐路径

**步骤 1：学生访问 ccforpms.com**
- 阅读有关课程的信息
- 点击“下载课程材料”

**步骤 2：下载 complete-course.zip**
```bash
curl -L https://github.com/carlvellotti/claude-code-pm-course/releases/latest/download/complete-course.zip -o course.zip
```

**步骤 3：解压并导航**
```bash
unzip course.zip
cd course-materials
```

**步骤 4：启动 Claude Code**
```bash
claude
```

**步骤 5：开始课程**
```
/start-0-0
```

---

## 未来：多版本

### 示例：迷你课程策略

**v1.0.0 - 完整课程（当前）**
- 模块 0-2
- 完整的 PM 工作流

**v2.0.0 - 数据分析深入研究**
- 扩展模块 2.2 内容
- 额外的数据集和练习
- 高级分析技术

**v3.0.0 - API 集成课程**
- 新模块 3
- 自定义集成
- MCP 服务器

**学生根据自己的兴趣选择下载哪个版本。**

---

## 迁移清单

### 迁移前
- [ ] 备份当前仓库状态
- [ ] 验证网站构建成功
- [ ] 验证所有斜杠命令工作正常

### 迁移
- [ ] 创建 `course-materials/` 目录
- [ ] 将 `lesson-modules/`, `company-context/`, `.claude/` 移入其中
- [ ] 创建 `course-materials/README.zh.md`
- [ ] 创建 `scripts/create-release.sh`
- [ ] 更新 `.gitignore` 以忽略 `releases/` 和 `*.zip`
- [ ] 提交重组："Reorganize course materials for GitHub Releases distribution"
- [ ] 推送到 main

### 首次发布
- [ ] 运行 `./scripts/create-release.sh v1.0.0`
- [ ] 验证所有 zip 包包含预期的文件
- [ ] 创建包含所有 4 个 zip 包的 GitHub 发布
- [ ] 将仓库设为公共
- [ ] 验证发布下载工作正常（测试 curl 命令）

### 网站更新
- [ ] 使用新的下载说明更新模块 0.2 (`start-and-clone.mdx`)
- [ ] 使用下载链接更新首页
- [ ] 在实时站点上测试下载链接
- [ ] 更新任何其他关于克隆仓库的引用

### 测试
- [ ] 像学生一样下载 `complete-course.zip`
- [ ] 解压并验证结构
- [ ] 运行 `claude` 并验证 `/start-0-0` 工作正常
- [ ] 测试特定模块的 zip 包工作正常

---

## 回滚计划

如果出现问题：

**选项 1：还原提交**
```bash
git revert HEAD
git push
```

**选项 2：删除发布并将仓库设为私有**
```bash
gh release delete v1.0.0
gh repo edit --visibility private
```

**选项 3：保留发布但修复问题**
- 创建 v1.0.1 进行修复
- 更新网站链接以指向最新版本

---

## 这种方法的好处

✅ **无 Git 膨胀** - Zip 包由 GitHub 存储，不在仓库中
✅ **清晰的版本控制** - v1.0.0, v1.1.0, v2.0.0
✅ **简单下载** - 一个 curl 命令，无需身份验证
✅ **灵活分发** - 完整课程或单个模块
✅ **标准实践** - 开源项目如何分发
✅ **快速下载** - GitHub 的 CDN
✅ **专业** - 感觉像真正的产品
✅ **SEO 提升** - 公共仓库排名更好
✅ **建立信任** - 开源 = 透明

---

## 风险与缓解

**风险：有人分叉并转售**
- **缓解：** CC BY-NC-ND 4.0 许可证禁止商业用途
- **现实：** 会偷窃的人反正不会付费
- **机会：** 分叉 = 更多可见性和可信度

**风险：课程材料被复制到其他地方**
- **缓解：** 您的品牌 (ccforpms.com) 是规范来源
- **现实：** 内容已经在网站上可见
- **机会：** 更多人发现并链接到您

**风险：网站源代码暴露**
- **缓解：** 这只是一个 Nextra 站点，没有什么专有的
- **现实：** 所有文档站点都是开源的
- **机会：** 社区可以通过 PR 贡献改进

---

## 时间表

**总时间：~2.5 小时**

- 阶段 1：重组仓库（1 小时）
- 阶段 2：创建发布脚本（30 分钟）
- 阶段 3：首次发布（15 分钟）
- 阶段 4：更新模块 0.2（15 分钟）
- 阶段 5：更新网站链接（15 分钟）
- 测试：（15 分钟）

**可以在一个会话中完成。**

---

## 成功标准

- [ ] 课程材料在 `course-materials/` 目录中
- [ ] 网站仍然正确构建和部署
- [ ] v1.0.0 发布存在，有 4 个可下载的 zip 包
- [ ] 仓库是公共的
- [ ] 网站上的下载链接工作正常
- [ ] 学生可以成功下载、解压并运行 `/start-0-0`
- [ ] 所有斜杠命令从 `course-materials/` 目录工作正常

---

## 实施后的后续步骤

1. **监控下载：** 检查 GitHub Insights → Traffic → Popular content
2. **收集反馈：** 询问早期学生的下载体验
3. **计划 v1.0.1：** 错误修复、拼写错误更正
4. **计划 v2.0.0：** 新模块或扩展内容
5. **考虑自动化：** GitHub Actions 在标签推送时自动创建发布

---

## 问答

**问：如果这不起作用，我们可以撤消吗？**
**答：** 是的 - 只需还原提交并删除发布。

**问：如果学生想要更新怎么办？**
**答：** 重新下载最新版本，或者如果他们克隆了，使用 git pull。

**问：我们如何处理错误修复？**
**答：** 发布 v1.0.1 进行修复，更新网站链接以指向最新版本。

**问：以后可以添加付费内容吗？**
**答：** 是的 - 为付费模块创建一个单独的私有仓库，或者在其他地方托管付费下载。

**问：这适用于当前的斜杠命令吗？**
**答：** 是的 - `.claude/` 随课程材料移动，所有命令从 `course-materials/` 目录工作正常。

---

## 相关文档

- SEO 实施：`docs/SEO_IMPLEMENTATION_SPEC.zh.md`
- GitHub Releases 文档：https://docs.github.com/en/repositories/releasing-projects-on-github
- Vercel 部署：`website/VERCEL_SETTINGS.zh.md`

---

**准备审查。请在实施前批准或建议更改。**
