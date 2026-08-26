import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Boolean, PositiveInteger, RefType, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue import TagWithOptionalValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import ApplicationEndpoint, SdClientConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel import SocketConnection, SocketConnectionBundle
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    AbstractServiceInstance,
    ConsumedEventGroup,
    ConsumedServiceInstance,
    EventHandler,
    GenericTp,
    InitialSdDelayConfig,
    PduActivationRoutingGroup,
    ProvidedServiceInstance,
    RequestResponseDelay,
    SdServerConfig,
    ServiceVersionAcceptanceKindEnum,
    SoAdConfig,
    SocketAddress,
    SomeipSdClientEventGroupTimingConfig,
    SomeipSdClientServiceInstanceConfig,
    SomeipSdServerEventGroupTimingConfig,
    SomeipServiceVersion,
    StaticSocketConnection,
    TcpTp,
    TcpUdpConfig,
    TpPort,
    TransportProtocolConfiguration,
    UdpChecksumCalculationEnum,
    UdpTp,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_Fibex4EthernetServiceInstances:
    """Test cases for Fibex4Ethernet ServiceInstances classes."""

    def test_TransportProtocolConfiguration(self):
        """Test TransportProtocolConfiguration abstract class instantiation."""
        with pytest.raises(TypeError):
            TransportProtocolConfiguration()

    def test_GenericTp(self):
        """Test GenericTp class functionality."""
        tp = GenericTp()

        assert isinstance(tp, TransportProtocolConfiguration)

        # Test default values
        assert tp.getTpAddress() is None
        assert tp.getTpTechnology() is None

        # Test setter/getter methods with method chaining - with None
        assert tp == tp.setTpAddress(None)  # Test method chaining with None
        assert tp.getTpAddress() is None  # Should remain None

        assert tp == tp.setTpTechnology(None)  # Test method chaining with None
        assert tp.getTpTechnology() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        tp.setTpAddress("tcp://192.168.1.1:8080")
        assert tp.getTpAddress() == "tcp://192.168.1.1:8080"
        assert tp == tp.setTpAddress("tcp://192.168.1.1:8080")  # Test method chaining

        tp.setTpTechnology("TCP")
        assert tp.getTpTechnology() == "TCP"
        assert tp == tp.setTpTechnology("TCP")  # Test method chaining

    def test_TcpUdpConfig(self):
        """Test TcpUdpConfig abstract class instantiation."""
        with pytest.raises(TypeError):
            TcpUdpConfig()

    def test_TpPort(self):
        """Test TpPort class functionality."""
        port = TpPort()

        assert isinstance(port, ARObject)

        # Test default values
        assert port.getDynamicallyAssigned() is None
        assert port.getPortNumber() is None

        # Test setter/getter methods with method chaining - with None
        assert port == port.setDynamicallyAssigned(None)  # Test method chaining with None
        assert port.getDynamicallyAssigned() is None  # Should remain None

        assert port == port.setPortNumber(None)  # Test method chaining with None
        assert port.getPortNumber() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        port.setDynamicallyAssigned(True)
        assert port.getDynamicallyAssigned() is True
        assert port == port.setDynamicallyAssigned(True)  # Test method chaining

        port.setPortNumber(8080)
        assert port.getPortNumber() == 8080
        assert port == port.setPortNumber(8080)  # Test method chaining

    def test_UdpTp(self):
        """Test UdpTp class functionality."""
        tp = UdpTp()

        assert isinstance(tp, TcpUdpConfig)

        # Test default values
        assert tp.getUdpTpPort() is None

        # Test setter/getter methods with method chaining - with None
        assert tp == tp.setUdpTpPort(None)  # Test method chaining with None
        assert tp.getUdpTpPort() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual value
        port = TpPort()
        tp.setUdpTpPort(port)
        assert tp.getUdpTpPort() == port
        assert tp == tp.setUdpTpPort(port)  # Test method chaining

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

        # Test setter/getter methods with method chaining - with None
        assert tp == tp.setKeepAliveInterval(None)  # Test method chaining with None
        assert tp.getKeepAliveInterval() is None  # Should remain None

        assert tp == tp.setKeepAliveProbesMax(None)  # Test method chaining with None
        assert tp.getKeepAliveProbesMax() is None  # Should remain None

        assert tp == tp.setKeepAlives(None)  # Test method chaining with None
        assert tp.getKeepAlives() is None  # Should remain None

        assert tp == tp.setKeepAliveTime(None)  # Test method chaining with None
        assert tp.getKeepAliveTime() is None  # Should remain None

        assert tp == tp.setNaglesAlgorithm(None)  # Test method chaining with None
        assert tp.getNaglesAlgorithm() is None  # Should remain None

        assert tp == tp.setReceiveWindowMin(None)  # Test method chaining with None
        assert tp.getReceiveWindowMin() is None  # Should remain None

        assert tp == tp.setTcpRetransmissionTimeout(None)  # Test method chaining with None
        assert tp.getTcpRetransmissionTimeout() is None  # Should remain None

        assert tp == tp.setTcpTpPort(None)  # Test method chaining with None
        assert tp.getTcpTpPort() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        tp.setKeepAliveTime(7200)
        assert tp.getKeepAliveTime() == 7200
        assert tp == tp.setKeepAliveTime(7200)  # Test method chaining

        tp.setNaglesAlgorithm(True)
        assert tp.getNaglesAlgorithm() is True
        assert tp == tp.setNaglesAlgorithm(True)  # Test method chaining

        tp.setKeepAliveProbesMax(5)
        assert tp.getKeepAliveProbesMax() == 5
        assert tp == tp.setKeepAliveProbesMax(5)  # Test method chaining

        tp.setKeepAliveInterval(1000)
        assert tp.getKeepAliveInterval() == 1000
        assert tp == tp.setKeepAliveInterval(1000)  # Test method chaining

        tp.setReceiveWindowMin(1024)
        assert tp.getReceiveWindowMin() == 1024
        assert tp == tp.setReceiveWindowMin(1024)  # Test method chaining

        tp.setTcpRetransmissionTimeout(3000)
        assert tp.getTcpRetransmissionTimeout() == 3000
        assert tp == tp.setTcpRetransmissionTimeout(3000)  # Test method chaining

        port = TpPort()
        tp.setTcpTpPort(port)
        assert tp.getTcpTpPort() == port
        assert tp == tp.setTcpTpPort(port)  # Test method chaining

    def test_InitialSdDelayConfig(self):
        """Test InitialSdDelayConfig class functionality."""
        config = InitialSdDelayConfig()

        assert isinstance(config, ARObject)

        # Test default values
        assert config.getInitialDelayMaxValue() is None
        assert config.getInitialDelayMinValue() is None
        assert config.getInitialRepetitionsBaseDelay() is None
        assert config.getInitialRepetitionsMax() is None

        # Test setter/getter methods with method chaining - with None
        assert config == config.setInitialDelayMaxValue(None)  # Test method chaining with None
        assert config.getInitialDelayMaxValue() is None  # Should remain None

        assert config == config.setInitialDelayMinValue(None)  # Test method chaining with None
        assert config.getInitialDelayMinValue() is None  # Should remain None

        assert config == config.setInitialRepetitionsBaseDelay(None)  # Test method chaining with None
        assert config.getInitialRepetitionsBaseDelay() is None  # Should remain None

        assert config == config.setInitialRepetitionsMax(None)  # Test method chaining with None
        assert config.getInitialRepetitionsMax() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        config.setInitialDelayMaxValue(5000)
        assert config.getInitialDelayMaxValue() == 5000
        assert config == config.setInitialDelayMaxValue(5000)  # Test method chaining

        config.setInitialDelayMinValue(1000)
        assert config.getInitialDelayMinValue() == 1000
        assert config == config.setInitialDelayMinValue(1000)  # Test method chaining

        config.setInitialRepetitionsBaseDelay(2000)
        assert config.getInitialRepetitionsBaseDelay() == 2000
        assert config == config.setInitialRepetitionsBaseDelay(2000)  # Test method chaining

        config.setInitialRepetitionsMax(3)
        assert config.getInitialRepetitionsMax() == 3
        assert config == config.setInitialRepetitionsMax(3)  # Test method chaining

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

        # Test setter/getter methods with method chaining - with None
        assert config == config.setCapabilityRecords(None)  # Test method chaining with None
        assert config.getCapabilityRecords() == []  # Should remain empty

        assert config == config.setInitialOfferBehavior(None)  # Test method chaining with None
        assert config.getInitialOfferBehavior() is None  # Should remain None

        assert config == config.setOfferCyclicDelay(None)  # Test method chaining with None
        assert config.getOfferCyclicDelay() is None  # Should remain None

        assert config == config.setRequestResponseDelay(None)  # Test method chaining with None
        assert config.getRequestResponseDelay() is None  # Should remain None

        assert config == config.setServerServiceMajorVersion(None)  # Test method chaining with None
        assert config.getServerServiceMajorVersion() is None  # Should remain None

        assert config == config.setServerServiceMinorVersion(None)  # Test method chaining with None
        assert config.getServerServiceMinorVersion() is None  # Should remain None

        assert config == config.setTtl(None)  # Test method chaining with None
        assert config.getTtl() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        config.setCapabilityRecords(["record1", "record2"])
        assert "record1" in config.getCapabilityRecords()
        assert config == config.setCapabilityRecords(["record1", "record2"])  # Test method chaining

        delay_config = InitialSdDelayConfig()
        config.setInitialOfferBehavior(delay_config)
        assert config.getInitialOfferBehavior() == delay_config
        assert config == config.setInitialOfferBehavior(delay_config)  # Test method chaining

        config.setOfferCyclicDelay(1000)
        assert config.getOfferCyclicDelay() == 1000
        assert config == config.setOfferCyclicDelay(1000)  # Test method chaining

        config.setRequestResponseDelay("delay_config")
        assert config.getRequestResponseDelay() == "delay_config"
        assert config == config.setRequestResponseDelay("delay_config")  # Test method chaining

        config.setServerServiceMajorVersion(2)
        assert config.getServerServiceMajorVersion() == 2
        assert config == config.setServerServiceMajorVersion(2)  # Test method chaining

        config.setServerServiceMinorVersion(1)
        assert config.getServerServiceMinorVersion() == 1
        assert config == config.setServerServiceMinorVersion(1)  # Test method chaining

        config.setTtl(64)
        assert config.getTtl() == 64
        assert config == config.setTtl(64)  # Test method chaining

    def test_EventHandler(self):
        """Test EventHandler class functionality (Table 6.166)."""
        parent = MockParent()
        handler = EventHandler(parent, "test_event_handler")

        assert isinstance(handler, Identifiable)

        # Test default values
        assert handler.getConsumedEventGroupRefs() == []
        assert handler.getEventGroupIdentifier() is None
        assert handler.getEventMulticastAddressRef() is None
        assert handler.getMulticastThreshold() is None
        assert handler.getPduActivationRoutingGroups() == []
        assert handler.getRoutingGroupRefs() == []
        assert handler.getSdServerConfig() is None
        assert handler.getSdServerEgTimingConfigRef() is None

        # Test setter/getter methods with method chaining - with None no-ops
        assert handler == handler.setMulticastThreshold(None)  # Test method chaining with None
        assert handler.getMulticastThreshold() is None  # Should remain None

        assert handler == handler.setSdServerConfig(None)  # Test method chaining with None
        assert handler.getSdServerConfig() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        handler.setMulticastThreshold(10)
        assert handler.getMulticastThreshold() == 10
        assert handler == handler.setMulticastThreshold(10)  # Test method chaining

        config = SdServerConfig()
        handler.setSdServerConfig(config)
        assert handler.getSdServerConfig() == config
        assert handler == handler.setSdServerConfig(config)  # Test method chaining

        # Test add methods
        handler.addConsumedEventGroupRef("event_group_ref1")
        assert "event_group_ref1" in handler.getConsumedEventGroupRefs()
        assert handler == handler.addConsumedEventGroupRef("event_group_ref1")  # Test method chaining

        handler.addRoutingGroupRef("routing_ref1")
        assert "routing_ref1" in handler.getRoutingGroupRefs()
        assert handler == handler.addRoutingGroupRef("routing_ref1")  # Test method chaining

    def test_ProvidedServiceInstance(self):
        """Test ProvidedServiceInstance class functionality."""
        parent = MockParent()
        instance = ProvidedServiceInstance(parent, "test_provided_service_instance")

        assert isinstance(instance, AbstractServiceInstance)

        # Test default values
        assert instance.getEventHandlers() == []
        assert instance.getInstanceIdentifier() is None
        assert instance.getLoadBalancingPriority() is None
        assert instance.getLoadBalancingWeight() is None
        assert instance.getLocalUnicastAddressRefs() == []
        assert instance.getMinorVersion() is None
        assert instance.getPriority() is None
        assert instance.getRemoteMulticastSubscriptionAddressRefs() == []
        assert instance.getRemoteUnicastAddressRefs() == []
        assert instance.getSdServerConfig() is None
        assert instance.getSdServerTimerConfigRef() is None
        assert instance.getServiceIdentifier() is None

        # Test setter/getter methods with method chaining - with None
        assert instance == instance.setInstanceIdentifier(None)  # Test method chaining with None
        assert instance.getInstanceIdentifier() is None  # Should remain None

        assert instance == instance.setLoadBalancingPriority(None)  # Test method chaining with None
        assert instance.getLoadBalancingPriority() is None  # Should remain None

        assert instance == instance.setLoadBalancingWeight(None)  # Test method chaining with None
        assert instance.getLoadBalancingWeight() is None  # Should remain None

        assert instance == instance.setMinorVersion(None)  # Test method chaining with None
        assert instance.getMinorVersion() is None  # Should remain None

        assert instance == instance.setPriority(None)  # Test method chaining with None
        assert instance.getPriority() is None  # Should remain None

        assert instance == instance.setSdServerConfig(None)  # Test method chaining with None
        assert instance.getSdServerConfig() is None  # Should remain None

        assert instance == instance.setSdServerTimerConfigRef(None)  # Test method chaining with None
        assert instance.getSdServerTimerConfigRef() is None  # Should remain None

        assert instance == instance.setServiceIdentifier(None)  # Test method chaining with None
        assert instance.getServiceIdentifier() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        instance.setInstanceIdentifier(200)
        assert instance.getInstanceIdentifier() == 200
        assert instance == instance.setInstanceIdentifier(200)  # Test method chaining

        instance.setLoadBalancingPriority(7)
        assert instance.getLoadBalancingPriority() == 7
        assert instance == instance.setLoadBalancingPriority(7)  # Test method chaining

        instance.setLoadBalancingWeight(3)
        assert instance.getLoadBalancingWeight() == 3
        assert instance == instance.setLoadBalancingWeight(3)  # Test method chaining

        instance.setMinorVersion(2)
        assert instance.getMinorVersion() == 2
        assert instance == instance.setMinorVersion(2)  # Test method chaining

        instance.setPriority(3)
        assert instance.getPriority() == 3
        assert instance == instance.setPriority(3)  # Test method chaining

        config = object()
        instance.setSdServerConfig(config)
        assert instance.getSdServerConfig() == config
        assert instance == instance.setSdServerConfig(config)  # Test method chaining

        instance.setSdServerTimerConfigRef("sd_server_timer_config_ref")
        assert instance.getSdServerTimerConfigRef() == "sd_server_timer_config_ref"
        assert instance == instance.setSdServerTimerConfigRef("sd_server_timer_config_ref")  # Test method chaining

        instance.setServiceIdentifier(25)
        assert instance.getServiceIdentifier() == 25
        assert instance == instance.setServiceIdentifier(25)  # Test method chaining

        # Test add methods for reference lists
        instance.addLocalUnicastAddressRef("local_unicast_ref1")
        assert "local_unicast_ref1" in instance.getLocalUnicastAddressRefs()
        assert instance == instance.addLocalUnicastAddressRef("local_unicast_ref1")  # Test method chaining

        instance.addAllowedServiceConsumerRef("network_endpoint_ref1")
        assert "network_endpoint_ref1" in instance.getAllowedServiceConsumerRefs()
        assert instance == instance.addAllowedServiceConsumerRef("network_endpoint_ref1")  # Test method chaining
        assert instance == instance.setAllowedServiceConsumerRefs(["network_endpoint_ref2"])
        assert instance.getAllowedServiceConsumerRefs() == ["network_endpoint_ref2"]
        assert instance == instance.setAllowedServiceConsumerRefs(None)  # None no-op
        assert instance.getAllowedServiceConsumerRefs() == ["network_endpoint_ref2"]

        instance.setLocalUnicastAddressRefs(["local_unicast_ref2"])
        assert "local_unicast_ref2" in instance.getLocalUnicastAddressRefs()

        instance.addRemoteMulticastSubscriptionAddressRef("remote_multicast_ref1")
        assert "remote_multicast_ref1" in instance.getRemoteMulticastSubscriptionAddressRefs()
        assert instance == instance.addRemoteMulticastSubscriptionAddressRef("remote_multicast_ref1")  # Test method chaining

        instance.addRemoteUnicastAddressRef("remote_unicast_ref1")
        assert "remote_unicast_ref1" in instance.getRemoteUnicastAddressRefs()
        assert instance == instance.addRemoteUnicastAddressRef("remote_unicast_ref1")  # Test method chaining

        # Test create method for event handlers
        event_handler = instance.createEventHandler("test_event_handler")
        assert isinstance(event_handler, EventHandler)
        assert len(instance.getEventHandlers()) == 1

        # Test autoAvailable attribute (Boolean, 0..1)
        assert instance == instance.setAutoAvailable(None)  # None no-op
        assert instance.getAutoAvailable() is None
        instance.setAutoAvailable(True)
        assert instance.getAutoAvailable() is True
        assert instance == instance.setAutoAvailable(True)  # Test method chaining

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

        # Test setter/getter methods with method chaining - with None
        assert endpoint == endpoint.setMaxNumberOfConnections(None)  # Test method chaining with None
        assert endpoint.getMaxNumberOfConnections() is None  # Should remain None

        assert endpoint == endpoint.setNetworkEndpointRef(None)  # Test method chaining with None
        assert endpoint.getNetworkEndpointRef() is None  # Should remain None

        assert endpoint == endpoint.setPriority(None)  # Test method chaining with None
        assert endpoint.getPriority() is None  # Should remain None

        assert endpoint == endpoint.setTlsCryptoMappingRef(None)  # Test method chaining with None
        assert endpoint.getTlsCryptoMappingRef() is None  # Should remain None

        assert endpoint == endpoint.setTpConfiguration(None)  # Test method chaining with None
        assert endpoint.getTpConfiguration() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        endpoint.setMaxNumberOfConnections(10)
        assert endpoint.getMaxNumberOfConnections() == 10
        assert endpoint == endpoint.setMaxNumberOfConnections(10)  # Test method chaining

        endpoint.setNetworkEndpointRef("network_endpoint_ref")
        assert endpoint.getNetworkEndpointRef() == "network_endpoint_ref"
        assert endpoint == endpoint.setNetworkEndpointRef("network_endpoint_ref")  # Test method chaining

        endpoint.setPriority(4)
        assert endpoint.getPriority() == 4
        assert endpoint == endpoint.setPriority(4)  # Test method chaining

        endpoint.setTlsCryptoMappingRef("tls_mapping_ref")
        assert endpoint.getTlsCryptoMappingRef() == "tls_mapping_ref"
        assert endpoint == endpoint.setTlsCryptoMappingRef("tls_mapping_ref")  # Test method chaining

        config = object()
        endpoint.setTpConfiguration(config)
        assert endpoint.getTpConfiguration() == config
        assert endpoint == endpoint.setTpConfiguration(config)  # Test method chaining

        # Test create methods
        consumed_instance = endpoint.createConsumedServiceInstance("test_consumed_instance")
        assert isinstance(consumed_instance, ConsumedServiceInstance)
        assert len(endpoint.getConsumedServiceInstances()) == 1

        provided_instance = endpoint.createProvidedServiceInstance("test_provided_instance")
        assert isinstance(provided_instance, ProvidedServiceInstance)
        assert len(endpoint.getProvidedServiceInstances()) == 1

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
        assert address.getStaticSocketConnections() == []
        assert address.getUdpChecksumHandling() is None

        # Test setter/getter methods with method chaining - with None
        assert address == address.setAllowedIPv6ExtHeadersRef(None)  # Test method chaining with None
        assert address.getAllowedIPv6ExtHeadersRef() is None  # Should remain None

        assert address == address.setAllowedTcpOptionsRef(None)  # Test method chaining with None
        assert address.getAllowedTcpOptionsRef() is None  # Should remain None

        assert address == address.setConnectorRef(None)  # Test method chaining with None
        assert address.getConnectorRef() is None  # Should remain None

        assert address == address.setDifferentiatedServiceField(None)  # Test method chaining with None
        assert address.getDifferentiatedServiceField() is None  # Should remain None

        assert address == address.setFlowLabel(None)  # Test method chaining with None
        assert address.getFlowLabel() is None  # Should remain None

        assert address == address.setPathMtuDiscoveryEnabled(None)  # Test method chaining with None
        assert address.getPathMtuDiscoveryEnabled() is None  # Should remain None

        assert address == address.setPduCollectionMaxBufferSize(None)  # Test method chaining with None
        assert address.getPduCollectionMaxBufferSize() is None  # Should remain None

        assert address == address.setPduCollectionTimeout(None)  # Test method chaining with None
        assert address.getPduCollectionTimeout() is None  # Should remain None

        assert address == address.setUdpChecksumHandling(None)  # Test method chaining with None
        assert address.getUdpChecksumHandling() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        address.setAllowedIPv6ExtHeadersRef("ipv6_ext_ref")
        assert address.getAllowedIPv6ExtHeadersRef() == "ipv6_ext_ref"
        assert address == address.setAllowedIPv6ExtHeadersRef("ipv6_ext_ref")  # Test method chaining

        address.setAllowedTcpOptionsRef("tcp_options_ref")
        assert address.getAllowedTcpOptionsRef() == "tcp_options_ref"
        assert address == address.setAllowedTcpOptionsRef("tcp_options_ref")  # Test method chaining

        address.setConnectorRef("connector_ref")
        assert address.getConnectorRef() == "connector_ref"
        assert address == address.setConnectorRef("connector_ref")  # Test method chaining

        address.setDifferentiatedServiceField(46)
        assert address.getDifferentiatedServiceField() == 46
        assert address == address.setDifferentiatedServiceField(46)  # Test method chaining

        address.setFlowLabel(12345)
        assert address.getFlowLabel() == 12345
        assert address == address.setFlowLabel(12345)  # Test method chaining

        address.setPathMtuDiscoveryEnabled(True)
        assert address.getPathMtuDiscoveryEnabled() is True
        assert address == address.setPathMtuDiscoveryEnabled(True)  # Test method chaining

        address.setPduCollectionMaxBufferSize(1024)
        assert address.getPduCollectionMaxBufferSize() == 1024
        assert address == address.setPduCollectionMaxBufferSize(1024)  # Test method chaining

        address.setPduCollectionTimeout(5000)
        assert address.getPduCollectionTimeout() == 5000
        assert address == address.setPduCollectionTimeout(5000)  # Test method chaining

        address.setUdpChecksumHandling("udp_checksum")
        assert address.getUdpChecksumHandling() == "udp_checksum"
        assert address == address.setUdpChecksumHandling("udp_checksum")  # Test method chaining

        # Test add methods
        address.addMulticastConnectorRef("multicast_connector_ref")
        assert "multicast_connector_ref" in address.getMulticastConnectorRefs()
        assert address == address.addMulticastConnectorRef("multicast_connector_ref")  # Test method chaining

        address.addStaticSocketConnection("static_connection")
        assert "static_connection" in address.getStaticSocketConnections()
        assert address == address.addStaticSocketConnection("static_connection")  # Test method chaining

        # Test create method for application endpoint
        app_endpoint = address.createApplicationEndpoint("test_app_endpoint")
        assert isinstance(app_endpoint, ApplicationEndpoint)
        assert address.getApplicationEndpoint() == app_endpoint

    def test_SoAdConfig(self):
        """
        Test SoAdConfig class functionality (Table 6.117).
        """
        config = SoAdConfig()

        assert isinstance(config, ARObject)

        # Test default values
        assert config.getConnections() == []
        assert config.getConnectionBundles() == []
        assert config.getSocketAddresses() == []

        # Test addConnection (connection * aggr, obsolete; SocketConnection is a Describable value type — not Referrable)
        connection = SocketConnection()
        result = config.addConnection(connection)
        assert config.getConnections() == [connection]
        assert result == config  # method chaining

        # Test createSocketConnectionBundle (connectionBundle * aggr, obsolete)
        bundle = config.createSocketConnectionBundle("test_bundle")
        assert isinstance(bundle, SocketConnectionBundle)
        assert len(config.getConnectionBundles()) == 1

        config.createSocketConnectionBundle("test_bundle2")
        assert len(config.getConnectionBundles()) == 2

        # Test createSocketAddress (socketAddress * aggr)
        socket_addr = config.createSocketAddress("test_socket_addr")
        assert isinstance(socket_addr, SocketAddress)
        assert len(config.getSocketAddresses()) == 1
        assert config.getSocketAddresses()[0].getShortName() == "test_socket_addr"


