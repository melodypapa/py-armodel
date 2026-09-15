import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements import Table
from armodel.parser.arxml_parser import ARXMLParser


class TestTable:
    def test_read_table(self):
        element = ET.fromstring(
            '<TABLE xmlns="http://autosar.org/schema/r4.0" S="checksum" T="timestamp" '
            'COLSEP="1" FLOAT="float" FRAME="ALL" HELP-ENTRY="help" ORIENT="LAND" '
            'PGWIDE="pgwide" ROWSEP="0" TABSTYLE="style">'
            "<TABLE-CAPTION><SHORT-NAME>cap</SHORT-NAME></TABLE-CAPTION>"
            '<TGROUP COLS="1"><TBODY><ROW /></TBODY></TGROUP>'
            "</TABLE>"
        )
        table = Table()

        ARXMLParser().readTable(element, table)

        assert table.getChecksum().getValue() == "checksum"
        assert table.getTimestamp().getValue() == "timestamp"
        assert table.getColsep().getValue() == "1"
        assert table.getFloat().getValue() == "float"
        assert table.getFrame().getValue() == "ALL"
        assert table.getHelpEntry().getValue() == "help"
        assert table.getOrient().getValue() == "LAND"
        assert table.getPgwide().getValue() == "pgwide"
        assert table.getRowsep().getValue() == "0"
        assert table.getTabstyle().getValue() == "style"
        assert table.getTableCaption().getShortName() == "cap"
        assert len(table.getTgroups()) == 1
        assert len(table.getTgroups()[0].getTbody().getRows()) == 1

    def test_read_table_without_optional_content(self):
        table = Table()

        ARXMLParser().readTable(
            ET.fromstring('<TABLE xmlns="http://autosar.org/schema/r4.0"><TGROUP COLS="1" /></TABLE>'),
            table,
        )

        assert table.getColsep() is None
        assert table.getFloat() is None
        assert table.getFrame() is None
        assert table.getHelpEntry() is None
        assert table.getOrient() is None
        assert table.getPgwide() is None
        assert table.getRowsep() is None
        assert table.getTableCaption() is None
        assert table.getTabstyle() is None
        assert len(table.getTgroups()) == 1
