"""Writer tests for the Area class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.17)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import Area, AreaEnumNohref, AreaEnumShape
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_full_area() -> Area:
    area = Area()
    area.setAccesskey(String().setValue("a"))
    area.setAlt(String().setValue("alternative text"))
    area.setClass(String().setValue("c1 c2"))
    area.setCoords(String().setValue("0,0,10,10"))
    area.setHref(String().setValue("https://example.com"))
    area.setNohref(AreaEnumNohref().setValue(AreaEnumNohref.NOHREF))
    area.setOnblur(String().setValue("blur()"))
    area.setOnclick(String().setValue("click()"))
    area.setOndblclick(String().setValue("dblclick()"))
    area.setOnfocus(String().setValue("focus()"))
    area.setOnkeydown(String().setValue("keydown()"))
    area.setOnkeypress(String().setValue("keypress()"))
    area.setOnkeyup(String().setValue("keyup()"))
    area.setOnmousedown(String().setValue("mousedown()"))
    area.setOnmousemove(String().setValue("mousemove()"))
    area.setOnmouseout(String().setValue("mouseout()"))
    area.setOnmouseover(String().setValue("mouseover()"))
    area.setOnmouseup(String().setValue("mouseup()"))
    area.setShape(AreaEnumShape().setValue(AreaEnumShape.RECT))
    area.setStyle(String().setValue("color:red"))
    area.setTabindex(String().setValue("5"))
    area.setTitle(String().setValue("area title"))
    return area


class TestAreaWriter:
    def test_set_area_writes_all_attributes(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setArea(element, "AREA", _build_full_area())

        written = element.find("AREA")
        assert written is not None
        assert written.attrib["ACCESSKEY"] == "a"
        assert written.attrib["ALT"] == "alternative text"
        assert written.attrib["CLASS"] == "c1 c2"
        assert written.attrib["COORDS"] == "0,0,10,10"
        assert written.attrib["HREF"] == "https://example.com"
        assert written.attrib["NOHREF"] == "NOHREF"
        assert written.attrib["ONBLUR"] == "blur()"
        assert written.attrib["ONCLICK"] == "click()"
        assert written.attrib["ONDBLCLICK"] == "dblclick()"
        assert written.attrib["ONFOCUS"] == "focus()"
        assert written.attrib["ONKEYDOWN"] == "keydown()"
        assert written.attrib["ONKEYPRESS"] == "keypress()"
        assert written.attrib["ONKEYUP"] == "keyup()"
        assert written.attrib["ONMOUSEDOWN"] == "mousedown()"
        assert written.attrib["ONMOUSEMOVE"] == "mousemove()"
        assert written.attrib["ONMOUSEOUT"] == "mouseout()"
        assert written.attrib["ONMOUSEOVER"] == "mouseover()"
        assert written.attrib["ONMOUSEUP"] == "mouseup()"
        assert written.attrib["SHAPE"] == "RECT"
        assert written.attrib["STYLE"] == "color:red"
        assert written.attrib["TABINDEX"] == "5"
        assert written.attrib["TITLE"] == "area title"

    def test_set_area_omits_unset_attributes(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setArea(element, "AREA", Area())

        written = element.find("AREA")
        assert written is not None
        assert written.attrib == {}

    def test_set_area_none_is_noop(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setArea(element, "AREA", None)

        assert element.find("AREA") is None

    def test_area_write_read_roundtrip(self):
        writer_element = ET.Element("PARENT")
        ARXMLWriter().setArea(writer_element, "AREA", _build_full_area())

        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        xml_bytes = ET.tostring(writer_element, encoding="unicode")
        parsed = ET.fromstring(xml_bytes)

        area = ARXMLParser().getArea(parsed, "AREA")

        assert area.getAccesskey().getValue() == "a"
        assert area.getClass().getValue() == "c1 c2"
        assert area.getNohref().getValue() == "NOHREF"
        assert area.getShape().getValue() == "RECT"
        assert area.getTabindex().getValue() == "5"
        assert area.getTitle().getValue() == "area title"