class TestSomeipSdClientServiceInstanceConfig:
    """Test cases for SomeipSdClientServiceInstanceConfig class."""

    def test_initialization(self):
        """Test SomeipSdClientServiceInstanceConfig defaults."""
        parent = MockParent()
        config = SomeipSdClientServiceInstanceConfig(parent, "test_config")

        assert config.getInitialFindBehavior() is None
        assert config.getPriority() is None
        assert config.getServiceFindTimeToLive() is None

    def test_get_set_initialFindBehavior(self):
        """Test get/set initialFindBehavior with None no-op and chaining."""
        parent = MockParent()
        config = SomeipSdClientServiceInstanceConfig(parent, "test_config")

        assert config == config.setInitialFindBehavior(None)
        assert config.getInitialFindBehavior() is None

        behavior = InitialSdDelayConfig()
        config.setInitialFindBehavior(behavior)
        assert config.getInitialFindBehavior() == behavior
        assert config == config.setInitialFindBehavior(behavior)

    def test_get_set_priority(self):
        """Test get/set priority with None no-op and chaining."""
        parent = MockParent()
        config = SomeipSdClientServiceInstanceConfig(parent, "test_config")

        assert config == config.setPriority(None)
        assert config.getPriority() is None

        config.setPriority(5)
        assert config.getPriority() == 5
        assert config == config.setPriority(5)

    def test_get_set_serviceFindTimeToLive(self):
        """Test get/set serviceFindTimeToLive with None no-op and chaining."""
        parent = MockParent()
        config = SomeipSdClientServiceInstanceConfig(parent, "test_config")

        assert config == config.setServiceFindTimeToLive(None)
        assert config.getServiceFindTimeToLive() is None

        config.setServiceFindTimeToLive(60)
        assert config.getServiceFindTimeToLive() == 60
        assert config == config.setServiceFindTimeToLive(60)


