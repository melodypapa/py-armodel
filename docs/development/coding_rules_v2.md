# V2 Coding Rules

This document defines coding standards for all V2 modules in py-armodel (`src/armodel/v2/`). These rules complement the general coding rules in `coding_rules.md` and focus on V2-specific requirements.

## Overview

V2 represents a refactored architecture for py-armodel with enhanced coding standards, improved type hints, and better separation of concerns. V2 includes:

- **V2 Models**: `src/armodel/v2/models/` - AUTOSAR M2 model classes
- **V2 Reader**: `src/armodel/v2/reader/` - ARXML deserialization
- **V2 Writer**: `src/armodel/v2/writer/` - ARXML serialization
- **V2 Utils**: `src/armodel/v2/utils/` - Shared utilities

These rules ensure all V2 modules maintain high code quality, avoid circular imports, and provide a consistent architecture for extension and maintenance.

### V2 Architecture Principles

1. **Clean Imports**: Absolute imports only, no TYPE_CHECKING blocks
2. **Extensibility**: Open for extension, closed for modification
3. **Modern Python**: Use latest Python features and best practices
4. **Type Safety**: Explicit type hints with string annotations for forward refs
5. **Modularity**: Clear separation of concerns between modules
6. **Clean Break**: No V1 compatibility constraints - fresh design

---

## CODING_RULE_V2_00001: Absolute Imports Only

**Maturity**: accept

**Scope**: All V2 modules (models, reader, writer, utils)

**Description**: All V2 modules MUST use absolute imports only. Relative imports (`from .` or `from ..`) are prohibited.

**Example:**
```python
# CORRECT - Absolute imports
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
from armodel.v2.reader.base_reader import ARXMLReader
from armodel.v2.writer.base_writer import ARXMLWriter

# WRONG - Relative imports
from .components import PPortPrototype
from ..reader import ARXMLReader
```

**Rationale**: Absolute imports improve code clarity, avoid confusion, and make the codebase easier to navigate. They make dependencies explicit and work consistently across different execution contexts.

**References**:
- PEP 8 - Style Guide for Python Code (Imports)
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00002: TYPE_CHECKING Blocks for Circular Imports

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules SHOULD prefer string annotations for forward references. However, `TYPE_CHECKING` blocks MAY be used when string annotations alone are insufficient to resolve circular import dependencies.

**Example:**
```python
# PREFERRED - String annotation (when no circular dependency)
def createPort(self) -> "PPortPrototype":
    from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
    return PPortPrototype(self, short_name)

# ACCEPTABLE - TYPE_CHECKING block for circular imports
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements import (
        DocumentationBlock,
    )

class Identifiable:
    def __init__(self) -> None:
        self.introduction: DocumentationBlock | None = None  # Type available due to TYPE_CHECKING
```

**When to Use TYPE_CHECKING:**
- When string annotations create ruff F821 "undefined name" errors
- When imports form a circular dependency that cannot be resolved with string annotations alone
- When type checkers (mypy) require the actual type to be imported for proper validation

**Files Using TYPE_CHECKING for Circular Imports:**
- `GenericStructure/GeneralTemplateClasses/Identifiable.py` - DocumentationBlock
- `GenericStructure/LifeCycles.py` - DocumentationBlock
- `MSR/Documentation/Annotation.py` - DocumentationBlock
- `MSR/Documentation/MsrQuery.py` - DocumentationBlock
- `MSR/Documentation/TextModel/BlockElements/RequirementsTracing.py` - DocumentationBlock
- `GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py` - AtpBlueprintMapping

**Rationale**: While string annotations work for most forward references, complex circular dependencies in large AUTOSAR model structures sometimes require TYPE_CHECKING blocks. This pragmatic approach balances type safety with code maintainability.

**References**:
- PEP 484 - Type Hints
- PEP 563 - Postponed Evaluation of Annotations
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00003: Explicit __all__ in __init__.py

**Maturity**: accept

**Scope**: All V2 modules

**Description**: Every `__init__.py` file in V2 MUST define `__all__` to explicitly declare the public API.

**Example:**
```python
# Models __init__.py
from armodel.v2.models.M2.AUTOSARTemplates.SwComponentType import SwComponentType
from armodel.v2.models.M2.AUTOSARTemplates.Components import PPortPrototype

__all__ = ['SwComponentType', 'PPortPrototype']

# Reader __init__.py
from armodel.v2.reader.base_reader import ARXMLReader
from armodel.v2.reader.schema_registry import SchemaRegistry

__all__ = ['ARXMLReader', 'SchemaRegistry']
```

