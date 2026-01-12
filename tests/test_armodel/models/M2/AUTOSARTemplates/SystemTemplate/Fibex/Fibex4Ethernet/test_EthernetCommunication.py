import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    SocketConnection,
    SocketConnectionIpduIdentifier,
    SocketConnectionBundle,
    SoAdRoutingGroup
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable, Identifiable, Referrable


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
        
        connection.setClientPortRef("port_ref")
        assert connection.getClientPortRef() == "port_ref"
        
        # Test adding PDUs
        mock_pdu = SocketConnectionIpduIdentifier()
        connection.addPdu(mock_pdu)
        assert connection.getPdus() == [mock_pdu]
        
        # Test adding PDU socket connection IPDUs
        connection.addPduSocketConnectionIpdu("identifier1")
        connection.addPduSocketConnectionIpdu("identifier2")
        assert connection.getPduSocketConnectionIpdus() == ["identifier1", "identifier2"]

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
        
        identifier.setPduCollectionPduTimeout("10ms")
        assert identifier.getPduCollectionPduTimeout() == "10ms"
        
        # Test adding routing group refs
        identifier.setRoutingGroupRefs(["ref1", "ref2"])
        assert identifier.getRoutingGroupRefs() == ["ref1", "ref2"]

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
        
        bundle.setFlowLabel(100)
        assert bundle.getFlowLabel() == 100
        
        bundle.setPathMtuDiscoveryEnabled(True)
        assert bundle.getPathMtuDiscoveryEnabled() is True
        
        # Test adding bundled connections
        mock_conn = SocketConnection()
        bundle.addBundledConnection(mock_conn)
        assert bundle.getBundledConnections() == [mock_conn]

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