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

1. **Clean Imports**: Absolute imports only, TYPE_CHECKING blocks only for self-referencing return types
2. **Extensibility**: Open for extension, closed for modification
3. **Modern Python**: Use latest Python features and best practices
4. **Type Safety**: Explicit type hints with direct imports for non-self types, string annotations only for self-referencing
5. **Modularity**: Clear separation of concerns between modules
6. **Clean Break**: No V1 compatibility constraints - fresh design

---

## Import Rules

### CODING_RULE_V2_00001: Absolute Imports Only

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

### CODING_RULE_V2_00002: TYPE_CHECKING for Self-Referencing Return Types

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules MUST use `TYPE_CHECKING` blocks and string annotations ONLY for method return types involving `self`. All other type annotations should use direct imports without TYPE_CHECKING.

**Example:**
```python
# CORRECT - TYPE_CHECKING for self-referencing return type
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import (
        SwComponentType,
    )

class SwComponentType:
    def with_short_name(self, value: str) -> "SwComponentType":
        """Return self for method chaining - use string annotation."""
        self.short_name = value
        return self

    def with_category(self, value: str) -> "SwComponentType":
        """Return self for method chaining - use string annotation."""
        self.category = value
        return self

# CORRECT - Direct import for non-self types
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    PPortPrototype,
)

class SwComponentType:
    def create_port(self, short_name: str) -> PPortPrototype:
        """Return different type - use direct import."""
        return PPortPrototype(self, short_name)

# WRONG - TYPE_CHECKING for non-self types
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype

class SwComponentType:
    def create_port(self, short_name: str) -> "PPortPrototype":  # Wrong: use direct import
        return PPortPrototype(self, short_name)
```

**Requirements:**

1. **Use TYPE_CHECKING ONLY for Self-Referencing Methods**:
   - Methods that return `self` for chaining
   - Factory methods that return the same class type
   - Any method where the return type is the class itself

2. **Use Direct Imports for All Other Types**:
   - Return types that are different classes
   - Parameter types (even if forward references)
   - Attribute types in `__init__`

3. **String Annotation Format for Self-Referencing**:
   ```python
   def with_method(self) -> "ClassName":  # Use quotes for self-referencing
       return self
   ```

4. **TYPE_CHECKING Block Placement**:
   - Place at module level after standard imports
   - Import only the self-referencing class
   - Use in method return type annotations

**Why This Approach:**

- **Self-referencing is the only circular dependency**: When a method returns `self`, the class refers to itself, creating a circular dependency
- **All other types can be imported directly**: Forward references to other classes don't create circular dependencies in V2's clean architecture
- **Simpler code**: Reduces unnecessary TYPE_CHECKING usage
- **Better IDE support**: Direct imports provide better autocomplete and navigation

**Rationale**: V2's clean architecture eliminates most circular dependencies. The only remaining circular dependency is when a class references itself in method return types (e.g., for method chaining). Using TYPE_CHECKING only for this specific case keeps the code simple and maintainable.

**References**:
- PEP 484 - Type Hints
- PEP 563 - Postponed Evaluation of Annotations
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

### CODING_RULE_V2_00003: Explicit __all__ in __init__.py

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

### CODING_RULE_V2_00004: V2 Module Path Convention

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

### CODING_RULE_V2_00011: __all__ Placement After Imports

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

### CODING_RULE_V2_00012: Explicit Class Imports

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

### CODING_RULE_V2_00013: Block Import Style

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

## Type System Rules

### CODING_RULE_V2_00005: Direct Imports for Non-Self Types

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules MUST use direct imports for all type annotations EXCEPT method return types involving `self`. String annotations are only allowed for self-referencing return types (see CODING_RULE_V2_00002).

**Example:**
```python
# CORRECT - Direct import for non-self types
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    PPortPrototype,
)
from typing import List

class SwComponentType:
    _ports: List[PPortPrototype]  # Direct import for attribute type

    def get_ports(self) -> List[PPortPrototype]:  # Direct import for return type
        """Return list of ports - different type, use direct import."""
        return self._ports

    def create_port(self, short_name: str) -> PPortPrototype:  # Direct import
        """Create and return a new port - different type, use direct import."""
        return PPortPrototype(self, short_name)

# CORRECT - String annotation for self-referencing (see CODING_RULE_V2_00002)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import (
        SwComponentType,
    )

class SwComponentType:
    def with_short_name(self, value: str) -> "SwComponentType":  # String annotation
        """Return self for chaining - self-referencing, use string annotation."""
        self.short_name = value
        return self

# WRONG - String annotation for non-self types
def get_ports(self) -> List["PPortPrototype"]:  # Wrong: should use direct import
    return self._ports
```

