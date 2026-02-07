"""Test ARObject property-based dual API (NEW in redesigned V2)."""

import pytest
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class TestARObjectProperties:
    """Test Pythonic property access (NEW)."""

    def test_uuid_property_getter_returns_value(self):
        """Test uuid property getter returns value."""
        # Create concrete ARObject subclass for testing
        class ConcreteARObject(ARObject):
            def __init__(self) -> None:
                super().__init__()

        obj = ConcreteARObject()
        obj._uuid = "test-uuid-123"
        assert obj.uuid == "test-uuid-123"

    def test_uuid_property_setter_valid(self):
        """Test uuid property setter accepts valid string."""
        class ConcreteARObject(ARObject):
            def __init__(self) -> None:
                super().__init__()

        obj = ConcreteARObject()
        obj.uuid = "test-uuid-456"
        assert obj._uuid == "test-uuid-456"

    def test_uuid_property_setter_none_allowed(self):
        """Test uuid property setter accepts None."""
        class ConcreteARObject(ARObject):
            def __init__(self) -> None:
                super().__init__()

        obj = ConcreteARObject()
        obj.uuid = None
        assert obj._uuid is None

    def test_parent_property_getter(self):
        """Test parent property getter returns value."""
        class ConcreteARObject(ARObject):
            def __init__(self) -> None:
                super().__init__()

        parent = ConcreteARObject()
        child = ConcreteARObject()
        child._parent = parent
        assert child.parent is parent

    def test_parent_property_is_readonly(self):
        """Test parent property is read-only (no setter)."""
        class ConcreteARObject(ARObject):
            def __init__(self) -> None:
                super().__init__()

        obj = ConcreteARObject()
        with pytest.raises(AttributeError):
            obj.parent = ConcreteARObject()


class TestARObjectWithMethods:
    """Test fluent with_ methods (NEW)."""

    def test_with_uuid_method_sets_value_and_returns_self(self):
        """Test with_uuid() method sets value and returns self for chaining."""
        class ConcreteARObject(ARObject):
            def __init__(self) -> None:
                super().__init__()

        obj = ConcreteARObject()
        result = obj.with_uuid("test-uuid")
        assert obj._uuid == "test-uuid"
        assert result is obj  # Method chaining


class TestARObjectAutosarCompatibility:
    """Test AUTOSAR method compatibility (EXISTING - must still work)."""

    def test_getUUID_returns_value(self):
        """Test getUUID() method returns value."""
        class ConcreteARObject(ARObject):
            def __init__(self) -> None:
                super().__init__()

        obj = ConcreteARObject()
        obj._uuid = "test-uuid"
        assert obj.getUUID() == "test-uuid"

    def test_setUUID_sets_value_and_returns_self(self):
        """Test setUUID() method sets value and returns self for chaining."""
        class ConcreteARObject(ARObject):
            def __init__(self) -> None:
                super().__init__()

        obj = ConcreteARObject()
        result = obj.setUUID("test-uuid")
        assert obj._uuid == "test-uuid"
        assert result is obj

    def test_getParent_returns_value(self):
        """Test getParent() method returns value."""
        class ConcreteARObject(ARObject):
            def __init__(self) -> None:
                super().__init__()

        parent = ConcreteARObject()
        child = ConcreteARObject()
        child._parent = parent
        assert child.getParent() is parent
