#!/usr/bin/env python3
"""Fix syntax errors in V2 models where __all__ = [] is misplaced."""

import os
import re
from pathlib import Path

# Find all __init__.py files in models_v2
models_v2_path = Path(__file__).parent.parent / "src" / "armodel" / "models_v2"
init_files = list(models_v2_path.rglob("__init__.py"))

fixed_count = 0
skipped_count = 0

for init_file in init_files:
    try:
        with open(init_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if __all__ = [] is misplaced (not at the end or in the middle of imports)
        # Pattern: __all__ = [] appearing before the end of file
        if '__all__ = []' in content:
            lines = content.split('\n')

            # Find the line with __all__ = []
            all_index = None
            for i, line in enumerate(lines):
                if '__all__ = []' in line and not line.strip().startswith('#'):
                    all_index = i
                    break

            if all_index is not None:
                # Check if this is at the end of the file
                # If there are non-empty, non-comment lines after it, it's misplaced
                has_content_after = False
                for line in lines[all_index + 1:]:
                    stripped = line.strip()
                    if stripped and not stripped.startswith('#') and stripped != '':
                        has_content_after = True
                        break

                if has_content_after:
                    print(f"Fixing: {init_file.relative_to(models_v2_path.parent.parent)}")

                    # Extract all imported class names from import statements
                    imported_classes = set()
                    import_pattern = r'^\s*from\s+\S+\s+import\s*\((.*?)\)'
                    import_end_pattern = r'^\s*\)'

                    in_multiline_import = False
                    for line in lines:
                        stripped = line.strip()
                        if re.match(import_pattern, stripped):
                            in_multiline_import = True
                            # Extract classes from this line
                            match = re.search(r'from\s+\S+\s+import\s*\((.*)', stripped)
                            if match:
                                classes_str = match.group(1)
                                # Remove trailing comment if any
                                if '#' in classes_str:
                                    classes_str = classes_str.split('#')[0]
                                for cls in classes_str.split(','):
                                    cls = cls.strip()
                                    if cls and cls != '':
                                        imported_classes.add(cls)
                        elif in_multiline_import:
                            if stripped == ')':
                                in_multiline_import = False
                            elif stripped and not stripped.startswith('#'):
                                # This is a class name line
                                classes_str = stripped
                                if '#' in classes_str:
                                    classes_str = classes_str.split('#')[0]
                                # Remove trailing comma if any
                                classes_str = classes_str.rstrip(',')
                                for cls in classes_str.split(','):
                                    cls = cls.strip()
                                    if cls and cls != '':
                                        imported_classes.add(cls)

                    # Remove the misplaced __all__ = []
                    new_lines = []
                    for i, line in enumerate(lines):
                        if i == all_index and '__all__ = []' in line:
                            continue
                        new_lines.append(line)

                    # Add proper __all__ at the end
                    if imported_classes:
                        new_lines.append('')
                        new_lines.append('__all__ = [')
                        for cls in sorted(imported_classes):
                            new_lines.append(f'    "{cls}",')
                        new_lines.append(']')
                    else:
                        new_lines.append('')
                        new_lines.append('__all__ = []')

                    new_content = '\n'.join(new_lines)

                    with open(init_file, 'w', encoding='utf-8') as f:
                        f.write(new_content)

                    fixed_count += 1
                else:
                    skipped_count += 1

    except Exception as e:
        print(f"Error processing {init_file}: {e}")

print(f"\nFixed {fixed_count} files")
print(f"Skipped {skipped_count} files (already correct)")