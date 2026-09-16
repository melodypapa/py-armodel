import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import TraceableTable
from armodel.parser.arxml_parser import ARXMLParser


class TestTraceableTable:
    def test_read_traceable_table(self):
        element = ET.fromstring(
            '<TRACEABLE-TABLE xmlns="http://autosar.org/schema/r4.0" S="checksum" T="timestamp" '
            'UUID="uuid-tt-1" SI="semantic" VIEW="view-a view-b" BREAK="BREAK" KEEP-WITH-PREVIOUS="KEEP">'
            "<SHORT-NAME>tt</SHORT-NAME>"
            '<TRACE-REFS><TRACE-REF DEST="TRACEABLE-TEXT">/pkg/req1</TRACE-REF></TRACE-REFS>'
            '<TABLE><TGROUP COLS="1"><TBODY><ROW /></TBODY></TGROUP></TABLE>'
            "</TRACEABLE-TABLE>"
        )
        traceable_table = TraceableTable(None, "tt")

        ARXMLParser().readTraceableTable(element, traceable_table)

        assert traceable_table.getChecksum().getValue() == "checksum"
        assert traceable_table.getTimestamp().getValue() == "timestamp"
        assert traceable_table.getUuid().getValue() == "uuid-tt-1"
        assert traceable_table.getShortName() == "tt"
        assert traceable_table.getSi().getValue() == "semantic"
        assert traceable_table.getView().getValue() == "view-a view-b"
        assert traceable_table.getBreak().getValue() == "BREAK"
        assert traceable_table.getKeepWithPrevious().getValue() == "KEEP"
        assert len(traceable_table.getTraceRefs()) == 1
        assert traceable_table.getTraceRefs()[0].getValue() == "/pkg/req1"
        assert traceable_table.getTraceRefs()[0].getDest() == "TRACEABLE-TEXT"
        assert traceable_table.getTable() is not None
        assert len(traceable_table.getTable().getTgroups()) == 1

    def test_read_traceable_table_without_optional_content(self):
        traceable_table = TraceableTable(None, "tt")

        ARXMLParser().readTraceableTable(
            ET.fromstring('<TRACEABLE-TABLE xmlns="http://autosar.org/schema/r4.0" />'),
            traceable_table,
        )

        assert traceable_table.getSi() is None
        assert traceable_table.getView() is None
        assert traceable_table.getBreak() is None
        assert traceable_table.getKeepWithPrevious() is None
        assert traceable_table.getTraceRefs() == []
        assert traceable_table.getTable() is None

    def test_get_traceable_table(self):
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0">' "<TRACEABLE-TABLE><SHORT-NAME>tt</SHORT-NAME></TRACEABLE-TABLE>" "</ROOT>")

        traceable_table = ARXMLParser().getTraceableTable(element, "TRACEABLE-TABLE")

        assert traceable_table is not None
        assert traceable_table.getShortName() == "tt"

    def test_get_traceable_table_missing_returns_none(self):
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0" />')

        assert ARXMLParser().getTraceableTable(element, "TRACEABLE-TABLE") is None
