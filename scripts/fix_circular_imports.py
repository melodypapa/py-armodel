#!/usr/bin/env python3
"""Fix circular imports in V2 models by using lazy imports."""

import re
from pathlib import Path

# Fix InternalBehavior.py to use lazy imports
internal_behavior_path = Path(__file__).parent.parent / "src" / "armodel" / "models_v2" / "M2" / "AUTOSARTemplates" / "CommonStructure" / "InternalBehavior.py"

with open(internal_behavior_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the import statement
old_import = """from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    ParameterDataPrototype,
    VariableDataPrototype,
)"""

new_import = """# Lazy imports to avoid circular dependency
# from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
#     ParameterDataPrototype,
#     VariableDataPrototype,
# )"""

content = content.replace(old_import, new_import)

# Add lazy import helper function at the top of the file (after imports)
lazy_import_helper = '''
def _get_data_prototype_classes():
    """Lazy import to avoid circular dependency."""
    from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
        ParameterDataPrototype,
        VariableDataPrototype,
    )
    return ParameterDataPrototype, VariableDataPrototype
'''

# Find where to insert the helper function (after the last import statement)
import_end_pattern = r'([^\n]*import [^\n]+\n)+'
match = re.search(import_end_pattern, content)

if match:
    last_import_end = match.end()
    content = content[:last_import_end] + lazy_import_helper + content[last_import_end:]

# Replace all occurrences of ParameterDataPrototype and VariableDataPrototype
# with function calls that get them lazily

# First, let's find all methods that use these classes
# Pattern: def createConstantMemory(..., ) -> ParameterDataPrototype:
# We need to replace the return type annotation

# Replace return type annotations
content = re.sub(
    r'\) -> ParameterDataPrototype:',
    ') -> "_ParameterDataPrototype":',
    content
)
content = re.sub(
    r'\) -> VariableDataPrototype:',
    ') -> "_VariableDataPrototype":',
    content
)

# Replace List[ParameterDataPrototype] with list type hints
content = re.sub(
    r': List\[ParameterDataPrototype\]',
    ': List["_ParameterDataPrototype"]',
    content
)
content = re.sub(
    r': List\[VariableDataPrototype\]',
    ': List["_VariableDataPrototype"]',
    content
)

# Replace class usage in methods with lazy loading
# Pattern: prototype = ParameterDataPrototype(self, short_name)
content = re.sub(
    r'prototype = ParameterDataPrototype\(self, short_name\)',
    '''ParameterDataPrototype, _ = _get_data_prototype_classes()
        prototype = ParameterDataPrototype(self, short_name)''',
    content
)

# Write back
with open(internal_behavior_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed circular imports in {internal_behavior_path.relative_to(internal_behavior_path.parent.parent.parent.parent.parent)}")
