import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements import Entry
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


def _build_entry_element():
    xml = (
        '<ENTRY xmlns="{ns}"'
        ' ALIGN="CENTER" BGCOLOR="#FFFFFF" COLNAME="c1" COLSEP="1"'
        ' MOREROWS="0" NAMEEND="c2" NAMEST="c1" ROTATE="0" ROWSEP="0"'
        ' SPANNAME="span" VALIGN="TOP">'
        "<DOCUMENTATION-BLOCK/></ENTRY>"
    ).format(ns=NS)
    return ET.fromstring(xml)


class TestEntry:
    def test_read_entry_all_attributes(self):
        parser = ARXMLParser()
        element = _build_entry_element()
        entry = Entry()
        parser.readEntry(element, entry)

        assert entry.getAlign().getValue() == "CENTER"
        assert entry.getBgcolor().getValue() == "#FFFFFF"
        assert entry.getColname().getValue() == "c1"
        assert entry.getColsep().getValue() == "1"
        assert isinstance(entry.getEntryContents(), DocumentationBlock)
        assert entry.getMorerows().getValue() == "0"
        assert entry.getNameend().getValue() == "c2"
        assert entry.getNamest().getValue() == "c1"
        assert entry.getRotate().getValue() == "0"
        assert entry.getRowsep().getValue() == "0"
        assert entry.getSpanname().getValue() == "span"
        assert entry.getValign().getValue() == "TOP"

    def test_read_entry_minimal(self):
        parser = ARXMLParser()
        element = ET.fromstring('<ENTRY xmlns="{ns}"><DOCUMENTATION-BLOCK/></ENTRY>'.format(ns=NS))
        entry = Entry()
        parser.readEntry(element, entry)

        assert entry.getAlign() is None
        assert entry.getBgcolor() is None
        assert entry.getColname() is None
        assert entry.getColsep() is None
        assert isinstance(entry.getEntryContents(), DocumentationBlock)
        assert entry.getMorerows() is None
        assert entry.getNameend() is None
        assert entry.getNamest() is None
        assert entry.getRotate() is None
        assert entry.getRowsep() is None
        assert entry.getSpanname() is None
        assert entry.getValign() is None
