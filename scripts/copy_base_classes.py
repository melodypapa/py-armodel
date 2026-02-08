#!/usr/bin/env python3
"""
Script to copy critical base classes from V1 to V2.
These classes are prerequisites for completing the remaining migrations.
"""

import re
from pathlib import Path

# Critical base classes to copy
BASE_CLASSES = [
    {
        'source': 'src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py',
        'target': 'src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py',
        'classes': ['ARObject']
    },
    {
        'source': 'src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py',
        'target': 'src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py',
        'classes': ['Referrable', 'MultilanguageReferrable', 'Identifiable', 'PackageableElement', 'ARElement', 'Describable']
    },
    {
        'source': 'src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ARPackage.py',
        'target': 'src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ARPackage.py',
        'classes': ['ReferenceBase']
    },
]


def convert_v1_to_v2(source_content: str) -> str:
    """
    Convert V1 class to V2 style.
    - Remove parent parameter from __init__
    - Convert property methods to Pythonic properties
    - Simplify initialization
    """
    lines = source_content.split('\n')
    converted_lines = []
    
    for line in lines:
        # Remove V1-specific patterns
        if 'self.short_name = short_name' in line or 'parent:' in line:
            continue
        if 'def get' in line and '(' in line and ')' in line and '->' not in line:
            # Skip old getter methods
            continue
        if 'self.' in line and '= []' in line:
            # Keep initialization
            converted_lines.append(line)
        elif line.strip() and not line.strip().startswith('#'):
            converted_lines.append(line)
    
    return '\n'.join(converted_lines)


def extract_class_from_source(source_file: str, class_name: str) -> str:
    """Extract a single class definition from source file."""
    with open(source_file, 'r') as f:
        content = f.read()
    
    # Find class definition
    class_pattern = rf'class {class_name}\([^)]+\):.*?(?=\nclass |\Z)'
    match = re.search(class_pattern, content, re.DOTALL)
    
    if match:
        return match.group(0)
    return ""


def main():
    """Copy base classes from V1 to V2."""
    print("=== Copying Critical Base Classes from V1 to V2 ===\n")
    
    for base_class in BASE_CLASSES:
        source_file = base_class['source']
        target_file = base_class['target']
        classes = base_class['classes']
        
        print(f"Processing {Path(target_file).name}:")
        
        # Create target directory
        Path(target_file).parent.mkdir(parents=True, exist_ok=True)
        
        # Extract and combine classes
        all_classes = []
        for class_name in classes:
            class_def = extract_class_from_source(source_file, class_name)
            if class_def:
                all_classes.append(class_def)
                print(f"  ✓ Found {class_name}")
            else:
                print(f"  ✗ Not found: {class_name}")
        
        if all_classes:
            # Write to target file
            with open(target_file, 'w') as f:
                f.write('\'\'\'')
                f.write(f'V2 base classes copied from {Path(source_file).name}')
                f.write('\'\'\'\n\n')
                
                # Add imports
                f.write('from abc import ABC\n')
                f.write('from typing import Optional\n\n')
                
                # Add classes
                for class_def in all_classes:
                    f.write('\n')
                    f.write(class_def)
                    f.write('\n')
            
            print(f"  → Created {target_file}")
        print()


if __name__ == '__main__':
    main()