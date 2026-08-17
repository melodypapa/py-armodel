import pytest

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPin
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestHwPin:
    def test_initialization(self):
        """Test HwPin initialization"""
        pin = HwPin(None, "TestPin")
        assert pin.getShortName() == "TestPin"
        assert pin.getFunctionName() is None
        assert pin.getPackagingPinName() is None
        assert pin.getPinNumber() is None

    def test_set_function_name(self):
        """Test setFunctionName method"""
        pin = HwPin(None, "TestPin")
        result = pin.setFunctionName("CAN_TX")
        assert result is pin
        assert pin.getFunctionName() == "CAN_TX"

    def test_set_function_name_none(self):
        """Test setFunctionName with None value"""
        pin = HwPin(None, "TestPin")
        result = pin.setFunctionName(None)
        assert result is pin
        assert pin.getFunctionName() is None

    def test_set_packaging_pin_name(self):
        """Test setPackagingPinName method"""
        pin = HwPin(None, "TestPin")
        result = pin.setPackagingPinName("P1_23")
        assert result is pin
        assert pin.getPackagingPinName() == "P1_23"

    def test_set_packaging_pin_name_none(self):
        """Test setPackagingPinName with None value"""
        pin = HwPin(None, "TestPin")
        result = pin.setPackagingPinName(None)
        assert result is pin
        assert pin.getPackagingPinName() is None

    def test_set_pin_number(self):
        """Test setPinNumber method"""
        pin = HwPin(None, "TestPin")
        result = pin.setPinNumber(42)
        assert result is pin
        assert pin.getPinNumber() == 42

    def test_set_pin_number_none(self):
        """Test setPinNumber with None value"""
        pin = HwPin(None, "TestPin")
        result = pin.setPinNumber(None)
        assert result is pin
        assert pin.getPinNumber() is None

    def test_method_chaining(self):
        """Test method chaining for all setters"""
        pin = HwPin(None, "TestPin")
        result = pin.setFunctionName("CAN_TX").setPackagingPinName("P1_23").setPinNumber(42)
        assert result is pin
        assert pin.getFunctionName() == "CAN_TX"
        assert pin.getPackagingPinName() == "P1_23"
        assert pin.getPinNumber() == 42

    def test_inherited_hw_description_entity_methods(self):
        """Test inherited HwDescriptionEntity methods"""
        pin = HwPin(None, "TestPin")
        ref = RefType()

        # Test addHwCategoryRef from HwDescriptionEntity
        result = pin.addHwCategoryRef(ref)
        assert result is pin
        assert pin.getHwCategoryRefs() == [ref]
