"""
Test cases for the HwElementConnector module.
These tests ensure 100% code coverage for the HwElementConnector class.
"""

from src.armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementConnector import HwElementConnector


def test_hw_element_connector_init():
    """
    Test initialization of HwElementConnector class.
    
    Test Steps:
    1. Create a HwElementConnector instance
    2. Verify default attributes are set correctly
    """
    # Initialize HwElementConnector
    hw_connector = HwElementConnector()
    
    # Verify initial values
    assert hw_connector.hwElementRef is None
    assert hw_connector.hwPinRef is None


def test_hw_element_connector_getters_and_setters():
    """
    Test all getter and setter methods of HwElementConnector class.
    
    Test Steps:
    1. Create a HwElementConnector instance
    2. Test setting and getting hwElementRef
    3. Test setting and getting hwPinRef
    4. Verify method chaining (return self)
    """
    hw_connector = HwElementConnector()
    
    # Test hwElementRef setter and getter
    test_element_ref = "test_element_ref"
    return_value = hw_connector.setHwElementRef(test_element_ref)
    assert return_value == hw_connector  # Verify method chaining
    assert hw_connector.getHwElementRef() == test_element_ref
    
    # Test hwPinRef setter and getter
    test_pin_ref = "test_pin_ref"
    return_value = hw_connector.setHwPinRef(test_pin_ref)
    assert return_value == hw_connector  # Verify method chaining
    assert hw_connector.getHwPinRef() == test_pin_ref
    
    # Test with None values (should not set)
    original_element_ref = hw_connector.getHwElementRef()
    hw_connector.setHwElementRef(None)
    assert hw_connector.getHwElementRef() == original_element_ref  # Should remain unchanged
    
    original_pin_ref = hw_connector.getHwPinRef()
    hw_connector.setHwPinRef(None)
    assert hw_connector.getHwPinRef() == original_pin_ref  # Should remain unchanged


if __name__ == '__main__':
    test_hw_element_connector_init()
    test_hw_element_connector_getters_and_setters()
    print("All HwElementConnector tests passed!")