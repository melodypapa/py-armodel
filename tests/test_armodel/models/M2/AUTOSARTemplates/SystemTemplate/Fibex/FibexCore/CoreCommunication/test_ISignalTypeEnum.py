import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ISignalTypeEnum,
)

CLASS_NOTE = "This enumeration defines ISignal types that are used for derivation of the ComSignalType in the COM configuration."


class TestISignalTypeEnum:
    """Test cases for ISignalTypeEnum class (Table 6.9, p.322)."""

    def test_member_presence_and_values(self):
        assert ISignalTypeEnum.ARRAY == "ARRAY"
        assert ISignalTypeEnum.PRIMITIVE == "PRIMITIVE"
        assert list(ISignalTypeEnum().getEnumValues()) == [
            ISignalTypeEnum.ARRAY,
            ISignalTypeEnum.PRIMITIVE,
        ]

    def test_instantiability(self):
        enum = ISignalTypeEnum()
        assert enum == enum.setValue(ISignalTypeEnum.PRIMITIVE)
        assert enum.getValue() == ISignalTypeEnum.PRIMITIVE

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ISignalTypeEnum.__doc__) == CLASS_NOTE
