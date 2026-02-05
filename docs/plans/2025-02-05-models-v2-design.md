# Models V2 Design Document

**Date:** 2025-02-05
**Author:** Claude Code
**Status:** Approved
**Version:** 1.0

## Overview

This document outlines the design for `models_v2` - a refactored version of the py-armodel models with clean import architecture, no TYPE_CHECKING blocks, and full backward compatibility with V1.

## Goals

1. **Remove unnecessary TYPE_CHECKING** - Use string annotations for forward references
2. **Solve circular imports** - Eliminate runtime circular dependencies
3. **Achieve clean __init__.py** - Explicit imports with __all__ exports
4. **Support future refactoring** - Maintain V1 for legacy, V2 for active development
5. **Follow Python best practices** - Absolute imports, PEP 8 compliance, standard patterns

## Architecture

### Parallel V1/V2 Structure

**Phase 1 (Current):**
```
src/armodel/
├── models/          # V1 - Keep untouched (legacy)
│   ├── M2/
│   └── __init__.py
└── models_v2/       # V2 - Active development (new)
    ├── M2/
    │   ├── MSR/
    │   │   ├── AsamHdo/
    │   │   ├── DataDictionary/
    │   │   ├── Documentation/
    │   │   └── CalibrationData/
    │   └── AUTOSARTemplates/
    │       ├── CommonStructure/
    │       ├── SWComponentTemplate/
    │       ├── SystemTemplate/
    │       ├── BswModuleTemplate/
    │       └── ...
    ├── __init__.py      # V2 entry point
    └── base/
        └── AREnum.py
```

**Phase 2 (After V2 proven, ~6 months):**
```
src/armodel/
├── models/          # V2 (rename models_v2 → models)
│   ├── __init__.py
│   ├── M2/
│   └── v1/          # V1 shim (move old models here)
│       ├── __init__.py
│       └── M2/
└── models_backup/   # V1 backup
```

**Key Principle:** V1 frozen (bug fixes only), V2 active development

## Import Architecture

### V2 Import Rules

1. **Absolute imports only** (CODING_RULE_V2_00001)
2. **No TYPE_CHECKING** (CODING_RULE_V2_00002)
3. **Explicit __all__** (CODING_RULE_V2_00003)
4. **String annotations** (CODING_RULE_V2_00005)
5. **No runtime circular imports** (CODING_RULE_V2_00006)

### Example Transformation

**Before (V1):**
```python
from typing import List, TYPE_CHECKING
from .base import ARObject

if TYPE_CHECKING:
    from .components import PPortPrototype

class SwComponentType:
    def createPPortPrototype(self, short_name: str):
        from .components import PPortPrototype  # Inline import
        prototype = PPortPrototype(self, short_name)
        return prototype
```

**After (V2):**
```python
from typing import List
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype

class SwComponentType:
    def createPPortPrototype(self, short_name: str) -> "PPortPrototype":
        prototype = PPortPrototype(self, short_name)
        return prototype
```

### Import Resolution

**At import time:**
```python
# File: SwComponentType.py
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype  # Executes

class SwComponentType:
    def createPort(self, short_name: str) -> "PPortPrototype":  # String - not evaluated
        return PPortPrototype(self, short_name)  # Uses imported class
```

**Why this works:**
- All imports at top (PEP 8 compliant)
- String annotations don't evaluate at import time
- No circular dependency!

## V2-Specific Coding Rules

### CODING_RULE_V2_00001: Absolute Imports Only

V2 models MUST use absolute imports only. Relative imports (`from .` or `from ..`) are prohibited.

```python
# CORRECT
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype

# WRONG
from .components import PPortPrototype
```

### CODING_RULE_V2_00002: No TYPE_CHECKING Blocks

V2 models MUST NOT use `TYPE_CHECKING` imports. Use string annotations for forward references instead.

```python
# CORRECT
def createPort(self) -> "PPortPrototype":
    pass

# WRONG
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .components import PPortPrototype
```

### CODING_RULE_V2_00003: Explicit __all__ in __init__.py

