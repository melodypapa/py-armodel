#!/usr/bin/env python3
"""
Add __all__ to __init__.py files that are missing it.
"""

import re
from pathlib import Path


def add_all_to_init(init_file: Path) -> bool:
    """Add __all__ declaration to __init__.py file."""
    with open(init_file, 'r') as f:
        content = f.read()

    if "__all__" in content:
        return False

    lines = content.split('\n')

    # Find all imported names (from ... import Name, Name2)
    imported_names = set()
    for line in lines:
        match = re.match(r'from \S+ import\s+\((.+)\)', line)
        if match:
            names_str = match.group(1)
            # Extract names from multi-line import
            names = [name.strip().strip(',') for name in names_str.split('\n') if name.strip() and not name.strip().startswith('#')]
            for name in names:
                # Get the actual identifier
                if ' as ' in name:
                    name = name.split(' as ')[1].strip()
                imported_names.add(name.strip())

    if not imported_names:
        # No explicit imports, add minimal __all__
        all_line = "\n__all__ = []\n"
    else:
        # Create __all__ with imported names
        names_list = ', '.join(f'"{name}"' for name in sorted(imported_names))
        all_line = f"\n__all__ = [{names_list}]\n"

    # Insert after last import
    last_import_idx = -1
    for i, line in enumerate(lines):
        if line.strip().startswith('from ') or line.strip().startswith('import '):
            last_import_idx = i

    if last_import_idx >= 0:
        # Insert after imports, skip blank lines
        insert_idx = last_import_idx + 1
        while insert_idx < len(lines) and not lines[insert_idx].strip():
            insert_idx += 1

        lines.insert(insert_idx, all_line)

        with open(init_file, 'w') as f:
            f.write('\n'.join(lines))

        print(f"✅ Added __all__ to {init_file} ({len(imported_names)} imports)")
        return True
    else:
        # No imports found, just append
        lines.append(all_line)
        with open(init_file, 'w') as f:
            f.write('\n'.join(lines))

        print(f"✅ Added __all__ to {init_file} (empty)")
        return True


def main():
    """Main function."""
    init_files = [
        "src/armodel/models_v2/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication/__init__.py",
        "src/armodel/models_v2/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/__init__.py",
        "src/armodel/models_v2/M2/AUTOSARTemplates/SystemTemplate/Transformer/__init__.py",
        "src/armodel/models_v2/M2/AUTOSARTemplates/SystemTemplate/__init__.py",
        "src/armodel/models_v2/M2/AUTOSARTemplates/GenericStructure/VariantHandling/AttributeValueVariationPoints/__init__.py",
        "src/armodel/models_v2/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py",
        "src/armodel/models_v2/M2/AUTOSARTemplates/GenericStructure/DocumentationOnM1/__init__.py",
        "src/armodel/models_v2/M2/AUTOSARTemplates/BswModuleTemplate/BswOverview/__init__.py",
        "src/armodel/models_v2/M2/AUTOSARTemplates/DiagnosticExtract/__init__.py",
        "src/armodel/models_v2/M2/AUTOSARTemplates/AutosarTopLevelStructure/__init__.py",
        "src/armodel/models_v2/M2/AUTOSARTemplates/ECUCParameterDefTemplate/__init__.py",
        "src/armodel/models_v2/M2/AUTOSARTemplates/ECUCDescriptionTemplate/__init__.py",
        "src/armodel/models_v2/M2/AUTOSARTemplates/CommonStructure/__init__.py",
        "src/armodel/models_v2/M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py",
    ]

    print("Adding __all__ to __init__.py files...")
    print()

    fixed_count = 0
    for init_file_str in init_files:
        init_file = Path(init_file_str)
        if add_all_to_init(init_file):
            fixed_count += 1

    print()
    print(f"✅ Added __all__ to {fixed_count} files")

    return 0


if __name__ == "__main__":
    exit(main())
