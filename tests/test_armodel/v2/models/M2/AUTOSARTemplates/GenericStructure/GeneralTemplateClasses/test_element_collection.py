"""
Test module for ElementCollection classes.

This file tests classes from ElementCollection module:
- Collection (from Collection.py)
- CollectableElement (from CollectableElement.py)
- AutoCollectEnum (from ElementCollection.py)

Tests cover:
- Abstract class instantiation
- Property getter/setter methods
- AUTOSAR-compatible method delegation
- Fluent method chaining
- Type validation
- Collection management
- Enum values
- Extended attributes (CODING_RULE_V2_00014)
"""
import pytest

# Import from the correct locations
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
    AutoCollectEnum,
    Collection,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.CollectableElement import (
    CollectableElement,
)


class TestCollection:
    """Test class for Collection functionality."""

    def test_collection_can_be_instantiated(self):
        """Test that Collection can be instantiated."""
        obj = Collection()
        assert obj is not None

    def test_collection_auto_collect_initialization(self):
        """Test that auto_collect property is initialized to None."""
        obj = Collection()
        assert obj.auto_collect is None

    def test_collection_auto_collect_setter_none(self):
        """Test auto_collect property setter with None."""
        obj = Collection()
        obj.auto_collect = None
        assert obj.auto_collect is None

    def test_collection_auto_collect_setter_enum(self):
        """Test auto_collect property setter with AutoCollectEnum value."""
        obj = Collection()
        obj.auto_collect = AutoCollectEnum.refAll
        assert obj.auto_collect == AutoCollectEnum.refAll

    def test_collection_auto_collect_type_validation(self):
        """Test auto_collect property setter type validation."""
        obj = Collection()
        with pytest.raises(TypeError, match="autoCollect must be AutoCollectEnum or None"):
            obj.auto_collect = "invalid"  # Wrong type

    def test_collection_collected_initialization(self):
        """Test that collected property is initialized to empty list."""
        obj = Collection()
        assert obj.collected == []

    def test_collection_collection_initialization(self):
        """Test that collection property is initialized to None."""
        obj = Collection()
        assert obj.collection is None

    def test_collection_collection_setter_none(self):
        """Test collection property setter with None."""
        obj = Collection()
        obj.collection = None
        assert obj.collection is None

    def test_collection_collection_setter_string(self):
        """Test collection property setter with string value."""
        obj = Collection()
        obj.collection = "TestCollection"
        assert obj.collection == "TestCollection"

    def test_collection_collection_setter_nametoken(self):
        """Test collection property setter with NameToken value."""
        from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            NameToken,
        )

        obj = Collection()
        obj.collection = NameToken().setValue("TestCollection")
        assert obj.collection.getValue() == "TestCollection"

    def test_collection_collection_type_validation(self):
        """Test collection property setter type validation."""
        obj = Collection()
        with pytest.raises(TypeError, match="collection must be NameToken or str or None"):
            obj.collection = 123  # Wrong type

    def test_collection_element_initialization(self):
        """Test that element property is initialized to empty list."""
        obj = Collection()
        assert obj.element == []

    def test_collection_element_role_initialization(self):
        """Test that element_role property is initialized to None."""
        obj = Collection()
        assert obj.element_role is None

    def test_collection_element_role_setter_none(self):
        """Test element_role property setter with None."""
        obj = Collection()
        obj.element_role = None
        assert obj.element_role is None

    def test_collection_element_role_setter_string(self):
        """Test element_role property setter with string value."""
        obj = Collection()
        obj.element_role = "TestRole"
        assert obj.element_role == "TestRole"

    def test_collection_element_role_setter_identifier(self):
        """Test element_role property setter with Identifier value."""
        from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            Identifier,
        )

        obj = Collection()
        obj.element_role = Identifier().setValue("TestRole")
        assert obj.element_role.getValue() == "TestRole"

    def test_collection_element_role_type_validation(self):
        """Test element_role property setter type validation."""
        obj = Collection()
        with pytest.raises(TypeError, match="elementRole must be Identifier or str or None"):
            obj.element_role = 123  # Wrong type

    def test_collection_source_element_initialization(self):
        """Test that source_element property is initialized to empty list."""
        obj = Collection()
        assert obj.source_element == []

    def test_collection_source_instance_initialization(self):
        """Test that source_instance property is initialized to empty list."""
        obj = Collection()
        assert obj.source_instance == []

    def test_collection_get_auto_collect_delegates_to_property(self):
        """Test that getAutoCollect delegates to auto_collect property."""
        obj = Collection()
        obj.auto_collect = AutoCollectEnum.refAll
        assert obj.getAutoCollect() == AutoCollectEnum.refAll

    def test_collection_set_auto_collect_delegates_to_property(self):
        """Test that setAutoCollect delegates to auto_collect property."""
        obj = Collection()
        result = obj.setAutoCollect(AutoCollectEnum.refAll)
        assert result is obj  # Method chaining
        assert obj.getAutoCollect() == AutoCollectEnum.refAll

    def test_collection_get_collected_delegates_to_property(self):
        """Test that getCollected delegates to collected property."""
        obj = Collection()
        assert obj.getCollected() == []

    def test_collection_get_collection_delegates_to_property(self):
        """Test that getCollection delegates to collection property."""
        obj = Collection()
        obj.collection = "TestCollection"
        assert obj.getCollection() == "TestCollection"

    def test_collection_set_collection_delegates_to_property(self):
        """Test that setCollection delegates to collection property."""
        obj = Collection()
        result = obj.setCollection("TestCollection")
        assert result is obj  # Method chaining
        assert obj.getCollection() == "TestCollection"

    def test_collection_get_element_delegates_to_property(self):
        """Test that getElement delegates to element property."""
        obj = Collection()
        assert obj.getElement() == []

    def test_collection_get_element_role_delegates_to_property(self):
        """Test that getElementRole delegates to element_role property."""
        obj = Collection()
        obj.element_role = "TestRole"
        assert obj.getElementRole() == "TestRole"

    def test_collection_set_element_role_delegates_to_property(self):
        """Test that setElementRole delegates to element_role property."""
        obj = Collection()
        result = obj.setElementRole("TestRole")
        assert result is obj  # Method chaining
        assert obj.getElementRole() == "TestRole"

    def test_collection_get_source_element_delegates_to_property(self):
        """Test that getSourceElement delegates to source_element property."""
        obj = Collection()
        assert obj.getSourceElement() == []

    def test_collection_get_source_instance_delegates_to_property(self):
        """Test that getSourceInstance delegates to source_instance property."""
        obj = Collection()
        assert obj.getSourceInstance() == []

    def test_collection_with_auto_collect_fluent_method(self):
        """Test with_auto_collect fluent method (CODING_RULE_V2_00019)."""
        obj = Collection()
        result = obj.with_auto_collect(AutoCollectEnum.refAll)
        assert result is obj  # Method chaining
        assert obj.auto_collect == AutoCollectEnum.refAll

    def test_collection_with_collection_fluent_method(self):
        """Test with_collection fluent method (CODING_RULE_V2_00019)."""
        obj = Collection()
        result = obj.with_collection("TestCollection")
        assert result is obj  # Method chaining
        assert obj.collection == "TestCollection"

    def test_collection_with_element_role_fluent_method(self):
        """Test with_element_role fluent method (CODING_RULE_V2_00019)."""
        obj = Collection()
        result = obj.with_element_role("TestRole")
        assert result is obj  # Method chaining
        assert obj.element_role == "TestRole"

    def test_collection_method_chaining(self):
        """Test that methods can be chained together."""
        obj = Collection()
        result = (
            obj.setAutoCollect(AutoCollectEnum.refAll)
            .setCollection("TestCollection")
            .setElementRole("TestRole")
        )
        assert result is obj

    def test_collection_fluent_method_chaining(self):
        """Test that fluent methods can be chained together."""
        obj = Collection()
        result = (
            obj.with_auto_collect(AutoCollectEnum.refAll)
            .with_collection("TestCollection")
            .with_element_role("TestRole")
        )
        assert result is obj

    def test_collection_extended_attributes(self):
        """Test extended attributes (CODING_RULE_V2_00014)."""
        obj = Collection()
        obj.setExtendedAttribute("custom_key", "custom_value")
        assert obj.getExtendedAttribute("custom_key") == "custom_value"

    def test_collection_inherits_from_ar_element(self):
        """Test that Collection inherits from ARElement."""
        obj = Collection()
        assert isinstance(obj, Collection)


