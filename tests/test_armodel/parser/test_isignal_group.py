"""Parser tests for ISignalGroup (Table 6.12, p.324).

Child set and order per the I-SIGNAL-GROUP group of AUTOSAR_00052.xsd (l.66868).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalGroup
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    EndToEndTransformationISignalProps,
    SOMEIPTransformationISignalProps,
    UserDefinedTransformationISignalProps,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_XML = f"""<I-SIGNAL-GROUP xmlns='{NS}'>
    <SHORT-NAME>ISigGroup1</SHORT-NAME>
    <COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS>
        <DATA-TRANSFORMATION-REF-CONDITIONAL>
            <DATA-TRANSFORMATION-REF DEST='DATA-TRANSFORMATION'>/AUTOSAR/DataTransformation</DATA-TRANSFORMATION-REF>
        </DATA-TRANSFORMATION-REF-CONDITIONAL>
    </COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS>
    <I-SIGNAL-REFS>
        <I-SIGNAL-REF DEST='I-SIGNAL'>/AUTOSAR/ISignal1</I-SIGNAL-REF>
        <I-SIGNAL-REF DEST='I-SIGNAL'>/AUTOSAR/ISignal2</I-SIGNAL-REF>
    </I-SIGNAL-REFS>
    <SYSTEM-SIGNAL-GROUP-REF DEST='SYSTEM-SIGNAL-GROUP'>/AUTOSAR/SystemSignalGroup</SYSTEM-SIGNAL-GROUP-REF>
    <TRANSFORMATION-I-SIGNAL-PROPSS>
        <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS>
            <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
                <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
                    <DATA-LENGTH>64</DATA-LENGTH>
                </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
            </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
        </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS>
        <SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS/>
        <USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS/>
    </TRANSFORMATION-I-SIGNAL-PROPSS>
</I-SIGNAL-GROUP>"""


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadISignalGroup:
    def test_read_full(self):
        group = ISignalGroup(None, "ISigGroup1")
        ARXMLParser().readISignalGroup(ET.fromstring(FULL_XML), group)

        assert group.getShortName() == "ISigGroup1"
        assert group.getComBasedSignalGroupTransformationRef().getValue() == "/AUTOSAR/DataTransformation"
        assert group.getComBasedSignalGroupTransformationRef().getDest() == "DATA-TRANSFORMATION"

        signal_refs = group.getISignalRefs()
        assert len(signal_refs) == 2
        assert signal_refs[0].getValue() == "/AUTOSAR/ISignal1"
        assert signal_refs[0].getDest() == "I-SIGNAL"
        assert signal_refs[1].getValue() == "/AUTOSAR/ISignal2"
        assert signal_refs[1].getDest() == "I-SIGNAL"

        assert group.getSystemSignalGroupRef().getValue() == "/AUTOSAR/SystemSignalGroup"
        assert group.getSystemSignalGroupRef().getDest() == "SYSTEM-SIGNAL-GROUP"

        props_list = group.getTransformationISignalProps()
        assert len(props_list) == 3
        assert isinstance(props_list[0], EndToEndTransformationISignalProps)
        assert props_list[0].getDataLength().getValue() == 64
        assert isinstance(props_list[1], SOMEIPTransformationISignalProps)
        assert isinstance(props_list[2], UserDefinedTransformationISignalProps)

    def test_read_minimal(self):
        group = ISignalGroup(None, "ISigGroup1")
        element = ET.fromstring(f"<I-SIGNAL-GROUP xmlns='{NS}'><SHORT-NAME>ISigGroup1</SHORT-NAME></I-SIGNAL-GROUP>")
        ARXMLParser().readISignalGroup(element, group)

        assert group.getShortName() == "ISigGroup1"
        assert group.getComBasedSignalGroupTransformationRef() is None
        assert group.getISignalRefs() == []
        assert group.getSystemSignalGroupRef() is None
        assert group.getTransformationISignalProps() == []

    def test_read_empty_wrapper_lists(self):
        group = ISignalGroup(None, "ISigGroup1")
        element = ET.fromstring(
            f"<I-SIGNAL-GROUP xmlns='{NS}'>"
            "<SHORT-NAME>ISigGroup1</SHORT-NAME>"
            "<COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS/>"
            "<I-SIGNAL-REFS/>"
            "<TRANSFORMATION-I-SIGNAL-PROPSS/>"
            "</I-SIGNAL-GROUP>"
        )
        ARXMLParser().readISignalGroup(element, group)

        assert group.getComBasedSignalGroupTransformationRef() is None
        assert group.getISignalRefs() == []
        assert group.getSystemSignalGroupRef() is None
        assert group.getTransformationISignalProps() == []
