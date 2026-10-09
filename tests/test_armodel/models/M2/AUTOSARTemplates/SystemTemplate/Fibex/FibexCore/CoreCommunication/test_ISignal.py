import inspect

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import DataTypePolicyEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ISignal,
    ISignalProps,
    ISignalTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import EndToEndTransformationISignalProps
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps

CLASS_NOTE = 'Signal of the Interaction Layer. The RTE supports a "signal fan-out" where the same System Signal is sent in different SignalIPdus to multiple receivers. To support the RTE "signal fan-out" each SignalIPdu contains ISignals. If the same System Signal is to be mapped into several SignalIPdus there is one ISignal needed for each ISignalToIPduMapping. ISignals describe the Interface between the Precompile configured RTE and the potentially Postbuild configured Com Stack (see ECUC Parameter Mapping). In case of the SystemSignalGroup an ISignal shall be created for each SystemSignal contained in the SystemSignalGroup.'
DATA_TRANSFORMATION_REF_NOTE = "Optional reference to a DataTransformation which represents the transformer chain that is used to transform the data that shall be placed inside this ISignal. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataTransformation.dataTransformation, dataTransformation.variationPoint.shortLabel vh.latestBindingTime=codeGenerationTime"
DATA_TYPE_POLICY_NOTE = 'With the aggregation of SwDataDefProps an ISignal specifies how it is represented on the network. This representation follows a particular policy. Note that this causes some redundancy which is intended and can be used to support flexible development methodology as well as subsequent integrity checks. If the policy "networkRepresentationFromComSpec" is chosen the network representation from the ComSpec that is aggregated by the PortPrototype shall be used. If the "override" policy is chosen the requirements specified in the PortInterface and in the ComSpec are not fulfilled by the networkRepresentationProps. In case the System Description doesn\'t use a complete Software Component Description (VFB View) the "legacy" policy can be chosen.'
INIT_VALUE_NOTE = "Optional definition of a ISignal's initValue in case the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy system signals. This value can be used to configure the Signal's \"Init Value\". If a full DataMapping exist for the SystemSignal this information may be available from a configured Sender ComSpec and ReceiverComSpec. In this case the initvalues in SenderComSpec and/or ReceiverComSpec override this optional value specification. Further restrictions apply from the RTE specification."
I_SIGNAL_PROPS_NOTE = "Additional optional ISignal properties that may be stored in different files. Stereotypes: atpSplitable Tags: atp.Splitkey=iSignalProps"
I_SIGNAL_TYPE_NOTE = "This attribute defines whether this iSignal is an array that results in a UINT8_N / UINT8_DYN ComSignalType in the COM configuration or a primitive type."
LENGTH_NOTE = "Size of the signal in bits. The size needs to be derived from the mapped VariableDataPrototype according to the mapping of primitive DataTypes to BaseTypes as used in the RTE. Indicates maximum size for dynamic length signals. The ISignal length of zero bits is allowed."
NETWORK_REPRESENTATION_PROPS_NOTE = 'Specification of the actual network representation. The usage of SwDataDefProps for this purpose is restricted to the attributes compuMethod and baseType. The optional baseType attributes "memAllignment" and "byteOrder" shall not be used. The attribute "dataTypePolicy" in the SystemTemplate element defines whether this network representation shall be ignored and the information shall be taken over from the network representation of the ComSpec. If "override" is chosen by the system integrator the network representation can violate against the requirements defined in the PortInterface and in the network representation of the ComSpec. In case that the System Description doesn\'t use a complete Software Component Description (VFB View) this element is used to configure "ComSignalDataInvalid Value" and the Data Semantics. Stereotypes: atpSplitable Tags: atp.Splitkey=networkRepresentationProps'
SYSTEM_SIGNAL_REF_NOTE = "Reference to the System Signal that is supposed to be transmitted in the ISignal."
TIMEOUT_SUBSTITUTION_VALUE_NOTE = "Defines and enables the ComTimeoutSubstituition for this ISignal."
TRANSFORMATION_I_SIGNAL_PROPS_NOTE = "A transformer chain consists of an ordered list of transformers. The ISignal specific configuration properties for each transformer are defined in the TransformationISignalProps class. The transformer configuration properties that are common for all ISignals are described in the TransformationTechnology class. Stereotypes: atpSplitable Tags: atp.Splitkey=transformationISignalProps"