class TestSomeipSdClientEventGroupTimingConfig:
    """Test cases for SomeipSdClientEventGroupTimingConfig class."""

    def test_initialization(self):
        """Test SomeipSdClientEventGroupTimingConfig defaults."""
        parent = MockParent()
        config = SomeipSdClientEventGroupTimingConfig(parent, "test_config")

        assert config.getRequestResponseDelay() is None
        assert config.getSubscribeEventgroupRetryDelay() is None
        assert config.getSubscribeEventgroupRetryMax() is None
        assert config.getTimeToLive() is None

    def test_get_set_requestResponseDelay(self):
        """Test get/set requestResponseDelay with None no-op and chaining."""
        parent = MockParent()
        config = SomeipSdClientEventGroupTimingConfig(parent, "test_config")

        assert config == config.setRequestResponseDelay(None)
        assert config.getRequestResponseDelay() is None

        delay = RequestResponseDelay()
        config.setRequestResponseDelay(delay)
        assert config.getRequestResponseDelay() == delay
        assert config == config.setRequestResponseDelay(delay)

    def test_get_set_subscribeEventgroupRetryDelay(self):
        """Test get/set subscribeEventgroupRetryDelay with None no-op and chaining."""
        parent = MockParent()
        config = SomeipSdClientEventGroupTimingConfig(parent, "test_config")

        assert config == config.setSubscribeEventgroupRetryDelay(None)
        assert config.getSubscribeEventgroupRetryDelay() is None

        config.setSubscribeEventgroupRetryDelay(5)
        assert config.getSubscribeEventgroupRetryDelay() == 5
        assert config == config.setSubscribeEventgroupRetryDelay(5)

    def test_get_set_subscribeEventgroupRetryMax(self):
        """Test get/set subscribeEventgroupRetryMax with None no-op and chaining."""
        parent = MockParent()
        config = SomeipSdClientEventGroupTimingConfig(parent, "test_config")

        assert config == config.setSubscribeEventgroupRetryMax(None)
        assert config.getSubscribeEventgroupRetryMax() is None

        config.setSubscribeEventgroupRetryMax(60)
        assert config.getSubscribeEventgroupRetryMax() == 60
        assert config == config.setSubscribeEventgroupRetryMax(60)

    def test_get_set_timeToLive(self):
        """Test get/set timeToLive with None no-op and chaining."""
        parent = MockParent()
        config = SomeipSdClientEventGroupTimingConfig(parent, "test_config")

        assert config == config.setTimeToLive(None)
        assert config.getTimeToLive() is None

        config.setTimeToLive(255)
        assert config.getTimeToLive() == 255
        assert config == config.setTimeToLive(255)


