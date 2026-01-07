# 模块 3.1.4: 构建你的风格数据库

欢迎来到模块 3.1.4: 构建你的风格数据库。

到目前为止，我们已经学习了如何生成图像并应用黄金法则。但这里有一个更大的游戏 - 一个将普通用户与高级用户区分开来的游戏。

元技能是：建立一个随你成长的个人创意工具包。你不是每次都从头开始，而是建立一个可以重用的风格库。

想一想 - 你创造的每一张好图，每一个完美运作的提示词，你发现的每一个风格... 它们都成为你工具包的一部分。这就是偶尔使用 AI 与将 AI 作为创意超能力之间的区别。

停止：目前为止有道理吗？

用户：是的

---

这就是 Claude Code 成为你完美伙伴的地方。我可以为你管理整个风格数据库。只需说“使用风格 #3”或“把这个添加到我的库”，我就会处理一切 - 完整的上下文，无需复制粘贴，无需在旧聊天记录中寻找。

有三种扩展你的库的方法：
- **边做边存 (Save prompts as you go)** - 当你做出你喜欢的东西时
- **从网上收集 (Collect prompts from online)** - 数据库、社交媒体、教程
- **从任何图像提取 (Extract styles from any image)** - 大招

我们今天会尝试所有这三种方法。

我已经为你设置了一个初始风格库。让我自动在你的浏览器中打开它。

行动：在用户浏览器中打开风格库：
- Mac: `open [style-library.html 的绝对路径]`
- Windows: `start [style-library.html 的绝对路径]`

它应该刚刚在你的浏览器中打开了。

停止：看一看风格库。当你浏览完后告诉我。

用户：打开了

---

## 第 2 部分：介绍风格库

现在，重要澄清：这不是一个真正的网站！它只是一个本地 HTML 文件 - 一种直接从你的电脑可视化你的风格集合的方式。

最酷的部分是：你总是可以通过问我来改变设计或功能。现在不要做，但在未来你可以让我添加新列、改变布局、添加搜索功能 - 无论你想要什么。这是你的工具包。让它为你服务。

停止：很酷，对吧？

用户：是的

---

让我为你介绍一下结构。每个风格都有：
- **索引号** - 这样你就可以直接说“使用风格 #02”
- **缩略图预览** - 悬停放大
- **名称和标签** - 用于快速扫描
- **类别** - 用于筛选
- **完整提示词** - 悬停展开，点击复制
- **示例用途** - 这样你就知道何时使用它

试试顶部的筛选按钮来查看不同的类别。

停止：花一分钟浏览一下。哪个风格吸引了你的眼球？

用户：[选择一个风格]

---

很好的选择！让我们试一试。

停止：你想用那种风格生成什么主题？告诉我风格编号和你的主题。

用户：[风格编号和主题]

行动：运行 `python3 get_style.py [number]` 获取风格提示词。然后使用该提示词结合他们的主题生成图像。

你的图像准备好了！

行动：提供输出图像文件的确切路径

打开 outputs 文件夹查看它。

停止：你觉得怎么样？

用户：[回应]

---

## 第 3 部分：扩展你的库 - 方法 1：边做边存

这是使用库的第一种方法 - 选择现有风格。现在让我们谈谈 **扩展** 它。

方法 1 最简单：边做边存。每当你创造出你喜欢的东西，就告诉我把它添加到你的库中。

让我们试一试。我要你生成任何你想要的图像。

停止：你想创作什么？任何主题，任何风格 - 随你描述。

用户：[描述他们的图像]

---

行动：根据他们的描述使用 image_gen.py 生成图像

完成！检查 outputs 文件夹查看你的图像。

行动：提供输出图像文件的确切路径

停止：看一看 - 你喜欢这个风格吗？

用户：[回应]

---

如果你喜欢它，你可以将此风格保存到你的库中以备将来使用。

停止：试一试 - 告诉我把这个风格添加到你的库中。

用户：把这个添加到我的库 / Add this style to my library

行动：用新的风格条目更新 style-library.html：
- 找到下一个可用的 ID 号
- 从提示词中提取描述性名称
- 从以下类别中选择合适的类别：Illustration（插画）, Photo - Portrait（照片-肖像）, Photo - Product（照片-产品）, Photo - Environment（照片-环境）, Diagram（图表）, UI/Mockup（UI/样机）, 3D/Isometric（3D/等轴测）, Presentation（演示）, Marketing（营销）, Artistic（艺术）
- 添加 3-5 个相关标签
- 将输出图像复制到 thumbnails/ 文件夹，使用描述性文件名
- 将条目添加到 JavaScript 部分的 styles 数组中
- 写一个简短的“exampleUse”描述

完成！刷新浏览器中的风格库。

停止：看到你的新风格了吗？

用户：是的

---

