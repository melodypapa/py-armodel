"""Writer round-trip tests for IPduMapping (Table 8.3, p.840).

Element order per XSD group I-PDU-MAPPING: INTRODUCTION, PDU-MAX-LENGTH,
PDUR-TP-CHUNK-SIZE, SOURCE-I-PDU-REF, TARGET-I-PDU, VARIATION-POINT.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import IPduMapping, TargetIPduRef
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _posint(value):
    number = PositiveInteger()
    number.setValue(value)
    return number


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _new_mapping():
    mapping = IPduMapping()

    block = DocumentationBlock()
    block.addP(_paragraph())
    mapping.setIntroduction(block)

    mapping.setPduMaxLength(_posint(1500))
    mapping.setPdurTpChunkSize(_posint(64))
    mapping.setSourceIPduRef(_ref("/Cluster/PT_Source", "PDU-TRIGGERING"))

    target = TargetIPduRef()
    target.setTargetIPduRef(_ref("/Cluster/PT_Target", "PDU-TRIGGERING"))
    mapping.setTargetIPdu(target)
    return mapping


def _paragraph():
    from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
    from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph

    paragraph = MultiLanguageParagraph()
    l_paragraph = LParagraph()
    l_paragraph.setValue("Introductory documentation about the mapping.")
    l_paragraph.setL("EN")
    paragraph.addL1(l_paragraph)
    return paragraph


class TestWriteIPduMapping:
    def test_write_content_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setIPduMappings(parent, [_new_mapping()])
        mappings_tag = parent.find("I-PDU-MAPPINGS")
        assert mappings_tag is not None
        node = mappings_tag.find("I-PDU-MAPPING")
        children = [child.tag for child in node]
        assert children == ["INTRODUCTION", "PDU-MAX-LENGTH", "PDUR-TP-CHUNK-SIZE", "SOURCE-I-PDU-REF", "TARGET-I-PDU"]
        assert node.find("PDU-MAX-LENGTH").text == "1500"
        assert node.find("PDUR-TP-CHUNK-SIZE").text == "64"
        source_ref = node.find("SOURCE-I-PDU-REF")
        assert source_ref.text == "/Cluster/PT_Source"
        assert source_ref.attrib["DEST"] == "PDU-TRIGGERING"
        assert node.find("TARGET-I-PDU/TARGET-I-PDU-REF").text == "/Cluster/PT_Target"

    def test_write_empty_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setIPduMappings(parent, [])
        assert len(list(parent)) == 0

    def test_round_trip_preserves_all_values(self):
        mapping = _new_mapping()
        parent = ET.Element("PARENT")
        ARXMLWriter().setIPduMappings(parent, [mapping])
        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        mappings = ARXMLParser().getIPduMappings(reparsed)

        assert len(mappings) == 1
        parsed = mappings[0]
        assert parsed.getPduMaxLength().getValue() == 1500
        assert parsed.getPdurTpChunkSize().getValue() == 64
        assert parsed.getSourceIPduRef().getValue() == "/Cluster/PT_Source"
        assert parsed.getSourceIPduRef().getDest() == "PDU-TRIGGERING"
        assert parsed.getTargetIPdu().getTargetIPduRef().getValue() == "/Cluster/PT_Target"
        assert parsed.getIntroduction() is not None
        assert parsed.getIntroduction().getPs()[0].getL1s()[0].getValue() == "Introductory documentation about the mapping."
