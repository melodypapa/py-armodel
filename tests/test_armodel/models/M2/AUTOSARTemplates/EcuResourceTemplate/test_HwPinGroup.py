from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinGroup, HwPinGroupContent
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestHwPinGroup:
    def test_initialization(self):
        """Test HwPinGroup initialization"""
        group = HwPinGroup(None, "TestGroup")
        assert group.getShortName() == "TestGroup"
        assert group.getHwPinGroupContent() is None

    def test_set_get_hw_pin_group_content(self):
        """Test setHwPinGroupContent / getHwPinGroupContent round-trip"""
        group = HwPinGroup(None, "TestGroup")
        content = HwPinGroupContent()
        result = group.setHwPinGroupContent(content)
        assert result is group
        assert group.getHwPinGroupContent() is content

    def test_set_hw_pin_group_content_none_noop(self):
        """Test setHwPinGroupContent with None is a no-op"""
        group = HwPinGroup(None, "TestGroup")
        content = HwPinGroupContent()
        group.setHwPinGroupContent(content)
        result = group.setHwPinGroupContent(None)
        assert result is group
        assert group.getHwPinGroupContent() is content

    def test_method_chaining(self):
        """Test method chaining for setHwPinGroupContent"""
        group = HwPinGroup(None, "TestGroup")
        content = HwPinGroupContent()
        result = group.setHwPinGroupContent(content)
        assert result is group
        assert group.getHwPinGroupContent() is content

    def test_content_with_pin(self):
        """Test a HwPinGroupContent carrying a nested HwPin"""
        group = HwPinGroup(None, "TestGroup")
        content = HwPinGroupContent()
        pin = content.createHwPin("P1")
        group.setHwPinGroupContent(content)
        assert group.getHwPinGroupContent().getHwPin() is pin
        assert pin.getShortName() == "P1"

    def test_inherited_hw_description_entity_methods(self):
        """Test inherited HwDescriptionEntity methods"""
        group = HwPinGroup(None, "TestGroup")
        ref = RefType()
        result = group.addHwCategoryRef(ref)
        assert result is group
        assert group.getHwCategoryRefs() == [ref]
