import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    Ipv4AddressSourceEnum,
)

CLASS_NOTE = """Defines how the node obtains its IPv4-Address."""


class TestIpv4AddressSourceEnum:
    """Test cases for Ipv4AddressSourceEnum (Table 6.137, p.465)."""

    def test_member_presence_and_values(self):
        assert Ipv4AddressSourceEnum.AUTO_IP == "autoIp"
        assert Ipv4AddressSourceEnum.AUTO_IP_DOIP == "autoIp_doip"
        assert Ipv4AddressSourceEnum.DHCPV4 == "dhcpv4"
        assert Ipv4AddressSourceEnum.FIXED == "fixed"
        assert list(Ipv4AddressSourceEnum().getEnumValues()) == ["autoIp", "autoIp_doip", "dhcpv4", "fixed"]

    def test_instantiability(self):
        enum = Ipv4AddressSourceEnum()
        assert enum == enum.setValue(Ipv4AddressSourceEnum.AUTO_IP)
        assert enum.getValue() == "autoIp"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Ipv4AddressSourceEnum.__doc__) == CLASS_NOTE
