import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements import Tbody
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import ValignEnum
from armodel.parser.arxml_parser import ARXMLParser


class TestTbody:
    def test_read_tbody(self):
        element = ET.fromstring('<TBODY xmlns="http://autosar.org/schema/r4.0" S="checksum" T="timestamp" VALIGN="MIDDLE">' '<ROW VALIGN="TOP" />' '<ROW ROWSEP="1" />' "</TBODY>")
        tbody = Tbody()

        ARXMLParser().readTbody(element, tbody)

        assert tbody.getChecksum().getValue() == "checksum"
        assert tbody.getTimestamp().getValue() == "timestamp"
        assert tbody.getValign().getValue() == ValignEnum.MIDDLE
        assert len(tbody.getRows()) == 2
        assert tbody.getRows()[0].getValign().getValue() == ValignEnum.TOP
        assert tbody.getRows()[1].getRowsep().getValue() == "1"

    def test_read_tbody_without_optional_content(self):
        tbody = Tbody()

        ARXMLParser().readTbody(ET.fromstring('<TBODY xmlns="http://autosar.org/schema/r4.0" />'), tbody)

        assert tbody.getRows() == []
        assert tbody.getValign() is None
