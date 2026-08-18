from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import (
    HwPin,
    HwPinGroup,
    HwPinGroupContent,
)


class TestHwPinGroupContent:
    def test_initialization(self):
        """Test HwPinGroupContent initialization"""
        content = HwPinGroupContent()
        assert content.getHwPin() is None
        assert content.getHwPinGroup() is None

    def test_create_hw_pin(self):
        """Test createHwPin method"""
        content = HwPinGroupContent()
        pin = content.createHwPin("TestPin")
        assert pin is not None
        assert isinstance(pin, HwPin)
        assert pin.getShortName() == "TestPin"
        assert content.getHwPin() is pin

    def test_set_hw_pin_group(self):
        """Test setHwPinGroup method"""
        content = HwPinGroupContent()
        group = HwPinGroup(None, "TestGroup")
        result = content.setHwPinGroup(group)
        assert result is content
        assert content.getHwPinGroup() is group

    def test_set_hw_pin_group_none(self):
        """Test setHwPinGroup with None value"""
        content = HwPinGroupContent()
        result = content.setHwPinGroup(None)
        assert result is content
        assert content.getHwPinGroup() is None

    def test_exclusive_pin_or_group(self):
        """Test that pin or group can coexist (per XSD choice)"""
        content = HwPinGroupContent()

        # Set a pin
        content.createHwPin("TestPin")
        assert content.getHwPin() is not None

        # Set a group (both can coexist in model, though XML choice is invalid)
        group = HwPinGroup(None, "TestGroup")
        content.setHwPinGroup(group)
        assert content.getHwPin() is not None
        assert content.getHwPinGroup() is not None