**Requirements:**

1. **Use Direct Imports for All Non-Self Types**:
   - Attribute types in class definitions
   - Parameter types in method signatures
   - Return types that are different from the containing class
   - Generic type parameters (List, Dict, Optional, etc.)

2. **Use String Annotations ONLY for Self-Referencing**:
   - Method return types that return the class itself
   - Factory methods returning the same class type
   - Any type annotation where the class refers to itself

3. **Import Placement**:
   - Place direct imports at module level
   - Place TYPE_CHECKING block after standard imports
   - Keep imports organized by category (standard library, third-party, local)

**Why This Approach:**

- **V2 architecture eliminates circular dependencies**: The clean module structure with absolute imports means most forward references don't create circular dependencies
- **Better tooling support**: Direct imports provide better IDE autocomplete, navigation, and refactoring
- **Explicit is better than implicit**: Direct imports make dependencies visible and explicit
- **Simpler code**: Reduces unnecessary complexity from widespread string annotation usage

**Rationale**: With V2's clean architecture and absolute imports, circular dependencies are rare. The only remaining case is when a class references itself (e.g., for method chaining). Using direct imports for everything else improves code clarity and tool support.

**References**:
- PEP 484 - Forward References
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

### CODING_RULE_V2_00006: No Runtime Circular Imports

**Maturity**: accept

**Scope**: All V2 modules

**Description**: All V2 modules MUST NOT have circular imports at runtime. With V2's clean architecture and absolute imports, circular imports should be rare. The only acceptable circular import pattern is self-referencing return types handled via TYPE_CHECKING (see CODING_RULE_V2_00002).

**Example:**
```python
# CORRECT - Direct import at module level (preferred)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    PPortPrototype,
)

class SwComponentType:
    def create_port(self, short_name: str) -> PPortPrototype:
        """Create and return port - direct import, no circular dependency."""
        return PPortPrototype(self, short_name)

# CORRECT - Lazy import at method scope (only when necessary)
class SwComponentType:
    def create_complex_object(self, config: dict) -> "SomeComplexType":
        """
        Lazy import only when necessary for complex initialization.

        Use this pattern ONLY when:
        1. Import would cause circular dependency
        2. Type is only used in this method
        3. Cannot use direct import at module level
        """
        from armodel.v2.models.M2.AUTOSARTemplates.SomeModule import SomeComplexType
        return SomeComplexType(config)

# CORRECT - Self-referencing via TYPE_CHECKING (see CODING_RULE_V2_00002)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import (
        SwComponentType,
    )

class SwComponentType:
    def with_short_name(self, value: str) -> "SwComponentType":
        """Return self for chaining - self-referencing only."""
        self.short_name = value
        return self

# WRONG - Module-level circular import
from .components import PPortPrototype  # Wrong: relative import
from armodel.v2.models.M2.AUTOSARTemplates.SWCInternalBehavior import InternalBehavior  # Wrong: causes circular dependency

class SwComponentType:
    _behavior: InternalBehavior  # This will cause ImportError at runtime
```

**Circular Import Prevention Strategies:**

1. **Use Direct Imports (Preferred)**:
   - Import at module level using absolute paths
   - V2's clean architecture prevents most circular dependencies
   - This provides best IDE support and code clarity

2. **Use Lazy Imports (When Necessary)**:
   - Import inside method/function body only when needed
   - Use when direct import would cause circular dependency
   - Use when type is only used in a specific method

3. **Use TYPE_CHECKING (Self-Referencing Only)**:
   - For methods returning `self` or the same class type
   - See CODING_RULE_V2_00002 for details

4. **Refactor Architecture (Last Resort)**:
   - If circular dependencies persist, consider refactoring module structure
   - Extract common types to separate modules
   - Use dependency injection instead of direct imports

**Common V2 Circular Import Patterns (Should Be Rare):**

