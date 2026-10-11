"""Writer tests for the Topic1 class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.73)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.MSR.Documentation.Chapters import Topic1, TopicContent, TopicContentOrMsrQuery
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _parent():
    return AUTOSAR.getInstance().createARPackage("AUTOSAR")


def _full_topic() -> Topic1:
    topic = Topic1(_parent(), "TopicA")
    topic.setHelpEntry(String().setValue("topic.help.entry"))
    topic.setTopicContent(TopicContentOrMsrQuery().setTopicContent(TopicContent()))
    topic.setVariationPoint(VariationPoint())
    return topic


def _reparse(element: ET.Element) -> Topic1:
    element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
    parsed = ET.fromstring(ET.tostring(element, encoding="unicode"))
    topic_element = parsed[0]
    assert topic_element.tag.endswith("TOPIC-1")
    return ARXMLParser().readTopic1(topic_element, _parent())


class TestTopic1Writer:
    def test_write_wraps_in_topic_1_element(self):
        """writeTopic1 owns its TOPIC-1 wrapper element (XSD group TOPIC-1 is referenced from a parent choice)."""
        element = ET.Element("CHAPTER-MODEL")
        ARXMLWriter().writeTopic1(element, _full_topic())

        written = element.find("TOPIC-1")
        assert written is not None
        assert written.find("SHORT-NAME").text == "TopicA"
        assert written.get("HELP-ENTRY") == "topic.help.entry"

    def test_write_payload_element_order(self):
        """XSD group TOPIC-1 (00052 L16707) is <choice: TOPIC-CONTENT-OR-MSR-QUERY> then VARIATION-POINT
        (sequenceOffset=10000); VARIATION-POINT must therefore be emitted after the content payload, not at the
        Identifiable level."""
        element = ET.Element("CHAPTER-MODEL")
        ARXMLWriter().writeTopic1(element, _full_topic())

        written = element.find("TOPIC-1")
        assert [child.tag for child in written] == ["SHORT-NAME", "TOPIC-CONTENT", "VARIATION-POINT"]

    def test_write_empty_topic(self):
        """An empty Topic1 still writes the TOPIC-1 wrapper with only SHORT-NAME — no content, no VARIATION-POINT."""
        element = ET.Element("CHAPTER-MODEL")
        ARXMLWriter().writeTopic1(element, Topic1(_parent(), "BareTopic"))

        written = element.find("TOPIC-1")
        assert [child.tag for child in written] == ["SHORT-NAME"]

    def test_topic1_write_read_roundtrip(self):
        element = ET.Element("CHAPTER-MODEL")
        ARXMLWriter().writeTopic1(element, _full_topic())

        result = _reparse(element)

        assert result.getShortName() == "TopicA"
        assert result.getHelpEntry().getValue() == "topic.help.entry"
        assert result.getTopicContent() is not None
        assert result.getTopicContent().getTopicContent() is not None
        assert result.getVariationPoint() is not None

    def test_incoming_variation_point_is_read(self):
        """A VARIATION-POINT arriving on the wire is read onto the Topic1, not only written from the model."""
        element = ET.Element("CHAPTER-MODEL")
        ARXMLWriter().writeTopic1(
            element,
            Topic1(_parent(), "IncomingVP"),
        )
        written = element.find("TOPIC-1")
        vp_element = ET.SubElement(written, "VARIATION-POINT")
        ET.SubElement(vp_element, "SHORT-LABEL").text = "incoming variation point"
        ET.SubElement(vp_element, "DESC").text = "variation point description"

        result = _reparse(element)

        assert result.getVariationPoint() is not None
        assert result.getVariationPoint().getShortLabel().getValue() == "incoming variation point"
        assert result.getVariationPoint().getDesc() is not None
