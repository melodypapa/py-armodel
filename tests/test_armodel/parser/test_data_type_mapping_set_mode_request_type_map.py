"""
Tests for parsing DATA-TYPE-MAPPING-SET MODE-REQUEST-TYPE-MAPS children —
ModeRequestTypeMap (SWC TPS Table 4.18, all attrs 0..1 refs).

Round-trip counterpart: tests/test_armodel/writer/test_data_type_mapping_set_mode_request_type_map.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import DataTypeMappingSet
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


def _mapping_set(short_name: str = "dtms") -> DataTypeMappingSet:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return DataTypeMappingSet(ar_root, short_name)


def _parse(parser: ARXMLParser, mapping_set: DataTypeMappingSet, inner: str):
    element = ET.fromstring(
        f"""<DATA-TYPE-MAPPING-SET xmlns='{NS}'>
            <SHORT-NAME>dtms</SHORT-NAME>
            {inner}
        </DATA-TYPE-MAPPING-SET>"""
    )
    parser.readModeRequestTypeMaps(element, mapping_set)


class TestReadModeRequestTypeMaps:
    """
    Test the MODE-REQUEST-TYPE-MAPS children of DATA-TYPE-MAPPING-SET —
    ModeRequestTypeMap (SWC TPS Table 4.18, all attrs 0..1 refs).
    """

    def test_read_field_values(self, parser):
        """
        Test that both MODE-REQUEST-TYPE-MAP refs populate the mapping with
        value and DEST preserved, in XSD element order.
        """
        mapping_set = _mapping_set()
        _parse(
            parser,
            mapping_set,
            """<MODE-REQUEST-TYPE-MAPS>
                <MODE-REQUEST-TYPE-MAP>
                    <IMPLEMENTATION-DATA-TYPE-REF DEST='ABSTRACT-IMPLEMENTATION-DATA-TYPE'>/pkg/mode-idt</IMPLEMENTATION-DATA-TYPE-REF>
                    <MODE-GROUP-REF DEST='MODE-DECLARATION-GROUP'>/pkg/mode-group</MODE-GROUP-REF>
                </MODE-REQUEST-TYPE-MAP>
            </MODE-REQUEST-TYPE-MAPS>""",
        )

        maps = mapping_set.getModeRequestTypeMaps()
        assert len(maps) == 1
        assert maps[0].getImplementationDataTypeRef().getValue() == "/pkg/mode-idt"
        assert maps[0].getImplementationDataTypeRef().getDest() == "ABSTRACT-IMPLEMENTATION-DATA-TYPE"
        assert maps[0].getModeGroupRef().getValue() == "/pkg/mode-group"
        assert maps[0].getModeGroupRef().getDest() == "MODE-DECLARATION-GROUP"

    def test_read_multiple_maps(self, parser):
        """
        Test that each MODE-REQUEST-TYPE-MAP child becomes its own map
        in document order.
        """
        mapping_set = _mapping_set()
        _parse(
            parser,
            mapping_set,
            """<MODE-REQUEST-TYPE-MAPS>
                <MODE-REQUEST-TYPE-MAP>
                    <IMPLEMENTATION-DATA-TYPE-REF DEST='ABSTRACT-IMPLEMENTATION-DATA-TYPE'>/pkg/idt1</IMPLEMENTATION-DATA-TYPE-REF>
                    <MODE-GROUP-REF DEST='MODE-DECLARATION-GROUP'>/pkg/group1</MODE-GROUP-REF>
                </MODE-REQUEST-TYPE-MAP>
                <MODE-REQUEST-TYPE-MAP>
                    <IMPLEMENTATION-DATA-TYPE-REF DEST='ABSTRACT-IMPLEMENTATION-DATA-TYPE'>/pkg/idt2</IMPLEMENTATION-DATA-TYPE-REF>
                    <MODE-GROUP-REF DEST='MODE-DECLARATION-GROUP'>/pkg/group2</MODE-GROUP-REF>
                </MODE-REQUEST-TYPE-MAP>
            </MODE-REQUEST-TYPE-MAPS>""",
        )

        maps = mapping_set.getModeRequestTypeMaps()
        assert len(maps) == 2
        assert maps[0].getImplementationDataTypeRef().getValue() == "/pkg/idt1"
        assert maps[1].getModeGroupRef().getValue() == "/pkg/group2"

    def test_read_absent_refs(self, parser):
        """
        Test that omitted ref elements inside a MODE-REQUEST-TYPE-MAP stay
        None (0..1).
        """
        mapping_set = _mapping_set()
        _parse(
            parser,
            mapping_set,
            """<MODE-REQUEST-TYPE-MAPS>
                <MODE-REQUEST-TYPE-MAP>
                    <IMPLEMENTATION-DATA-TYPE-REF DEST='ABSTRACT-IMPLEMENTATION-DATA-TYPE'>/pkg/mode-idt</IMPLEMENTATION-DATA-TYPE-REF>
                </MODE-REQUEST-TYPE-MAP>
            </MODE-REQUEST-TYPE-MAPS>""",
        )

        mode_map = mapping_set.getModeRequestTypeMaps()[0]
        assert mode_map.getImplementationDataTypeRef().getValue() == "/pkg/mode-idt"
        assert mode_map.getModeGroupRef() is None

    def test_read_no_wrapper(self, parser):
        """
        Test that a DATA-TYPE-MAPPING-SET without MODE-REQUEST-TYPE-MAPS
        yields an empty map list.
        """
        mapping_set = _mapping_set()
        _parse(parser, mapping_set, "")

        assert mapping_set.getModeRequestTypeMaps() == []
