# fix-package-implementation.py

## Overview

The `fix-package-implementation.py` script is a powerful tool for generating missing AUTOSAR M2 package implementations in the py-armodel project. It automatically creates Python class files based on JSON requirements, along with corresponding test cases, and validates the generated code.

## Purpose

This script addresses the gap between documented AUTOSAR M2 model requirements and actual Python implementation by:

1. **Generating Missing Classes**: Automatically creates Python class files for classes documented in the requirements but not yet implemented
2. **Creating Test Cases**: Generates pytest test files for all generated classes
3. **Validating Code**: Performs syntax validation and ruff linting on generated code
4. **Handling Dependencies**: Recursively creates missing parent classes and type dependencies
5. **Line Length Enforcement**: Ensures all generated docstrings and comments stay under 80 characters

## Usage

### Basic Usage

```bash
# Generate missing classes for a specific package
python scripts/fix-package-implementation.py M2::AUTOSARTemplates::AbstractPlatform

# Preview changes without modifying files (dry-run)
python scripts/fix-package-implementation.py M2::AUTOSARTemplates::AbstractPlatform --dry-run

# Merge generated code into existing classes (preserves manual changes)
python scripts/fix-package-implementation.py M2::AUTOSARTemplates::AbstractPlatform --merge
```

### Command Line Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `package` | string | Yes | Specific package to fix (format: M2::xxx::xxxx) |
| `--dry-run` | flag | No | Preview fixes without modifying files |
| `--merge` | flag | No | Merge generated code into existing classes |

### Package Path Format

Package paths use the format `M2::AUTOSARTemplates::<Category>::<Subcategory>...`:

- `M2::AUTOSARTemplates::AbstractPlatform` - Top-level package
- `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior` - Subpackage
- `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface` - Specific component

### Package Structure Rules

The script follows AUTOSAR M2 package structure rules defined in the requirements:

1. **Leaf Packages** (no subpackages):
   - Implemented as a single `.py` file
   - Example: `BswModuleTemplate/BswBehavior.py` contains all classes for BswBehavior package
   - Import path: `from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import ClassName`

2. **Non-Leaf Packages** (have subpackages):
   - Implemented as a directory with `__init__.py`
   - Example: `BswModuleTemplate/BswOverview/` contains multiple class files and subdirectories
   - Import path: `from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import ClassName`

The script automatically checks the requirements JSON to determine which structure each package should have:

- Reads the `subpackages` field in package JSON files
- If `subpackages` is non-empty → creates directory structure
- If `subpackages` is empty → creates single `.py` file

### Hybrid Structure Handling

The script detects and reports **hybrid structures** (where both a `.py` file and a directory with the same name exist):

```
BswBehavior.py          ← Single file
BswBehavior/            ← Directory (conflict!)
  ├── __init__.py
  ├── Class1.py
  └── Class2.py
```

The script will:
1. Check requirements to determine the correct structure
2. Report an error if the actual structure doesn't match requirements
3. Provide guidance on how to fix the mismatch

**Example Error Message:**
```
✗ Error: Package 'M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior'
   should be a directory (has subpackages) but is implemented as a single file: BswBehavior.py

Expected structure: BswBehavior/ (directory with __init__.py)
Current structure: BswBehavior.py (single file)

To fix this, please migrate to package structure:
  1. Create directory: BswBehavior/
  2. Move classes from BswBehavior.py to individual files in BswBehavior/
  3. Create BswBehavior/__init__.py with imports
  4. Remove BswBehavior.py
```

## Features

### 1. Class Generation

The script generates complete Python class implementations including:

- **Class Definition**: Proper inheritance from parent classes
- **Constructor**: `__init__` method with correct signature
- **Attributes**: All attributes with proper typing
- **Getters/Setters**: Getter and setter methods for each attribute
- **Add Methods**: `addXxxx()` methods for list-type attributes
- **Docstrings**: Comprehensive class and method documentation

#### Example Generated Class

```python
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    PortInterface,
)
from typing import List

class ApplicationInterface(PortInterface):
    """
    This represents the ability to define a PortInterface that consists of a
    composition of commands (method calls), indications (events) and attributes
    (fields) Tags: atp.Status=draft atp.recommendedPackage=Interfaces

    Sources:
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 28, Foundation
      R23-11)
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the set of attributes defined in the context Abstract
        # Platform ApplicationInterface.
        # atpVariation.
        self.attributes: List[Field] = []

    def getAttributes(self) -> List[Field]:
        return self.attributes

    def setAttributes(self, value: List[Field]) -> "ApplicationInterface":
        self.attributes = value
        return self

    def addAttributes(self, value: Field) -> "ApplicationInterface":
        """Adds a value to the attributes list."""
        self.attributes.append(value)
        return self
```

