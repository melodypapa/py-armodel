"""
Tests for reading DATA-TYPE-MAP elements — DataTypeMap, Table 5.3 (p.233, R23-11).

DataTypeMap (Base = ARObject) carries the two own attributes applicationDataType
(APPLICATION-DATA-TYPE-REF 0..1) and implementationDataType (IMPLEMENTATION-DATA-TYPE-REF
0..1), in XSD group order. It is aggregated by DataTypeMappingSet.dataTypeMap and read
through readDataTypeMappingSet → readDataTypeMaps.

Round-trip counterpart: tests/test_armodel/writer/test_data_type_map.py
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import DataTypeMap, DataTypeMappingSet
from tests.test_armodel.parser._helpers import _autosar_root, _snip


class TestReadDataTypeMaps:
    """Tests for readDataTypeMaps — own element field values (Table 5.3)."""

    def test_own_element_field_values(self, parser):
        """Test that both REF elements are read with their values and DEST attributes."""
        mapping_set = DataTypeMappingSet(_autosar_root(), "Set")
        element = _snip(
            """
            <DATA-TYPE-MAPS>
                <DATA-TYPE-MAP>
                    <APPLICATION-DATA-TYPE-REF DEST="APPLICATION-PRIMITIVE-DATA-TYPE">/pkg/AppType</APPLICATION-DATA-TYPE-REF>
                    <IMPLEMENTATION-DATA-TYPE-REF DEST="IMPLEMENTATION-DATA-TYPE">/pkg/ImplType</IMPLEMENTATION-DATA-TYPE-REF>
                </DATA-TYPE-MAP>
            </DATA-TYPE-MAPS>
            """,
            root_tag="DATA-TYPE-MAPPING-SET",
        )

        parser.readDataTypeMaps(element, mapping_set)

        maps = mapping_set.getDataTypeMaps()
        assert len(maps) == 1
        data_type_map = maps[0]
        assert isinstance(data_type_map, DataTypeMap)
        assert data_type_map.getApplicationDataTypeRef() is not None
        assert data_type_map.getApplicationDataTypeRef().getValue() == "/pkg/AppType"
        assert data_type_map.getApplicationDataTypeRef().getDest() == "APPLICATION-PRIMITIVE-DATA-TYPE"
        assert data_type_map.getImplementationDataTypeRef() is not None
        assert data_type_map.getImplementationDataTypeRef().getValue() == "/pkg/ImplType"
        assert data_type_map.getImplementationDataTypeRef().getDest() == "IMPLEMENTATION-DATA-TYPE"

    def test_empty_element(self, parser):
        """Test that an empty DATA-TYPE-MAP element yields an instance with both refs None."""
        mapping_set = DataTypeMappingSet(_autosar_root(), "Set")
        element = _snip(
            "<DATA-TYPE-MAPS><DATA-TYPE-MAP></DATA-TYPE-MAP></DATA-TYPE-MAPS>",
            root_tag="DATA-TYPE-MAPPING-SET",
        )

        parser.readDataTypeMaps(element, mapping_set)

        maps = mapping_set.getDataTypeMaps()
        assert len(maps) == 1
        assert maps[0].getApplicationDataTypeRef() is None
        assert maps[0].getImplementationDataTypeRef() is None

    def test_ar_object_attributes_read(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read."""
        mapping_set = DataTypeMappingSet(_autosar_root(), "Set")
        element = _snip(
            """
            <DATA-TYPE-MAPS>
                <DATA-TYPE-MAP S="abc123" T="2024-01-01T12:00:00+00:00">
                    <APPLICATION-DATA-TYPE-REF DEST="APPLICATION-PRIMITIVE-DATA-TYPE">/pkg/AppType</APPLICATION-DATA-TYPE-REF>
                </DATA-TYPE-MAP>
            </DATA-TYPE-MAPS>
            """,
            root_tag="DATA-TYPE-MAPPING-SET",
        )

        parser.readDataTypeMaps(element, mapping_set)

        maps = mapping_set.getDataTypeMaps()
        assert len(maps) == 1
        assert maps[0].getChecksum() is not None
        assert maps[0].getChecksum().getValue() == "abc123"
        assert maps[0].getTimestamp() is not None

    def test_read_via_data_type_mapping_set_dispatch(self, parser):
        """Test that the DataTypeMappingSet aggregation reads the map with field values, absent elements skipped."""
        mapping_set = DataTypeMappingSet(_autosar_root(), "Set")
        element = _snip(
            """
            <SHORT-NAME>Set</SHORT-NAME>
            <DATA-TYPE-MAPS>
                <DATA-TYPE-MAP>
                    <APPLICATION-DATA-TYPE-REF DEST="APPLICATION-PRIMITIVE-DATA-TYPE">/pkg/AppType</APPLICATION-DATA-TYPE-REF>
                </DATA-TYPE-MAP>
            </DATA-TYPE-MAPS>
            """,
            root_tag="DATA-TYPE-MAPPING-SET",
        )

        parser.readDataTypeMappingSet(element, mapping_set)

        maps = mapping_set.getDataTypeMaps()
        assert len(maps) == 1
        assert maps[0].getApplicationDataTypeRef() is not None
        assert maps[0].getApplicationDataTypeRef().getValue() == "/pkg/AppType"
        assert maps[0].getImplementationDataTypeRef() is None
