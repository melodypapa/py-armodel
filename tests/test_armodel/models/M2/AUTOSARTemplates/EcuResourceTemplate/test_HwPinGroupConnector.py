from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestHwPinGroupConnector:
    """Test HwPinGroupConnector class"""

    def test_initialization(self):
        """Test HwPinGroupConnector initialization"""
        # Import after class is created
        from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinGroupConnector

        connector = HwPinGroupConnector()
        assert connector.getHwPinConnections() == []
        assert connector.getHwPinGroupRefs() == []

    def test_add_hw_pin_connection(self):
        """Test addHwPinConnection method"""
        from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinConnector
        from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinGroupConnector

        connector = HwPinGroupConnector()
        pin_conn = HwPinConnector()

        result = connector.addHwPinConnection(pin_conn)
        assert result is connector
        assert connector.getHwPinConnections() == [pin_conn]

    def test_add_hw_pin_connection_none(self):
        """Test addHwPinConnection with None value"""
        from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinGroupConnector

        connector = HwPinGroupConnector()
        result = connector.addHwPinConnection(None)
        assert result is connector
        assert connector.getHwPinConnections() == []

    def test_add_hw_pin_group_ref(self):
        """Test addHwPinGroupRef method"""
        from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinGroupConnector

        connector = HwPinGroupConnector()
        ref = RefType()
        result = connector.addHwPinGroupRef(ref)
        assert result is connector
        assert connector.getHwPinGroupRefs() == [ref]

    def test_add_hw_pin_group_ref_none(self):
        """Test addHwPinGroupRef with None value"""
        from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinGroupConnector

        connector = HwPinGroupConnector()
        result = connector.addHwPinGroupRef(None)
        assert result is connector
        assert connector.getHwPinGroupRefs() == []

    def test_method_chaining(self):
        """Test method chaining for all adders"""
        from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinConnector
        from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinGroupConnector

        connector = HwPinGroupConnector()
        pin_conn1 = HwPinConnector()
        pin_conn2 = HwPinConnector()
        ref1 = RefType()
        ref2 = RefType()

        result = connector.addHwPinConnection(pin_conn1).addHwPinConnection(pin_conn2).addHwPinGroupRef(ref1).addHwPinGroupRef(ref2)

        assert result is connector
        assert connector.getHwPinConnections() == [pin_conn1, pin_conn2]
        assert connector.getHwPinGroupRefs() == [ref1, ref2]