1. **Self-Referencing (Expected)**:
   - Methods returning `self` for chaining
   - Solution: Use TYPE_CHECKING (see CODING_RULE_V2_00002)

2. **Mutual Dependencies (Avoid)**:
   - Module A imports Module B, Module B imports Module A
   - Solution: Refactor to extract common functionality

3. **Wildcards Cause Circular Imports (Avoid)**:
   - `from module import *` can create hidden circular dependencies
   - Solution: Use explicit imports (see CODING_RULE_V2_00012)

**Rationale**: Runtime circular imports cause ImportError and prevent modules from loading. V2's clean architecture with absolute imports eliminates most circular dependencies. The only acceptable pattern is self-referencing return types, which are handled via TYPE_CHECKING. All other circular dependencies should be resolved through refactoring.

**References**:
- Python Circular Import Solutions
- Design Document: `docs/plans/2025-02-05-models-v2-design.md`

---

## Module Structure Rules

### CODING_RULE_V2_00007: V2 Test Structure

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

### CODING_RULE_V2_00008: V2 Module Initialization

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

### CODING_RULE_V2_00010: V2 Documentation Requirements

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

## Architecture & Extensibility Rules

### CODING_RULE_V2_00014: V2 Model Extensibility

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

### CODING_RULE_V2_00015: V2 Module Integration Contract

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

## API Design Rules

### CODING_RULE_V2_00016: Property-Based Dual API for Attributes

**Maturity**: accept

**Scope**: All V2 model classes

**Description**: All V2 model classes MUST provide Pythonic `@property` decorators for attribute access while maintaining AUTOSAR camelCase internal storage and AUTOSAR-compatible getter/setter methods.

**Example:**
```python
# CORRECT - Property-based dual API
from dataclasses import dataclass, field

@dataclass
class SwComponentType(ARObject):
    # Internal storage (AUTOSAR camelCase)
    _shortName: str = field(default="", init=False, repr=False)

    # Pythonic property (snake_case)
    @property
    def short_name(self) -> str:
        """Get short name (Pythonic accessor)."""
        return self._shortName

    @short_name.setter
    def short_name(self, value: str) -> None:
        """Set short name with validation."""
        if not isinstance(value, str):
            raise TypeError(f"short_name must be str, got {type(value).__name__}")
        if not value:
            raise ValueError("short_name cannot be empty")
        self._shortName = value

    # AUTOSAR-compatible methods (camelCase)
    def getShortName(self) -> str:
        """AUTOSAR-compliant getter."""
        return self.short_name

    def setShortName(self, value: str) -> "SwComponentType":
        """AUTOSAR-compliant setter with method chaining."""
        self.short_name = value
        return self

# WRONG - Direct attribute access without properties
@dataclass
class SwComponentType(ARObject):
    short_name: str  # No validation, no AUTOSAR compatibility
```

**Requirements:**

1. **Internal Storage Naming**: All internal attributes MUST use AUTOSAR camelCase with underscore prefix (`_shortName`, `_uuid`)

2. **Property Naming**: All public properties MUST use Pythonic snake_case (`short_name`, `uuid`)

3. **AUTOSAR Methods**: All classes MUST maintain AUTOSAR getter/setter methods (`getShortName()`, `setShortName()`)

4. **Delegation Pattern**: AUTOSAR methods MUST delegate to properties to avoid code duplication:
   ```python
   def getShortName(self) -> str:
       return self.short_name  # Delegates to property
   ```

5. **Type Hints**: All properties and methods MUST have complete type hints

6. **Validation**: Property setters MUST perform validation (see CODING_RULE_V2_00018)

**Rationale**: Property-based dual API provides modern Python ergonomics while maintaining AUTOSAR compatibility. Internal camelCase storage matches XML serialization needs. Delegation ensures DRY principle and single source of truth for validation logic.

**References**:
- Python @property decorator pattern
- Design Document: `docs/plans/2026-02-07-v2-redesign-easier-to-use.md`
- Pydantic-style field access patterns

---

### CODING_RULE_V2_00017: AUTOSAR Method Compatibility Layer

**Maturity**: accept

**Scope**: All V2 model classes

**Description**: All V2 model classes MUST maintain AUTOSAR-compatible getter/setter methods alongside Pythonic properties. AUTOSAR methods MUST delegate to properties to avoid duplication and ensure consistent validation.

