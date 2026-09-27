import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    InfrastructureServices,
    IPSecConfig,
    Ipv4Configuration,
    NetworkEndpoint,
)

CLASS_NOTE = """The network endpoint defines the network addressing (e.g. IP-Address or MAC multicast address)."""


class TestNetworkEndpoint:
    """Test cases for NetworkEndpoint (Table 6.134, p.463)."""

    def _obj(self):
        return NetworkEndpoint(None, "Obj")

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getFullyQualifiedDomainName() is None
        assert obj.getInfrastructureServices() is None
        assert obj.getIpSecConfig() is None
        assert obj.networkEndpointAddresses == []
        assert obj.getPriority() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()
        assert obj.setFullyQualifiedDomainName("x") is obj
        assert obj.getFullyQualifiedDomainName() == "x"
        obj.setFullyQualifiedDomainName(None)
        assert obj.getFullyQualifiedDomainName() == "x"
        item = InfrastructureServices()
        assert obj.setInfrastructureServices(item) is obj
        assert obj.getInfrastructureServices() is item
        obj.setInfrastructureServices(None)
        assert obj.getInfrastructureServices() is item
        item = IPSecConfig()
        assert obj.setIpSecConfig(item) is obj
        assert obj.getIpSecConfig() is item
        obj.setIpSecConfig(None)
        assert obj.getIpSecConfig() is item
        item = Ipv4Configuration()
        assert obj.addNetworkEndpointAddress(item) is obj
        assert obj.networkEndpointAddresses == [item]
        obj.addNetworkEndpointAddress(None)
        assert obj.networkEndpointAddresses == [item]
        assert obj.setPriority(7) is obj
        assert obj.getPriority() == 7
        obj.setPriority(None)
        assert obj.getPriority() == 7

    def test_class_docstring_note(self):
        assert inspect.cleandoc(NetworkEndpoint.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getFullyQualifiedDomainName.__doc__) == "Defines the fully qualified domain name (FQDN) e.g. some.example.host."
        assert inspect.cleandoc(obj.setFullyQualifiedDomainName.__doc__).split("\n")[0] == "Defines the fully qualified domain name (FQDN) e.g. some.example.host."
        assert inspect.cleandoc(obj.getInfrastructureServices.__doc__) == "Defines the network infrastructure services provided or consumed."
        assert inspect.cleandoc(obj.setInfrastructureServices.__doc__).split("\n")[0] == "Defines the network infrastructure services provided or consumed."
        assert inspect.cleandoc(obj.getIpSecConfig.__doc__) == "Optional IPSec configuration that provides security services for IP packets."
        assert inspect.cleandoc(obj.setIpSecConfig.__doc__).split("\n")[0] == "Optional IPSec configuration that provides security services for IP packets."
        assert inspect.cleandoc(obj.addNetworkEndpointAddress.__doc__).split("\n")[0] == "Definition of a Network Address. Tags: xml.namePlural=NETWORK-ENDPOINT-ADDRESSES"
        assert inspect.cleandoc(obj.getPriority.__doc__) == "Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed."
        assert inspect.cleandoc(obj.setPriority.__doc__).split("\n")[0] == "Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed."
