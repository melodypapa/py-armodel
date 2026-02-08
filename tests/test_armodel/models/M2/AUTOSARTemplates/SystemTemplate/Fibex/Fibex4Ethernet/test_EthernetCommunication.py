
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Describable,
    Identifiable,
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    SoAdRoutingGroup,
    SocketConnection,
    SocketConnectionBundle,
    SocketConnectionIpduIdentifier,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_Fibex4EthernetCommunication:
    """Test cases for Fibex4Ethernet Communication classes."""

    def test_SocketConnection(self):
        """Test SocketConnection class functionality."""
        connection = SocketConnection()

        assert isinstance(connection, Describable)

        # Test default values
        assert connection.getAllowedIPv6ExtHeadersRef() is None
        assert connection.getAllowedTcpOptionsRef() is None
        assert connection.getClientIpAddrFromConnectionRequest() is None
        assert connection.getClientPortRef() is None
        assert connection.getClientPortFromConnectionRequest() is None
        assert connection.getPdus() == []
        assert connection.getPduSocketConnectionIpdus() == []
        assert connection.getPduCollectionMaxBufferSize() is None
        assert connection.getPduCollectionTimeout() is None
        assert connection.getRuntimeIpAddressConfiguration() is None
        assert connection.getRuntimePortConfiguration() is None
        assert connection.getShortLabel() is None

        # Test setter/getter methods
        connection.setAllowedIPv6ExtHeadersRef("ipv6_ref")
        assert connection.getAllowedIPv6ExtHeadersRef() == "ipv6_ref"
        assert connection == connection.setAllowedIPv6ExtHeadersRef("ipv6_ref")  # Test method chaining

        connection.setAllowedTcpOptionsRef("tcp_ref")
        assert connection.getAllowedTcpOptionsRef() == "tcp_ref"
        assert connection == connection.setAllowedTcpOptionsRef("tcp_ref")  # Test method chaining

        connection.setClientIpAddrFromConnectionRequest(True)
        assert connection.getClientIpAddrFromConnectionRequest() is True
        assert connection == connection.setClientIpAddrFromConnectionRequest(True)  # Test method chaining

        connection.setClientPortRef("port_ref")
        assert connection.getClientPortRef() == "port_ref"
        assert connection == connection.setClientPortRef("port_ref")  # Test method chaining

        connection.setClientPortFromConnectionRequest(False)
        assert connection.getClientPortFromConnectionRequest() is False
        assert connection == connection.setClientPortFromConnectionRequest(False)  # Test method chaining

        connection.setPduCollectionMaxBufferSize(1024)
        assert connection.getPduCollectionMaxBufferSize() == 1024
        assert connection == connection.setPduCollectionMaxBufferSize(1024)  # Test method chaining

        connection.setPduCollectionTimeout("10ms")
        assert connection.getPduCollectionTimeout() == "10ms"
        assert connection == connection.setPduCollectionTimeout("10ms")  # Test method chaining

        connection.setRuntimeIpAddressConfiguration("config")
        assert connection.getRuntimeIpAddressConfiguration() == "config"
        assert connection == connection.setRuntimeIpAddressConfiguration("config")  # Test method chaining

        connection.setRuntimePortConfiguration("port_config")
        assert connection.getRuntimePortConfiguration() == "port_config"
        assert connection == connection.setRuntimePortConfiguration("port_config")  # Test method chaining

        connection.setShortLabel("label")
        assert connection.getShortLabel() == "label"
        assert connection == connection.setShortLabel("label")  # Test method chaining

        # Test adding PDUs
        mock_pdu = SocketConnectionIpduIdentifier()
        connection.addPdu(mock_pdu)
        assert connection.getPdus() == [mock_pdu]
        assert connection == connection.addPdu(mock_pdu)  # Test method chaining

        # Test adding PDU socket connection IPDUs
        connection.addPduSocketConnectionIpdu("identifier1")
        connection.addPduSocketConnectionIpdu("identifier2")
        assert connection.getPduSocketConnectionIpdus() == ["identifier1", "identifier2"]
        assert connection == connection.addPduSocketConnectionIpdu("identifier3")  # Test method chaining

    def test_SocketConnectionIpduIdentifier(self):
        """Test SocketConnectionIpduIdentifier class functionality."""
        identifier = SocketConnectionIpduIdentifier()

        assert isinstance(identifier, ARObject)

        # Test default values
        assert identifier.getHeaderId() is None
        assert identifier.getPduCollectionPduTimeout() is None
        assert identifier.getPduCollectionSemantics() is None
        assert identifier.getPduCollectionTrigger() is None
        assert identifier.getPduRef() is None
        assert identifier.getPduTriggeringRef() is None
        assert identifier.getRoutingGroupRefs() == []

        # Test setter/getter methods
        identifier.setHeaderId(123)
        assert identifier.getHeaderId() == 123
        assert identifier == identifier.setHeaderId(123)  # Test method chaining

        identifier.setPduCollectionPduTimeout("10ms")
        assert identifier.getPduCollectionPduTimeout() == "10ms"
        assert identifier == identifier.setPduCollectionPduTimeout("10ms")  # Test method chaining

        identifier.setPduCollectionSemantics("semantics")
        assert identifier.getPduCollectionSemantics() == "semantics"
        assert identifier == identifier.setPduCollectionSemantics("semantics")  # Test method chaining

        identifier.setPduCollectionTrigger("trigger")
        assert identifier.getPduCollectionTrigger() == "trigger"
        assert identifier == identifier.setPduCollectionTrigger("trigger")  # Test method chaining

        identifier.setPduRef("pdu_ref")
        assert identifier.getPduRef() == "pdu_ref"
        assert identifier == identifier.setPduRef("pdu_ref")  # Test method chaining

        identifier.setPduTriggeringRef("trigger_ref")
        assert identifier.getPduTriggeringRef() == "trigger_ref"
        assert identifier == identifier.setPduTriggeringRef("trigger_ref")  # Test method chaining

        # Test adding routing group refs
        identifier.setRoutingGroupRefs(["ref1", "ref2"])
        assert identifier.getRoutingGroupRefs() == ["ref1", "ref2"]
        assert identifier == identifier.setRoutingGroupRefs(["ref1", "ref2"])  # Test method chaining

    def test_SocketConnectionBundle(self):
        """Test SocketConnectionBundle class functionality."""
        parent = MockParent()
        bundle = SocketConnectionBundle(parent, "test_socket_conn_bundle")

        assert isinstance(bundle, Referrable)

        # Test default values
        assert bundle.getBundledConnections() == []
        assert bundle.getDifferentiatedServiceField() is None
        assert bundle.getFlowLabel() is None
        assert bundle.getPathMtuDiscoveryEnabled() is None
        assert bundle.getPdus() == []
        assert bundle.getServerPortRef() is None
        assert bundle.getUdpChecksumHandling() is None

        # Test setter/getter methods
        bundle.setDifferentiatedServiceField(48)
        assert bundle.getDifferentiatedServiceField() == 48
        assert bundle == bundle.setDifferentiatedServiceField(48)  # Test method chaining

        bundle.setFlowLabel(100)
        assert bundle.getFlowLabel() == 100
        assert bundle == bundle.setFlowLabel(100)  # Test method chaining

        bundle.setPathMtuDiscoveryEnabled(True)
        assert bundle.getPathMtuDiscoveryEnabled() is True
        assert bundle == bundle.setPathMtuDiscoveryEnabled(True)  # Test method chaining

        bundle.setServerPortRef("server_port_ref")
        assert bundle.getServerPortRef() == "server_port_ref"
        assert bundle == bundle.setServerPortRef("server_port_ref")  # Test method chaining

        bundle.setUdpChecksumHandling("udp_handling")
        assert bundle.getUdpChecksumHandling() == "udp_handling"
        assert bundle == bundle.setUdpChecksumHandling("udp_handling")  # Test method chaining

        bundle.setPdus(["pdu1", "pdu2"])
        assert bundle.getPdus() == ["pdu1", "pdu2"]
        assert bundle == bundle.setPdus(["pdu1", "pdu2"])  # Test method chaining

        # Test adding bundled connections
        mock_conn = SocketConnection()
        bundle.addBundledConnection(mock_conn)
        assert bundle.getBundledConnections() == [mock_conn]
        assert bundle == bundle.addBundledConnection(mock_conn)  # Test method chaining

    def test_SoAdRoutingGroup(self):
        """Test SoAdRoutingGroup class functionality."""
        parent = MockParent()
        group = SoAdRoutingGroup(parent, "test_soad_routing_group")

        assert isinstance(group, Identifiable)

        # Test default values
        assert group.getEventGroupControlType() is None

        # Test setter/getter methods
        group.setEventGroupControlType("control_type")
        assert group.getEventGroupControlType() == "control_type"