这就是方法 1 - 边做边存。每次你创造出你喜欢的东西，就告诉我保存它。随着时间的推移，你的库将变成一个经过验证的风格金矿。

停止：准备好尝试方法 2 了吗？

用户：是的

---

## 第 4 部分：扩展你的库 - 方法 2：从网上收集

方法 2：从网上收集提示词。社交媒体、提示词数据库和教程上到处都是惊人的提示词。当你找到一个喜欢的，测试它，然后把它添加到你的库中。

这是来自 Nano Banana 官方账号的一个很好的例子：https://x.com/NanoBanana/status/1998085942201163905

提示词是：“Make a photo that is perfectly isometric. It is not a miniature, it is a captured photo that just happened to be perfectly isometric. It is a photo of [subject].”

停止：我们应该用什么主题来制作等轴测照片？

用户：[他们的主题]

---

行动：使用他们的主题生成等轴测图像，提示词为：“Make a photo that is perfectly isometric. It is not a miniature, it is a captured photo that just happened to be perfectly isometric. It is a photo of [their subject].”

看看你的等轴测照片！

行动：提供输出图像文件的确切路径

打开 outputs 文件夹查看它。

停止：很酷的效果，对吧？你想把这个风格添加到你的库中吗？

用户：是的 / 把这个添加到我的库

行动：用等轴测风格更新 style-library.html：
- 名称：“Perfect Isometric Photo”
- 类别：“3D/Isometric”
- 标签：["isometric", "photography", "geometric", "perspective"]
- 提示词：“Make a photo that is perfectly isometric. It is not a miniature, it is a captured photo that just happened to be perfectly isometric. It is a photo of [subject].”
- 将输出图像复制到 thumbnails/
- 将条目添加到 styles 数组

完成！刷新你的浏览器查看它。

停止：添加了两个风格！准备好尝试大招了吗？

用户：是的

---

## 第 5 部分：扩展你的库 - 方法 3：从任何图像提取

方法 3 是大招。

Gemini 3 Pro 不仅仅擅长创建图像 - 它拥有任何模型中最好的图像理解能力。这意味着我们可以从 **任何** 图像中提取风格并重新创建它。

在 Pinterest 上看到喜欢的图片？Instagram？杂志？提取风格，永远保存。

我构建了一个风格提取模块来专门做这件事。

停止：想看看它的实际效果吗？

用户：是的

---

行动：确认 lesson-modules/3-nano-banana/ 目录中存在 style_extract.py 文件

`style_extract.py` 模块分析任何图像并提取详细的风格信息。不是作为 JSON 或结构化数据 - 而是作为 Gemini 可以直接使用的自然语言。

它捕捉：调色板、光照、构图、纹理、情绪、艺术风格、排版、特效 - 所有让图像看起来那样的元素。

让我们在一张故意 **很难** 的图片上测试它。

行动：获取此模块文件夹中 recursive-painter.jpg 的确切路径

打开此文件查看它：[提供确切路径]

停止：你看到了吗？这是一个男人在画他自己画他自己，还有一台 CRT 电视显示着同样的场景 - 带有日期戳的 90 年代美学。

用户：是的，我看到了

递归、复杂、分层。如果我们能提取 **这种** 风格，我们就能提取任何风格。

停止：准备好运行提取了吗？

用户：是的

---

行动：通过执行以下代码在 recursive-painter.jpg 上运行风格提取：
```python
import sys
sys.path.insert(0, '[course root path]')
from style_extract import extract_style
result = extract_style('[path to recursive-painter.jpg]')
print(result)
```

这是提取发现的内容：

行动：向用户显示提取的风格描述

[明确显示输出]

看看所有这些细节 - 调色板、光照质量、构图说明、纹理描述。

现在真正的测试来了：我们能否仅凭这段文字描述重新创建 **完全相同** 的图像？

停止：告诉我使用提取的风格重新创建图像。

用户：重新创建图像 / 生成它

---

行动：使用提取的风格描述生成图像。提示词应该重新创建递归画家场景 - 一个男人在艺术工作室画他自己画他自己，有一台 CRT 电视显示同样的递归场景，90 年代模拟快照美学，带有日期戳。

行动：提供输出图像文件的确切路径

打开输出并与原图并排比较。

停止：你觉得怎么样？你能看到捕捉到了相同的风格吗？

用户：[回应 - 应该印象深刻]

---

这就是惊叹时刻。

我们拿了一张复杂、分层、递归的图像，并将其本质提取为纯文本。然后从头开始重新创建了它。

现在想象一下用你喜欢的任何图像做这件事 - 你想捕捉的任何风格。Pinterest 灵感 → 提取 → 保存 → 永远属于你。

停止：想把这个提取的风格添加到你的库中吗？

用户：是的 / 添加它

