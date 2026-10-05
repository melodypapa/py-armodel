"""
Tests for parsing VIEW-MAP-SET and VIEW-MAP elements (ViewMapSet Table 14.1, ViewMap Table 14.2).

Round-trip counterpart: tests/test_armodel/writer/test_view_map_set.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.ViewMapSet import (
    ViewMapSet,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _make_view_map_set() -> ViewMapSet:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return ar_root.createViewMapSet("MyViewMapSet")


class TestReadViewMapSet:
    """
    Test readViewMapSet (ViewMapSet, Table 14.1).
    """

    def test_read_view_maps(self, parser):
        """Test that the VIEW-MAPS wrapper populates viewMaps with VIEW-MAP children."""
        view_map_set = _make_view_map_set()
        element = ET.fromstring(
            f"""<VIEW-MAP-SET xmlns='{NS}'>
                <SHORT-NAME>MyViewMapSet</SHORT-NAME>
                <VIEW-MAPS>
                    <VIEW-MAP>
                        <SHORT-NAME>Map1</SHORT-NAME>
                        <ROLE>AR_SystemDescription_SystemExtract</ROLE>
                    </VIEW-MAP>
                    <VIEW-MAP>
                        <SHORT-NAME>Map-2</SHORT-NAME>
                    </VIEW-MAP>
                </VIEW-MAPS>
            </VIEW-MAP-SET>"""
        )

        parser.readViewMapSet(element, view_map_set)

        view_maps = view_map_set.getViewMaps()
        assert len(view_maps) == 2
        assert view_maps[0].getShortName() == "Map1"
        assert view_maps[0].getRole().getValue() == "AR_SystemDescription_SystemExtract"
        assert view_maps[1].getShortName() == "Map-2"

    def test_read_empty_view_maps(self, parser):
        """Test that an absent VIEW-MAPS wrapper leaves viewMaps empty (empty-wrapper case)."""
        view_map_set = _make_view_map_set()
        element = ET.fromstring(
            f"""<VIEW-MAP-SET xmlns='{NS}'>
                <SHORT-NAME>MyViewMapSet</SHORT-NAME>
            </VIEW-MAP-SET>"""
        )

        parser.readViewMapSet(element, view_map_set)

        assert view_map_set.getViewMaps() == []

    def test_load_via_ar_package(self, parser):
        """Test that the ARPackage ELEMENTS dispatch reads a VIEW-MAP-SET into getViewMapSets()."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        content = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>AUTOSAR</SHORT-NAME>
            <ELEMENTS>
                <VIEW-MAP-SET>
                    <SHORT-NAME>MyViewMapSet</SHORT-NAME>
                    <VIEW-MAPS>
                        <VIEW-MAP>
                            <SHORT-NAME>Map1</SHORT-NAME>
                        </VIEW-MAP>
                    </VIEW-MAPS>
                </VIEW-MAP-SET>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            document = AUTOSAR.getInstance()
            document.clear()
            parser.load(file_path, document)

            view_map_sets = document.getARPackages()[0].getViewMapSets()
            assert len(view_map_sets) == 1
            assert view_map_sets[0].getShortName() == "MyViewMapSet"
            assert view_map_sets[0].getViewMaps()[0].getShortName() == "Map1"
        finally:
            os.remove(file_path)


class TestReadViewMap:
    """
    Test readViewMap (ViewMap, Table 14.2).
    """

    def test_read_view_map_members(self, parser):
        """Test that ROLE, FIRST/SECOND-ELEMENT-REFS and INSTANCE-IREFS populate the ViewMap."""
        view_map_set = _make_view_map_set()
        element = ET.fromstring(
            f"""<VIEW-MAP xmlns='{NS}'>
                <SHORT-NAME>Map1</SHORT-NAME>
                <ROLE>AR_AbstractSystemDescription_SystemDescription</ROLE>
                <FIRST-ELEMENT-REFS>
                    <FIRST-ELEMENT-REF DEST="COLLECTION">/AUTOSAR/FirstColl</FIRST-ELEMENT-REF>
                </FIRST-ELEMENT-REFS>
                <SECOND-ELEMENT-REFS>
                    <SECOND-ELEMENT-REF DEST="COLLECTION">/AUTOSAR/SecondColl</SECOND-ELEMENT-REF>
                </SECOND-ELEMENT-REFS>
                <FIRST-ELEMENT-INSTANCE-IREFS>
                    <FIRST-ELEMENT-INSTANCE-IREF>
                        <BASE-REF DEST="IDENTIFIABLE">/AUTOSAR/Base</BASE-REF>
                        <CONTEXT-ELEMENT-REF DEST="COLLECTION">/AUTOSAR/Ctx</CONTEXT-ELEMENT-REF>
                        <TARGET-REF DEST="IDENTIFIABLE">/AUTOSAR/Target</TARGET-REF>
                    </FIRST-ELEMENT-INSTANCE-IREF>
                </FIRST-ELEMENT-INSTANCE-IREFS>
                <SECOND-ELEMENT-INSTANCE-IREFS>
                    <SECOND-ELEMENT-INSTANCE-IREF>
                        <TARGET-REF DEST="IDENTIFIABLE">/AUTOSAR/Target</TARGET-REF>
                    </SECOND-ELEMENT-INSTANCE-IREF>
                </SECOND-ELEMENT-INSTANCE-IREFS>
            </VIEW-MAP>"""
        )

        view_map = view_map_set.createViewMap("Map1")
        parser.readViewMap(element, view_map)

        assert view_map.getRole().getValue() == "AR_AbstractSystemDescription_SystemDescription"
        first_element_refs = view_map.getFirstElementRefs()
        assert len(first_element_refs) == 1
        assert first_element_refs[0].getDest() == "COLLECTION"
        assert first_element_refs[0].getValue() == "/AUTOSAR/FirstColl"
        second_element_refs = view_map.getSecondElementRefs()
        assert len(second_element_refs) == 1
        assert second_element_refs[0].getValue() == "/AUTOSAR/SecondColl"
        first_irefs = view_map.getFirstElementIRefs()
        assert len(first_irefs) == 1
        assert first_irefs[0].getBaseRef().getValue() == "/AUTOSAR/Base"
        assert first_irefs[0].getContextElementRefs()[0].getValue() == "/AUTOSAR/Ctx"
        assert first_irefs[0].getTargetRef().getValue() == "/AUTOSAR/Target"
        second_irefs = view_map.getSecondElementIRefs()
        assert len(second_irefs) == 1
        assert second_irefs[0].getTargetRef().getValue() == "/AUTOSAR/Target"

    def test_read_absent_optional_members(self, parser):
        """Test that absent optional members leave the fields untouched (empty case)."""
        view_map_set = _make_view_map_set()
        element = ET.fromstring(
            f"""<VIEW-MAP xmlns='{NS}'>
                <SHORT-NAME>Map1</SHORT-NAME>
            </VIEW-MAP>"""
        )

        view_map = view_map_set.createViewMap("Map1")
        parser.readViewMap(element, view_map)

        assert view_map.getRole() is None
        assert view_map.getFirstElementRefs() == []
        assert view_map.getFirstElementIRefs() == []
        assert view_map.getSecondElementRefs() == []
        assert view_map.getSecondElementIRefs() == []