class TestSomeipSdServerEventGroupTimingConfig:
    """Test cases for SomeipSdServerEventGroupTimingConfig class."""

    def test_initialization(self):
        """Test SomeipSdServerEventGroupTimingConfig defaults."""
        parent = MockParent()
        config = SomeipSdServerEventGroupTimingConfig(parent, "test_config")

        assert config.getRequestResponseDelay() is None

    def test_get_set_requestResponseDelay(self):
        """Test get/set requestResponseDelay with None no-op and chaining."""
        parent = MockParent()
        config = SomeipSdServerEventGroupTimingConfig(parent, "test_config")

        assert config == config.setRequestResponseDelay(None)
        assert config.getRequestResponseDelay() is None

        delay = RequestResponseDelay()
        config.setRequestResponseDelay(delay)
        assert config.getRequestResponseDelay() == delay
        assert config == config.setRequestResponseDelay(delay)


class TestSomeipServiceVersion:
    """Test cases for SomeipServiceVersion class (Table F.118, p.2059)."""

    def test_initialization(self):
        """Test SomeipServiceVersion defaults."""
        version = SomeipServiceVersion()

        assert isinstance(version, ARObject)
        assert version.getMajorVersion() is None
        assert version.getMinorVersion() is None

    def test_get_set_majorVersion(self):
        """Test get/set majorVersion with None no-op and chaining."""
        version = SomeipServiceVersion()

        assert version == version.setMajorVersion(None)
        assert version.getMajorVersion() is None

        version.setMajorVersion(PositiveInteger().setValue("4"))
        assert version.getMajorVersion().getValue() == 4
        assert version == version.setMajorVersion(PositiveInteger().setValue("4"))

    def test_get_set_minorVersion(self):
        """Test get/set minorVersion with None no-op and chaining."""
        version = SomeipServiceVersion()

        assert version == version.setMinorVersion(None)
        assert version.getMinorVersion() is None

        version.setMinorVersion(PositiveInteger().setValue("2"))
        assert version.getMinorVersion().getValue() == 2
        assert version == version.setMinorVersion(PositiveInteger().setValue("2"))


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


