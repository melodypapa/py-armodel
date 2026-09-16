import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    NameTokens,
    RefType,
    String,
    ViewTokens,
)
from armodel.models.M2.MSR.Documentation.BlockElements import Row, Table, Tbody, Tgroup
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import ChapterEnumBreak, KeepWithPreviousEnum
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import TraceableTable
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestTraceableTable:
    def test_write_traceable_table(self):
        traceable_table = TraceableTable(None, "tt")
        traceable_table.setChecksum(String().setValue("checksum"))
        traceable_table.setTimestamp(String().setValue("timestamp"))
        traceable_table.setUuid(String().setValue("uuid-tt-1"))
        traceable_table.setSi(NameTokens().setValue("semantic"))
        traceable_table.setView(ViewTokens().setValue("view-a view-b"))
        traceable_table.setBreak(ChapterEnumBreak().setValue(ChapterEnumBreak.BREAK))
        traceable_table.setKeepWithPrevious(KeepWithPreviousEnum().setValue(KeepWithPreviousEnum.KEEP))
        trace_ref = RefType()
        trace_ref.setValue("/pkg/req1")
        trace_ref.setDest("TRACEABLE-TEXT")
        traceable_table.addTraceRef(trace_ref)
        table = Table()
        table.addTgroup(Tgroup().setCols(Integer().setValue(1)).setTbody(Tbody().addRow(Row())))
        traceable_table.setTable(table)
        root = ET.Element("ROOT")

        ARXMLWriter().setTraceableTable(root, "TRACEABLE-TABLE", traceable_table)
        element = root.find("TRACEABLE-TABLE")

        assert element is not None
        assert element.attrib["S"] == "checksum"
        assert element.attrib["T"] == "timestamp"
        assert element.attrib["UUID"] == "uuid-tt-1"
        assert element.attrib["SI"] == "semantic"
        assert element.attrib["VIEW"] == "view-a view-b"
        assert element.attrib["BREAK"] == "BREAK"
        assert element.attrib["KEEP-WITH-PREVIOUS"] == "KEEP"
        assert element.find("SHORT-NAME").text == "tt"
        trace_ref_element = element.find("TRACE-REFS/TRACE-REF")
        assert trace_ref_element.text == "/pkg/req1"
        assert trace_ref_element.attrib["DEST"] == "TRACEABLE-TEXT"
        assert element.find("TABLE/TGROUP") is not None

    def test_write_traceable_table_without_optional_content(self):
        root = ET.Element("ROOT")

        ARXMLWriter().setTraceableTable(root, "TRACEABLE-TABLE", TraceableTable(None, "tt"))
        element = root.find("TRACEABLE-TABLE")

        assert element.find("SHORT-NAME").text == "tt"
        assert element.find("TRACE-REFS") is None
        assert element.find("TABLE") is None
        assert "SI" not in element.attrib
        assert "VIEW" not in element.attrib
        assert "BREAK" not in element.attrib
        assert "KEEP-WITH-PREVIOUS" not in element.attrib

    def test_write_then_read_roundtrip(self):
        traceable_table = TraceableTable(None, "tt")
        traceable_table.setSi(NameTokens().setValue("semantic"))
        traceable_table.setView(ViewTokens().setValue("view-a"))
        traceable_table.setBreak(ChapterEnumBreak().setValue(ChapterEnumBreak.NO_BREAK))
        traceable_table.setKeepWithPrevious(KeepWithPreviousEnum().setValue(KeepWithPreviousEnum.NO_KEEP))
        trace_ref = RefType()
        trace_ref.setValue("/pkg/req2")
        trace_ref.setDest("TRACEABLE-TEXT")
        traceable_table.addTraceRef(trace_ref)
        table = Table()
        table.addTgroup(Tgroup().setCols(Integer().setValue(2)).setTbody(Tbody().addRow(Row())))
        traceable_table.setTable(table)
        root = ET.Element("ROOT")
        ARXMLWriter().setTraceableTable(root, "TRACEABLE-TABLE", traceable_table)

        wrapped = '<ROOT xmlns="http://autosar.org/schema/r4.0">' + ET.tostring(root.find("TRACEABLE-TABLE"), encoding="unicode") + "</ROOT>"
        reparsed_element = ET.fromstring(wrapped).find("{http://autosar.org/schema/r4.0}TRACEABLE-TABLE")
        reparsed = TraceableTable(None, "tt")
        ARXMLParser().readTraceableTable(reparsed_element, reparsed)

        assert reparsed.getSi().getValue() == "semantic"
        assert reparsed.getView().getValue() == "view-a"
        assert reparsed.getBreak().getValue() == "NO-BREAK"
        assert reparsed.getKeepWithPrevious().getValue() == "NO-KEEP"
        assert reparsed.getTraceRefs()[0].getValue() == "/pkg/req2"
        assert reparsed.getTraceRefs()[0].getDest() == "TRACEABLE-TEXT"
        assert reparsed.getTable().getTgroups()[0].getCols().getValue() == 2
