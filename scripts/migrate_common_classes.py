#!/usr/bin/env python3
"""
Migrate CommonStructure classes to correct files based on class-package.json.
"""

import json
from pathlib import Path

# Load class-package.json
with open('docs/requirements/class-package.json', 'r') as f:
    data = json.load(f)

# Get CommonStructure classes
common_classes = [c for c in data['classes']
                  if 'v2' in c['python_file'] and 'CommonStructure' in c['python_file']]

# Group by target file
target_files = {}
for cls in common_classes:
    target = cls['python_file']
    if target not in target_files:
        target_files[target] = []
    target_files[target].append(cls['name'])

# Build map of class -> current file
v2_dir = Path('src/armodel/v2/models/M2/AUTOSARTemplates/CommonStructure')
current_files = {}
for py_file in v2_dir.rglob('*.py'):
    if '__pycache__' in str(py_file) or py_file.name.startswith('_'):
        continue
    # Extract class name from file name
    class_name = py_file.stem
    current_files[class_name] = py_file

print(f'=== CommonStructure Migration ===')
print(f'Total classes to migrate: {len(common_classes)}')
print(f'Target files: {len(target_files)}')
print()

# Migrate each target file
for target_file in target_files:
    classes_to_migrate = target_files[target_file]
    target_path = Path(target_file)

    print(f'\nMigrating {len(classes_to_migrate)} classes to {target_file}:')

    # Create target directory if needed
    target_path.parent.mkdir(parents=True, exist_ok=True)

    # Collect content from source files
    content_parts = []
    files_to_delete = []

    for class_name in classes_to_migrate:
        source_file = current_files.get(class_name)

        if source_file and source_file.exists():
            with open(source_file, 'r') as f:
                content = f.read()
                # Remove trailing whitespace from last line
                content = content.rstrip()
                content_parts.append(content)
                files_to_delete.append(source_file)
                print(f'  ✓ {class_name} from {source_file.name}')
        else:
            print(f'  ✗ {class_name} - file not found')

    # Write merged content
    if content_parts:
        merged_content = '\n\n'.join(content_parts) + '\n'
        with open(target_path, 'w') as f:
            f.write(merged_content)
        print(f'  → Created {target_path}')

    # Delete old files
    for old_file in files_to_delete:
        if old_file.exists() and old_file != target_path:
            old_file.unlink()
            print(f'  → Deleted {old_file.name}')

print('\n=== Migration Complete ===')