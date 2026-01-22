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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import SocketConnectionBundle
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


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

    def test_AbstractServiceInstance(self):
        """Test AbstractServiceInstance abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(TypeError):
            AbstractServiceInstance(parent, "test_abstract_service_instance")

    def test_AbstractServiceInstance_methods(self):
        """Test AbstractServiceInstance concrete implementation methods."""
        class ConcreteServiceInstance(AbstractServiceInstance):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = MockParent()
        instance = ConcreteServiceInstance(parent, "test_concrete_service_instance")

        # Test default values
        assert instance.getCapabilityRecords() == []
        assert instance.getMajorVersion() is None
        assert instance.getMethodActivationRoutingGroup() is None
        assert instance.getRoutingGroupRefs() == []

        # Test addCapabilityRecord method with None value (this should not add anything)
        instance.addCapabilityRecord(None)
        assert instance.getCapabilityRecords() == []  # Should remain empty
        assert instance == instance.addCapabilityRecord(None)  # Test method chaining

        # Test addCapabilityRecord method with actual value
        instance.addCapabilityRecord("capability1")
        assert "capability1" in instance.getCapabilityRecords()
        assert instance == instance.addCapabilityRecord("capability2")  # Test method chaining
        assert len(instance.getCapabilityRecords()) == 2

        # Test setMajorVersion with None
        instance.setMajorVersion(None)
        assert instance.getMajorVersion() is None  # Should remain None
        assert instance == instance.setMajorVersion(None)  # Test method chaining

        # Test setMajorVersion with actual value
        instance.setMajorVersion(2)
        assert instance.getMajorVersion() == 2
        assert instance == instance.setMajorVersion(2)  # Test method chaining

        # Test other methods
        instance.setMethodActivationRoutingGroup("routing_group")
        assert instance.getMethodActivationRoutingGroup() == "routing_group"
        assert instance == instance.setMethodActivationRoutingGroup("routing_group")  # Test method chaining

        instance.addRoutingGroupRef("routing_ref")
        assert "routing_ref" in instance.getRoutingGroupRefs()
        assert instance == instance.addRoutingGroupRef("routing_ref")  # Test method chaining

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

        # Test setter/getter methods with method chaining - with None
        assert group == group.setApplicationEndpointRef(None)  # Test method chaining with None
        assert group.getApplicationEndpointRef() is None  # Should remain None

        assert group == group.setAutoRequire(None)  # Test method chaining with None
        assert group.getAutoRequire() is None  # Should remain None

        assert group == group.setEventGroupIdentifier(None)  # Test method chaining with None
        assert group.getEventGroupIdentifier() is None  # Should remain None

        assert group == group.setPriority(None)  # Test method chaining with None
        assert group.getPriority() is None  # Should remain None

        assert group == group.setSdClientConfig(None)  # Test method chaining with None
        assert group.getSdClientConfig() is None  # Should remain None

        assert group == group.setSdClientTimerConfigRef(None)  # Test method chaining with None
        assert group.getSdClientTimerConfigRef() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        group.setApplicationEndpointRef("app_endpoint_ref")
        assert group.getApplicationEndpointRef() == "app_endpoint_ref"
        assert group == group.setApplicationEndpointRef("app_endpoint_ref")  # Test method chaining

        group.setAutoRequire(True)
        assert group.getAutoRequire() is True
        assert group == group.setAutoRequire(True)  # Test method chaining

        group.setEventGroupIdentifier(10)
        assert group.getEventGroupIdentifier() == 10
        assert group == group.setEventGroupIdentifier(10)  # Test method chaining

        group.setPriority(5)
        assert group.getPriority() == 5
        assert group == group.setPriority(5)  # Test method chaining

        config = object()
        group.setSdClientConfig(config)
        assert group.getSdClientConfig() == config
        assert group == group.setSdClientConfig(config)  # Test method chaining

        group.setSdClientTimerConfigRef("timer_config_ref")
        assert group.getSdClientTimerConfigRef() == "timer_config_ref"
        assert group == group.setSdClientTimerConfigRef("timer_config_ref")  # Test method chaining

        # Test add methods
        group.addEventMulticastAddressRef("multicast_ref1")
        assert "multicast_ref1" in group.getEventMulticastAddressRefs()
        assert group == group.addEventMulticastAddressRef("multicast_ref1")  # Test method chaining

        group.addRoutingGroupRef("routing_ref1")
        assert "routing_ref1" in group.getRoutingGroupRefs()
        assert group == group.addRoutingGroupRef("routing_ref1")  # Test method chaining

        group.setPduActivationRoutingGroups(["pdu_routing_group"])
        assert "pdu_routing_group" in group.getPduActivationRoutingGroups()
        assert group == group.setPduActivationRoutingGroups(["pdu_routing_group"])  # Test method chaining

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

        # Test setter/getter methods with method chaining - with None
        assert instance == instance.setAutoRequire(None)  # Test method chaining with None
        assert instance.getAutoRequire() is None  # Should remain None

        assert instance == instance.setBlocklistedVersions(None)  # Test method chaining with None
        assert instance.getBlocklistedVersions() == []  # Should remain empty

        assert instance == instance.setEventMulticastSubscriptionAddressRef(None)  # Test method chaining with None
        assert instance.getEventMulticastSubscriptionAddressRef() is None  # Should remain None

        assert instance == instance.setInstanceIdentifier(None)  # Test method chaining with None
        assert instance.getInstanceIdentifier() is None  # Should remain None

        assert instance == instance.setMinorVersion(None)  # Test method chaining with None
        assert instance.getMinorVersion() is None  # Should remain None

        assert instance == instance.setProvidedServiceInstanceRef(None)  # Test method chaining with None
        assert instance.getProvidedServiceInstanceRef() is None  # Should remain None

        assert instance == instance.setSdClientConfig(None)  # Test method chaining with None
        assert instance.getSdClientConfig() is None  # Should remain None

        assert instance == instance.setSdClientTimerConfigRef(None)  # Test method chaining with None
        assert instance.getSdClientTimerConfigRef() is None  # Should remain None

        assert instance == instance.setVersionDrivenFindBehavior(None)  # Test method chaining with None
        assert instance.getVersionDrivenFindBehavior() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        instance.setAutoRequire(True)
        assert instance.getAutoRequire() is True
        assert instance == instance.setAutoRequire(True)  # Test method chaining

        instance.setBlocklistedVersions(["v1.0", "v1.1"])
        assert "v1.0" in instance.getBlocklistedVersions()
        assert instance == instance.setBlocklistedVersions(["v1.0", "v1.1"])  # Test method chaining

        instance.setEventMulticastSubscriptionAddressRef("multicast_sub_ref")
        assert instance.getEventMulticastSubscriptionAddressRef() == "multicast_sub_ref"
        assert instance == instance.setEventMulticastSubscriptionAddressRef("multicast_sub_ref")  # Test method chaining

        instance.setInstanceIdentifier(100)
        assert instance.getInstanceIdentifier() == 100
        assert instance == instance.setInstanceIdentifier(100)  # Test method chaining

        instance.setMinorVersion("2.1")
        assert instance.getMinorVersion() == "2.1"
        assert instance == instance.setMinorVersion("2.1")  # Test method chaining

        instance.setProvidedServiceInstanceRef("provider_ref")
        assert instance.getProvidedServiceInstanceRef() == "provider_ref"
        assert instance == instance.setProvidedServiceInstanceRef("provider_ref")  # Test method chaining

        instance.setSdClientConfig("sd_client_config")
        assert instance.getSdClientConfig() == "sd_client_config"
        assert instance == instance.setSdClientConfig("sd_client_config")  # Test method chaining

        instance.setSdClientTimerConfigRef("timer_ref")
        assert instance.getSdClientTimerConfigRef() == "timer_ref"
        assert instance == instance.setSdClientTimerConfigRef("timer_ref")  # Test method chaining

        instance.setVersionDrivenFindBehavior("find_behavior")
        assert instance.getVersionDrivenFindBehavior() == "find_behavior"
        assert instance == instance.setVersionDrivenFindBehavior("find_behavior")  # Test method chaining

        instance.setServiceIdentifier(50)
        assert instance.getServiceIdentifier() == 50
        assert instance == instance.setServiceIdentifier(50)  # Test method chaining

        # Test add methods
        instance.setAllowedServiceProviderRefs(["provider1", "provider2"])
        assert "provider1" in instance.getAllowedServiceProviderRefs()
        assert instance == instance.setAllowedServiceProviderRefs(["provider1", "provider2"])  # Test method chaining

        instance.setLocalUnicastAddressRefs(["local1", "local2"])
        assert "local1" in instance.getLocalUnicastAddressRefs()
        assert instance == instance.setLocalUnicastAddressRefs(["local1", "local2"])  # Test method chaining

        instance.setRemoteUnicastAddressRefs(["remote1", "remote2"])
        assert "remote1" in instance.getRemoteUnicastAddressRefs()
        assert instance == instance.setRemoteUnicastAddressRefs(["remote1", "remote2"])  # Test method chaining

        # Test create method for consumed event groups
        event_group = instance.createConsumedEventGroup("test_event_group")
        assert isinstance(event_group, ConsumedEventGroup)
        assert len(instance.getConsumedEventGroups()) == 1

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

        # Test setter/getter methods with method chaining - with None
        assert handler == handler.setApplicationEndpointRef(None)  # Test method chaining with None
        assert handler.getApplicationEndpointRef() is None  # Should remain None

        assert handler == handler.setMulticastThreshold(None)  # Test method chaining with None
        assert handler.getMulticastThreshold() is None  # Should remain None

        assert handler == handler.setSdServerConfig(None)  # Test method chaining with None
        assert handler.getSdServerConfig() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        handler.setApplicationEndpointRef("app_endpoint_ref")
        assert handler.getApplicationEndpointRef() == "app_endpoint_ref"
        assert handler == handler.setApplicationEndpointRef("app_endpoint_ref")  # Test method chaining

        handler.setMulticastThreshold(10)
        assert handler.getMulticastThreshold() == 10
        assert handler == handler.setMulticastThreshold(10)  # Test method chaining

        config = object()
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
        assert instance.getPriority() is None
        assert instance.getSdServerConfig() is None
        assert instance.getServiceIdentifier() is None

        # Test setter/getter methods with method chaining - with None
        assert instance == instance.setInstanceIdentifier(None)  # Test method chaining with None
        assert instance.getInstanceIdentifier() is None  # Should remain None

        assert instance == instance.setPriority(None)  # Test method chaining with None
        assert instance.getPriority() is None  # Should remain None

        assert instance == instance.setSdServerConfig(None)  # Test method chaining with None
        assert instance.getSdServerConfig() is None  # Should remain None

        assert instance == instance.setServiceIdentifier(None)  # Test method chaining with None
        assert instance.getServiceIdentifier() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        instance.setInstanceIdentifier(200)
        assert instance.getInstanceIdentifier() == 200
        assert instance == instance.setInstanceIdentifier(200)  # Test method chaining

        instance.setPriority(3)
        assert instance.getPriority() == 3
        assert instance == instance.setPriority(3)  # Test method chaining

        config = object()
        instance.setSdServerConfig(config)
        assert instance.getSdServerConfig() == config
        assert instance == instance.setSdServerConfig(config)  # Test method chaining

        instance.setServiceIdentifier(25)
        assert instance.getServiceIdentifier() == 25
        assert instance == instance.setServiceIdentifier(25)  # Test method chaining

        # Test create method for event handlers
        event_handler = instance.createEventHandler("test_event_handler")
        assert isinstance(event_handler, EventHandler)
        assert len(instance.getEventHandlers()) == 1

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
        assert address.getPortAddress() is None
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

        assert address == address.setPortAddress(None)  # Test method chaining with None
        assert address.getPortAddress() is None  # Should remain None

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

        address.setPortAddress(8080)
        assert address.getPortAddress() == 8080
        assert address == address.setPortAddress(8080)  # Test method chaining

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
        """Test SoAdConfig class functionality."""
        config = SoAdConfig()

        assert isinstance(config, ARObject)
        
        # Test default values
        assert config.getConnections() == []
        assert config.getConnectionBundles() == []
        assert config.getSocketAddresses() == []

        # Test setter/getter methods with method chaining
        config.setConnections(["connection1", "connection2"])
        assert "connection1" in config.getConnections()
        assert config == config.setConnections(["connection1", "connection2"])  # Test method chaining

        config.setConnectionBundles(["bundle1", "bundle2"])
        assert "bundle1" in config.getConnectionBundles()
        assert config == config.setConnectionBundles(["bundle1", "bundle2"])  # Test method chaining

        # Test create method for socket connection bundle - this should add to the existing list
        bundle = config.createSocketConnectionBundle("test_bundle")
        assert isinstance(bundle, SocketConnectionBundle)
        assert len(config.getConnectionBundles()) == 3  # 2 from setConnectionBundles + 1 from createSocketConnectionBundle

        # Create another config to test just the create method
        config2 = SoAdConfig()
        bundle2 = config2.createSocketConnectionBundle("test_bundle2")
        assert isinstance(bundle2, SocketConnectionBundle)
        assert len(config2.getConnectionBundles()) == 1

        # Test createSocketAddress method
        config3 = SoAdConfig()
        socket_addr = config3.createSocketAddress("test_socket_addr")
        assert isinstance(socket_addr, SocketAddress)
        assert len(config3.getSocketAddresses()) == 1