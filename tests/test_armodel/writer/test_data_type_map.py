"""
Tests for writing DATA-TYPE-MAP elements — DataTypeMap, Table 5.3 (p.233, R23-11).

DataTypeMap (Base = ARObject) carries the two own attributes applicationDataType
(APPLICATION-DATA-TYPE-REF 0..1) and implementationDataType (IMPLEMENTATION-DATA-TYPE-REF
0..1). Writer element order must follow the XSD sequence (AUTOSAR_00052.xsd complexType
DATA-TYPE-MAP: AR-OBJECT group → DATA-TYPE-MAP group), so APPLICATION-DATA-TYPE-REF is
emitted before IMPLEMENTATION-DATA-TYPE-REF. The DATA-TYPE-MAPS wrapper is emitted only
when non-empty. The set-level round-trip goes through the DataTypeMappingSet aggregation
(writeDataTypeMappingSet dispatch → readDataTypeMappingSet dispatch).

Round-trip counterpart: tests/test_armodel/parser/test_data_type_map.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import DataTypeMap, DataTypeMappingSet
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _mapping_set():
    return DataTypeMappingSet(AUTOSAR.getInstance(), "Set")


def _filled_mapping_set():
    mapping_set = _mapping_set()
    data_type_map = DataTypeMap()
    data_type_map.setApplicationDataTypeRef(_ref("/pkg/AppType", "APPLICATION-PRIMITIVE-DATA-TYPE"))
    data_type_map.setImplementationDataTypeRef(_ref("/pkg/ImplType", "IMPLEMENTATION-DATA-TYPE"))
    mapping_set.addDataTypeMap(data_type_map)
    return mapping_set


class TestWriteDataTypeMaps:
    """Tests for writeDataTypeMappingSet — own element field values (Table 5.3)."""

    def test_write_field_values(self, writer):
        """Test that both REF elements are emitted with their values read through the getters."""
        parent = ET.Element("PARENT")

        writer.writeDataTypeMappingSet(parent, _filled_mapping_set())

        set_element = parent.find("DATA-TYPE-MAPPING-SET")
        assert set_element is not None
        maps_wrapper = set_element.find("DATA-TYPE-MAPS")
        assert maps_wrapper is not None
        map_element = maps_wrapper.find("DATA-TYPE-MAP")
        assert map_element is not None
        app_ref = map_element.find("APPLICATION-DATA-TYPE-REF")
        assert app_ref is not None
        assert app_ref.text == "/pkg/AppType"
        assert app_ref.attrib.get("DEST") == "APPLICATION-PRIMITIVE-DATA-TYPE"
        impl_ref = map_element.find("IMPLEMENTATION-DATA-TYPE-REF")
        assert impl_ref is not None
        assert impl_ref.text == "/pkg/ImplType"
        assert impl_ref.attrib.get("DEST") == "IMPLEMENTATION-DATA-TYPE"

    def test_write_xsd_element_order(self, writer):
        """Test that APPLICATION-DATA-TYPE-REF is emitted before IMPLEMENTATION-DATA-TYPE-REF (XSD group order)."""
        parent = ET.Element("PARENT")

        writer.writeDataTypeMappingSet(parent, _filled_mapping_set())

        map_element = parent.find("DATA-TYPE-MAPPING-SET/DATA-TYPE-MAPS/DATA-TYPE-MAP")
        assert map_element is not None
        assert [elem.tag for elem in map_element] == ["APPLICATION-DATA-TYPE-REF", "IMPLEMENTATION-DATA-TYPE-REF"]

    def test_write_empty_mapping_set_emits_no_wrapper(self, writer):
        """Test that a mapping set without maps emits no DATA-TYPE-MAPS wrapper element."""
        parent = ET.Element("PARENT")

        writer.writeDataTypeMappingSet(parent, _mapping_set())

        set_element = parent.find("DATA-TYPE-MAPPING-SET")
        assert set_element is not None
        assert set_element.find("DATA-TYPE-MAPS") is None


class TestDataTypeMapRoundTrip:
    """Round-trip through the DataTypeMappingSet aggregation (set → save → reload → assert)."""

    def test_round_trip_field_values(self, writer):
        """Test that both ref field values survive a set-level write/read cycle."""
        parent = ET.Element("PARENT")
        writer.writeDataTypeMappingSet(parent, _filled_mapping_set())
        set_element = parent.find("DATA-TYPE-MAPPING-SET")

        xml_text = ET.tostring(set_element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("DATA-TYPE-MAPPING-SET", "DATA-TYPE-MAPPING-SET xmlns='http://autosar.org/schema/r4.0'", 1))

        reloaded_set = DataTypeMappingSet(AUTOSAR.getInstance(), "Set")
        ARXMLParser().readDataTypeMappingSet(reloaded_element, reloaded_set)
        maps = reloaded_set.getDataTypeMaps()
        assert len(maps) == 1
        reloaded = maps[0]
        assert isinstance(reloaded, DataTypeMap)
        assert reloaded.getApplicationDataTypeRef() is not None
        assert reloaded.getApplicationDataTypeRef().getValue() == "/pkg/AppType"
        assert reloaded.getApplicationDataTypeRef().getDest() == "APPLICATION-PRIMITIVE-DATA-TYPE"
        assert reloaded.getImplementationDataTypeRef() is not None
        assert reloaded.getImplementationDataTypeRef().getValue() == "/pkg/ImplType"
        assert reloaded.getImplementationDataTypeRef().getDest() == "IMPLEMENTATION-DATA-TYPE"

    def test_round_trip_ar_object_attributes(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) survive the write/read cycle."""
        mapping_set = _mapping_set()
        data_type_map = DataTypeMap()
        checksum = String()
        checksum.setValue("abc123")
        data_type_map.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T12:00:00+00:00")
        data_type_map.setTimestamp(timestamp)
        mapping_set.addDataTypeMap(data_type_map)

        parent = ET.Element("PARENT")
        writer.writeDataTypeMappingSet(parent, mapping_set)
        map_element = parent.find("DATA-TYPE-MAPPING-SET/DATA-TYPE-MAPS/DATA-TYPE-MAP")
        assert map_element is not None
        assert map_element.attrib.get("S") is not None
        assert map_element.attrib.get("T") is not None

        xml_text = ET.tostring(map_element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("DATA-TYPE-MAP", "DATA-TYPE-MAP xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = DataTypeMap()
        ARXMLParser().readARObject(reloaded_element, reloaded)
        assert reloaded.getChecksum() is not None
        assert reloaded.getChecksum().getValue() == "abc123"
        assert reloaded.getTimestamp() is not None
