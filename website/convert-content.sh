#!/bin/bash

# Script to convert REFERENCE_GUIDE.md files to MDX for Nextra site
# This automates the entire content conversion process

set -e  # Exit on error

COURSE_ROOT="/Users/carl/claude-code-pm-course"
WEBSITE_DIR="$COURSE_ROOT/website"
PAGES_DIR="$WEBSITE_DIR/pages"

echo "🚀 Starting content conversion..."

# Function to add frontmatter and convert to MDX
convert_to_mdx() {
    local source_file=$1
    local dest_file=$2
    local title=$3
    local description=$4
    
    # Extract first paragraph after title as description if not provided
    if [ -z "$description" ]; then
        description=$(grep -A 5 "^#" "$source_file" | grep -v "^#" | grep -v "^$" | head -1 | sed 's/^\*\*//;s/\*\*$//')
    fi
    
    # Create frontmatter
    echo "---" > "$dest_file"
    echo "title: $title" >> "$dest_file"
    echo "description: $description" >> "$dest_file"
    echo "---" >> "$dest_file"
    echo "" >> "$dest_file"
    
    # Append content (skip the first title if it matches)
    tail -n +2 "$source_file" >> "$dest_file"
    
    echo "  ✓ Converted: $dest_file"
}

# Convert Company Context files
echo ""
echo "📦 Converting company-context files..."
convert_to_mdx "$COURSE_ROOT/company-context/COMPANY.md" \
    "$PAGES_DIR/company-context/overview.mdx" \
    "TaskFlow Company Overview" \
    "Welcome to TaskFlow - your fictional company throughout the Claude Code PM Course"

convert_to_mdx "$COURSE_ROOT/company-context/PRODUCT.md" \
    "$PAGES_DIR/company-context/product.mdx" \
    "TaskFlow Product Overview" \
    "Your complete guide to the TaskFlow product"

convert_to_mdx "$COURSE_ROOT/company-context/PERSONAS.md" \
    "$PAGES_DIR/company-context/personas.mdx" \
    "TaskFlow User Personas" \
    "Deep dive into who uses TaskFlow and why"

convert_to_mdx "$COURSE_ROOT/company-context/COMPETITIVE.md" \
    "$PAGES_DIR/company-context/competitive.mdx" \
    "TaskFlow Competitive Landscape" \
    "Understanding our market position and competitors"

# Convert Getting Started modules
echo ""
echo "📦 Converting getting-started modules..."
convert_to_mdx "$COURSE_ROOT/lesson-modules/0.0-introduction/REFERENCE_GUIDE.md" \
    "$PAGES_DIR/getting-started/introduction.mdx" \
    "0.0: Introduction to Claude Code for PMs" \
    "Discover how Claude Code transforms PM work - from documentation to data analysis"

convert_to_mdx "$COURSE_ROOT/lesson-modules/0.1-installation/REFERENCE_GUIDE.md" \
    "$PAGES_DIR/getting-started/installation.mdx" \
    "0.1: Installation & Prerequisites" \
    "Get Claude Code installed and verified on your machine in 15 minutes"

convert_to_mdx "$COURSE_ROOT/lesson-modules/0.2-start-and-clone/REFERENCE_GUIDE.md" \
    "$PAGES_DIR/getting-started/start-and-clone.mdx" \
    "0.2: Start Claude Code & Clone the Course" \
    "Have your first real interaction with Claude Code and let it set up your learning environment"

# Convert Fundamentals modules
echo ""
echo "📦 Converting fundamentals modules..."
convert_to_mdx "$COURSE_ROOT/lesson-modules/1.1-welcome/REFERENCE_GUIDE.md" \
    "$PAGES_DIR/fundamentals/welcome.mdx" \
    "1.1: Welcome to TaskFlow" \
    "Introduction to TaskFlow and the course project - your fictional company for hands-on learning"

convert_to_mdx "$COURSE_ROOT/lesson-modules/1.2-visualizing-files/REFERENCE_GUIDE.md" \
    "$PAGES_DIR/fundamentals/visualizing-files.mdx" \
    "1.2: Visualizing Files with Obsidian" \
    "Set up Obsidian to see your files visually alongside Claude Code for a seamless split-screen workflow"

convert_to_mdx "$COURSE_ROOT/lesson-modules/1.3-first-tasks/REFERENCE_GUIDE.md" \
    "$PAGES_DIR/fundamentals/first-tasks.mdx" \
    "1.3: Your First PM Tasks" \
    "Process meeting notes, analyze research, work with images, and create reusable templates"

convert_to_mdx "$COURSE_ROOT/lesson-modules/1.4-agents/REFERENCE_GUIDE.md" \
    "$PAGES_DIR/fundamentals/agents.mdx" \
    "1.4: Agents for Parallel Work" \
    "Clone yourself - run multiple AI agents in parallel to process work 10x faster"

convert_to_mdx "$COURSE_ROOT/lesson-modules/1.5-custom-subagents/REFERENCE_GUIDE.md" \
    "$PAGES_DIR/fundamentals/custom-subagents.mdx" \
    "1.5: Custom Sub-Agents" \
    "Create specialized AI personas for different types of reviews and feedback"

convert_to_mdx "$COURSE_ROOT/lesson-modules/1.6-project-memory/REFERENCE_GUIDE.md" \
    "$PAGES_DIR/fundamentals/project-memory.mdx" \
    "1.6: Project Memory (CLAUDE.md)" \
    "Use CLAUDE.md to give Claude persistent context about your product, team, and preferences"

# Check if 1.7 exists (there are two versions)
if [ -f "$COURSE_ROOT/lesson-modules/1.7-claude-code-navigation/REFERENCE_GUIDE.md" ]; then
    convert_to_mdx "$COURSE_ROOT/lesson-modules/1.7-claude-code-navigation/REFERENCE_GUIDE.md" \
        "$PAGES_DIR/fundamentals/claude-code-navigation.mdx" \
        "1.7: Claude Code Navigation" \
        "Master file operations, searches, and navigation techniques"
elif [ -f "$COURSE_ROOT/lesson-modules/1.7-planning-mode/REFERENCE_GUIDE.md" ]; then
    convert_to_mdx "$COURSE_ROOT/lesson-modules/1.7-planning-mode/REFERENCE_GUIDE.md" \
        "$PAGES_DIR/fundamentals/planning-mode.mdx" \
        "1.7: Planning Mode" \
        "Use planning mode to break down complex tasks before execution"
fi

# Convert Advanced modules
echo ""
echo "📦 Converting advanced modules..."
convert_to_mdx "$COURSE_ROOT/lesson-modules/2.1-write-prd/REFERENCE_GUIDE.md" \
    "$PAGES_DIR/advanced/write-prd.mdx" \
    "2.1: Write a PRD" \
    "Partner with AI to create comprehensive product requirements documents"

convert_to_mdx "$COURSE_ROOT/lesson-modules/2.2-analyze-data/REFERENCE_GUIDE.md" \
    "$PAGES_DIR/advanced/analyze-data.mdx" \
    "2.2: Analyze Data" \
    "Make data-driven product decisions with AI-assisted analysis"

convert_to_mdx "$COURSE_ROOT/lesson-modules/2.3-product-strategy/REFERENCE_GUIDE.md" \
    "$PAGES_DIR/advanced/product-strategy.mdx" \
    "2.3: Product Strategy" \
    "Develop strategic plans and competitive analysis with AI support"

echo ""
echo "✅ Content conversion complete!"
echo "📁 All MDX files created in $PAGES_DIR"

