import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.BlockElements import Row, Tbody
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import ValignEnum
from armodel.writer.arxml_writer import ARXMLWriter


class TestTbody:
    def test_write_tbody(self):
        tbody = Tbody()
        tbody.setChecksum(String().setValue("checksum"))
        tbody.setTimestamp(String().setValue("timestamp"))
        tbody.setValign(ValignEnum().setValue(ValignEnum.MIDDLE))
        tbody.addRow(Row()).addRow(Row())
        element = ET.Element("TBODY")

        ARXMLWriter().writeTbody(element, tbody)

        assert element.attrib["S"] == "checksum"
        assert element.attrib["T"] == "timestamp"
        assert element.attrib["VALIGN"] == "MIDDLE"
        assert [child.tag for child in element] == ["ROW", "ROW"]

    def test_write_tbody_without_optional_content(self):
        element = ET.Element("TBODY")

        ARXMLWriter().writeTbody(element, Tbody())

        assert element.attrib == {}
        assert list(element) == []
