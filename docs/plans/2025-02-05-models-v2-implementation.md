# Models V2 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Refactor py-armodel models to V2 with clean imports (absolute imports, no TYPE_CHECKING, explicit __all__) while maintaining 100% V1 API compatibility.

**Architecture:** Parallel V1/V2 development where V1 models remain frozen and V2 models become the new standard with cleaner import architecture following PEP 8 and Python best practices.

**Tech Stack:** Python 3.10+, pytest, ruff, git worktrees

---

## Prerequisites

Before starting, ensure you have:
- Read the design document: `docs/plans/2025-02-05-models-v2-design.md`
- Read V2 coding rules in `docs/development/coding_rules.md` (CODING_RULE_V2_00001-00010)
- Created a git worktree for isolated development (recommended)

---

## Task 1: Create V2 Directory Structure

**Files:**
- Create: `src/armodel/models_v2/`
- Create: `src/armodel/models_v2/M2/`
- Create: `src/armodel/models_v2/M2/MSR/`
- Create: `src/armodel/models_v2/M2/AUTOSARTemplates/`
- Create: `src/armodel/models_v2/base/`

**Step 1: Create base V2 directories**

Run:
```bash
mkdir -p src/armodel/models_v2/M2/MSR
mkdir -p src/armodel/models_v2/M2/AUTOSARTemplates
mkdir -p src/armodel/models_v2/base
```

Expected: Directories created successfully

**Step 2: Copy V1 models to V2**

Run:
```bash
cp -r src/armodel/models/M2/* src/armodel/models_v2/M2/
cp -r src/armodel/models/base/* src/armodel/models_v2/base/
```

Expected: All V1 model files copied to V2

**Step 3: Verify V2 structure**

Run:
```bash
ls -la src/armodel/models_v2/M2/
ls -la src/armodel/models_v2/base/
```

Expected: V2 directories contain copies of V1 files

**Step 4: Commit initial V2 structure**

Run:
```bash
git add src/armodel/models_v2/
git commit -m "feat(v2): Create initial V2 directory structure

- Copy V1 models to models_v2
- Establish parallel V1/V2 development
- V1 models remain frozen in src/armodel/models/
- V2 models ready for refactoring

Ref: docs/plans/2025-02-05-models-v2-design.md"
```

---

## Task 2: Create V2 Automation Scripts

**Files:**
- Create: `scripts/create_v2_structure.py`
- Create: `scripts/refactor_v2_imports.py`
- Create: `scripts/validate_v2.py`

**Step 1: Write create_v2_structure.py script**

Create file: `scripts/create_v2_structure.py`

```python
"""Create models_v2 directory structure by copying models."""

import shutil
from pathlib import Path


def create_v2_structure():
    """Create V2 directory structure."""
    src = Path("src/armodel")
    models = src / "models"
    models_v2 = src / "models_v2"

    if models_v2.exists():
        print(f"WARNING: {models_v2} already exists")
        response = input("Delete and recreate? (y/N): ")
        if response.lower() == "y":
            shutil.rmtree(models_v2)
        else:
            print("Aborted")
            return

    print(f"Copying {models} -> {models_v2}")
    shutil.copytree(models, models_v2)

    print(f"✓ Created {models_v2}")
    print("Next: Run scripts/refactor_v2_imports.py")


if __name__ == "__main__":
    create_v2_structure()
```

**Step 2: Write validate_v2.py script**

Create file: `scripts/validate_v2.py`

```python
"""Validate V2 structure and coding rules."""

import sys
from pathlib import Path


def validate_v2():
    """Validate V2 structure."""
    models_v2 = Path("src/armodel/models_v2")

    if not models_v2.exists():
        print("✗ models_v2 does not exist")
        return 1

    # Check for TYPE_CHECKING
    type_checking_files = []
    for py_file in models_v2.rglob("*.py"):
        if "TYPE_CHECKING" in py_file.read_text():
            type_checking_files.append(py_file)

    if type_checking_files:
        print(f"✗ Found TYPE_CHECKING in {len(type_checking_files)} files:")
        for f in type_checking_files:
            print(f"  - {f}")
        return 1

    # Check for relative imports
    relative_import_files = []
    for py_file in models_v2.rglob("*.py"):
        content = py_file.read_text()
        if "from ." in content:
            relative_import_files.append(py_file)

    if relative_import_files:
        print(f"✗ Found relative imports in {len(relative_import_files)} files:")
        for f in relative_import_files:
            print(f"  - {f}")
        return 1

    print("✓ V2 validation passed!")
    return 0


if __name__ == "__main__":
    sys.exit(validate_v2())
```

