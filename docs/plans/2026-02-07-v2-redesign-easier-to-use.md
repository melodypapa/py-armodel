# V2 Models Redesign: Easier to Use

**Date**: 2026-02-07
**Status**: Design Approved
**Author**: AI Assistant (Claude Code)
**Related Documents**:
- `docs/development/coding_rules_v2.md` - V2 coding standards
- `docs/development/v2_migration_guide.md` - V1 to V2 migration guide

---

## Executive Summary

This document outlines the redesign of V2 AUTOSAR models to make them significantly easier to use for building AUTOSAR models and generating ARXML files. The redesign introduces modern Python patterns while maintaining full backward compatibility with existing AUTOSAR APIs.

**Key Goals:**
1. ✅ Reduce code verbosity (3-5x shorter)
2. ✅ Improve IDE support (autocomplete, type hints)
3. ✅ Provide clear, actionable error messages
4. ✅ Maintain 100% backward compatibility
5. ✅ Follow successful Python project best practices (Pydantic, SQLAlchemy, dataclasses)

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Class Design and Implementation](#2-class-design-and-implementation)
3. [Parent-Child Relationships and Collections](#3-parent-child-relationships-and-collections)
4. [Validation Framework and Error Handling](#4-validation-framework-and-error-handling)
5. [Migration Strategy and Backward Compatibility](#5-migration-strategy-and-backward-compatibility)
6. [Testing Strategy](#6-testing-strategy)
7. [Implementation Plan](#7-implementation-plan)
8. [Documentation Strategy](#8-documentation-strategy)
9. [Chained Assignment with `with_` Methods](#9-chained-assignment-with-with_-methods)
10. [Summary and Next Steps](#10-summary-and-next-steps)

---

## 1. Architecture Overview

The redesigned V2 models will follow a **hybrid architecture** that provides:

1. **Dual API Layer**: Every AUTOSAR attribute exposes both:
   - **Pythonic snake_case attributes** for modern code: `component.short_name`
   - **AUTOSAR camelCase methods** for spec compliance: `component.getShortName()`

2. **Property-Based Implementation**: Use Python `@property` decorators to bridge snake_case attributes to internal camelCase storage, maintaining compatibility while providing clean syntax.

3. **Enhanced Dataclasses**: Build on the current dataclass foundation with:
   - `__post_init__` validation (eager validation)
   - Type hints on all attributes for IDE/mypy support
   - Custom `__init__` accepting keyword arguments
   - Automatic parent management in add methods

4. **Validation Framework**:
   - Lightweight validation in `__post_init__` (type checks, required fields)
   - Full validation in setter methods (constraint checking)
   - Clear, actionable error messages

5. **Backward Compatibility**: Keep all existing AUTOSAR methods as a compatibility layer, deprecating gradually over major versions.

### Example of the Hybrid Approach

```python
# Modern Pythonic usage
component = ApplicationSwComponentType(
    short_name='MyComponent',
    uuid='12345'
)
component.short_name  # Direct attribute access
component.short_name = 'NewComponent'  # Direct setting

# AUTOSAR-compliant usage (still works)
component.getShortName()  # Returns 'NewComponent'
component.setShortName('AnotherComponent')  # Works too

# Fluent chaining with with_ methods (NEW)
component = (ApplicationSwComponentType()
             .with_short_name('MyComponent')
             .with_uuid('12345')
             .with_category('APPLICATION'))
```

---

## 2. Class Design and Implementation

### Core Design Pattern

Each V2 model class will use **property-based dual access** with internal storage following AUTOSAR naming conventions:

```python
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class ApplicationSwComponentType(ARObject):
    # Internal storage (AUTOSAR camelCase naming)
    _shortName: str = field(default="", init=False, repr=False)
    _uuid: Optional[str] = field(default=None, init=False, repr=False)

    # Pythonic snake_case properties
    @property
    def short_name(self) -> str:
        """Get the short name (Pythonic accessor)."""
        return self._shortName

    @short_name.setter
    def short_name(self, value: str) -> None:
        """Set the short name with validation."""
        if not value:
            raise ValueError("short_name cannot be empty")
        self._shortName = value

    @property
    def uuid(self) -> Optional[str]:
        """Get the UUID (Pythonic accessor)."""
        return self._uuid

    @uuid.setter
    def uuid(self, value: Optional[str]) -> None:
        """Set the UUID with validation."""
        if value is not None and not self._validate_uuid(value):
            raise ValueError(f"Invalid UUID format: {value}")
        self._uuid = value

    # AUTOSAR-compliant methods (compatibility layer)
    def getShortName(self) -> str:
        """AUTOSAR-compliant getter."""
        return self.short_name

    def setShortName(self, value: str) -> "ApplicationSwComponentType":
        """AUTOSAR-compliant setter with method chaining."""
        self.short_name = value
        return self  # Enable chaining

    def getUUID(self) -> Optional[str]:
        """AUTOSAR-compliant getter."""
        return self.uuid

    def setUUID(self, value: str) -> "ApplicationSwComponentType":
        """AUTOSAR-compliant setter."""
        self.uuid = value
        return self
```

### Key Implementation Details

1. **Internal Naming**: All internal attributes use AUTOSAR camelCase (`_shortName`, `_uuid`) to match XML serialization needs

2. **Property Decorators**: Expose snake_case properties that map to internal storage, providing validation and type safety

3. **Method Chaining**: AUTOSAR setters return `self` to support existing chaining patterns: `obj.setShortName("x").setUUID("y")`

4. **Type Hints**: Full type annotations on properties and methods for IDE autocomplete and mypy checking

5. **Constructor Enhancement**: Custom `__init__` accepts keyword arguments:
```python
def __init__(self, **kwargs):
    """Initialize with keyword arguments."""
    for key, value in kwargs.items():
        if hasattr(self, key):
            setattr(self, key, value)
    self._validate_abstract()
```

### Validation Strategy

- **Property setters**: Lightweight validation (non-empty, format checks)
- **`__post_init__`**: Required field validation
- **Explicit `validate()` method**: Full constraint validation (optional, for complex rules)

---

## 3. Parent-Child Relationships and Collections

### Collection Management Pattern

Based on your choice of explicit add methods, we'll enhance the current V2 pattern with automatic parent management and validation:

```python
from typing import List, Optional, TypeVar

T = TypeVar('T', bound='ARObject')

@dataclass
class ARPackage(ARObject):
    # Internal storage
    _arPackages: List['ARPackage'] = field(default_factory=list, init=False, repr=False)
    _elements: List['ARObject'] = field(default_factory=list, init=False, repr=False)

    # Pythonic property accessors
    @property
    def ar_packages(self) -> List['ARPackage']:
        """Get child packages (Pythonic accessor)."""
        return self._arPackages

    @property
    def elements(self) -> List['ARObject']:
        """Get elements (Pythonic accessor)."""
        return self._elements

    # Explicit add methods (V2 style enhanced)
    def addARPackage(self, package: 'ARPackage') -> 'ARPackage':
        """
        Add a child package.

        Args:
            package: The package to add

        Returns:
            self for method chaining

        Raises:
            ValueError: If package is None or already has a parent
            TypeError: If package is not an ARPackage
        """
        if package is None:
            raise ValueError("package cannot be None")

        if not isinstance(package, ARPackage):
            raise TypeError(f"Expected ARPackage, got {type(package).__name__}")

        if package.parent is not None:
            raise ValueError(f"Package already has parent: {package.parent}")

        self._arPackages.append(package)
        package._parent = self  # Set parent automatically
        return self

    def addElement(self, element: 'ARObject') -> 'ARPackage':
        """
        Add an element to this package.

        Args:
            element: The element to add

        Returns:
            self for method chaining

        Raises:
            ValueError: If element is None or already has a parent
            TypeError: If element is not an ARObject
        """
        if element is None:
            raise ValueError("element cannot be None")

        if not isinstance(element, ARObject):
            raise TypeError(f"Expected ARObject, got {type(element).__name__}")

        if element.parent is not None:
            raise ValueError(f"Element already has parent: {element.parent}")

        self._elements.append(element)
        element._parent = self  # Set parent automatically
        return self

    # Convenience methods (Pythonic aliases)
    def add_package(self, package: 'ARPackage') -> 'ARPackage':
        """Pythonic alias for addARPackage."""
        return self.addARPackage(package)

    def add_element(self, element: 'ARObject') -> 'ARPackage':
        """Pythonic alias for addElement."""
        return self.addElement(element)

    # AUTOSAR-compliant getters
    def getARPackages(self) -> List['ARPackage']:
        """AUTOSAR-compliant getter."""
        return self._arPackages

    def getElements(self) -> List['ARObject']:
        """AUTOSAR-compliant getter."""
        return self._elements
```

### Key Features

1. **Automatic Parent Management**: Adding a child automatically sets `child._parent`, eliminating manual parent assignment

2. **Validation in Add Methods**:
   - Type checking (isinstance checks)
   - Duplicate parent prevention
   - None value checks

3. **Method Chaining**: All add methods return `self` for fluent API:
   ```python
   pkg.add_package(child1).add_package(child2).add_element(elem)
   ```

4. **Dual Naming**: Both `addARPackage()` (AUTOSAR) and `add_package()` (Pythonic) provided

5. **Property Accessors**: Read-only access to collections via `@property` decorators (prevent direct list manipulation)

---

## 4. Validation Framework and Error Handling

### Three-Tier Validation Strategy

Based on your choice of eager validation, we'll implement validation at three levels:

```python
from dataclasses import dataclass
from typing import Optional, List
import re

@dataclass
class SwComponentType(ARObject):
    # Internal storage
    _shortName: str = field(default="", init=False, repr=False)
    _category: Optional[str] = field(default=None, init=False, repr=False)

    # Validation constants
    SHORT_NAME_PATTERN = re.compile(r'^[A-Za-z][A-Za-z0-9_]*$')
    VALID_CATEGORIES = ['APPLICATION', 'COMPOSITION', 'SENSOR_ACTUATOR']

    def __post_init__(self) -> None:
        """
        Lightweight validation after construction.
        Validates only critical required fields.

        Raises:
            ValueError: If required fields are missing or invalid
        """
        # Critical validation: short_name must be set
        if not self._shortName:
            raise ValueError("SwComponentType: short_name is required")

        # Critical validation: short_name format
        if not self.SHORT_NAME_PATTERN.match(self._shortName):
            raise ValueError(
                f"SwComponentType: short_name '{self._shortName}' must start with "
                f"letter and contain only letters, digits, underscores"
            )

        # Call parent validation
        super().__post_init__()

    @property
    def short_name(self) -> str:
        """Get short name (Pythonic accessor)."""
        return self._shortName

    @short_name.setter
    def short_name(self, value: str) -> None:
        """
        Set short name with immediate validation.

        Args:
            value: The short name to set

        Raises:
            ValueError: If value is empty or invalid format
            TypeError: If value is not a string
        """
        # Type check
        if not isinstance(value, str):
            raise TypeError(
                f"short_name must be str, got {type(value).__name__}"
            )

        # Lightweight validation: non-empty
        if not value:
            raise ValueError("short_name cannot be empty")

        # Lightweight validation: format check
        if not self.SHORT_NAME_PATTERN.match(value):
            raise ValueError(
                f"short_name '{value}' must start with letter and contain "
                f"only letters, digits, underscores"
            )

        # All checks passed - set value
        self._shortName = value

    @property
    def category(self) -> Optional[str]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional[str]) -> None:
        """
        Set category with validation.

        Args:
            value: The category to set (or None)

        Raises:
            ValueError: If value is not a valid category
        """
        if value is None:
            self._category = None
            return

        if not isinstance(value, str):
            raise TypeError(
                f"category must be str or None, got {type(value).__name__}"
            )

        # Lightweight validation: enum check
        if value not in self.VALID_CATEGORIES:
            raise ValueError(
                f"category '{value}' must be one of {self.VALID_CATEGORIES}"
            )

        self._category = value

    def validate(self) -> List[str]:
        """
        Perform full constraint validation.
        Use this for complex cross-field validations that are too expensive for setters.

        Returns:
            List of validation error messages (empty if valid)

        Example:
            errors = component.validate()
            if errors:
                for error in errors:
                    print(f"Validation error: {error}")
        """
        errors: List[str] = []

        # Complex validation: check category consistency
        if self._category == 'APPLICATION' and hasattr(self, 'requiresPort'):
            if not self.requiresPort:
                errors.append("APPLICATION component requires at least one port")

        # Add more complex validations here...

        return errors
```

### Error Message Design Principles

1. **Context-Rich Messages**: Include class name, field name, and actual value
   ```
   ✓ Good: "SwComponentType: short_name '123foo' must start with letter"
   ✗ Bad: "Invalid short name"
   ```

2. **Actionable Guidance**: Tell user what's allowed
   ```
   ✓ Good: "category 'INVALID' must be one of ['APPLICATION', 'COMPOSITION', 'SENSOR_ACTUATOR']"
   ✗ Bad: "Invalid category"
   ```

3. **Type Information**: Show expected vs actual types
   ```
   ✓ Good: "short_name must be str, got int"
   ✗ Bad: "Type error"
   ```

### Validation Levels Summary

| Level | When | Cost | Examples |
|-------|------|------|----------|
| **Property Setter** | Every attribute set | Low (microseconds) | Type checks, format validation, empty checks |
| **`__post_init__`** | After construction | Low (milliseconds) | Required fields, critical validations |
| **`validate()`** | Explicit call (optional) | High (seconds) | Cross-field constraints, business rules, referential integrity |

---

## 5. Migration Strategy and Backward Compatibility

### Phased Migration Approach

We'll migrate the existing V2 models incrementally without breaking existing code:

**Phase 1: Foundation (No Breaking Changes)**
- Add `@property` decorators alongside existing getter/setter methods
- Keep all existing AUTOSAR methods unchanged
- Add new Pythonic properties as additional accessors
- No changes to existing behavior

**Phase 2: Enhanced Validation (Gradual)**
- Add validation to property setters
- Add `__post_init__` validation
- Keep existing setters working (they delegate to properties)
- Add deprecation warnings for old patterns if needed

**Phase 3: Constructor Enhancement (Backward Compatible)**
- Add custom `__init__` accepting keyword arguments
- Still support empty constructor + setters pattern
- Ensure all existing code continues to work

**Phase 4: Documentation and Examples**
- Update docs to show Pythonic usage as primary
- Keep AUTOSAR examples for compatibility
- Provide migration guide for V2 users

### Implementation Example: Migration

```python
# Before (Current V2 - existing code)
@dataclass
class SwComponentType(ARObject):
    _shortName: str = ""

    def getShortName(self) -> str:
        return self._shortName

    def setShortName(self, value: str) -> "SwComponentType":
        self._shortName = value
        return self

# After (Migrated V2 - backward compatible)
@dataclass
class SwComponentType(ARObject):
    _shortName: str = field(default="", init=False, repr=False)

    # ===== NEW: Pythonic properties =====
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

    # ===== EXISTING: AUTOSAR methods (unchanged API) =====
    def getShortName(self) -> str:
        """AUTOSAR-compliant getter."""
        # Now delegates to property (DRY principle)
        return self.short_name

    def setShortName(self, value: str) -> "SwComponentType":
        """AUTOSAR-compliant setter."""
        # Delegates to property setter (gets validation)
        self.short_name = value
        return self
```

### Backward Compatibility Guarantees

| Existing Pattern | Still Works? | Notes |
|-----------------|--------------|-------|
| `obj.setShortName("x")` | ✅ Yes | Delegates to property setter |
| `name = obj.getShortName()` | ✅ Yes | Delegates to property getter |
| `obj._shortName = "x"` | ✅ Yes | Direct access still works (but discouraged) |
| Chaining: `obj.setShortName("x").setUUID("y")` | ✅ Yes | Returns `self` unchanged |
| Empty constructor: `obj = SwComponentType()` | ✅ Yes | Then use setters |

### New Patterns Enabled

```python
# NEW: Direct property access
component.short_name = "MyComponent"  # Pythonic
name = component.short_name

# NEW: Constructor with keyword arguments
component = SwComponentType(
    short_name="MyComponent",
    category="APPLICATION"
)

# NEW: Type hints and IDE autocomplete
component.short_name  # IDE knows this is str
```

---

## 6. Testing Strategy

### Test-Driven Development (TDD) Approach

Following your requirement for TDD methodology, we'll write tests before implementation:

```python
# tests/test_armodel/v2/models/M2/AUTOSARTemplates/SWComponentTemplate/test_application_sw_component_type.py

import pytest
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate import ApplicationSwComponentType

class TestApplicationSwComponentTypeProperties:
    """Test Pythonic property access (NEW in redesigned V2)."""

    def test_short_name_property_getter(self):
        """Test short_name property getter returns value."""
        component = ApplicationSwComponentType()
        component._shortName = "TestComponent"
        assert component.short_name == "TestComponent"

    def test_short_name_property_setter_valid(self):
        """Test short_name property setter accepts valid value."""
        component = ApplicationSwComponentType()
        component.short_name = "ValidName"
        assert component._shortName == "ValidName"

    def test_short_name_property_setter_empty_raises(self):
        """Test short_name property setter rejects empty string."""
        component = ApplicationSwComponentType()
        with pytest.raises(ValueError, match="short_name cannot be empty"):
            component.short_name = ""

    def test_short_name_property_setter_invalid_format_raises(self):
        """Test short_name property setter rejects invalid format."""
        component = ApplicationSwComponentType()
        with pytest.raises(ValueError, match="must start with letter"):
            component.short_name = "123Invalid"

    def test_short_name_property_setter_type_error(self):
        """Test short_name property setter rejects non-string."""
        component = ApplicationSwComponentType()
        with pytest.raises(TypeError, match="short_name must be str"):
            component.short_name = 123

class TestApplicationSwComponentTypeAutosarMethods:
    """Test AUTOSAR method compatibility (EXISTING V2 API)."""

    def test_getShortName_returns_value(self):
        """Test getShortName() method returns value."""
        component = ApplicationSwComponentType()
        component._shortName = "TestComponent"
        assert component.getShortName() == "TestComponent"

    def test_setShortName_sets_value_and_returns_self(self):
        """Test setShortName() method sets value and returns self for chaining."""
        component = ApplicationSwComponentType()
        result = component.setShortName("TestComponent")
        assert component._shortName == "TestComponent"
        assert result is component  # Method chaining

    def test_setShortName_delegates_to_property(self):
        """Test setShortName() delegates to property setter (gets validation)."""
        component = ApplicationSwComponentType()
        with pytest.raises(ValueError, match="short_name cannot be empty"):
            component.setShortName("")  # Should trigger property validation

class TestBackwardCompatibility:
    """Ensure existing V2 code patterns still work."""

    def test_existing_setter_pattern_works(self):
        """Test existing setter pattern still works."""
        component = ApplicationSwComponentType()
        component.setShortName("TestComp").setUUID("12345")
        assert component.short_name == "TestComp"
        assert component.uuid == "12345"

    def test_existing_getter_pattern_works(self):
        """Test existing getter pattern still works."""
        component = ApplicationSwComponentType()
        component._shortName = "TestComp"
        name = component.getShortName()
        assert name == "TestComp"
```

### Test Organization

```
tests/test_armodel/v2/models/
├── M2/
│   ├── AUTOSARTemplates/
│   │   ├── SWComponentTemplate/
│   │   │   ├── test_application_sw_component_type.py
│   │   │   ├── test_composition_sw_component_type.py
│   │   │   └── ...
│   │   ├── CommonStructure/
│   │   │   ├── test_ar_object.py
│   │   │   └── ...
│   │   └── ...
│   └── MSR/
│       └── ...
├── test_property_access.py           # Test property pattern
├── test_autosar_compatibility.py     # Test AUTOSAR method compatibility
├── test_validation.py                # Test validation framework
└── test_backward_compatibility.py    # Ensure existing code works
```

### Test Coverage Goals

| Category | Target Coverage | Notes |
|----------|----------------|-------|
| Property getters/setters | 100% | New Pythonic API |
| AUTOSAR methods | 100% | Compatibility layer |
| Validation logic | 100% | Critical for correctness |
| Parent-child relationships | 100% | Core AUTOSAR feature |
| Constructor with kwargs | 100% | New convenience feature |
| Error messages | 90%+ | Verify quality of error output |

---

## 7. Implementation Plan

### Implementation Phases

We'll implement the redesign incrementally, module by module, following TDD principles:

**Phase 1: Core Infrastructure (Foundation)**
- Duration: 1-2 weeks
- Files to modify:
  - `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py`
  - `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Referrable.py`
  - `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py`

Deliverables:
- Base classes with `@property` decorators
- Validation framework in place
- Tests for core functionality passing

**Phase 2: CommonStructure Module**
- Duration: 1-2 weeks
- High-priority, widely-used module
- Apply pattern to: ServiceNeeds, Implementation, InternalBehavior, etc.
- Each class: Test → Implement → Verify

**Phase 3: SWComponentTemplate Module**
- Duration: 2-3 weeks
- Critical for software component modeling
- Apply pattern to all component types and port interfaces
- High impact on usability

**Phase 4: SystemTemplate and BswModuleTemplate**
- Duration: 2 weeks each
- Apply same pattern systematically

**Phase 5: MSR Modules (Documentation, DataDictionary, etc.)**
- Duration: 1-2 weeks
- Complete the remaining modules

### Development Workflow Per Module

For each module/class, follow this TDD workflow:

```bash
# 1. Create test file (if not exists)
touch tests/test_armodel/v2/models/M2/AUTOSARTemplates/ModuleName/test_class_name.py

# 2. Write failing tests (RED)
# Add tests for new properties, validation, etc.

# 3. Run tests - see them fail
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/ModuleName/test_class_name.py -v

# 4. Implement the changes to make tests pass (GREEN)
# Edit src/armodel/v2/models/M2/AUTOSARTemplates/ModuleName/ClassName.py

# 5. Run tests again - verify they pass
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/ModuleName/test_class_name.py -v

# 6. Run linting
ruff check src/armodel/v2/models/M2/AUTOSARTemplates/ModuleName/ClassName.py

# 7. Run type checking
mypy src/armodel/v2/models/M2/AUTOSARTemplates/ModuleName/ClassName.py

# 8. Run all V2 tests to ensure no regressions
pytest tests/test_armodel/v2/models/ -v

# 9. Commit changes
git add .
git commit -m "feat: Add Pythonic properties to ClassName"
```

### Priority Order for Modules

Based on usage and dependency:

1. **High Priority** (Do first):
   - ✅ ArObject, Referrable, Identifiable (base classes)
   - CommonStructure (widely imported)
   - SWComponentTemplate (core functionality)

2. **Medium Priority**:
   - SystemTemplate (system configuration)
   - BswModuleTemplate (BSW modules)
   - ECUC-related modules

3. **Lower Priority**:
   - MSR modules (Documentation, etc.)
   - Specialized templates

### Quality Gates

Each phase must meet these criteria before proceeding:

```bash
# All tests passing
pytest tests/test_armodel/v2/models/ -v
# Expected: All tests pass

# Ruff check passes
ruff check src/armodel/v2/models/
# Expected: No new errors (current 18 errors acceptable)

# MyPy errors not increased
mypy src/armodel/v2 2>&1 | wc -l
# Expected: Error count <= 4142 (current baseline)

# Test coverage maintained
pytest tests/test_armodel/v2/models/ --cov=armodel.v2.models --cov-report=term-missing
# Expected: Coverage not decreased
```

---

## 8. Documentation Strategy

### Dual API Documentation

We'll document both Pythonic and AUTOSAR APIs, emphasizing Pythonic usage as the primary approach:

```python
class ApplicationSwComponentType(ARObject):
    """
    An AUTOSAR application software component type.

    **Pythonic Usage (Recommended):**

    Create with keyword arguments:

    >>> component = ApplicationSwComponentType(
    ...     short_name="MyComponent",
    ...     category="APPLICATION"
    ... )

    Access attributes directly:

    >>> component.short_name
    'MyComponent'
    >>> component.short_name = "NewComponent"

    **AUTOSAR-Compliant Usage (Also Supported):**

    For compatibility with AUTOSAR tools and existing code:

    >>> component = ApplicationSwComponentType()
    >>> component.setShortName("MyComponent")
    >>> name = component.getShortName()

    **Attributes:**
        short_name (str): The short name of this component (Pythonic property)
        category (str): Component category (APPLICATION/COMPOSITION/etc.)
        uuid (str | None): Unique identifier

    **AUTOSAR Methods:**
        getShortName(): Get short name (AUTOSAR-compliant)
        setShortName(value): Set short name with method chaining
    """
```

### Documentation Locations

**1. Module-Level Documentation**
- Location: `docs/development/v2_user_guide.md` (NEW)
- Content: Getting started guide, Pythonic API examples
- Migration guide from V1 to V2 (already exists: `docs/development/v2_migration_guide.md`)

**2. API Reference**
- Location: Docstrings in each class
- Format: Google-style docstrings
- Include: Pythonic API, AUTOSAR compatibility, examples

**3. Migration Guide**
- Update existing: `docs/development/v2_migration_guide.md`
- Add section: "Migrating to Redesigned V2 (Dual API)"
- Show before/after code examples

**4. Coding Rules**
- Update: `docs/development/coding_rules_v2.md`
- Add rules for property-based access, validation, and `with_` methods

### Documentation Structure

```
docs/
├── development/
│   ├── v2_user_guide.md              (NEW) - Pythonic API guide
│   ├── v2_migration_guide.md         (UPDATE) - Add dual API section
│   ├── coding_rules_v2.md            (UPDATE) - Add property/validation rules
│   └── v2_redesign_design.md         (NEW) - This design document
└── examples/
    ├── v2_pythonic_usage.py          (NEW) - Modern Python examples
    ├── v2_autosar_compatibility.py   (NEW) - AUTOSAR API examples
    └── v2_building_models.py         (NEW) - Complete example building a model
```

---

## 9. Chained Assignment with `with_` Methods

### Fluent API Design

Every attribute will have a corresponding `with_` method that sets the value and returns `self` for chaining:

```python
@dataclass
class ApplicationSwComponentType(ARObject):
    # Internal storage
    _shortName: str = field(default="", init=False, repr=False)
    _category: Optional[str] = field(default=None, init=False, repr=False)
    _uuid: Optional[str] = field(default=None, init=False, repr=False)

    # Properties (from Section 2)
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

    # ===== NEW: Fluent with_ methods for chaining =====
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
        """
        Set category and return self for chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Example:
            >>> component.with_category("APPLICATION").with_uuid("12345")
        """
        self.category = value  # Use property setter (gets validation)
        return self

    def with_uuid(self, value: str) -> "ApplicationSwComponentType":
        """
        Set UUID and return self for chaining.

        Args:
            value: The UUID to set

        Returns:
            self for method chaining

        Example:
            >>> component.with_uuid("12345").with_short_name("MyComp")
        """
        self.uuid = value  # Use property setter (gets validation)
        return self
```

### Usage Examples

**Before (current V2 - verbose):**
```python
component = ApplicationSwComponentType()
component.setShortName("MyComponent")
component.setCategory("APPLICATION")
component.setUUID("12345")
```

**After with `with_` methods (clean and fluent):**
```python
# All on one line
component = ApplicationSwComponentType().with_short_name("MyComponent").with_category("APPLICATION").with_uuid("12345")

# Multi-line for readability
component = (ApplicationSwComponentType()
             .with_short_name("MyComponent")
             .with_category("APPLICATION")
             .with_uuid("12345"))

# Partial chaining
component = ApplicationSwComponentType().with_short_name("MyComp")
component.with_category("APPLICATION")  # Continue chaining later
```

**Combining with parent-child relationships:**
```python
pkg = ARPackage(short_name="MyPackage")
component = (ApplicationSwComponentType()
             .with_short_name("MyComponent")
             .with_category("APPLICATION"))

pkg.add_element(component)
```

**Very complex example:**
```python
# Build complete component with ports
component = (ApplicationSwComponentType()
             .with_short_name("TemperatureController")
             .with_category("APPLICATION")
             .with_uuid("comp-001"))

# Create and add ports
port1 = (RPortPrototype()
         .with_short_name("TempSensor")
         .with_interface("TemperatureInterface"))

port2 = (PPortPrototype()
         .with_short_name("ActuatorCmd")
         .with_interface("CommandInterface"))

component.add_port(port1).add_port(port2)

# Add to package
pkg.add_element(component)
```

### Implementation Pattern

For consistency, all classes will follow this pattern:

```python
# Template for with_ method generation
def with_<attribute_name>(self, value: <type>) -> "<ClassName>":
    """
    Set <attribute> and return self for chaining.

    Args:
        value: The <attribute> to set

    Returns:
        self for method chaining
    """
    self.<attribute> = value  # Use property setter
    return self
```

### Benefits

1. **Readability**: Clear intent - "with_short_name" is self-documenting
2. **Type Safety**: Uses property setters, gets validation
3. **DRY Principle**: No duplicate validation logic
4. **IDE Friendly**: Method names show up in autocomplete
5. **Flexible**: Can chain any number of attributes
6. **Optional**: Not required, can still use direct assignment or setters

### Comparison: All Three Assignment Methods

```python
# Method 1: Direct property access (simple)
component.short_name = "MyComp"
component.category = "APPLICATION"

# Method 2: AUTOSAR setters (compatibility)
component.setShortName("MyComp").setCategory("APPLICATION")

# Method 3: Fluent with_ methods (NEW - recommended for chaining)
component.with_short_name("MyComp").with_category("APPLICATION")

# All three can be mixed as needed
component.short_name = "MyComp"  # Direct
component.with_category("APPLICATION")  # Chaining
component.setUUID("12345")  # AUTOSAR compatibility
```

---

## 10. Summary and Next Steps

### Design Summary

We're redesigning the V2 models to make them **easier to use** while maintaining **full AUTOSAR compliance**:

**Key Features:**
1. ✅ **Hybrid Architecture**: Modern Pythonic API + AUTOSAR compatibility
2. ✅ **Dual Naming**: `short_name` (Pythonic) + `getShortName()` (AUTOSAR)
3. ✅ **Chained Assignment**: `with_short_name().with_category().with_uuid()`
4. ✅ **Direct Attribute Access**: `component.short_name = "value"`
5. ✅ **Eager Validation**: Property setters validate immediately
6. ✅ **Explicit Add Methods**: `pkg.add_element(child)` with automatic parent management
7. ✅ **Full Type Hints**: IDE autocomplete and mypy support
8. ✅ **Backward Compatible**: All existing V2 code continues to work

### Before vs After Comparison

**Before (Current V2):**
```python
component = ApplicationSwComponentType()
component.setShortName("MyComponent")
component.setCategory("APPLICATION")
component.setUUID("12345")

pkg.addElement(component)
```

**After (Redesigned V2 - All styles work):**
```python
# Style 1: Fluent with_ methods (NEW - recommended)
component = (ApplicationSwComponentType()
             .with_short_name("MyComponent")
             .with_category("APPLICATION")
             .with_uuid("12345"))

# Style 2: Direct assignment
component = ApplicationSwComponentType()
component.short_name = "MyComponent"
component.category = "APPLICATION"

# Style 3: AUTOSAR setters (existing - still works)
component = ApplicationSwComponentType()
component.setShortName("MyComponent").setCategory("APPLICATION")

# All styles support the same add methods
pkg.add_element(component)
```

### Benefits

**For Developers:**
- ✅ Less verbose code (3-5x shorter)
- ✅ Better IDE support (autocomplete, type hints)
- ✅ Clearer error messages (validation at construction)
- ✅ Pythonic and intuitive

**For AUTOSAR Compliance:**
- ✅ All AUTOSAR methods still work
- ✅ XML serialization unchanged
- ✅ Parser/writer compatibility maintained
- ✅ Gradual migration path

**For Project Quality:**
- ✅ Type safety with mypy
- ✅ Validation catches errors early
- ✅ Easier to maintain (DRY principle)
- ✅ Better test coverage

### Next Steps

1. ✅ Design approved
2. ⏳ Write design document to `docs/plans/` (THIS DOCUMENT)
3. ⏳ Update `docs/development/coding_rules_v2.md` with new rules
4. ⏳ Create git branch for implementation
5. ⏳ Implement Phase 1: Core infrastructure (ArObject, Referrable, Identifiable)
6. ⏳ Implement Phases 2-6: Module-by-module migration
7. ⏳ Update documentation (user guide, examples)
8. ⏳ Verify all tests pass and backward compatibility

### Quality Metrics

| Metric | Current | Target |
|--------|---------|--------|
| MyPy errors | 4,142 | < 4,000 |
| Ruff errors | 18 | Maintain or reduce |
| Test pass rate | 100% | 100% |
| Test coverage | Current | No regression |
| Backward compatibility | N/A | 100% |

---

## Appendix A: Complete Example

```python
"""
Complete example of building an AUTOSAR model with redesigned V2.
"""
from armodel.models import AUTOSAR
from armodel.v2.models.M2.AUTOSARTemplates import (
    ARPackage,
    ApplicationSwComponentType,
    SenderReceiverInterface,
    PPortPrototype,
    DataPrototype,
)
from armodel.writer.arxml_writer import ARXMLWriter

# Set AUTOSAR version
AUTOSAR.setARRelease('R23-11')

# Create package structure
pkg = ARPackage(short_name="MyApplication")

# Create interface
interface = (SenderReceiverInterface()
             .with_short_name("TemperatureSensor")
             .with_is_queued(False))

# Add data prototype to interface
temp_proto = (DataPrototype()
              .with_short_name("TemperatureValue")
              .with_type("float")
              .with_unit("Celsius"))

interface.add_element(temp_proto)

# Create component
component = (ApplicationSwComponentType()
             .with_short_name("TemperatureController")
             .with_category("APPLICATION")
             .with_uuid("comp-001"))

# Create port
port = (PPortPrototype()
        .with_short_name("TempSensorPort")
        .with_interface(interface))

# Add port to component
component.add_port(port)

# Add everything to package
pkg.add_element(interface)
pkg.add_element(component)

# Add to AUTOSAR root
autosar = AUTOSAR.getInstance()
autosar.addARPackage(pkg)

# Write to ARXML
writer = ARXMLWriter()
writer.save('MyApplication.arxml', autosar)
```

---

## Appendix B: References

**Design Patterns:**
- Property-based access: Python `@property` decorator
- Fluent interface: Method chaining pattern
- Builder pattern: For complex object construction
- Template method pattern: For extensible base classes

**Similar Projects:**
- Pydantic: Validation and type checking
- SQLAlchemy: Hybrid attribute pattern
- Django Models: Property-based field access
- Dataclasses: Foundation for model classes

**AUTOSAR Standards:**
- AUTOSAR Classic Platform R23-11
- AUTOSAR M2 Meta-Model
- AUTOSAR XML Schema Definitions

**Python Best Practices:**
- PEP 8: Style Guide
- PEP 20: Zen of Python ("Explicit is better than implicit")
- PEP 484: Type Hints
- PEP 257: Docstrings
- PEP 287: reStructuredText docstrings

---

**Document Status:** ✅ Design Complete - Ready for Implementation

**Change Log:**
- 2026-02-07: Initial design document created (all 10 sections approved)
