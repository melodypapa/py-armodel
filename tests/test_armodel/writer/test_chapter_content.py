"""Writer tests for the ChapterContent class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.60)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.Chapters import ChapterContent, TopicContent, TopicContentOrMsrQuery
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryP1, MsrQueryProps
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_full_chapter_content() -> ChapterContent:
    paragraph = MultiLanguageParagraph()
    l1 = LParagraph()
    l1.setL("EN")
    l1.setValue("chapter content")
    paragraph.addL1(l1)
    block = DocumentationBlock()
    block.addP(paragraph)

    props = MsrQueryProps().setMsrQueryName(String().setValue("chapter-query"))
    return ChapterContent().setTopicContent(TopicContentOrMsrQuery().setMsrQueryP1(MsrQueryP1().setMsrQueryProps(props)).setTopicContent(TopicContent().setBlockLevelContent(block)))


class TestChapterContentWriter:
    def test_write_wraps_in_chapter_content_element(self):
        """The chapter content is serialized under a CHAPTER-CONTENT wrapper element (XSD element CHAPTER-CONTENT)."""
        element = ET.Element("CHAPTER-MODEL")

        ARXMLWriter().writeChapterContent(element, _build_full_chapter_content())

        written = element.find("CHAPTER-CONTENT")
        assert written is not None
        assert written.find("MSR-QUERY-P-1/MSR-QUERY-PROPS/MSR-QUERY-NAME").text == "chapter-query"
        assert written.find("TOPIC-CONTENT/DOCUMENTATION-BLOCK/P/L-1").text == "chapter content"

    def test_write_payload_element_order(self):
        """XSD group CHAPTER-CONTENT order: the TOPIC-CONTENT-OR-MSR-QUERY payload alternatives come first (MSR-QUERY-P-1 before TOPIC-CONTENT)."""
        element = ET.Element("CHAPTER-MODEL")

        ARXMLWriter().writeChapterContent(element, _build_full_chapter_content())

        written = element.find("CHAPTER-CONTENT")
        assert [child.tag for child in written] == ["MSR-QUERY-P-1", "TOPIC-CONTENT"]

    def test_write_empty_chapter_content(self):
        """An empty ChapterContent still writes the CHAPTER-CONTENT wrapper with no payload children (round-trips as an empty wrapper)."""
        element = ET.Element("CHAPTER-MODEL")

        ARXMLWriter().writeChapterContent(element, ChapterContent())

        written = element.find("CHAPTER-CONTENT")
        assert written is not None
        assert list(written) == []

    def test_chapter_content_write_read_roundtrip(self):
        writer_element = ET.Element("CHAPTER-MODEL")
        ARXMLWriter().writeChapterContent(writer_element, _build_full_chapter_content())
        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(writer_element, encoding="unicode"))
        content_element = parsed[0]
        assert content_element.tag.endswith("CHAPTER-CONTENT")

        result = ARXMLParser().readChapterContent(content_element, None)

        topic_content_or_msr_query = result.getTopicContent()
        assert topic_content_or_msr_query.getMsrQueryP1().getMsrQueryProps().getMsrQueryName().getValue() == "chapter-query"
        assert topic_content_or_msr_query.getTopicContent().getBlockLevelContent().getPs()[0].getL1s()[0].getValue() == "chapter content"
