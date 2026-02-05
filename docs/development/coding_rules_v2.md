# V2 Model Coding Rules

This document defines coding standards specific to V2 models (`src/armodel/v2/models/`). These rules complement the general coding rules in `coding_rules.md` and focus on V2-specific requirements.

## Overview

V2 models represent a refactored architecture for the AUTOSAR M2 model with enhanced coding standards, improved type hints, and better separation of concerns. These rules ensure V2 models maintain high code quality and avoid common issues like circular imports.

---

## CODING_RULE_V2_00001: Absolute Imports Only

**Maturity**: accept

**Description**: V2 models MUST use absolute imports only. Relative imports (`from .` or `from ..`) are prohibited.

**Example:**
```python
# CORRECT
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype

# WRONG
from .components import PPortPrototype
```

**Rationale**: Absolute imports improve code clarity, avoid confusion, and make the codebase easier to navigate.

**References**:
- PEP 8 - Style Guide for Python Code (Imports)
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00002: No TYPE_CHECKING Blocks

**Maturity**: accept

**Description**: V2 models MUST NOT use `TYPE_CHECKING` imports. Use string annotations for forward references instead.

**Example:**
```python
# CORRECT
def createPort(self) -> "PPortPrototype":
    from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
    return PPortPrototype(self, short_name)

# WRONG
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .components import PPortPrototype

def createPort(self) -> PPortPrototype:
    return PPortPrototype(self, short_name)
```

**Rationale**: String annotations break circular dependencies without requiring TYPE_CHECKING blocks, making code cleaner and easier to understand.

**References**:
- PEP 484 - Type Hints
- PEP 563 - Postponed Evaluation of Annotations
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00003: Explicit __all__ in __init__.py

**Maturity**: accept

**Description**: Every `__init__.py` file in V2 MUST define `__all__` to explicitly declare the public API.

**Example:**
```python
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import SwComponentType
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype

__all__ = ['SwComponentType', 'PPortPrototype']
```

**Rationale**: Explicit exports make the public API clear, improve IDE support, and prevent unintended exports.

**References**:
- PEP 8 - Module level dunder names
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00004: V2 Module Path Convention

**Maturity**: accept

**Description**: All V2 imports MUST use `armodel.v2.models` as the base module path.

**Example:**
```python
# CORRECT
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate import SwComponentType

# WRONG
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate import SwComponentType
```

**Rationale**: Clear separation between V1 and V2 modules prevents confusion and ensures V2 purity.

**References**:
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00005: String Annotations for Forward References

**Maturity**: accept

**Description**: V2 models MUST use string literals for type hints involving circular dependencies.

**Example:**
```python
# CORRECT
def getPorts(self) -> List["PPortPrototype"]:
    from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
    return self.ports

# WRONG
from .components import PPortPrototype
def getPorts(self) -> List[PPortPrototype]:
    return self.ports
```

**Rationale**: String annotations don't evaluate at import time, breaking circular dependencies while maintaining type hints.

**References**:
- PEP 484 - Forward References
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00006: No Runtime Circular Imports

**Maturity**: accept

**Description**: V2 models MUST NOT have circular imports at runtime. Use string annotations and lazy imports to prevent circular dependency evaluation.

**Example:**
```python
# CORRECT - Import at method scope
class SwComponentType:
    def createPort(self, short_name: str) -> "PPortPrototype":
        from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
        return PPortPrototype(self, short_name)

# WRONG - Circular import at module level
from .components import PPortPrototype
class SwComponentType:
    def createPort(self, short_name: str) -> PPortPrototype:
        return PPortPrototype(self, short_name)
```

**Rationale**: Runtime circular imports cause ImportError and prevent modules from loading. String annotations delay evaluation until runtime.

**Common Circular Import Patterns in V2:**

1. **InternalBehavior ↔ DataPrototypes**:
   - `CommonStructure/InternalBehavior.py` imports from `SWComponentTemplate/Datatype/DataPrototypes`
   - Solution: Use string annotations and lazy imports in `Components/__init__.py`

2. **Identifiable ↔ AsamHdo**:
   - `GenericStructure/GeneralTemplateClasses/Identifiable.py` imports from `MSR/AsamHdo`
   - Solution: Remove wildcard imports from `MSR/__init__.py` and `MSR/AsamHdo/__init__.py`