**Example:**
```python
# CORRECT - AUTOSAR methods delegate to properties
@dataclass
class ApplicationSwComponentType(ARObject):
    _shortName: str = field(default="", init=False, repr=False)

    @property
    def short_name(self) -> str:
        return self._shortName

    @short_name.setter
    def short_name(self, value: str) -> None:
        # Validation here
        self._shortName = value

    # AUTOSAR compatibility layer (delegates to property)
    def getShortName(self) -> str:
        """AUTOSAR-compliant getter."""
        return self.short_name

    def setShortName(self, value: str) -> "ApplicationSwComponentType":
        """AUTOSAR-compliant setter with method chaining."""
        self.short_name = value  # Gets validation from property
        return self

# WRONG - Duplicate validation logic
def getShortName(self) -> str:
    return self._shortName

def setShortName(self, value: str) -> "ApplicationSwComponentType":
    if not isinstance(value, str):  # Duplicate validation!
        raise TypeError(...)
    self._shortName = value
    return self
```

**Requirements:**

1. **Getter Methods**: MUST return value from property (no direct `_attribute` access)
   ```python
   def getShortName(self) -> str:
       return self.short_name  # ✓ Delegates to property
   ```

2. **Setter Methods**: MUST set via property (gets validation automatically)
   ```python
   def setShortName(self, value: str) -> "ApplicationSwComponentType":
       self.short_name = value  # ✓ Gets validation from property setter
       return self  # ✓ Returns self for chaining
   ```

3. **Method Chaining**: All AUTOSAR setters MUST return `self` for method chaining
   ```python
   component.setShortName("x").setCategory("y")  # Must work
   ```

4. **Documentation**: AUTOSAR methods MUST be documented as "AUTOSAR-compatibility" methods

5. **No Logic Duplication**: AUTOSAR methods MUST NOT contain validation or business logic (delegate to properties)

**Rationale**: Maintaining AUTOSAR methods ensures backward compatibility with existing code, AUTOSAR tools, and the AUTOSAR standard. Delegation to properties avoids code duplication and ensures consistent validation across both APIs. Method chaining preserves existing fluent patterns.

**References**:
- Backward compatibility principles
- Design Document: `docs/plans/2026-02-07-v2-redesign-easier-to-use.md`
- Section 5: Migration Strategy and Backward Compatibility

---

### CODING_RULE_V2_00018: Validation in Property Setters

**Maturity**: accept

**Scope**: All V2 model class property setters

**Description**: All property setters MUST perform validation before setting internal attribute values. Validation MUST happen eagerly (at set time) and provide clear, actionable error messages.

**Example:**
```python
# CORRECT - Validation in property setter
@property
def short_name(self) -> str:
    """Get short name (Pythonic accessor)."""
    return self._shortName

@short_name.setter
def short_name(self, value: str) -> None:
    """
    Set short name with validation.

    Args:
        value: The short name to set

    Raises:
        TypeError: If value is not a string
        ValueError: If value is empty or has invalid format
    """
    # Type check
    if not isinstance(value, str):
        raise TypeError(
            f"short_name must be str, got {type(value).__name__}"
        )

    # Lightweight validation: non-empty
    if not value:
        raise ValueError("short_name cannot be empty")

    # Format validation
    if not self.SHORT_NAME_PATTERN.match(value):
        raise ValueError(
            f"short_name '{value}' must start with letter and contain "
            f"only letters, digits, underscores"
        )

    # All checks passed - set value
    self._shortName = value

# WRONG - No validation
@short_name.setter
def short_name(self, value: str) -> None:
    self._shortName = value  # No validation!
```

**Validation Requirements:**

1. **Type Checking**: Validate input type matches expected type
   ```python
   if not isinstance(value, str):
       raise TypeError(f"short_name must be str, got {type(value).__name__}")
   ```

2. **Required Field Validation**: Check for empty/None values
   ```python
   if not value:
       raise ValueError("short_name cannot be empty")
   ```

3. **Format Validation**: Validate string formats, patterns, ranges
   ```python
   if not self.SHORT_NAME_PATTERN.match(value):
       raise ValueError(f"Invalid format: {value}")
   ```

4. **Enum Validation**: Validate against allowed values
   ```python
   if value not in self.VALID_CATEGORIES:
       raise ValueError(f"category must be one of {self.VALID_CATEGORIES}")
   ```

