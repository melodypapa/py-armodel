import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import (
    NetworkEndpointAddress,
    Ipv4Configuration,
    Ipv6Configuration,
    DoIpEntity,
    TimeSyncClientConfiguration,
    TimeSyncServerConfiguration,
    TimeSynchronization,
    InfrastructureServices,
    NetworkEndpoint
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_Fibex4EthernetNetworkEndpoint:
    """Test cases for Fibex4Ethernet NetworkEndpoint classes."""
    
    def test_NetworkEndpointAddress(self):
        """Test NetworkEndpointAddress abstract class instantiation."""
        with pytest.raises(TypeError):
            NetworkEndpointAddress()

    def test_Ipv4Configuration(self):
        """Test Ipv4Configuration class functionality."""
        config = Ipv4Configuration()

        assert isinstance(config, NetworkEndpointAddress)
        
        # Test default values
        assert config.getAssignmentPriority() is None
        assert config.getDefaultGateway() is None
        assert config.getDnsServerAddresses() == []
        assert config.getIpAddressKeepBehavior() is None
        assert config.getIpv4Address() is None
        assert config.getIpv4AddressSource() is None
        assert config.getNetworkMask() is None
        assert config.getTtl() is None
        
        # Test setter/getter methods with method chaining
        result = config.setAssignmentPriority(1)
        assert config.getAssignmentPriority() == 1
        assert result == config  # Test method chaining

        result = config.setDefaultGateway("192.168.1.254")
        assert config.getDefaultGateway() == "192.168.1.254"
        assert result == config  # Test method chaining

        result = config.setIpAddressKeepBehavior("keep")
        assert config.getIpAddressKeepBehavior() == "keep"
        assert result == config  # Test method chaining

        result = config.setIpv4Address("192.168.1.1")
        assert config.getIpv4Address() == "192.168.1.1"
        assert result == config  # Test method chaining

        result = config.setIpv4AddressSource("dhcp")
        assert config.getIpv4AddressSource() == "dhcp"
        assert result == config  # Test method chaining

        result = config.setNetworkMask("255.255.255.0")
        assert config.getNetworkMask() == "255.255.255.0"
        assert result == config  # Test method chaining

        result = config.setTtl(64)
        assert config.getTtl() == 64
        assert result == config  # Test method chaining

        # Test adding DNS server addresses with method chaining
        result = config.addDnsServerAddress("8.8.8.8")
        assert config.getDnsServerAddresses() == ["8.8.8.8"]
        assert result == config  # Test method chaining

        result = config.addDnsServerAddress("8.8.4.4")
        assert config.getDnsServerAddresses() == ["8.8.8.8", "8.8.4.4"]
        assert result == config  # Test method chaining

    def test_Ipv6Configuration(self):
        """Test Ipv6Configuration class functionality."""
        config = Ipv6Configuration()

        assert isinstance(config, NetworkEndpointAddress)
        
        # Test default values
        assert config.getAssignmentPriority() is None
        assert config.getDefaultRouter() is None
        assert config.getDnsServerAddresses() == []
        assert config.getEnableAnycast() is None
        assert config.getHopCount() is None
        assert config.getIpAddressKeepBehavior() is None
        assert config.getIpAddressPrefixLength() is None
        assert config.getIpv6Address() is None
        assert config.getIpv6AddressSource() is None
        
        # Test setter/getter methods with method chaining
        result = config.setAssignmentPriority(2)
        assert config.getAssignmentPriority() == 2
        assert result == config  # Test method chaining

        result = config.setDefaultRouter("2001:db8::1")
        assert config.getDefaultRouter() == "2001:db8::1"
        assert result == config  # Test method chaining

        result = config.setEnableAnycast(True)
        assert config.getEnableAnycast() is True
        assert result == config  # Test method chaining

        result = config.setHopCount(64)
        assert config.getHopCount() == 64
        assert result == config  # Test method chaining

        result = config.setIpAddressKeepBehavior("keep")
        assert config.getIpAddressKeepBehavior() == "keep"
        assert result == config  # Test method chaining

        result = config.setIpAddressPrefixLength(64)
        assert config.getIpAddressPrefixLength() == 64
        assert result == config  # Test method chaining

        result = config.setIpv6Address("2001:db8::1")
        assert config.getIpv6Address() == "2001:db8::1"
        assert result == config  # Test method chaining

        result = config.setIpv6AddressSource("auto")
        assert config.getIpv6AddressSource() == "auto"
        assert result == config  # Test method chaining

        # Test setting DNS server addresses with method chaining
        result = config.setDnsServerAddresses(["2001:4860:4860::8888", "2001:4860:4860::8844"])
        assert config.getDnsServerAddresses() == ["2001:4860:4860::8888", "2001:4860:4860::8844"]
        assert result == config  # Test method chaining

    def test_DoIpEntity(self):
        """Test DoIpEntity class functionality."""
        entity = DoIpEntity()

        assert isinstance(entity, ARObject)
        
        # Test default values
        assert entity.getDoIpEntityRole() is None
        
        # Test setter/getter methods with method chaining
        result = entity.setDoIpEntityRole("tester")
        assert entity.getDoIpEntityRole() == "tester"
        assert result == entity  # Test method chaining

    def test_TimeSyncClientConfiguration(self):
        """Test TimeSyncClientConfiguration class functionality."""
        config = TimeSyncClientConfiguration()

        assert isinstance(config, ARObject)
        
        # Test default values
        assert config.getOrderedMasters() == []
        assert config.getTimeSyncTechnology() is None
        
        # Test setter/getter methods with method chaining
        result = config.setTimeSyncTechnology("IEEE_1588")
        assert config.getTimeSyncTechnology() == "IEEE_1588"
        assert result == config  # Test method chaining

        # Test adding ordered masters with method chaining
        result = config.addOrderedMaster("master1")
        assert config.getOrderedMasters() == ["master1"]
        assert result == config  # Test method chaining

        result = config.addOrderedMaster("master2")
        assert config.getOrderedMasters() == ["master1", "master2"]
        assert result == config  # Test method chaining

    def test_TimeSyncServerConfiguration(self):
        """Test TimeSyncServerConfiguration class functionality."""
        config = TimeSyncServerConfiguration()

        assert isinstance(config, ARObject)
        
        # Test default values
        assert config.getPriority() is None
        assert config.getSyncInterval() is None
        assert config.getTimeSyncServerIdentifier() is None
        assert config.getTimeSyncTechnology() is None
        
        # Test setter/getter methods with method chaining
        result = config.setPriority(10)
        assert config.getPriority() == 10
        assert result == config  # Test method chaining

        result = config.setSyncInterval("100ms")
        assert config.getSyncInterval() == "100ms"
        assert result == config  # Test method chaining

        result = config.setTimeSyncServerIdentifier("server1")
        assert config.getTimeSyncServerIdentifier() == "server1"
        assert result == config  # Test method chaining

        result = config.setTimeSyncTechnology("IEEE_1588")
        assert config.getTimeSyncTechnology() == "IEEE_1588"
        assert result == config  # Test method chaining

    def test_TimeSynchronization(self):
        """Test TimeSynchronization class functionality."""
        sync = TimeSynchronization()

        assert isinstance(sync, ARObject)
        
        # Test default values
        assert sync.getTimeSyncClient() is None
        assert sync.getTimeSyncServer() is None
        
        # Test setter/getter methods with method chaining
        client_config = TimeSyncClientConfiguration()
        result = sync.setTimeSyncClient(client_config)
        assert sync.getTimeSyncClient() == client_config
        assert result == sync  # Test method chaining

        server_config = TimeSyncServerConfiguration()
        result = sync.setTimeSyncServer(server_config)
        assert sync.getTimeSyncServer() == server_config
        assert result == sync  # Test method chaining

    def test_InfrastructureServices(self):
        """Test InfrastructureServices class functionality."""
        services = InfrastructureServices()

        assert isinstance(services, ARObject)
        
        # Test default values
        assert services.getDoIpEntity() is None
        assert services.getTimeSynchronization() is None
        
        # Test setter/getter methods with method chaining
        doip_entity = DoIpEntity()
        result = services.setDoIpEntity(doip_entity)
        assert services.getDoIpEntity() == doip_entity
        assert result == services  # Test method chaining

        time_sync = TimeSynchronization()
        result = services.setTimeSynchronization(time_sync)
        assert services.getTimeSynchronization() == time_sync
        assert result == services  # Test method chaining

    def test_NetworkEndpoint(self):
        """Test NetworkEndpoint class functionality."""
        parent = MockParent()
        endpoint = NetworkEndpoint(parent, "test_network_endpoint")

        assert isinstance(endpoint, Identifiable)
        
        # Test default values
        assert endpoint.getFullyQualifiedDomainName() is None
        assert endpoint.getInfrastructureServices() is None
        assert endpoint.getIpSecConfig() is None
        assert endpoint.getNetworkEndpointAddresses() == []
        assert endpoint.getPriority() is None
        
        # Test setter/getter methods with method chaining
        result = endpoint.setFullyQualifiedDomainName("example.com")
        assert endpoint.getFullyQualifiedDomainName() == "example.com"
        assert result == endpoint  # Test method chaining

        result = endpoint.setInfrastructureServices(InfrastructureServices())
        assert isinstance(endpoint.getInfrastructureServices(), InfrastructureServices)
        assert result == endpoint  # Test method chaining

        result = endpoint.setIpSecConfig("ipsec_config")
        assert endpoint.getIpSecConfig() == "ipsec_config"
        assert result == endpoint  # Test method chaining

        result = endpoint.setPriority(5)
        assert endpoint.getPriority() == 5
        assert result == endpoint  # Test method chaining

        # Test adding network endpoint addresses with method chaining
        ipv4_config = Ipv4Configuration()
        result = endpoint.addNetworkEndpointAddress(ipv4_config)
        assert endpoint.getNetworkEndpointAddresses() == [ipv4_config]
        assert result == endpoint  # Test method chaining