class TestConsumedEventGroup:
    def _group(self):
        return ConsumedEventGroup(MockParent(), "ceg")

    def test_initialization(self):
        """Test __init__ defaults for all fields (Table 6.168)."""
        group = self._group()

        assert isinstance(group, Identifiable)
        assert group.getShortName() == "ceg"
        assert group.getApplicationEndpointRef() is None
        assert group.getAutoRequire() is None
        assert group.getEventGroupIdentifier() is None
        assert group.getEventMulticastAddressRefs() == []
        assert group.getPduActivationRoutingGroups() == []
        assert group.getPriority() is None
        assert group.getRoutingGroupRefs() == []
        assert group.getSdClientConfig() is None
        assert group.getSdClientTimerConfigRef() is None

    def test_get_set_applicationEndpointRef(self):
        """Test get/set applicationEndpointRef with chaining and None no-op."""
        group = self._group()
        ref = _ref("/Ethernet/ApplicationEndpoint/AE1")

        assert group.setApplicationEndpointRef(ref) is group
        assert group.getApplicationEndpointRef() is ref

        group.setApplicationEndpointRef(None)
        assert group.getApplicationEndpointRef() is ref

    def test_get_set_autoRequire(self):
        """Test get/set autoRequire with chaining and None no-op."""
        group = self._group()
        value = Boolean().setValue("true")

        assert group.setAutoRequire(value) is group
        assert group.getAutoRequire() is value
        assert group.getAutoRequire().getValue() is True

        group.setAutoRequire(None)
        assert group.getAutoRequire() is value

    def test_get_set_eventGroupIdentifier(self):
        """Test get/set eventGroupIdentifier with chaining and None no-op."""
        group = self._group()

        assert group.setEventGroupIdentifier(PositiveInteger().setValue("42")) is group
        assert group.getEventGroupIdentifier().getValue() == 42

        group.setEventGroupIdentifier(None)
        assert group.getEventGroupIdentifier().getValue() == 42

    def test_add_get_eventMulticastAddressRefs(self):
        """Test add/get eventMulticastAddressRefs append order and None no-op."""
        group = self._group()
        ref1 = _ref("/Ethernet/ApplicationEndpoint/MC1")
        ref2 = _ref("/Ethernet/ApplicationEndpoint/MC2")

        assert group.addEventMulticastAddressRef(ref1) is group
        group.addEventMulticastAddressRef(ref2)
        assert group.getEventMulticastAddressRefs() == [ref1, ref2]

        group.addEventMulticastAddressRef(None)
        assert group.getEventMulticastAddressRefs() == [ref1, ref2]

    def test_add_get_pduActivationRoutingGroups(self):
        """Test add/get pduActivationRoutingGroups (placeholder child type) and None no-op."""
        group = self._group()
        routing_group1 = MockParent()
        routing_group2 = MockParent()

        assert group.addPduActivationRoutingGroup(routing_group1) is group
        group.addPduActivationRoutingGroup(routing_group2)
        assert group.getPduActivationRoutingGroups() == [routing_group1, routing_group2]

        group.addPduActivationRoutingGroup(None)
        assert group.getPduActivationRoutingGroups() == [routing_group1, routing_group2]

    def test_get_set_priority(self):
        """Test get/set priority with chaining and None no-op."""
        group = self._group()

        assert group.setPriority(PositiveInteger().setValue("5")) is group
        assert group.getPriority().getValue() == 5

        group.setPriority(None)
        assert group.getPriority().getValue() == 5

    def test_add_get_routingGroupRefs(self):
        """Test add/get routingGroupRefs append order and None no-op."""
        group = self._group()
        ref1 = _ref("/SoAd/RoutingGroup/RG1")
        ref2 = _ref("/SoAd/RoutingGroup/RG2")

        assert group.addRoutingGroupRef(ref1) is group
        group.addRoutingGroupRef(ref2)
        assert group.getRoutingGroupRefs() == [ref1, ref2]

        group.addRoutingGroupRef(None)
        assert group.getRoutingGroupRefs() == [ref1, ref2]

    def test_get_set_sdClientConfig(self):
        """Test get/set sdClientConfig with chaining and None no-op."""
        group = self._group()
        config = SdClientConfig()

        assert group.setSdClientConfig(config) is group
        assert group.getSdClientConfig() is config

        group.setSdClientConfig(None)
        assert group.getSdClientConfig() is config

    def test_get_set_sdClientTimerConfigRef(self):
        """Test get/set sdClientTimerConfigRef with chaining and None no-op."""
        group = self._group()
        ref = _ref("/SomeipSdTimingConfigs/Timing1")

        assert group.setSdClientTimerConfigRef(ref) is group
        assert group.getSdClientTimerConfigRef() is ref

        group.setSdClientTimerConfigRef(None)
        assert group.getSdClientTimerConfigRef() is ref


class TestConsumedServiceInstance:
    def _instance(self):
        return ConsumedServiceInstance(MockParent(), "csi")

    def test_initialization(self):
        """Test __init__ defaults for all fields (Table 6.167)."""
        instance = self._instance()

        assert isinstance(instance, AbstractServiceInstance)
        assert instance.getShortName() == "csi"
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

    def test_add_get_allowedServiceProviderRefs(self):
        """Test add/get allowedServiceProviderRefs append order and None no-op."""
        instance = self._instance()
        ref1 = _ref("/Ethernet/NetworkEndpoint/NE1")
        ref2 = _ref("/Ethernet/NetworkEndpoint/NE2")

        assert instance.addAllowedServiceProviderRef(ref1) is instance
        instance.addAllowedServiceProviderRef(ref2)
        assert instance.getAllowedServiceProviderRefs() == [ref1, ref2]

        instance.addAllowedServiceProviderRef(None)
        assert instance.getAllowedServiceProviderRefs() == [ref1, ref2]

    def test_get_set_autoRequire(self):
        """Test get/set autoRequire with chaining and None no-op."""
        instance = self._instance()
        value = Boolean().setValue("true")

        assert instance.setAutoRequire(value) is instance
        assert instance.getAutoRequire() is value
        assert instance.getAutoRequire().getValue() is True

        instance.setAutoRequire(None)
        assert instance.getAutoRequire() is value

    def test_add_get_blocklistedVersions(self):
        """Test add/get blocklistedVersions append order and None no-op."""
        instance = self._instance()
        version1 = SomeipServiceVersion()
        version1.setMajorVersion(PositiveInteger().setValue("1"))
        version1.setMinorVersion(PositiveInteger().setValue("0"))
        version2 = SomeipServiceVersion()
        version2.setMajorVersion(PositiveInteger().setValue("2"))
        version2.setMinorVersion(PositiveInteger().setValue("5"))

        assert instance.addBlocklistedVersion(version1) is instance
        instance.addBlocklistedVersion(version2)
        assert instance.getBlocklistedVersions() == [version1, version2]

        instance.addBlocklistedVersion(None)
        assert instance.getBlocklistedVersions() == [version1, version2]

    def test_create_get_consumedEventGroups(self):
        """Test create/get consumedEventGroups: appended, duplicate returns existing."""
        instance = self._instance()

        group = instance.createConsumedEventGroup("CEG1")
        assert isinstance(group, ConsumedEventGroup)
        assert instance.createConsumedEventGroup("CEG1") is group
        assert instance.getConsumedEventGroups() == [group]
        assert len(instance.getConsumedEventGroups()) == 1

    def test_get_set_eventMulticastSubscriptionAddressRef(self):
        """Test get/set eventMulticastSubscriptionAddressRef with chaining and None no-op."""
        instance = self._instance()
        ref = _ref("/Ethernet/ApplicationEndpoint/MC1")

        assert instance.setEventMulticastSubscriptionAddressRef(ref) is instance
        assert instance.getEventMulticastSubscriptionAddressRef() is ref

        instance.setEventMulticastSubscriptionAddressRef(None)
        assert instance.getEventMulticastSubscriptionAddressRef() is ref

    def test_get_set_instanceIdentifier(self):
        """Test get/set instanceIdentifier with chaining and None no-op."""
        instance = self._instance()
        value = String().setValue("123")

        assert instance.setInstanceIdentifier(value) is instance
        assert instance.getInstanceIdentifier() is value
        assert instance.getInstanceIdentifier().getValue() == "123"

        instance.setInstanceIdentifier(None)
        assert instance.getInstanceIdentifier() is value

    def test_add_get_localUnicastAddressRefs(self):
        """Test add/get localUnicastAddressRefs append order and None no-op."""
        instance = self._instance()
        ref1 = _ref("/Ethernet/ApplicationEndpoint/LU1")
        ref2 = _ref("/Ethernet/ApplicationEndpoint/LU2")

        assert instance.addLocalUnicastAddressRef(ref1) is instance
        instance.addLocalUnicastAddressRef(ref2)
        assert instance.getLocalUnicastAddressRefs() == [ref1, ref2]

        instance.addLocalUnicastAddressRef(None)
        assert instance.getLocalUnicastAddressRefs() == [ref1, ref2]

    def test_get_set_minorVersion(self):
        """Test get/set minorVersion with chaining and None no-op."""
        instance = self._instance()
        value = String().setValue("ANY")

        assert instance.setMinorVersion(value) is instance
        assert instance.getMinorVersion() is value
        assert instance.getMinorVersion().getValue() == "ANY"

        instance.setMinorVersion(None)
        assert instance.getMinorVersion() is value

    def test_get_set_providedServiceInstanceRef(self):
        """Test get/set providedServiceInstanceRef with chaining and None no-op."""
        instance = self._instance()
        ref = _ref("/Ether/Provider/PSI1")

        assert instance.setProvidedServiceInstanceRef(ref) is instance
        assert instance.getProvidedServiceInstanceRef() is ref

        instance.setProvidedServiceInstanceRef(None)
        assert instance.getProvidedServiceInstanceRef() is ref

    def test_add_get_remoteUnicastAddressRefs(self):
        """Test add/get remoteUnicastAddressRefs append order and None no-op."""
        instance = self._instance()
        ref1 = _ref("/Ethernet/ApplicationEndpoint/RU1")
        ref2 = _ref("/Ethernet/ApplicationEndpoint/RU2")

        assert instance.addRemoteUnicastAddressRef(ref1) is instance
        instance.addRemoteUnicastAddressRef(ref2)
        assert instance.getRemoteUnicastAddressRefs() == [ref1, ref2]

        instance.addRemoteUnicastAddressRef(None)
        assert instance.getRemoteUnicastAddressRefs() == [ref1, ref2]

    def test_get_set_sdClientConfig(self):
        """Test get/set sdClientConfig with chaining and None no-op."""
        instance = self._instance()
        config = SdClientConfig()

        assert instance.setSdClientConfig(config) is instance
        assert instance.getSdClientConfig() is config

        instance.setSdClientConfig(None)
        assert instance.getSdClientConfig() is config

    def test_get_set_sdClientTimerConfigRef(self):
        """Test get/set sdClientTimerConfigRef with chaining and None no-op."""
        instance = self._instance()
        ref = _ref("/SomeipSdTimingConfigs/InstanceTiming1")

        assert instance.setSdClientTimerConfigRef(ref) is instance
        assert instance.getSdClientTimerConfigRef() is ref

        instance.setSdClientTimerConfigRef(None)
        assert instance.getSdClientTimerConfigRef() is ref

    def test_get_set_serviceIdentifier(self):
        """Test get/set serviceIdentifier with chaining and None no-op."""
        instance = self._instance()

        assert instance.setServiceIdentifier(PositiveInteger().setValue("50")) is instance
        assert instance.getServiceIdentifier().getValue() == 50

        instance.setServiceIdentifier(None)
        assert instance.getServiceIdentifier().getValue() == 50

    def test_get_set_versionDrivenFindBehavior(self):
        """Test get/set versionDrivenFindBehavior with chaining and None no-op."""
        instance = self._instance()
        value = ARLiteral()
        value.setValue("minimumMinorVersion")

        assert instance.setVersionDrivenFindBehavior(value) is instance
        assert instance.getVersionDrivenFindBehavior() is value
        assert instance.getVersionDrivenFindBehavior().getValue() == "minimumMinorVersion"

        instance.setVersionDrivenFindBehavior(None)
        assert instance.getVersionDrivenFindBehavior() is value