5. **Error Message Quality**: Error messages MUST be:
   - **Context-Rich**: Include class name, field name, and actual value
   - **Actionable**: Tell user what's allowed
   - **Type-Aware**: Show expected vs actual types

   ```
   ✓ Good: "SwComponentType: short_name '123foo' must start with letter"
   ✗ Bad: "Invalid short name"
   ```

6. **Validation Constants**: Define validation patterns as class constants
   ```python
   SHORT_NAME_PATTERN = re.compile(r'^[A-Za-z][A-Za-z0-9_]*$')
   VALID_CATEGORIES = ['APPLICATION', 'COMPOSITION', 'SENSOR_ACTUATOR']
   ```

**Three-Tier Validation Strategy:**

| Tier | When | Cost | Examples |
|------|------|------|----------|
| **Property Setter** | Every attribute set | Low (μs) | Type checks, format, empty |
| **`__post_init__`** | After construction | Low (ms) | Required fields, critical |
| **`validate()`** | Explicit call | High (s) | Cross-field, business rules |

**Rationale**: Eager validation in property setters catches errors early, provides clear feedback, and prevents invalid state. Property-based validation ensures both Pythonic and AUTOSAR APIs get consistent validation. Three-tier strategy balances performance with thoroughness.

**References**:
- Fail-fast principle
- Design Document: `docs/plans/2026-02-07-v2-redesign-easier-to-use.md`
- Section 4: Validation Framework and Error Handling

---

### CODING_RULE_V2_00019: Fluent `with_` Methods for Chained Assignment

**Maturity**: accept

**Scope**: All V2 model classes

**Description**: All V2 model classes MUST provide `with_<attribute>` methods for fluent chained assignment. Each `with_` method MUST set the attribute via the property setter (to get validation) and return `self` for chaining.

**Example:**
```python
# CORRECT - Fluent with_ methods
@dataclass
class ApplicationSwComponentType(ARObject):
    _shortName: str = field(default="", init=False, repr=False)
    _category: Optional[str] = field(default=None, init=False, repr=False)

    # Properties (from CODING_RULE_V2_00016)
    @property
    def short_name(self) -> str:
        return self._shortName

    @short_name.setter
    def short_name(self, value: str) -> None:
        # Validation from CODING_RULE_V2_00018
        self._shortName = value

    # Fluent with_ methods
    def with_short_name(self, value: str) -> "ApplicationSwComponentType":
        """
        Set short_name and return self for chaining.

        Args:
            value: The short name to set

        Returns:
            self for method chaining

        Example:
            >>> component.with_short_name("MyComp").with_category("APPLICATION")
        """
        self.short_name = value  # Use property setter (gets validation)
        return self

    def with_category(self, value: str) -> "ApplicationSwComponentType":
        """Set category and return self for chaining."""
        self.category = value  # Use property setter
        return self

# Usage
component = (ApplicationSwComponentType()
             .with_short_name("MyComponent")
             .with_category("APPLICATION")
             .with_uuid("12345"))

# WRONG - No with_ methods or incorrect implementation
def with_short_name(self, value: str) -> None:
    self._shortName = value  # No return value, can't chain!
```

**Requirements:**

1. **Method Naming**: All fluent methods MUST use `with_<attribute_name>` pattern (snake_case)

2. **Return Type**: All `with_` methods MUST return `self` for method chaining

3. **Delegation**: `with_` methods MUST set attributes via property setters (not direct `_attribute` access)
   ```python
   def with_short_name(self, value: str) -> "ApplicationSwComponentType":
       self.short_name = value  # ✓ Uses property (gets validation)
       return self
   ```

4. **Type Hints**: `with_` methods MUST have return type hint of `"ClassName"` for chaining

5. **Documentation**: `with_` methods MUST include:
   - Description of chaining behavior
   - Args documentation
   - Returns documentation mentioning `self`
   - Usage example showing chaining

6. **Validation**: `with_` methods automatically get validation from property setters (no duplicate validation needed)

**Optional Attributes:**

For Optional attributes, `with_` methods should accept None:
```python
def with_category(self, value: Optional[str]) -> "ApplicationSwComponentType":
    """Set category (None allowed) and return self for chaining."""
    self.category = value
    return self
```

