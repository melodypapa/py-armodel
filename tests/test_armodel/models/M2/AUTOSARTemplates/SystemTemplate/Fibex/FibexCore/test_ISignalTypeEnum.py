from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalTypeEnum


class Test_ISignalTypeEnum:
    """Test cases for ISignalTypeEnum class."""

    def test_members(self):
        """Test ISignalTypeEnum member values."""
        enum = ISignalTypeEnum()
        values = enum.getEnumValues()
        assert ISignalTypeEnum.ARRAY == "array"
        assert ISignalTypeEnum.PRIMITIVE == "primitive"
        assert ISignalTypeEnum.ARRAY in values
        assert ISignalTypeEnum.PRIMITIVE in values
