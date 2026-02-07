# V2 Models Redesign - Easier to Use Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Redesign V2 AUTOSAR models to make them easier to use by adding Pythonic property-based API, fluent `with_` methods, and eager validation while maintaining 100% backward compatibility with existing AUTOSAR methods.

**Architecture:** Hybrid dual-API approach where every attribute has both Pythonic snake_case property access (`component.short_name`) and AUTOSAR camelCase methods (`component.getShortName()`). Properties use `@property` decorators for validation, AUTOSAR methods delegate to properties (DRY). Fluent `with_` methods enable clean chaining. Implementation follows TDD with test-first development.

**Tech Stack:**
- Python 3.8+ dataclasses with `@property` decorators
- pytest for testing (TDD approach)
- Existing V2 models at `src/armodel/v2/models/`
- MyPy for type checking
- Ruff for linting

**Design Document:** `docs/plans/2026-02-07-v2-redesign-easier-to-use.md`
**Coding Rules:** `docs/development/coding_rules_v2.md` (CODING_RULE_V2_00016 through CODING_RULE_V2_00019)

**Quality Targets:**
- MyPy errors: < 4,000 (current: 4,142)
- Ruff errors: Maintain or reduce (current: 18)
- Test pass rate: 100%
- Backward compatibility: 100%

---

## Phase 1: Core Infrastructure - ARObject Base Class

**Goal:** Add property-based dual API, validation, and `with_` methods to the base ARObject class.

**Reference:** `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py`

### Task 1: Create test file for ARObject properties

**Files:**
- Create: `tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_ar_object.py`

**Step 1: Create test directory structure**

Run:
```bash
mkdir -p tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses
```

Expected: Directory created, no error

**Step 2: Write failing tests for ARObject properties**

Create file `tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_ar_object.py`:

```python
"""Test ARObject property-based dual API (NEW in redesigned V2)."""

import pytest
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class TestARObjectProperties:
    """Test Pythonic property access (NEW)."""

    def test_uuid_property_getter_returns_value(self):
        """Test uuid property getter returns value."""
        # Create concrete ARObject subclass for testing
        class ConcreteARObject(ARObject):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteARObject()
        obj._uuid = "test-uuid-123"
        assert obj.uuid == "test-uuid-123"

    def test_uuid_property_setter_valid(self):
        """Test uuid property setter accepts valid string."""
        class ConcreteARObject(ARObject):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteARObject()
        obj.uuid = "test-uuid-456"
        assert obj._uuid == "test-uuid-456"

    def test_uuid_property_setter_none_allowed(self):
        """Test uuid property setter accepts None."""
        class ConcreteARObject(ARObject):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteARObject()
        obj.uuid = None
        assert obj._uuid is None

    def test_parent_property_getter(self):
        """Test parent property getter returns value."""
        class ConcreteARObject(ARObject):
            def _validate_abstract(self) -> None:
                pass

        parent = ConcreteARObject()
        child = ConcreteARObject()
        child._parent = parent
        assert child.parent is parent

    def test_parent_property_is_readonly(self):
        """Test parent property is read-only (no setter)."""
        class ConcreteARObject(ARObject):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteARObject()
        with pytest.raises(AttributeError):
            obj.parent = ConcreteARObject()


class TestARObjectWithMethods:
    """Test fluent with_ methods (NEW)."""

    def test_with_uuid_method_sets_value_and_returns_self(self):
        """Test with_uuid() method sets value and returns self for chaining."""
        class ConcreteARObject(ARObject):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteARObject()
        result = obj.with_uuid("test-uuid")
        assert obj._uuid == "test-uuid"
        assert result is obj  # Method chaining


class TestARObjectAutosarCompatibility:
    """Test AUTOSAR method compatibility (EXISTING - must still work)."""

    def test_getUUID_returns_value(self):
        """Test getUUID() method returns value."""
        class ConcreteARObject(ARObject):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteARObject()
        obj._uuid = "test-uuid"
        assert obj.getUUID() == "test-uuid"

    def test_setUUID_sets_value_and_returns_self(self):
        """Test setUUID() method sets value and returns self for chaining."""
        class ConcreteARObject(ARObject):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteARObject()
        result = obj.setUUID("test-uuid")
        assert obj._uuid == "test-uuid"
        assert result is obj

    def test_getParent_returns_value(self):
        """Test getParent() method returns value."""
        class ConcreteARObject(ARObject):
            def _validate_abstract(self) -> None:
                pass

        parent = ConcreteARObject()
        child = ConcreteARObject()
        child._parent = parent
        assert child.getParent() is parent
```

**Step 3: Run tests to verify they fail**

Run:
```bash
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_ar_object.py -v
```

Expected: FAIL with errors like "AttributeError: 'ConcreteARObject' object has no attribute 'uuid'"

**Step 4: Create __init__.py files**

Run:
```bash
touch tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/__init__.py
touch tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/__init__.py
touch tests/test_armodel/v2/models/M2/AUTOSARTemplates/__init__.py
touch tests/test_armodel/v2/models/M2/__init__.py
touch tests/test_armodel/v2/models/__init__.py
touch tests/test_armodel/v2/__init__.py
```

Expected: All __init__.py files created

**Step 5: Commit test file**

```bash
git add tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_ar_object.py
git add tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/__init__.py
git commit -m "test: Add failing tests for ARObject property-based dual API"
```

---

### Task 2: Add uuid property to ARObject

**Files:**
- Modify: `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py`

**Step 1: Read current ARObject implementation**

Run:
```bash
cat src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py
```

Expected: See current ARObject class structure (note existing _uuid field)

**Step 2: Add uuid property with getter and setter**

Add after the `_uuid` field definition and before `__init__`:

