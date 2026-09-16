"""Writer tests for the LGraphic class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.25)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import Graphic, LGraphic, Map
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_full_l_graphic() -> LGraphic:
    l_graphic = LGraphic()
    l_graphic.setL("en")
    graphic = Graphic()
    graphic.setFilename(NameToken().setValue("image.png"))
    l_graphic.setGraphic(graphic)
    map_obj = Map()
    map_obj.setName(NameToken().setValue("map1"))
    l_graphic.setMap(map_obj)
    return l_graphic


class TestLGraphicWriter:
    def test_set_l_graphic_writes_attributes_and_children(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setLGraphic(element, "L-GRAPHIC", _build_full_l_graphic())

        written = element.find("L-GRAPHIC")
        assert written is not None
        assert written.attrib["L"] == "en"
        graphic_el = written.find("GRAPHIC")
        assert graphic_el is not None
        assert graphic_el.attrib["FILENAME"] == "image.png"
        map_el = written.find("MAP")
        assert map_el is not None
        assert map_el.attrib["NAME"] == "map1"
        # XSD sequenceOffset: GRAPHIC (20) before MAP (30)
        assert list(child.tag for child in written) == ["GRAPHIC", "MAP"]

    def test_set_l_graphic_omits_unset_members(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setLGraphic(element, "L-GRAPHIC", LGraphic())

        written = element.find("L-GRAPHIC")
        assert written is not None
        assert written.attrib == {}
        assert written.find("GRAPHIC") is None
        assert written.find("MAP") is None

    def test_set_l_graphic_none_is_noop(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setLGraphic(element, "L-GRAPHIC", None)

        assert element.find("L-GRAPHIC") is None

    def test_l_graphic_write_read_roundtrip(self):
        writer_element = ET.Element("PARENT")
        ARXMLWriter().setLGraphic(writer_element, "L-GRAPHIC", _build_full_l_graphic())

        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        xml_bytes = ET.tostring(writer_element, encoding="unicode")
        parsed = ET.fromstring(xml_bytes)

        l_graphic = ARXMLParser().getLGraphic(parsed, "L-GRAPHIC")

        assert l_graphic.getL() == "en"
        assert l_graphic.getGraphic().getFilename().getValue() == "image.png"
        assert l_graphic.getMap().getName().getValue() == "map1"
