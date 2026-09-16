import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, NameToken, String
from armodel.models.M2.MSR.Documentation.BlockElements import Caption, Row, Table, Tbody, Tgroup
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    FloatEnum,
    FrameEnum,
    OrientEnum,
    TableSeparatorString,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestTable:
    def test_write_table(self):
        table = Table()
        table.setChecksum(String().setValue("checksum"))
        table.setTimestamp(String().setValue("timestamp"))
        table.setColsep(TableSeparatorString().setValue("1"))
        table.setFloat(FloatEnum().setValue(FloatEnum.FLOAT))
        table.setFrame(FrameEnum().setValue(FrameEnum.ALL))
        table.setHelpEntry(String().setValue("help"))
        table.setOrient(OrientEnum().setValue(OrientEnum.LAND))
        table.setPgwide(NameToken().setValue("pgwide"))
        table.setRowsep(TableSeparatorString().setValue("0"))
        table.setTabstyle(NameToken().setValue("style"))
        table.setTableCaption(Caption(None, "cap"))
        table.addTgroup(Tgroup().setCols(Integer().setValue(1)).setTbody(Tbody().addRow(Row())))
        element = ET.Element("TABLE")

        ARXMLWriter().writeTable(element, table)

        assert element.attrib["S"] == "checksum"
        assert element.attrib["T"] == "timestamp"
        assert element.attrib["COLSEP"] == "1"
        assert element.attrib["FLOAT"] == "float"
        assert element.attrib["FRAME"] == "ALL"
        assert element.attrib["HELP-ENTRY"] == "help"
        assert element.attrib["ORIENT"] == "LAND"
        assert element.attrib["PGWIDE"] == "pgwide"
        assert element.attrib["ROWSEP"] == "0"
        assert element.attrib["TABSTYLE"] == "style"
        assert [child.tag for child in element] == ["TABLE-CAPTION", "TGROUP"]
        assert element.find("TABLE-CAPTION/SHORT-NAME").text == "cap"

    def test_write_table_without_optional_content(self):
        element = ET.Element("TABLE")

        ARXMLWriter().writeTable(element, Table())

        assert element.attrib == {}
        assert list(element) == []

    def test_write_then_read_roundtrip(self):
        table = Table()
        table.setColsep(TableSeparatorString().setValue("1"))
        table.setFloat(FloatEnum().setValue(FloatEnum.FLOAT))
        table.setFrame(FrameEnum().setValue(FrameEnum.ALL))
        table.setOrient(OrientEnum().setValue(OrientEnum.PORT))
        table.setTableCaption(Caption(None, "cap"))
        table.addTgroup(Tgroup().setCols(Integer().setValue(2)).setTbody(Tbody().addRow(Row())))
        element = ET.Element("TABLE")
        ARXMLWriter().writeTable(element, table)

        wrapped = '<ROOT xmlns="http://autosar.org/schema/r4.0">' + ET.tostring(element, encoding="unicode") + "</ROOT>"
        reparsed_element = ET.fromstring(wrapped).find("{http://autosar.org/schema/r4.0}TABLE")
        reparsed = Table()
        ARXMLParser().readTable(reparsed_element, reparsed)

        assert reparsed.getColsep().getValue() == "1"
        assert reparsed.getFloat().getValue() == "float"
        assert reparsed.getFrame().getValue() == "ALL"
        assert reparsed.getOrient().getValue() == "PORT"
        assert reparsed.getTableCaption().getShortName() == "cap"
        assert len(reparsed.getTgroups()) == 1
        assert reparsed.getTgroups()[0].getCols().getValue() == 2
