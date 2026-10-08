from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import J1939TpNode


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestJ1939TpNode:
    """Test class for J1939TpNode (R23-11, Table 6.270, p.626)."""

    def test_initialization(self):
        """
        Test J1939TpNode initialization and field defaults.
        """
        parent = MockParent()
        node = J1939TpNode(parent, "test_j1939_tp_node")

        assert node is not None
        assert node.getShortName() == "test_j1939_tp_node"
        assert isinstance(node, Identifiable)

        assert node.getConnectorRef() is None
        assert node.getTpAddressRef() is None

    def test_get_set_connector_ref(self):
        parent = MockParent()
        node = J1939TpNode(parent, "node")
        ref = RefType()
        ref.setValue("/Topology/Connector1")

        result = node.setConnectorRef(ref)
        assert result is node
        assert node.getConnectorRef() is ref
        node.setConnectorRef(None)
        assert node.getConnectorRef() is ref

    def test_get_set_tp_address_ref(self):
        parent = MockParent()
        node = J1939TpNode(parent, "node")
        ref = RefType()
        ref.setValue("/TpConfigs/Config1/TpAddress1")

        result = node.setTpAddressRef(ref)
        assert result is node
        assert node.getTpAddressRef() is ref
        node.setTpAddressRef(None)
        assert node.getTpAddressRef() is ref
