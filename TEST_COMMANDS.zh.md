# 测试命令

用于测试课程发布的命令。

## 下载并运行测试发布

```bash
cd ~/Documents && \
curl -L https://github.com/carlvellotti/claude-code-pm-course/releases/download/nano-banana-test-v1/complete-course.zip -o test-course.zip && \
unzip test-course.zip -d test-course && \
cd test-course && \
claude
```

## 测试斜杠命令

进入 Claude Code 后，测试这些命令：

```
/start-1-1
```

```
/start-3-1-1
```

```
/start-3-2-1
```

## 清理

```bash
cd ~/Documents && rm -rf test-course test-course.zip
```
