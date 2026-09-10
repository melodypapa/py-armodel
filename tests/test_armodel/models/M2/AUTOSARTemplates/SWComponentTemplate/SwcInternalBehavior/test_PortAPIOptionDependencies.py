from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import DataTransformationErrorHandlingEnum


class TestDataTransformationErrorHandlingEnum:
    def test_literals_and_instantiation(self):
        enum = DataTransformationErrorHandlingEnum()
        assert enum.getEnumValues() == [
            DataTransformationErrorHandlingEnum.NO_TRANSFORMER_ERROR_HANDLING,
            DataTransformationErrorHandlingEnum.TRANSFORMER_ERROR_HANDLING,
        ]
        assert DataTransformationErrorHandlingEnum.NO_TRANSFORMER_ERROR_HANDLING == "noTransformerErrorHandling"
        assert DataTransformationErrorHandlingEnum.TRANSFORMER_ERROR_HANDLING == "transformerErrorHandling"
