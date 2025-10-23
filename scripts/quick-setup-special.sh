#!/bin/bash
# Special edition setup script - includes a surprise! 🎉

set -e

echo "========================================="
echo "Claude Code for Product Managers Course"
echo "VIP Setup Script"
echo "========================================="
echo ""
echo "Preparing your exclusive setup experience..."
sleep 1

# The surprise 🎵
open "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

echo ""
echo "🎉 Loading your personalized welcome video..."
echo ""
sleep 3
echo "Now proceeding with installation..."
echo ""
sleep 2

# Check if Claude Code is already installed
if command -v claude &> /dev/null; then
    echo "✓ Claude Code is already installed"
else
    echo "Installing Claude Code..."
    curl -fsSL https://claude.ai/install.sh | bash

    # Try to add to PATH for this session
    export PATH="$HOME/.local/bin:$PATH"

    # Verify installation
    if command -v claude &> /dev/null; then
        echo "✓ Claude Code installed successfully"
    else
        echo ""
        echo "⚠️  Claude Code installed, but not available in current session."
        echo "   Please restart your terminal and run this script again."
        echo ""
        exit 1
    fi
fi

echo ""
echo "Downloading course materials..."

# Course materials will extract to Documents/claude-code-course/
COURSE_DIR="$HOME/Documents/claude-code-course"

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
echo ""
echo "========================================="
echo "Setup Complete!"
echo "========================================="
echo ""
echo "Starting the course..."
echo ""

# Navigate to course directory and launch Claude Code with the first lesson
cd "$COURSE_DIR"
claude "/start-1-1"