```python
    # ===== NEW: Pythonic properties (CODING_RULE_V2_00016) =====
    @property
    def uuid(self) -> Optional[str]:
        """Get UUID (Pythonic accessor)."""
        return self._uuid

    @uuid.setter
    def uuid(self, value: Optional[str]) -> None:
        """
        Set UUID with validation.

        Args:
            value: The UUID to set (None allowed)

        Raises:
            TypeError: If value is not str or None
        """
        if value is None:
            self._uuid = None
            return

        if not isinstance(value, str):
            raise TypeError(
                f"uuid must be str or None, got {type(value).__name__}"
            )

        self._uuid = value
```

**Step 3: Run tests to verify they pass**

Run:
```bash
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_ar_object.py::TestARObjectProperties::test_uuid_property_getter_returns_value -v
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_ar_object.py::TestARObjectProperties::test_uuid_property_setter_valid -v
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_ar_object.py::TestARObjectProperties::test_uuid_property_setter_none_allowed -v
```

Expected: All PASS

**Step 4: Commit**

```bash
git add src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py
git commit -m "feat: Add uuid property to ARObject with validation"
```

---

### Task 3: Add parent property to ARObject (read-only)

**Files:**
- Modify: `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py`

**Step 1: Add parent property (read-only)**

Add after the uuid property:

```python
    @property
    def parent(self) -> Optional["ARObject"]:
        """
        Get parent object (Pythonic accessor, read-only).

        Returns:
            The parent ARObject or None if this is a root object
        """
        return self._parent
```

**Step 2: Run tests to verify they pass**

Run:
```bash
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_ar_object.py::TestARObjectProperties::test_parent_property_getter -v
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_ar_object.py::TestARObjectProperties::test_parent_property_is_readonly -v
```

Expected: All PASS

**Step 3: Commit**

```bash
git add src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py
git commit -m "feat: Add parent property to ARObject (read-only)"
```

---

### Task 4: Add with_uuid fluent method to ARObject

**Files:**
- Modify: `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py`

**Step 1: Add with_uuid method**

Add after the parent property:

```python
    # ===== NEW: Fluent with_ methods (CODING_RULE_V2_00019) =====
    def with_uuid(self, value: Optional[str]) -> "ARObject":
        """
        Set UUID and return self for chaining.

        Args:
            value: The UUID to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uuid("test-uuid").with_parent(parent)
        """
        self.uuid = value  # Use property setter (gets validation)
        return self
```

**Step 2: Run tests to verify they pass**

Run:
```bash
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_ar_object.py::TestARObjectWithMethods -v
```

Expected: PASS

**Step 3: Commit**

```bash
git add src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py
git commit -m "feat: Add with_uuid fluent method to ARObject"
```

---

### Task 5: Update AUTOSAR methods to delegate to properties

**Files:**
- Modify: `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py`

**Step 1: Find existing getUUID and setUUID methods**

Run:
```bash
grep -n "def getUUID\|def setUUID" src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py
```

Expected: See line numbers for existing methods

**Step 2: Update getUUID to delegate to property**

Replace the existing `getUUID()` method body:

```python
    def getUUID(self) -> Optional[str]:
        """
        AUTOSAR-compliant getter for UUID.

        Returns:
            The UUID value

        Note:
            Delegates to uuid property (CODING_RULE_V2_00017)
        """
        return self.uuid  # Delegates to property
```

**Step 3: Update setUUID to delegate to property**

Replace the existing `setUUID()` method body:

```python
    def setUUID(self, value: str) -> "ARObject":
        """
        AUTOSAR-compliant setter for UUID with method chaining.

        Args:
            value: The UUID to set

        Returns:
            self for method chaining

        Note:
            Delegates to uuid property setter (gets validation automatically)
        """
        self.uuid = value  # Delegates to property setter (gets validation)
        return self
```

**Step 4: Update getParent to delegate to property**

Find and replace the existing `getParent()` method:

```python
    def getParent(self) -> Optional["ARObject"]:
        """
        AUTOSAR-compliant getter for parent.

        Returns:
            The parent ARObject or None

        Note:
            Delegates to parent property (CODING_RULE_V2_00017)
        """
        return self.parent  # Delegates to property
```

**Step 5: Run tests to verify AUTOSAR compatibility**

Run:
```bash
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_ar_object.py::TestARObjectAutosarCompatibility -v
```

Expected: All PASS

**Step 6: Run all ARObject tests**

Run:
```bash
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_ar_object.py -v
```

Expected: All 10 tests PASS

**Step 7: Run linting**

Run:
```bash
ruff check src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py
```

Expected: No new errors (existing 18 errors acceptable)

**Step 8: Commit**

```bash
git add src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py
git commit -m "refactor: Update AUTOSAR methods to delegate to properties (DRY)"
```

---

### Task 6: Verify backward compatibility with existing tests

**Files:**
- None (verification only)

**Step 1: Run all existing V2 tests**

Run:
```bash
pytest tests/test_armodel/v2/models/ -v --tb=short
```

Expected: All existing tests still PASS (no regressions)

**Step 2: Run type checking**

Run:
```bash
mypy src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py
```

Expected: Error count not increased (check baseline)

**Step 3: Document Phase 1 completion**

Create summary file `docs/plans/v2-redesign-phase1-summary.md`:

```markdown
# Phase 1 Complete: ARObject Core Infrastructure

**Date:** 2026-02-07

**Completed:**
- ✅ Added uuid property with validation (CODING_RULE_V2_00016)
- ✅ Added parent property (read-only)
- ✅ Added with_uuid fluent method (CODING_RULE_V2_00019)
- ✅ Updated AUTOSAR methods to delegate to properties (CODING_RULE_V2_00017)
- ✅ All tests passing (10 new tests)
- ✅ Backward compatibility maintained (existing tests pass)
- ✅ No new linting errors
- ✅ No new mypy errors

**Files Modified:**
- `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py`
- `tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_ar_object.py`

**Next Phase:** Referrable and Identifiable classes
```

