import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    TransportProtocolConfiguration,
    GenericTp,
    TcpUdpConfig,
    TpPort,
    UdpTp,
    TcpTp,
    AbstractServiceInstance,
    ConsumedEventGroup,
    ConsumedServiceInstance,
    InitialSdDelayConfig,
    SdServerConfig,
    EventHandler,
    ProvidedServiceInstance,
    ApplicationEndpoint,
    SocketAddress,
    SoAdConfig
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_Fibex4EthernetServiceInstances:
    """Test cases for Fibex4Ethernet ServiceInstances classes."""
    
    def test_TransportProtocolConfiguration(self):
        """Test TransportProtocolConfiguration abstract class instantiation."""
        with pytest.raises(NotImplementedError):
            TransportProtocolConfiguration()

    def test_GenericTp(self):
        """Test GenericTp class functionality."""
        tp = GenericTp()

        assert isinstance(tp, TransportProtocolConfiguration)
        
        # Test default values
        assert tp.getTpAddress() is None
        assert tp.getTpTechnology() is None
        
        # Test setter/getter methods
        tp.setTpAddress("tcp://192.168.1.1:8080")
        assert tp.getTpAddress() == "tcp://192.168.1.1:8080"
        
        tp.setTpTechnology("TCP")
        assert tp.getTpTechnology() == "TCP"

    def test_TcpUdpConfig(self):
        """Test TcpUdpConfig abstract class instantiation."""
        with pytest.raises(NotImplementedError):
            TcpUdpConfig()

    def test_TpPort(self):
        """Test TpPort class functionality."""
        port = TpPort()

        assert isinstance(port, ARObject)
        
        # Test default values
        assert port.getDynamicallyAssigned() is None
        assert port.getPortNumber() is None
        
        # Test setter/getter methods
        port.setDynamicallyAssigned(True)
        assert port.getDynamicallyAssigned() is True
        
        port.setPortNumber(8080)
        assert port.getPortNumber() == 8080

    def test_UdpTp(self):
        """Test UdpTp class functionality."""
        tp = UdpTp()

        assert isinstance(tp, TcpUdpConfig)
        
        # Test default values
        assert tp.getUdpTpPort() is None
        
        # Test setter/getter methods
        port = TpPort()
        tp.setUdpTpPort(port)
        assert tp.getUdpTpPort() == port

    def test_TcpTp(self):
        """Test TcpTp class functionality."""
        tp = TcpTp()

        assert isinstance(tp, TcpUdpConfig)
        
        # Test default values
        assert tp.getKeepAliveInterval() is None
        assert tp.getKeepAliveProbesMax() is None
        assert tp.getKeepAlives() is None
        assert tp.getKeepAliveTime() is None
        assert tp.getNaglesAlgorithm() is None
        assert tp.getReceiveWindowMin() is None
        assert tp.getTcpRetransmissionTimeout() is None
        assert tp.getTcpTpPort() is None
        
        # Test setter/getter methods
        tp.setKeepAliveTime("7200s")
        assert tp.getKeepAliveTime() == "7200s"
        
        tp.setNaglesAlgorithm(True)
        assert tp.getNaglesAlgorithm() is True

    def test_AbstractServiceInstance(self):
        """Test AbstractServiceInstance abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            AbstractServiceInstance(parent, "test_abstract_service_instance")

    def test_ConsumedEventGroup(self):
        """Test ConsumedEventGroup class functionality."""
        parent = MockParent()
        group = ConsumedEventGroup(parent, "test_consumed_event_group")

        assert isinstance(group, Identifiable)
        
        # Test default values
        assert group.getApplicationEndpointRef() is None
        assert group.getAutoRequire() is None
        assert group.getEventGroupIdentifier() is None
        assert group.getEventMulticastAddressRefs() == []
        assert group.getPduActivationRoutingGroups() == []
        assert group.getPriority() is None
        assert group.getRoutingGroupRefs() == []
        assert group.getSdClientConfig() is None
        assert group.getSdClientTimerConfigRef() is None
        
        # Test setter/getter methods
        group.setApplicationEndpointRef("app_endpoint_ref")
        assert group.getApplicationEndpointRef() == "app_endpoint_ref"
        
        group.setAutoRequire(True)
        assert group.getAutoRequire() is True

    def test_ConsumedServiceInstance(self):
        """Test ConsumedServiceInstance class functionality."""
        parent = MockParent()
        instance = ConsumedServiceInstance(parent, "test_consumed_service_instance")

        assert isinstance(instance, AbstractServiceInstance)
        
        # Test default values
        assert instance.getAllowedServiceProviderRefs() == []
        assert instance.getAutoRequire() is None
        assert instance.getBlocklistedVersions() == []
        assert instance.getConsumedEventGroups() == []
        assert instance.getEventMulticastSubscriptionAddressRef() is None
        assert instance.getInstanceIdentifier() is None
        assert instance.getLocalUnicastAddressRefs() == []
        assert instance.getMinorVersion() is None
        assert instance.getProvidedServiceInstanceRef() is None
        assert instance.getRemoteUnicastAddressRefs() == []
        assert instance.getSdClientConfig() is None
        assert instance.getSdClientTimerConfigRef() is None
        assert instance.getServiceIdentifier() is None
        assert instance.getVersionDrivenFindBehavior() is None

    def test_InitialSdDelayConfig(self):
        """Test InitialSdDelayConfig class functionality."""
        config = InitialSdDelayConfig()

        assert isinstance(config, ARObject)
        
        # Test default values
        assert config.getInitialDelayMaxValue() is None
        assert config.getInitialDelayMinValue() is None
        assert config.getInitialRepetitionsBaseDelay() is None
        assert config.getInitialRepetitionsMax() is None
        
        # Test setter/getter methods
        config.setInitialDelayMaxValue("100ms")
        assert config.getInitialDelayMaxValue() == "100ms"

    def test_SdServerConfig(self):
        """Test SdServerConfig class functionality."""
        config = SdServerConfig()

        assert isinstance(config, ARObject)
        
        # Test default values
        assert config.getCapabilityRecords() == []
        assert config.getInitialOfferBehavior() is None
        assert config.getOfferCyclicDelay() is None
        assert config.getRequestResponseDelay() is None
        assert config.getServerServiceMajorVersion() is None
        assert config.getServerServiceMinorVersion() is None
        assert config.getTtl() is None

    def test_EventHandler(self):
        """Test EventHandler class functionality."""
        parent = MockParent()
        handler = EventHandler(parent, "test_event_handler")

        assert isinstance(handler, Identifiable)
        
        # Test default values
        assert handler.getApplicationEndpointRef() is None
        assert handler.getConsumedEventGroupRefs() == []
        assert handler.getMulticastThreshold() is None
        assert handler.getRoutingGroupRefs() == []
        assert handler.getSdServerConfig() is None

    def test_ProvidedServiceInstance(self):
        """Test ProvidedServiceInstance class functionality."""
        parent = MockParent()
        instance = ProvidedServiceInstance(parent, "test_provided_service_instance")

        assert isinstance(instance, AbstractServiceInstance)
        
        # Test default values
        assert instance.getEventHandlers() == []
        assert instance.getInstanceIdentifier() is None
        assert instance.getPriority() is None
        assert instance.getSdServerConfig() is None
        assert instance.getServiceIdentifier() is None

    def test_ApplicationEndpoint(self):
        """Test ApplicationEndpoint class functionality."""
        parent = MockParent()
        endpoint = ApplicationEndpoint(parent, "test_app_endpoint")

        assert isinstance(endpoint, Identifiable)
        
        # Test default values
        assert endpoint.getConsumedServiceInstances() == []
        assert endpoint.getMaxNumberOfConnections() is None
        assert endpoint.getNetworkEndpointRef() is None
        assert endpoint.getPriority() is None
        assert endpoint.getProvidedServiceInstances() == []
        assert endpoint.getTlsCryptoMappingRef() is None
        assert endpoint.getTpConfiguration() is None

    def test_SocketAddress(self):
        """Test SocketAddress class functionality."""
        parent = MockParent()
        address = SocketAddress(parent, "test_socket_address")

        assert isinstance(address, Identifiable)
        
        # Test default values
        assert address.getAllowedIPv6ExtHeadersRef() is None
        assert address.getAllowedTcpOptionsRef() is None
        assert address.getApplicationEndpoint() is None
        assert address.getConnectorRef() is None
        assert address.getDifferentiatedServiceField() is None
        assert address.getFlowLabel() is None
        assert address.getMulticastConnectorRefs() == []
        assert address.getPathMtuDiscoveryEnabled() is None
        assert address.getPduCollectionMaxBufferSize() is None
        assert address.getPduCollectionTimeout() is None
        assert address.getPortAddress() is None
        assert address.getStaticSocketConnections() == []
        assert address.getUdpChecksumHandling() is None

    def test_SoAdConfig(self):
        """Test SoAdConfig class functionality."""
        config = SoAdConfig()

        assert isinstance(config, ARObject)
        
        # Test default values
        assert config.getConnections() == []
        assert config.getConnectionBundles() == []
        assert config.getSocketAddresses() == []