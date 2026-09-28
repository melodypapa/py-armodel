"""Writer round-trip tests for ISignalMapping (AUTOSAR_CP_TPS_SystemTemplate Table 8.7, p.846).

Element order per XSD group I-SIGNAL-MAPPING (00052.xsd L67213): INTRODUCTION,
SOURCE-SIGNAL-REF, TARGET-SIGNAL-REF; complexType = AR-OBJECT group + own group.
Aggregated by Gateway.signalMapping via the SIGNAL-MAPPINGS wrapper (GATEWAY group
order: ECU-REF, FRAME-MAPPINGS, I-PDU-MAPPINGS, SIGNAL-MAPPINGS).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import Gateway, IPduMapping, ISignalMapping
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


def _introduction(text="Signal mapping intro"):
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
    ref.setDest("I-SIGNAL-TRIGGERING")
    ref.setValue(value)
    return ref


def _mapping(source=None, target=None, with_introduction=False):
    mapping = ISignalMapping()
    if with_introduction:
        mapping.setIntroduction(_introduction())
    if source is not None:
        mapping.setSourceSignalRef(_ref(source))
    if target is not None:
        mapping.setTargetSignalRef(_ref(target))
    return mapping


class TestWriteISignalMapping:
    def test_write_content_in_xsd_order(self):
        element = ET.Element("I-SIGNAL-MAPPING")
        ARXMLWriter().writeISignalMapping(element, _mapping("/CanCluster/SignalTriggering_A", "/CanCluster/SignalTriggering_B", with_introduction=True))

        children = [child.tag for child in element]
        assert children == ["INTRODUCTION", "SOURCE-SIGNAL-REF", "TARGET-SIGNAL-REF"]
        assert element.find("SOURCE-SIGNAL-REF").text == "/CanCluster/SignalTriggering_A"
        assert element.find("SOURCE-SIGNAL-REF").attrib["DEST"] == "I-SIGNAL-TRIGGERING"
        assert element.find("TARGET-SIGNAL-REF").text == "/CanCluster/SignalTriggering_B"

    def test_write_omits_absent_elements(self):
        element = ET.Element("I-SIGNAL-MAPPING")
        ARXMLWriter().writeISignalMapping(element, _mapping())

        assert len(list(element)) == 0

    def test_write_partial_element(self):
        element = ET.Element("I-SIGNAL-MAPPING")
        ARXMLWriter().writeISignalMapping(element, _mapping(target="/Cluster/T"))

        assert element.find("INTRODUCTION") is None
        assert element.find("SOURCE-SIGNAL-REF") is None
        assert element.find("TARGET-SIGNAL-REF").text == "/Cluster/T"

    def test_set_i_signal_mappings_wrapper_and_empty_omission(self):
        writer = ARXMLWriter()
        gateway_element = ET.Element("GATEWAY")
        writer.setISignalMappings(gateway_element, [])
        assert gateway_element.find("SIGNAL-MAPPINGS") is None

        writer.setISignalMappings(gateway_element, [_mapping("/C/S", "/C/T")])
        mappings = gateway_element.findall("SIGNAL-MAPPINGS/I-SIGNAL-MAPPING")
        assert len(mappings) == 1
        assert mappings[0].find("SOURCE-SIGNAL-REF").text == "/C/S"

    def test_gateway_dispatch_writes_signal_mappings_last(self):
        gateway = Gateway(None, "Gateway")
        ecu_ref = RefType()
        ecu_ref.setDest("ECU-INSTANCE")
        ecu_ref.setValue("/Ecu/Ecu_A")
        gateway.setEcuRef(ecu_ref)
        gateway.addIPduMapping(IPduMapping())
        gateway.addSignalMapping(_mapping("/C/S", "/C/T"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeGateway(parent, gateway)

        node = parent.find("GATEWAY")
        children = [child.tag for child in node]
        assert children.index("ECU-REF") < children.index("I-PDU-MAPPINGS") < children.index("SIGNAL-MAPPINGS")

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalMapping(parent, _mapping("/C/S", "/C/T", with_introduction=True))
        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        parser = ARXMLParser()
        mapping = ISignalMapping()
        parser.readISignalMapping(reparsed, mapping)

        assert mapping.getSourceSignalRef().getValue() == "/C/S"
        assert mapping.getSourceSignalRef().getDest() == "I-SIGNAL-TRIGGERING"
        assert mapping.getTargetSignalRef().getValue() == "/C/T"
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
        ARXMLWriter().writeISignalMapping(parent, mapping)
        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        parsed = ISignalMapping()
        ARXMLParser().readISignalMapping(reparsed, parsed)

        assert parsed.getVariationPoint().getShortLabel().getValue() == "vp1"
