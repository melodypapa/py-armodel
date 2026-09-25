"""Writer tests for the TopicContentOrMsrQuery class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.79)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.Chapters import TopicContent, TopicContentOrMsrQuery
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryP1, MsrQueryProps
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_full_topic_content_or_msr_query() -> TopicContentOrMsrQuery:
    paragraph = MultiLanguageParagraph()
    l1 = LParagraph()
    l1.setL("EN")
    l1.setValue("manual content")
    paragraph.addL1(l1)
    block = DocumentationBlock()
    block.addP(paragraph)

    props = MsrQueryProps().setMsrQueryName(String().setValue("paragraph-query"))
    return TopicContentOrMsrQuery().setMsrQueryP1(MsrQueryP1().setMsrQueryProps(props)).setTopicContent(TopicContent().setBlockLevelContent(block))


class TestTopicContentOrMsrQueryWriter:
    def test_write_msr_query_p1_uses_xsd_element_name(self):
        """The msrQueryP1 role element must be written as MSR-QUERY-P-1 (XSD 00052 group TOPIC-CONTENT-OR-MSR-QUERY)."""
        element = ET.Element("PARENT")

        ARXMLWriter().writeTopicContentOrMsrQuery(element, _build_full_topic_content_or_msr_query())

        written = element.find("MSR-QUERY-P-1")
        assert written is not None
        assert written.find("MSR-QUERY-PROPS/MSR-QUERY-NAME").text == "paragraph-query"
        # XSD group order: MSR-QUERY-P-1 alternative before the TOPIC-CONTENT payload
        assert [child.tag for child in element] == ["MSR-QUERY-P-1", "TOPIC-CONTENT"]

    def test_write_topic_content_payload(self):
        element = ET.Element("PARENT")

        ARXMLWriter().writeTopicContentOrMsrQuery(element, _build_full_topic_content_or_msr_query())

        written = element.find("TOPIC-CONTENT")
        assert written is not None
        l1 = written.find("DOCUMENTATION-BLOCK/P/L-1")
        assert l1 is not None
        assert l1.attrib["L"] == "EN"
        assert l1.text == "manual content"

    def test_write_empty_writes_nothing(self):
        element = ET.Element("PARENT")

        ARXMLWriter().writeTopicContentOrMsrQuery(element, TopicContentOrMsrQuery())

        assert list(element) == []

    def test_topic_content_or_msr_query_write_read_roundtrip(self):
        writer_element = ET.Element("PARENT")
        ARXMLWriter().writeTopicContentOrMsrQuery(writer_element, _build_full_topic_content_or_msr_query())
        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(writer_element, encoding="unicode"))

        result = ARXMLParser().readTopicContentOrMsrQuery(parsed, None)

        assert result.getMsrQueryP1().getMsrQueryProps().getMsrQueryName().getValue() == "paragraph-query"
        assert result.getTopicContent().getBlockLevelContent().getPs()[0].getL1s()[0].getValue() == "manual content"
