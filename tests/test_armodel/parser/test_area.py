"""Reader tests for the Area class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.17)."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestAreaParser:
    def test_get_area_reads_all_typed_attributes(self):
        parser = ARXMLParser()
        element = ET.fromstring(
            '<PARENT xmlns="http://autosar.org/schema/r4.0">'
            '<AREA S="checksum" T="timestamp"'
            ' ACCESSKEY="a" ALT="alternative text" CLASS="c1 c2" COORDS="0,0,10,10" HREF="https://example.com"'
            ' NOHREF="NOHREF" ONBLUR="blur()" ONCLICK="click()" ONDBLCLICK="dblclick()" ONFOCUS="focus()"'
            ' ONKEYDOWN="keydown()" ONKEYPRESS="keypress()" ONKEYUP="keyup()" ONMOUSEDOWN="mousedown()"'
            ' ONMOUSEMOVE="mousemove()" ONMOUSEOUT="mouseout()" ONMOUSEOVER="mouseover()" ONMOUSEUP="mouseup()"'
            ' SHAPE="RECT" STYLE="color:red" TABINDEX="5" TITLE="area title">'
            "</AREA></PARENT>"
        )

        area = parser.getArea(element, "AREA")

        assert area.getChecksum().getValue() == "checksum"
        assert area.getTimestamp().getValue() == "timestamp"
        assert area.getAccesskey().getValue() == "a"
        assert area.getAlt().getValue() == "alternative text"
        assert area.getClass().getValue() == "c1 c2"
        assert area.getCoords().getValue() == "0,0,10,10"
        assert area.getHref().getValue() == "https://example.com"
        assert area.getNohref().getValue() == "NOHREF"
        assert area.getOnblur().getValue() == "blur()"
        assert area.getOnclick().getValue() == "click()"
        assert area.getOndblclick().getValue() == "dblclick()"
        assert area.getOnfocus().getValue() == "focus()"
        assert area.getOnkeydown().getValue() == "keydown()"
        assert area.getOnkeypress().getValue() == "keypress()"
        assert area.getOnkeyup().getValue() == "keyup()"
        assert area.getOnmousedown().getValue() == "mousedown()"
        assert area.getOnmousemove().getValue() == "mousemove()"
        assert area.getOnmouseout().getValue() == "mouseout()"
        assert area.getOnmouseover().getValue() == "mouseover()"
        assert area.getOnmouseup().getValue() == "mouseup()"
        assert area.getShape().getValue() == "RECT"
        assert area.getStyle().getValue() == "color:red"
        assert area.getTabindex().getValue() == "5"
        assert area.getTitle().getValue() == "area title"

    def test_get_area_parses_enum_attribute_values(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0">' '<AREA NOHREF="NOHREF" SHAPE="CIRCLE"></AREA></PARENT>')

        area = parser.getArea(element, "AREA")

        from armodel.models.M2.MSR.Documentation.BlockElements.Figure import AreaEnumNohref, AreaEnumShape

        assert area.getNohref().getValue() == AreaEnumNohref.NOHREF
        assert area.getShape().getValue() == AreaEnumShape.CIRCLE

    def test_get_area_missing_returns_none(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"/>')

        assert parser.getArea(element, "AREA") is None
