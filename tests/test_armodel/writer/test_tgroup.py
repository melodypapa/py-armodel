import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, String
from armodel.models.M2.MSR.Documentation.BlockElements import Colspec, Row, Tbody, Tgroup
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import AlignEnum, TableSeparatorString
from armodel.writer.arxml_writer import ARXMLWriter


class TestTgroup:
    def test_write_tgroup(self):
        tgroup = Tgroup()
        tgroup.setChecksum(String().setValue("checksum"))
        tgroup.setTimestamp(String().setValue("timestamp"))
        tgroup.setAlign(AlignEnum().setValue(AlignEnum.CENTER))
        tgroup.setCols(Integer().setValue(2))
        tgroup.setColsep(TableSeparatorString().setValue("1"))
        tgroup.setRowsep(TableSeparatorString().setValue("0"))
        tgroup.addColspec(Colspec())
        tgroup.setThead(Tbody().addRow(Row()))
        tgroup.setTfoot(Tbody().addRow(Row()))
        tgroup.setTbody(Tbody().addRow(Row()))
        element = ET.Element("TGROUP")

        ARXMLWriter().writeTgroup(element, tgroup)

        assert element.attrib["S"] == "checksum"
        assert element.attrib["T"] == "timestamp"
        assert element.attrib["ALIGN"] == "CENTER"
        assert element.attrib["COLS"] == "2"
        assert [child.tag for child in element] == ["COLSPEC", "THEAD", "TFOOT", "TBODY"]

    def test_write_tgroup_without_optional_content(self):
        element = ET.Element("TGROUP")

        ARXMLWriter().writeTgroup(element, Tgroup())

        assert element.attrib == {}
        assert list(element) == []