class TestAbstractServiceInstance:
    class ConcreteServiceInstance(AbstractServiceInstance):
        def __init__(self, parent, short_name):
            super().__init__(parent, short_name)

    def _instance(self):
        return self.ConcreteServiceInstance(MockParent(), "asi")

    def test_abstract_instantiation_blocked(self):
        """Test AbstractServiceInstance cannot be instantiated directly."""
        with pytest.raises(TypeError):
            AbstractServiceInstance(MockParent(), "asi")

    def test_initialization(self):
        """Test __init__ defaults for all fields (Table 6.158)."""
        instance = self._instance()

        assert isinstance(instance, Identifiable)
        assert instance.getShortName() == "asi"
        assert instance.getCapabilityRecords() == []
        assert instance.getMajorVersion() is None
        assert instance.getMethodActivationRoutingGroup() is None
        assert instance.getRoutingGroupRefs() == []

    def test_add_get_capabilityRecords(self):
        """Test add/get capabilityRecords append order and None no-op."""
        instance = self._instance()
        tag1 = TagWithOptionalValue()
        tag1.setKey(String().setValue("service"))
        tag2 = TagWithOptionalValue()
        tag2.setKey(String().setValue("config"))

        assert instance.addCapabilityRecord(tag1) is instance
        instance.addCapabilityRecord(tag2)
        assert instance.getCapabilityRecords() == [tag1, tag2]
        assert instance.getCapabilityRecords()[0].getKey().getValue() == "service"

        instance.addCapabilityRecord(None)
        assert instance.getCapabilityRecords() == [tag1, tag2]

    def test_get_set_majorVersion(self):
        """Test get/set majorVersion with chaining and None no-op."""
        instance = self._instance()
        value = PositiveInteger().setValue("33")

        assert instance.setMajorVersion(value) is instance
        assert instance.getMajorVersion() is value
        assert instance.getMajorVersion().getValue() == 33

        instance.setMajorVersion(None)
        assert instance.getMajorVersion() is value

    def test_get_set_methodActivationRoutingGroup(self):
        """Test get/set methodActivationRoutingGroup with chaining and None no-op (placeholder type)."""
        instance = self._instance()
        value = MockParent()

        assert instance.setMethodActivationRoutingGroup(value) is instance
        assert instance.getMethodActivationRoutingGroup() is value

        instance.setMethodActivationRoutingGroup(None)
        assert instance.getMethodActivationRoutingGroup() is value

    def test_add_get_routingGroupRefs(self):
        """Test add/get routingGroupRefs append order and None no-op."""
        instance = self._instance()
        ref1 = _ref("/Ether/RoutingGroup/RG1")
        ref2 = _ref("/Ether/RoutingGroup/RG2")

        assert instance.addRoutingGroupRef(ref1) is instance
        instance.addRoutingGroupRef(ref2)
        assert instance.getRoutingGroupRefs() == [ref1, ref2]
        assert instance.getRoutingGroupRefs()[0].getValue() == "/Ether/RoutingGroup/RG1"

        instance.addRoutingGroupRef(None)
        assert instance.getRoutingGroupRefs() == [ref1, ref2]


class TestApplicationEndpoint:
    def _endpoint(self):
        return ApplicationEndpoint(MockParent(), "aep")

    def test_initialization(self):
        """Test __init__ defaults for all fields (Table 6.124)."""
        endpoint = self._endpoint()

        assert isinstance(endpoint, Identifiable)
        assert endpoint.getShortName() == "aep"
        assert endpoint.getConsumedServiceInstances() == []
        assert endpoint.getMaxNumberOfConnections() is None
        assert endpoint.getNetworkEndpointRef() is None
        assert endpoint.getPriority() is None
        assert endpoint.getProvidedServiceInstances() == []
        assert endpoint.getTlsCryptoMappingRef() is None
        assert endpoint.getTpConfiguration() is None

    def test_create_get_consumedServiceInstances(self):
        """Test create/get consumedServiceInstance append and duplicate returns existing."""
        endpoint = self._endpoint()
        instance = endpoint.createConsumedServiceInstance("CSI1")

        assert isinstance(instance, ConsumedServiceInstance)
        assert endpoint.createConsumedServiceInstance("CSI1") is instance
        assert len(endpoint.getConsumedServiceInstances()) == 1
        assert endpoint.getConsumedServiceInstances()[0].getShortName() == "CSI1"

    def test_get_set_maxNumberOfConnections(self):
        """Test get/set maxNumberOfConnections with chaining and None no-op."""
        endpoint = self._endpoint()
        value = PositiveInteger().setValue("10")

        assert endpoint.setMaxNumberOfConnections(value) is endpoint
        assert endpoint.getMaxNumberOfConnections() is value
        assert endpoint.getMaxNumberOfConnections().getValue() == 10

        endpoint.setMaxNumberOfConnections(None)
        assert endpoint.getMaxNumberOfConnections() is value

    def test_get_set_networkEndpointRef(self):
        """Test get/set networkEndpointRef with chaining and None no-op."""
        endpoint = self._endpoint()
        value = _ref("/Ether/NetworkEndpoint/NE1")

        assert endpoint.setNetworkEndpointRef(value) is endpoint
        assert endpoint.getNetworkEndpointRef() is value
        assert endpoint.getNetworkEndpointRef().getValue() == "/Ether/NetworkEndpoint/NE1"

        endpoint.setNetworkEndpointRef(None)
        assert endpoint.getNetworkEndpointRef() is value

    def test_get_set_priority(self):
        """Test get/set priority with chaining and None no-op."""
        endpoint = self._endpoint()
        value = PositiveInteger().setValue("4")

        assert endpoint.setPriority(value) is endpoint
        assert endpoint.getPriority() is value
        assert endpoint.getPriority().getValue() == 4

        endpoint.setPriority(None)
        assert endpoint.getPriority() is value

    def test_create_get_providedServiceInstances(self):
        """Test create/get providedServiceInstance append and duplicate returns existing."""
        endpoint = self._endpoint()
        instance = endpoint.createProvidedServiceInstance("PSI1")

        assert isinstance(instance, ProvidedServiceInstance)
        assert endpoint.createProvidedServiceInstance("PSI1") is instance
        assert len(endpoint.getProvidedServiceInstances()) == 1
        assert endpoint.getProvidedServiceInstances()[0].getShortName() == "PSI1"

    def test_get_set_tlsCryptoMappingRef(self):
        """Test get/set tlsCryptoMappingRef with chaining and None no-op."""
        endpoint = self._endpoint()
        value = _ref("/Ether/TlsCryptoServiceMapping/TCSM1")

        assert endpoint.setTlsCryptoMappingRef(value) is endpoint
        assert endpoint.getTlsCryptoMappingRef() is value
        assert endpoint.getTlsCryptoMappingRef().getValue() == "/Ether/TlsCryptoServiceMapping/TCSM1"

        endpoint.setTlsCryptoMappingRef(None)
        assert endpoint.getTlsCryptoMappingRef() is value

    def test_get_set_tpConfiguration(self):
        """Test get/set tpConfiguration with chaining and None no-op."""
        endpoint = self._endpoint()
        value = GenericTp()

        assert endpoint.setTpConfiguration(value) is endpoint
        assert endpoint.getTpConfiguration() is value

        endpoint.setTpConfiguration(None)
        assert endpoint.getTpConfiguration() is value


