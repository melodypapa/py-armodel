from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import (
    HwAttributeDef,
    HwAttributeLiteralDef,
    HwAttributeValue,
    HwCategory,
    HwType,
)

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


def test_hw_attribute_def_init():
    """
    Test initialization of HwAttributeDef class.

    Test Steps:
    1. Create a HwAttributeDef instance with parent and short_name
    2. Verify default attributes are set correctly
    """
    # Create a mock parent object
    parent = object()

    # Initialize HwAttributeDef
    hw_attr_def = HwAttributeDef(parent, "test_hw_attr_def")

    # Verify initial values
    assert hw_attr_def.parent == parent
    assert hw_attr_def.short_name == "test_hw_attr_def"
    assert hw_attr_def.hwAttributeLiterals == []
    assert hw_attr_def.isRequired is None
    assert hw_attr_def.unitRef is None


def test_hw_attribute_def_getters_and_setters():
    """
    Test all getter and setter methods of HwAttributeDef class.

    Test Steps:
    1. Create a HwAttributeDef instance
    2. Test setting and getting hwAttributeLiterals
    3. Test setting and getting isRequired
    4. Test setting and getting unitRef
    5. Verify method chaining (return self)
    """
    hw_attr_def = HwAttributeDef(None, "test_hw_attr_def")

    # Test hwAttributeLiterals setter and getter
    test_literals = [HwAttributeLiteralDef(None, "literal1"), HwAttributeLiteralDef(None, "literal2")]
    return_value = hw_attr_def.setHwAttributeLiterals(test_literals)
    assert return_value == hw_attr_def  # Verify method chaining
    assert hw_attr_def.getHwAttributeLiterals() == test_literals

    # Test isRequired setter and getter
    test_required = True
    return_value = hw_attr_def.setIsRequired(test_required)
    assert return_value == hw_attr_def  # Verify method chaining
    assert hw_attr_def.getIsRequired() == test_required

    # Test unitRef setter and getter
    test_unit_ref = "test_unit_ref"
    return_value = hw_attr_def.setUnitRef(test_unit_ref)
    assert return_value == hw_attr_def  # Verify method chaining
    assert hw_attr_def.getUnitRef() == test_unit_ref

    # Test with None values (should not set)
    original_literals = hw_attr_def.getHwAttributeLiterals()
    hw_attr_def.setHwAttributeLiterals(None)
    assert hw_attr_def.getHwAttributeLiterals() == original_literals  # Should remain unchanged

    original_required = hw_attr_def.getIsRequired()
    hw_attr_def.setIsRequired(None)
    assert hw_attr_def.getIsRequired() == original_required  # Should remain unchanged

    original_unit_ref = hw_attr_def.getUnitRef()
    hw_attr_def.setUnitRef(None)
    assert hw_attr_def.getUnitRef() == original_unit_ref  # Should remain unchanged


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


if __name__ == "__main__":
    test_hw_type_init()
    test_hw_attribute_def_init()
    test_hw_attribute_def_getters_and_setters()
    test_hw_category_init()
    test_hw_category_getters_and_create_hw_attribute_def()
    print("All HwElementCategory tests passed!")


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
