from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import DataTransformationStatusForwardingEnum


class TestDataTransformationStatusForwardingEnum:
    def test_literals_and_instantiation(self):
        enum = DataTransformationStatusForwardingEnum()
        assert enum.getEnumValues() == [
            DataTransformationStatusForwardingEnum.NO_TRANSFORMER_STATUS_FORWARDING,
            DataTransformationStatusForwardingEnum.TRANSFORMER_STATUS_FORWARDING,
        ]
        assert DataTransformationStatusForwardingEnum.NO_TRANSFORMER_STATUS_FORWARDING == "NO-TRANSFORMER-STATUS-FORWARDING"
        assert DataTransformationStatusForwardingEnum.TRANSFORMER_STATUS_FORWARDING == "TRANSFORMER-STATUS-FORWARDING"
