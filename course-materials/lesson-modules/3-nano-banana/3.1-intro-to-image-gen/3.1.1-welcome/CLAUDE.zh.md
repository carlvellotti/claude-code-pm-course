# 模块 3.1.1: 欢迎与第一次生成

**Claude Code 教学脚本**

---

## 教学流程

欢迎来到 **面向产品经理的 Claude Code Nano Banana Pro 课程**！

我要在这里引用课程创建者 Carl 的话：“你不会相信这有多么他妈的惊人。”

他是对的。我们将使用 Gemini 3 Pro - 也被称为 Nano Banana Pro - Google 最先进的图像生成模型。它可以创建逼真的图像，转换参考照片，生成文本覆盖，还有更多。

停止：准备好看看它能做什么了吗？

用户：是的 / 准备好了

---

在我们生成任何东西之前，我们需要设置你的 API 密钥。这大约需要 2-3 分钟，而且你只需要做一次。

首先，去 Google AI Studio：

**https://aistudio.google.com/**

停止：在浏览器中打开那个链接，到了告诉我。

用户：我到了

---

如果这是你第一次来，接受服务条款。

然后：
1. 点击左侧栏的 **“Get API Key”**
2. 点击右上角的 **“Create API key”**
3. 给你的密钥起个名字，并选择 **“Default Gemini Project”**
4. 点击仪表板上的密钥以显示它
5. 复制密钥 - 它以 "AIza..." 开头

停止：你复制好你的 API 密钥了吗？

用户：是的

---

重要提示：你还需要设置计费才能让 Gemini 3 Pro 工作。

不用担心费用 - 每张图片大约 $0.10，整个课程花费不到 $5。（这是给 Google 的，不是给 Carl 的... 很遗憾。）

1. 在 Google AI Studio 中，去 **Get API key**（左侧栏底部）
2. 在 **“Quota tier”** 列下，点击 **Set up billing**
3. 按照提示添加支付方式

停止：你的计费设置好了吗？

用户：是的 / 完成

---

现在让我们把你的 API 密钥添加到这个项目中。你有两个选择：

**选项 1:** 直接在这里粘贴你的 API 密钥，我为你创建 `.env` 文件。

**选项 2:** 自己做 - 将 `.env.example` 复制为 `.env` 并添加你的密钥：`GEMINI_API_KEY=YourKeyHere`

停止：在这里粘贴你的 API 密钥，或者如果你手动设置好了说“完成”。

用户：[粘贴 API 密钥] / 完成

---

行动：如果用户提供了 API 密钥，创建带有 `GEMINI_API_KEY=[他们的密钥]` 的 `.env` 文件。如果用户说“完成”，验证 `.env` 是否存在。

太好了，你都设置好了！

现在是有趣的部分 - 让我们生成你的第一张图像。

我有一张课程创建者 Carl 的参考照片。如果你想看的话，可以在 `lesson-modules/3-nano-banana/3.1-intro-to-image-gen/3.1.1-welcome/carl-reference.JPG` 找到它。我们要让他穿上香蕉服来欢迎你加入课程。

停止：说“生成 Carl 穿着香蕉服欢迎我加入 Nano Banana”

用户：生成 Carl 穿着香蕉服欢迎我加入 Nano Banana

---
这大约需要 10-15 秒

行动：运行 generate()，使用参考图像 `carl-reference.JPG` 和提示词：“Carl in a bright yellow banana suit, standing confidently with arms crossed, big friendly smile, ready to teach. Text overlay says 'Welcome to Nano Banana!' Professional course instructor vibe but fun and playful.”

你的图像已保存到 `outputs/` 文件夹 - 打开它看看结果！

停止：你觉得怎么样？

用户：关于图像的回应

---

相当不可思议，对吧？

这就是 Gemini 3 Pro。它可以获取参考照片并对其进行转换，同时保持人物的可识别性。而且因为我们在 Claude Code 中做这件事，我为你处理所有的复杂性：

- API 调用
- 会话管理
- 保存输出
- 选择智能参数

通过本课程，你将建立自己的提示词、参考图像和风格系统。我们将从一般用途开始，然后在下一个模块中转向产品经理用例。

停止：想听听本模块接下来有什么吗？

用户：是的

---

这是我们在模块 3.1 中将要涵盖的内容：

- **理解基础** - generate() 函数如何工作，可用参数，输出结构
- **一致性与风格** - 使用参考图像，建立风格数据库，从现有图像中提取风格
- **迭代策略** - 会话，逐步优化图像，需要时回滚

一旦你掌握了基础知识，模块 3.2 将向你展示具体的产品经理用例，如样机、画像和图表。

停止：准备好继续下一课了吗？

用户：是的 / 准备好了

---

太棒了！在下一课中，你将学习 `generate()` 函数如何工作以及所有可用的选项。

当你准备好继续时，运行 `/start-3-1-2`。

行动：结束模块

---

## 给 Claude 的重要提示

**本模块中的文件操作：**
- 读取 `.env.example` 向学生展示模板
- 当学生请求时将 `.env.example` 复制为 `.env`
- 学生手动粘贴他们的 API 密钥 - 不要试图为他们插入

**对于图像生成：**
- 使用 `image_gen.py` 中的 `generate()` 函数
- 传递参考图像路径和指定的准确提示词
- 输出将自动保存到 `outputs/`

**如果出了问题：**
- API 密钥错误：让他们仔细检查密钥是否正确粘贴在 `.env` 中
- 计费错误：确认 Google AI Studio 设置中已设置计费
- 生成失败：检查错误消息并相应地进行故障排除

**打开图像：** 如果用户在查找图像时遇到困难，主动提出使用 `open [path]` (Mac) 或 `start [path]` (Windows) 为他们打开。

---

## 成功标准

模块 3.1.1 是成功的，如果学生：

- ✅ 在 `.env` 中设置了他们的 Gemini API 密钥
- ✅ 在 Google AI Studio 中配置了计费
- ✅ 生成了他们的第一张图像（Carl 穿香蕉服）
- ✅ 理解他们将在本模块中学到什么
- ✅ 知道如何继续下一课

---

**记住：这是学生第一次尝试图像生成。让它变得神奇。第一张生成的图像带来的“哇”时刻为整个模块定下了基调。**
