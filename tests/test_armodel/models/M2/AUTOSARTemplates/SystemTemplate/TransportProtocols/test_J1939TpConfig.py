from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    J1939TpConfig,
    J1939TpConnection,
    J1939TpNode,
    TpAddress,
    TpConfig,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestJ1939TpConfig:
    """Test class for J1939TpConfig (R23-11, Table 6.267, p.624)."""

    def test_initialization(self):
        """
        Test J1939TpConfig initialization and field defaults.
        """
        parent = MockParent()
        config = J1939TpConfig(parent, "test_j1939_tp_config")

        assert config is not None
        assert config.getShortName() == "test_j1939_tp_config"
        assert isinstance(config, TpConfig)

        assert config.getTpAddresses() == []
        assert config.getTpConnections() == []
        assert config.getTpNodes() == []

    def test_tp_addresses(self):
        """
        Test the tpAddress aggregation (createTpAddress / getTpAddresses).
        """
        parent = MockParent()
        config = J1939TpConfig(parent, "config")

        address = config.createTpAddress("Address1")
        assert isinstance(address, TpAddress)
        assert address in config.getTpAddresses()
        assert len(config.getTpAddresses()) == 1

        config.createTpAddress("Address2")
        assert len(config.getTpAddresses()) == 2

        duplicate = config.createTpAddress("Address1")
        assert duplicate is address
        assert len(config.getTpAddresses()) == 2

    def test_tp_connections(self):
        """
        Test the tpConnection aggregation (addTpConnection / getTpConnections).
        """
        parent = MockParent()
        config = J1939TpConfig(parent, "config")

        connection = J1939TpConnection()
        config.addTpConnection(connection)
        assert connection in config.getTpConnections()
        assert len(config.getTpConnections()) == 1

        assert config.addTpConnection(None) is config
        assert len(config.getTpConnections()) == 1

    def test_tp_nodes(self):
        """
        Test the tpNode aggregation (createJ1939TpNode / getTpNodes).
        """
        parent = MockParent()
        config = J1939TpConfig(parent, "config")

        node = config.createJ1939TpNode("Node1")
        assert isinstance(node, J1939TpNode)
        assert node in config.getTpNodes()
        assert len(config.getTpNodes()) == 1

        duplicate = config.createJ1939TpNode("Node1")
        assert duplicate is node
        assert len(config.getTpNodes()) == 1