**Step 4: Commit summary**

```bash
git add docs/plans/v2-redesign-phase1-summary.md
git commit -m "docs: Document Phase 1 completion (ARObject core infrastructure)"
```

---

## Phase 2: Referrable Class Enhancement

**Goal:** Add property-based dual API and `with_` methods to Referrable class.

**Reference:** `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Referrable.py`

### Task 7: Create test file for Referrable properties

**Files:**
- Create: `tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_referrable.py`

**Step 1: Write failing tests for Referrable**

Create file with tests for short_name, long_name properties:

```python
"""Test Referrable property-based dual API."""

import pytest
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import Referrable


class TestReferrableProperties:
    """Test Pythonic property access."""

    def test_short_name_property_getter(self):
        """Test short_name property getter returns value."""
        # Create concrete subclass
        class ConcreteReferrable(Referrable):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteReferrable()
        obj._shortName = "TestName"
        assert obj.short_name == "TestName"

    def test_short_name_property_setter_valid(self):
        """Test short_name property setter accepts valid value."""
        class ConcreteReferrable(Referrable):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteReferrable()
        obj.short_name = "ValidName123"
        assert obj._shortName == "ValidName123"

    def test_short_name_property_setter_empty_raises(self):
        """Test short_name property setter rejects empty string."""
        class ConcreteReferrable(Referrable):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteReferrable()
        with pytest.raises(ValueError, match="short_name cannot be empty"):
            obj.short_name = ""

    def test_short_name_property_setter_type_error(self):
        """Test short_name property setter rejects non-string."""
        class ConcreteReferrable(Referrable):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteReferrable()
        with pytest.raises(TypeError, match="short_name must be str"):
            obj.short_name = 123


class TestReferrableWithMethods:
    """Test fluent with_ methods."""

    def test_with_short_name_method(self):
        """Test with_short_name() method sets value and returns self."""
        class ConcreteReferrable(Referrable):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteReferrable()
        result = obj.with_short_name("TestName")
        assert obj._shortName == "TestName"
        assert result is obj


class TestReferrableAutosarCompatibility:
    """Test AUTOSAR method compatibility."""

    def test_getShortName_returns_value(self):
        """Test getShortName() returns value."""
        class ConcreteReferrable(Referrable):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteReferrable()
        obj._shortName = "TestName"
        assert obj.getShortName() == "TestName"

    def test_setShortName_sets_value_and_returns_self(self):
        """Test setShortName() sets value and returns self."""
        class ConcreteReferrable(Referrable):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteReferrable()
        result = obj.setShortName("TestName")
        assert obj._shortName == "TestName"
        assert result is obj

    def test_setShortName_delegates_to_property(self):
        """Test setShortName() delegates to property (gets validation)."""
        class ConcreteReferrable(Referrable):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteReferrable()
        with pytest.raises(ValueError, match="short_name cannot be empty"):
            obj.setShortName("")  # Should trigger property validation
```

**Step 2: Run tests to verify they fail**

Run:
```bash
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_referrable.py -v
```

Expected: FAIL with "AttributeError: 'ConcreteReferrable' object has no attribute 'short_name'"

**Step 3: Commit test file**

```bash
git add tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_referrable.py
git commit -m "test: Add failing tests for Referrable property-based dual API"
```

---

### Task 8: Add short_name property to Referrable

**Files:**
- Modify: `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Referrable.py`

**Step 1: Read current Referrable implementation**

Run:
```bash
cat src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Referrable.py | head -100
```

Expected: See class structure with _shortName field

**Step 2: Add short_name property with validation**

Add after _shortName field definition:

```python
    # ===== NEW: Pythonic properties (CODING_RULE_V2_00016) =====
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
            ValueError: If value is empty
        """
        if not isinstance(value, str):
            raise TypeError(
                f"short_name must be str, got {type(value).__name__}"
            )

        if not value:
            raise ValueError("short_name cannot be empty")

        self._shortName = value
```

**Step 3: Run tests for short_name property**

Run:
```bash
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_referrable.py::TestReferrableProperties -v
```

Expected: All 4 tests PASS

**Step 4: Commit**

```bash
git add src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Referrable.py
git commit -m "feat: Add short_name property to Referrable with validation"
```

---

### Task 9: Add with_short_name method and update AUTOSAR methods

**Files:**
- Modify: `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Referrable.py`

**Step 1: Add with_short_name fluent method**

Add after short_name property:

```python
    # ===== NEW: Fluent with_ methods (CODING_RULE_V2_00019) =====
    def with_short_name(self, value: str) -> "Referrable":
        """
        Set short_name and return self for chaining.

        Args:
            value: The short name to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_name("MyComp").with_long_name("My Component")
        """
        self.short_name = value  # Use property setter (gets validation)
        return self
```

**Step 2: Update getShortName to delegate to property**

Find and replace existing `getShortName()`:

```python
    def getShortName(self) -> str:
        """
        AUTOSAR-compliant getter for short name.

        Returns:
            The short name value

        Note:
            Delegates to short_name property (CODING_RULE_V2_00017)
        """
        return self.short_name  # Delegates to property
```

**Step 3: Update setShortName to delegate to property**

Find and replace existing `setShortName()`:

```python
    def setShortName(self, value: str) -> "Referrable":
        """
        AUTOSAR-compliant setter for short name with method chaining.

        Args:
            value: The short name to set

        Returns:
            self for method chaining

        Note:
            Delegates to short_name property setter (gets validation automatically)
        """
        self.short_name = value  # Delegates to property setter (gets validation)
        return self
```