**Rationale**: Explicit exports make the public API clear, improve IDE support, and prevent unintended exports. This applies to all V2 module packages.

**References**:
- PEP 8 - Module level dunder names
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00004: V2 Module Path Convention

**Maturity**: accept

**Scope**: All V2 imports

**Description**: All V2 imports MUST use `armodel.v2` as the base module path with appropriate sub-module (models, reader, writer, utils).

**Example:**
```python
# CORRECT - Use appropriate V2 sub-module paths
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate import SwComponentType
from armodel.v2.reader.base_reader import ARXMLReader
from armodel.v2.writer.base_writer import ARXMLWriter
from armodel.v2.utils.errors import ReadError

# WRONG - Don't mix V1 and V2 paths
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate import SwComponentType
```

**Rationale**: Clear separation between V1 and V2 modules prevents confusion and ensures V2 purity. Using correct sub-module paths (models, reader, writer, utils) makes dependencies explicit.

**References**:
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00005: String Annotations for Forward References

**Maturity**: accept

**Scope**: All V2 modules

**Description**: All V2 modules MUST use string literals for type hints involving circular dependencies.

**Example:**
```python
# CORRECT - String annotations
def getPorts(self) -> List["PPortPrototype"]:
    from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
    return self.ports

# WRONG - Direct import causes circular dependency
from .components import PPortPrototype
def getPorts(self) -> List[PPortPrototype]:
    return self.ports
```

**Rationale**: String annotations don't evaluate at import time, breaking circular dependencies while maintaining type hints. This applies to models, reader, writer, and all V2 code.

**References**:
- PEP 484 - Forward References
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00006: No Runtime Circular Imports

**Maturity**: accept

**Scope**: All V2 modules

**Description**: All V2 modules MUST NOT have circular imports at runtime. Use string annotations and lazy imports to prevent circular dependency evaluation.

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

## CODING_RULE_V2_00008: V2 Module Initialization

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

## CODING_RULE_V2_00011: __all__ Placement After Imports

**Maturity**: accept

**Description**: In V2 `__init__.py` files, `__all__` MUST be placed after all import statements.

**Example:**
```python
# CORRECT
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import SwComponentType
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype

__all__ = ['SwComponentType', 'PPortPrototype']

# WRONG
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import SwComponentType
__all__ = ['SwComponentType', 'PPortPrototype']
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
```

**Rationale**: Placing `__all__` after all imports ensures the module is fully loaded before defining its public API, improves readability, and prevents confusion about what is exported.

**References**:
- PEP 8 - Module Level Dunder Names
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00012: Explicit Class Imports

**Maturity**: accept

**Description**: V2 models MUST use explicit class imports instead of wildcard imports (`from module import *`). Wildcard imports are prohibited except in specific documented cases.

**Example:**
```python
# CORRECT - Explicit imports
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import (
    SwComponentType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    PPortPrototype,
    RPortPrototype,
)

__all__ = [
    "SwComponentType",
    "PPortPrototype",
    "RPortPrototype",
]

# WRONG - Wildcard imports
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import *
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import *
```

**Exceptions:**
Wildcard imports (`import *`) are ONLY allowed in these specific cases:
1. When documented in the module with a comment explaining the circular dependency issue
2. When re-exporting from subpackages in `__init__.py` files (with explicit `__all__`)
3. When specifically approved in the V2 design documentation

**Rationale**: Explicit imports improve code clarity, make dependencies visible, enable better IDE support, and prevent unintentional namespace pollution. Wildcard imports hide what is actually being used and can cause naming conflicts.

**References**:
- PEP 8 - Imports
- PEP 20 - The Zen of Python ("Explicit is better than implicit")
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00013: Block Import Style

**Maturity**: accept

**Description**: V2 models MUST use block import style (multi-line with parentheses) for imports. Single-line comma-separated imports are prohibited.

**Example:**
```python
# CORRECT - Block import style (multi-line with parentheses)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import (
    SwComponentType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    PPortPrototype,
    RPortPrototype,
    ProvidePortPrototype,
)

# WRONG - Single-line comma-separated imports
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype, RPortPrototype, ProvidePortPrototype

# WRONG - Backslash continuation (use parentheses instead)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import \
    PPortPrototype, RPortPrototype
```

