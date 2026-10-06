import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    IpAddressKeepEnum,
)

CLASS_NOTE = "Defines the behavior after a dynamic IP address has been assigned."


class TestIpAddressKeepEnum:
    """Test cases for IpAddressKeepEnum (Table 6.138, p.466)."""

    def test_member_presence_and_values(self):
        assert IpAddressKeepEnum.FORGET == "FORGET"
        assert IpAddressKeepEnum.STORE_PERSISTENTLY == "STORE-PERSISTENTLY"
        assert list(IpAddressKeepEnum().getEnumValues()) == ["FORGET", "STORE-PERSISTENTLY"]

    def test_instantiability(self):
        enum = IpAddressKeepEnum()
        assert enum == enum.setValue(IpAddressKeepEnum.STORE_PERSISTENTLY)
        assert enum.getValue() == IpAddressKeepEnum.STORE_PERSISTENTLY

    def test_class_docstring_note(self):
        assert inspect.cleandoc(IpAddressKeepEnum.__doc__) == CLASS_NOTE
