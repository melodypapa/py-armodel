"""
Test cases for the EcuResourceTemplate __init__.py module.
These tests ensure 100% code coverage for the HwDescriptionEntity, HwPin, HwPinGroupContent, HwPinGroup, and HwElement classes.
"""

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwElement, HwPin, HwPinGroup, HwPinGroupContent
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementConnector import HwElementConnector
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


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
    assert hw_pin.functionNames == []
    assert hw_pin.packagingPinName is None
    assert hw_pin.pinNumber is None


def test_hw_pin_getters_and_setters():
    """
    Test all getter and setter methods of HwPin class.

    Test Steps:
    1. Create a HwPin instance
    2. Test setting and getting functionNames (list)
    3. Test setting and getting packagingPinName
    4. Test setting and getting pinNumber
    5. Verify method chaining (return self)
    """
    hw_pin = HwPin(None, "test_hw_pin")

    # Test functionNames setter and getter with list
    test_function_names = ["CLK", "DATA"]
    return_value = hw_pin.setFunctionNames(test_function_names)
    assert return_value == hw_pin  # Verify method chaining
    assert hw_pin.getFunctionNames() == test_function_names

    # Test createFunctionName and addFunctionName
    func_name = hw_pin.createFunctionName("RESET")
    assert func_name == "RESET"
    assert "RESET" in hw_pin.getFunctionNames()

    return_value = hw_pin.addFunctionName("POWER")
    assert return_value == hw_pin  # Verify method chaining
    assert "POWER" in hw_pin.getFunctionNames()

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
    original_function_names = hw_pin.getFunctionNames()
    hw_pin.setFunctionNames(None)
    assert hw_pin.getFunctionNames() == original_function_names  # Should remain unchanged

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
    from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinGroup

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
    from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinGroupContent

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
    2. Test adding and getting hwElementConnections
    3. Test createHwPinGroup method
    4. Test adding and getting nestedElementRefs
    5. Verify method chaining (return self) and None no-op
    """

    hw_element = HwElement(None, "test_hw_element")

    # Test hwElementConnections adder and getter
    connection1 = HwElementConnector()
    ref1 = RefType()
    ref1.setDest("HW-ELEMENT")
    ref1.setValue("/pkg/elem1")
    connection1.setHwElementRef(ref1)
    connection2 = HwElementConnector()
    ref2 = RefType()
    ref2.setDest("HW-PIN")
    ref2.setValue("/pkg/elem1/pinA")
    connection2.setHwPinRef(ref2)
    return_value = hw_element.addHwElementConnection(connection1)
    assert return_value == hw_element  # Verify method chaining
    hw_element.addHwElementConnection(connection2)
    assert hw_element.getHwElementConnections() == [connection1, connection2]

    # Test createHwPinGroup
    new_pin_group = hw_element.createHwPinGroup("new_pin_group")
    assert new_pin_group is not None
    assert new_pin_group.short_name == "new_pin_group"
    assert new_pin_group in hw_element.getHwPinGroups()

    # Test nestedElementRefs adder and getter
    ref1 = RefType()
    ref1.setDest("HW-ELEMENT")
    ref1.setValue("/pkg/elem2")
    ref2 = RefType()
    ref2.setDest("HW-ELEMENT")
    ref2.setValue("/pkg/elem3")
    return_value = hw_element.addNestedElementRef(ref1)
    assert return_value == hw_element  # Verify method chaining
    hw_element.addNestedElementRef(ref2)
    assert hw_element.getNestedElementRefs() == [ref1, ref2]

    # Test with None values (should not add)
    original_connections = hw_element.getHwElementConnections()
    hw_element.addHwElementConnection(None)
    assert hw_element.getHwElementConnections() == original_connections  # Should remain unchanged

    original_nested_refs = hw_element.getNestedElementRefs()
    hw_element.addNestedElementRef(None)
    assert hw_element.getNestedElementRefs() == original_nested_refs  # Should remain unchanged


if __name__ == "__main__":
    test_hw_pin_init()
    test_hw_pin_getters_and_setters()
    test_hw_pin_group_content_init()
    test_hw_pin_group_content_getters_and_setters()
    test_hw_pin_group_init()
    test_hw_pin_group_getters_and_setters()
    test_hw_element_init()
    test_hw_element_getters_and_setters()
    print("All EcuResourceTemplate __init__ tests passed!")
