import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    RuntimeAddressConfigurationEnum,
)

CLASS_NOTE = "This enumeration defines the protocol to be used to obtain the address information."


class TestRuntimeAddressConfigurationEnum:
    """Test cases for RuntimeAddressConfigurationEnum (R4.3.1 Table 6.121, p.320)."""

    def test_member_presence_and_values(self):
        assert RuntimeAddressConfigurationEnum.NONE == "NONE"
        assert RuntimeAddressConfigurationEnum.SD == "SD"
        assert list(RuntimeAddressConfigurationEnum().getEnumValues()) == ["NONE", "SD"]

    def test_instantiability(self):
        enum = RuntimeAddressConfigurationEnum()
        assert enum == enum.setValue(RuntimeAddressConfigurationEnum.SD)
        assert enum.getValue() == RuntimeAddressConfigurationEnum.SD

    def test_class_docstring_note(self):
        assert inspect.cleandoc(RuntimeAddressConfigurationEnum.__doc__) == CLASS_NOTE
