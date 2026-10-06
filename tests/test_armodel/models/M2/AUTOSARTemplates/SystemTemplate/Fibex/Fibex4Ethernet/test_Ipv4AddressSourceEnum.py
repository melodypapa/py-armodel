import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    Ipv4AddressSourceEnum,
)

CLASS_NOTE = """Defines how the node obtains its IPv4-Address."""


class TestIpv4AddressSourceEnum:
    """Test cases for Ipv4AddressSourceEnum (Table 6.137, p.465)."""

    def test_member_presence_and_values(self):
        assert Ipv4AddressSourceEnum.AUTO_IP == "AUTO-IP"
        assert Ipv4AddressSourceEnum.AUTO_IP_DOIP == "AUTO-IP--DOIP"
        assert Ipv4AddressSourceEnum.DHCPV4 == "DHCPV-4"
        assert Ipv4AddressSourceEnum.FIXED == "FIXED"
        assert list(Ipv4AddressSourceEnum().getEnumValues()) == ["AUTO-IP", "AUTO-IP--DOIP", "DHCPV-4", "FIXED"]

    def test_instantiability(self):
        enum = Ipv4AddressSourceEnum()
        assert enum == enum.setValue(Ipv4AddressSourceEnum.AUTO_IP)
        assert enum.getValue() == Ipv4AddressSourceEnum.AUTO_IP

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Ipv4AddressSourceEnum.__doc__) == CLASS_NOTE
