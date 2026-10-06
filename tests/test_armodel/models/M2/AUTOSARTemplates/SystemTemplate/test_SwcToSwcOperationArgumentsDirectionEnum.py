import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SwcToSwcOperationArgumentsDirectionEnum


class TestSwcToSwcOperationArgumentsDirectionEnum:
    """Test cases for SwcToSwcOperationArgumentsDirectionEnum (Table 5.39, p.254)."""

    def test_inheritance(self):
        assert issubclass(SwcToSwcOperationArgumentsDirectionEnum, AREnum)

    def test_members(self):
        assert SwcToSwcOperationArgumentsDirectionEnum.IN == "IN"
        assert SwcToSwcOperationArgumentsDirectionEnum.OUT == "OUT"

    def test_literal_values(self):
        enum = SwcToSwcOperationArgumentsDirectionEnum()
        assert list(enum.getEnumValues()) == ["IN", "OUT"]

    def test_instantiability(self):
        enum = SwcToSwcOperationArgumentsDirectionEnum()
        enum.setValue(SwcToSwcOperationArgumentsDirectionEnum.IN)
        assert enum.getValue() == SwcToSwcOperationArgumentsDirectionEnum.IN
        enum.setValue(SwcToSwcOperationArgumentsDirectionEnum.OUT)
        assert enum.getValue() == SwcToSwcOperationArgumentsDirectionEnum.OUT

    def test_type_hints(self):
        hints = typing.get_type_hints(SwcToSwcOperationArgumentsDirectionEnum.getValue)
        assert "return" in hints
        hints = typing.get_type_hints(SwcToSwcOperationArgumentsDirectionEnum.setValue)
        assert "val" in hints