**Formatting Rules:**
1. Opening parenthesis on the same line as `import`
2. One import per line
3. Each import line ends with a comma
4. Closing parenthesis on its own line
5. Indent with 4 spaces for the import names
6. Trailing comma on the last import (enables cleaner git diffs)

**Rationale**: Block import style improves readability, makes imports easier to scan, enables cleaner version control diffs (adding/removing imports doesn't touch other lines), and follows Python best practices for multi-line imports.

**References**:
- PEP 8 - Imports (Multi-line Imports)
- PEP 8 - Maximum Line Length (block style helps manage long AUTOSAR paths)
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## CODING_RULE_V2_00014: V2 Model Extensibility

**Maturity**: accept

**Description**: V2 base model classes MUST be designed for extensibility. All core V2 models (ARObject, Identifiable, AUTOSAR, ARPackage) MUST support extension by other V2 modules without requiring modification to base classes.

**Example:**
```python
# CORRECT - Extensible base class design
class ARObject(ABC):
    """Base class for all AUTOSAR objects - extensible for V2 modules."""

    @abstractmethod
    def _validate_abstract(self) -> None:
        """Validate that this is a concrete class."""
        pass

    def __init__(self) -> None:
        if type(self) is ARObject:
            raise TypeError("ARObject is an abstract class.")
        self._validate_abstract()
        self.parent: Optional["ARObject"] = None
        self.uuid: Optional[str] = None
        # Extensible attributes dict for custom properties
        self._extended_attributes: Dict[str, Any] = {}

    # Core methods that can be overridden
    def getTagName(self) -> str:
        """Get the XML tag name for this object."""
        return self.__class__.__name__

    def getExtendedAttribute(self, key: str) -> Any:
        """Get extended attribute for custom V2 module properties."""
        return self._extended_attributes.get(key)

    def setExtendedAttribute(self, key: str, value: Any) -> None:
        """Set extended attribute for custom V2 module properties."""
        self._extended_attributes[key] = value

# CORRECT - V2 module can extend without modifying base
class SwComponentType(Identifiable):
    """Extended for SW component template - no base class changes needed."""

    def __init__(self) -> None:
        super().__init__()
        # Module-specific attributes
        self.adminData: Optional[AdminData] = None
        self.behaviorRef: Optional[InternalBehavior] = None
```

**Requirements:**

1. **Base Classes Must Provide Extension Points**:
   - Protected attributes with `_` prefix for derived classes
   - Template method pattern for customizable behavior
   - Hooks for pre/post processing
   - Extended attributes dictionary for custom properties

2. **V2 Modules MUST Not Modify Base Classes**:
   - Use inheritance to extend functionality
   - Use composition for optional features
   - Use mixins for cross-cutting concerns
   - Never modify `armodel/v2/models/ar_object.py` or `models.py` directly

3. **Follow Open/Closed Principle**:
   - Open for extension through inheritance
   - Closed for modification in base classes
   - Use abstract methods to define extension points

4. **Use Modern Python Patterns**:
   - Prefer composition over inheritance
   - Use dataclasses for simple data containers
   - Use type hints for better IDE support
   - Follow PEP 8 naming conventions

**Rationale**: Extensible design allows other V2 modules (reader, writer, etc.) to enhance functionality without modifying core models, following SOLID principles and making the codebase more maintainable.

**References**:
- SOLID Principles - Open/Closed Principle
- Design Patterns - Template Method Pattern
- Design Document: `docs/plans/2026-02-07-v2-arxml-reader-writer-design.md`

---

## CODING_RULE_V2_00015: V2 Module Integration Contract

**Maturity**: accept

**Description**: All V2 modules (reader, writer, etc.) MUST adhere to the V2 Model Integration Contract when working with V2 models.

**Contract Requirements:**

1. **Reader Module Contract**:
```python
# Readers MUST work with any ARObject subclass
class ARXMLReader:
    def load(self, file_path: str, document: AUTOSAR) -> None:
        """Load ARXML into AUTOSAR document.

        Contract:
        - MUST handle all ARObject subclasses
        - MUST preserve parent-child relationships
        - MUST not require model modifications
        - MUST use public API only (no private attribute access)
        """
```

2. **Writer Module Contract**:
```python
# Writers MUST serialize any ARObject subclass
class ARXMLWriter:
    def save(self, file_path: str, document: AUTOSAR) -> None:
        """Save AUTOSAR document to ARXML file.

        Contract:
        - MUST handle all ARObject subclasses
        - MUST use getTagName() for XML element names
        - MUST not require model modifications
        - MUST use public API only
        """
```

3. **Model Extension Contract**:
```python
# V2 modules extending models MUST:
# - Call super().__init__() to preserve base initialization
# - Override getTagName() for custom XML tags
# - Implement _validate_abstract() for concrete classes
# - Use extended_attributes for custom properties
class CustomV2Model(Identifiable):
    def __init__(self) -> None:
        super().__init__()  # MUST call super
        # Module-specific initialization
```

**Validation:**
```python
# Test that module respects contract
def test_v2_module_contract():
    """Verify V2 module doesn't require model modifications."""
    from armodel.v2.models import AUTOSAR, ARObject

    # Module must work with base classes
    autosar = AUTOSAR.getInstance()
    reader = ARXMLReader()
    writer = ARXMLWriter()

    # Must not require modifications to base classes
    assert hasattr(ARObject, "getTagName")
    assert hasattr(ARObject, "getExtendedAttribute")
    assert hasattr(ARObject, "setExtendedAttribute")
```

**Rationale**: Clear integration contracts ensure V2 modules can work together without tight coupling, making the codebase more modular and maintainable.

**References**:
- Design Patterns - Contract Pattern
- Design Document: `docs/plans/2026-02-07-v2-arxml-reader-writer-design.md`

---

## Enforcement

V2 coding rules are enforced through:

1. **Code review** - All PRs must be reviewed for V2 compliance across all modules
2. **Linting** - `ruff check src/armodel/v2/` for style violations (all V2 modules)
3. **Type checking** - `mypy src/armodel/v2/` for type correctness (all V2 modules)
4. **Testing** - `pytest tests/test_armodel/v2/ -v` for V2-specific tests
5. **Circular import detection** - `pytest tests/test_armodel/v2/ -k circular` for import validation

### Running V2 CI Checks

```bash
# Install dev dependencies
pip install pytest pytest-cov ruff mypy

# Run all checks for all V2 modules
ruff check src/armodel/v2/
mypy src/armodel/v2/
pytest tests/test_armodel/v2/ -v --cov=src/armodel/v2 --cov-report=term
```

### Module-Specific Validation

```bash
# Models validation
pytest tests/test_armodel/v2/models/ -v

# Reader validation
pytest tests/test_armodel/v2/reader/ -v

# Writer validation
pytest tests/test_armodel/v2/writer/ -v

# Integration tests
pytest tests/test_armodel/v2/integration/ -v

# Extensibility tests
pytest tests/test_armodel/v2/test_model_extensibility.py -v
```

### V2 Validation Scripts

The project provides helper scripts for V2 validation:

```bash
# Check V2 coding rules compliance
python scripts/check_v2_coding_rules.py

# Auto-fix V2 coding rule violations
python scripts/fix_v2_coding_rules.py

# Validate V2 structure
python scripts/validate_v2.py
```

---

## V2 Module Structure

```
src/armodel/v2/
├── models/           # AUTOSAR M2 model classes
│   ├── ar_object.py  # Base ARObject class
│   ├── models.py     # Core models (AUTOSAR, ARPackage, Identifiable)
│   └── M2/           # AUTOSAR M2 schema structure
├── reader/           # ARXML deserialization
│   ├── base_reader.py
│   ├── schema_registry.py
│   └── element_handler.py
├── writer/           # ARXML serialization
│   └── base_writer.py
└── utils/            # Shared utilities
    ├── errors.py
    └── context.py
```

---

## References

This document references these industry-standard style guides:

- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/) - Code layout, naming conventions, and general Python style
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/) - Type annotation standards
- [PEP 563 - Postponed Evaluation of Annotations](https://peps.python.org/pep-0563/) - Forward reference evaluation
- [PEP 396 - Module Version Numbers](https://peps.python.org/pep-0396/) - Version information
- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/) - Docstring formatting
- Design Document: `docs/plans/2026-02-07-v2-arxml-reader-writer-design.md`

---

## Related Documentation

- [General Coding Rules](coding_rules.md) - Project-wide coding standards
- [AGENTS.md](../../AGENTS.md) - Agent guidelines and V2 overview
- [CLAUDE.md](../../CLAUDE.md) - Project guidance for Claude Code
- [V2 Reader/Writer Design](../../plans/2026-02-07-v2-arxml-reader-writer-design.md) - V2 architecture design