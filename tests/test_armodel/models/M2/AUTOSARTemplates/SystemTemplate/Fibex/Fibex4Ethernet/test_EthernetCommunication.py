from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable, Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    IPv6ExtHeaderFilterList,
    RuntimeAddressConfigurationEnum,
    SoAdRoutingGroup,
    SocketConnection,
    SocketConnectionBundle,
    SocketConnectionIpduIdentifier,
    TcpOptionFilterList,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_Fibex4EthernetCommunication:
    """Test cases for Fibex4Ethernet Communication classes."""

    def test_SocketConnection(self):
        """Test SocketConnection class functionality (R4.3.1 Table 6.120, p.319)."""
        connection = SocketConnection()

        assert isinstance(connection, Describable)

        # Test default values
        assert connection.getRuntimePortConfiguration() is None
        assert connection.getShortLabel() is None

        # Test shortLabel setter/getter with method chaining
        result = connection.setShortLabel("label")
        assert connection.getShortLabel() == "label"
        assert result == connection
        result = connection.setShortLabel(None)
        assert connection.getShortLabel() == "label"  # None no-op

        # Test runtimePortConfiguration setter/getter with enum value
        enum_value = RuntimeAddressConfigurationEnum()
        enum_value.setValue("sd")
        result = connection.setRuntimePortConfiguration(enum_value)
        assert connection.getRuntimePortConfiguration() is enum_value
        assert result == connection
        result = connection.setRuntimePortConfiguration(None)
        assert connection.getRuntimePortConfiguration() is enum_value  # None no-op

        # Test enum literal values from R4.3.1 Table 6.121
        assert RuntimeAddressConfigurationEnum.NONE == "none"
        assert RuntimeAddressConfigurationEnum.SD == "sd"

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

    def test_IPv6ExtHeaderFilterList(self):
        """Test IPv6ExtHeaderFilterList class functionality (R4.3.1 Table 6.129, p.325)."""
        parent = MockParent()
        filter_list = IPv6ExtHeaderFilterList(parent, "test_ipv6_ext_header_filter_list")

        assert isinstance(filter_list, Identifiable)

        # Test default values
        assert filter_list.getShortName() == "test_ipv6_ext_header_filter_list"
        assert filter_list.getAllowedIPv6ExtHeaders() == []

        # Test adding allowed IPv6 extension headers
        assert filter_list == filter_list.addAllowedIPv6ExtHeader(6)  # Test method chaining
        filter_list.addAllowedIPv6ExtHeader(43)
        assert filter_list.getAllowedIPv6ExtHeaders() == [6, 43]

        # Test None is a no-op
        filter_list.addAllowedIPv6ExtHeader(None)
        assert filter_list.getAllowedIPv6ExtHeaders() == [6, 43]

    def test_TcpOptionFilterList(self):
        """Test TcpOptionFilterList class functionality (R4.3.1 Table 6.131, p.326)."""
        parent = MockParent()
        filter_list = TcpOptionFilterList(parent, "test_tcp_option_filter_list")

        assert isinstance(filter_list, Identifiable)

        # Test default values
        assert filter_list.getShortName() == "test_tcp_option_filter_list"
        assert filter_list.getAllowedTcpOptions() == []

        # Test adding allowed TCP options
        assert filter_list == filter_list.addAllowedTcpOption(2)  # Test method chaining
        filter_list.addAllowedTcpOption(8)
        assert filter_list.getAllowedTcpOptions() == [2, 8]

        # Test None is a no-op
        filter_list.addAllowedTcpOption(None)
        assert filter_list.getAllowedTcpOptions() == [2, 8]

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
