"""Parser tests for EndToEndProtectionISignalIPdu (Table 6.56, p.385).

ARObject-based (no SHORT-NAME of its own) aggregated by
EndToEndProtection.endToEndProtectionISignalIPdu through the
END-TO-END-PROTECTION-I-SIGNAL-I-PDUS wrapper (XSD group
END-TO-END-PROTECTION-I-SIGNAL-I-PDU, AUTOSAR_00052.xsd l.54301):
DATA-OFFSET, I-SIGNAL-GROUP-REF, I-SIGNAL-I-PDU-REF, then VARIATION-POINT
(sequenceOffset 10000).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndProtection
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.EndToEndProtection import EndToEndProtectionISignalIPdu
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    xml = "<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner)
    return ET.fromstring(xml)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


IPDU_XML = (
    "<END-TO-END-PROTECTION-I-SIGNAL-I-PDU>"
    "<DATA-OFFSET>16</DATA-OFFSET>"
    '<I-SIGNAL-GROUP-REF DEST="I-SIGNAL-GROUP">/ISignalGroups/Protected</I-SIGNAL-GROUP-REF>'
    '<I-SIGNAL-I-PDU-REF DEST="I-SIGNAL-I-PDU">/IPdus/Carrier</I-SIGNAL-I-PDU-REF>'
    "<VARIATION-POINT />"
    "</END-TO-END-PROTECTION-I-SIGNAL-I-PDU>"
)


class TestReadEndToEndProtectionISignalIPdu:
    def test_read_full(self):
        ipdu = EndToEndProtectionISignalIPdu()
        root = _snip(IPDU_XML)
        ARXMLParser().readEndToEndProtectionISignalIPdu(root[0], ipdu)

        assert ipdu.getDataOffset() is not None
        assert ipdu.getDataOffset().getValue() == 16

        group_ref = ipdu.getISignalGroupRef()
        assert group_ref.getValue() == "/ISignalGroups/Protected"
        assert group_ref.getDest() == "I-SIGNAL-GROUP"

        pdu_ref = ipdu.getISignalIPduRef()
        assert pdu_ref.getValue() == "/IPdus/Carrier"
        assert pdu_ref.getDest() == "I-SIGNAL-I-PDU"

        assert ipdu.getVariationPoint() is not None

    def test_read_empty(self):
        ipdu = EndToEndProtectionISignalIPdu()
        root = _snip("<END-TO-END-PROTECTION-I-SIGNAL-I-PDU />")
        ARXMLParser().readEndToEndProtectionISignalIPdu(root[0], ipdu)

        assert ipdu.getDataOffset() is None
        assert ipdu.getISignalGroupRef() is None
        assert ipdu.getISignalIPduRef() is None
        assert ipdu.getVariationPoint() is None


class TestReadEndToEndProtectionEndToEndProtectionISignalIPdus:
    def test_read_multiple(self):
        protection = EndToEndProtection(MockParent(), "Protection")
        root = _snip(
            "<END-TO-END-PROTECTION-I-SIGNAL-I-PDUS>"
            "<END-TO-END-PROTECTION-I-SIGNAL-I-PDU>"
            "<DATA-OFFSET>16</DATA-OFFSET>"
            "</END-TO-END-PROTECTION-I-SIGNAL-I-PDU>"
            "<END-TO-END-PROTECTION-I-SIGNAL-I-PDU>"
            "<DATA-OFFSET>32</DATA-OFFSET>"
            "</END-TO-END-PROTECTION-I-SIGNAL-I-PDU>"
            "</END-TO-END-PROTECTION-I-SIGNAL-I-PDUS>"
        )
        ARXMLParser().readEndToEndProtectionEndToEndProtectionISignalIPdus(root, protection)

        ipdus = protection.getEndToEndProtectionISignalIPdus()
        assert len(ipdus) == 2
        assert ipdus[0].getDataOffset().getValue() == 16
        assert ipdus[1].getDataOffset().getValue() == 32

    def test_read_empty_wrapper(self):
        protection = EndToEndProtection(MockParent(), "Protection")
        root = _snip("<END-TO-END-PROTECTION-I-SIGNAL-I-PDUS />")
        ARXMLParser().readEndToEndProtectionEndToEndProtectionISignalIPdus(root, protection)

        assert protection.getEndToEndProtectionISignalIPdus() == []
