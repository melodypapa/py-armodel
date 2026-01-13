"""
Test cases for the EcuResourceTemplate __init__.py module.
These tests ensure 100% code coverage for the HwDescriptionEntity, HwPin, HwPinGroupContent, HwPinGroup, and HwElement classes.
"""

from src.armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwDescriptionEntity, HwPin, HwPinGroupContent, HwPinGroup, HwElement
from src.armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwAttributeValue import HwAttributeValue
from src.armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementConnector import HwElementConnector


def test_hw_description_entity_init():
    """
    Test initialization of HwDescriptionEntity class.
    
    Test Steps:
    1. Create a HwDescriptionEntity instance with parent and short_name
    2. Verify default attributes are set correctly
    """
    # Create a mock parent object
    parent = object()
    
    # Initialize HwDescriptionEntity
    hw_desc_entity = HwDescriptionEntity(parent, "test_hw_desc_entity")
    
    # Verify initial values
    assert hw_desc_entity.parent == parent
    assert hw_desc_entity.short_name == "test_hw_desc_entity"
    assert hw_desc_entity.hwAttributeValues == []
    assert hw_desc_entity.hwCategoryRefs == []
    assert hw_desc_entity.hwTypeRef is None


def test_hw_description_entity_getters_and_setters():
    """
    Test all getter and setter methods of HwDescriptionEntity class.
    
    Test Steps:
    1. Create a HwDescriptionEntity instance
    2. Test setting and getting hwAttributeValues
    3. Test adding and getting hwCategoryRefs
    4. Test setting and getting hwTypeRef
    5. Verify method chaining (return self)
    """
    hw_desc_entity = HwDescriptionEntity(None, "test_hw_desc_entity")
    
    # Test hwAttributeValues setter and getter
    test_attr_values = [HwAttributeValue(None, "attr1"), HwAttributeValue(None, "attr2")]
    return_value = hw_desc_entity.setHwAttributeValues(test_attr_values)
    assert return_value == hw_desc_entity  # Verify method chaining
    assert hw_desc_entity.getHwAttributeValues() == test_attr_values
    
    # Test addHwCategoryRef and getHwCategoryRefs
    test_category_ref = "test_category_ref"
    return_value = hw_desc_entity.addHwCategoryRef(test_category_ref)
    assert return_value == hw_desc_entity  # Verify method chaining
    assert test_category_ref in hw_desc_entity.getHwCategoryRefs()
    
    # Test hwTypeRef setter and getter
    test_type_ref = "test_type_ref"
    return_value = hw_desc_entity.setHwTypeRef(test_type_ref)
    assert return_value == hw_desc_entity  # Verify method chaining
    assert hw_desc_entity.getHwTypeRef() == test_type_ref
    
    # Test with None values (should not set/add)
    original_attr_values = hw_desc_entity.getHwAttributeValues()
    hw_desc_entity.setHwAttributeValues(None)
    assert hw_desc_entity.getHwAttributeValues() == original_attr_values  # Should remain unchanged
    
    original_type_ref = hw_desc_entity.getHwTypeRef()
    hw_desc_entity.setHwTypeRef(None)
    assert hw_desc_entity.getHwTypeRef() == original_type_ref  # Should remain unchanged
    
    original_category_refs_count = len(hw_desc_entity.getHwCategoryRefs())
    hw_desc_entity.addHwCategoryRef(None)
    assert len(hw_desc_entity.getHwCategoryRefs()) == original_category_refs_count  # Should remain unchanged


def test_hw_pin_init():
    """
    Test initialization of HwPin class.
    
    Test Steps:
    1. Create a HwPin instance with parent and short_name
    2. Verify default attributes are set correctly
    """
    # Create a mock parent object
    parent = object()
    
    # Initialize HwPin
    hw_pin = HwPin(parent, "test_hw_pin")
    
    # Verify initial values
    assert hw_pin.parent == parent
    assert hw_pin.short_name == "test_hw_pin"
    assert hw_pin.hwAttributeValues == []
    assert hw_pin.hwCategoryRefs == []
    assert hw_pin.hwTypeRef is None
    assert hw_pin.functionName is None
    assert hw_pin.packagingPinName is None
    assert hw_pin.pinNumber is None


