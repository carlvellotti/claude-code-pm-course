#!/usr/bin/env python3
import os
import re
from pathlib import Path

def fix_frontmatter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has frontmatter
    if not content.startswith('---'):
        return False
    
    # Split frontmatter from content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    frontmatter = parts[1].strip()
    body = parts[2]
    
    # Parse frontmatter lines
    lines = frontmatter.split('\n')
    fixed_lines = []
    
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            # Remove existing quotes if present
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            
            # Clean the value - replace newlines and extra spaces
            value = value.replace('\n', ' ').replace('\r', '')
            value = re.sub(r'\s+', ' ', value)
            
            # Quote the value
            fixed_lines.append(f'{key}: "{value}"')
        else:
            fixed_lines.append(line)
    
    # Reconstruct file
    new_content = f"---\n{chr(10).join(fixed_lines)}\n---{body}"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

# Process all MDX files
pages_dir = Path('/Users/carl/claude-code-pm-course/website/pages')
mdx_files = list(pages_dir.rglob('*.mdx'))

print(f"Found {len(mdx_files)} MDX files")
fixed_count = 0

for mdx_file in mdx_files:
    if fix_frontmatter(mdx_file):
        fixed_count += 1
        print(f"✓ Fixed: {mdx_file.relative_to(pages_dir)}")

print(f"\n✅ Fixed {fixed_count} files")