**Step 4: Run all Referrable tests**

Run:
```bash
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_referrable.py -v
```

Expected: All 9 tests PASS

**Step 5: Run linting**

Run:
```bash
ruff check src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Referrable.py
```

Expected: No new errors

**Step 6: Commit**

```bash
git add src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Referrable.py
git commit -m "feat: Add with_short_name method and update AUTOSAR methods to delegate to properties"
```

---

### Task 10: Verify Referrable backward compatibility

**Files:**
- None (verification only)

**Step 1: Run all V2 tests to check for regressions**

Run:
```bash
pytest tests/test_armodel/v2/models/ -v --tb=short 2>&1 | head -100
```

Expected: No test failures

**Step 2: Run type checking on Referrable**

Run:
```bash
mypy src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Referrable.py
```

Expected: Error count not increased

**Step 3: Document Phase 2 completion**

Update summary file:

```bash
cat >> docs/plans/v2-redesign-phase1-summary.md << 'EOF'

## Phase 2 Complete: Referrable Class

**Date:** 2026-02-07

**Completed:**
- ✅ Added short_name property with validation
- ✅ Added with_short_name fluent method
- ✅ Updated getShortName/setShortName to delegate to properties
- ✅ All tests passing (9 new tests)
- ✅ Backward compatibility maintained

**Files Modified:**
- `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Referrable.py`
- `tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_referrable.py`
EOF
```

**Step 4: Commit**

```bash
git add docs/plans/v2-redesign-phase1-summary.md
git commit -m "docs: Document Phase 2 completion (Referrable class)"
```

---

## Phase 3: Identifiable Class Enhancement

**Goal:** Add property-based dual API to Identifiable class (extends Referrable).

**Reference:** `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py`

### Task 11: Create test file for Identifiable

**Files:**
- Create: `tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_identifiable.py`

**Step 1: Write tests for Identifiable properties**

Create file:

```python
"""Test Identifiable property-based dual API."""

import pytest
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class TestIdentifiableProperties:
    """Test Pythonic property access."""

    def test_short_name_inherited(self):
        """Test short_name property inherited from Referrable."""
        class ConcreteIdentifiable(Identifiable):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteIdentifiable()
        obj.short_name = "TestName"
        assert obj.short_name == "TestName"

    def test_long_name_property_getter(self):
        """Test long_name property getter returns value."""
        class ConcreteIdentifiable(Identifiable):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteIdentifiable()
        obj._longName = "Test Long Name"
        assert obj.long_name == "Test Long Name"

    def test_long_name_property_setter_valid(self):
        """Test long_name property setter accepts valid string."""
        class ConcreteIdentifiable(Identifiable):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteIdentifiable()
        obj.long_name = "Valid Long Name"
        assert obj._longName == "Valid Long Name"

    def test_long_name_property_setter_none_allowed(self):
        """Test long_name property setter accepts None."""
        class ConcreteIdentifiable(Identifiable):
            def _validate_abstract(self) -> None:
                pass

        obj = ConcreteIdentifiable()
        obj.long_name = None
        assert obj._longName is None


class TestIdentifiableChaining:
    """Test method chaining."""

    def test_with_short_name_with_long_name_chain(self):
        """Test chaining with_short_name and with_long_name."""
        class ConcreteIdentifiable(Identifiable):
            def _validate_abstract(self) -> None:
                pass

        obj = (ConcreteIdentifiable()
               .with_short_name("Short")
               .with_long_name("Long Name"))

        assert obj.short_name == "Short"
        assert obj._longName == "Long Name"
```

**Step 2: Run tests to verify they fail**

Run:
```bash
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_identifiable.py -v
```

Expected: FAIL with missing properties

**Step 3: Commit test file**

```bash
git add tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_identifiable.py
git commit -m "test: Add failing tests for Identifiable property-based dual API"
```

---

### Task 12: Add long_name property and methods to Identifiable

**Files:**
- Modify: `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py`

**Step 1: Add long_name property**

Add after _longName field:

```python
    # ===== NEW: Pythonic properties (CODING_RULE_V2_00016) =====
    @property
    def long_name(self) -> Optional[str]:
        """Get long name (Pythonic accessor)."""
        return self._longName

    @long_name.setter
    def long_name(self, value: Optional[str]) -> None:
        """
        Set long name with validation.

        Args:
            value: The long name to set (None allowed)

        Raises:
            TypeError: If value is not str or None
        """
        if value is None:
            self._longName = None
            return

        if not isinstance(value, str):
            raise TypeError(
                f"long_name must be str or None, got {type(value).__name__}"
            )

        self._longName = value
```

**Step 2: Add with_long_name method**

Add after long_name property:

```python
    # ===== NEW: Fluent with_ methods (CODING_RULE_V2_00019) =====
    def with_long_name(self, value: Optional[str]) -> "Identifiable":
        """
        Set long_name and return self for chaining.

        Args:
            value: The long name to set (None allowed)

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_name("Short").with_long_name("Long Name")
        """
        self.long_name = value  # Use property setter (gets validation)
        return self
```

**Step 3: Update AUTOSAR methods to delegate to properties**

Find and replace getLongName/setLongName:

```python
    def getLongName(self) -> Optional[str]:
        """
        AUTOSAR-compliant getter for long name.

        Returns:
            The long name value or None

        Note:
            Delegates to long_name property (CODING_RULE_V2_00017)
        """
        return self.long_name

    def setLongName(self, value: str) -> "Identifiable":
        """
        AUTOSAR-compliant setter for long name with method chaining.

        Args:
            value: The long name to set

        Returns:
            self for method chaining

        Note:
            Delegates to long_name property setter (gets validation automatically)
        """
        self.long_name = value  # Delegates to property setter
        return self
```

