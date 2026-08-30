from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Describable, Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    RuntimeAddressConfigurationEnum,
    SocketConnectionBundle,
    SocketConnectionIpduIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList import IPv6ExtHeaderFilterList
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel import (
    SoAdRoutingGroup,
    SocketConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet import (
    TcpOptionFilterList,
    TcpOptionFilterSet,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_Fibex4EthernetCommunication:
    """Test cases for Fibex4Ethernet Communication classes."""

    def test_SocketConnection(self):
        """Test SocketConnection class functionality (R4.3.1 Table 6.120, p.319; member set per R4.3.1 AUTOSAR_00044.xsd SOCKET-CONNECTION group)."""
        connection = SocketConnection()

        assert isinstance(connection, Describable)

        # Test default values
        assert connection.getAllowedIPv6ExtHeadersRef() is None
        assert connection.getAllowedTcpOptionsRef() is None
        assert connection.getClientIpAddrFromConnectionRequest() is None
        assert connection.getClientPortFromConnectionRequest() is None
        assert connection.getClientPortRef() is None
        assert connection.getPdus() == []
        assert connection.getPduCollectionMaxBufferSize() is None
        assert connection.getPduCollectionTimeout() is None
        assert connection.getRuntimeIpAddressConfiguration() is None
        assert connection.getRuntimePortConfiguration() is None
        assert connection.getShortLabel() is None

        # Test reference setters/getters with method chaining and None no-op
        result = connection.setAllowedIPv6ExtHeadersRef("/Pkgs/IPv6List")
        assert connection.getAllowedIPv6ExtHeadersRef() == "/Pkgs/IPv6List"
        assert result == connection
        connection.setAllowedIPv6ExtHeadersRef(None)
        assert connection.getAllowedIPv6ExtHeadersRef() == "/Pkgs/IPv6List"  # None no-op

        result = connection.setAllowedTcpOptionsRef("/Pkgs/TcpList")
        assert connection.getAllowedTcpOptionsRef() == "/Pkgs/TcpList"
        assert result == connection

        result = connection.setClientPortRef("/Sock/SA1")
        assert connection.getClientPortRef() == "/Sock/SA1"
        assert result == connection

        # Test boolean setters/getters
        result = connection.setClientIpAddrFromConnectionRequest(True)
        assert connection.getClientIpAddrFromConnectionRequest() is True
        assert result == connection
        connection.setClientIpAddrFromConnectionRequest(None)
        assert connection.getClientIpAddrFromConnectionRequest() is True  # None no-op

        result = connection.setClientPortFromConnectionRequest(False)
        assert connection.getClientPortFromConnectionRequest() is False
        assert result == connection

        # Test pdu aggregation
        pdu = SocketConnectionIpduIdentifier()
        assert connection == connection.addPdu(pdu)
        assert connection.getPdus() == [pdu]
        connection.addPdu(None)
        assert connection.getPdus() == [pdu]  # None no-op

        # Test numerical/time setters/getters
        result = connection.setPduCollectionMaxBufferSize(1024)
        assert connection.getPduCollectionMaxBufferSize() == 1024
        assert result == connection

        result = connection.setPduCollectionTimeout("10ms")
        assert connection.getPduCollectionTimeout() == "10ms"
        assert result == connection

        # Test runtime enum setters/getters
        ip_enum = RuntimeAddressConfigurationEnum()
        ip_enum.setValue("sd")
        result = connection.setRuntimeIpAddressConfiguration(ip_enum)
        assert connection.getRuntimeIpAddressConfiguration() is ip_enum
        assert result == connection
        connection.setRuntimeIpAddressConfiguration(None)
        assert connection.getRuntimeIpAddressConfiguration() is ip_enum  # None no-op

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

    def test_TcpOptionFilterSet(self):
        """Test TcpOptionFilterSet class functionality (R4.3.1 Table 6.130, p.326)."""
        parent = MockParent()
        tcp_set = TcpOptionFilterSet(parent, "test_tcp_option_filter_set")

        assert isinstance(tcp_set, ARElement)

        # Test default values
        assert tcp_set.getShortName() == "test_tcp_option_filter_set"
        assert tcp_set.getTcpOptionFilterLists() == []

        # Test creating filter lists (create appends; duplicate returns existing)
        first = tcp_set.createTcpOptionFilterList("list1")
        assert first.getShortName() == "list1"
        assert tcp_set.getTcpOptionFilterLists() == [first]
        duplicate = tcp_set.createTcpOptionFilterList("list1")
        assert duplicate is first
        second = tcp_set.createTcpOptionFilterList("list2")
        assert tcp_set.getTcpOptionFilterLists() == [first, second]

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