行动：用 90 年代模拟快照风格更新 style-library.html：
- 名称：“90s Analog Snapshot”
- 类别：“Photo - Portrait”
- 标签：["vintage", "film grain", "flash", "nostalgic", "datestamp"]
- 提示词：使用提取的风格描述
- 将生成的输出图像复制到 thumbnails/
- 将条目添加到 styles 数组

刷新你的浏览器 - 你现在有了三个新风格！

停止：你的库看起来怎么样？

用户：[回应]

---

## 第 6 部分：总结

让我们回顾一下你学到了什么。

元技能：建立一个随你成长的个人创意工具包。扩展库的三种方法：
- **边做边存** - 创造喜欢的东西 → 添加它
- **从网上收集** - 找到提示词 → 测试 → 保存
- **从任何图像提取** - 大招

任何你喜欢的图像 → 提取 → 保存 → 永远重用。而且我为你管理这一切 - 只需说“使用风格 #3”或“把这个添加到我的库”。

停止：关于构建你的风格数据库有什么问题吗？

用户：[有问题或没有]

---

你现在对使用 Nano Banana Pro 所需的一切有了完整、高级的理解。你知道黄金法则，你知道如何迭代，你知道如何构建风格工具包。

在模块 3.2 中，我们将把所有这些学习应用到实际的产品经理用例中 - 样机、图表、演示文稿等等。

停止：准备好进入模块 3.2 了吗？

用户：是的

太好了！输入 `/start-3-2-1` 继续。

---

## 给 Claude 的重要提示

### 文件路径
- `style-library.html` 在此模块文件夹中：`lesson-modules/3-nano-banana/3.1-intro-to-image-gen/3.1.4-style-database/`
- `recursive-painter.jpg` 也在从模块文件夹中
- `style_extract.py` 和 `image_gen.py` 在 `lesson-modules/3-nano-banana/` 中
- 输出图像去往 `lesson-modules/3-nano-banana/outputs/`
- 缩略图去往此模块文件夹中的 `thumbnails/` 文件夹

### 添加风格到库时
1. 读取当前的 style-library.html 以找到 styles 数组和 CANONICAL_TAGS 对象
2. 确定下一个 ID 号
3. 创建一个描述性名称
4. 从 CATEGORIES 数组中选择一个类别（见下文）
5. 仅从该类别的 CANONICAL_TAGS 中选择 2-4 个标签
6. 将输出图像复制到 thumbnails/ 并使用 kebab-case 文件名
7. 将新条目添加到 HTML 文件中的 styles 数组
8. 更新缩略图路径以指向新文件

### 类别和规范标签
style-library.html 包含 CATEGORIES 和 CANONICAL_TAGS 对象。你必须严格使用这些：

**类别 (Categories):** Framework, Flow, Architecture, Mockup, Persona, Marketing, Artistic

**按类别的规范标签 (Canonical Tags):**
- **Framework:** 2x2-matrix, pyramid, venn, canvas, concentric, triangle
- **Flow:** process, journey-map, flowchart, steps, sequence
- **Architecture:** hierarchy, hub-spoke, system-diagram, org-chart, tree
- **Mockup:** wireframe, device-frame, ui-concept, landing-page, mobile, desktop
- **Persona:** portrait, lifestyle, headshot, context, illustrated, scene
- **Marketing:** ad, social, announcement, banner, hero
- **Artistic:** flat-illustration, hand-drawn, watercolor, photography, retro, minimalist, bold-graphic, 3d-render

不要发明新标签或类别。始终参考 HTML 文件中的 CANONICAL_TAGS。

**注意：** 用户可以组合不同类别的风格（例如，“使用 Artistic 中的复古风格和 Persona 中的场景风格”）来创建可组合的结果。

### 运行风格提取
使用 style_extract.py 中的 extract_style() 函数。它接受图像路径并返回视觉风格的详细自然语言描述。

### 终端限制
- 无法直接显示图像 - 始终提供文件路径供用户打开
- 使用封闭式验证问题（“你看到了吗？”）而不是开放式问题
- **打开图像：** 如果用户在查找图像时遇到困难，主动提出使用 `open [path]` (Mac) 或 `start [path]` (Windows) 为他们打开

## 成功标准

当满足以下条件时，模块完成：
- [ ] 用户已经打开并探索了风格库 HTML
- [ ] 用户已经使用库中的现有风格生成了图像
- [ ] 用户已经使用方法 1（边做边存）添加了至少一个自定义风格
- [ ] 用户已经使用方法 2（从网上收集）添加了等轴测风格
- [ ] 用户已经在 recursive-painter.jpg 上看到了风格提取的实际效果
- [ ] 用户已经看到了重新创建的图像与原图的对比
- [ ] 用户已经被提议将提取的风格添加到他们的库中
- [ ] 用户被引导至模块 3.2，使用 `/start-3-2-1`
