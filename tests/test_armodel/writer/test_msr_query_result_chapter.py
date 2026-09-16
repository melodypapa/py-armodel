"""Writer tests for the MsrQueryResultChapter class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.87)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.Chapters import Chapter
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryResultChapter
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_full_result() -> MsrQueryResultChapter:
    result = MsrQueryResultChapter()
    result.addChapter(Chapter(None, "ch1"))
    result.addChapter(Chapter(None, "ch2"))
    return result


class TestMsrQueryResultChapterWriter:
    def test_set_msr_query_result_chapter_writes_chapter_children(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setMsrQueryResultChapter(element, "MSR-QUERY-RESULT-CHAPTER", _build_full_result())

        written = element.find("MSR-QUERY-RESULT-CHAPTER")
        assert written is not None
        chapters = written.findall("CHAPTER")
        assert len(chapters) == 2
        assert chapters[0].find("SHORT-NAME").text == "ch1"
        assert chapters[1].find("SHORT-NAME").text == "ch2"

    def test_set_msr_query_result_chapter_empty_omits_children(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setMsrQueryResultChapter(element, "MSR-QUERY-RESULT-CHAPTER", MsrQueryResultChapter())

        written = element.find("MSR-QUERY-RESULT-CHAPTER")
        assert written is not None
        assert written.findall("CHAPTER") == []

    def test_set_msr_query_result_chapter_none_is_noop(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setMsrQueryResultChapter(element, "MSR-QUERY-RESULT-CHAPTER", None)

        assert element.find("MSR-QUERY-RESULT-CHAPTER") is None

    def test_msr_query_result_chapter_write_read_roundtrip(self):
        writer_element = ET.Element("PARENT")
        ARXMLWriter().setMsrQueryResultChapter(writer_element, "MSR-QUERY-RESULT-CHAPTER", _build_full_result())

        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        xml_bytes = ET.tostring(writer_element, encoding="unicode")
        parsed = ET.fromstring(xml_bytes)

        result = ARXMLParser().getMsrQueryResultChapter(parsed, "MSR-QUERY-RESULT-CHAPTER")

        chapters = result.getChapters()
        assert len(chapters) == 2
        assert chapters[0].getShortName() == "ch1"
        assert chapters[1].getShortName() == "ch2"