### 2. Test Case Generation

For each generated class, the script creates a comprehensive test file:

```python
"""
Auto-generated test cases for ApplicationInterface.
Generated by fix-package-implementation.py.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.AbstractPlatform.ApplicationInterface import ApplicationInterface
from armodel import AUTOSAR

class TestApplicationInterface:
    """Test cases for ApplicationInterface class."""

    def test_initialization(self):
        """Test initialization of ApplicationInterface with proper attributes."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        obj = ApplicationInterface(ar_root, "test_applicationinterface")
        assert obj.short_name == "test_applicationinterface"

    def test_get_attribute(self):
        """Test getting attribute list."""
        # ... test implementation
```

### 3. Dependency Resolution

The script automatically handles:

- **Parent Classes**: Creates missing parent classes recursively
- **Type Imports**: Generates correct import statements for attribute types
- **Reference Types**: Uses `RefType` for reference attributes instead of concrete types
- **Self-References**: Handles classes with attributes of their own type
- **Constructor Signatures**: Determines correct `__init__` signature based on parent class

#### Constructor Signature Detection

The script maintains a list `_PARENTS_WITH_INIT_ARGS` of classes that have `__init__(parent, short_name)` signature. Classes whose parent is in this list will have:

```python
def __init__(self, parent: ARObject, short_name: str):
    super().__init__(parent, short_name)
```

Otherwise, they will have:

```python
def __init__(self):
    super().__init__()
```

The list includes:

**Referrable Hierarchy:**
- `Referrable` - Base class that introduces `short_name`
- `MultilanguageReferrable` - Inherits from Referrable
- `Identifiable` - Inherits from MultilanguageReferrable
- `ARElement` - Inherits from PackageableElement → Identifiable
- `PackageableElement` - Inherits from Identifiable

**ATP Blueprintable Hierarchy:**
- `AtpBlueprintable` - Inherits from Identifiable
- `AtpClassifier` - Inherits from Identifiable
- `AtpType` - Inherits from AtpClassifier
- `AtpPrototype` - Inherits from AtpBlueprintable
- `AtpStructureElement` - Inherits from AtpBlueprintable
- `AtpFeature` - Inherits from Identifiable

**Other Classes with short_name:**
- `CollectableElement` - Has `short_name` but doesn't inherit from Referrable
- `ElementCollection` - Has `short_name` but doesn't inherit from Referrable
- `ARPackage` - Has `short_name` but doesn't inherit from Referrable
- Various component, behavior, and data type classes

### 4. Code Quality Features

#### Line Length Enforcement (80 Characters)

The script ensures all generated content stays under 80 characters:

- **Class Docstrings**: Wrapped at 80 characters
- **Attribute Comments**: Multi-line comments properly wrapped
- **Source References**: Long source references split across lines

#### Example of Wrapped Content

```python
"""
This represents the ability to define a PortInterface that consists of a
composition of commands (method calls), indications (events) and attributes
(fields) Tags: atp.Status=draft atp.recommendedPackage=Interfaces

Sources:
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 28, Foundation
  R23-11)
"""
```

### 5. Validation and Linting

The script performs automatic validation:

- **Syntax Check**: Validates generated code with Python AST parser
- **Ruff Check**: Runs ruff linter to ensure code quality
- **Import Validation**: Ensures all imports are valid and non-circular
- **Type Checking**: Validates type annotations are correct

## Architecture

### Key Components

#### 1. Requirements Loading

- `load_requirements_index()`: Loads the main requirements index
- `load_package_json()`: Loads individual package JSON files
- `get_all_packages()`: Recursively processes package hierarchy

#### 2. Type Resolution

- `build_type_index()`: Builds a global index of all types in codebase
- `find_type_in_codebase_cached()`: Fast type lookup using cache
- `_generate_import_path()`: Generates correct import paths considering wildcard exports

#### 3. Package Structure Determination