class TestSocketAddress:
    def _address(self):
        return SocketAddress(MockParent(), "sa")

    def test_initialization(self):
        """Test __init__ defaults for all fields (Table 6.118)."""
        address = self._address()

        assert isinstance(address, Identifiable)
        assert address.getShortName() == "sa"
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
        assert address.getStaticSocketConnections() == []
        assert address.getUdpChecksumHandling() is None
        assert not hasattr(address, "portAddress")

    def test_get_set_allowedIPv6ExtHeadersRef(self):
        """Test get/set allowedIPv6ExtHeadersRef with chaining and None no-op."""
        address = self._address()
        value = _ref("/Ether/TcpOptionFilterSet/IPV6List1")

        assert address.setAllowedIPv6ExtHeadersRef(value) is address
        assert address.getAllowedIPv6ExtHeadersRef() is value

        address.setAllowedIPv6ExtHeadersRef(None)
        assert address.getAllowedIPv6ExtHeadersRef() is value

    def test_get_set_allowedTcpOptionsRef(self):
        """Test get/set allowedTcpOptionsRef with chaining and None no-op."""
        address = self._address()
        value = _ref("/Ether/TcpOptionFilterSet/TcpList1")

        assert address.setAllowedTcpOptionsRef(value) is address
        assert address.getAllowedTcpOptionsRef() is value

        address.setAllowedTcpOptionsRef(None)
        assert address.getAllowedTcpOptionsRef() is value

    def test_create_get_applicationEndpoint(self):
        """Test create/get applicationEndpoint append and duplicate returns existing."""
        address = self._address()
        end_point = address.createApplicationEndpoint("AEP1")

        assert isinstance(end_point, ApplicationEndpoint)
        assert address.createApplicationEndpoint("AEP1") is end_point
        assert address.getApplicationEndpoint() is end_point
        assert end_point.getShortName() == "AEP1"

    def test_get_set_connectorRef(self):
        """Test get/set connectorRef with chaining and None no-op."""
        address = self._address()
        value = _ref("/Ether/Ecu1/Connector1")

        assert address.setConnectorRef(value) is address
        assert address.getConnectorRef() is value

        address.setConnectorRef(None)
        assert address.getConnectorRef() is value

    def test_get_set_differentiatedServiceField(self):
        """Test get/set differentiatedServiceField with chaining and None no-op."""
        address = self._address()
        value = PositiveInteger().setValue("0")

        assert address.setDifferentiatedServiceField(value) is address
        assert address.getDifferentiatedServiceField() is value
        assert address.getDifferentiatedServiceField().getValue() == 0

        address.setDifferentiatedServiceField(None)
        assert address.getDifferentiatedServiceField() is value

    def test_get_set_flowLabel(self):
        """Test get/set flowLabel with chaining and None no-op."""
        address = self._address()
        value = PositiveInteger().setValue("1048575")

        assert address.setFlowLabel(value) is address
        assert address.getFlowLabel() is value
        assert address.getFlowLabel().getValue() == 1048575

        address.setFlowLabel(None)
        assert address.getFlowLabel() is value

    def test_add_get_multicastConnectorRefs(self):
        """Test add/get multicastConnectorRefs append, chaining and None no-op."""
        address = self._address()
        ref1 = _ref("/Ether/Ecu2/Connector2")
        ref2 = _ref("/Ether/Ecu3/Connector3")

        assert address.addMulticastConnectorRef(ref1) is address
        assert address.addMulticastConnectorRef(ref2) is address
        assert address.getMulticastConnectorRefs() == [ref1, ref2]

        address.addMulticastConnectorRef(None)
        assert address.getMulticastConnectorRefs() == [ref1, ref2]

    def test_get_set_pathMtuDiscoveryEnabled(self):
        """Test get/set pathMtuDiscoveryEnabled with chaining and None no-op."""
        address = self._address()
        value = Boolean().setValue("true")

        assert address.setPathMtuDiscoveryEnabled(value) is address
        assert address.getPathMtuDiscoveryEnabled() is value
        assert address.getPathMtuDiscoveryEnabled().getValue() is True

        address.setPathMtuDiscoveryEnabled(None)
        assert address.getPathMtuDiscoveryEnabled() is value

    def test_get_set_pduCollectionMaxBufferSize(self):
        """Test get/set pduCollectionMaxBufferSize with chaining and None no-op."""
        address = self._address()
        value = PositiveInteger().setValue("2048")

        assert address.setPduCollectionMaxBufferSize(value) is address
        assert address.getPduCollectionMaxBufferSize() is value
        assert address.getPduCollectionMaxBufferSize().getValue() == 2048

        address.setPduCollectionMaxBufferSize(None)
        assert address.getPduCollectionMaxBufferSize() is value

    def test_get_set_pduCollectionTimeout(self):
        """Test get/set pduCollectionTimeout with chaining and None no-op."""
        address = self._address()
        value = TimeValue().setValue("0.005")

        assert address.setPduCollectionTimeout(value) is address
        assert address.getPduCollectionTimeout() is value
        assert address.getPduCollectionTimeout().getValue() == 0.005

        address.setPduCollectionTimeout(None)
        assert address.getPduCollectionTimeout() is value

    def test_add_get_staticSocketConnections(self):
        """Test add/get staticSocketConnections (placeholder child type) and None no-op."""
        address = self._address()
        connection1 = MockParent()
        connection2 = MockParent()

        assert address.addStaticSocketConnection(connection1) is address
        assert address.addStaticSocketConnection(connection2) is address
        assert address.getStaticSocketConnections() == [connection1, connection2]

        address.addStaticSocketConnection(None)
        assert address.getStaticSocketConnections() == [connection1, connection2]

    def test_get_set_udpChecksumHandling(self):
        """Test get/set udpChecksumHandling with chaining and None no-op."""
        address = self._address()
        value = ARLiteral()

        assert address.setUdpChecksumHandling(value) is address
        assert address.getUdpChecksumHandling() is value

        address.setUdpChecksumHandling(None)
        assert address.getUdpChecksumHandling() is value


class TestServiceVersionAcceptanceKindEnum:
    """
    Test cases for ServiceVersionAcceptanceKindEnum (Table F.113).
    """

    def test_member_presence_and_values(self):
        """
        Test that both spec literals exist with their index order.
        """
        assert ServiceVersionAcceptanceKindEnum.EXACT_OR_ANY_MINOR_VERSION == "exactOrAnyMinorVersion"
        assert ServiceVersionAcceptanceKindEnum.MINIMUM_MINOR_VERSION == "minimumMinorVersion"
        assert list(ServiceVersionAcceptanceKindEnum().getEnumValues()) == [
            "exactOrAnyMinorVersion",
            "minimumMinorVersion",
        ]

    def test_instantiability(self):
        """
        Test instantiability and setValue with an enum member.
        """
        enum = ServiceVersionAcceptanceKindEnum()
        result = enum.setValue(ServiceVersionAcceptanceKindEnum.MINIMUM_MINOR_VERSION)
        assert result == enum  # method chaining
        assert enum.getValue() == "minimumMinorVersion"