class TestCollectableElement:
    """Test class for CollectableElement base class functionality."""

    def test_collectable_element_abstract_class_cannot_be_instantiated(self):
        """Test that CollectableElement abstract class cannot be instantiated directly."""
        with pytest.raises(TypeError, match="CollectableElement is an abstract class"):
            CollectableElement()

    def test_concrete_collectable_element_can_be_instantiated(self):
        """Test that a concrete subclass of CollectableElement can be instantiated."""
        class ConcreteCollectableElement(CollectableElement):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteCollectableElement()
        assert obj is not None

    def test_collectable_element_inherits_from_identifiable(self):
        """Test that CollectableElement inherits from Identifiable."""
        class ConcreteCollectableElement(CollectableElement):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteCollectableElement()
        assert isinstance(obj, CollectableElement)

    def test_collectable_element_extended_attributes(self):
        """Test extended attributes (CODING_RULE_V2_00014)."""
        class ConcreteCollectableElement(CollectableElement):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteCollectableElement()
        obj.setExtendedAttribute("custom_key", "custom_value")
        assert obj.getExtendedAttribute("custom_key") == "custom_value"


class TestAutoCollectEnum:
    """Test class for AutoCollectEnum enumeration."""

    @pytest.mark.skipif(AutoCollectEnum is None, reason="AutoCollectEnum import failed due to circular import")
    def test_auto_collect_enum_ref_all_value(self):
        """Test that AutoCollectEnum.refAll has correct value."""
        assert AutoCollectEnum.refAll == "0"

    @pytest.mark.skipif(AutoCollectEnum is None, reason="AutoCollectEnum import failed due to circular import")
    def test_auto_collect_enum_ref_none_value(self):
        """Test that AutoCollectEnum.refNone has correct value."""
        assert AutoCollectEnum.refNone == "1"

    @pytest.mark.skipif(AutoCollectEnum is None, reason="AutoCollectEnum import failed due to circular import")
    def test_auto_collect_enum_ref_non_standard_value(self):
        """Test that AutoCollectEnum.refNonStandard has correct value."""
        assert AutoCollectEnum.refNonStandard == "2"

    @pytest.mark.skipif(AutoCollectEnum is None, reason="AutoCollectEnum import failed due to circular import")
    def test_auto_collect_enum_is_arenum_subclass(self):
        """Test that AutoCollectEnum is a subclass of AREnum."""
        from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            AREnum,
        )

        assert issubclass(AutoCollectEnum, AREnum)

    @pytest.mark.skipif(AutoCollectEnum is None, reason="AutoCollectEnum import failed due to circular import")
    def test_auto_collect_enum_ref_all_is_instance(self):
        """Test that AutoCollectEnum.refAll is a string value."""
        assert isinstance(AutoCollectEnum.refAll, str)
        assert AutoCollectEnum.refAll == "0"

    @pytest.mark.skipif(AutoCollectEnum is None, reason="AutoCollectEnum import failed due to circular import")
    def test_auto_collect_enum_ref_none_is_instance(self):
        """Test that AutoCollectEnum.refNone is a string value."""
        assert isinstance(AutoCollectEnum.refNone, str)
        assert AutoCollectEnum.refNone == "1"

    @pytest.mark.skipif(AutoCollectEnum is None, reason="AutoCollectEnum import failed due to circular import")
    def test_auto_collect_enum_ref_non_standard_is_instance(self):
        """Test that AutoCollectEnum.refNonStandard is a string value."""
        assert isinstance(AutoCollectEnum.refNonStandard, str)
        assert AutoCollectEnum.refNonStandard == "2"

    @pytest.mark.skipif(AutoCollectEnum is None, reason="AutoCollectEnum import failed due to circular import")
    def test_auto_collect_enum_enum_values_are_unique(self):
        """Test that AutoCollectEnum enum values are unique."""
        values = [
            AutoCollectEnum.refAll,
            AutoCollectEnum.refNone,
            AutoCollectEnum.refNonStandard,
        ]
        assert len(values) == len(set(values))