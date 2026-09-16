"""Reader tests for the MsrQueryChapter class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.84)."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestMsrQueryChapterParser:
    def test_read_msr_query_chapter_reads_all_members(self):
        parser = ARXMLParser()
        element = ET.fromstring(
            '<PARENT xmlns="http://autosar.org/schema/r4.0">'
            '<MSR-QUERY-CHAPTER S="checksum" T="timestamp" SI="si-tokens" VIEW="view-tokens"'
            ' BREAK="BREAK" KEEP-WITH-PREVIOUS="KEEP">'
            "<MSR-QUERY-PROPS><MSR-QUERY-NAME>query-1</MSR-QUERY-NAME></MSR-QUERY-PROPS>"
            "<MSR-QUERY-RESULT-CHAPTER>"
            "<CHAPTER><SHORT-NAME>ch1</SHORT-NAME></CHAPTER>"
            "</MSR-QUERY-RESULT-CHAPTER>"
            "</MSR-QUERY-CHAPTER></PARENT>"
        )

        chapter_element = parser.find(element, "MSR-QUERY-CHAPTER")
        msr_query_chapter = parser.readMsrQueryChapter(chapter_element, None)

        assert msr_query_chapter.getChecksum().getValue() == "checksum"
        assert msr_query_chapter.getTimestamp().getValue() == "timestamp"
        assert msr_query_chapter.getSi().getValue() == "si-tokens"
        assert msr_query_chapter.getView().getValue() == "view-tokens"
        assert msr_query_chapter.getBreak().getValue() == "BREAK"
        assert msr_query_chapter.getKeepWithPrevious().getValue() == "KEEP"
        props = msr_query_chapter.getMsrQueryProps()
        assert props is not None
        assert props.getMsrQueryName().getValue() == "query-1"
        result = msr_query_chapter.getMsrQueryResultChapter()
        assert result is not None
        chapters = result.getChapters()
        assert len(chapters) == 1
        assert chapters[0].getShortName() == "ch1"

    def test_read_msr_query_chapter_without_result(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0">' "<MSR-QUERY-CHAPTER/>" "</PARENT>")

        chapter_element = parser.find(element, "MSR-QUERY-CHAPTER")
        msr_query_chapter = parser.readMsrQueryChapter(chapter_element, None)

        assert msr_query_chapter.getMsrQueryProps() is None
        assert msr_query_chapter.getMsrQueryResultChapter() is None
