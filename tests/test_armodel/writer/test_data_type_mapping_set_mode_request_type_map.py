"""
Tests for writing DATA-TYPE-MAPPING-SET MODE-REQUEST-TYPE-MAPS children —
ModeRequestTypeMap (SWC TPS Table 4.18, all attrs 0..1 refs).

Round-trip counterpart: tests/test_armodel/parser/test_data_type_mapping_set_mode_request_type_map.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeRequestTypeMap
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import DataTypeMappingSet
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _mapping_set(short_name: str = "dtms") -> DataTypeMappingSet:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return DataTypeMappingSet(ar_root, short_name)


def _ref(value: str, dest: str) -> RefType:
    ref = RefType().setValue(value)
    ref.setDest(dest)
    return ref


class TestWriteModeRequestTypeMaps:
    """
    Test the MODE-REQUEST-TYPE-MAPS children of DATA-TYPE-MAPPING-SET —
    ModeRequestTypeMap (SWC TPS Table 4.18, all attrs 0..1 refs).
    """

    def test_write_field_values(self, writer):
        """
        Test that both refs are emitted under MODE-REQUEST-TYPE-MAPS in XSD
        element order with value and DEST preserved.
        """
        mapping_set = _mapping_set()
        mode_map = ModeRequestTypeMap()
        mode_map.setImplementationDataTypeRef(_ref("/pkg/mode-idt", "ABSTRACT-IMPLEMENTATION-DATA-TYPE"))
        mode_map.setModeGroupRef(_ref("/pkg/mode-group", "MODE-DECLARATION-GROUP"))
        mapping_set.addModeRequestTypeMap(mode_map)

        parent = ET.Element("PARENT")
        writer.writeModeRequestTypeMaps(parent, mapping_set)

        assert len(parent) == 1
        maps_tag = parent[0]
        assert maps_tag.tag == "MODE-REQUEST-TYPE-MAPS"
        assert len(maps_tag) == 1
        mr_map = maps_tag[0]
        assert mr_map.tag == "MODE-REQUEST-TYPE-MAP"
        assert [element.tag for element in mr_map] == ["IMPLEMENTATION-DATA-TYPE-REF", "MODE-GROUP-REF"]
        assert mr_map.find("IMPLEMENTATION-DATA-TYPE-REF").text == "/pkg/mode-idt"
        assert mr_map.find("IMPLEMENTATION-DATA-TYPE-REF").attrib["DEST"] == "ABSTRACT-IMPLEMENTATION-DATA-TYPE"
        assert mr_map.find("MODE-GROUP-REF").text == "/pkg/mode-group"
        assert mr_map.find("MODE-GROUP-REF").attrib["DEST"] == "MODE-DECLARATION-GROUP"

    def test_write_absent_refs(self, writer):
        """
        Test that a MODE-REQUEST-TYPE-MAP with no refs set emits the map
        element without any ref children.
        """
        mapping_set = _mapping_set()
        mapping_set.addModeRequestTypeMap(ModeRequestTypeMap())

        parent = ET.Element("PARENT")
        writer.writeModeRequestTypeMaps(parent, mapping_set)

        assert len(parent) == 1
        mr_map = parent[0][0]
        assert mr_map.tag == "MODE-REQUEST-TYPE-MAP"
        assert len(mr_map) == 0

    def test_write_no_wrapper_when_empty(self, writer):
        """
        Test that no MODE-REQUEST-TYPE-MAPS element is emitted when the
        mapping set holds no mode request type maps.
        """
        mapping_set = _mapping_set()

        parent = ET.Element("PARENT")
        writer.writeModeRequestTypeMaps(parent, mapping_set)

        assert len(parent) == 0

    def test_write_read_round_trip(self, writer):
        """
        Test the full write -> read round-trip preserves both ref values and
        DEST attributes.
        """
        mapping_set = _mapping_set()
        mode_map = ModeRequestTypeMap()
        mode_map.setImplementationDataTypeRef(_ref("/pkg/mode-idt", "ABSTRACT-IMPLEMENTATION-DATA-TYPE"))
        mode_map.setModeGroupRef(_ref("/pkg/mode-group", "MODE-DECLARATION-GROUP"))
        mapping_set.addModeRequestTypeMap(mode_map)

        parent = ET.Element("DATA-TYPE-MAPPING-SET", {"xmlns": NS})
        writer.writeModeRequestTypeMaps(parent, mapping_set)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = _mapping_set("dtms2")
        ARXMLParser().readModeRequestTypeMaps(ET.fromstring(xml_text), reloaded)

        maps = reloaded.getModeRequestTypeMaps()
        assert len(maps) == 1
        assert maps[0].getImplementationDataTypeRef().getValue() == "/pkg/mode-idt"
        assert maps[0].getImplementationDataTypeRef().getDest() == "ABSTRACT-IMPLEMENTATION-DATA-TYPE"
        assert maps[0].getModeGroupRef().getValue() == "/pkg/mode-group"
        assert maps[0].getModeGroupRef().getDest() == "MODE-DECLARATION-GROUP"
