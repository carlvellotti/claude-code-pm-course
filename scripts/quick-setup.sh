#!/bin/bash

# 注意：不使用 'set -e'，以便脚本可以优雅地处理错误

# 测试模式标志 - 设置为 1 以模拟执行而不实际更改
TEST_MODE=${TEST_MODE:-0}

if [ "$TEST_MODE" = "1" ]; then
    echo "========================================="
    echo "测试模式 - 不会进行任何更改"
    echo "========================================="
    echo ""
fi

echo "========================================="
echo "产品经理 Claude Code 课程"
echo "快速设置脚本"
echo "========================================="
echo ""

# 检查 Node.js 版本
echo "正在检查先决条件..."
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version | cut -d 'v' -f 2 | cut -d '.' -f 1)
    if [ "$NODE_VERSION" -ge 18 ]; then
        echo "✓ Node.js $(node --version) 已安装"
    else
        echo "⚠️  发现 Node.js $(node --version)，但需要 18+ 版本"
        echo "正在升级 Node.js..."
        if [ "$TEST_MODE" = "1" ]; then
            echo "[测试] 将通过 Homebrew 升级 Node.js"
        else
            brew upgrade node
        fi
    fi
else
    echo "未找到 Node.js。正在安装..."
    if [ "$TEST_MODE" = "1" ]; then
        echo "[测试] 将安装 Node.js"
    else
        # 检查是否已安装 Homebrew
        if ! command -v brew &> /dev/null; then
            echo "正在首先安装 Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" < /dev/null
        fi

        echo "正在通过 Homebrew 安装 Node.js..."
        brew install node < /dev/null

        # 将 Homebrew 的 bin 目录添加到当前脚本会话的 PATH 中
        export PATH="/opt/homebrew/bin:$PATH"

        echo "✓ Node.js 已安装"
    fi
fi

echo ""

# 检查 Claude Code 是否已安装
if command -v claude &> /dev/null; then
    echo "✓ Claude Code 已安装"
else
    echo "正在安装 Claude Code..."
    if [ "$TEST_MODE" = "1" ]; then
        echo "[测试] 将运行：curl -fsSL https://claude.ai/install.sh | bash"
        echo "✓ [测试] Claude Code 安装已模拟"
    else
        curl -fsSL https://claude.ai/install.sh | bash < /dev/null

        # 尝试将其添加到当前会话的 PATH 中
        # Claude Code 通常安装在 macOS/Linux 的 ~/.local/bin
        export PATH="$HOME/.local/bin:$PATH"

        # 验证安装
        if command -v claude &> /dev/null; then
            echo "✓ Claude Code 安装成功"
        else
            echo ""
            echo "⚠️  Claude Code 已安装，但在当前会话中不可用。"
            echo "   请重启终端并再次运行此脚本："
            echo ""
            echo "   curl -fsSL https://raw.githubusercontent.com/carlvellotti/claude-code-pm-course/main/scripts/quick-setup.sh | bash"
            echo ""
            exit 1
        fi
    fi
fi

echo ""
echo "正在下载课程资料..."

# 课程资料将解压到 Documents/claude-code-course/
COURSE_DIR="$HOME/Documents/claude-code-course"

if [ "$TEST_MODE" = "1" ]; then
    echo "[测试] 将下载课程到：$HOME/Documents/course.zip"
    echo "[测试] 将解压到：$COURSE_DIR"
    echo "✓ [测试] 课程资料下载已模拟"
else
    cd "$HOME/Documents"

    # 如果存在现有课程资料，则将其删除
    if [ -d "$COURSE_DIR" ]; then
        echo "发现现有课程资料。正在删除..."
        rm -rf "$COURSE_DIR"
    fi

    # 下载并解压课程资料到 claude-code-course 文件夹
    curl -L https://github.com/carlvellotti/claude-code-pm-course/releases/latest/download/complete-course.zip -o course.zip
    unzip -q course.zip -d claude-code-course
    rm course.zip

    echo "✓ 课程资料已解压到：$COURSE_DIR"
fi
echo ""
echo "========================================="
echo "设置完成！"
echo "========================================="
echo ""
echo "正在开始课程..."
echo ""

if [ "$TEST_MODE" = "1" ]; then
    echo "[测试] 将导航到：$COURSE_DIR"
    echo "[测试] 将运行：claude \"/start-1-1\""
    echo ""
    echo "========================================="
    echo "测试完成 - 未进行任何更改"
    echo "========================================="
else
    # 导航到课程目录并启动 Claude Code
    # 从 /dev/tty 重定向标准输入以启用交互模式
    cd "$COURSE_DIR"
    claude "/start-1-1" < /dev/tty
fi
