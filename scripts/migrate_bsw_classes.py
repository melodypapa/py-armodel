#!/usr/bin/env python3
"""
Migrate BswModuleTemplate classes to correct files.
"""

import json
from pathlib import Path
from collections import defaultdict


def load_class_package_json():
    """Load class-package.json file."""
    with open('docs/requirements/class-package.json', 'r') as f:
        data = json.load(f)
    return data['classes']


def group_classes_by_target(classes_data):
    """Group classes by their target file."""
    groups = defaultdict(list)
    for cls in classes_data:
        if 'BswModuleTemplate' in cls['package_path']:
            groups[cls['python_file']].append(cls)
    return dict(groups)


def migrate_bswmoduletemplate():
    """Main migration function."""
    print("=" * 80)
    print("Migrating BswModuleTemplate Classes")
    print("=" * 80)

    # Load class package data
    print("\n[1/4] Loading class-package.json...")
    classes_data = load_class_package_json()
    
    # Group by target file
    print("[2/4] Grouping classes by target file...")
    target_groups = group_classes_by_target(classes_data)
    
    # Process each target file
    print("[3/4] Migrating classes...")
    
    project_root = Path('/Users/ray/Workspace/py-armodel')
    
    for target_file_rel, classes in target_groups.items():
        target_file = project_root / target_file_rel
        
        # Skip if target already exists
        if target_file.exists():
            print(f"  Skipping {target_file.name} (already exists)")
            continue
        
        # Read all source files and concatenate content
        all_content = []
        all_classes = []
        
        for cls in classes:
            class_name = cls['name']
            
            # Find source file
            source_file = None
            for py_file in (project_root / 'src/armodel/v2/models/M2/AUTOSARTemplates/BswModuleTemplate').rglob('*.py'):
                if '__pycache__' in str(py_file):
                    continue
                if py_file.name == class_name + '.py':
                    source_file = py_file
                    break
            
            if source_file:
                print(f"  Processing {class_name}...")
                try:
                    with open(source_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        all_content.append(content)
                        all_classes.append(class_name)
                        print(f"    ✓ Read from {source_file.name}")
                except Exception as e:
                    print(f"    ✗ Error reading {source_file.name}: {e}")
        
        # Write merged file
        if all_content:
            print(f"\n  Creating {target_file.name} with {len(all_classes)} classes...")
            target_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Simple concatenation with separators
            merged_content = '\n\n'.join(all_content)
            
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(merged_content)
            
            print(f"  ✓ Created {target_file.name}")
    
    # Delete old single-class files
    print("\n[4/4] Cleaning up old files...")
    
    classes_moved = []
    for target_file_rel, classes in target_groups.items():
        for cls in classes:
            classes_moved.append(cls['name'])
    
    deleted_count = 0
    for class_name in classes_moved:
        source_file = project_root / 'src/armodel/v2/models/M2/AUTOSARTemplates/BswModuleTemplate' / (class_name + '.py')
        if source_file.exists() and source_file != project_root / target_file_rel:
            try:
                source_file.unlink()
                deleted_count += 1
                print(f"  ✓ Deleted {source_file.name}")
            except Exception as e:
                print(f"  ✗ Could not delete {source_file.name}: {e}")
    
    print("\n" + "=" * 80)
    print(f"Migration complete! Deleted {deleted_count} old files")
    print("=" * 80)


if __name__ == "__main__":
    migrate_bswmoduletemplate()