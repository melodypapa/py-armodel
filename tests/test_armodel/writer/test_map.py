"""Writer tests for the Map class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.23)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, String
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import Area, AreaEnumShape, Map
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_full_map() -> Map:
    map_obj = Map()
    map_obj.setClass(String().setValue("c1 c2"))
    map_obj.setName(NameToken().setValue("map1"))
    map_obj.setOnclick(String().setValue("click()"))
    map_obj.setOndblclick(String().setValue("dblclick()"))
    map_obj.setOnkeydown(String().setValue("keydown()"))
    map_obj.setOnkeypress(String().setValue("keypress()"))
    map_obj.setOnkeyup(String().setValue("keyup()"))
    map_obj.setOnmousedown(String().setValue("mousedown()"))
    map_obj.setOnmousemove(String().setValue("mousemove()"))
    map_obj.setOnmouseout(String().setValue("mouseout()"))
    map_obj.setOnmouseover(String().setValue("mouseover()"))
    map_obj.setOnmouseup(String().setValue("mouseup()"))
    map_obj.setTitle(String().setValue("map title"))
    area1 = Area()
    area1.setShape(AreaEnumShape().setValue(AreaEnumShape.RECT))
    area1.setCoords(String().setValue("0,0,10,10"))
    area1.setAlt(String().setValue("first"))
    area2 = Area()
    area2.setShape(AreaEnumShape().setValue(AreaEnumShape.CIRCLE))
    area2.setCoords(String().setValue("5,5,2"))
    area2.setAlt(String().setValue("second"))
    map_obj.addArea(area1)
    map_obj.addArea(area2)
    return map_obj


class TestMapWriter:
    def test_set_map_writes_attributes_and_area_children(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setMap(element, "MAP", _build_full_map())

        written = element.find("MAP")
        assert written is not None
        assert written.attrib["CLASS"] == "c1 c2"
        assert written.attrib["NAME"] == "map1"
        assert written.attrib["ONCLICK"] == "click()"
        assert written.attrib["ONDBLCLICK"] == "dblclick()"
        assert written.attrib["ONKEYDOWN"] == "keydown()"
        assert written.attrib["ONKEYPRESS"] == "keypress()"
        assert written.attrib["ONKEYUP"] == "keyup()"
        assert written.attrib["ONMOUSEDOWN"] == "mousedown()"
        assert written.attrib["ONMOUSEMOVE"] == "mousemove()"
        assert written.attrib["ONMOUSEOUT"] == "mouseout()"
        assert written.attrib["ONMOUSEOVER"] == "mouseover()"
        assert written.attrib["ONMOUSEUP"] == "mouseup()"
        assert written.attrib["TITLE"] == "map title"
        areas = written.findall("AREA")
        assert len(areas) == 2
        assert areas[0].attrib["SHAPE"] == "RECT"
        assert areas[0].attrib["COORDS"] == "0,0,10,10"
        assert areas[0].attrib["ALT"] == "first"
        assert areas[1].attrib["SHAPE"] == "CIRCLE"
        assert areas[1].attrib["ALT"] == "second"

    def test_set_map_omits_unset_members(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setMap(element, "MAP", Map())

        written = element.find("MAP")
        assert written is not None
        assert written.attrib == {}
        assert written.findall("AREA") == []

    def test_set_map_none_is_noop(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setMap(element, "MAP", None)

        assert element.find("MAP") is None

    def test_map_write_read_roundtrip(self):
        writer_element = ET.Element("PARENT")
        ARXMLWriter().setMap(writer_element, "MAP", _build_full_map())

        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        xml_bytes = ET.tostring(writer_element, encoding="unicode")
        parsed = ET.fromstring(xml_bytes)

        map_obj = ARXMLParser().getMap(parsed, "MAP")

        assert map_obj.getClass().getValue() == "c1 c2"
        assert map_obj.getName().getValue() == "map1"
        assert map_obj.getOnclick().getValue() == "click()"
        assert map_obj.getOndblclick().getValue() == "dblclick()"
        areas = map_obj.getAreas()
        assert len(areas) == 2
        assert areas[0].getShape().getValue() == "RECT"
        assert areas[0].getAlt().getValue() == "first"
        assert areas[1].getShape().getValue() == "CIRCLE"
        assert areas[1].getAlt().getValue() == "second"
