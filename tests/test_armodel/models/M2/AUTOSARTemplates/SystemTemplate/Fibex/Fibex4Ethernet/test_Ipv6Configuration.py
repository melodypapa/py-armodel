import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Ip6AddressString,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    IpAddressKeepEnum,
    Ipv6AddressSourceEnum,
    Ipv6Configuration,
)

CLASS_NOTE = "Internet Protocol version 6 (IPv6) configuration."

DNS_NOTE = "IP addresses of pre configured DNS servers. Tags: xml.namePlural=DNS-SERVER-ADDRESSES"


class TestIpv6Configuration:
    """Test cases for Ipv6Configuration (Table 6.139, p.466)."""

    def _obj(self):
        return Ipv6Configuration()

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getAssignmentPriority() is None
        assert obj.getDefaultRouter() is None
        assert obj.getDnsServerAddresses() == []
        assert obj.getEnableAnycast() is None
        assert obj.getHopCount() is None
        assert obj.getIpAddressKeepBehavior() is None
        assert obj.getIpAddressPrefixLength() is None
        assert obj.getIpv6Address() is None
        assert obj.getIpv6AddressSource() is None

    def test_get_set_assignment_priority(self):
        obj = self._obj()
        value = PositiveInteger().setValue("1")
        assert obj.setAssignmentPriority(value) is obj
        assert obj.getAssignmentPriority() is value
        obj.setAssignmentPriority(None)
        assert obj.getAssignmentPriority() is value

    def test_get_set_default_router(self):
        obj = self._obj()
        value = Ip6AddressString().setValue("fe80::1")
        assert obj.setDefaultRouter(value) is obj
        assert obj.getDefaultRouter() is value
        obj.setDefaultRouter(None)
        assert obj.getDefaultRouter() is value

    def test_add_dns_server_address(self):
        obj = self._obj()
        value = Ip6AddressString().setValue("2001:db8::53")
        assert obj.addDnsServerAddress(value) is obj
        assert obj.getDnsServerAddresses() == [value]
        obj.addDnsServerAddress(None)
        assert obj.getDnsServerAddresses() == [value]

    def test_get_set_enable_anycast(self):
        obj = self._obj()
        value = Boolean().setValue("true")
        assert obj.setEnableAnycast(value) is obj
        assert obj.getEnableAnycast() is value
        obj.setEnableAnycast(None)
        assert obj.getEnableAnycast() is value

    def test_get_set_hop_count(self):
        obj = self._obj()
        value = PositiveInteger().setValue("64")
        assert obj.setHopCount(value) is obj
        assert obj.getHopCount() is value
        obj.setHopCount(None)
        assert obj.getHopCount() is value

    def test_get_set_ip_address_keep_behavior(self):
        obj = self._obj()
        value = IpAddressKeepEnum().setValue(IpAddressKeepEnum.STORE_PERSISTENTLY)
        assert obj.setIpAddressKeepBehavior(value) is obj
        assert obj.getIpAddressKeepBehavior() is value
        obj.setIpAddressKeepBehavior(None)
        assert obj.getIpAddressKeepBehavior() is value

    def test_get_set_ip_address_prefix_length(self):
        obj = self._obj()
        value = PositiveInteger().setValue("48")
        assert obj.setIpAddressPrefixLength(value) is obj
        assert obj.getIpAddressPrefixLength() is value
        obj.setIpAddressPrefixLength(None)
        assert obj.getIpAddressPrefixLength() is value

    def test_get_set_ipv6_address(self):
        obj = self._obj()
        value = Ip6AddressString().setValue("2001:db8::1")
        assert obj.setIpv6Address(value) is obj
        assert obj.getIpv6Address() is value
        obj.setIpv6Address(None)
        assert obj.getIpv6Address() is value

    def test_get_set_ipv6_address_source(self):
        obj = self._obj()
        value = Ipv6AddressSourceEnum().setValue(Ipv6AddressSourceEnum.DHCPV6)
        assert obj.setIpv6AddressSource(value) is obj
        assert obj.getIpv6AddressSource() is value
        obj.setIpv6AddressSource(None)
        assert obj.getIpv6AddressSource() is value

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Ipv6Configuration.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert (
            inspect.cleandoc(obj.getAssignmentPriority.__doc__)
            == "Priority of assignment (1 is highest). If a new address from an assignment method with a higher priority is available, it overwrites the IP address previously assigned by an assignment method with a lower priority."
        )
        assert inspect.cleandoc(obj.getDefaultRouter.__doc__) == "IP address of the default router."
        assert inspect.cleandoc(obj.getDnsServerAddresses.__doc__) == DNS_NOTE
        assert inspect.cleandoc(obj.addDnsServerAddress.__doc__).split("\n")[0] == DNS_NOTE
        assert inspect.cleandoc(obj.getEnableAnycast.__doc__) == "This attribute is used to enable anycast addressing (i.e. to one of multiple receivers)."
        assert inspect.cleandoc(obj.getHopCount.__doc__) == "The distance between two hosts. The hop count n means that n gateways separate the source host from the destination host (Range 0..255)"
        assert inspect.cleandoc(obj.getIpAddressKeepBehavior.__doc__) == "Defines the lifetime of a dynamically fetched IP address."
        assert inspect.cleandoc(obj.getIpAddressPrefixLength.__doc__) == "IPv6 prefix length defines the part of the IPv6 address that is the network prefix."
        assert (
            inspect.cleandoc(obj.getIpv6Address.__doc__)
            == "IPv6 Address. Notation: FFFF:...:FFFF. The IP Address shall be declared in case the ipv6AddressSource is FIXED and thus no auto-configuration mechanism is used."
        )
        assert inspect.cleandoc(obj.getIpv6AddressSource.__doc__) == "Defines how the node obtains its IP address."