- `get_package_has_subpackages()`: Checks requirements JSON to determine if a package has subpackages
- Package structure logic:
  - **Leaf packages** (no subpackages): Single `.py` file
  - **Non-leaf packages** (has subpackages): Directory with `__init__.py`
- Hybrid structure detection and reporting

The script reads the `subpackages` field from package JSON files to determine the correct structure:
```json
{
  "name": "M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior",
  "subpackages": []  // Empty → leaf package → single .py file
}

{
  "name": "M2::AUTOSARTemplates::BswModuleTemplate::BswOverview",
  "subpackages": [  // Non-empty → non-leaf package → directory
    {
      "name": "InstanceRefs",
      ...
    }
  ]
}
```

#### 4. Code Generation

- `generate_class_code()`: Main function for generating class code
- `generate_imports()`: Generates import statements
- `_wrap_docstring_line()`: Wraps long lines to 80 characters
- `_format_attr_comment()`: Formats attribute comments with proper wrapping

#### 4. Validation

- `validate_code()`: Validates generated code syntax
- `format_code_with_ruff()`: Formats code with ruff formatter

### Global State

The script maintains several global caches:

- `_type_index_cache`: Maps class names to import paths
- `created_classes`: Tracks classes created during execution
- `generation_report`: Tracks errors, warnings, and unresolved types

### Parent Class Signatures

The script maintains a list `_PARENTS_WITH_INIT_ARGS` of classes that have `__init__(parent, short_name)` signature, ensuring correct constructor generation for inherited classes.

## Requirements Data Structure

The script expects JSON requirements in `docs/requirements/packages/` with the following structure:

```json
{
  "package": "M2::AUTOSARTemplates::AbstractPlatform",
  "classes": [
    {
      "name": "ApplicationInterface",
      "is_abstract": false,
      "parent": "PortInterface",
      "note": "Class description",
      "sources": [
        {
          "pdf_file": "AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf",
          "page_number": 28,
          "autosar_standard": "Foundation",
          "standard_release": "R23-11"
        }
      ],
      "attributes": {
        "attribute": {
          "type": "Field",
          "multiplicity": "*",
          "kind": "attribute",
          "is_ref": false,
          "note": "Attribute description"
        }
      }
    }
  ]
}
```

### Attribute Multiplicity

| Value | Python Type | Description |
|-------|-------------|-------------|
| `1` | `type` | Single required value |
| `0..1` | `Optional[type]` | Optional value |
| `*` | `List[type]` | List of values |

### Reference Attributes

When `is_ref: true`, the script:
- Uses `RefType` instead of the actual type
- Skips importing the actual type (to avoid unused imports)
- Maintains reference semantics in the generated code

## Output Structure

### Generated Files

For a package `M2::AUTOSARTemplates::AbstractPlatform` with class `ApplicationInterface`:

```
src/armodel/models/M2/AUTOSARTemplates/AbstractPlatform/
├── __init__.py                      # Updated with import statement
└── ApplicationInterface.py           # Generated class file

tests/test_armodel/models/M2/AUTOSARTemplates/AbstractPlatform/
├── __init__.py                      # Created if needed
└── test_ApplicationInterface.py     # Generated test file
```

### File Updates

- `__init__.py`: Automatically updated with `from .<ClassName> import <ClassName>`
- Test directory structure mirrors source structure
- All files follow py-armodel naming conventions

## Error Handling

### Common Issues and Solutions

#### 1. Syntax Error in Generated Code

**Error**: `Syntax error at line N: unexpected indent`

**Cause**: Incorrect comment wrapping or indentation

**Solution**: The script now properly wraps comments to 80 characters. If you see this error, check the `_format_attr_comment()` function.

#### 2. Unused Import Warning

**Error**: `F401 <type> imported but unused`

**Cause**: Reference attribute types being imported but replaced with `RefType`

**Solution**: The script now skips importing types when `is_ref: true`

#### 3. Missing Parent Class

**Error**: `Parent class '<name>' not found in codebase or JSON`

**Cause**: Parent class not yet implemented

**Solution**: The script attempts to create missing parent classes recursively

#### 4. Circular Import

**Error**: Import creates circular dependency

**Cause**: Self-referencing types or complex inheritance

**Solution**: The script uses string type annotations (`"ClassName"`) for forward references

### Generation Report

The script tracks and reports:

- **Unresolved Types**: Types that couldn't be found or created
- **Warnings**: Non-critical issues during generation
- **Errors**: Critical errors that prevented generation

