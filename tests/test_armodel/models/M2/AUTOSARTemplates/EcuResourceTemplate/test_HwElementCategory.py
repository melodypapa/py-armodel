from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import (
    HwAttributeDef,
    HwAttributeLiteralDef,
    HwAttributeValue,
    HwCategory,
    HwType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType


def make_ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


"""
Test cases for the HwElementCategory module.
These tests ensure 100% code coverage for the HwType, HwAttributeDef, and HwCategory classes.
"""


def test_hw_type_init():
    """
    Test initialization of HwType class.

    Test Steps:
    1. Create a HwType instance with parent and short_name
    2. Verify basic attributes are set correctly
    """
    # Create a mock parent object
    parent = object()

    # Initialize HwType
    hw_type = HwType(parent, "test_hw_type")

    # Verify initial values
    assert hw_type.parent == parent
    assert hw_type.short_name == "test_hw_type"


def test_hw_type_is_concrete():
    """HwType must be instantiable although its base HwDescriptionEntity is abstract."""
    parent = object()
    hw_type = HwType(parent, "concrete_hw_type")
    assert isinstance(hw_type, HwType)


def test_hw_type_inherited_members_round_trip():
    """
    HwType inherits the HwDescriptionEntity aggregations/associations. Verify they
    round-trip through a HwType instance (herit/marker-subclass behavior).
    """
    hw_type = HwType(None, "typed")

    attr_value = HwAttributeValue()
    attr_value.setHwAttributeDefRef("def_ref").setValue("v")
    hw_type.addHwAttributeValue(attr_value)
    assert hw_type.getHwAttributeValues() == [attr_value]

    hw_type.addHwCategoryRef("cat_ref_a")
    hw_type.addHwCategoryRef("cat_ref_b")
    assert hw_type.getHwCategoryRefs() == ["cat_ref_a", "cat_ref_b"]

    return_value = hw_type.setHwTypeRef("type_ref")
    assert return_value == hw_type  # method chaining
    assert hw_type.getHwTypeRef() == "type_ref"


def test_hw_type_inherited_members_none_noop():
    """Setters inherited from HwDescriptionEntity must ignore None (no-op)."""
    hw_type = HwType(None, "typed")

    original_refs = hw_type.getHwCategoryRefs()
    hw_type.addHwCategoryRef(None)
    assert hw_type.getHwCategoryRefs() == original_refs

    hw_type.setHwTypeRef("type_ref")
    original_type_ref = hw_type.getHwTypeRef()
    hw_type.setHwTypeRef(None)
    assert hw_type.getHwTypeRef() == original_type_ref


HW_ATTRIBUTE_DEF_NOTE = (
    "This metaclass represents the ability to define a particular hardware attribute. "
    "The category of this element defines the type of the attributeValue. "
    "If the category is Enumeration the hwAttributeEnumerationLiterals specify the available literals."
)


def test_hw_attribute_def_docstring_verbatim():
    """Class docstring must equal the Table 2.13 Note verbatim (XSD authoritative)."""
    assert HwAttributeDef.__doc__.strip() == HW_ATTRIBUTE_DEF_NOTE


def test_hw_attribute_def_init_doc_is_none():
    assert HwAttributeDef.__init__.__doc__ is None


def test_hw_attribute_def_is_concrete_identifiable_subclass():
    hw_attr_def = HwAttributeDef(None, "attr_def")
    assert isinstance(hw_attr_def, HwAttributeDef)
    assert issubclass(HwAttributeDef, Identifiable)


def test_hw_attribute_def_defaults():
    """
    Test initialization of HwAttributeDef class (Table 2.13 displayed order:
    hwAttributeLiteral (* aggr), isRequired (0..1 attr), unit (0..1 ref)).
    """
    parent = object()
    hw_attr_def = HwAttributeDef(parent, "test_hw_attr_def")

    assert hw_attr_def.parent == parent
    assert hw_attr_def.short_name == "test_hw_attr_def"
    assert hw_attr_def.hwAttributeLiterals == []
    assert hw_attr_def.isRequired is None
    assert hw_attr_def.unitRef is None


def test_hw_attribute_def_setters_round_trip():
    """Get/set round-trips must return the same instance and support chaining."""
    hw_attr_def = HwAttributeDef(None, "test_hw_attr_def")

    required = Boolean()
    required.setValue(True)
    assert hw_attr_def.setIsRequired(required) is hw_attr_def
    assert hw_attr_def.getIsRequired() is required

    unit_ref = make_ref("/Units/Length", "UNIT")
    assert hw_attr_def.setUnitRef(unit_ref) is hw_attr_def
    assert hw_attr_def.getUnitRef() is unit_ref

    literals = [HwAttributeLiteralDef(None, "literal1"), HwAttributeLiteralDef(None, "literal2")]
    assert hw_attr_def.setHwAttributeLiterals(literals) is hw_attr_def
    assert hw_attr_def.getHwAttributeLiterals() is literals


def test_hw_attribute_def_setters_none_noop():
    """A None value is a no-op and does not overwrite an existing value."""
    hw_attr_def = HwAttributeDef(None, "test_hw_attr_def")

    required = Boolean()
    required.setValue(True)
    hw_attr_def.setIsRequired(required)
    hw_attr_def.setIsRequired(None)
    assert hw_attr_def.getIsRequired() is required

    unit_ref = make_ref("/Units/Length", "UNIT")
    hw_attr_def.setUnitRef(unit_ref)
    hw_attr_def.setUnitRef(None)
    assert hw_attr_def.getUnitRef() is unit_ref

    literals = [HwAttributeLiteralDef(None, "literal1")]
    hw_attr_def.setHwAttributeLiterals(literals)
    hw_attr_def.setHwAttributeLiterals(None)
    assert hw_attr_def.getHwAttributeLiterals() is literals


def test_hw_attribute_def_add_hw_attribute_literal():
    """The * add accessor must append, ignore None and return self."""
    hw_attr_def = HwAttributeDef(None, "test_hw_attr_def")

    literal1 = HwAttributeLiteralDef(None, "literal1")
    assert hw_attr_def.addHwAttributeLiteral(literal1) is hw_attr_def
    assert hw_attr_def.getHwAttributeLiterals() == [literal1]

    literal2 = HwAttributeLiteralDef(None, "literal2")
    hw_attr_def.addHwAttributeLiteral(literal2)
    assert hw_attr_def.getHwAttributeLiterals() == [literal1, literal2]

    hw_attr_def.addHwAttributeLiteral(None)
    assert hw_attr_def.getHwAttributeLiterals() == [literal1, literal2]


def test_hw_attribute_def_create_hw_attribute_literal():
    """createHwAttributeLiteral must guard duplicates via IsElementExists."""
    hw_attr_def = HwAttributeDef(None, "test_hw_attr_def")

    literal = hw_attr_def.createHwAttributeLiteral("literal1")
    assert literal.short_name == "literal1"
    assert literal in hw_attr_def.getHwAttributeLiterals()

    assert hw_attr_def.createHwAttributeLiteral("literal1") is literal
    assert len(hw_attr_def.getHwAttributeLiterals()) == 1


def test_hw_category_init():
    """
    Test initialization of HwCategory class.

    Test Steps:
    1. Create a HwCategory instance with parent and short_name
    2. Verify default attributes are set correctly
    """
    # Create a mock parent object
    parent = object()

    # Initialize HwCategory
    hw_category = HwCategory(parent, "test_hw_category")

    # Verify initial values
    assert hw_category.parent == parent
    assert hw_category.short_name == "test_hw_category"
    assert hw_category.hwAttributeDefs == []


def test_hw_category_getters_and_create_hw_attribute_def():
    """
    Test getter and createHwAttributeDef method of HwCategory class.

    Test Steps:
    1. Create a HwCategory instance
    2. Test getting hwAttributeDefs
    3. Test creating a new HwAttributeDef
    4. Verify the created HwAttributeDef is added to the category
    """
    hw_category = HwCategory(None, "test_hw_category")

    # Test getHwAttributeDefs
    assert hw_category.getHwAttributeDefs() == []

    # Test createHwAttributeDef
    new_attr_def = hw_category.createHwAttributeDef("new_attr_def")
    assert new_attr_def is not None
    assert new_attr_def.short_name == "new_attr_def"
    assert new_attr_def in hw_category.getHwAttributeDefs()

    # Test creating another one with the same name (should return existing)
    same_attr_def = hw_category.createHwAttributeDef("new_attr_def")
    assert same_attr_def == new_attr_def  # Should return the same instance


"""
Test cases for the HwAttributeValue module.
These tests ensure 100% code coverage for the HwAttributeValue and HwAttributeLiteralDef classes.
"""


def test_hw_attribute_value_init():
    """
    Test initialization of HwAttributeValue class.

    Test Steps:
    1. Create a HwAttributeValue instance
    2. Verify default attributes are set correctly
    """
    # Initialize HwAttributeValue
    hw_attr_value = HwAttributeValue()

    # Verify initial values
    assert hw_attr_value.parent is None
    assert hw_attr_value.hwAttributeDefRef is None
    assert hw_attr_value.value is None


def test_hw_attribute_value_getters_and_setters():
    """
    Test all getter and setter methods of HwAttributeValue class.

    Test Steps:
    1. Create a HwAttributeValue instance
    2. Test setting and getting the hwAttributeDefRef
    3. Test setting and getting the value
    4. Verify method chaining (return self)
    """
    hw_attr_value = HwAttributeValue()

    # Test hwAttributeDefRef setter and getter
    test_ref = "test_ref"
    return_value = hw_attr_value.setHwAttributeDefRef(test_ref)
    assert return_value == hw_attr_value  # Verify method chaining
    assert hw_attr_value.getHwAttributeDefRef() == test_ref

    # Test value setter and getter
    test_value = "test_value"
    return_value = hw_attr_value.setValue(test_value)
    assert return_value == hw_attr_value  # Verify method chaining
    assert hw_attr_value.getValue() == test_value

    # Test with None values (should not set)
    original_ref = hw_attr_value.getHwAttributeDefRef()
    hw_attr_value.setHwAttributeDefRef(None)
    assert hw_attr_value.getHwAttributeDefRef() == original_ref  # Should remain unchanged

    original_value = hw_attr_value.getValue()
    hw_attr_value.setValue(None)
    assert hw_attr_value.getValue() == original_value  # Should remain unchanged


def test_hw_attribute_literal_def_init():
    """
    Test initialization of HwAttributeLiteralDef class.

    Test Steps:
    1. Create a HwAttributeLiteralDef instance with parent and short_name
    2. Verify default attributes are set correctly
    """
    # Create a mock parent object
    parent = object()

    # Initialize HwAttributeLiteralDef
    hw_attr_literal = HwAttributeLiteralDef(parent, "test_hw_attr_literal")

    # Verify initial values
    assert hw_attr_literal.parent == parent
    assert hw_attr_literal.short_name == "test_hw_attr_literal"
    assert hw_attr_literal.value is None


def test_hw_attribute_literal_def_getters_and_setters():
    """
    Test all getter and setter methods of HwAttributeLiteralDef class.

    Test Steps:
    1. Create a HwAttributeLiteralDef instance
    2. Test setting and getting the value
    3. Verify method chaining (return self)
    """
    hw_attr_literal = HwAttributeLiteralDef(None, "test_hw_attr_literal")

    # Test value setter and getter
    test_value = "test_literal_value"
    return_value = hw_attr_literal.setValue(test_value)
    assert return_value == hw_attr_literal  # Verify method chaining
    assert hw_attr_literal.getValue() == test_value

    # Test with None values (should not set)
    original_value = hw_attr_literal.getValue()
    hw_attr_literal.setValue(None)
    assert hw_attr_literal.getValue() == original_value  # Should remain unchanged


if __name__ == "__main__":
    test_hw_attribute_value_init()
    test_hw_attribute_value_getters_and_setters()
    test_hw_attribute_literal_def_init()
    test_hw_attribute_literal_def_getters_and_setters()
    print("All HwAttributeValue tests passed!")
