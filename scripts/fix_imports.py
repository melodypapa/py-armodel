#!/usr/bin/env python3
"""Fix malformed import statements in V2 model files."""

import sys
from pathlib import Path

def fix_file(file_path: Path) -> bool:
    """Fix malformed import statements in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        original_lines = lines[:]
        fixed = False
        
        i = 0
        while i < len(lines):
            # Check for pattern: "from ... import (\n"
            if i < len(lines) and lines[i].strip().endswith('import ('):
                # Found opening paren
                import_start_line = i
                
                # Look ahead to find the structure
                j = i + 1
                content_lines = []
                has_nested_import = False
                nested_import_line = -1
                
                while j < len(lines):
                    line = lines[j]
                    
                    # Check if we hit another import statement
                    if line.strip().startswith('from ') or line.strip().startswith('import '):
                        has_nested_import = True
                        nested_import_line = j
                        j += 1
                        # Continue to collect content after the nested import
                        continue
                    
                    # Check for closing paren
                    if line.strip() == ')':
                        break
                    
                    # Collect indented content
                    if line.strip() and not line.strip().startswith('#'):
                        content_lines.append(line)
                    
                    j += 1
                
                # If we found nested import and content, fix it
                if has_nested_import and content_lines and nested_import_line > 0:
                    # Extract the nested import
                    nested_import = lines[nested_import_line]
                    
                    # Remove the malformed block
                    # Replace with: from ... import (\n    content,\n)
                    # And keep the nested import separately
                    
                    # Remove lines from i to j (the entire malformed block)
                    del lines[i:j+1]
                    
                    # Insert the fixed import
                    indent = '    '
                    fixed_import = f"{lines[import_start_line].rstrip()}\n"
                    for content_line in content_lines:
                        fixed_import += content_line
                    fixed_import += f"{indent})\n"
                    
                    # Insert the fixed import and nested import
                    lines.insert(i, fixed_import)
                    lines.insert(i + 1, nested_import)
                    
                    fixed = True
                    i += 1  # Skip ahead to avoid reprocessing
                    continue
            
            i += 1
        
        if fixed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            return True
        
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return False

def main():
    """Main function."""
    v2_dir = Path('/Users/ray/Workspace/py-armodel/worktree/src/armodel/v2/models/M2/AUTOSARTemplates')
    
    if not v2_dir.exists():
        print(f"Directory not found: {v2_dir}")
        return
    
    # Get list of files with syntax errors
    result = subprocess.run(
        ['ruff', 'check', str(v2_dir), '--output-format', 'concise'],
        capture_output=True,
        text=True
    )
    
    # Extract unique file paths
    files_with_errors = set()
    for line in result.stdout.split('\n'):
        if 'invalid-syntax' in line:
            file_path = line.split(':')[0]
            files_with_errors.add(file_path)
    
    print(f"Found {len(files_with_errors)} files with syntax errors")
    
    fixed_count = 0
    for file_path_str in files_with_errors:
        file_path = Path(file_path_str)
        if fix_file(file_path):
            print(f"Fixed: {file_path}")
            fixed_count += 1
    
    print(f"\nTotal files fixed: {fixed_count}")

if __name__ == '__main__':
    import subprocess
    main()