Every `__init__.py` file in V2 MUST define `__all__` to explicitly declare the public API.

```python
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import SwComponentType
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype

__all__ = ['SwComponentType', 'PPortPrototype']
```

### CODING_RULE_V2_00004: V2 Module Path Convention

All V2 imports MUST use `armodel.models_v2` as the base module path.

```python
# CORRECT
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate import SwComponentType

# WRONG
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate import SwComponentType
```

### CODING_RULE_V2_00005: String Annotations for Forward References

V2 models MUST use string literals for type hints involving circular dependencies.

```python
# CORRECT
def getPorts(self) -> List["PPortPrototype"]:
    pass

# WRONG
def getPorts(self) -> List[PPortPrototype]:
    pass
```

### CODING_RULE_V2_00006: No Runtime Circular Imports

V2 models MUST NOT have circular imports at runtime.

```python
# CORRECT - Import at method scope
class SwComponentType:
    def createPort(self, short_name: str) -> "PPortPrototype":
        from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
        return PPortPrototype(self, short_name)
```

## Testing Strategy

### Test Structure

```
tests/
├── test_armodel/
│   ├── models/          # V1 tests - Keep as-is
│   └── models_v2/       # NEW: V2 tests
│       ├── test_M2/
│       │   ├── test_MSR/
│       │   │   ├── test_asamhdo.py
│       │   │   └── test_datadictionary.py
│       │   └── test_AUTOSARTemplates/
│       │       ├── test_commonstructure.py
│       │       └── test_swcomponenttemplate.py
│       ├── test_imports.py
│       └── test_api_compatibility.py
```

### Test Types

**1. Import Tests**
```python
def test_all_v2_modules_import():
    """Test that all V2 modules can be imported without circular import errors."""
    from armodel.models_v2 import M2
    from armodel.models_v2.M2 import MSR, AUTOSARTemplates
```

**2. API Compatibility Tests**
```python
def test_v2_has_same_methods():
    """V2 should have all methods from V1."""
    from armodel.models import SwComponentType as V1SwComponentType
    from armodel.models_v2 import SwComponentType as V2SwComponentType

    v1_methods = set(dir(V1SwComponentType))
    v2_methods = set(dir(V2SwComponentType))
    assert v1_methods.issubset(v2_methods)
```

**3. Functional Tests**
```python
def test_create_pport_prototype():
    """Test creating PPortPrototype in V2."""
    from armodel.models_v2 import AUTOSAR, SwComponentType

    autosar = AUTOSAR.getInstance()
    component = SwComponentType(autosar, "TestComponent")
    port = component.createPPortPrototype("TestPort")

    assert port.getShortName() == "TestPort"
```

## Automation Scripts

### Script 1: Create V2 Structure

```python
# File: scripts/create_v2_structure.py
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
        return

    print(f"Copying {models} -> {models_v2}")
    shutil.copytree(models, models_v2)
    print(f"✓ Created {models_v2}")

if __name__ == "__main__":
    create_v2_structure()
```

### Script 2: Validate V2

```python
# File: scripts/validate_v2.py
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
    type_checking_files = list(models_v2.rglob("*.py"))
    type_checking_files = [f for f in type_checking_files if "TYPE_CHECKING" in f.read_text()]

    if type_checking_files:
        print(f"✗ Found TYPE_CHECKING in {len(type_checking_files)} files")
        return 1

    # Check for relative imports
    relative_import_files = []
    for py_file in models_v2.rglob("*.py"):
        if 'from .' in py_file.read_text():
            relative_import_files.append(py_file)

    if relative_import_files:
        print(f"✗ Found relative imports in {len(relative_import_files)} files")
        return 1

    print("✓ V2 validation passed!")
    return 0

if __name__ == "__main__":
    sys.exit(validate_v2())
```

## Error Handling

### Common Import Errors

**Error 1: Circular Import Detected**
```python
# Symptom: ImportError: cannot import name 'SwComponentType' from partially initialized module

# Solution: Use string annotations
def getPort(self) -> "PPortPrototype":  # String - not evaluated
    return self.ports[0]
```