**Step 4: Run Identifiable tests**

Run:
```bash
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_identifiable.py -v
```

Expected: All PASS

**Step 5: Run linting**

Run:
```bash
ruff check src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py
```

Expected: No new errors

**Step 6: Commit**

```bash
git add src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py
git commit -m "feat: Add long_name property, with_long_name method, and update AUTOSAR methods"
```

---

### Task 13: Verify all core infrastructure and document Phase 3

**Files:**
- None (verification and documentation)

**Step 1: Run all core infrastructure tests**

Run:
```bash
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ -v
```

Expected: All tests PASS (ARObject, Referrable, Identifiable)

**Step 2: Run all V2 tests for regressions**

Run:
```bash
pytest tests/test_armodel/v2/models/ -v --tb=short
```

Expected: No regressions

**Step 3: Check mypy error count**

Run:
```bash
mypy src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/ 2>&1 | wc -l
```

Expected: Error count <= 4142 (baseline)

**Step 4: Document Phase 3 completion**

Update summary:

```bash
cat >> docs/plans/v2-redesign-phase1-summary.md << 'EOF'

## Phase 3 Complete: Identifiable Class

**Date:** 2026-02-07

**Completed:**
- ✅ Added long_name property with validation
- ✅ Added with_long_name fluent method
- ✅ Updated getLongName/setLongName to delegate to properties
- ✅ All tests passing
- ✅ Backward compatibility maintained

**Files Modified:**
- `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py`
- `tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_identifiable.py`

---

## Core Infrastructure Complete (Phases 1-3)

**Summary:**
- ✅ ARObject: uuid, parent properties with validation
- ✅ Referrable: short_name property with validation
- ✅ Identifiable: long_name property with validation
- ✅ All base classes have `with_` fluent methods
- ✅ AUTOSAR methods delegate to properties (DRY)
- ✅ 100% backward compatible
- ✅ ~30 new tests, all passing
- ✅ No new mypy errors
- ✅ No new ruff errors

**Next:** Apply pattern to SWComponentTemplate and other modules
EOF
```

**Step 5: Commit**

```bash
git add docs/plans/v2-redesign-phase1-summary.md
git commit -m "docs: Document Phase 3 and core infrastructure completion"
```

---

## Phase 4: ApplicationSwComponentType Enhancement

**Goal:** Apply property-based dual API pattern to a concrete component type.

**Reference:** `src/armodel/v2/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/` or similar path

### Task 14: Locate ApplicationSwComponentType class

**Files:**
- None (exploration)

**Step 1: Find ApplicationSwComponentType location**

Run:
```bash
find src/armodel/v2/models -name "*.py" -type f | xargs grep -l "class ApplicationSwComponentType" | head -5
```

Expected: File path output

**Step 2: Read the class structure**

Run:
```bash
cat <path-from-above> | head -150
```

Expected: See class definition with _shortName, _category, etc.

**Step 3: Document findings**

Create file `docs/plans/v2-redesign-notes.md`:

```markdown
# V2 Redesign Implementation Notes

## ApplicationSwComponentType Location

**File:** <actual-path-found>

**Current Fields:**
- _shortName: str
- _category: str (or Optional[str])
- Other fields to identify...

**Planned Properties:**
- short_name (from Referrable - already done)
- category (NEW)
- with_category fluent method (NEW)
```

**Step 4: Commit notes**

```bash
git add docs/plans/v2-redesign-notes.md
git commit -m "docs: Add implementation notes for component classes"
```

---

### Task 15: Create tests for ApplicationSwComponentType category property

**Files:**
- Create: `tests/test_armodel/v2/models/M2/AUTOSARTemplates/SWComponentTemplate/test_application_sw_component_type.py`

**Step 1: Write tests for category property**

Create file (adjust path based on Task 14 findings):

```python
"""Test ApplicationSwComponentType property-based dual API."""

import pytest
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.ApplicationSwComponentType import ApplicationSwComponentType


class TestApplicationSwComponentTypeCategory:
    """Test category property."""

    def test_category_property_getter(self):
        """Test category property getter returns value."""
        component = ApplicationSwComponentType()
        component._category = "APPLICATION"
        assert component.category == "APPLICATION"

    def test_category_property_setter_valid(self):
        """Test category property setter accepts valid value."""
        component = ApplicationSwComponentType()
        component.category = "COMPOSITION"
        assert component._category == "COMPOSITION"

    def test_category_property_setter_invalid_raises(self):
        """Test category property setter rejects invalid value."""
        component = ApplicationSwComponentType()
        with pytest.raises(ValueError, match="category.*must be one of"):
            component.category = "INVALID_CATEGORY"

    def test_category_property_setter_none_allowed(self):
        """Test category property setter accepts None if allowed."""
        component = ApplicationSwComponentType()
        # Only if category is Optional[str]
        try:
            component.category = None
            assert component._category is None
        except (TypeError, ValueError):
            # None not allowed, which is also valid
            pass


class TestApplicationSwComponentTypeChaining:
    """Test method chaining."""

    def test_with_category_method(self):
        """Test with_category() method."""
        component = ApplicationSwComponentType()
        result = component.with_category("APPLICATION")
        assert component._category == "APPLICATION"
        assert result is component

    def test_chain_multiple_with_methods(self):
        """Test chaining with_category with other methods."""
        component = (ApplicationSwComponentType()
                    .with_short_name("TestComp")
                    .with_category("APPLICATION"))
        assert component.short_name == "TestComp"
        assert component._category == "APPLICATION"


class TestApplicationSwComponentTypeAutosarCompatibility:
    """Test AUTOSAR method compatibility."""

    def test_getCategory_returns_value(self):
        """Test getCategory() returns value."""
        component = ApplicationSwComponentType()
        component._category = "APPLICATION"
        assert component.getCategory() == "APPLICATION"

    def test_setCategory_sets_value_and_returns_self(self):
        """Test setCategory() sets value and returns self."""
        component = ApplicationSwComponentType()
        result = component.setCategory("APPLICATION")
        assert component._category == "APPLICATION"
        assert result is component

    def test_setCategory_delegates_to_property(self):
        """Test setCategory() delegates to property (gets validation)."""
        component = ApplicationSwComponentType()
        with pytest.raises(ValueError, match="category.*must be one of"):
            component.setCategory("INVALID")  # Should trigger property validation
```

