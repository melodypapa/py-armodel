# V2 Migration Guide

**Version:** 2.0.0
**Date:** 2025-02-06
**Status:** Stable

---

## Overview

V2 models (`armodel.models_v2`) provide a cleaner import architecture with no TYPE_CHECKING blocks, absolute imports only, and explicit exports. V2 maintains 100% API compatibility with V1, making migration seamless.

### What's New in V2?

- **Absolute imports only** - No relative imports, clearer module paths
- **No TYPE_CHECKING** - Uses string annotations for forward references
- **Explicit __all__ exports** - Clear public API definition
- **No circular imports** - Cleaner dependencies, faster imports
- **Full V1 API compatibility** - Drop-in replacement for V1

### V2 vs V1 Comparison

| Aspect | V1 | V2 |
|--------|----|----|
| Import path | `armodel.models` | `armodel.models_v2` |
| Imports | Relative allowed | Absolute only |
| TYPE_CHECKING | Used | Prohibited |
| __all__ | Optional | Required |
| Forward refs | TYPE_CHECKING | String annotations |
| Circular deps | Runtime allowed | Prohibited |
| API compatibility | Baseline | 100% compatible |

---

## API Compatibility

V2 is **100% API compatible** with V1. All V1 code works with V2 with only import path changes.

### Example: V1 Code

```python
from armodel.models import AUTOSAR, SwComponentType

autosar = AUTOSAR.getInstance()
component = SwComponentType(autosar, "MyComponent")
port = component.createPPortPrototype("MyPort")
```

### Example: V2 Code (Same Functionality)

```python
from armodel.models_v2 import AUTOSAR, SwComponentType

autosar = AUTOSAR.getInstance()
component = SwComponentType(autosar, "MyComponent")
port = component.createPPortPrototype("MyPort")
```

**Only the import path changed. All API calls remain identical.**

---

## Migration Steps

### Step 1: Update Import Paths

Change all `from armodel.models` to `from armodel.models_v2`:

```bash
# Find all V1 imports
grep -r "from armodel.models" your_code/

# Replace with V2 imports (manual or using sed)
find your_code/ -name "*.py" -exec sed -i 's/from armodel\.models/from armodel.models_v2/g' {} +
```

### Step 2: Update Import Statements

**Before (V1):**
```python
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate import SwComponentType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
```

**After (V2):**
```python
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate import SwComponentType
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
```

### Step 3: Verify Your Code

Run your tests to ensure everything works:

```bash
# Run your test suite
python -m pytest tests/

# Test imports
python -c "from armodel.models_v2 import AUTOSAR; print('V2 imports work')"
```

### Step 4: Update Dependencies (if any)

If you have any pinned dependencies or requirements files, update them to use V2:

```python
# requirements.txt or setup.py
armodel[models_v2] >= 2.0.0  # For V2 models
```

---

## Breaking Changes

**None.** V2 maintains 100% backward compatibility with V1.

### Deprecated Features

No features are deprecated in V2. V1 features continue to work in V2.

### Removed Features

No features are removed in V2.

---

## Common Migration Scenarios

### Scenario 1: Simple Import Migration

**Code before (V1):**
```python
from armodel.models import AUTOSAR

document = AUTOSAR.getInstance()
```

**Code after (V2):**
```python
from armodel.models_v2 import AUTOSAR

document = AUTOSAR.getInstance()
```

**Migration:** Just add `_v2` to the import path.

### Scenario 2: Deep Import Migration

**Code before (V1):**
```python
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
```

**Code after (V2):**
```python
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
```

**Migration:** Add `_v2` to `models` → `models_v2`.

### Scenario 3: TYPE_CHECKING Migration

**Code before (V1):**
```python
from typing import TYPE_CHECKING
from armodel.models import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate import SwComponentType

def my_func(obj: ARObject) -> SwComponentType:
    pass
```

**Code after (V2):**
```python
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate import SwComponentType

def my_func(obj: ARObject) -> "SwComponentType":  # String annotation
    pass
```

**Migration:** Remove TYPE_CHECKING, use string annotations for forward references.

---

## Benefits of Migrating to V2

### 1. Cleaner Code
- No TYPE_CHECKING blocks
- Absolute imports are clearer
- Explicit __all__ exports

### 2. Better IDE Support
- IDEs can better understand explicit exports
- Auto-completion works better
- Navigation is easier

### 3. Faster Imports
- No circular import resolution overhead
- Cleaner dependency graph

### 4. Future-Proof
- V2 is actively developed
- V1 is frozen (bug fixes only)
- New features in V2 only

### 5. Easier Maintenance
- Clearer module structure
- Easier to refactor
- Better documentation

---

## Rollback Plan

If you encounter issues with V2, you can easily rollback to V1.

### Step 1: Revert Import Paths

```bash
# Revert to V1 imports
find your_code/ -name "*.py" -exec sed -i 's/from armodel\.models_v2/from armodel.models/g' {} +
```

### Step 2: Restore TYPE_CHECKING (if needed)

If you were using TYPE_CHECKING in V1:

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate import SwComponentType

def my_func(obj: ARObject) -> SwComponentType:
    pass
```

---

## FAQ

### Q: Do I need to change my code?

**A:** Only import paths need to change. All API calls remain the same.

### Q: Is V2 stable?

**A:** Yes, V2 is production-ready and maintains 100% V1 API compatibility.

### Q: Will V1 be deprecated?

**A:** V1 will be maintained for bug fixes only. New features will be in V2 only. We recommend migrating to V2 within 6 months.

### Q: Can I use V1 and V2 together?

**A:** Yes, you can import both in the same project:
```python
from armodel.models import AUTOSAR as V1_AUTOSAR
from armodel.models_v2 import AUTOSAR as V2_AUTOSAR
```

However, we recommend using one version consistently per project.

### Q: What if I find a bug in V2?

**A:** Please report it on GitHub Issues: https://github.com/melodypapa/py-armodel/issues

---

## Migration Checklist

Use this checklist to ensure a complete migration:

- [ ] Update all `from armodel.models` to `from armodel.models_v2`
- [ ] Update all deep imports (M2.AUTOSARTemplates, etc.)
- [ ] Remove any TYPE_CHECKING blocks
- [ ] Use string annotations for forward references
- [ ] Run your test suite
- [ ] Verify all imports work
- [ ] Check for any warnings or errors
- [ ] Update documentation (if needed)
- [ ] Train your team on V2

---

## Timeline

- **Now:** V2 available for testing
- **Month 1-3:** Migration period for users
- **Month 4-6:** V1 and V2 both supported
- **Month 6+:** V1 frozen (bug fixes only), V2 recommended

---

## Support

For questions or issues:
- **Documentation:** [Design Document](../plans/2025-02-05-models-v2-design.md)
- **Coding Rules:** [V2 Coding Rules](coding_rules.md#v2-specific-coding-rules)
- **GitHub Issues:** https://github.com/melodypapa/py-armodel/issues
- **Discussions:** https://github.com/melodypapa/py-armodel/discussions

---

**Happy migrating!**
