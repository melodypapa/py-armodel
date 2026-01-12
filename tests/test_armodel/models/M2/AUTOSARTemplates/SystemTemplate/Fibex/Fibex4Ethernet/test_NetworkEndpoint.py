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
        with pytest.raises(NotImplementedError):
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
        
        # Test setter/getter methods
        config.setAssignmentPriority(1)
        assert config.getAssignmentPriority() == 1
        
        config.setIpv4Address("192.168.1.1")
        assert config.getIpv4Address() == "192.168.1.1"
        
        # Test adding DNS server addresses
        config.addDnsServerAddress("8.8.8.8")
        config.addDnsServerAddress("8.8.4.4")
        assert config.getDnsServerAddresses() == ["8.8.8.8", "8.8.4.4"]

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
        
        # Test setter/getter methods
        config.setIpv6Address("2001:db8::1")
        assert config.getIpv6Address() == "2001:db8::1"
        
        config.setEnableAnycast(True)
        assert config.getEnableAnycast() is True

    def test_DoIpEntity(self):
        """Test DoIpEntity class functionality."""
        entity = DoIpEntity()

        assert isinstance(entity, ARObject)
        
        # Test default values
        assert entity.getDoIpEntityRole() is None
        
        # Test setter/getter methods
        entity.setDoIpEntityRole("tester")
        assert entity.getDoIpEntityRole() == "tester"

    def test_TimeSyncClientConfiguration(self):
        """Test TimeSyncClientConfiguration class functionality."""
        config = TimeSyncClientConfiguration()

        assert isinstance(config, ARObject)
        
        # Test default values
        assert config.getOrderedMasters() == []
        assert config.getTimeSyncTechnology() is None
        
        # Test setter/getter methods
        config.setTimeSyncTechnology("IEEE_1588")
        assert config.getTimeSyncTechnology() == "IEEE_1588"

    def test_TimeSyncServerConfiguration(self):
        """Test TimeSyncServerConfiguration class functionality."""
        config = TimeSyncServerConfiguration()

        assert isinstance(config, ARObject)
        
        # Test default values
        assert config.getPriority() is None
        assert config.getSyncInterval() is None
        assert config.getTimeSyncServerIdentifier() is None
        assert config.getTimeSyncTechnology() is None
        
        # Test setter/getter methods
        config.setPriority(10)
        assert config.getPriority() == 10
        
        config.setSyncInterval("100ms")
        assert config.getSyncInterval() == "100ms"

    def test_TimeSynchronization(self):
        """Test TimeSynchronization class functionality."""
        sync = TimeSynchronization()

        assert isinstance(sync, ARObject)
        
        # Test default values
        assert sync.getTimeSyncClient() is None
        assert sync.getTimeSyncServer() is None
        
        # Test setter/getter methods
        client_config = TimeSyncClientConfiguration()
        sync.setTimeSyncClient(client_config)
        assert sync.getTimeSyncClient() == client_config

    def test_InfrastructureServices(self):
        """Test InfrastructureServices class functionality."""
        services = InfrastructureServices()

        assert isinstance(services, ARObject)
        
        # Test default values
        assert services.getDoIpEntity() is None
        assert services.getTimeSynchronization() is None
        
        # Test setter/getter methods
        doip_entity = DoIpEntity()
        services.setDoIpEntity(doip_entity)
        assert services.getDoIpEntity() == doip_entity

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
        
        # Test setter/getter methods
        endpoint.setFullyQualifiedDomainName("example.com")
        assert endpoint.getFullyQualifiedDomainName() == "example.com"
        
        # Test adding network endpoint addresses
        ipv4_config = Ipv4Configuration()
        endpoint.addNetworkEndpointAddress(ipv4_config)
        assert endpoint.getNetworkEndpointAddresses() == [ipv4_config]