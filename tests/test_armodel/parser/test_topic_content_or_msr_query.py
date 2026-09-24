"""Reader tests for the TopicContentOrMsrQuery class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.79)."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestTopicContentOrMsrQueryParser:
    def test_read_msr_query_p1_element(self):
        """The msrQueryP1 role element is MSR-QUERY-P-1 (XSD 00052 group TOPIC-CONTENT-OR-MSR-QUERY) and must populate msrQueryP1."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<PARENT xmlns="http://autosar.org/schema/r4.0">' "<MSR-QUERY-P-1>" "<MSR-QUERY-PROPS><MSR-QUERY-NAME>paragraph-query</MSR-QUERY-NAME></MSR-QUERY-PROPS>" "</MSR-QUERY-P-1>" "</PARENT>"
        )

        result = parser.readTopicContentOrMsrQuery(element, None)

        assert result is not None
        msr_query_p1 = result.getMsrQueryP1()
        assert msr_query_p1 is not None
        assert msr_query_p1.getMsrQueryProps().getMsrQueryName().getValue() == "paragraph-query"
        assert result.getTopicContent() is None

    def test_read_topic_content_element(self):
        """A TOPIC-CONTENT payload populates topicContent with the manual content."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<PARENT xmlns="http://autosar.org/schema/r4.0">' '<TOPIC-CONTENT><DOCUMENTATION-BLOCK><P><L-1 L="EN">manual content</L-1></P></DOCUMENTATION-BLOCK></TOPIC-CONTENT>' "</PARENT>"
        )

        result = parser.readTopicContentOrMsrQuery(element, None)

        assert result is not None
        assert result.getMsrQueryP1() is None
        topic_content = result.getTopicContent()
        assert topic_content is not None
        assert topic_content.getBlockLevelContent().getPs()[0].getL1s()[0].getValue() == "manual content"

    def test_read_without_children_returns_none(self):
        """Neither alternative present — the helper yields None so no empty wrapper is attached."""
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"/>')

        assert parser.readTopicContentOrMsrQuery(element, None) is None
