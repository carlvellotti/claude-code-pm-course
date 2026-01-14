---
name: pptx
description: 从 markdown 文档创建 PowerPoint 演示文稿。当用户需要将战略文档、PRD 或分析转换为专业的幻灯片组以进行利益相关者演示时，使用此技能。
---

# PowerPoint 演示文稿创建技能

你可以从 markdown 文档创建专业的 PowerPoint 演示文稿（.pptx 文件）。此技能旨在帮助产品经理将其书面工作转化为适合高管的幻灯片组。

## 能力

- 将 markdown 文档转换为 PowerPoint 演示文稿
- 根据内容结构创建适当的幻灯片布局
- 应用专业的格式和设计
- 生成标题幻灯片、内容幻灯片和摘要幻灯片
- 支持战略演示、PRD 和分析文档

## 何时使用此技能

当用户需要执行以下操作时使用此技能：
- 从战略文档创建高管演示文稿
- 将书面分析转化为幻灯片组
- 向利益相关者展示 PRD 或功能规格
- 为领导层审查生成专业幻灯片

## 如何创建演示文稿

创建演示文稿时，请遵循此工作流程：

### 1. 分析源文档

阅读 markdown 文档并识别：
- 应成为幻灯片的主要部分
- 关键点和支持细节
- 视觉层次和流程
- 高管摘要内容

### 2. 设计幻灯片结构

规划演示文稿结构：
- **标题幻灯片**：文档标题、日期、背景
- **高管摘要**：关键要点（1-2 张幻灯片）
- **主要内容幻灯片**：每个主要部分一张幻灯片
- **详情幻灯片**：支持信息，分解以提高可读性
- **结束幻灯片**：摘要、后续步骤或行动号召

### 3. 创建演示文稿

使用 Python 和 `python-pptx` 库生成 .pptx 文件：

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

# Create presentation object
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# Define reusable layouts
def add_title_slide(prs, title, subtitle):
    slide = prs.slides.add_slide(prs.slide_layouts[0])  # Title layout
    slide.shapes.title.text = title
    slide.placeholders[1].text = subtitle
    return slide

def add_content_slide(prs, title, content_items):
    slide = prs.slides.add_slide(prs.slide_layouts[1])  # Title and Content layout
    slide.shapes.title.text = title

    # Add content as bullet points
    body = slide.placeholders[1].text_frame
    for item in content_items:
        p = body.add_paragraph()
        p.text = item
        p.level = 0
    return slide

def add_section_slide(prs, section_title):
    slide = prs.slides.add_slide(prs.slide_layouts[2])  # Section header layout
    slide.shapes.title.text = section_title
    return slide

# Example: Create slides
add_title_slide(prs, "Strategy Title", "Presentation Date")
add_section_slide(prs, "Section 1: Diagnosis")
add_content_slide(prs, "Key Findings", [
    "Finding 1: Description here",
    "Finding 2: Description here",
    "Finding 3: Description here"
])

# Save presentation
prs.save('output.pptx')
```

### 4. 格式指南

应用专业格式：

**排版：**
- 标题字体：幻灯片标题 44pt，章节标题 54pt
- 正文文本：主要内容 18-24pt，详情 16pt
- 使用无衬线字体（Calibri, Arial, 或 Helvetica）

**布局：**
- 每张幻灯片最多 3-5 个要点
- 使用两栏布局进行比较
- 将密集内容拆分到多张幻灯片
- 留白以提高可读性

**内容原则：**
- 每张幻灯片一个核心观点
- 使用主动、简洁的语言
- 要点结构应平行
- 包含幻灯片编号以供参考

**特殊幻灯片类型：**

*战略幻灯片：*
- 诊断 → 指导方针 → 行动结构
- 使用视觉层次显示关系
- 突出权衡和关键决策

*路线图幻灯片：*
- 按季度/月的时间轴视图
- 对相关举措进行分组
- 标出依赖关系

*指标幻灯片：*
- 当前 vs 目标绩效
- 使用简单的表格或图表（口头描述，作为格式化文本实施）
- 包含成功标准

## 输出

创建演示文稿后：
1. 使用描述性名称保存 .pptx 文件
2. 向用户确认文件位置
3. 总结幻灯片结构（幻灯片数量和关键部分）
4. 说明为适应演示格式而简化或重组的任何内容

## 依赖项

此技能需要 `python-pptx` 库。如果未安装，引导用户安装它：

```bash
pip install python-pptx
```

## 最佳实践

- **高管优先**：从高管能在 2 分钟内读完的摘要幻灯片开始
- **可扫描**：每张幻灯片应在 10 秒内被理解
- **可操作**：以明确的后续步骤或所需决策结束
- **专业**：始终使用一致的格式
- **上下文感知**：根据受众调整正式程度和细节

## 示例用法

**用户请求**：“从我的战略文档创建一个幻灯片组”

**你的工作流程**：
1. 阅读战略文档
2. 识别关键部分（诊断、指导方针、行动等）
3. 规划约 12-15 张涵盖战略的幻灯片
4. 使用 python-pptx 生成 Python 代码
5. 创建 .pptx 文件
6. 确认创建并总结结构

## 备注

- 对于本课程，演示文稿用于将 PM 文档（战略、PRD、分析）转换为适合利益相关者的格式
- 关注清晰度和专业性，而非视觉设计的复杂性
- 如有疑问，使用层次清晰的简单布局
- 目标是让书面工作准备好进行演示，而不是制作营销材料