**Usage Patterns:**

```python
# Single-line chaining
component = (ApplicationSwComponentType()
             .with_short_name("MyComp")
             .with_category("APPLICATION"))

# Multi-line for readability
component = (ApplicationSwComponentType()
             .with_short_name("TemperatureController")
             .with_category("APPLICATION")
             .with_uuid("comp-001"))

# Partial chaining (can continue later)
component = ApplicationSwComponentType().with_short_name("MyComp")
component.with_category("APPLICATION")  # Continue chaining

# Combining with add methods
pkg.add_element(
    ApplicationSwComponentType()
    .with_short_name("MyComp")
    .with_category("APPLICATION")
)
```

**Comparison of Assignment Methods:**

```python
# Method 1: Direct property access
component.short_name = "MyComp"

# Method 2: AUTOSAR setters (existing)
component.setShortName("MyComp")

# Method 3: Fluent with_ methods (NEW - recommended for chaining)
component.with_short_name("MyComp")
```

**Rationale**: Fluent `with_` methods provide clean, readable chaining for object construction. The `with_` prefix clearly indicates intent and follows successful patterns from libraries like SQLAlchemy. Delegation to property setters ensures DRY principle and consistent validation without code duplication.

**References**:
- Fluent interface pattern
- Method chaining pattern
- SQLAlchemy's session construction pattern
- Design Document: `docs/plans/2026-02-07-v2-redesign-easier-to-use.md`
- Section 9: Chained Assignment with `with_` Methods

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

---

## Type Hints

### CODING_RULE_TYPE_00001: Mandatory Type Annotations

**Maturity**: accept

**Scope**: All V2 modules

**Description**: All function parameters and return values in V2 modules MUST have type hints.

**Example:**
```python
def get_class(self, name: str) -> Optional[AutosarClass]:
    """Get a class by name."""
    for cls in self.classes:
        if cls.name == name:
            return cls
    return None

def add_subpackage(self, pkg: "AutosarPackage") -> None:
    """Add a subpackage to this package."""
    pkg_names = {p.name for p in self.subpackages}
    if pkg.name in pkg_names:
        raise ValueError(f"Subpackage '{pkg.name}' already exists")
    self.subpackages.append(pkg)
```

**Rationale**: Type hints improve code clarity, enable better IDE support, and catch type errors early.

**References**:
- PEP 484 - Type Hints
- CODING_RULE_V2_00005: Direct Imports for Non-Self Types

---

### CODING_RULE_TYPE_00002: Union Types (Python 3.7+ Compatibility)

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules MUST use `typing.Union` for Python 3.7+ compatibility (project requires >= 3.7).

**Example:**
```python
# Required (Python 3.7+ compatibility):
from typing import Union, Optional

def get_class(self, name: str) -> Optional[AutosarClass]:
    """Get a class by name."""

def get_value(self) -> Union[str, int]:
    """Get value which can be string or int."""
```

**Note**: The `X | Y` syntax is only available in Python 3.10+ and should NOT be used since the project requires Python >= 3.7.

**Rationale**: Python 3.7 compatibility is a project requirement. Using `typing.Union` ensures all supported Python versions work correctly.

**References**:
- pyproject.toml: `requires-python = ">=3.7"`

---

### CODING_RULE_TYPE_00003: Collection Types

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules MUST use imported generics from `typing` module for collection types.

**Example:**
```python
from typing import List, Set, Tuple, Dict

def parse_pdf(self, pdf_path: str) -> List[AutosarPackage]:
    """Parse a PDF file."""

def process_names(self, names: Set[str]) -> Tuple[str, int]:
    """Process unique names."""

def build_map(self) -> Dict[str, AutosarPackage]:
    """Build a package map."""
```

**Rationale**: Using typing module generics provides better type checking and IDE support.

**References**:
- PEP 484 - Type Hints

---

### CODING_RULE_TYPE_00004: Forward References

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules MUST use string literals for circular dependencies (see CODING_RULE_V2_00002 for TYPE_CHECKING usage).

**Example:**
```python
from dataclasses import dataclass, field

@dataclass
class AutosarPackage:
    name: str
    subpackages: List["AutosarPackage"] = field(default_factory=list)

def get_subpackage(self, name: str) -> Optional["AutosarPackage"]:
    """Get a subpackage by name."""
```

