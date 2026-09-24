"""Reader tests for the ChapterModel class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.59)."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestChapterModelParser:
    def test_read_chapter_content_payload(self):
        """A CHAPTER-CONTENT payload (first CHAPTER-MODEL group alternative) populates chapterContent with the manual content."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<CHAPTER-MODEL xmlns="http://autosar.org/schema/r4.0">'
            '<CHAPTER-CONTENT><TOPIC-CONTENT><DOCUMENTATION-BLOCK><P><L-1 L="EN">chapter content</L-1></P></DOCUMENTATION-BLOCK></TOPIC-CONTENT></CHAPTER-CONTENT>'
            "</CHAPTER-MODEL>"
        )

        result = parser.readChapterModel(element, None)

        assert result is not None
        content = result.getChapterContent()
        assert content is not None
        assert content.getTopicContent().getTopicContent().getBlockLevelContent().getPs()[0].getL1s()[0].getValue() == "chapter content"
        assert result.getTopic1() is None
        assert result.getChapter() is None

    def test_read_topic1_payloads(self):
        """TOPIC-1 and MSR-QUERY-TOPIC-1 payloads populate topic1 (second CHAPTER-MODEL group alternative, XSD group TOPIC-OR-MSR-QUERY)."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<CHAPTER-MODEL xmlns="http://autosar.org/schema/r4.0">'
            "<TOPIC-1><SHORT-NAME>TopicA</SHORT-NAME></TOPIC-1>"
            "<TOPIC-1><SHORT-NAME>TopicB</SHORT-NAME></TOPIC-1>"
            "<MSR-QUERY-TOPIC-1><MSR-QUERY-PROPS><MSR-QUERY-NAME>topic-query</MSR-QUERY-NAME></MSR-QUERY-PROPS></MSR-QUERY-TOPIC-1>"
            "</CHAPTER-MODEL>"
        )

        result = parser.readChapterModel(element, None)

        topic1 = result.getTopic1()
        assert topic1 is not None
        assert [topic.getShortName() for topic in topic1.getTopic1s()] == ["TopicA", "TopicB"]
        assert topic1.getMsrQueryTopic1().getMsrQueryProps().getMsrQueryName().getValue() == "topic-query"
        assert result.getChapterContent() is None

    def test_read_chapter_payloads(self):
        """CHAPTER and MSR-QUERY-CHAPTER payloads populate chapter (third CHAPTER-MODEL group alternative, XSD group CHAPTER-OR-MSR-QUERY)."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<CHAPTER-MODEL xmlns="http://autosar.org/schema/r4.0">'
            "<CHAPTER><SHORT-NAME>ChapterA</SHORT-NAME></CHAPTER>"
            "<CHAPTER><SHORT-NAME>ChapterB</SHORT-NAME></CHAPTER>"
            "<MSR-QUERY-CHAPTER><MSR-QUERY-PROPS><MSR-QUERY-NAME>chapter-query</MSR-QUERY-NAME></MSR-QUERY-PROPS></MSR-QUERY-CHAPTER>"
            "</CHAPTER-MODEL>"
        )

        result = parser.readChapterModel(element, None)

        chapter = result.getChapter()
        assert chapter is not None
        assert [sub_chapter.getShortName() for sub_chapter in chapter.getChapters()] == ["ChapterA", "ChapterB"]
        assert chapter.getMsrQueryChapter().getMsrQueryProps().getMsrQueryName().getValue() == "chapter-query"
        assert result.getTopic1() is None

    def test_read_empty_chapter_model(self):
        """No payload children — an empty ChapterModel is returned with all three attributes left unset."""
        parser = ARXMLParser()
        element = ET.fromstring('<CHAPTER-MODEL xmlns="http://autosar.org/schema/r4.0"/>')

        result = parser.readChapterModel(element, None)

        assert result is not None
        assert result.getChapterContent() is None
        assert result.getTopic1() is None
        assert result.getChapter() is None
