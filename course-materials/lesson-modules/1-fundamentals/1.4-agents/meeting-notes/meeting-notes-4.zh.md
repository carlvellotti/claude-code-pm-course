DESIGN REVIEW - DARK MODE IMPLEMENTATION
日期：2024-10-09
与会：Jordan Kim（设计负责人）、你（高级 PM）、前端 TL、UX 设计师 Amy

讨论：
- Jordan 讲解暗黑模式设计，审查配色/对比/可及性，均达 WCAG AAA。
- 讨论实现：默认跟随系统，同时提供手动开关；开关放在用户设置。
- 边界：嵌入图片/截图、代码高亮、Figma embed。大多已处理，但 Figma embed 在暗黑下发灰，Amy 去问 Figma 团队暗黑支持。
- 前端估 2-3 周；部分组件需重构支持主题。建议分阶段发布：先核心 UI，再集成/嵌入。

行动项：
- Jordan 10/12 前定稿设计系统色彩 tokens
- 前端 TL 10/11 前给分阶段实施计划
- Amy 联系 Figma 询问暗黑 embed 支持
- 你更新 PRD，加入分阶段方案
- 前端 10/14 当周开工

决定：暗黑分 2 阶段。Phase1 核心 UI 11/15 前；Phase2 集成 12/01 前。