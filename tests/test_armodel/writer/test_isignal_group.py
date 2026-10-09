"""Writer round-trip tests for ISignalGroup (Table 6.12, p.324).

Serialized through the I-SIGNAL-GROUP element; child order per the I-SIGNAL-GROUP
group of AUTOSAR_00052.xsd (l.66868).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalGroup
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    EndToEndTransformationISignalProps,
    SOMEIPTransformationISignalProps,
    UserDefinedTransformationISignalProps,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS",
    "I-SIGNAL-REFS",
    "SYSTEM-SIGNAL-GROUP-REF",
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


def _populate(group: ISignalGroup):
    group.setComBasedSignalGroupTransformationRef(_ref("/AUTOSAR/DataTransformation", "DATA-TRANSFORMATION"))
    group.addISignalRef(_ref("/AUTOSAR/ISignal1", "I-SIGNAL"))
    group.addISignalRef(_ref("/AUTOSAR/ISignal2", "I-SIGNAL"))
    group.setSystemSignalGroupRef(_ref("/AUTOSAR/SystemSignalGroup", "SYSTEM-SIGNAL-GROUP"))

    e2e_props = EndToEndTransformationISignalProps()
    data_length = PositiveInteger()
    data_length.setValue("64")
    e2e_props.setDataLength(data_length)
    group.addTransformationISignalProps(e2e_props)
    group.addTransformationISignalProps(SOMEIPTransformationISignalProps())
    group.addTransformationISignalProps(UserDefinedTransformationISignalProps())


class TestWriteISignalGroup:
    def test_write_empty(self):
        group = ISignalGroup(None, "ISigGroup1")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalGroup(parent, group)

        node = parent.find("I-SIGNAL-GROUP")
        assert node.find("COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS") is None
        assert node.find("I-SIGNAL-REFS") is None
        assert node.find("SYSTEM-SIGNAL-GROUP-REF") is None
        assert node.find("TRANSFORMATION-I-SIGNAL-PROPSS") is None

    def test_write_full_child_order_matches_xsd(self):
        group = ISignalGroup(None, "ISigGroup1")
        _populate(group)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalGroup(parent, group)

        node = parent.find("I-SIGNAL-GROUP")
        tags = [child.tag for child in node]
        assert [tag for tag in tags if tag in XSD_CHILD_ORDER] == XSD_CHILD_ORDER

    def test_write_full_field_values(self):
        group = ISignalGroup(None, "ISigGroup1")
        _populate(group)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalGroup(parent, group)

        node = parent.find("I-SIGNAL-GROUP")
        ref = node.find("COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS/DATA-TRANSFORMATION-REF-CONDITIONAL/DATA-TRANSFORMATION-REF")
        assert ref.text == "/AUTOSAR/DataTransformation"
        assert ref.get("DEST") == "DATA-TRANSFORMATION"

        signal_refs = node.findall("I-SIGNAL-REFS/I-SIGNAL-REF")
        assert len(signal_refs) == 2
        assert signal_refs[0].text == "/AUTOSAR/ISignal1"
        assert signal_refs[0].get("DEST") == "I-SIGNAL"
        assert signal_refs[1].text == "/AUTOSAR/ISignal2"
        assert signal_refs[1].get("DEST") == "I-SIGNAL"

        assert node.find("SYSTEM-SIGNAL-GROUP-REF").text == "/AUTOSAR/SystemSignalGroup"
        assert node.find("SYSTEM-SIGNAL-GROUP-REF").get("DEST") == "SYSTEM-SIGNAL-GROUP"

        wrapper = node.find("TRANSFORMATION-I-SIGNAL-PROPSS")
        assert [child.tag for child in wrapper] == [
            "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS",
            "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS",
            "USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS",
        ]
        assert wrapper.find("END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS/END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS/END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL/DATA-LENGTH").text == "64"

    def test_round_trip_full(self):
        group = ISignalGroup(None, "ISigGroup1")
        _populate(group)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalGroup(parent, group)

        reloaded = ISignalGroup(None, "ISigGroup1")
        ARXMLParser().readISignalGroup(_with_ns(parent)[0], reloaded)

        assert reloaded.getShortName() == "ISigGroup1"
        assert reloaded.getComBasedSignalGroupTransformationRef().getValue() == "/AUTOSAR/DataTransformation"
        assert reloaded.getComBasedSignalGroupTransformationRef().getDest() == "DATA-TRANSFORMATION"

        signal_refs = reloaded.getISignalRefs()
        assert len(signal_refs) == 2
        assert signal_refs[0].getValue() == "/AUTOSAR/ISignal1"
        assert signal_refs[0].getDest() == "I-SIGNAL"
        assert signal_refs[1].getValue() == "/AUTOSAR/ISignal2"
        assert signal_refs[1].getDest() == "I-SIGNAL"

        assert reloaded.getSystemSignalGroupRef().getValue() == "/AUTOSAR/SystemSignalGroup"
        assert reloaded.getSystemSignalGroupRef().getDest() == "SYSTEM-SIGNAL-GROUP"

        props_list = reloaded.getTransformationISignalProps()
        assert len(props_list) == 3
        assert isinstance(props_list[0], EndToEndTransformationISignalProps)
        assert props_list[0].getDataLength().getValue() == 64
        assert isinstance(props_list[1], SOMEIPTransformationISignalProps)
        assert isinstance(props_list[2], UserDefinedTransformationISignalProps)

    def test_round_trip_empty(self):
        group = ISignalGroup(None, "ISigGroup1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalGroup(parent, group)

        reloaded = ISignalGroup(None, "ISigGroup1")
        ARXMLParser().readISignalGroup(_with_ns(parent)[0], reloaded)

        assert reloaded.getComBasedSignalGroupTransformationRef() is None
        assert reloaded.getISignalRefs() == []
        assert reloaded.getSystemSignalGroupRef() is None
        assert reloaded.getTransformationISignalProps() == []