**Rationale**: String annotations allow forward references to avoid circular imports while maintaining type safety.

**References**:
- PEP 484 - Forward References
- CODING_RULE_V2_00002: TYPE_CHECKING for Self-Referencing Return Types

---

### CODING_RULE_TYPE_00005: Dataclass Field Types

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules MUST use `field(default_factory=list)` for mutable defaults in dataclasses.

**Example:**
```python
from dataclasses import dataclass, field

@dataclass
class AutosarPackage:
    name: str
    classes: List[AutosarClass] = field(default_factory=list)
    subpackages: List["AutosarPackage"] = field(default_factory=list)
```

**Rationale**: Using `default_factory` prevents mutable default value sharing between instances.

**References**:
- PEP 557 - Data Classes

---

## Docstrings

### CODING_RULE_DOC_00001: Google-Style Docstrings

**Maturity**: accept

**Scope**: All V2 modules

**Description**: All public classes, methods, and functions in V2 modules MUST have Google-style docstrings.

**Example:**
```python
class SwComponentType(Identifiable):
    """Represents a software component type.

    Attributes:
        short_name: The short name of the component.
        category: The component category.

    Examples:
        >>> comp = SwComponentType()
        >>> comp.short_name = "MyComponent"
    """

    def get_ports(self) -> List[PPortPrototype]:
        """Get all ports of this component.

        Returns:
            List of port prototypes.
        """
```

**Rationale**: Google-style docstrings provide consistent, readable documentation format.

**References**:
- PEP 257 - Docstring Conventions
- Google Python Style Guide

---

### CODING_RULE_DOC_00002: Class Docstrings

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 class docstrings MUST include: Description, Attributes, Examples

**Example:**
```python
@dataclass
class AutosarClass:
    """Represents an AUTOSAR class.

    Attributes:
        name: The name of the class.
        is_abstract: Whether the class is abstract.

    Examples:
        >>> cls = AutosarClass("RunnableEntity", False)
    """
```

**Rationale**: Complete class documentation helps users understand the purpose and usage of the class.

**References**:
- PEP 257 - Docstring Conventions

---

### CODING_RULE_DOC_00003: Method Docstrings

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 method docstrings MUST include: Description, Args, Returns, Raises (if applicable)

**Example:**
```python
def add_class(self, cls: AutosarClass) -> None:
    """Add a class to the package.

    Args:
        cls: The AutosarClass to add.

    Raises:
        ValueError: If a class with the same name already exists.
    """
```

**Rationale**: Complete method documentation helps users understand the method's purpose, parameters, return value, and exceptions.

**References**:
- PEP 257 - Docstring Conventions

---

### CODING_RULE_DOC_00004: Docstring Language

**Maturity**: accept

**Scope**: All V2 modules

**Description**: All docstrings in V2 modules MUST be in English.

**Rationale**: English is the universal language for technical documentation, ensuring broad accessibility.

**References**:
- PEP 257 - Docstring Conventions

---

## Whitespace

### CODING_RULE_WS_00001: Avoid Extraneous Whitespace

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules MUST avoid extraneous whitespace per PEP 8.

**Example:**
```python
# Correct
spam(ham[1], {eggs: 2})

# Wrong
spam( ham[ 1 ], { eggs: 2 } )
```

**Rationale**: Proper whitespace improves code readability.

**References**:
- PEP 8 - Whitespace in Expressions

---

### CODING_RULE_WS_00002: Whitespace Around Operators

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules MUST surround binary operators with single space.

**Example:**
```python
# Correct
i = i + 1
x = x * 2 - 1

# Wrong
i=i+1
x = x * 2 - 1
```

**Rationale**: Consistent spacing improves readability.

**References**:
- PEP 8 - Whitespace in Expressions

---

### CODING_RULE_WS_00003: Keyword Arguments

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules MUST NOT use spaces around `=` in keyword arguments.

**Example:**
```python
# Correct
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# Wrong
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```

**Rationale**: PEP 8 standard for keyword arguments.

**References**:
- PEP 8 - Other Recommendations

---

### CODING_RULE_WS_00004: Function Annotations

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules MUST use spaces around `->` arrow in function annotations.

**Example:**
```python
# Correct
def munge(input: AnyStr) -> AnyStr:
    pass

# Wrong
def munge(input:AnyStr):
    pass
```

