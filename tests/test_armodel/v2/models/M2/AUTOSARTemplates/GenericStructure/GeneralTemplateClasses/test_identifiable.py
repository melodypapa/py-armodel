"""
Test module for Identifiable.py.

This file tests all classes defined in Identifiable.py:
- Describable
- Referrable
- ShortNameFragment
- MultilanguageReferrable
- SingleLanguageReferrable
- Identifiable

Tests cover:
- Abstract class instantiation
- Property getter/setter methods
- AUTOSAR-compatible method delegation
- Fluent method chaining
- Type validation
- Extended attributes (CODING_RULE_V2_00014)
"""
import pytest

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Describable,
    Referrable,
    ShortNameFragment,
    MultilanguageReferrable,
    SingleLanguageReferrable,
    Identifiable,
)


class TestDescribable:
    """Test class for Describable base class functionality."""

    def test_describable_abstract_class_cannot_be_instantiated(self):
        """Test that Describable abstract class cannot be instantiated directly."""
        with pytest.raises(TypeError, match="Describable is an abstract class"):
            Describable()

    def test_concrete_describable_can_be_instantiated(self):
        """Test that a concrete subclass of Describable can be instantiated."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        assert obj is not None

    def test_admin_data_property_initialization(self):
        """Test that admin_data property is initialized to None."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        assert obj.admin_data is None

    def test_admin_data_property_setter_none(self):
        """Test admin_data property setter with None."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        obj.admin_data = None
        assert obj.admin_data is None

    def test_category_property_initialization(self):
        """Test that category property is initialized to None."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        assert obj.category is None

    def test_category_property_setter_none(self):
        """Test category property setter with None."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        obj.category = None
        assert obj.category is None

    def test_desc_property_initialization(self):
        """Test that desc property is initialized to None."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        assert obj.desc is None

    def test_desc_property_setter_none(self):
        """Test desc property setter with None."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        obj.desc = None
        assert obj.desc is None

    def test_introduction_property_initialization(self):
        """Test that introduction property is initialized to None."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        assert obj.introduction is None

    def test_introduction_property_setter_none(self):
        """Test introduction property setter with None."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        obj.introduction = None
        assert obj.introduction is None

    def test_get_admin_data_delegates_to_property(self):
        """Test that getAdminData delegates to admin_data property."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        assert obj.getAdminData() is None

    def test_set_admin_data_delegates_to_property(self):
        """Test that setAdminData delegates to admin_data property."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        result = obj.setAdminData(None)
        assert result is obj  # Method chaining
        assert obj.getAdminData() is None

    def test_get_category_delegates_to_property(self):
        """Test that getCategory delegates to category property."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        assert obj.getCategory() is None

    def test_set_category_delegates_to_property(self):
        """Test that setCategory delegates to category property."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        result = obj.setCategory(None)
        assert result is obj  # Method chaining
        assert obj.getCategory() is None

    def test_get_desc_delegates_to_property(self):
        """Test that getDesc delegates to desc property."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        assert obj.getDesc() is None

    def test_set_desc_delegates_to_property(self):
        """Test that setDesc delegates to desc property."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        result = obj.setDesc(None)
        assert result is obj  # Method chaining
        assert obj.getDesc() is None

    def test_get_introduction_delegates_to_property(self):
        """Test that getIntroduction delegates to introduction property."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        assert obj.getIntroduction() is None

    def test_set_introduction_delegates_to_property(self):
        """Test that setIntroduction delegates to introduction property."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        result = obj.setIntroduction(None)
        assert result is obj  # Method chaining
        assert obj.getIntroduction() is None

    def test_with_admin_data_fluent_method(self):
        """Test with_admin_data fluent method (CODING_RULE_V2_00019)."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        result = obj.with_admin_data(None)
        assert result is obj  # Method chaining
        assert obj.admin_data is None

    def test_with_category_fluent_method(self):
        """Test with_category fluent method (CODING_RULE_V2_00019)."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        result = obj.with_category(None)
        assert result is obj  # Method chaining
        assert obj.category is None

    def test_with_desc_fluent_method(self):
        """Test with_desc fluent method (CODING_RULE_V2_00019)."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        result = obj.with_desc(None)
        assert result is obj  # Method chaining
        assert obj.desc is None

    def test_with_introduction_fluent_method(self):
        """Test with_introduction fluent method (CODING_RULE_V2_00019)."""
        class ConcreteDescribable(Describable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteDescribable()
        result = obj.with_introduction(None)
        assert result is obj  # Method chaining
        assert obj.introduction is None


class TestReferrable:
    """Test class for Referrable base class functionality."""

    def test_referrable_abstract_class_cannot_be_instantiated(self):
        """Test that Referrable abstract class cannot be instantiated directly."""
        with pytest.raises(TypeError, match="Referrable is an abstract class"):
            Referrable()

    def test_concrete_referrable_can_be_instantiated(self):
        """Test that a concrete subclass of Referrable can be instantiated."""
        class ConcreteReferrable(Referrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteReferrable()
        assert obj is not None

    def test_short_name_property_initialization(self):
        """Test that short_name property is initialized to None."""
        class ConcreteReferrable(Referrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteReferrable()
        assert obj.short_name is None

    def test_short_name_property_setter_string(self):
        """Test short_name property setter with string value."""
        class ConcreteReferrable(Referrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteReferrable()
        obj.short_name = "TestName"
        assert obj.short_name == "TestName"

    def test_short_name_property_setter_identifier(self):
        """Test short_name property setter with Identifier value."""
        from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            Identifier,
        )

        class ConcreteReferrable(Referrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteReferrable()
        obj.short_name = Identifier().setValue("TestName")
        assert obj.short_name.getValue() == "TestName"

    def test_short_name_property_type_validation(self):
        """Test short_name property setter type validation."""
        class ConcreteReferrable(Referrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteReferrable()
        with pytest.raises(TypeError, match="shortName must be Identifier or str"):
            obj.short_name = 123  # Wrong type

    def test_short_name_fragment_property_initialization(self):
        """Test that short_name_fragment property is initialized to empty list."""
        class ConcreteReferrable(Referrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteReferrable()
        assert obj.short_name_fragment == []

    def test_get_short_name_delegates_to_property(self):
        """Test that getShortName delegates to short_name property."""
        class ConcreteReferrable(Referrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteReferrable()
        obj.short_name = "TestName"
        assert obj.getShortName() == "TestName"

    def test_set_short_name_delegates_to_property(self):
        """Test that setShortName delegates to short_name property."""
        class ConcreteReferrable(Referrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteReferrable()
        result = obj.setShortName("TestName")
        assert result is obj  # Method chaining
        assert obj.getShortName() == "TestName"

    def test_get_short_name_fragment_delegates_to_property(self):
        """Test that getShortNameFragment delegates to short_name_fragment property."""
        class ConcreteReferrable(Referrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteReferrable()
        assert obj.getShortNameFragment() == []

    def test_with_short_name_fluent_method(self):
        """Test with_short_name fluent method (CODING_RULE_V2_00019)."""
        class ConcreteReferrable(Referrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteReferrable()
        result = obj.with_short_name("TestName")
        assert result is obj  # Method chaining
        assert obj.short_name == "TestName"


class TestShortNameFragment:
    """Test class for ShortNameFragment functionality."""

    def test_short_name_fragment_can_be_instantiated(self):
        """Test that ShortNameFragment can be instantiated."""
        obj = ShortNameFragment()
        assert obj is not None

    def test_fragment_property_initialization(self):
        """Test that fragment property is initialized to None."""
        obj = ShortNameFragment()
        # Access the property to trigger initialization
        _ = obj.fragment
        assert obj.fragment is None

    def test_fragment_property_setter_string(self):
        """Test fragment property setter with string value."""
        obj = ShortNameFragment()
        obj.fragment = "TestFragment"
        assert obj.fragment == "TestFragment"

    def test_fragment_property_setter_identifier(self):
        """Test fragment property setter with plain string."""
        obj = ShortNameFragment()
        obj.fragment = "TestFragment"
        assert obj.fragment == "TestFragment"

    def test_fragment_property_type_validation(self):
        """Test fragment property setter type validation."""
        obj = ShortNameFragment()
        with pytest.raises(TypeError, match="fragment must be Identifier or str"):
            obj.fragment = 123  # Wrong type

    def test_role_property_initialization(self):
        """Test that role property is initialized to None."""
        obj = ShortNameFragment()
        # Access the property to trigger initialization
        _ = obj.role
        assert obj.role is None

    def test_role_property_setter_string(self):
        """Test role property setter with string value."""
        obj = ShortNameFragment()
        obj.role = "TestRole"
        assert obj.role == "TestRole"

    def test_role_property_setter_string_type(self):
        """Test role property setter with plain string."""
        obj = ShortNameFragment()
        obj.role = "TestRole"
        assert obj.role == "TestRole"

    def test_role_property_type_validation(self):
        """Test role property setter type validation."""
        obj = ShortNameFragment()
        with pytest.raises(TypeError, match="role must be String or str"):
            obj.role = 123  # Wrong type

    def test_get_fragment_delegates_to_property(self):
        """Test that getFragment delegates to fragment property."""
        obj = ShortNameFragment()
        obj.fragment = "TestFragment"
        assert obj.getFragment() == "TestFragment"

    def test_set_fragment_delegates_to_property(self):
        """Test that setFragment delegates to fragment property."""
        obj = ShortNameFragment()
        result = obj.setFragment("TestFragment")
        assert result is obj  # Method chaining
        assert obj.getFragment() == "TestFragment"

    def test_get_role_delegates_to_property(self):
        """Test that getRole delegates to role property."""
        obj = ShortNameFragment()
        obj.role = "TestRole"
        assert obj.getRole() == "TestRole"

    def test_set_role_delegates_to_property(self):
        """Test that setRole delegates to role property."""
        obj = ShortNameFragment()
        result = obj.setRole("TestRole")
        assert result is obj  # Method chaining
        assert obj.getRole() == "TestRole"

    def test_with_fragment_fluent_method(self):
        """Test with_fragment fluent method (CODING_RULE_V2_00019)."""
        obj = ShortNameFragment()
        result = obj.with_fragment("TestFragment")
        assert result is obj  # Method chaining
        assert obj.fragment == "TestFragment"

    def test_with_role_fluent_method(self):
        """Test with_role fluent method (CODING_RULE_V2_00019)."""
        obj = ShortNameFragment()
        result = obj.with_role("TestRole")
        assert result is obj  # Method chaining
        assert obj.role == "TestRole"


class TestMultilanguageReferrable:
    """Test class for MultilanguageReferrable base class functionality."""

    def test_multilanguage_referrable_abstract_class_cannot_be_instantiated(self):
        """Test that MultilanguageReferrable abstract class cannot be instantiated directly."""
        with pytest.raises(
            TypeError, match="MultilanguageReferrable is an abstract class"
        ):
            MultilanguageReferrable()

    def test_concrete_multilanguage_referrable_can_be_instantiated(self):
        """Test that a concrete subclass of MultilanguageReferrable can be instantiated."""
        class ConcreteMultilanguageReferrable(MultilanguageReferrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteMultilanguageReferrable()
        assert obj is not None

    def test_long_name_property_initialization(self):
        """Test that long_name property is initialized to None."""
        class ConcreteMultilanguageReferrable(MultilanguageReferrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteMultilanguageReferrable()
        assert obj.long_name is None

    def test_long_name_property_setter_none(self):
        """Test long_name property setter with None."""
        class ConcreteMultilanguageReferrable(MultilanguageReferrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteMultilanguageReferrable()
        obj.long_name = None
        assert obj.long_name is None

    def test_get_long_name_delegates_to_property(self):
        """Test that getLongName delegates to long_name property."""
        class ConcreteMultilanguageReferrable(MultilanguageReferrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteMultilanguageReferrable()
        assert obj.getLongName() is None

    def test_set_long_name_delegates_to_property(self):
        """Test that setLongName delegates to long_name property."""
        class ConcreteMultilanguageReferrable(MultilanguageReferrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteMultilanguageReferrable()
        result = obj.setLongName(None)
        assert result is obj  # Method chaining
        assert obj.getLongName() is None

    def test_with_long_name_fluent_method(self):
        """Test with_long_name fluent method (CODING_RULE_V2_00019)."""
        class ConcreteMultilanguageReferrable(MultilanguageReferrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteMultilanguageReferrable()
        result = obj.with_long_name(None)
        assert result is obj  # Method chaining
        assert obj.long_name is None


class TestSingleLanguageReferrable:
    """Test class for SingleLanguageReferrable base class functionality."""

    def test_single_language_referrable_abstract_class_cannot_be_instantiated(
        self,
    ):
        """Test that SingleLanguageReferrable abstract class cannot be instantiated directly."""
        with pytest.raises(
            TypeError, match="SingleLanguageReferrable is an abstract class"
        ):
            SingleLanguageReferrable()

    def test_concrete_single_language_referrable_can_be_instantiated(self):
        """Test that a concrete subclass of SingleLanguageReferrable can be instantiated."""
        class ConcreteSingleLanguageReferrable(SingleLanguageReferrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteSingleLanguageReferrable()
        assert obj is not None

    def test_long_name1_property_initialization(self):
        """Test that long_name1 property is initialized to None."""
        class ConcreteSingleLanguageReferrable(SingleLanguageReferrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteSingleLanguageReferrable()
        assert obj.long_name1 is None

    def test_long_name1_property_setter_none(self):
        """Test long_name1 property setter with None."""
        class ConcreteSingleLanguageReferrable(SingleLanguageReferrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteSingleLanguageReferrable()
        obj.long_name1 = None
        assert obj.long_name1 is None

    def test_get_long_name1_delegates_to_property(self):
        """Test that getLongName1 delegates to long_name1 property."""
        class ConcreteSingleLanguageReferrable(SingleLanguageReferrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteSingleLanguageReferrable()
        assert obj.getLongName1() is None

    def test_set_long_name1_delegates_to_property(self):
        """Test that setLongName1 delegates to long_name1 property."""
        class ConcreteSingleLanguageReferrable(SingleLanguageReferrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteSingleLanguageReferrable()
        result = obj.setLongName1(None)
        assert result is obj  # Method chaining
        assert obj.getLongName1() is None

    def test_with_long_name1_fluent_method(self):
        """Test with_long_name1 fluent method (CODING_RULE_V2_00019)."""
        class ConcreteSingleLanguageReferrable(SingleLanguageReferrable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteSingleLanguageReferrable()
        result = obj.with_long_name1(None)
        assert result is obj  # Method chaining
        assert obj.long_name1 is None


class TestIdentifiable:
    """Test class for Identifiable base class functionality."""

    def test_identifiable_abstract_class_cannot_be_instantiated(self):
        """Test that Identifiable abstract class cannot be instantiated directly."""
        with pytest.raises(TypeError, match="Identifiable is an abstract class"):
            Identifiable()

    def test_concrete_identifiable_can_be_instantiated(self):
        """Test that a concrete subclass of Identifiable can be instantiated."""
        class ConcreteIdentifiable(Identifiable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteIdentifiable()
        assert obj is not None

    def test_admin_data_property_initialization(self):
        """Test that admin_data property is initialized to None."""
        class ConcreteIdentifiable(Identifiable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteIdentifiable()
        assert obj.admin_data is None

    def test_annotation_property_initialization(self):
        """Test annotation property initialization."""
        # Access the property to trigger initialization
        _ = self.obj.annotation
        assert self.obj.annotation == []

    def test_inherited_from_multilanguage_referrable(self):
        """Test that Identifiable inherits from MultilanguageReferrable."""
        class ConcreteIdentifiable(Identifiable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteIdentifiable()
        # Should have properties from MultilanguageReferrable
        assert hasattr(obj, "long_name")
        assert obj.long_name is None

    def test_inherited_from_referrable(self):
        """Test that Identifiable inherits from Referrable."""
        class ConcreteIdentifiable(Identifiable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteIdentifiable()
        # Should have properties from Referrable
        assert hasattr(obj, "short_name")
        assert hasattr(obj, "short_name_fragment")

    def test_extended_attributes(self):
        """Test extended attributes (CODING_RULE_V2_00014)."""
        class ConcreteIdentifiable(Identifiable):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteIdentifiable()
        obj.setExtendedAttribute("custom_key", "custom_value")
        assert obj.getExtendedAttribute("custom_key") == "custom_value"