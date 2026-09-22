"""Parser tests for IPduMapping (Table 8.3, p.840).

Element order per XSD group I-PDU-MAPPING: INTRODUCTION, PDU-MAX-LENGTH,
PDUR-TP-CHUNK-SIZE, SOURCE-I-PDU-REF, TARGET-I-PDU, VARIATION-POINT.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import IPduMapping, TargetIPduRef
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))


IPDU_MAPPING_XML = (
    "<I-PDU-MAPPINGS>"
    "<I-PDU-MAPPING>"
    '<INTRODUCTION><P><L-1 L="EN">Introductory documentation about the mapping.</L-1></P></INTRODUCTION>'
    "<PDU-MAX-LENGTH>1500</PDU-MAX-LENGTH>"
    "<PDUR-TP-CHUNK-SIZE>64</PDUR-TP-CHUNK-SIZE>"
    '<SOURCE-I-PDU-REF DEST="PDU-TRIGGERING">/Cluster/PT_Source</SOURCE-I-PDU-REF>'
    "<TARGET-I-PDU>"
    '<TARGET-I-PDU-REF DEST="PDU-TRIGGERING">/Cluster/PT_Target</TARGET-I-PDU-REF>'
    "</TARGET-I-PDU>"
    "</I-PDU-MAPPING>"
    "</I-PDU-MAPPINGS>"
)


class TestReadIPduMapping:
    def test_read_field_values(self):
        root = _snip(IPDU_MAPPING_XML)
        mappings = ARXMLParser().getIPduMappings(root)

        assert len(mappings) == 1
        mapping = mappings[0]
        assert isinstance(mapping, IPduMapping)

        introduction = mapping.getIntroduction()
        assert introduction is not None
        assert introduction.getPs()[0].getL1s()[0].getValue() == "Introductory documentation about the mapping."

        assert mapping.getPduMaxLength().getValue() == 1500
        assert mapping.getPdurTpChunkSize().getValue() == 64
        assert mapping.getSourceIPduRef().getValue() == "/Cluster/PT_Source"
        assert mapping.getSourceIPduRef().getDest() == "PDU-TRIGGERING"

        target = mapping.getTargetIPdu()
        assert isinstance(target, TargetIPduRef)
        assert target.getTargetIPduRef().getValue() == "/Cluster/PT_Target"
        assert target.getTargetIPduRef().getDest() == "PDU-TRIGGERING"

    def test_read_minimal_mapping(self):
        root = _snip("<I-PDU-MAPPINGS><I-PDU-MAPPING>" '<SOURCE-I-PDU-REF DEST="PDU-TRIGGERING">/Cluster/PT_Source</SOURCE-I-PDU-REF>' "</I-PDU-MAPPING></I-PDU-MAPPINGS>")
        mappings = ARXMLParser().getIPduMappings(root)

        assert len(mappings) == 1
        mapping = mappings[0]
        assert mapping.getIntroduction() is None
        assert mapping.getPduMaxLength() is None
        assert mapping.getPdurTpChunkSize() is None
        assert mapping.getTargetIPdu() is None
        assert mapping.getSourceIPduRef().getValue() == "/Cluster/PT_Source"
