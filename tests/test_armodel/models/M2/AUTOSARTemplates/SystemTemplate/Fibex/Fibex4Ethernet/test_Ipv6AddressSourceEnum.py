import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    Ipv6AddressSourceEnum,
)

CLASS_NOTE = "Defines how the node obtains its IPv6-Address."


class TestIpv6AddressSourceEnum:
    """Test cases for Ipv6AddressSourceEnum (Table 6.140, p.467)."""

    def test_member_presence_and_values(self):
        assert Ipv6AddressSourceEnum.DHCPV6 == "dhcpv6"
        assert Ipv6AddressSourceEnum.FIXED == "fixed"
        assert Ipv6AddressSourceEnum.LINK_LOCAL == "linkLocal"
        assert Ipv6AddressSourceEnum.LINK_LOCAL_DOIP == "linkLocal_doip"
        assert Ipv6AddressSourceEnum.ROUTER_ADVERTISEMENT == "routerAdvertisement"
        assert list(Ipv6AddressSourceEnum().getEnumValues()) == [
            "dhcpv6",
            "fixed",
            "linkLocal",
            "linkLocal_doip",
            "routerAdvertisement",
        ]

    def test_instantiability(self):
        enum = Ipv6AddressSourceEnum()
        assert enum == enum.setValue(Ipv6AddressSourceEnum.LINK_LOCAL_DOIP)
        assert enum.getValue() == "linkLocal_doip"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Ipv6AddressSourceEnum.__doc__) == CLASS_NOTE
