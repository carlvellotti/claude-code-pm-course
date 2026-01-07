#!/usr/bin/env python3
import os
import re
from pathlib import Path

def fix_frontmatter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查文件是否有 frontmatter
    if not content.startswith('---'):
        return False
    
    # 将 frontmatter 与内容分离
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    frontmatter = parts[1].strip()
    body = parts[2]
    
    # 解析 frontmatter 行
    lines = frontmatter.split('\n')
    fixed_lines = []
    
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            # 如果存在现有引号，则将其移除
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            
            # 清理值 - 替换换行符和多余的空格
            value = value.replace('\n', ' ').replace('\r', '')
            value = re.sub(r'\s+', ' ', value)
            
            # 给值加上引号
            fixed_lines.append(f'{key}: "{value}"')
        else:
            fixed_lines.append(line)
    
    # 重构文件
    new_content = f"---\n{chr(10).join(fixed_lines)}\n---{body}"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

# 处理所有 MDX 文件
pages_dir = Path('/Users/carl/claude-code-pm-course/website/pages')
mdx_files = list(pages_dir.rglob('*.mdx'))

print(f"找到 {len(mdx_files)} 个 MDX 文件")
fixed_count = 0

for mdx_file in mdx_files:
    if fix_frontmatter(mdx_file):
        fixed_count += 1
        print(f"✓ 已修复: {mdx_file.relative_to(pages_dir)}")

print(f"\n✅ 已修复 {fixed_count} 个文件")

