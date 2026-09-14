import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements import Entry, Row
from armodel.parser.arxml_parser import ARXMLParser


class TestRow:
    def test_read_row(self):
        element = ET.fromstring('<ROW xmlns="http://autosar.org/schema/r4.0" S="checksum" T="timestamp" SI="row-view" BREAK="BREAK" ROWSEP="1" VALIGN="MIDDLE">' "<ENTRY />" "<ENTRY />" "</ROW>")
        row = Row()

        ARXMLParser().readRow(element, row)

        assert row.getChecksum().getValue() == "checksum"
        assert row.getTimestamp().getValue() == "timestamp"
        assert row.getSi().getValue() == "row-view"
        assert row.getBreak().getValue() == "BREAK"
        assert row.getRowsep().getValue() == "1"
        assert row.getValign().getValue() == "MIDDLE"
        assert len(row.getEntries()) == 2
        assert all(isinstance(entry, Entry) for entry in row.getEntries())

    def test_read_row_without_optional_content(self):
        row = Row()

        ARXMLParser().readRow(ET.fromstring('<ROW xmlns="http://autosar.org/schema/r4.0" />'), row)

        assert row.getEntries() == []
        assert row.getRowsep() is None
        assert row.getValign() is None
