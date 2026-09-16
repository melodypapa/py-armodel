"""Reader tests for the LGraphic class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.25)."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestLGraphicParser:
    def test_get_l_graphic_reads_attributes_and_children(self):
        parser = ARXMLParser()
        element = ET.fromstring(
            '<PARENT xmlns="http://autosar.org/schema/r4.0">'
            '<L-GRAPHIC S="checksum" T="timestamp" L="en">'
            '<GRAPHIC FILENAME="image.png"/>'
            '<MAP NAME="map1"><AREA SHAPE="RECT" COORDS="0,0,10,10"/></MAP>'
            "</L-GRAPHIC></PARENT>"
        )

        l_graphic = parser.getLGraphic(element, "L-GRAPHIC")

        assert l_graphic.getChecksum().getValue() == "checksum"
        assert l_graphic.getTimestamp().getValue() == "timestamp"
        assert l_graphic.getL() == "en"
        assert l_graphic.getGraphic().getFilename().getValue() == "image.png"
        assert l_graphic.getMap().getName().getValue() == "map1"
        assert len(l_graphic.getMap().getAreas()) == 1

    def test_get_l_graphic_empty_returns_object_without_members(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"><L-GRAPHIC/></PARENT>')

        l_graphic = parser.getLGraphic(element, "L-GRAPHIC")

        assert l_graphic is not None
        assert l_graphic.getL() is None
        assert l_graphic.getGraphic() is None
        assert l_graphic.getMap() is None

    def test_get_l_graphic_missing_returns_none(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"/>')

        assert parser.getLGraphic(element, "L-GRAPHIC") is None
