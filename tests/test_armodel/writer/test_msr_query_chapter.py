"""Writer tests for the MsrQueryChapter class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.84)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.Chapters import Chapter
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryChapter, MsrQueryProps, MsrQueryResultChapter
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_full_msr_query_chapter() -> MsrQueryChapter:
    msr_query_chapter = MsrQueryChapter()
    props = MsrQueryProps()
    props.setMsrQueryName(String().setValue("query-1"))
    msr_query_chapter.setMsrQueryProps(props)
    result = MsrQueryResultChapter()
    result.addChapter(Chapter(None, "ch1"))
    msr_query_chapter.setMsrQueryResultChapter(result)
    return msr_query_chapter


class TestMsrQueryChapterWriter:
    def test_write_msr_query_chapter_writes_members_in_xsd_order(self):
        element = ET.Element("PARENT")

        ARXMLWriter().writeMsrQueryChapter(element, _build_full_msr_query_chapter())

        written = element.find("MSR-QUERY-CHAPTER")
        assert written is not None
        # XSD MSR-QUERY-CHAPTER group order: MSR-QUERY-PROPS (20), MSR-QUERY-RESULT-CHAPTER (30)
        assert list(child.tag for child in written) == ["MSR-QUERY-PROPS", "MSR-QUERY-RESULT-CHAPTER"]
        assert written.find("MSR-QUERY-PROPS/MSR-QUERY-NAME").text == "query-1"
        chapters = written.findall("MSR-QUERY-RESULT-CHAPTER/CHAPTER")
        assert len(chapters) == 1
        assert chapters[0].find("SHORT-NAME").text == "ch1"

    def test_write_msr_query_chapter_empty_omits_members(self):
        element = ET.Element("PARENT")

        ARXMLWriter().writeMsrQueryChapter(element, MsrQueryChapter())

        written = element.find("MSR-QUERY-CHAPTER")
        assert written is not None
        assert len(list(written)) == 0

    def test_msr_query_chapter_write_read_roundtrip(self):
        writer_element = ET.Element("PARENT")
        ARXMLWriter().writeMsrQueryChapter(writer_element, _build_full_msr_query_chapter())

        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        xml_bytes = ET.tostring(writer_element, encoding="unicode")
        parsed = ET.fromstring(xml_bytes)

        msr_query_chapter = ARXMLParser().readMsrQueryChapter(ARXMLParser().find(parsed, "MSR-QUERY-CHAPTER"), None)

        assert msr_query_chapter.getMsrQueryProps().getMsrQueryName().getValue() == "query-1"
        result = msr_query_chapter.getMsrQueryResultChapter()
        assert result is not None
        assert result.getChapters()[0].getShortName() == "ch1"