Example output:
```
Generation Report:
❌ Errors:
  - ApplicationInterface: Syntax error at line 23: unexpected indent

⚠️ Warnings:
  - MissingType: Type 'SomeType' not found, using Any

ℹ️  Unresolved Types:
  - ApplicationInterface:
    - UnknownType (attribute some_attr)
```

## Best Practices

### 1. Use Dry-Run First

Always use `--dry-run` to preview changes:

```bash
python scripts/fix-package-implementation.py M2::Package --dry-run
```

### 2. Check Generated Code

After generation, review the generated files:

```bash
# Run ruff check
python3 -m ruff check src/armodel/models/M2/AUTOSARTemplates/Package/

# Run tests
python3 -m pytest tests/test_armodel/models/M2/AUTOSARTemplates/Package/
```

### 3. Handle Merge Conflicts

Use `--merge` flag when updating existing classes:

```bash
python scripts/fix-package-implementation.py M2::Package --merge
```

This preserves manual changes while adding generated code.

### 4. Incremental Updates

Work on specific subpackages rather than entire hierarchies:

```bash
# Good: Specific subpackage
python scripts/fix-package-implementation.py M2::Package::SubPackage

# Avoid: Very broad package
python scripts/fix-package-implementation.py M2::AUTOSARTemplates
```

## Integration with Other Scripts

### compare-package-implementation.py

Use this script first to identify what's missing:

```bash
# Find missing classes
python scripts/compare-package-implementation.py --package M2::Package

# Then fix them
python scripts/fix-package-implementation.py M2::Package
```

### deviation-package.py

After generating classes, verify they're in the correct location:

```bash
python scripts/deviation-package.py

# Review deviation_package.md for any path issues
```

### run_tests.py

After generation, verify tests pass:

```bash
python scripts/run_tests.py --unit
python scripts/run_tests.py --coverage
```

## Limitations

### 1. Single-File Packages

The script cannot create classes in packages implemented as single `.py` files (non-directory packages). These require manual implementation.

### 2. Complex Inheritance

Classes with complex multiple inheritance or mixins may require manual adjustment.

### 3. Method Implementation

Only getter, setter, and add methods are generated. Complex methods need manual implementation.

### 4. Enumerations

The script doesn't generate enumerations. These must be created manually.

## Troubleshooting

### Issue: Class Already Exists

**Symptom**: Script reports "No missing classes found" but class is incomplete

**Solution**: Use `--merge` flag to update existing class:
```bash
python scripts/fix-package-implementation.py M2::Package --merge
```

### Issue: Import Errors in Tests

**Symptom**: Tests fail with `ModuleNotFoundError`

**Cause**: Missing dependencies or incorrect import paths

**Solution**:
1. Check if all dependencies are implemented
2. Verify `__init__.py` files have correct imports
3. Run the script again to generate missing dependencies

### Issue: Ruff Format Differences

**Symptom**: Ruff reports formatting issues after generation

**Cause**: Different ruff version or configuration

**Solution**: The script runs `ruff format` automatically after generation. Ensure ruff is up to date:
```bash
pip install --upgrade ruff
```

## Future Enhancements

Potential improvements:

1. **Enumeration Generation**: Auto-generate enum classes
2. **Method Documentation**: Generate detailed docstrings for all methods
3. **Property Support**: Add `@property` decorators for attribute access
4. **Type Validation**: Add runtime type checking
5. **Documentation Integration**: Auto-generate API documentation
6. **Batch Processing**: Process multiple packages in one run

## Related Documentation

- [compare-package-implementation.md](compare-package-implementation.md) - Package comparison tool
- [deviation-package.md](deviation-package.md) - Package structure validation
- [run_tests.md](run_tests.md) - Test execution guide
- [AGENTS.md](../AGENTS.md) - Development guidelines and conventions

## Version History

- **1.0.0**: Initial implementation
- **1.1.0**: Added line length enforcement (80 characters)
- **1.2.0**: Improved attribute comment wrapping
- **1.3.0**: Fixed unused import warnings for reference attributes

## Contributing

When modifying this script:

1. **Preserve line length limit**: Keep all generated output under 80 characters
2. **Update tests**: Ensure generated code passes ruff and pytest
3. **Document changes**: Update this document for new features
4. **Test thoroughly**: Use `--dry-run` and review output before changes