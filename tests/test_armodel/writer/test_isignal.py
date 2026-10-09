"""Writer round-trip tests for ISignal (Table 6.7, p.321).

Serialized through the I-SIGNAL element; child order per the I-SIGNAL group of
AUTOSAR_00052.xsd (l.66683).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    NumericalValueSpecification,
    TextValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    PositiveInteger,
    RefType,
    UnlimitedInteger,
    VerbatimString,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import HandleOutOfRangeEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import DataTypePolicyEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ISignal,
    ISignalProps,
    ISignalTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    EndToEndTransformationISignalProps,
    SOMEIPTransformationISignalProps,
    UserDefinedTransformationISignalProps,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "DATA-TRANSFORMATIONS",
    "DATA-TYPE-POLICY",
    "I-SIGNAL-PROPS",
    "I-SIGNAL-TYPE",
    "INIT-VALUE",
    "LENGTH",
    "NETWORK-REPRESENTATION-PROPS",
    "SYSTEM-SIGNAL-REF",
    "TIMEOUT-SUBSTITUTION-VALUE",
    "TRANSFORMATION-I-SIGNAL-PROPSS",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _populate(signal: ISignal):
    signal.setDataTransformationRef(_ref("/AUTOSAR/DataTransformation", "DATA-TRANSFORMATION"))

    policy = DataTypePolicyEnum()
    policy.setValue(DataTypePolicyEnum.OVERRIDE)
    signal.setDataTypePolicy(policy)

    props = ISignalProps()
    handle = HandleOutOfRangeEnum()
    handle.setValue(HandleOutOfRangeEnum.SATURATE)
    props.setHandleOutOfRange(handle)
    signal.setISignalProps(props)

    signal_type = ISignalTypeEnum()
    signal_type.setValue(ISignalTypeEnum.ARRAY)
    signal.setISignalType(signal_type)

    init_value = TextValueSpecification()
    text = VerbatimString()
    text.setValue("42")
    init_value.setValue(text)
    signal.setInitValue(init_value)

    length = UnlimitedInteger()
    length.setValue("8")
    signal.setLength(length)

    network_props = SwDataDefProps()
    network_props.setBaseTypeRef(_ref("/AUTOSAR/BaseType/uint8", "SW-BASE-TYPE"))
    signal.setNetworkRepresentationProps(network_props)

    signal.setSystemSignalRef(_ref("/AUTOSAR/SystemSignal", "SYSTEM-SIGNAL"))

    timeout_value = NumericalValueSpecification()
    numerical = Numerical()
    numerical.setValue("3.5")
    timeout_value.setValue(numerical)
    signal.setTimeoutSubstitutionValue(timeout_value)

    e2e_props = EndToEndTransformationISignalProps()
    data_length = PositiveInteger()
    data_length.setValue("64")
    e2e_props.setDataLength(data_length)
    signal.addTransformationISignalProps(e2e_props)
    signal.addTransformationISignalProps(SOMEIPTransformationISignalProps())
    signal.addTransformationISignalProps(UserDefinedTransformationISignalProps())


class TestWriteISignal:
    def test_write_empty(self):
        signal = ISignal(None, "ISig1")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignal(parent, signal)

        node = parent.find("I-SIGNAL")
        assert node.find("DATA-TRANSFORMATIONS") is None
        assert node.find("DATA-TYPE-POLICY") is None
        assert node.find("I-SIGNAL-PROPS") is None
        assert node.find("I-SIGNAL-TYPE") is None
        assert node.find("INIT-VALUE") is None
        assert node.find("LENGTH") is None
        assert node.find("NETWORK-REPRESENTATION-PROPS") is None
        assert node.find("SYSTEM-SIGNAL-REF") is None
        assert node.find("TIMEOUT-SUBSTITUTION-VALUE") is None
        assert node.find("TRANSFORMATION-I-SIGNAL-PROPSS") is None

    def test_write_full_child_order_matches_xsd(self):
        signal = ISignal(None, "ISig1")
        _populate(signal)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignal(parent, signal)

        node = parent.find("I-SIGNAL")
        tags = [child.tag for child in node]
        assert [tag for tag in tags if tag in XSD_CHILD_ORDER] == XSD_CHILD_ORDER

    def test_write_full_field_values(self):
        signal = ISignal(None, "ISig1")
        _populate(signal)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignal(parent, signal)

        node = parent.find("I-SIGNAL")
        ref = node.find("DATA-TRANSFORMATIONS/DATA-TRANSFORMATION-REF-CONDITIONAL/DATA-TRANSFORMATION-REF")
        assert ref.text == "/AUTOSAR/DataTransformation"
        assert ref.get("DEST") == "DATA-TRANSFORMATION"
        assert node.find("DATA-TYPE-POLICY").text == "OVERRIDE"
        assert node.find("I-SIGNAL-PROPS/HANDLE-OUT-OF-RANGE").text == "SATURATE"
        assert node.find("I-SIGNAL-TYPE").text == "ARRAY"
        assert node.find("INIT-VALUE/TEXT-VALUE-SPECIFICATION/VALUE").text == "42"
        assert node.find("LENGTH").text == "8"
        assert node.find("NETWORK-REPRESENTATION-PROPS/SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL/BASE-TYPE-REF").text == "/AUTOSAR/BaseType/uint8"
        assert node.find("SYSTEM-SIGNAL-REF").text == "/AUTOSAR/SystemSignal"
        assert node.find("SYSTEM-SIGNAL-REF").get("DEST") == "SYSTEM-SIGNAL"
        assert node.find("TIMEOUT-SUBSTITUTION-VALUE/NUMERICAL-VALUE-SPECIFICATION/VALUE").text == "3.5"
        wrapper = node.find("TRANSFORMATION-I-SIGNAL-PROPSS")
        assert [child.tag for child in wrapper] == [
            "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS",
            "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS",
            "USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS",
        ]
        assert wrapper.find("END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS/END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS/END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL/DATA-LENGTH").text == "64"

    def test_round_trip_full(self):
        signal = ISignal(None, "ISig1")
        _populate(signal)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignal(parent, signal)

        reloaded = ISignal(None, "ISig1")
        ARXMLParser().readISignal(_with_ns(parent)[0], reloaded)

        assert reloaded.getShortName() == "ISig1"
        assert reloaded.getDataTransformationRef().getValue() == "/AUTOSAR/DataTransformation"
        assert reloaded.getDataTransformationRef().getDest() == "DATA-TRANSFORMATION"
        assert reloaded.getDataTypePolicy().value == "OVERRIDE"
        assert reloaded.getISignalProps().getHandleOutOfRange().value == "SATURATE"
        assert reloaded.getISignalType().value == "ARRAY"
        assert isinstance(reloaded.getInitValue(), TextValueSpecification)
        assert reloaded.getInitValue().getValue().getValue() == "42"
        assert reloaded.getLength().getValue() == 8
        assert reloaded.getNetworkRepresentationProps().getBaseTypeRef().getValue() == "/AUTOSAR/BaseType/uint8"
        assert reloaded.getSystemSignalRef().getValue() == "/AUTOSAR/SystemSignal"
        assert reloaded.getSystemSignalRef().getDest() == "SYSTEM-SIGNAL"
        assert isinstance(reloaded.getTimeoutSubstitutionValue(), NumericalValueSpecification)
        assert reloaded.getTimeoutSubstitutionValue().getValue().getValue() == 3.5

        props_list = reloaded.getTransformationISignalProps()
        assert len(props_list) == 3
        assert isinstance(props_list[0], EndToEndTransformationISignalProps)
        assert props_list[0].getDataLength().getValue() == 64
        assert isinstance(props_list[1], SOMEIPTransformationISignalProps)
        assert isinstance(props_list[2], UserDefinedTransformationISignalProps)

    def test_round_trip_empty(self):
        signal = ISignal(None, "ISig1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignal(parent, signal)

        reloaded = ISignal(None, "ISig1")
        ARXMLParser().readISignal(_with_ns(parent)[0], reloaded)

        assert reloaded.getDataTransformationRef() is None
        assert reloaded.getDataTypePolicy() is None
        assert reloaded.getISignalProps() is None
        assert reloaded.getISignalType() is None
        assert reloaded.getInitValue() is None
        assert reloaded.getLength() is None
        assert reloaded.getNetworkRepresentationProps() is None
        assert reloaded.getSystemSignalRef() is None
        assert reloaded.getTimeoutSubstitutionValue() is None
        assert reloaded.getTransformationISignalProps() == []