**Error 2: Module Not Found**
```python
# Symptom: ModuleNotFoundError: No module named 'armodel.models_v2.M2...'

# Solution: Verify path and ensure __init__.py exists
python -c "from armodel.models_v2 import M2"
```

**Error 3: AttributeError After Import**
```python
# Symptom: AttributeError: module 'armodel.models_v2' has no attribute 'SwComponentType'

# Solution: Add to __all__ in __init__.py
__all__ = ['SwComponentType', ...]
```

## Documentation Plan

### Documentation Structure

```
docs/
├── plans/
│   └── 2025-02-05-models-v2-design.md          # This document
├── development/
│   ├── coding_rules.md                          # Add V2 rules
│   └── v2_migration_guide.md                   # NEW: Migration guide
└── api/
    └── v2/                                      # NEW: V2 API docs
        └── models.md
```

### V2 Migration Guide Highlights

**What's New in V2:**
- Absolute imports only
- No TYPE_CHECKING
- Explicit __all__ exports
- No circular imports

**API Compatibility:**
- V2 is 100% API compatible with V1
- No code changes required for most users

**Migration Steps:**
1. Verify V2 functionality
2. Update imports (optional)
3. Run tests

## Implementation Timeline

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Phase 1: Setup | Week 1 | V2 directory structure + scripts |
| Phase 2: Refactoring | Weeks 2-3 | Clean V2 code |
| Phase 3: Testing | Weeks 4-5 | V2 test suite |
| Phase 4: Validation | Week 6 | All validation checks pass |
| Phase 5: Documentation | Week 7 | Complete documentation |
| Phase 6: Review | Week 8 | Merged and released |

## Success Criteria

V2 is considered complete when:

- ✅ All V2 code follows CODING_RULE_V2_*
- ✅ Zero TYPE_CHECKING in V2
- ✅ 100% absolute imports (no relative imports)
- ✅ All __init__.py have __all__
- ✅ V2 API 100% compatible with V1
- ✅ All V2 tests pass (target: same coverage as V1)
- ✅ V1 tests still pass (no regression)
- ✅ Documentation complete
- ✅ CI/CD passes for V2
- ✅ No circular import errors

## Benefits

1. **Cleaner code** - Absolute imports, no TYPE_CHECKING
2. **Better IDE support** - Explicit exports in __all__
3. **Faster imports** - No circular dependencies
4. **Standard practices** - Follows PEP 8 and industry patterns
5. **Future-proof** - Easier to refactor and maintain
6. **Backward compatible** - V1 and V2 can coexist

## References

- PEP 8 - Style Guide for Python Code
- PEP 484 - Type Hints
- PEP 562 - Module __getattr__ and __dir__
- TensorFlow v1/v2 compatibility guide
- Pydantic v1/v2 migration guide

## Appendix

### V2 vs V1 Comparison

| Aspect | V1 | V2 |
|--------|----|----|
| Imports | Relative allowed | Absolute only |
| TYPE_CHECKING | Used | Prohibited |
| __all__ | Optional | Required |
| Module path | armodel.models | armodel.models_v2 |
| Forward refs | TYPE_CHECKING | String annotations |
| Circular deps | Runtime allowed | Prohibited |
| Status | Legacy (frozen) | Active development |

### V2 Coding Rules Quick Reference

- CODING_RULE_V2_00001: Absolute imports only
- CODING_RULE_V2_00002: No TYPE_CHECKING
- CODING_RULE_V2_00003: Explicit __all__ in __init__.py
- CODING_RULE_V2_00004: V2 module path convention
- CODING_RULE_V2_00005: String annotations for forward references
- CODING_RULE_V2_0006: No runtime circular imports
- CODING_RULE_V2_0007: V2 test structure
- CODING_RULE_V2_0008: V2 backward compatibility
- CODING_RULE_V2_0009: V2 module initialization
- CODING_RULE_V2_0010: V2 documentation requirements

---

**Document Status:** Approved
**Next Steps:** Execute implementation plan (8-week timeline)
**Contact:** GitHub Issues - https://github.com/melodypapa/py-armodel/issues
