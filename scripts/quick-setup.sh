#!/bin/bash

set -e  # Exit on any error

# Test mode flag - set to 1 to simulate without executing
TEST_MODE=${TEST_MODE:-0}

if [ "$TEST_MODE" = "1" ]; then
    echo "========================================="
    echo "TEST MODE - No changes will be made"
    echo "========================================="
    echo ""
fi

echo "========================================="
echo "Claude Code for Product Managers Course"
echo "Quick Setup Script"
echo "========================================="
echo ""

# Check if Claude Code is already installed
if command -v claude &> /dev/null; then
    echo "✓ Claude Code is already installed"
else
    echo "Installing Claude Code..."
    if [ "$TEST_MODE" = "1" ]; then
        echo "[TEST] Would run: curl -fsSL https://claude.ai/install.sh | bash"
        echo "✓ [TEST] Claude Code installation simulated"
    else
        curl -fsSL https://claude.ai/install.sh | bash

        # Try to add to PATH for this session
        # Claude Code typically installs to ~/.local/bin on macOS/Linux
        export PATH="$HOME/.local/bin:$PATH"

        # Verify installation
        if command -v claude &> /dev/null; then
            echo "✓ Claude Code installed successfully"
        else
            echo ""
            echo "⚠️  Claude Code installed, but not available in current session."
            echo "   Please restart your terminal and run this script again:"
            echo ""
            echo "   curl -fsSL https://raw.githubusercontent.com/carlvellotti/claude-code-pm-course/main/scripts/quick-setup.sh | bash"
            echo ""
            exit 1
        fi
    fi
fi

echo ""
echo "Downloading course materials..."

# Course materials will extract to Documents/claude-code-course/
COURSE_DIR="$HOME/Documents/claude-code-course"

if [ "$TEST_MODE" = "1" ]; then
    echo "[TEST] Would download course to: $HOME/Documents/course.zip"
    echo "[TEST] Would extract to: $COURSE_DIR"
    echo "✓ [TEST] Course materials download simulated"
else
    cd "$HOME/Documents"

    # Remove existing course materials if they exist
    if [ -d "$COURSE_DIR" ]; then
        echo "Found existing course materials. Removing..."
        rm -rf "$COURSE_DIR"
    fi

    # Download and extract course materials into claude-code-course folder
    curl -L https://github.com/carlvellotti/claude-code-pm-course/releases/latest/download/complete-course.zip -o course.zip
    unzip -q course.zip -d claude-code-course
    rm course.zip

    echo "✓ Course materials extracted to: $COURSE_DIR"
fi
echo ""
echo "========================================="
echo "Setup Complete!"
echo "========================================="
echo ""
echo "Starting the course..."
echo ""

if [ "$TEST_MODE" = "1" ]; then
    echo "[TEST] Would navigate to: $COURSE_DIR"
    echo "[TEST] Would run: claude \"/start-1-1\""
    echo ""
    echo "========================================="
    echo "TEST COMPLETE - No changes were made"
    echo "========================================="
else
    # Navigate to course directory and launch Claude Code
    # Redirect stdin from /dev/tty to enable interactive mode when piped
    cd "$COURSE_DIR"
    claude "/start-1-1" < /dev/tty
fi
