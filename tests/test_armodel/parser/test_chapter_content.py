"""Reader tests for the ChapterContent class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.60)."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestChapterContentParser:
    def test_read_topic_content_payload(self):
        """A TOPIC-CONTENT payload (inlined TOPIC-CONTENT-OR-MSR-QUERY group alternative) populates topicContent with the manual content."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<CHAPTER-CONTENT xmlns="http://autosar.org/schema/r4.0">'
            '<TOPIC-CONTENT><DOCUMENTATION-BLOCK><P><L-1 L="EN">chapter content</L-1></P></DOCUMENTATION-BLOCK></TOPIC-CONTENT>'
            "</CHAPTER-CONTENT>"
        )

        result = parser.readChapterContent(element, None)

        assert result is not None
        topic_content_or_msr_query = result.getTopicContent()
        assert topic_content_or_msr_query is not None
        topic_content = topic_content_or_msr_query.getTopicContent()
        assert topic_content is not None
        assert topic_content.getBlockLevelContent().getPs()[0].getL1s()[0].getValue() == "chapter content"

    def test_read_msr_query_p1_payload(self):
        """An MSR-QUERY-P-1 payload populates topicContent.msrQueryP1 (XSD element name per group TOPIC-CONTENT-OR-MSR-QUERY)."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<CHAPTER-CONTENT xmlns="http://autosar.org/schema/r4.0">'
            "<MSR-QUERY-P-1><MSR-QUERY-PROPS><MSR-QUERY-NAME>chapter-query</MSR-QUERY-NAME></MSR-QUERY-PROPS></MSR-QUERY-P-1>"
            "</CHAPTER-CONTENT>"
        )

        result = parser.readChapterContent(element, None)

        topic_content_or_msr_query = result.getTopicContent()
        assert topic_content_or_msr_query is not None
        assert topic_content_or_msr_query.getMsrQueryP1().getMsrQueryProps().getMsrQueryName().getValue() == "chapter-query"
        assert topic_content_or_msr_query.getTopicContent() is None

    def test_read_empty_chapter_content(self):
        """No payload children — an empty ChapterContent is returned with topicContent left unset."""
        parser = ARXMLParser()
        element = ET.fromstring('<CHAPTER-CONTENT xmlns="http://autosar.org/schema/r4.0"/>')

        result = parser.readChapterContent(element, None)

        assert result is not None
        assert result.getTopicContent() is None
