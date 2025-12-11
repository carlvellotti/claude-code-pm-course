# Test Commands

Commands for testing the course release.

## Download and Run Test Release

```bash
cd ~/Documents && \
curl -L https://github.com/carlvellotti/claude-code-pm-course/releases/download/nano-banana-test-v1/complete-course.zip -o test-course.zip && \
unzip test-course.zip -d test-course && \
cd test-course && \
claude
```

## Test Slash Commands

Once in Claude Code, test these:

```
/start-1-1
```

```
/start-3-1-1
```

```
/start-3-2-1
```

## Cleanup

```bash
cd ~/Documents && rm -rf test-course test-course.zip
```
