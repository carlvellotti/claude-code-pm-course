#!/bin/bash
# Creates course material zips for GitHub Release

VERSION=$1

if [ -z "$VERSION" ]; then
  echo "Usage: ./scripts/create-release.sh v1.0.0"
  exit 1
fi

echo "Creating release zip for $VERSION..."

# Create temp directory
mkdir -p releases

# Create complete course zip (includes all modules, company-context, and .claude)
cd course-materials
zip -r ../releases/complete-course.zip . -x "*.DS_Store" -x "__pycache__/*" -x "*.pyc"
cd ..

echo ""
echo "✅ Release zip created:"
ls -lh releases/complete-course.zip

echo ""
echo "Next steps:"
echo "1. Test the zip: unzip -l releases/complete-course.zip"
echo "2. Create GitHub release: gh release create $VERSION releases/complete-course.zip --title \"$VERSION - Course Release\" --notes \"Complete course materials including all modules.\""