class TestPduActivationRoutingGroup:
    """
    Test cases for PduActivationRoutingGroup (Table 6.161).
    """

    def test_initialization(self):
        """
        Test initialization and Identifiable base.
        """
        parent = MockParent()
        group = PduActivationRoutingGroup(parent, "Group1")

        assert isinstance(group, Identifiable)
        assert group.getShortName() == "Group1"
        assert group.getEventGroupControlType() is None
        assert group.getIPduIdentifierTcpRefs() == []
        assert group.getIPduIdentifierUdpRefs() == []

    def test_event_group_control_type(self):
        """
        Test eventGroupControlType round-trip and None no-op.
        """
        parent = MockParent()
        group = PduActivationRoutingGroup(parent, "Group1")
        control_type = ARLiteral().setValue("activateAndTriggerUnicast")

        result = group.setEventGroupControlType(control_type)
        assert group.getEventGroupControlType() is control_type
        assert result == group  # method chaining

        # None no-op
        result = group.setEventGroupControlType(None)
        assert group.getEventGroupControlType() is control_type

    def test_ipdu_identifier_refs(self):
        """
        Test iPduIdentifierTcp/Udp ref lists, append semantics and None no-op.
        """
        parent = MockParent()
        group = PduActivationRoutingGroup(parent, "Group1")
        ref_tcp = RefType()
        ref_udp = RefType()

        result = group.addIPduIdentifierTcpRef(ref_tcp)
        assert group.getIPduIdentifierTcpRefs() == [ref_tcp]
        assert result == group  # method chaining

        group.addIPduIdentifierTcpRef(None)
        assert group.getIPduIdentifierTcpRefs() == [ref_tcp]

        result = group.addIPduIdentifierUdpRef(ref_udp)
        assert group.getIPduIdentifierUdpRefs() == [ref_udp]
        assert result == group  # method chaining

        group.addIPduIdentifierUdpRef(None)
        assert group.getIPduIdentifierUdpRefs() == [ref_udp]


class TestStaticSocketConnection:
    """
    Test cases for StaticSocketConnection (Table 6.201).
    """

    def test_initialization(self):
        """
        Test initialization and Identifiable base.
        """
        parent = MockParent()
        connection = StaticSocketConnection(parent, "Conn1")

        assert isinstance(connection, Identifiable)
        assert connection.getShortName() == "Conn1"
        assert connection.getIPduIdentifierRefs() == []
        assert connection.getRemoteAddressRef() is None
        assert connection.getTcpConnectTimeout() is None
        assert connection.getTcpRole() is None

    def test_ipdu_identifier_refs(self):
        """
        Test iPduIdentifier ref list append semantics and None no-op.
        """
        parent = MockParent()
        connection = StaticSocketConnection(parent, "Conn1")
        ref = RefType()

        result = connection.addIPduIdentifierRef(ref)
        assert connection.getIPduIdentifierRefs() == [ref]
        assert result == connection  # method chaining

        connection.addIPduIdentifierRef(None)
        assert connection.getIPduIdentifierRefs() == [ref]

    def test_remote_address_ref(self):
        """
        Test remoteAddressRef round-trip and None no-op.
        """
        parent = MockParent()
        connection = StaticSocketConnection(parent, "Conn1")
        ref = RefType()
        ref.setValue("/Ecu/SoAd/SocketAddress/Remote")

        result = connection.setRemoteAddressRef(ref)
        assert connection.getRemoteAddressRef() is ref
        assert result == connection  # method chaining

        # None no-op
        result = connection.setRemoteAddressRef(None)
        assert connection.getRemoteAddressRef() is ref

    def test_tcp_connect_timeout(self):
        """
        Test tcpConnectTimeout round-trip and None no-op.
        """
        parent = MockParent()
        connection = StaticSocketConnection(parent, "Conn1")
        timeout = TimeValue().setValue(30)

        result = connection.setTcpConnectTimeout(timeout)
        assert connection.getTcpConnectTimeout() is timeout
        assert result == connection  # method chaining

        # None no-op
        result = connection.setTcpConnectTimeout(None)
        assert connection.getTcpConnectTimeout() is timeout

    def test_tcp_role(self):
        """
        Test tcpRole round-trip and None no-op.
        """
        parent = MockParent()
        connection = StaticSocketConnection(parent, "Conn1")
        role = ARLiteral().setValue("connect")

        result = connection.setTcpRole(role)
        assert connection.getTcpRole() is role
        assert result == connection  # method chaining

        # None no-op
        result = connection.setTcpRole(None)
        assert connection.getTcpRole() is role


class TestUdpChecksumCalculationEnum:
    """
    Test cases for UdpChecksumCalculationEnum (Table 6.119).
    """

    def test_member_presence_and_values(self):
        """
        Test that both spec literals exist with their index order.
        """
        assert UdpChecksumCalculationEnum.UDP_CHECKSUM_ENABLED == "udpChecksumEnabled"
        assert UdpChecksumCalculationEnum.UDP_CHECKSUM_DISABLED == "udpChecksumDisabled"
        assert list(UdpChecksumCalculationEnum().getEnumValues()) == [
            "udpChecksumEnabled",
            "udpChecksumDisabled",
        ]

    def test_instantiability(self):
        """
        Test instantiability and setValue with an enum member.
        """
        enum = UdpChecksumCalculationEnum()
        result = enum.setValue(UdpChecksumCalculationEnum.UDP_CHECKSUM_DISABLED)
        assert result == enum  # method chaining
        assert enum.getValue() == "udpChecksumDisabled"


class TestEventHandler:
    """
    Test cases for EventHandler (Table 6.166).
    """

    def _new_handler(self):
        return EventHandler(MockParent(), "EH1")

    def test_initialization(self):
        """
        Test initialization and defaults.
        """
        handler = self._new_handler()

        assert isinstance(handler, Identifiable)
        assert handler.getShortName() == "EH1"
        assert handler.getConsumedEventGroupRefs() == []
        assert handler.getEventGroupIdentifier() is None
        assert handler.getEventMulticastAddressRef() is None
        assert handler.getMulticastThreshold() is None
        assert handler.getPduActivationRoutingGroups() == []
        assert handler.getRoutingGroupRefs() == []
        assert handler.getSdServerConfig() is None
        assert handler.getSdServerEgTimingConfigRef() is None

    def test_event_group_identifier(self):
        """
        Test eventGroupIdentifier round-trip and None no-op.
        """
        handler = self._new_handler()
        identifier = PositiveInteger().setValue(7)

        result = handler.setEventGroupIdentifier(identifier)
        assert handler.getEventGroupIdentifier() == identifier
        assert result == handler  # method chaining

        # None no-op
        result = handler.setEventGroupIdentifier(None)
        assert handler.getEventGroupIdentifier() == identifier

    def test_event_multicast_address_ref(self):
        """
        Test eventMulticastAddressRef round-trip and None no-op.
        """
        handler = self._new_handler()
        ref = RefType()
        ref.setValue("/Ether/ApplicationEndpoint/MC1")

        result = handler.setEventMulticastAddressRef(ref)
        assert handler.getEventMulticastAddressRef() is ref
        assert result == handler  # method chaining

        # None no-op
        result = handler.setEventMulticastAddressRef(None)
        assert handler.getEventMulticastAddressRef() is ref

    def test_pdu_activation_routing_groups(self):
        """
        Test pduActivationRoutingGroups append semantics and None no-op.
        """
        handler = self._new_handler()
        group = PduActivationRoutingGroup(MockParent(), "PARG1")

        result = handler.addPduActivationRoutingGroup(group)
        assert handler.getPduActivationRoutingGroups() == [group]
        assert result == handler  # method chaining

        handler.addPduActivationRoutingGroup(None)
        assert handler.getPduActivationRoutingGroups() == [group]

    def test_sd_server_eg_timing_config_ref(self):
        """
        Test sdServerEgTimingConfigRef round-trip and None no-op.
        """
        handler = self._new_handler()
        ref = RefType()
        ref.setValue("/SomeipSdTimingConfigs/ServerTiming1")

        result = handler.setSdServerEgTimingConfigRef(ref)
        assert handler.getSdServerEgTimingConfigRef() is ref
        assert result == handler  # method chaining

        # None no-op
        result = handler.setSdServerEgTimingConfigRef(None)
        assert handler.getSdServerEgTimingConfigRef() is ref

    def test_application_endpoint_ref_removed(self):
        """
        applicationEndpoint is atp.Status=removed since 4.4.0 and absent from Table 6.166 (Rule 0015).
        """
        handler = self._new_handler()
        assert not hasattr(handler, "applicationEndpointRef")
