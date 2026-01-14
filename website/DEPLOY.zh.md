# 部署到 Vercel

网站已经准备好部署了！以下是你的选项：

## 快速部署（推荐）

### 选项 1：通过 Vercel 仪表板部署

1. **推送到 GitHub**（如果你还没有这样做）：
   ```bash
   cd /Users/carl/claude-code-pm-course
   git add website/
   git commit -m "Add Nextra documentation website"
   git push origin main
   ```

2. **前往 Vercel**：
   - 访问 https://vercel.com/new
   - 使用 GitHub 登录
   - 点击 "Import Project"（导入项目）
   - 选择你的仓库：`carlvellotti/claude-code-pm-course`

3. **配置构建设置**：
   - **Root Directory**（根目录）：`website`
   - **Framework Preset**（框架预设）：Next.js
   - **Build Command**（构建命令）：`npm run build`（默认即可）
   - **Output Directory**（输出目录）：`out`
   - **Install Command**（安装命令）：`npm install`（默认即可）

4. **部署**：
   - 点击 "Deploy"（部署）
   - 等待约 2-3 分钟进行构建
   - 你的网站将在 `https://your-project.vercel.app` 上线

5. **自定义域名**（可选）：
   - 在 Vercel 仪表板中，前往 Settings → Domains
   - 添加你的自定义域名
   - 按照 DNS 说明进行操作

## 选项 2：通过 Vercel CLI 部署

```bash
# 全局安装 Vercel CLI
npm install -g vercel

# 导航到 website 目录
cd /Users/carl/claude-code-pm-course/website

# 登录 Vercel（仅第一次需要）
vercel login

# 部署到预览环境
vercel

# 部署到生产环境
vercel --prod
```

## 部署内容

构建好的网站包括：
- ✅ 所有课程内容（20 个页面）
- ✅ 左侧侧边栏导航
- ✅ 右侧目录
- ✅ 客户端搜索（Pagefind）
- ✅ 公司背景部分
- ✅ 所有图片
- ✅ 响应式移动端布局
- ✅ 快速静态网站（无需服务器）

## 部署后

部署完成后：

1. **测试网站**：
   - 检查所有导航链接是否正常工作
   - 测试搜索功能
   - 验证图片是否正确加载
   - 在移动设备上测试

2. **更新 README** 为即时 URL

3. **分享链接**！

## 更新内容

要在部署后更新网站：

1. 编辑 `/lesson-modules/` 中的 REFERENCE_GUIDE.md 文件
2. 运行转换脚本：
   ```bash
   cd /Users/carl/claude-code-pm-course/website
   ./convert-content.sh
   ```
3. 本地构建和测试：
   ```bash
   npm run build
   npm run preview  # 本地测试
   ```
4. 提交并推送：
   ```bash
   git add .
   git commit -m "Update course content"
   git push
   ```
5. Vercel 将自动重新构建并重新部署！

## 故障排除

### 在 Vercel 上构建失败
- 在 Vercel 仪表板中检查构建日志
- 确保 `website/` 被设置为根目录
- 验证 Node.js 版本（应为 18+）

### 搜索不工作
- Pagefind 在 `postbuild` 脚本中运行
- 检查构建输出中是否存在 `/pagefind/` 目录
- 清除浏览器缓存

### 图片未加载
- 图片应位于 `/public/images/` 中
- 在 MDX 文件中引用为 `/images/filename.png`
- 检查浏览器控制台是否有 404 错误

## 环境变量

不需要！这是一个没有后端或密钥的静态网站。

## 成本

**Vercel 免费层级包括：**
- 无限部署
- 每月 100 GB 带宽
- 自动 HTTPS
- 自定义域名
- PR 的预览部署

你的静态文档网站完全可以适应免费层级。

---

**准备好部署了吗？** 按照上面的选项 1（Vercel 仪表板）操作 - 这是最简单的！🚀
