from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import (
    HwPin,
    HwPinGroup,
    HwPinGroupContent,
)


class TestHwPinGroupContent:
    def test_initialization(self):
        """Test HwPinGroupContent initialization defaults (Table 2.6)"""
        content = HwPinGroupContent()
        assert content.hwPin is None
        assert content.hwPinGroup is None
        assert content.getHwPin() is None
        assert content.getHwPinGroup() is None

    def test_create_hw_pin(self):
        """Test createHwPin creates the HwPin child and assigns it"""
        content = HwPinGroupContent()
        pin = content.createHwPin("TestPin")
        assert isinstance(pin, HwPin)
        assert pin.getShortName() == "TestPin"
        assert content.getHwPin() is pin

    def test_create_hw_pin_duplicate_returns_existing(self):
        """createHwPin returns the existing child when the short name already exists"""
        content = HwPinGroupContent()
        pin = content.createHwPin("TestPin")
        assert content.createHwPin("TestPin") is pin

    def test_create_hw_pin_group(self):
        """Test createHwPinGroup creates the HwPinGroup child and assigns it"""
        content = HwPinGroupContent()
        group = content.createHwPinGroup("TestGroup")
        assert isinstance(group, HwPinGroup)
        assert group.getShortName() == "TestGroup"
        assert content.getHwPinGroup() is group

    def test_create_hw_pin_group_duplicate_returns_existing(self):
        """createHwPinGroup returns the existing child when the short name already exists"""
        content = HwPinGroupContent()
        group = content.createHwPinGroup("TestGroup")
        assert content.createHwPinGroup("TestGroup") is group

    def test_pin_and_group_can_coexist(self):
        """The hwPin and hwPinGroup slots are independent in the model (XSD choice governs the XML only)"""
        content = HwPinGroupContent()
        pin = content.createHwPin("TestPin")
        group = content.createHwPinGroup("TestGroup")
        assert content.getHwPin() is pin
        assert content.getHwPinGroup() is group

    def test_member_docstrings_verbatim(self):
        """Member docstrings must carry the Table 2.6 Notes verbatim (Rule 0001.4/0012)."""
        assert HwPinGroupContent.__doc__ is not None, "Class docstring must contain spec Note"
        assert "This meta-class specifies a mixture of hwPins and hwPinGroups." in HwPinGroupContent.__doc__, "Class docstring must contain spec Note verbatim"

        notes = {
            "getHwPin": "This aggregation represents a hardware pin in a hardware pin group.",
            "createHwPin": "This aggregation represents a hardware pin in a hardware pin group.",
            "getHwPinGroup": "This aggregation represents a nested hardware pin group.",
            "createHwPinGroup": "This aggregation represents a nested hardware pin group.",
        }
        for method_name, note in notes.items():
            method = getattr(HwPinGroupContent, method_name)
            assert method.__doc__ is not None, "%s must have a docstring" % method_name
            assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name

    def test_member_annotations(self):
        """create/get shall resolve to HwPin / Optional[HwPin] / HwPinGroup / Optional[HwPinGroup] (Rule 0003/0006 get_type_hints pin)."""
        import typing

        hints = typing.get_type_hints(HwPinGroupContent.createHwPin)
        assert hints["short_name"] is str
        assert hints["return"] is HwPin
        assert typing.get_type_hints(HwPinGroupContent.getHwPin)["return"] == typing.Optional[HwPin]
        hints = typing.get_type_hints(HwPinGroupContent.createHwPinGroup)
        assert hints["short_name"] is str
        assert hints["return"] is HwPinGroup
        assert typing.get_type_hints(HwPinGroupContent.getHwPinGroup)["return"] == typing.Optional[HwPinGroup]