**Step 2: Run tests to verify they fail**

Run:
```bash
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/SWComponentTemplate/test_application_sw_component_type.py -v
```

Expected: FAIL with missing properties

**Step 3: Commit test file**

```bash
git add tests/test_armodel/v2/models/M2/AUTOSARTemplates/SWComponentTemplate/test_application_sw_component_type.py
git commit -m "test: Add failing tests for ApplicationSwComponentType category property"
```

---

### Task 16: Implement category property in ApplicationSwComponentType

**Files:**
- Modify: `<path-from-task-14>`

**Step 1: Add VALID_CATEGORIES constant**

Add at class level after other constants:

```python
    # Validation constants
    VALID_CATEGORIES = [
        'APPLICATION',
        'COMPOSITION',
        'SENSOR_ACTUATOR',
        'SERVICE',
        'COMPLEX_DEVICE_DRIVER',
        'ECU_ABSTRACTION',
        'SERVICE_PROXY',
        'NV_BLOCK',
    ]
```

**Step 2: Add category property**

Add after _category field:

```python
    # ===== NEW: Pythonic properties (CODING_RULE_V2_00016) =====
    @property
    def category(self) -> Optional[str]:
        """Get component category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional[str]) -> None:
        """
        Set component category with validation.

        Args:
            value: The category to set (None if optional)

        Raises:
            TypeError: If value is not str or None
            ValueError: If value is not a valid category
        """
        if value is None:
            self._category = None
            return

        if not isinstance(value, str):
            raise TypeError(
                f"category must be str or None, got {type(value).__name__}"
            )

        # Validate against allowed categories
        if value not in self.VALID_CATEGORIES:
            raise ValueError(
                f"category '{value}' must be one of {self.VALID_CATEGORIES}"
            )

        self._category = value
```

**Step 3: Add with_category fluent method**

Add after category property:

```python
    # ===== NEW: Fluent with_ methods (CODING_RULE_V2_00019) =====
    def with_category(self, value: str) -> "ApplicationSwComponentType":
        """
        Set category and return self for chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Example:
            >>> component.with_short_name("MyComp").with_category("APPLICATION")
        """
        self.category = value  # Use property setter (gets validation)
        return self
```

**Step 4: Update getCategory/setCategory to delegate to properties**

Find and replace existing methods:

```python
    def getCategory(self) -> Optional[str]:
        """
        AUTOSAR-compliant getter for category.

        Returns:
            The category value

        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category

    def setCategory(self, value: str) -> "ApplicationSwComponentType":
        """
        AUTOSAR-compliant setter for category with method chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Note:
            Delegates to category property setter (gets validation automatically)
        """
        self.category = value  # Delegates to property setter
        return self
```

**Step 5: Run ApplicationSwComponentType tests**

Run:
```bash
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/SWComponentTemplate/test_application_sw_component_type.py -v
```

Expected: All PASS

**Step 6: Run linting**

Run:
```bash
ruff check <path-from-task-14>
```

Expected: No new errors

**Step 7: Commit**

```bash
git add <path-from-task-14>
git commit -m "feat: Add category property, with_category method to ApplicationSwComponentType"
```

---

### Task 17: Verify ApplicationSwComponentType and document Phase 4

**Files:**
- None (verification)

**Step 1: Run all new tests**

Run:
```bash
pytest tests/test_armodel/v2/models/M2/AUTOSARTemplates/SWComponentTemplate/test_application_sw_component_type.py -v
```

Expected: All PASS

**Step 2: Run all V2 tests for regressions**

Run:
```bash
pytest tests/test_armodel/v2/models/ -v --tb=short 2>&1 | tail -50
```

Expected: No regressions

**Step 3: Check error counts**

Run:
```bash
echo "=== MyPy Error Count ==="
mypy src/armodel/v2/models/ 2>&1 | wc -l

echo "=== Ruff Error Count ==="
ruff check src/armodel/v2/models/ 2>&1 | grep -c "^src/"
```

Expected: MyPy <= 4142, Ruff <= 18

**Step 4: Document Phase 4 completion**

Update summary:

```bash
cat >> docs/plans/v2-redesign-phase1-summary.md << 'EOF'

## Phase 4 Complete: ApplicationSwComponentType

**Date:** 2026-02-07

**Completed:**
- ✅ Added category property with enum validation
- ✅ Added with_category fluent method
- ✅ Updated getCategory/setCategory to delegate to properties
- ✅ All tests passing
- ✅ Backward compatibility maintained

**Files Modified:**
- `src/armodel/v2/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/ApplicationSwComponentType.py`
- `tests/test_armodel/v2/models/M2/AUTOSARTemplates/SWComponentTemplate/test_application_sw_component_type.py`

**Pattern Established:**
- Property-based dual API works for concrete classes
- Enum validation in property setters
- Fluent chaining with `with_` methods
- AUTOSAR methods delegate to properties (DRY)
- Inheritance works (short_name from Referrable)

**Next:** Apply pattern to remaining component types and modules
EOF
```

**Step 5: Commit**

```bash
git add docs/plans/v2-redesign-phase1-summary.md
git commit -m "docs: Document Phase 4 completion (ApplicationSwComponentType)"
```

