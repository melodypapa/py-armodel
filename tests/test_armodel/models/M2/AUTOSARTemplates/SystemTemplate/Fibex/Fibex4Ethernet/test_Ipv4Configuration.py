import ast
import inspect
import sys

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    Ip4AddressString,
    IpAddressKeepEnum,
    Ipv4AddressSourceEnum,
    Ipv4Configuration,
)

CLASS_NOTE = """Internet Protocol version 4 (IPv4) configuration."""


class TestIpv4Configuration:
    """Test cases for Ipv4Configuration (Table 6.136, p.465)."""

    def _obj(self):
        return Ipv4Configuration()

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getAssignmentPriority() is None
        assert obj.getDefaultGateway() is None
        assert obj.getDnsServerAddresses() == []
        assert obj.getIpAddressKeepBehavior() is None
        assert obj.getIpv4Address() is None
        assert obj.getIpv4AddressSource() is None
        assert obj.getNetworkMask() is None
        assert obj.getTtl() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()
        assert obj.setAssignmentPriority(7) is obj
        assert obj.getAssignmentPriority() == 7
        obj.setAssignmentPriority(None)
        assert obj.getAssignmentPriority() == 7
        item = Ip4AddressString()
        assert obj.setDefaultGateway(item) is obj
        assert obj.getDefaultGateway() is item
        obj.setDefaultGateway(None)
        assert obj.getDefaultGateway() is item
        item = Ip4AddressString()
        assert obj.addDnsServerAddress(item) is obj
        assert obj.getDnsServerAddresses() == [item]
        obj.addDnsServerAddress(None)
        assert obj.getDnsServerAddresses() == [item]
        item = IpAddressKeepEnum()
        assert obj.setIpAddressKeepBehavior(item) is obj
        assert obj.getIpAddressKeepBehavior() is item
        obj.setIpAddressKeepBehavior(None)
        assert obj.getIpAddressKeepBehavior() is item
        item = Ip4AddressString()
        assert obj.setIpv4Address(item) is obj
        assert obj.getIpv4Address() is item
        obj.setIpv4Address(None)
        assert obj.getIpv4Address() is item
        item = Ipv4AddressSourceEnum()
        assert obj.setIpv4AddressSource(item) is obj
        assert obj.getIpv4AddressSource() is item
        obj.setIpv4AddressSource(None)
        assert obj.getIpv4AddressSource() is item
        item = Ip4AddressString()
        assert obj.setNetworkMask(item) is obj
        assert obj.getNetworkMask() is item
        obj.setNetworkMask(None)
        assert obj.getNetworkMask() is item
        assert obj.setTtl(7) is obj
        assert obj.getTtl() == 7
        obj.setTtl(None)
        assert obj.getTtl() == 7

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Ipv4Configuration.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert (
            inspect.cleandoc(obj.getAssignmentPriority.__doc__)
            == "Priority of assignment (1 is highest). If a new address from an assignment method with a higher priority is available, it overwrites the IP address previously assigned by an assignment method with a lower priority."
        )
        assert (
            inspect.cleandoc(obj.setAssignmentPriority.__doc__).split("\n")[0]
            == "Priority of assignment (1 is highest). If a new address from an assignment method with a higher priority is available, it overwrites the IP address previously assigned by an assignment method with a lower priority."
        )
        assert inspect.cleandoc(obj.getDefaultGateway.__doc__) == "IP address of the default gateway."
        assert inspect.cleandoc(obj.setDefaultGateway.__doc__).split("\n")[0] == "IP address of the default gateway."
        assert inspect.cleandoc(obj.getDnsServerAddresses.__doc__) == "IP addresses of preconfigured DNS servers."
        assert inspect.cleandoc(obj.addDnsServerAddress.__doc__).split("\n")[0] == "IP addresses of preconfigured DNS servers."
        assert inspect.cleandoc(obj.getIpAddressKeepBehavior.__doc__) == "Defines the lifetime of a dynamically fetched IP address."
        assert inspect.cleandoc(obj.setIpAddressKeepBehavior.__doc__).split("\n")[0] == "Defines the lifetime of a dynamically fetched IP address."
        assert (
            inspect.cleandoc(obj.getIpv4Address.__doc__)
            == "IPv4 Address. Notation: 255.255.255.255. The IP Address shall be declared in case the ipv4AddressSource is FIXED and thus no auto-configuration mechanism is used."
        )
        assert (
            inspect.cleandoc(obj.setIpv4Address.__doc__).split("\n")[0]
            == "IPv4 Address. Notation: 255.255.255.255. The IP Address shall be declared in case the ipv4AddressSource is FIXED and thus no auto-configuration mechanism is used."
        )
        assert inspect.cleandoc(obj.getIpv4AddressSource.__doc__) == "Defines how the node obtains its IP address."
        assert inspect.cleandoc(obj.setIpv4AddressSource.__doc__).split("\n")[0] == "Defines how the node obtains its IP address."
        assert inspect.cleandoc(obj.getNetworkMask.__doc__) == "Network mask. Notation 255.255.255.255"
        assert inspect.cleandoc(obj.setNetworkMask.__doc__).split("\n")[0] == "Network mask. Notation 255.255.255.255"
        assert (
            inspect.cleandoc(obj.getTtl.__doc__)
            == "Lifespan of data (0..255). The purpose of the TimeToLive field is to avoid a situation in which an undeliverable datagram keeps circulating on a system."
        )
        assert (
            inspect.cleandoc(obj.setTtl.__doc__).split("\n")[0]
            == "Lifespan of data (0..255). The purpose of the TimeToLive field is to avoid a situation in which an undeliverable datagram keeps circulating on a system."
        )

    def test_dns_pair_is_mutator_first_in_source(self):
        module = sys.modules[Ipv4Configuration.__module__]
        tree = ast.parse(inspect.getsource(module))
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "Ipv4Configuration")
        methods = [n.name for n in cls.body if isinstance(n, ast.FunctionDef)]
        assert methods.index("addDnsServerAddress") < methods.index("getDnsServerAddresses")
