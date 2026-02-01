"""
Test cases for the HwElementCategory module.
These tests ensure 100% code coverage for the HwType, HwAttributeDef, and HwCategory classes.
"""

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwType, HwAttributeDef, HwCategory
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwAttributeValue import HwAttributeLiteralDef


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


if __name__ == '__main__':
    test_hw_type_init()
    test_hw_attribute_def_init()
    test_hw_attribute_def_getters_and_setters()
    test_hw_category_init()
    test_hw_category_getters_and_create_hw_attribute_def()
    print("All HwElementCategory tests passed!")