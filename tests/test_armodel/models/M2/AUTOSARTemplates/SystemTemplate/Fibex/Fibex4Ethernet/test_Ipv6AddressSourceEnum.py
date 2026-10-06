import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    Ipv6AddressSourceEnum,
)

CLASS_NOTE = "Defines how the node obtains its IPv6-Address."


class TestIpv6AddressSourceEnum:
    """Test cases for Ipv6AddressSourceEnum (Table 6.140, p.467)."""

    def test_member_presence_and_values(self):
        assert Ipv6AddressSourceEnum.DHCPV6 == "DHCPV-6"
        assert Ipv6AddressSourceEnum.FIXED == "FIXED"
        assert Ipv6AddressSourceEnum.LINK_LOCAL == "LINK-LOCAL"
        assert Ipv6AddressSourceEnum.LINK_LOCAL_DOIP == "LINK-LOCAL--DOIP"
        assert Ipv6AddressSourceEnum.ROUTER_ADVERTISEMENT == "ROUTER-ADVERTISEMENT"
        assert list(Ipv6AddressSourceEnum().getEnumValues()) == [
            Ipv6AddressSourceEnum.DHCPV6,
            "FIXED",
            Ipv6AddressSourceEnum.LINK_LOCAL,
            Ipv6AddressSourceEnum.LINK_LOCAL_DOIP,
            Ipv6AddressSourceEnum.ROUTER_ADVERTISEMENT,
        ]

    def test_instantiability(self):
        enum = Ipv6AddressSourceEnum()
        assert enum == enum.setValue(Ipv6AddressSourceEnum.LINK_LOCAL_DOIP)
        assert enum.getValue() == Ipv6AddressSourceEnum.LINK_LOCAL_DOIP

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Ipv6AddressSourceEnum.__doc__) == CLASS_NOTE