**Step 3: Make scripts executable**

Run:
```bash
chmod +x scripts/create_v2_structure.py
chmod +x scripts/validate_v2.py
```

Expected: Scripts now executable

**Step 4: Test validate_v2.py script**

Run:
```python
python scripts/validate_v2.py
```

Expected: Passes (may have warnings since we haven't refactored yet)

**Step 5: Commit automation scripts**

Run:
```bash
git add scripts/create_v2_structure.py scripts/validate_v2.py
git commit -m "feat(v2): Add V2 automation scripts

- Add create_v2_structure.py for V2 setup
- Add validate_v2.py for V2 validation
- Scripts check for TYPE_CHECKING and relative imports

Ref: docs/plans/2025-02-05-models-v2-design.md"
```

---

## Task 3: Refactor V2 Base Classes

**Files:**
- Modify: `src/armodel/models_v2/base/AREnum.py`
- Test: Manual verification

**Step 1: Review AREnum.py for V2 compliance**

Open file: `src/armodel/models_v2/base/AREnum.py`

Check:
- No TYPE_CHECKING (should already be clean)
- No relative imports
- Absolute imports from other V2 modules

Expected: AREnum.py should already be V2 compliant

**Step 2: Add V2 docstring to AREnum.py**

Open file: `src/armodel/models_v2/base/AREnum.py`

Add at top after imports:
```python
"""AUTOSAR Enum base class for V2 models.

V2 Implementation:
- Absolute imports only
- No TYPE_CHECKING
- String annotations for forward references

Compatible with V1 API.
"""
```

**Step 3: Commit base class updates**

Run:
```bash
git add src/armodel/models_v2/base/
git commit -m "feat(v2): Update base classes for V2

- Add V2 documentation to AREnum.py
- Ensure V2 compliance in base module

Ref: docs/plans/2025-02-05-models-v2-design.md"
```

---

## Task 4: Refactor V2 MSR Modules

**Files:**
- Modify: `src/armodel/models_v2/M2/MSR/__init__.py`
- Modify: `src/armodel/models_v2/M2/MSR/AsamHdo/__init__.py`
- Modify: `src/armodel/models_v2/M2/MSR/DataDictionary/__init__.py`
- Modify: `src/armodel/models_v2/M2/MSR/Documentation/__init__.py`
- Modify: `src/armodel/models_v2/M2/MSR/CalibrationData/__init__.py`

**Step 1: Remove TYPE_CHECKING from MSR/AsamHdo/__init__.py**

Open file: `src/armodel/models_v2/M2/MSR/AsamHdo/__init__.py`

Find and remove:
```python
# Remove these lines:
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    ...
```

Replace with nothing (delete the TYPE_CHECKING block)

**Step 2: Convert relative imports to absolute in MSR/AsamHdo/__init__.py**

Open file: `src/armodel/models_v2/M2/MSR/AsamHdo/__init__.py`

Find:
```python
# Before:
from .admin_data import AdminData
from ..some_module import Something
```

Replace with:
```python
# After:
from armodel.models_v2.M2.MSR.AsamHdo.AdminData import AdminData
from armodel.models_v2.M2.MSR.SomeModule import Something
```

**Step 3: Add __all__ to MSR/AsamHdo/__init__.py**

Open file: `src/armodel/models_v2/M2/MSR/AsamHdo/__init__.py`

Add at end of file:
```python
__all__ = [
    'AdminData',
    'AsamHdo',
    'AsamHdoDesc',
    'AsamHdoDimension',
    # ... add all exported classes
]
```

**Step 4: Repeat for other MSR modules**

Apply Steps 1-3 to:
- `src/armodel/models_v2/M2/MSR/DataDictionary/__init__.py`
- `src/armodel/models_v2/M2/MSR/Documentation/__init__.py`
- `src/armodel/models_v2/M2/MSR/CalibrationData/__init__.py`

**Step 5: Validate MSR modules**

Run:
```bash
python scripts/validate_v2.py
```

Expected: No TYPE_CHECKING in MSR modules

**Step 6: Commit MSR refactoring**

Run:
```bash
git add src/armodel/models_v2/M2/MSR/
git commit -m "feat(v2): Refactor MSR modules for V2

- Remove TYPE_CHECKING from all MSR modules
- Convert to absolute imports
- Add __all__ to all __init__.py files
- Follow CODING_RULE_V2_00001, 00002, 00003

Ref: docs/plans/2025-02-05-models-v2-design.md"
```

---

## Task 5: Refactor V2 CommonStructure Module

**Files:**
- Modify: `src/armodel/models_v2/M2/AUTOSARTemplates/CommonStructure/__init__.py`
- Modify: `src/armodel/models_v2/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py`
- Modify: `src/armodel/models_v2/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py`

**Step 1: Refactor CommonStructure/__init__.py**

Open file: `src/armodel/models_v2/M2/AUTOSARTemplates/CommonStructure/__init__.py`

Remove TYPE_CHECKING:
```python
# Delete these lines:
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    pass
```

Convert relative to absolute imports:
```python
# Before:
from .internalbehavior import InternalBehavior
from .implementationdatatypes import ImplementationDataType

# After:
from armodel.models_v2.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import InternalBehavior
from armodel.models_v2.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType
```

Add __all__:
```python
__all__ = [
    'ARObject',
    'Referrable',
    'Identifiable',
    'InternalBehavior',
    'ImplementationDataType',
    # ... add all classes
]
```

**Step 2: Refactor InternalBehavior.py**

Open file: `src/armodel/models_v2/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py`

Convert imports to absolute:
```python
# Before:
from ..generalgenericstructureclasses.identifiable import Identifiable
from ..swcbswmapping import SwcBswMapping

# After:
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models_v2.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import SwcBswMapping
```

Convert type hints to string annotations:
```python
# Before:
def getDataType(self) -> ImplementationDataType:

# After:
def getDataType(self) -> "ImplementationDataType":
```

**Step 3: Validate CommonStructure**

Run:
```bash
python scripts/validate_v2.py
```

Expected: No TYPE_CHECKING or relative imports

**Step 4: Test CommonStructure imports**

Run:
```python
python -c "from armodel.models_v2.M2.AUTOSARTemplates.CommonStructure import InternalBehavior"
```

Expected: No ImportError

**Step 5: Commit CommonStructure refactoring**

Run:
```bash
git add src/armodel/models_v2/M2/AUTOSARTemplates/CommonStructure/
git commit -m "feat(v2): Refactor CommonStructure for V2

- Remove TYPE_CHECKING
- Convert to absolute imports
- Add string annotations for type hints
- Add __all__ exports

Ref: docs/plans/2025-02-05-models-v2-design.md"
```

---

## Task 6: Refactor V2 SWComponentTemplate Module

**Files:**
- Modify: `src/armodel/models_v2/M2/AUTOSARTemplates/SWComponentTemplate/__init__.py`
- Modify: `src/armodel/models_v2/M2/AUTOSARTemplates/SWComponentTemplate/SwComponentType/__init__.py`
- Modify: `src/armodel/models_v2/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

**Step 1: Refactor SwComponentType/__init__.py**

Open file: `src/armodel/models_v2/M2/AUTOSARTemplates/SWComponentTemplate/SwComponentType/__init__.py`

Remove TYPE_CHECKING:
```python
# Remove:
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype

# Delete entire TYPE_CHECKING block
```

Convert to absolute imports:
```python
# Add at top with other imports:
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.Components import RPortPrototype
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.Components import PRPortPrototype
```

Add string annotations to method signatures:
```python
# Before:
class SwComponentType(AtpType, ABC):
    def createPPortPrototype(self, short_name: str):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
        prototype = PPortPrototype(self, short_name)
        self.addElement(prototype)
        self.ports.append(prototype)
        return prototype

# After:
class SwComponentType(AtpType, ABC):
    def createPPortPrototype(self, short_name: str) -> "PPortPrototype":
        from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
        prototype = PPortPrototype(self, short_name)
        self.addElement(prototype)
        self.ports.append(prototype)
        return prototype
```

**Step 2: Refactor Components/__init__.py**

Open file: `src/armodel/models_v2/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

Remove TYPE_CHECKING (if present)

Convert to absolute imports:
```python
# Before:
from ..swcomponenttype import SwComponentType

# After:
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import SwComponentType
```

Add __all__:
```python
__all__ = [
    'PortPrototype',
    'PPortPrototype',
    'RPortPrototype',
    'PRPortPrototype',
]
```

**Step 3: Validate SWComponentTemplate**

Run:
```bash
python scripts/validate_v2.py
```

Expected: No TYPE_CHECKING, no relative imports

**Step 4: Test circular dependency resolution**

Run:
```python
python -c "
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate import SwComponentType
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
print('✓ No circular import error')
"
```

Expected: Prints "✓ No circular import error"

**Step 5: Commit SWComponentTemplate refactoring**

Run:
```bash
git add src/armodel/models_v2/M2/AUTOSARTemplates/SWComponentTemplate/
git commit -m "feat(v2): Refactor SWComponentTemplate for V2

- Remove TYPE_CHECKING from SwComponentType and Components
- Convert to absolute imports
- Add string annotations for circular dependencies
- Add __all__ exports
- Verify no runtime circular imports

Ref: docs/plans/2025-02-05-models-v2-design.md"
```

---

## Task 7: Create V2 Top-Level __init__.py

**Files:**
- Create: `src/armodel/models_v2/__init__.py`

**Step 1: Create V2 __init__.py**

Create file: `src/armodel/models_v2/__init__.py`

```python
"""V2 Models - Clean architecture with absolute imports and no TYPE_CHECKING.

This module provides the V2 implementation of AUTOSAR models with:
- Absolute imports only (no relative imports)
- No TYPE_CHECKING blocks
- Explicit __all__ exports
- String annotations for forward references

V2 is fully API-compatible with V1.

Migration Guide: See docs/development/v2_migration_guide.md
"""

# MSR
from armodel.models_v2.M2.MSR.AsamHdo import *
from armodel.models_v2.M2.MSR.DataDictionary import *
from armodel.models_v2.M2.MSR.Documentation import *
from armodel.models_v2.M2.MSR.CalibrationData import *

# AUTOSAR Templates
from armodel.models_v2.M2.AUTOSARTemplates.AutosarTopLevelStructure import *
from armodel.models_v2.M2.AUTOSARTemplates.CommonStructure import *
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate import *
from armodel.models_v2.M2.AUTOSARTemplates.SystemTemplate import *
from armodel.models_v2.M2.AUTOSARTemplates.BswModuleTemplate import *
from armodel.models_v2.M2.AUTOSARTemplates.ECUCDescriptionTemplate import *
from armodel.models_v2.M2.AUTOSARTemplates.ECUCParameterDefTemplate import *
from armodel.models_v2.M2.AUTOSARTemplates.EcuResourceTemplate import *
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure import *

__all__ = [
    # MSR
    'AsamHdo',
    'AdminData',
    'DataDictionary',
    'Documentation',
    'CalibrationData',
    # AUTOSAR Templates
    'AUTOSAR',
    'ARObject',
    'SwComponentType',
    # ... add all exported classes
]

__version__ = "2.0.0"
```

**Step 2: Test V2 imports**

Run:
```python
python -c "from armodel.models_v2 import AUTOSAR, SwComponentType; print('✓ V2 imports work')"
```

Expected: Prints "✓ V2 imports work"

**Step 3: Commit V2 __init__.py**

Run:
```bash
git add src/armodel/models_v2/__init__.py
git commit -m "feat(v2): Add V2 top-level __init__.py

- Add absolute imports for all V2 modules
- Add __all__ exports
- Add V2 version string
- Add module documentation

Ref: docs/plans/2025-02-05-models-v2-design.md"
```

---

## Task 8: Create V2 Test Structure

**Files:**
- Create: `tests/test_armodel/models_v2/`
- Create: `tests/test_armodel/models_v2/__init__.py`
- Create: `tests/test_armodel/models_v2/test_imports.py`
- Create: `tests/test_armodel/models_v2/test_api_compatibility.py`

**Step 1: Create V2 test directories**

Run:
```bash
mkdir -p tests/test_armodel/models_v2/test_M2/test_MSR
mkdir -p tests/test_armodel/models_v2/test_M2/test_AUTOSARTemplates
```

Expected: Test directories created

**Step 2: Create test_imports.py**

Create file: `tests/test_armodel/models_v2/test_imports.py`

```python
"""Test that all V2 modules can be imported."""

import pytest


def test_all_v2_modules_import():
    """Test that all V2 modules can be imported without circular import errors."""
    from armodel.models_v2 import M2
    from armodel.models_v2.M2 import MSR, AUTOSARTemplates
    from armodel.models_v2.M2.MSR import AsamHdo, DataDictionary
    from armodel.models_v2.M2.AUTOSARTemplates import CommonStructure

    # Should not raise ImportError or CircularImportError


def test_v2_top_level_imports():
    """Test V2 top-level imports."""
    from armodel.models_v2 import AUTOSAR, SwComponentType

    assert AUTOSAR is not None
    assert SwComponentType is not None


def test_no_type_checking_in_v2():
    """Test that V2 has no TYPE_CHECKING imports."""
    from pathlib import Path

    models_v2 = Path("src/armodel/models_v2")

    for py_file in models_v2.rglob("*.py"):
        content = py_file.read_text()
        assert "TYPE_CHECKING" not in content, f"{py_file} contains TYPE_CHECKING"


def test_no_relative_imports_in_v2():
    """Test that V2 has no relative imports."""
    from pathlib import Path

    models_v2 = Path("src/armodel/models_v2")

    for py_file in models_v2.rglob("*.py"):
        content = py_file.read_text()
        # Ignore comments and docstrings
        lines = [
            line for line in content.split('\n')
            if line.strip() and not line.strip().startswith('#')
        ]
        for line in lines:
            if 'from .' in line and 'from .' in line.split('#')[0]:
                assert False, f"{py_file} has relative import: {line}"


def test_all_init_files_have_all():
    """Test that all __init__.py files in V2 have __all__ defined."""
    from pathlib import Path

    models_v2 = Path("src/armodel/models_v2")

    for init_file in models_v2.rglob("__init__.py"):
        content = init_file.read_text()
        assert "__all__" in content, f"{init_file} missing __all__"
```

**Step 3: Create test_api_compatibility.py**

Create file: `tests/test_armodel/models_v2/test_api_compatibility.py`

```python
"""Test V2 API compatibility with V1."""

import pytest
from armodel.models import SwComponentType as V1SwComponentType
from armodel.models_v2 import SwComponentType as V2SwComponentType


def test_v2_has_same_methods():
    """V2 should have all V1 methods."""
    v1_methods = set(dir(V1SwComponentType))
    v2_methods = set(dir(V2SwComponentType))

    # V2 should have at least all V1 methods
    assert v1_methods.issubset(v2_methods)


def test_v2_method_signatures():
    """V2 method signatures should match V1."""
    # Check critical methods exist
    assert hasattr(V2SwComponentType, 'getShortName')
    assert hasattr(V2SwComponentType, 'setShortName')
    assert hasattr(V2SwComponentType, 'createPPortPrototype')
    assert hasattr(V2SwComponentType, 'createRPortPrototype')


def test_v2_instantiation():
    """Test V2 can be instantiated like V1."""
    from armodel.models_v2 import AUTOSAR

    autosar = AUTOSAR.getInstance()
    component = V2SwComponentType(autosar, "TestComponent")

    assert component.getShortName() == "TestComponent"


def test_v2_create_port():
    """Test creating port in V2."""
    from armodel.models_v2 import AUTOSAR

    autosar = AUTOSAR.getInstance()
    component = V2SwComponentType(autosar, "TestComponent")
    port = component.createPPortPrototype("TestPort")

    assert port.getShortName() == "TestPort"
    assert port.parent == component
```

**Step 4: Create __init__.py in tests**

Create file: `tests/test_armodel/models_v2/__init__.py`

```python
"""Tests for V2 models."""
```

**Step 5: Run V2 tests**

Run:
```bash
pytest tests/test_armodel/models_v2/test_imports.py -v
pytest tests/test_armodel/models_v2/test_api_compatibility.py -v
```

Expected: Tests pass (may have some failures initially)

**Step 6: Commit V2 test structure**

Run:
```bash
git add tests/test_armodel/models_v2/
git commit -m "feat(v2): Add V2 test structure

- Add test_imports.py for import validation
- Add test_api_compatibility.py for V1/V2 compatibility
- Tests check for TYPE_CHECKING, relative imports, __all__
- Verify V2 API compatibility with V1

Ref: docs/plans/2025-02-05-models-v2-design.md"
```

---

## Task 9: Add V2 Coding Rules to Documentation

**Files:**
- Modify: `docs/development/coding_rules.md`

**Step 1: Add V2 coding rules section**

Open file: `docs/development/coding_rules.md`

Add before "## Enforcement" section:

```markdown
---

## V2 Model Architecture Rules

### CODING_RULE_V2_00001: Absolute Imports Only

**Maturity**: accept

**V2 models MUST use absolute imports only. Relative imports (`from .` or `from ..`) are prohibited.**

[... add all V2 rules from design document ...]
```

**Step 2: Commit documentation update**

Run:
```bash
git add docs/development/coding_rules.md
git commit -m "docs(v2): Add V2-specific coding rules

- Add CODING_RULE_V2_00001 through CODING_RULE_V2_0010
- Cover absolute imports, no TYPE_CHECKING, __all__ requirements
- Document V2 module path conventions
- Add V2 testing and compatibility rules

Ref: docs/plans/2025-02-05-models-v2-design.md"
```

---

## Task 10: Create V2 Migration Guide

**Files:**
- Create: `docs/development/v2_migration_guide.md`

**Step 1: Create migration guide**

Create file: `docs/development/v2_migration_guide.md`

```markdown
# V1 → V2 Migration Guide

## Overview

V2 models provide the same AUTOSAR functionality with a cleaner, more maintainable codebase.

## What's New in V2

### Architecture Improvements
- **Absolute imports only** - No relative imports
- **No TYPE_CHECKING** - Uses string annotations
- **Explicit __all__** - Clear public API
- **No circular imports** - Cleaner dependency graph

## API Compatibility

**V2 is fully API-compatible with V1!**

```python
# V1 code - works unchanged with V2
from armodel.models import SwComponentType

component = SwComponentType(autosar, "MyComponent")
port = component.createPPortPrototype("MyPort")
```

## Migration Steps

### Step 1: Verify V2 Functionality

```bash
# Run existing tests with V2
pytest tests/ -v
```

### Step 2: Update Imports (Optional)

```python
# Explicit V2 (recommended for new code)
from armodel.models_v2 import SwComponentType
```

### Step 3: Adopt V2 Coding Rules (For Contributors)

1. Use absolute imports
2. No TYPE_CHECKING
3. Add __all__ to __init__.py

## Breaking Changes

**None!** V2 maintains 100% API compatibility.

## Deprecation Timeline

- **Now** - V1 and V2 available in parallel
- **6 months** - V2 becomes default
- **12 months** - V1 deprecated
- **18 months** - V1 removed
```

**Step 2: Commit migration guide**

Run:
```bash
git add docs/development/v2_migration_guide.md
git commit -m "docs(v2): Add V2 migration guide

- User-facing migration guide from V1 to V2
- API compatibility information
- Migration steps and timeline
- No breaking changes

Ref: docs/plans/2025-02-05-models-v2-design.md"
```

---

## Task 11: Final Validation and Testing

**Files:**
- Test: All V2 code
- Test: V2 test suite

**Step 1: Run V2 validation**

Run:
```bash
python scripts/validate_v2.py
```

Expected: "✓ V2 validation passed!"

If fails, fix issues before proceeding.

**Step 2: Run V2 test suite**

Run:
```bash
pytest tests/test_armodel/models_v2/ -v
```

Expected: All tests pass

**Step 3: Run V1 tests to ensure no regression**

Run:
```bash
pytest tests/test_armodel/models/ -v
```

Expected: All V1 tests still pass

**Step 4: Run full test suite**

Run:
```bash
pytest tests/ -v
```

Expected: All tests pass (both V1 and V2)

**Step 5: Run linting on V2**

Run:
```bash
ruff check src/armodel/models_v2/
ruff format --check src/armodel/models_v2/
```

Expected: No linting errors

**Step 6: Fix any issues**

If any steps fail:
1. Identify the issue
2. Fix the code
3. Re-run validation
4. Commit fixes

**Step 7: Final commit**

Run:
```bash
git add .
git commit -m "feat(v2): Complete V2 implementation and validation

- All V2 code follows CODING_RULE_V2_*
- Zero TYPE_CHECKING in V2
- 100% absolute imports
- All __init__.py have __all__
- V2 API 100% compatible with V1
- All V2 tests pass
- V1 tests still pass (no regression)
- Documentation complete

Ref: docs/plans/2025-02-05-models-v2-design.md"
```

---

## Task 12: Create Pull Request

**Files:**
- Git branch and PR

**Step 1: Create feature branch**

Run:
```bash
git checkout -b feature/models-v2-implementation
```

Expected: Switched to new branch

**Step 2: Push to remote**

Run:
```bash
git push -u origin feature/models-v2-implementation
```

Expected: Branch pushed to remote

**Step 3: Create pull request**

Run:
```bash
gh pr create --title "feat: Implement models_v2 with clean imports" --body "$(cat <<'EOF'
## Summary

Implement V2 models with clean import architecture while maintaining 100% V1 API compatibility.

## Changes

### V2 Architecture
- ✅ Absolute imports only (no relative imports)
- ✅ No TYPE_CHECKING blocks
- ✅ String annotations for forward references
- ✅ Explicit __all__ exports
- ✅ Zero circular imports

### Files Modified
- `src/armodel/models_v2/` - New V2 implementation
- `scripts/create_v2_structure.py` - V2 setup script
- `scripts/validate_v2.py` - V2 validation script
- `tests/test_armodel/models_v2/` - V2 test suite
- `docs/development/coding_rules.md` - Added V2 rules
- `docs/development/v2_migration_guide.md` - User migration guide

### API Compatibility
- ✅ V2 is 100% API compatible with V1
- ✅ All V1 methods preserved
- ✅ No breaking changes

### Testing
- ✅ V2 tests: Import validation, API compatibility
- ✅ V1 tests: All pass (no regression)
- ✅ Validation scripts: No TYPE_CHECKING, no relative imports

## Documentation

- Design: `docs/plans/2025-02-05-models-v2-design.md`
- Implementation: `docs/plans/2025-02-05-models-v2-implementation.md`
- Migration Guide: `docs/development/v2_migration_guide.md`
- Coding Rules: `docs/development/coding_rules.md` (CODING_RULE_V2_00001-00010)

## Checklist

- [x] All V2 code follows CODING_RULE_V2_*
- [x] Zero TYPE_CHECKING in V2
- [x] 100% absolute imports (no relative imports)
- [x] All __init__.py have __all__
- [x] V2 API 100% compatible with V1
- [x] All V2 tests pass
- [x] V1 tests still pass
- [x] Documentation complete
- [x] CI/CD passes

## Breaking Changes

None! V1 and V2 coexist safely.

## Related

- Design: #XXX
- Ref: `docs/plans/2025-02-05-models-v2-design.md`
EOF
)"
```

Expected: Pull request created

**Step 4: Monitor CI/CD**

Check that all CI checks pass:
- V1 tests
- V2 tests
- Linting
- Type checking

**Step 5: Address review feedback**

If changes requested:
1. Make changes
2. Commit to branch
3. Push updates
4. Request review again

---

## Success Criteria

V2 implementation is complete when:

- ✅ All V2 code follows CODING_RULE_V2_00001-00010
- ✅ Zero TYPE_CHECKING in V2 codebase
- ✅ 100% absolute imports (no relative imports)
- ✅ All __init__.py files have __all__ defined
- ✅ V2 API 100% compatible with V1
- ✅ All V2 tests pass (match V1 coverage)
- ✅ V1 tests still pass (no regression)
- ✅ Documentation complete (design, implementation, migration guide, coding rules)
- ✅ CI/CD passes for V2
- ✅ No circular import errors
- ✅ Pull request merged

## Notes

- **YAGNI**: Don't refactor V1 code, only V2
- **TDD**: Write tests before refactoring where possible
- **Frequent commits**: Commit after each task
- **DRY**: Use automation scripts to avoid repetition
- **V1 frozen**: V1 models should remain unchanged

## References

- Design document: `docs/plans/2025-02-05-models-v2-design.md`
- V2 coding rules: `docs/development/coding_rules.md` (CODING_RULE_V2_*)
- Migration guide: `docs/development/v2_migration_guide.md`
- Coding standards: `docs/development/coding_rules.md`

---

**Plan complete! Ready to execute.**