class TestISignal:
    """Test cases for ISignal class (Table 6.7, p.321)."""

    def test_initialization_defaults(self):
        signal = ISignal(None, "ISignal")
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement

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
        signal = ISignal(None, "ISignal")

        ref = RefType()
        ref.setValue("/FibexCore/DataTransformation")
        assert signal.setDataTransformationRef(ref) is signal
        assert signal.getDataTransformationRef() is ref
        signal.setDataTransformationRef(None)
        assert signal.getDataTransformationRef() is ref

    def test_get_set_data_type_policy(self):
        signal = ISignal(None, "ISignal")

        policy = DataTypePolicyEnum()
        policy.setValue(DataTypePolicyEnum.OVERRIDE)
        assert signal.setDataTypePolicy(policy) is signal
        assert signal.getDataTypePolicy() is policy
        signal.setDataTypePolicy(None)
        assert signal.getDataTypePolicy() is policy

    def test_get_set_init_value(self):
        signal = ISignal(None, "ISignal")

        value = TextValueSpecification()
        assert signal.setInitValue(value) is signal
        assert signal.getInitValue() is value
        signal.setInitValue(None)
        assert signal.getInitValue() is value

    def test_get_set_i_signal_props(self):
        signal = ISignal(None, "ISignal")

        props = ISignalProps()
        assert signal.setISignalProps(props) is signal
        assert signal.getISignalProps() is props
        signal.setISignalProps(None)
        assert signal.getISignalProps() is props

    def test_get_set_i_signal_type(self):
        signal = ISignal(None, "ISignal")

        signal_type = ISignalTypeEnum()
        signal_type.setValue(ISignalTypeEnum.PRIMITIVE)
        assert signal.setISignalType(signal_type) is signal
        assert signal.getISignalType() is signal_type
        signal.setISignalType(None)
        assert signal.getISignalType() is signal_type

    def test_get_set_length(self):
        signal = ISignal(None, "ISignal")

        length = UnlimitedInteger()
        length.setValue("8")
        assert signal.setLength(length) is signal
        assert signal.getLength() is length
        assert signal.getLength().getValue() == 8
        signal.setLength(None)
        assert signal.getLength() is length

    def test_get_set_network_representation_props(self):
        signal = ISignal(None, "ISignal")

        props = SwDataDefProps()
        assert signal.setNetworkRepresentationProps(props) is signal
        assert signal.getNetworkRepresentationProps() is props
        signal.setNetworkRepresentationProps(None)
        assert signal.getNetworkRepresentationProps() is props

    def test_get_set_system_signal_ref(self):
        signal = ISignal(None, "ISignal")

        ref = RefType()
        ref.setValue("/FibexCore/SystemSignal")
        assert signal.setSystemSignalRef(ref) is signal
        assert signal.getSystemSignalRef() is ref
        signal.setSystemSignalRef(None)
        assert signal.getSystemSignalRef() is ref

    def test_get_set_timeout_substitution_value(self):
        signal = ISignal(None, "ISignal")

        value = TextValueSpecification()
        assert signal.setTimeoutSubstitutionValue(value) is signal
        assert signal.getTimeoutSubstitutionValue() is value
        signal.setTimeoutSubstitutionValue(None)
        assert signal.getTimeoutSubstitutionValue() is value

    def test_add_get_transformation_i_signal_props(self):
        signal = ISignal(None, "ISignal")

        props = EndToEndTransformationISignalProps()
        assert signal.addTransformationISignalProps(props) is signal
        assert signal.getTransformationISignalProps() == [props]
        other = EndToEndTransformationISignalProps()
        signal.addTransformationISignalProps(other)
        assert signal.getTransformationISignalProps() == [props, other]
        signal.addTransformationISignalProps(None)
        assert signal.getTransformationISignalProps() == [props, other]

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ISignal.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        signal = ISignal(None, "ISignal")
        assert inspect.cleandoc(signal.getDataTransformationRef.__doc__) == DATA_TRANSFORMATION_REF_NOTE
        assert inspect.cleandoc(signal.setDataTransformationRef.__doc__).split("\n")[0] == DATA_TRANSFORMATION_REF_NOTE
        assert inspect.cleandoc(signal.getDataTypePolicy.__doc__) == DATA_TYPE_POLICY_NOTE
        assert inspect.cleandoc(signal.setDataTypePolicy.__doc__).split("\n")[0] == DATA_TYPE_POLICY_NOTE
        assert inspect.cleandoc(signal.getInitValue.__doc__) == INIT_VALUE_NOTE
        assert inspect.cleandoc(signal.setInitValue.__doc__).split("\n")[0] == INIT_VALUE_NOTE
        assert inspect.cleandoc(signal.getISignalProps.__doc__) == I_SIGNAL_PROPS_NOTE
        assert inspect.cleandoc(signal.setISignalProps.__doc__).split("\n")[0] == I_SIGNAL_PROPS_NOTE
        assert inspect.cleandoc(signal.getISignalType.__doc__) == I_SIGNAL_TYPE_NOTE
        assert inspect.cleandoc(signal.setISignalType.__doc__).split("\n")[0] == I_SIGNAL_TYPE_NOTE
        assert inspect.cleandoc(signal.getLength.__doc__) == LENGTH_NOTE
        assert inspect.cleandoc(signal.setLength.__doc__).split("\n")[0] == LENGTH_NOTE
        assert inspect.cleandoc(signal.getNetworkRepresentationProps.__doc__) == NETWORK_REPRESENTATION_PROPS_NOTE
        assert inspect.cleandoc(signal.setNetworkRepresentationProps.__doc__).split("\n")[0] == NETWORK_REPRESENTATION_PROPS_NOTE
        assert inspect.cleandoc(signal.getSystemSignalRef.__doc__) == SYSTEM_SIGNAL_REF_NOTE
        assert inspect.cleandoc(signal.setSystemSignalRef.__doc__).split("\n")[0] == SYSTEM_SIGNAL_REF_NOTE
        assert inspect.cleandoc(signal.getTimeoutSubstitutionValue.__doc__) == TIMEOUT_SUBSTITUTION_VALUE_NOTE
        assert inspect.cleandoc(signal.setTimeoutSubstitutionValue.__doc__).split("\n")[0] == TIMEOUT_SUBSTITUTION_VALUE_NOTE
        assert inspect.cleandoc(signal.addTransformationISignalProps.__doc__).split("\n")[0] == TRANSFORMATION_I_SIGNAL_PROPS_NOTE
        assert inspect.cleandoc(signal.getTransformationISignalProps.__doc__) == TRANSFORMATION_I_SIGNAL_PROPS_NOTE

    def test_init_has_no_docstring(self):
        assert ISignal.__init__.__doc__ is None
