import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    RuntimeAddressConfigurationEnum,
)

CLASS_NOTE = "This enumeration defines the protocol to be used to obtain the address information."


class TestRuntimeAddressConfigurationEnum:
    """Test cases for RuntimeAddressConfigurationEnum (R4.3.1 Table 6.121, p.320)."""

    def test_member_presence_and_values(self):
        assert RuntimeAddressConfigurationEnum.NONE == "none"
        assert RuntimeAddressConfigurationEnum.SD == "sd"
        assert list(RuntimeAddressConfigurationEnum().getEnumValues()) == ["none", "sd"]

    def test_instantiability(self):
        enum = RuntimeAddressConfigurationEnum()
        assert enum == enum.setValue(RuntimeAddressConfigurationEnum.SD)
        assert enum.getValue() == "sd"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(RuntimeAddressConfigurationEnum.__doc__) == CLASS_NOTE
