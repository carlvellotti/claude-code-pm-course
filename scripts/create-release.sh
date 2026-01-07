#!/bin/bash
# 为 GitHub Release 创建课程资料 zip 包

VERSION=$1

if [ -z "$VERSION" ]; then
  echo "用法：./scripts/create-release.sh v1.0.0"
  exit 1
fi

echo "正在为 $VERSION 创建发布 zip 包..."

# 创建 releases 目录并删除任何现有的 zip 包
mkdir -p releases
rm -f releases/complete-course.zip

# 创建完整的课程 zip 包（包括所有模块、company-context 和 .claude）
cd course-materials
zip -r ../releases/complete-course.zip . -x "*.DS_Store" -x "__pycache__/*" -x "*.pyc" -x ".venv/*" -x ".env" -x ".env.local"
cd ..

echo ""
echo "✅ 发布 zip 包已创建："
ls -lh releases/complete-course.zip

echo ""
echo "下一步："
echo "1. 测试 zip 包：unzip -l releases/complete-course.zip"
echo "2. 创建 GitHub release：gh release create $VERSION releases/complete-course.zip --title \"$VERSION - Course Release\" --notes \"Complete course materials including all modules.\""
