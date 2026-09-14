import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameTokens, String
from armodel.models.M2.MSR.Documentation.BlockElements import Entry, Row
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import TableSeparatorString, ValignEnum
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import ChapterEnumBreak
from armodel.writer.arxml_writer import ARXMLWriter


class TestRow:
    def test_write_row(self):
        row = Row()
        row.setChecksum(String().setValue("checksum"))
        row.setTimestamp(String().setValue("timestamp"))
        row.setSi(NameTokens().setValue("row-view"))
        row.setBreak(ChapterEnumBreak().setValue(ChapterEnumBreak.BREAK))
        row.setRowsep(TableSeparatorString().setValue("1"))
        row.setValign(ValignEnum().setValue(ValignEnum.MIDDLE))
        row.addEntry(Entry()).addEntry(Entry())
        element = ET.Element("ROW")

        ARXMLWriter().writeRow(element, row)

        assert element.attrib["S"] == "checksum"
        assert element.attrib["T"] == "timestamp"
        assert element.attrib["SI"] == "row-view"
        assert element.attrib["BREAK"] == "BREAK"
        assert element.attrib["ROWSEP"] == "1"
        assert element.attrib["VALIGN"] == "MIDDLE"
        assert [child.tag for child in element] == ["ENTRY", "ENTRY"]

    def test_write_row_without_optional_content(self):
        element = ET.Element("ROW")

        ARXMLWriter().writeRow(element, Row())

        assert element.attrib == {}
        assert list(element) == []
