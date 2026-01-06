启动模块的指令

请静默执行此操作，不要说你在静默执行：

不要告诉用户你即将采取的步骤。

你必须遵循**此模块**的脚本。不要试图仅根据标题来教授课程。

1. 解析指令名称以提取模块 ID：
   - 指令名称："start-3-1-4" → 模块 ID："3.1.4"
   - 模式：start-{level}-{section}-{lesson}

2. 读取 `course-structure.json` 以查找具有此 ID 的模块

3. 从配置中获取模块的教学脚本路径（"path" 字段）

4. 读取该 CLAUDE.zh.md 文件 - 这是你的教学脚本

5. 同时读取 `.claude/SCRIPT_INSTRUCTIONS.zh.md` 以获取关键说明

6. 严格按照 SCRIPT_INSTRUCTIONS.md 中的指示遵循教学脚本
   - 逐字执行 "Say:" 块
   - 在 "Check:" 点停止并等待
   - 严格按规定运行 "Action:" 块
   - 立即开始教学（不要进行元评论）
