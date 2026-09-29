"""
Tests for writing VIEW-MAP-SET and VIEW-MAP elements (ViewMapSet Table 14.1, ViewMap Table 14.2).

Round-trip counterpart: tests/test_armodel/parser/test_view_map_set.py
"""

import logging
import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ViewMapSet,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ViewMap,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    RefType,
)
from armodel.writer.arxml_writer import ARXMLWriter


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    return writer


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestWriteViewMapSet:
    """
    Test writeViewMapSet (ViewMapSet, Table 14.1).
    """

    def test_write_view_maps(self):
        """Test that viewMaps are written as a VIEW-MAPS wrapper with VIEW-MAP children."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        view_map_set = ViewMapSet(None, "MyViewMapSet")
        view_map_set.createViewMap("Map-1")
        view_map_set.createViewMap("Map-2")

        writer.writeViewMapSet(element, view_map_set)

        view_map_set_tag = element.find("VIEW-MAP-SET")
        assert view_map_set_tag is not None
        maps_tag = view_map_set_tag.find("VIEW-MAPS")
        assert maps_tag is not None
        map_tags = maps_tag.findall("VIEW-MAP")
        assert len(map_tags) == 2
        assert map_tags[0].find("SHORT-NAME").text == "Map-1"
        assert map_tags[1].find("SHORT-NAME").text == "Map-2"

    def test_write_empty_wrappers(self):
        """Test that a ViewMapSet with no viewMaps writes no VIEW-MAPS wrapper (empty-wrapper case)."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        view_map_set = ViewMapSet(None, "MyViewMapSet")
        writer.writeViewMapSet(element, view_map_set)

        view_map_set_tag = element.find("VIEW-MAP-SET")
        assert view_map_set_tag is not None
        assert view_map_set_tag.find("VIEW-MAPS") is None

    def test_round_trip(self):
        """Write a ViewMapSet with viewMaps, reparse, and assert all fields survive."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        view_map_set = ar_root.createViewMapSet("MyViewMapSet")

        view_map_set.createViewMap("Map-1")
        view_map_set.createViewMap("Map-2")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            from armodel.parser.arxml_parser import ARXMLParser

            ARXMLParser().load(file_path, document_2)

            view_map_set_2 = document_2.getARPackages()[0].getViewMapSets()[0]
            assert view_map_set_2.getShortName() == "MyViewMapSet"
            view_maps = view_map_set_2.getViewMaps()
            assert len(view_maps) == 2
            assert view_maps[0].getShortName() == "Map-1"
            assert view_maps[1].getShortName() == "Map-2"
        finally:
            os.remove(file_path)


class TestWriteViewMap:
    """
    Test writeViewMap (ViewMap, Table 14.2).
    """

    def test_write_members_in_xsd_order(self):
        """Test that own members are written in the XSD VIEW-MAP group order."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        view_map = ViewMap(None, "Map-1")
        view_map.setRole(Identifier().setValue("AR_SystemDescription_SystemExtract"))
        view_map.addFirstElementRef(_ref("COLLECTION", "/AUTOSAR/FirstColl"))
        view_map.addSecondElementRef(_ref("COLLECTION", "/AUTOSAR/SecondColl"))

        writer.writeViewMap(element, view_map)

        view_map_tag = element.find("VIEW-MAP")
        assert view_map_tag is not None
        own_tags = [child.tag for child in view_map_tag if child.tag in ("ROLE", "FIRST-ELEMENT-REFS", "SECOND-ELEMENT-REFS", "FIRST-ELEMENT-INSTANCE-IREFS", "SECOND-ELEMENT-INSTANCE-IREFS")]
        assert own_tags == ["ROLE", "FIRST-ELEMENT-REFS", "SECOND-ELEMENT-REFS"]
        assert view_map_tag.find("ROLE").text == "AR_SystemDescription_SystemExtract"
        assert view_map_tag.find("FIRST-ELEMENT-REFS/FIRST-ELEMENT-REF").text == "/AUTOSAR/FirstColl"
        assert view_map_tag.find("SECOND-ELEMENT-REFS/SECOND-ELEMENT-REF").text == "/AUTOSAR/SecondColl"

    def test_write_empty(self):
        """Test that a ViewMap with no own members writes no own elements (empty case)."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        view_map = ViewMap(None, "Map-1")
        writer.writeViewMap(element, view_map)

        view_map_tag = element.find("VIEW-MAP")
        assert view_map_tag is not None
        assert view_map_tag.find("ROLE") is None
        assert view_map_tag.find("FIRST-ELEMENT-REFS") is None
        assert view_map_tag.find("SECOND-ELEMENT-REFS") is None
        assert view_map_tag.find("FIRST-ELEMENT-INSTANCE-IREFS") is None
        assert view_map_tag.find("SECOND-ELEMENT-INSTANCE-IREFS") is None
