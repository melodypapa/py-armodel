"""Writer round-trip tests for EndToEndProtectionISignalIPdu (Table 6.56, p.385).

Element order per XSD group END-TO-END-PROTECTION-I-SIGNAL-I-PDU
(AUTOSAR_00052.xsd l.54301): DATA-OFFSET, I-SIGNAL-GROUP-REF,
I-SIGNAL-I-PDU-REF, then VARIATION-POINT (sequenceOffset 10000).
Aggregated through the END-TO-END-PROTECTION-I-SIGNAL-I-PDUS wrapper,
emitted only when non-empty.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndProtection
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.EndToEndProtection import EndToEndProtectionISignalIPdu
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _int(value):
    integer = Integer()
    integer.setValue(str(value))
    return integer


def _new_ipdu():
    ipdu = EndToEndProtectionISignalIPdu()
    ipdu.setDataOffset(_int(16))
    ipdu.setISignalGroupRef(_ref("/ISignalGroups/Protected", "I-SIGNAL-GROUP"))
    ipdu.setISignalIPduRef(_ref("/IPdus/Carrier", "I-SIGNAL-I-PDU"))
    return ipdu


def _with_ns(element: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(element).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteEndToEndProtectionISignalIPdu:
    def test_none(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeEndToEndProtectionISignalIPdu(parent, None)
        assert len(parent) == 0

    def test_empty(self):
        ipdu = EndToEndProtectionISignalIPdu()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeEndToEndProtectionISignalIPdu(parent, ipdu)

        node = parent.find("END-TO-END-PROTECTION-I-SIGNAL-I-PDU")
        assert node is not None
        assert node.find("DATA-OFFSET") is None
        assert node.find("I-SIGNAL-GROUP-REF") is None
        assert node.find("I-SIGNAL-I-PDU-REF") is None
        assert node.find("VARIATION-POINT") is None

    def test_full_element_order_and_values(self):
        ipdu = _new_ipdu()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeEndToEndProtectionISignalIPdu(parent, ipdu)

        node = parent.find("END-TO-END-PROTECTION-I-SIGNAL-I-PDU")
        assert node is not None
        tags = [child.tag for child in node]
        assert tags == ["DATA-OFFSET", "I-SIGNAL-GROUP-REF", "I-SIGNAL-I-PDU-REF"]

        assert node.find("DATA-OFFSET").text == "16"
        assert node.find("I-SIGNAL-GROUP-REF").text == "/ISignalGroups/Protected"
        assert node.find("I-SIGNAL-GROUP-REF").attrib["DEST"] == "I-SIGNAL-GROUP"
        assert node.find("I-SIGNAL-I-PDU-REF").text == "/IPdus/Carrier"
        assert node.find("I-SIGNAL-I-PDU-REF").attrib["DEST"] == "I-SIGNAL-I-PDU"

    def test_round_trip(self):
        ipdu = _new_ipdu()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeEndToEndProtectionISignalIPdu(parent, ipdu)

        reloaded = EndToEndProtectionISignalIPdu()
        ARXMLParser().readEndToEndProtectionISignalIPdu(_with_ns(parent)[0], reloaded)

        assert reloaded.getDataOffset().getValue() == 16
        assert reloaded.getISignalGroupRef().getValue() == "/ISignalGroups/Protected"
        assert reloaded.getISignalGroupRef().getDest() == "I-SIGNAL-GROUP"
        assert reloaded.getISignalIPduRef().getValue() == "/IPdus/Carrier"
        assert reloaded.getISignalIPduRef().getDest() == "I-SIGNAL-I-PDU"


class TestWriteEndToEndProtectionEndToEndProtectionISignalIPdus:
    def test_empty_list_omits_wrapper(self):
        protection = EndToEndProtection(MockParent(), "Protection")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeEndToEndProtectionEndToEndProtectionISignalIPdus(parent, protection)
        assert len(parent) == 0
        assert parent.find("END-TO-END-PROTECTION-I-SIGNAL-I-PDUS") is None

    def test_full_round_trip_via_wrapper(self):
        protection = EndToEndProtection(MockParent(), "Protection")
        protection.addEndToEndProtectionISignalIPdu(_new_ipdu())
        second = EndToEndProtectionISignalIPdu()
        second.setDataOffset(_int(32))
        protection.addEndToEndProtectionISignalIPdu(second)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEndToEndProtectionEndToEndProtectionISignalIPdus(parent, protection)

        wrapper = parent.find("END-TO-END-PROTECTION-I-SIGNAL-I-PDUS")
        assert wrapper is not None
        nodes = wrapper.findall("END-TO-END-PROTECTION-I-SIGNAL-I-PDU")
        assert len(nodes) == 2
        assert nodes[0].find("DATA-OFFSET").text == "16"
        assert nodes[1].find("DATA-OFFSET").text == "32"

        reloaded = EndToEndProtection(MockParent(), "Protection")
        ARXMLParser().readEndToEndProtectionEndToEndProtectionISignalIPdus(_with_ns(parent), reloaded)
        ipdus = reloaded.getEndToEndProtectionISignalIPdus()
        assert len(ipdus) == 2
        assert ipdus[0].getDataOffset().getValue() == 16
        assert ipdus[0].getISignalGroupRef().getValue() == "/ISignalGroups/Protected"
        assert ipdus[0].getISignalIPduRef().getValue() == "/IPdus/Carrier"
        assert ipdus[1].getDataOffset().getValue() == 32
        assert ipdus[1].getISignalGroupRef() is None
