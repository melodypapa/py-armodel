import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestTopicContent:
    def test_read_topic_content(self):
        element = ET.fromstring(
            '<TOPIC-CONTENT xmlns="http://autosar.org/schema/r4.0">'
            "<DOCUMENTATION-BLOCK><P><L-1 L='EN'>cell text</L-1></P></DOCUMENTATION-BLOCK>"
            '<TABLE FRAME="TOP"><TGROUP COLS="2"><TBODY><ROW /></TBODY></TGROUP></TABLE>'
            "<TRACEABLE-TABLE><SHORT-NAME>tt</SHORT-NAME></TRACEABLE-TABLE>"
            "</TOPIC-CONTENT>"
        )

        topic_content = ARXMLParser().readTopicContent(element, None)

        assert topic_content.getBlockLevelContent() is not None
        assert topic_content.getBlockLevelContent().getPs()[0].getL1s()[0].getValue() == "cell text"
        assert topic_content.getTable() is not None
        assert topic_content.getTable().getFrame().getValue() == "TOP"
        assert topic_content.getTable().getTgroups()[0].getCols().getValue() == 2
        assert topic_content.getTraceableTable() is not None
        assert topic_content.getTraceableTable().getShortName() == "tt"

    def test_read_topic_content_without_optional_content(self):
        element = ET.fromstring('<TOPIC-CONTENT xmlns="http://autosar.org/schema/r4.0" />')

        topic_content = ARXMLParser().readTopicContent(element, None)

        assert topic_content.getBlockLevelContent() is None
        assert topic_content.getTable() is None
        assert topic_content.getTraceableTable() is None
