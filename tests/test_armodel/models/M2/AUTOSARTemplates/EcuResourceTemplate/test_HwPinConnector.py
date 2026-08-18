from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestHwPinConnector:
    """Test HwPinConnector class"""

    def test_initialization(self):
        """Test HwPinConnector initialization"""
        # Import after class is created
        from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwPinConnector import HwPinConnector

        connector = HwPinConnector()
        assert connector.getHwPinRefs() == []

    def test_add_hw_pin_ref(self):
        """Test addHwPinRef method"""
        from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwPinConnector import HwPinConnector

        connector = HwPinConnector()
        ref = RefType()
        result = connector.addHwPinRef(ref)
        assert result is connector
        assert connector.getHwPinRefs() == [ref]

    def test_add_hw_pin_ref_none(self):
        """Test addHwPinRef with None value"""
        from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwPinConnector import HwPinConnector

        connector = HwPinConnector()
        result = connector.addHwPinRef(None)
        assert result is connector
        assert connector.getHwPinRefs() == []

    def test_add_multiple_hw_pin_refs(self):
        """Test addHwPinRef with multiple refs"""
        from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwPinConnector import HwPinConnector

        connector = HwPinConnector()
        ref1 = RefType()
        ref2 = RefType()

        connector.addHwPinRef(ref1).addHwPinRef(ref2)

        refs = connector.getHwPinRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[1] is ref2