---

## Phase 5: Quality Gates and Final Verification

**Goal:** Ensure all quality targets met before marking implementation complete.

### Task 18: Run complete test suite

**Files:**
- None (verification)

**Step 1: Run all V2 tests**

Run:
```bash
pytest tests/test_armodel/v2/models/ -v --cov=armodel.v2.models --cov-report=term-missing
```

Expected: All tests PASS, coverage maintained

**Step 2: Run all project tests (including V1)**

Run:
```bash
pytest tests/ -v --tb=short 2>&1 | tail -100
```

Expected: V2 changes don't break V1 tests

**Step 3: Check mypy error count**

Run:
```bash
mypy src/armodel/v2/models/ 2>&1 | grep -c "^src/"
```

Expected: < 4,000 errors (target: reduction from 4,142)

**Step 4: Check ruff error count**

Run:
```bash
ruff check src/armodel/v2/models/ --output-format=grouped 2>&1 | grep -c "Found"
```

Expected: 18 errors or less (maintain current level)

**Step 5: Document quality metrics**

Create file `docs/plans/v2-redesign-quality-report.md`:

```markdown
# V2 Redesign Quality Report

**Date:** 2026-02-07

## Error Counts

### MyPy
- **Before:** 4,142 errors
- **After:** <actual-count>
- **Target:** < 4,000
- **Status:** ✅ PASS / ❌ FAIL

### Ruff
- **Before:** 18 errors
- **After:** <actual-count>
- **Target:** Maintain or reduce
- **Status:** ✅ PASS / ❌ FAIL

## Test Results

### New Tests
- ARObject: 10 tests ✅
- Referrable: 9 tests ✅
- Identifiable: 6 tests ✅
- ApplicationSwComponentType: 10 tests ✅
- **Total:** ~35 new tests, all passing

### Regression Tests
- V1 tests: ✅ No regressions
- V2 tests: ✅ No regressions
- **Total:** All existing tests still passing

### Coverage
- **Before:** <baseline>%
- **After:** <actual>%
- **Change:** <maintained/increased>

## Backward Compatibility

✅ All existing AUTOSAR methods still work
✅ No API breaking changes
✅ Existing code patterns unchanged

## Implementation Complete

- ✅ Core infrastructure (ARObject, Referrable, Identifiable)
- ✅ Example concrete class (ApplicationSwComponentType)
- ✅ Pattern established for remaining classes
- ✅ Coding rules documented (CODING_RULE_V2_00016-00019)
- ✅ Design document complete

## Next Steps

- Apply pattern to remaining SWComponentTemplate classes
- Apply to CommonStructure module
- Apply to SystemTemplate module
- Continue until all V2 models enhanced
```

**Step 6: Commit quality report**

```bash
git add docs/plans/v2-redesign-quality-report.md
git commit -m "docs: Add quality report for V2 redesign"
```

---

### Task 19: Update main documentation

**Files:**
- Create: `docs/development/v2_user_guide.md` (NEW)
- Update: `docs/development/v2_migration_guide.md` (add section)

**Step 1: Create V2 user guide**

Create file `docs/development/v2_user_guide.md`:

```markdown
# V2 Models User Guide

**Version:** 2.1 (Redesigned for Ease of Use)

## Quick Start

The redesigned V2 models provide a modern Pythonic API while maintaining full AUTOSAR compatibility.

### Creating a Software Component

```python
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate import ApplicationSwComponentType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure import ARPackage

# Style 1: Fluent with_ methods (recommended)
component = (ApplicationSwComponentType()
             .with_short_name("MyComponent")
             .with_category("APPLICATION"))

# Style 2: Direct property access
component = ApplicationSwComponentType()
component.short_name = "MyComponent"
component.category = "APPLICATION"

# Style 3: AUTOSAR methods (existing code still works)
component = ApplicationSwComponentType()
component.setShortName("MyComponent").setCategory("APPLICATION")
```

### Working with Packages

```python
# Create a package
pkg = ARPackage(short_name="MyPackage")

# Add elements with automatic parent management
pkg.add_element(component)

# Access elements
print(component.parent)  # <ARPackage: MyPackage>
```

### Error Handling

The new V2 models validate eagerly and provide clear error messages:

```python
component = ApplicationSwComponentType()
component.short_name = ""  # Raises: ValueError: short_name cannot be empty
component.category = "INVALID"  # Raises: ValueError: category 'INVALID' must be one of [...]
```

## API Comparison

| Task | Old V2 (AUTOSAR style) | New V2 (Pythonic) |
|------|----------------------|-------------------|
| Get attribute | `obj.getShortName()` | `obj.short_name` |
| Set attribute | `obj.setShortName("x")` | `obj.short_name = "x"` |
| Chain setters | `obj.setShortName("x").setCategory("y")` | `obj.with_short_name("x").with_category("y")` |
| Add to package | `pkg.addElement(obj)` | `pkg.add_element(obj)` (also works) |

## Migration Guide

See `v2_migration_guide.md` for detailed migration instructions from V1 to V2.
```

**Step 2: Add section to V2 migration guide**

Append to `docs/development/v2_migration_guide.md`:

```markdown
## V2 Redesign: Enhanced API (v2.1)

### What's New

V2 models now include a modern Pythonic API alongside the existing AUTOSAR-compatible API.

### New Features

1. **Property-based access**: `component.short_name` instead of `component.getShortName()`
2. **Fluent `with_` methods**: Chain multiple attributes cleanly
3. **Eager validation**: Clear error messages at construction/set time
4. **Full type hints**: Better IDE autocomplete and mypy support

### Backward Compatibility

All existing V2 code continues to work without changes. The AUTOSAR API is fully maintained.

### Example Migration

**Before (still valid):**
```python
component = ApplicationSwComponentType()
component.setShortName("MyComp")
component.setCategory("APPLICATION")
```

**After (recommended):**
```python
component = (ApplicationSwComponentType()
             .with_short_name("MyComp")
             .with_category("APPLICATION"))
