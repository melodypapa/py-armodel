"""Writer round-trip tests for FrameMapping (AUTOSAR_CP_TPS_SystemTemplate Table 8.2, p.838).

Element order per XSD group FRAME-MAPPING (00052.xsd L63012): INTRODUCTION,
SOURCE-FRAME-REF, TARGET-FRAME-REF; complexType = AR-OBJECT group + own group.
Aggregated by Gateway.frameMapping via the FRAME-MAPPINGS wrapper (GATEWAY group
order: ECU-REF, FRAME-MAPPINGS, I-PDU-MAPPINGS, SIGNAL-MAPPINGS).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import FrameMapping
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _introduction(text="Frame mapping intro"):
    paragraph = MultiLanguageParagraph()
    l1 = LParagraph()
    l1.setL("EN")
    l1.setValue(text)
    paragraph.addL1(l1)
    block = DocumentationBlock()
    block.addP(paragraph)
    return block


def _ref(value):
    ref = RefType()
    ref.setDest("FRAME-TRIGGERING")
    ref.setValue(value)
    return ref


def _mapping(source=None, target=None, with_introduction=False):
    mapping = FrameMapping()
    if with_introduction:
        mapping.setIntroduction(_introduction())
    if source is not None:
        mapping.setSourceFrameRef(_ref(source))
    if target is not None:
        mapping.setTargetFrameRef(_ref(target))
    return mapping


class TestWriteFrameMapping:
    def test_write_content_in_xsd_order(self):
        element = ET.Element("FRAME-MAPPING")
        ARXMLWriter().writeFrameMapping(element, _mapping("/CanCluster/FrameTriggering_A", "/CanCluster/FrameTriggering_B", with_introduction=True))

        children = [child.tag for child in element]
        assert children == ["INTRODUCTION", "SOURCE-FRAME-REF", "TARGET-FRAME-REF"]
        assert element.find("SOURCE-FRAME-REF").text == "/CanCluster/FrameTriggering_A"
        assert element.find("SOURCE-FRAME-REF").attrib["DEST"] == "FRAME-TRIGGERING"
        assert element.find("TARGET-FRAME-REF").text == "/CanCluster/FrameTriggering_B"

    def test_write_omits_absent_elements(self):
        element = ET.Element("FRAME-MAPPING")
        ARXMLWriter().writeFrameMapping(element, _mapping())

        assert len(list(element)) == 0

    def test_write_partial_element(self):
        element = ET.Element("FRAME-MAPPING")
        ARXMLWriter().writeFrameMapping(element, _mapping(target="/Cluster/T"))

        assert element.find("INTRODUCTION") is None
        assert element.find("SOURCE-FRAME-REF") is None
        assert element.find("TARGET-FRAME-REF").text == "/Cluster/T"

    def test_set_frame_mappings_wrapper_and_empty_omission(self):
        writer = ARXMLWriter()
        gateway_element = ET.Element("GATEWAY")
        writer.setFrameMappings(gateway_element, [])
        assert gateway_element.find("FRAME-MAPPINGS") is None

        writer.setFrameMappings(gateway_element, [_mapping("/C/S", "/C/T")])
        mappings = gateway_element.findall("FRAME-MAPPINGS/FRAME-MAPPING")
        assert len(mappings) == 1
        assert mappings[0].find("SOURCE-FRAME-REF").text == "/C/S"

    def test_gateway_dispatch_writes_frame_mappings_between_ecu_ref_and_ipdu_mappings(self):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import Gateway, IPduMapping

        gateway = Gateway(None, "Gateway")
        ecu_ref = RefType()
        ecu_ref.setDest("ECU-INSTANCE")
        ecu_ref.setValue("/Ecu/Ecu_A")
        gateway.setEcuRef(ecu_ref)
        gateway.addFrameMapping(_mapping("/C/S", "/C/T"))
        gateway.addIPduMapping(IPduMapping())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeGateway(parent, gateway)

        node = parent.find("GATEWAY")
        children = [child.tag for child in node]
        assert children.index("ECU-REF") < children.index("FRAME-MAPPINGS") < children.index("I-PDU-MAPPINGS")

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeFrameMapping(parent, _mapping("/C/S", "/C/T", with_introduction=True))
        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        parser = ARXMLParser()
        mapping = FrameMapping()
        parser.readFrameMapping(reparsed, mapping)

        assert mapping.getSourceFrameRef().getValue() == "/C/S"
        assert mapping.getTargetFrameRef().getValue() == "/C/T"
        introduction = mapping.getIntroduction()
        assert introduction is not None
        paragraphs = introduction.getPs()
        assert len(paragraphs) == 1

    def test_round_trip_variation_point(self):
        mapping = _mapping("/C/S", "/C/T")
        variation_point = VariationPoint()
        short_label = ARLiteral()
        short_label.setValue("vp1")
        variation_point.setShortLabel(short_label)
        mapping.setVariationPoint(variation_point)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeFrameMapping(parent, mapping)
        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        parsed = FrameMapping()
        ARXMLParser().readFrameMapping(reparsed, parsed)

        assert parsed.getVariationPoint().getShortLabel().getValue() == "vp1"
