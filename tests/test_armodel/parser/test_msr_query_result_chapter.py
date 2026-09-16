"""Reader tests for the MsrQueryResultChapter class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.87)."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestMsrQueryResultChapterParser:
    def test_get_msr_query_result_chapter_reads_chapters(self):
        parser = ARXMLParser()
        element = ET.fromstring(
            '<PARENT xmlns="http://autosar.org/schema/r4.0">'
            '<MSR-QUERY-RESULT-CHAPTER S="checksum" T="timestamp">'
            '<CHAPTER HELP-ENTRY="help-1"><SHORT-NAME>ch1</SHORT-NAME></CHAPTER>'
            "<CHAPTER><SHORT-NAME>ch2</SHORT-NAME></CHAPTER>"
            "</MSR-QUERY-RESULT-CHAPTER></PARENT>"
        )

        result = parser.getMsrQueryResultChapter(element, "MSR-QUERY-RESULT-CHAPTER")

        assert result is not None
        assert result.getChecksum().getValue() == "checksum"
        assert result.getTimestamp().getValue() == "timestamp"
        chapters = result.getChapters()
        assert len(chapters) == 2
        assert chapters[0].getShortName() == "ch1"
        assert chapters[0].getHelpEntry().getValue() == "help-1"
        assert chapters[1].getShortName() == "ch2"

    def test_get_msr_query_result_chapter_empty_returns_object(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"><MSR-QUERY-RESULT-CHAPTER/></PARENT>')

        result = parser.getMsrQueryResultChapter(element, "MSR-QUERY-RESULT-CHAPTER")

        assert result is not None
        assert result.getChapters() == []

    def test_get_msr_query_result_chapter_missing_returns_none(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"/>')

        assert parser.getMsrQueryResultChapter(element, "MSR-QUERY-RESULT-CHAPTER") is None