def test_hw_pin_getters_and_setters():
    """
    Test all getter and setter methods of HwPin class.
    
    Test Steps:
    1. Create a HwPin instance
    2. Test setting and getting functionName
    3. Test setting and getting packagingPinName
    4. Test setting and getting pinNumber
    5. Verify method chaining (return self)
    """
    hw_pin = HwPin(None, "test_hw_pin")
    
    # Test functionName setter and getter
    test_function_name = "test_function"
    return_value = hw_pin.setFunctionName(test_function_name)
    assert return_value == hw_pin  # Verify method chaining
    assert hw_pin.getFunctionName() == test_function_name
    
    # Test packagingPinName setter and getter
    test_packaging_name = "test_packaging"
    return_value = hw_pin.setPackagingPinName(test_packaging_name)
    assert return_value == hw_pin  # Verify method chaining
    assert hw_pin.getPackagingPinName() == test_packaging_name
    
    # Test pinNumber setter and getter
    test_pin_number = 123
    return_value = hw_pin.setPinNumber(test_pin_number)
    assert return_value == hw_pin  # Verify method chaining
    assert hw_pin.getPinNumber() == test_pin_number
    
    # Test with None values (should not set)
    original_function_name = hw_pin.getFunctionName()
    hw_pin.setFunctionName(None)
    assert hw_pin.getFunctionName() == original_function_name  # Should remain unchanged
    
    original_packaging_name = hw_pin.getPackagingPinName()
    hw_pin.setPackagingPinName(None)
    assert hw_pin.getPackagingPinName() == original_packaging_name  # Should remain unchanged
    
    original_pin_number = hw_pin.getPinNumber()
    hw_pin.setPinNumber(None)
    assert hw_pin.getPinNumber() == original_pin_number  # Should remain unchanged


def test_hw_pin_group_content_init():
    """
    Test initialization of HwPinGroupContent class.
    
    Test Steps:
    1. Create a HwPinGroupContent instance
    2. Verify default attributes are set correctly
    """
    # Initialize HwPinGroupContent
    hw_pin_group_content = HwPinGroupContent()
    
    # Verify initial values
    assert hw_pin_group_content.hwPin is None
    assert hw_pin_group_content.hwPinGroup is None


def test_hw_pin_group_content_getters_and_setters():
    """
    Test all getter and setter methods of HwPinGroupContent class.
    
    Test Steps:
    1. Create a HwPinGroupContent instance
    2. Test createHwPin method
    3. Test setHwPinGroup and getHwPinGroup methods
    4. Verify method chaining (return self)
    """
    from src.armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinGroup
    
    hw_pin_group_content = HwPinGroupContent()
    
    # Test createHwPin
    new_pin = hw_pin_group_content.createHwPin("new_pin")
    assert new_pin is not None
    assert new_pin.short_name == "new_pin"
    assert hw_pin_group_content.getHwPin() == new_pin
    
    # Test getHwPin
    assert hw_pin_group_content.getHwPin() == new_pin
    
    # Test setHwPinGroup and getHwPinGroup
    hw_pin_group = HwPinGroup(None, "test_pin_group")
    return_value = hw_pin_group_content.setHwPinGroup(hw_pin_group)
    assert return_value == hw_pin_group_content  # Verify method chaining
    assert hw_pin_group_content.getHwPinGroup() == hw_pin_group
    
    # Test with None values (should not set)
    original_pin_group = hw_pin_group_content.getHwPinGroup()
    hw_pin_group_content.setHwPinGroup(None)
    assert hw_pin_group_content.getHwPinGroup() == original_pin_group  # Should remain unchanged


def test_hw_pin_group_init():
    """
    Test initialization of HwPinGroup class.
    
    Test Steps:
    1. Create a HwPinGroup instance with parent and short_name
    2. Verify default attributes are set correctly
    """
    # Create a mock parent object
    parent = object()
    
    # Initialize HwPinGroup
    hw_pin_group = HwPinGroup(parent, "test_hw_pin_group")
    
    # Verify initial values
    assert hw_pin_group.parent == parent
    assert hw_pin_group.short_name == "test_hw_pin_group"
    assert hw_pin_group.hwAttributeValues == []
    assert hw_pin_group.hwCategoryRefs == []
    assert hw_pin_group.hwTypeRef is None
    assert hw_pin_group.hwPinGroupContent is None