**Rationale**: PEP 8 standard for function annotations.

**References**:
- PEP 8 - Function Annotations

---

### CODING_RULE_WS_00005: Trailing Whitespace

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules MUST NOT have trailing whitespace.

**Rationale**: Trailing whitespace can cause issues with version control and is unnecessary.

**References**:
- PEP 8 - Whitespace in Expressions

---

### CODING_RULE_WS_00006: Compound Statements

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules MUST avoid compound statements (multiple statements on same line).

**Example:**
```python
# Correct
if foo == 'blah':
    do_blah_thing()
do_one()

# Wrong
if foo == 'blah': do_blah_thing()
do_one(); do_two()
```

**Rationale**: One statement per line improves readability.

**References**:
- PEP 8 - Other Recommendations

---

## Error Handling

### CODING_RULE_ERROR_00001: Validation Errors

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules MUST use `ValueError` for invalid arguments.

**Example:**
```python
def add_class(self, cls: AutosarClass) -> None:
    """Add a class to the package."""
    class_names = {c.name for c in self.classes}
    if cls.name in class_names:
        raise ValueError(f"Class '{cls.name}' already exists in package '{self.name}'")
    self.classes.append(cls)
```

**Rationale**: ValueError is the appropriate exception for invalid argument values.

**References**:
- Python Exception Hierarchy

---

### CODING_RULE_ERROR_00002: Immediate Validation

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules MUST validate inputs immediately and raise errors.

**Example:**
```python
def __post_init__(self) -> None:
    """Validate the package fields."""
    if not self.name or not self.name.strip():
        raise ValueError("Package name cannot be empty")
```

**Rationale**: Fail fast - validate inputs as early as possible.

**References**:
- Python Validation Patterns

---

### CODING_RULE_ERROR_00003: Exception Chaining

**Maturity**: accept

**Scope**: All V2 modules

**Description**: V2 modules MUST use `raise ... from e` to preserve exception context.

**Example:**
```python
try:
    with open(file_path) as f:
        data = f.read()
except Exception as e:
    raise Exception(f"Failed to read file: {e}") from e
```

**Rationale**: Exception chaining preserves the original exception context for debugging.

**References**:
- PEP 3134 - Exception Chaining

---

## Testing

### CODING_RULE_TEST_00001: Test Structure

**Maturity**: accept

**Scope**: V2 tests

**Description**: V2 tests MUST mirror source structure in `tests/test_armodel/v2/`.

**Example:**
```
tests/test_armodel/v2/
├── __init__.py
├── test_model_extensibility.py
├── integration/
│   └── test_roundtrip.py
├── models/
│   └── test_*.py
├── reader/
│   └── test_*.py
└── writer/
    └── test_*.py
```

**Rationale**: Consistent test structure makes tests easy to find and maintain.

**References**:
- pytest documentation

---

### CODING_RULE_TEST_00002: Test Coverage Goals

**Maturity**: accept

**Scope**: V2 tests

**Description**: V2 tests MUST target high coverage for all V2 modules.

**Requirements:**
- Test success paths, error paths, and edge cases
- Test nested structures and complex scenarios

**Rationale**: High coverage ensures code quality and reliability.

**References**:
- pytest-cov documentation

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
- Design Document: `docs/plans/2025-02-05-models-v2-design.md` - Original V2 design
- Design Document: `docs/plans/2026-02-07-v2-arxml-reader-writer-design.md` - V2 reader/writer design
- Design Document: `docs/plans/2026-02-07-v2-redesign-easier-to-use.md` - V2 redesign for usability

---

## Related Documentation

- [General Coding Rules](coding_rules.md) - Project-wide coding standards
- [AGENTS.md](../../AGENTS.md) - Agent guidelines and V2 overview
- [CLAUDE.md](../../CLAUDE.md) - Project guidance for Claude Code
- [V2 Models Design](../../plans/2025-02-05-models-v2-design.md) - Original V2 architecture design
- [V2 Reader/Writer Design](../../plans/2026-02-07-v2-arxml-reader-writer-design.md) - V2 reader/writer design
- [V2 Redesign for Usability](../../plans/2026-02-07-v2-redesign-easier-to-use.md) - V2 redesign to make models easier to use