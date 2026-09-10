"""
This module contains comprehensive tests for the PortAPIOptions module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the PortAPIOptions.py file to achieve 100% test coverage.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType, TRefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import (
    CommunicationBufferLocking,
    DataTransformationErrorHandlingEnum,
    DataTransformationStatusForwardingEnum,
    PortAPIOption,
    PortDefinedArgumentValue,
)


class TestPortDefinedArgumentValue:
    """Test class for PortDefinedArgumentValue class."""

    def test_port_defined_argument_value_spec_contract(self):
        arg_value = PortDefinedArgumentValue()
        assert arg_value.__class__.__doc__.strip() == (
            "A PortDefinedArgumentValue is passed to a RunnableEntity dealing with the ClientServerOperations provided by a given PortPrototype. Note that this is restricted to PPortPrototypes of a ClientServer Interface."
        )
        value = TextValueSpecification()
        value_type = TRefType().setValue("/Type/Ref")
        assert arg_value.setValue(value) is arg_value
        assert arg_value.setValueTypeTRef(value_type) is arg_value
        arg_value.setValue(None)
        arg_value.setValueTypeTRef(None)
        assert arg_value.getValue() is value
        assert arg_value.getValueTypeTRef() is value_type

    def test_port_defined_argument_value_initialization(self):
        """Test PortDefinedArgumentValue initialization and methods."""
        arg_value = PortDefinedArgumentValue()

        assert arg_value.value is None
        assert arg_value.valueTypeTRef is None

        # Test value methods
        from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification

        value_spec = TextValueSpecification()
        arg_value.setValue(value_spec)
        assert arg_value.getValue() == value_spec

        # Test valueTypeTRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TRefType

        type_ref = TRefType()
        type_ref.setValue("/Type/Ref")
        arg_value.setValueTypeTRef(type_ref)
        assert arg_value.getValueTypeTRef() == type_ref


class TestPortAPIOption:
    """Test class for PortAPIOption class."""

    def test_port_api_option_initialization(self):
        option = PortAPIOption()
        assert option.enableTakeAddress is None
        assert option.errorHandling is None
        assert option.indirectAPI is None
        assert option.portRef is None
        assert option.portArgValues == []
        assert option.supportedFeatures == []
        assert option.transformerStatusForwarding is None

    def test_port_api_option_class_docstring_verbatim(self):
        assert PortAPIOption.__doc__.strip() == (
            "Options how to generate the signatures of calls for an AtomicSwComponentType "
            "in order to communicate over a PortPrototype (for calls into a RunnableEntity "
            "as well as for calls from a Runnable Entity to the PortPrototype)."
        )

    def test_enable_take_address_round_trip(self):
        option = PortAPIOption()
        value = Boolean().setValue(True)
        assert option.setEnableTakeAddress(value) is option
        assert option.getEnableTakeAddress() is value
        option.setEnableTakeAddress(None)
        assert option.getEnableTakeAddress() is value

    def test_error_handling_round_trip(self):
        option = PortAPIOption()
        value = DataTransformationErrorHandlingEnum().setValue(DataTransformationErrorHandlingEnum.TRANSFORMER_ERROR_HANDLING)
        assert option.setErrorHandling(value) is option
        assert option.getErrorHandling() is value
        option.setErrorHandling(None)
        assert option.getErrorHandling() is value

    def test_indirect_api_round_trip(self):
        option = PortAPIOption()
        value = Boolean().setValue(False)
        assert option.setIndirectAPI(value) is option
        assert option.getIndirectAPI() is value
        option.setIndirectAPI(None)
        assert option.getIndirectAPI() is value

    def test_port_ref_round_trip(self):
        option = PortAPIOption()
        value = RefType().setValue("/Port/Ref")
        assert option.setPortRef(value) is option
        assert option.getPortRef() is value
        option.setPortRef(None)
        assert option.getPortRef() is value

    def test_port_arg_values_ordered(self):
        option = PortAPIOption()
        first = PortDefinedArgumentValue()
        second = PortDefinedArgumentValue()
        assert option.addPortArgValue(first) is option
        option.addPortArgValue(second)
        assert option.getPortArgValues() == [first, second]
        option.addPortArgValue(None)
        assert option.getPortArgValues() == [first, second]

    def test_supported_features_ordered(self):
        option = PortAPIOption()
        first = CommunicationBufferLocking().setSupportBufferLocking(DataTransformationStatusForwardingEnum.NO_TRANSFORMER_STATUS_FORWARDING)
        second = CommunicationBufferLocking().setSupportBufferLocking(DataTransformationStatusForwardingEnum.TRANSFORMER_STATUS_FORWARDING)
        assert option.addSupportedFeature(first) is option
        option.addSupportedFeature(second)
        assert option.getSupportedFeatures() == [first, second]
        option.addSupportedFeature(None)
        assert option.getSupportedFeatures() == [first, second]

    def test_transformer_status_forwarding_round_trip(self):
        option = PortAPIOption()
        value = DataTransformationStatusForwardingEnum().setValue(DataTransformationStatusForwardingEnum.TRANSFORMER_STATUS_FORWARDING)
        assert option.setTransformerStatusForwarding(value) is option
        assert option.getTransformerStatusForwarding() is value
        option.setTransformerStatusForwarding(None)
        assert option.getTransformerStatusForwarding() is value