def test_hw_pin_group_getters_and_setters():
    """
    Test all getter and setter methods of HwPinGroup class.
    
    Test Steps:
    1. Create a HwPinGroup instance
    2. Test setting and getting hwPinGroupContent
    3. Verify method chaining (return self)
    """
    hw_pin_group = HwPinGroup(None, "test_hw_pin_group")
    
    # Test hwPinGroupContent setter and getter
    from src.armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinGroupContent
    test_content = HwPinGroupContent()
    return_value = hw_pin_group.setHwPinGroupContent(test_content)
    assert return_value == hw_pin_group  # Verify method chaining
    assert hw_pin_group.getHwPinGroupContent() == test_content
    
    # Test with None values (should not set)
    original_content = hw_pin_group.getHwPinGroupContent()
    hw_pin_group.setHwPinGroupContent(None)
    assert hw_pin_group.getHwPinGroupContent() == original_content  # Should remain unchanged


def test_hw_element_init():
    """
    Test initialization of HwElement class.
    
    Test Steps:
    1. Create a HwElement instance with parent and short_name
    2. Verify default attributes are set correctly
    """
    # Create a mock parent object
    parent = object()
    
    # Initialize HwElement
    hw_element = HwElement(parent, "test_hw_element")
    
    # Verify initial values
    assert hw_element.parent == parent
    assert hw_element.short_name == "test_hw_element"
    assert hw_element.hwAttributeValues == []
    assert hw_element.hwCategoryRefs == []
    assert hw_element.hwTypeRef is None
    assert hw_element.hwElementConnections == []
    assert hw_element.hwPinGroups == []
    assert hw_element.nestedElementRefs == []


def test_hw_element_getters_and_setters():
    """
    Test all getter and setter methods of HwElement class.
    
    Test Steps:
    1. Create a HwElement instance
    2. Test setting and getting hwElementConnections
    3. Test createHwPinGroup method
    4. Test setting and getting nestedElementRefs
    5. Verify method chaining (return self)
    """
    from src.armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementConnector import HwElementConnector
    
    hw_element = HwElement(None, "test_hw_element")
    
    # Test hwElementConnections setter and getter
    test_connections = [HwElementConnector(None, "conn1"), HwElementConnector(None, "conn2")]
    return_value = hw_element.setHwElementConnections(test_connections)
    assert return_value == hw_element  # Verify method chaining
    assert hw_element.getHwElementConnections() == test_connections
    
    # Test createHwPinGroup
    new_pin_group = hw_element.createHwPinGroup("new_pin_group")
    assert new_pin_group is not None
    assert new_pin_group.short_name == "new_pin_group"
    assert new_pin_group in hw_element.getHwPinGroups()
    
    # Test nestedElementRefs setter and getter
    test_nested_refs = ["ref1", "ref2", "ref3"]
    return_value = hw_element.setNestedElementRefs(test_nested_refs)
    assert return_value == hw_element  # Verify method chaining
    assert hw_element.getNestedElementRefs() == test_nested_refs
    
    # Test with None values (should not set)
    original_connections = hw_element.getHwElementConnections()
    hw_element.setHwElementConnections(None)
    assert hw_element.getHwElementConnections() == original_connections  # Should remain unchanged
    
    original_nested_refs = hw_element.getNestedElementRefs()
    hw_element.setNestedElementRefs(None)
    assert hw_element.getNestedElementRefs() == original_nested_refs  # Should remain unchanged


if __name__ == '__main__':
    test_hw_description_entity_init()
    test_hw_description_entity_getters_and_setters()
    test_hw_pin_init()
    test_hw_pin_getters_and_setters()
    test_hw_pin_group_content_init()
    test_hw_pin_group_content_getters_and_setters()
    test_hw_pin_group_init()
    test_hw_pin_group_getters_and_setters()
    test_hw_element_init()
    test_hw_element_getters_and_setters()
    print("All EcuResourceTemplate __init__ tests passed!")