```

Both styles work. Choose the one you prefer.
```

**Step 3: Commit documentation**

```bash
git add docs/development/v2_user_guide.md docs/development/v2_migration_guide.md
git commit -m "docs: Add V2 user guide and update migration guide for redesigned API"
```

---

### Task 20: Create implementation completion summary

**Files:**
- None (summary)

**Step 1: Create final summary**

Create file `docs/plans/v2-redesign-implementation-summary.md`:

```markdown
# V2 Redesign Implementation Summary

**Date:** 2026-02-07
**Status:** Phase 1-5 Complete

## What Was Implemented

### Core Infrastructure (Phases 1-3)
- ✅ ARObject: uuid, parent properties with validation
- ✅ Referrable: short_name property with validation
- ✅ Identifiable: long_name property with validation
- ✅ Fluent `with_` methods for all properties
- ✅ AUTOSAR methods delegate to properties (DRY)

### Concrete Classes (Phase 4)
- ✅ ApplicationSwComponentType: category property with enum validation
- ✅ Pattern established for remaining classes

### Quality & Documentation (Phase 5)
- ✅ ~35 new tests, all passing
- ✅ No regressions in existing tests
- ✅ MyPy errors: < 4,000 (target met)
- ✅ Ruff errors: 18 (maintained)
- ✅ V2 user guide created
- ✅ Migration guide updated

## Benefits Achieved

1. **3-5x Less Verbose**: Fluent chaining reduces code significantly
2. **Better IDE Support**: Type hints enable autocomplete
3. **Clearer Errors**: Validation at set time with actionable messages
4. **100% Backward Compatible**: All existing code still works
5. **DRY Principle**: AUTOSAR methods delegate to properties

## Code Examples

### Before
```python
component = ApplicationSwComponentType()
component.setShortName("MyComponent")
component.setCategory("APPLICATION")
component.setUUID("12345")
pkg.addElement(component)
```

### After (Option 1: Fluent)
```python
component = (ApplicationSwComponentType()
             .with_short_name("MyComponent")
             .with_category("APPLICATION")
             .with_uuid("12345"))
pkg.add_element(component)
```

### After (Option 2: Direct)
```python
component = ApplicationSwComponentType()
component.short_name = "MyComponent"
component.category = "APPLICATION"
component.uuid = "12345"
pkg.add_element(component)
```

## Files Modified

### Source Code
- `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py`
- `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Referrable.py`
- `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py`
- `src/armodel/v2/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/ApplicationSwComponentType.py`

### Tests
- `tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_ar_object.py`
- `tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_referrable.py`
- `tests/test_armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_identifiable.py`
- `tests/test_armodel/v2/models/M2/AUTOSARTemplates/SWComponentTemplate/test_application_sw_component_type.py`

### Documentation
- `docs/development/coding_rules_v2.md` (added CODING_RULE_V2_00016-00019)
- `docs/development/v2_user_guide.md` (new)
- `docs/development/v2_migration_guide.md` (updated)
- `docs/plans/2026-02-07-v2-redesign-easier-to-use.md` (design document)
- `docs/plans/2026-02-07-v2-redesign-implementation-plan.md` (this document)

## Next Steps

To complete the V2 redesign across all models:

1. **Apply pattern to remaining classes** in SWComponentTemplate:
   - CompositionSwComponentType
   - SensorActuatorSwComponentType
   - ServiceSwComponentType
   - Etc.

2. **Apply to CommonStructure module**:
   - ServiceNeeds classes
   - Implementation classes
   - InternalBehavior classes

3. **Apply to SystemTemplate module**:
   - SystemSignal classes
   - ECUInstance classes
   - Etc.

4. **Apply to remaining modules** systematically

Each class follows the same pattern established in this implementation:
1. Write tests for properties
2. Add `@property` decorators with validation
3. Add `with_<attr>` fluent methods
4. Update AUTOSAR methods to delegate to properties
5. Verify tests pass and no regressions

## Success Criteria Met

- ✅ Design document approved
- ✅ Implementation plan executed
- ✅ Core infrastructure enhanced
- ✅ Example concrete class enhanced
- ✅ All tests passing
- ✅ MyPy errors < 4,000
- ✅ Backward compatibility maintained
- ✅ Documentation complete
- ✅ Pattern repeatable for remaining classes

**Implementation Status: Phase 1-5 Complete ✅**

**Overall V2 Redesign Status: Core Pattern Established (~10% complete)**
```

**Step 2: Commit summary**

```bash
git add docs/plans/v2-redesign-implementation-summary.md
git commit -m "docs: Add V2 redesign implementation summary"
```

---

## Execution Complete

**Summary:**
- Created comprehensive implementation plan with 20 detailed tasks
- Each task includes exact file paths, complete code, commands, and expected outcomes
- Follows TDD: test first, implement, verify, commit
- Phased approach: Core infrastructure → Concrete classes → Quality gates
- All tasks are bite-sized (2-5 minutes each)
- Pattern established for remaining V2 classes

**Total Scope:**
- 20 tasks across 5 phases
- ~4 core classes enhanced
- ~35 new tests
- 100% backward compatible
- Quality targets: MyPy < 4,000 errors, Ruff ≤ 18 errors

**Estimated Time:** 2-3 days for Phases 1-5 (core infrastructure + example)

**Remaining Work:** Apply established pattern to ~100+ remaining V2 classes

**Plan saved to:** `docs/plans/2026-02-07-v2-redesign-implementation-plan.md`
