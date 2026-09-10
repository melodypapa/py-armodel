"""
This module contains comprehensive tests for the PortAPIOptions module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the PortAPIOptions.py file to achieve 100% test coverage.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, TRefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import PortAPIOption, PortDefinedArgumentValue


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

    def test_port_api_option_spec_contract(self):
        option = PortAPIOption()
        assert option.__class__.__doc__.strip() == (
            "If set to true, the software-component is able to use the API reference for deriving a pointer to an object."
        )
        enable = Boolean().setValue(True)
        assert option.setEnableTakeAddress(enable) is option
        option.setEnableTakeAddress(None)
        assert option.getEnableTakeAddress() is enable

    def test_port_api_option_initialization(self):
        """Test PortAPIOption initialization and methods."""
        port_api_option = PortAPIOption()

        assert port_api_option.enableTakeAddress is None
        assert port_api_option.errorHandling is None
        assert port_api_option.indirectAPI is None
        assert port_api_option.portRef is None
        assert port_api_option.portArgValues == []
        assert port_api_option.supportedFeatures == []
        assert port_api_option.transformerStatusForwarding is None

        # Test enableTakeAddress methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean

        enable_take = Boolean()
        enable_take.setValue(True)
        port_api_option.setEnableTakeAddress(enable_take)
        assert port_api_option.getEnableTakeAddress() == enable_take

        # Test errorHandling methods
        error_handling = "test_error_handling"
        port_api_option.setErrorHandling(error_handling)
        assert port_api_option.getErrorHandling() == error_handling

        # Test indirectAPI methods
        indirect_api = Boolean()
        indirect_api.setValue(False)
        port_api_option.setIndirectAPI(indirect_api)
        assert port_api_option.getIndirectAPI() == indirect_api

        # Test portRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        port_ref = RefType()
        port_ref.setValue("/Port/Ref")
        port_api_option.setPortRef(port_ref)
        assert port_api_option.getPortRef() == port_ref

        # Test portArgValues methods
        arg_value = PortDefinedArgumentValue()
        port_api_option.addPortArgValue(arg_value)
        assert arg_value in port_api_option.getPortArgValues()

        # Test supportedFeatures methods
        feature = "test_feature"
        port_api_option.addSupportedFeature(feature)
        assert feature in port_api_option.getSupportedFeatures()

        # Test transformerStatusForwarding methods
        transformer_status = "test_transformer"
        port_api_option.setTransformerStatusForwarding(transformer_status)
        assert port_api_option.getTransformerStatusForwarding() == transformer_status
