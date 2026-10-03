import inspect
import re
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    InfrastructureServices,
    IPSecConfig,
    Ipv4Configuration,
    NetworkEndpoint,
    NetworkEndpointAddress,
)

CLASS_NOTE = """The network endpoint defines the network addressing (e.g. IP-Address or MAC multicast address)."""

FIELD_ORDER = ["fullyQualifiedDomainName", "infrastructureServices", "ipSecConfig", "networkEndpointAddresses", "priority"]

METHOD_ORDER = [
    "__init__",
    "getFullyQualifiedDomainName",
    "setFullyQualifiedDomainName",
    "getInfrastructureServices",
    "setInfrastructureServices",
    "getIpSecConfig",
    "setIpSecConfig",
    "addNetworkEndpointAddress",
    "getNetworkEndpointAddresses",
    "getPriority",
    "setPriority",
]


class TestNetworkEndpoint:
    """Test cases for NetworkEndpoint (Table 6.134, p.463)."""

    def _obj(self):
        return NetworkEndpoint(None, "Obj")

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getFullyQualifiedDomainName() is None
        assert obj.getInfrastructureServices() is None
        assert obj.getIpSecConfig() is None
        assert obj.getNetworkEndpointAddresses() == []
        assert obj.getPriority() is None

    def test_fully_qualified_domain_name_round_trip_and_none_noop(self):
        obj = self._obj()
        name = String().setValue("some.example.host")
        assert obj.setFullyQualifiedDomainName(name) is obj
        assert obj.getFullyQualifiedDomainName() is name
        assert obj.getFullyQualifiedDomainName().getValue() == "some.example.host"
        obj.setFullyQualifiedDomainName(None)
        assert obj.getFullyQualifiedDomainName() is name

    def test_infrastructure_services_round_trip_and_none_noop(self):
        obj = self._obj()
        item = InfrastructureServices()
        assert obj.setInfrastructureServices(item) is obj
        assert obj.getInfrastructureServices() is item
        obj.setInfrastructureServices(None)
        assert obj.getInfrastructureServices() is item

    def test_ip_sec_config_round_trip_and_none_noop(self):
        obj = self._obj()
        item = IPSecConfig()
        assert obj.setIpSecConfig(item) is obj
        assert obj.getIpSecConfig() is item
        obj.setIpSecConfig(None)
        assert obj.getIpSecConfig() is item

    def test_add_network_endpoint_address_appends_and_returns(self):
        obj = self._obj()
        item = Ipv4Configuration()
        assert obj.addNetworkEndpointAddress(item) is obj
        assert obj.getNetworkEndpointAddresses() == [item]

    def test_add_network_endpoint_address_none_noop(self):
        obj = self._obj()
        assert obj.addNetworkEndpointAddress(None) is obj
        assert obj.getNetworkEndpointAddresses() == []

    def test_priority_round_trip_and_none_noop(self):
        obj = self._obj()
        value = PositiveInteger().setValue("7")
        assert obj.setPriority(value) is obj
        assert obj.getPriority() is value
        assert obj.getPriority().getValue() == 7
        obj.setPriority(None)
        assert obj.getPriority() is value

    def test_class_docstring_note(self):
        assert inspect.cleandoc(NetworkEndpoint.__doc__) == CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert NetworkEndpoint.__init__.__doc__ is None

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        fqdn = "Defines the fully qualified domain name (FQDN) e.g. some.example.host."
        services = "Defines the network infrastructure services provided or consumed."
        ipsec = "Optional IPSec configuration that provides security services for IP packets."
        address = "Definition of a Network Address."
        priority = "Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed."
        assert inspect.cleandoc(obj.getFullyQualifiedDomainName.__doc__) == fqdn
        assert inspect.cleandoc(obj.setFullyQualifiedDomainName.__doc__).split("\n")[0] == fqdn
        assert inspect.cleandoc(obj.setFullyQualifiedDomainName.__doc__).split("\n")[1] == "A None value is a no-op and does not overwrite an existing fullyQualifiedDomainName."
        assert inspect.cleandoc(obj.getInfrastructureServices.__doc__) == services
        assert inspect.cleandoc(obj.setInfrastructureServices.__doc__).split("\n")[0] == services
        assert inspect.cleandoc(obj.setInfrastructureServices.__doc__).split("\n")[1] == "A None value is a no-op and does not overwrite an existing infrastructureServices."
        assert inspect.cleandoc(obj.getIpSecConfig.__doc__) == ipsec
        assert inspect.cleandoc(obj.setIpSecConfig.__doc__).split("\n")[0] == ipsec
        assert inspect.cleandoc(obj.setIpSecConfig.__doc__).split("\n")[1] == "A None value is a no-op and does not overwrite an existing ipSecConfig."
        assert inspect.cleandoc(obj.addNetworkEndpointAddress.__doc__).split("\n")[0] == address
        assert inspect.cleandoc(obj.addNetworkEndpointAddress.__doc__).split("\n")[1] == "A None value is a no-op and is not appended to networkEndpointAddresses."
        assert inspect.cleandoc(obj.getNetworkEndpointAddresses.__doc__) == address
        assert inspect.cleandoc(obj.getPriority.__doc__) == priority
        assert inspect.cleandoc(obj.setPriority.__doc__).split("\n")[0] == priority
        assert inspect.cleandoc(obj.setPriority.__doc__).split("\n")[1] == "A None value is a no-op and does not overwrite an existing priority."

    def test_member_order_follows_spec_row_order(self):
        init_src = inspect.getsource(NetworkEndpoint.__init__)
        fields = re.findall(r"self\.(\w+):", init_src)
        assert fields == FIELD_ORDER

        class_src = inspect.getsource(NetworkEndpoint)
        methods = re.findall(r"def (\w+)\(self", class_src)
        assert methods == METHOD_ORDER

    def test_typing_pins(self):
        hints = typing.get_type_hints(NetworkEndpoint.getFullyQualifiedDomainName)
        assert hints.get("return") == typing.Optional[String]
        setter_hints = typing.get_type_hints(NetworkEndpoint.setFullyQualifiedDomainName)
        assert setter_hints.get("value") == typing.Optional[String]
        assert setter_hints.get("return") is NetworkEndpoint
        address_hints = typing.get_type_hints(NetworkEndpoint.getNetworkEndpointAddresses)
        assert address_hints.get("return") == typing.List[NetworkEndpointAddress]
        add_hints = typing.get_type_hints(NetworkEndpoint.addNetworkEndpointAddress)
        assert add_hints.get("value") == typing.Optional[NetworkEndpointAddress]
        assert add_hints.get("return") is NetworkEndpoint
