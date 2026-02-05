"""
Test cases for the HwAttributeValue module.
These tests ensure 100% code coverage for the HwAttributeValue and HwAttributeLiteralDef classes.
"""

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import (
    HwAttributeValue,
    HwAttributeLiteralDef,
)


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


if __name__ == '__main__':
    test_hw_attribute_value_init()
    test_hw_attribute_value_getters_and_setters()
    test_hw_attribute_literal_def_init()
    test_hw_attribute_literal_def_getters_and_setters()
    print("All HwAttributeValue tests passed!")