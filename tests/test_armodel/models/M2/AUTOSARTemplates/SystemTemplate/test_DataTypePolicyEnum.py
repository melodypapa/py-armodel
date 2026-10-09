from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import DataTypePolicyEnum


class Test_DataTypePolicyEnum:
    """Test cases for DataTypePolicyEnum class."""

    def test_members(self):
        """Test DataTypePolicyEnum member values."""
        enum = DataTypePolicyEnum()
        values = enum.getEnumValues()
        assert DataTypePolicyEnum.DDS_SERVICE == "DDS-SERVICE"
        assert DataTypePolicyEnum.DDS_SIGNAL == "DDS-SIGNAL"
        assert DataTypePolicyEnum.LEGACY == "LEGACY"
        assert DataTypePolicyEnum.NETWORK_REPRESENTATION_FROM_COM_SPEC == "NETWORK-REPRESENTATION-FROM-COM-SPEC"
        assert DataTypePolicyEnum.OVERRIDE == "OVERRIDE"
        assert DataTypePolicyEnum.TRANSFORMING_I_SIGNAL == "TRANSFORMING-I-SIGNAL"
        assert DataTypePolicyEnum.DDS_SERVICE in values
        assert DataTypePolicyEnum.DDS_SIGNAL in values
        assert DataTypePolicyEnum.LEGACY in values
        assert DataTypePolicyEnum.NETWORK_REPRESENTATION_FROM_COM_SPEC in values
        assert DataTypePolicyEnum.OVERRIDE in values
        assert DataTypePolicyEnum.TRANSFORMING_I_SIGNAL in values
