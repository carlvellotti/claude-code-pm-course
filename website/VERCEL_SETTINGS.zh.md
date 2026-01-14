# Vercel 部署设置

## Vercel 仪表板中使用的确切设置

在 Vercel 上导入项目时，请使用这些**确切**的设置：

### 项目设置
```
Project Name: claude-code-pm-course (或者你喜欢的任何名称)
```

### 构建与开发设置
```
Framework Preset:     Next.js
Root Directory:       website
Build Command:        npm run build
Output Directory:     out  
Install Command:      npm install
```

### 重要提示

1. **Root Directory（根目录）必须是 `website`** - 这很关键！
2. 所有其他设置应该能正确自动检测
3. 不要添加自定义的 `vercel.json` 文件
4. Node.js 版本：18.x 或更高（应自动检测）

## 如果构建仍然失败

在构建日志中查找错误。常见问题：

### 错误："Cannot find module" 或 "Module not found"
- 检查所有文件是否已提交到 git
- 验证 `node_modules` 是否在 `.gitignore` 中

### 错误："_meta.json not supported"
- 已修复 - 确保你拉取了 main 分支的最新代码
- 应该只有 `_meta.ts` 文件，没有 `_meta.json`

### 错误：Frontmatter 中的 "YAML parsing error"
- 已修复 - 所有 frontmatter 使用单引号
- 检查代码块之外是否有 `<` 或 `>` 符号

### 构建成功但网站是空白的
- 检查 Output Directory（输出目录）是否设置为 `out`
- 验证构建后 `/out` 目录是否包含 HTML 文件

## 本地测试

要测试 Vercel 将运行的确切构建：

```bash
cd /Users/carl/claude-code-pm-course/website
rm -rf .next out node_modules
npm install
npm run build

# 检查 out/ 目录是否有内容：
ls -la out/
```

如果本地运行正常，那么在 Vercel 上也应该正常。

## 分享错误

如果仍然失败，请分享：
1. Vercel 构建设置的截图
2. 从构建日志中复制/粘贴错误
3. 我会立即修复它！
