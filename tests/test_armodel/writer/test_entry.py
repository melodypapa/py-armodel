import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.BlockElements import Entry
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import AlignEnum, TableSeparatorString, ValignEnum
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


def _populated_entry():
    entry = Entry()
    entry.setAlign(AlignEnum().setValue(AlignEnum.CENTER))
    entry.setBgcolor(String().setValue("#FFFFFF"))
    entry.setColname(String().setValue("c1"))
    entry.setColsep(TableSeparatorString().setValue("1"))
    entry.setEntryContents(DocumentationBlock())
    entry.setMorerows(String().setValue("0"))
    entry.setNameend(String().setValue("c2"))
    entry.setNamest(String().setValue("c1"))
    entry.setRotate(String().setValue("0"))
    entry.setRowsep(TableSeparatorString().setValue("0"))
    entry.setSpanname(String().setValue("span"))
    entry.setValign(ValignEnum().setValue(ValignEnum.TOP))
    return entry


def test_write_entry_all_attributes():
    entry = _populated_entry()
    element = ET.Element("ENTRY")

    ARXMLWriter().writeEntry(element, entry)

    assert element.attrib == {
        "ALIGN": "CENTER",
        "BGCOLOR": "#FFFFFF",
        "COLNAME": "c1",
        "COLSEP": "1",
        "MOREROWS": "0",
        "NAMEEND": "c2",
        "NAMEST": "c1",
        "ROTATE": "0",
        "ROWSEP": "0",
        "SPANNAME": "span",
        "VALIGN": "TOP",
    }
    assert element.find("DOCUMENTATION-BLOCK") is not None


def test_write_entry_minimal():
    entry = Entry()
    entry.setEntryContents(DocumentationBlock())
    element = ET.Element("ENTRY")

    ARXMLWriter().writeEntry(element, entry)

    assert element.attrib == {}
    assert element.find("DOCUMENTATION-BLOCK") is not None


def test_entry_roundtrip():
    entry = _populated_entry()
    element = ET.Element("ENTRY")
    ARXMLWriter().writeEntry(element, entry)

    written = ET.tostring(element, encoding="unicode").replace("<ENTRY", '<ENTRY xmlns="{ns}"'.format(ns=NS), 1)
    reparsed_element = ET.fromstring(written)
    reparsed = Entry()
    ARXMLParser().readEntry(reparsed_element, reparsed)

    assert reparsed.getAlign().getValue() == "CENTER"
    assert reparsed.getBgcolor().getValue() == "#FFFFFF"
    assert reparsed.getColname().getValue() == "c1"
    assert reparsed.getColsep().getValue() == "1"
    assert isinstance(reparsed.getEntryContents(), DocumentationBlock)
    assert reparsed.getMorerows().getValue() == "0"
    assert reparsed.getNameend().getValue() == "c2"
    assert reparsed.getNamest().getValue() == "c1"
    assert reparsed.getRotate().getValue() == "0"
    assert reparsed.getRowsep().getValue() == "0"
    assert reparsed.getSpanname().getValue() == "span"
    assert reparsed.getValign().getValue() == "TOP"
