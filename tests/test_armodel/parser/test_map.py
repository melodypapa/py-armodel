"""Reader tests for the Map class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.23)."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestMapParser:
    def test_get_map_reads_attributes_and_area_children(self):
        parser = ARXMLParser()
        element = ET.fromstring(
            '<PARENT xmlns="http://autosar.org/schema/r4.0">'
            '<MAP S="checksum" T="timestamp" CLASS="c1 c2" NAME="map1" ONCLICK="click()" ONDBLCLICK="dblclick()"'
            ' ONKEYDOWN="keydown()" ONKEYPRESS="keypress()" ONKEYUP="keyup()" ONMOUSEDOWN="mousedown()"'
            ' ONMOUSEMOVE="mousemove()" ONMOUSEOUT="mouseout()" ONMOUSEOVER="mouseover()" ONMOUSEUP="mouseup()"'
            ' TITLE="map title">'
            '<AREA SHAPE="RECT" COORDS="0,0,10,10" ALT="first"/>'
            '<AREA SHAPE="CIRCLE" COORDS="5,5,2" ALT="second"/>'
            "</MAP></PARENT>"
        )

        map_obj = parser.getMap(element, "MAP")

        assert map_obj.getChecksum().getValue() == "checksum"
        assert map_obj.getTimestamp().getValue() == "timestamp"
        assert map_obj.getClass().getValue() == "c1 c2"
        assert map_obj.getName().getValue() == "map1"
        assert map_obj.getOnclick().getValue() == "click()"
        assert map_obj.getOndblclick().getValue() == "dblclick()"
        assert map_obj.getOnkeydown().getValue() == "keydown()"
        assert map_obj.getOnkeypress().getValue() == "keypress()"
        assert map_obj.getOnkeyup().getValue() == "keyup()"
        assert map_obj.getOnmousedown().getValue() == "mousedown()"
        assert map_obj.getOnmousemove().getValue() == "mousemove()"
        assert map_obj.getOnmouseout().getValue() == "mouseout()"
        assert map_obj.getOnmouseover().getValue() == "mouseover()"
        assert map_obj.getOnmouseup().getValue() == "mouseup()"
        assert map_obj.getTitle().getValue() == "map title"
        areas = map_obj.getAreas()
        assert len(areas) == 2
        assert areas[0].getShape().getValue() == "RECT"
        assert areas[0].getCoords().getValue() == "0,0,10,10"
        assert areas[0].getAlt().getValue() == "first"
        assert areas[1].getShape().getValue() == "CIRCLE"
        assert areas[1].getAlt().getValue() == "second"

    def test_get_map_empty_returns_object_without_areas(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"><MAP/></PARENT>')

        map_obj = parser.getMap(element, "MAP")

        assert map_obj is not None
        assert map_obj.getAreas() == []
        assert map_obj.getClass() is None

    def test_get_map_missing_returns_none(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"/>')

        assert parser.getMap(element, "MAP") is None
