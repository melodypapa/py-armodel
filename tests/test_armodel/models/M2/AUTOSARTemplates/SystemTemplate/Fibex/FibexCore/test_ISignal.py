from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import DataTypePolicyEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    FibexElement,
    ISignal,
    ISignalProps,
    ISignalTypeEnum,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_FibexCoreISignal:
    """Test cases for FibexCore ISignal class."""

    def test_initialization(self):
        """Test ISignal initialization with default values."""
        parent = MockParent()
        signal = ISignal(parent, "test_i_signal")

        assert isinstance(signal, FibexElement)

        assert signal.getDataTransformationRef() is None
        assert signal.getDataTypePolicy() is None
        assert signal.getInitValue() is None
        assert signal.getISignalProps() is None
        assert signal.getISignalType() is None
        assert signal.getLength() is None
        assert signal.getNetworkRepresentationProps() is None
        assert signal.getSystemSignalRef() is None
        assert signal.getTimeoutSubstitutionValue() is None
        assert signal.getTransformationISignalProps() == []

    def test_get_set_data_transformation_ref(self):
        """Test getDataTransformationRef/setDataTransformationRef."""
        parent = MockParent()
        signal = ISignal(parent, "test_i_signal")

        assert signal == signal.setDataTransformationRef(None)
        assert signal.getDataTransformationRef() is None

        ref = RefType()
        ref.setValue("/Test/DataTransformation")
        assert signal == signal.setDataTransformationRef(ref)
        assert signal.getDataTransformationRef() == ref
        assert signal == signal.setDataTransformationRef(None)
        assert signal.getDataTransformationRef() == ref

    def test_get_set_data_type_policy(self):
        """Test getDataTypePolicy/setDataTypePolicy."""
        parent = MockParent()
        signal = ISignal(parent, "test_i_signal")

        assert signal == signal.setDataTypePolicy(None)
        assert signal.getDataTypePolicy() is None

        policy = DataTypePolicyEnum()
        policy.setValue(DataTypePolicyEnum.OVERRIDE)
        assert signal == signal.setDataTypePolicy(policy)
        assert signal.getDataTypePolicy() == policy
        assert signal == signal.setDataTypePolicy(None)
        assert signal.getDataTypePolicy() == policy

    def test_get_set_init_value(self):
        """Test getInitValue/setInitValue."""
        parent = MockParent()
        signal = ISignal(parent, "test_i_signal")

        assert signal == signal.setInitValue(None)
        assert signal.getInitValue() is None

        value = ARLiteral()
        value.setValue("init_value")
        assert signal == signal.setInitValue(value)
        assert signal.getInitValue() == value
        assert signal == signal.setInitValue(None)
        assert signal.getInitValue() == value

    def test_get_set_i_signal_props(self):
        """Test getISignalProps/setISignalProps."""
        parent = MockParent()
        signal = ISignal(parent, "test_i_signal")

        assert signal == signal.setISignalProps(None)
        assert signal.getISignalProps() is None

        props = ISignalProps()
        assert signal == signal.setISignalProps(props)
        assert signal.getISignalProps() == props
        assert signal == signal.setISignalProps(None)
        assert signal.getISignalProps() == props

    def test_get_set_i_signal_type(self):
        """Test getISignalType/setISignalType."""
        parent = MockParent()
        signal = ISignal(parent, "test_i_signal")

        assert signal == signal.setISignalType(None)
        assert signal.getISignalType() is None

        signal_type = ISignalTypeEnum()
        signal_type.setValue(ISignalTypeEnum.PRIMITIVE)
        assert signal == signal.setISignalType(signal_type)
        assert signal.getISignalType() == signal_type
        assert signal == signal.setISignalType(None)
        assert signal.getISignalType() == signal_type

    def test_get_set_length(self):
        """Test getLength/setLength."""
        parent = MockParent()
        signal = ISignal(parent, "test_i_signal")

        assert signal == signal.setLength(None)
        assert signal.getLength() is None

        assert signal == signal.setLength(8)
        assert signal.getLength() == 8
        assert signal == signal.setLength(None)
        assert signal.getLength() == 8

    def test_get_set_network_representation_props(self):
        """Test getNetworkRepresentationProps/setNetworkRepresentationProps."""
        parent = MockParent()
        signal = ISignal(parent, "test_i_signal")

        assert signal == signal.setNetworkRepresentationProps(None)
        assert signal.getNetworkRepresentationProps() is None

        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps

        props = SwDataDefProps()
        assert signal == signal.setNetworkRepresentationProps(props)
        assert signal.getNetworkRepresentationProps() == props
        assert signal == signal.setNetworkRepresentationProps(None)
        assert signal.getNetworkRepresentationProps() == props

    def test_get_set_system_signal_ref(self):
        """Test getSystemSignalRef/setSystemSignalRef."""
        parent = MockParent()
        signal = ISignal(parent, "test_i_signal")

        assert signal == signal.setSystemSignalRef(None)
        assert signal.getSystemSignalRef() is None

        ref = RefType()
        ref.setValue("/Test/SystemSignal")
        assert signal == signal.setSystemSignalRef(ref)
        assert signal.getSystemSignalRef() == ref
        assert signal == signal.setSystemSignalRef(None)
        assert signal.getSystemSignalRef() == ref

    def test_get_set_timeout_substitution_value(self):
        """Test getTimeoutSubstitutionValue/setTimeoutSubstitutionValue."""
        parent = MockParent()
        signal = ISignal(parent, "test_i_signal")

        assert signal == signal.setTimeoutSubstitutionValue(None)
        assert signal.getTimeoutSubstitutionValue() is None

        value = ARLiteral()
        value.setValue("timeout_value")
        assert signal == signal.setTimeoutSubstitutionValue(value)
        assert signal.getTimeoutSubstitutionValue() == value
        assert signal == signal.setTimeoutSubstitutionValue(None)
        assert signal.getTimeoutSubstitutionValue() == value

    def test_add_get_transformation_i_signal_props(self):
        """Test addTransformationISignalProps/getTransformationISignalProps."""
        parent = MockParent()
        signal = ISignal(parent, "test_i_signal")

        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import EndToEndTransformationISignalProps

        props = EndToEndTransformationISignalProps()
        signal.addTransformationISignalProps(props)
        assert signal.getTransformationISignalProps() == [props]
        assert signal == signal.addTransformationISignalProps(props)
        assert len(signal.getTransformationISignalProps()) == 2
        assert signal == signal.addTransformationISignalProps(None)
        assert len(signal.getTransformationISignalProps()) == 2


class Test_DataTypePolicyEnum:
    """Test cases for DataTypePolicyEnum class."""

    def test_members(self):
        """Test DataTypePolicyEnum member values."""
        enum = DataTypePolicyEnum()
        values = enum.getEnumValues()
        assert DataTypePolicyEnum.DDS_SERVICE == "ddsService"
        assert DataTypePolicyEnum.DDS_SIGNAL == "ddsSignal"
        assert DataTypePolicyEnum.LEGACY == "legacy"
        assert DataTypePolicyEnum.NETWORK_REPRESENTATION_FROM_COM_SPEC == "networkRepresentationFromComSpec"
        assert DataTypePolicyEnum.OVERRIDE == "override"
        assert DataTypePolicyEnum.TRANSFORMING_I_SIGNAL == "transformingISignal"
        assert DataTypePolicyEnum.DDS_SERVICE in values
        assert DataTypePolicyEnum.DDS_SIGNAL in values
        assert DataTypePolicyEnum.LEGACY in values
        assert DataTypePolicyEnum.NETWORK_REPRESENTATION_FROM_COM_SPEC in values
        assert DataTypePolicyEnum.OVERRIDE in values
        assert DataTypePolicyEnum.TRANSFORMING_I_SIGNAL in values