3. **Components ↔ SwcInternalBehavior**:
   - `Components/__init__.py` imports from `SwcInternalBehavior`
   - Solution: Use TYPE_CHECKING for type hints, lazy imports in methods

**References**:
- Python Circular Import Solutions
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00007: V2 Test Structure

**Maturity**: accept

**Description**: V2 tests MUST be located in `tests/test_armodel/models_v2/` and follow the test structure conventions.

**Example:**
```
tests/test_armodel/models_v2/
├── __init__.py
├── test_imports.py
├── test_api_compatibility.py
└── test_M2/
    ├── test_MSR/
    └── test_AUTOSARTemplates/
```

**Rationale**: Consistent test structure makes tests easy to find and maintain.

**References**:
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00008: V2 Backward Compatibility

**Maturity**: accept

**Description**: V2 models MUST maintain backward compatibility with V1 API. No breaking changes to public API.

**Example:**
```python
# V2 must support all V1 public methods
from armodel.v2.models import SwComponentType

# These V1 methods must work in V2
component = SwComponentType()
component.createPPortPrototype("Port1")
component.getShortName()
component.setShortName("NewName")
```

**Rationale**: Maintaining V1 API compatibility allows users to migrate to V2 without code changes.

**References**:
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00009: V2 Module Initialization

**Maturity**: accept

**Description**: V2 modules MUST define `__version__` in the top-level `__init__.py` file.

**Example:**
```python
# In src/armodel/v2/models/__init__.py
__version__ = "2.0.0"
```

**Rationale**: Version information allows users to verify which V2 version they're using.

**References**:
- PEP 396 - Module Version Numbers
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00010: V2 Documentation Requirements

**Maturity**: accept

**Description**: V2 modules MUST include docstrings documenting V2-specific implementation details and coding rule compliance.

**Example:**
```python
"""
AUTOSAR V2 Models - Clean import architecture.

V2 Implementation:
- Absolute imports only (CODING_RULE_V2_00001)
- No TYPE_CHECKING (CODING_RULE_V2_00002)
- Explicit __all__ exports (CODING_RULE_V2_00003)
- String annotations for forward refs (CODING_RULE_V2_00005)

Compatible with V1 API.
"""
```

**Rationale**: Clear documentation helps developers understand V2 design decisions and maintain V2 compliance.

**References**:
- PEP 257 - Docstring Conventions
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## Enforcement

V2 coding rules are enforced through:

1. **Code review** - All PRs must be reviewed for V2 compliance
2. **Linting** - `ruff check src/armodel/v2/models/` for style violations
3. **Type checking** - `mypy src/armodel/v2/models/` for type correctness
4. **Testing** - `pytest tests/test_armodel/models_v2/ -v` for V2-specific tests
5. **Circular import detection** - `pytest tests/test_armodel/models_v2/test_imports.py::TestV2Imports::test_no_circular_imports`

### Running V2 CI Checks

```bash
# Install dev dependencies
pip install pytest pytest-cov ruff mypy

# Run all checks
ruff check src/armodel/v2/models/
mypy src/armodel/v2/models/
pytest tests/test_armodel/models_v2/ -v --cov=src/armodel/v2/models --cov-report=term
```

### V2 Validation Scripts

The project provides helper scripts for V2 validation:

```bash
# Check V2 coding rules compliance
python scripts/check_v2_coding_rules.py

# Auto-fix V2 coding rule violations
python scripts/fix_v2_coding_rules.py

# Validate V2 model structure
python scripts/validate_v2.py
```

---

## References

This document references these industry-standard style guides:

- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/) - Code layout, naming conventions, and general Python style
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/) - Type annotation standards
- [PEP 563 - Postponed Evaluation of Annotations](https://peps.python.org/pep-0563/) - Forward reference evaluation
- [PEP 396 - Module Version Numbers](https://peps.python.org/pep-0396/) - Version information
- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/) - Docstring formatting
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## Related Documentation

- [General Coding Rules](coding_rules.md) - Project-wide coding standards
- [AGENTS.md](../../AGENTS.md) - Agent guidelines and V2 model overview
- [V2 Migration Guide](../../AGENTS.md#v2-migration-guide) - Migrating from V1 to V2