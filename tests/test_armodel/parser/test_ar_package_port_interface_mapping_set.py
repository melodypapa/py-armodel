"""
Tests for parsing ARPackage PORT-INTERFACE-MAPPING-SET elements — Table 4.19 (portInterfaceMapping aggr).

Round-trip counterpart: tests/test_armodel/writer/test_ar_package_port_interface_mapping_set.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ClientServerInterfaceMapping,
    ModeInterfaceMapping,
    PortInterfaceMappingSet,
    VariableAndParameterInterfaceMapping,
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


def _mapping_set(short_name: str = "pims") -> PortInterfaceMappingSet:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return PortInterfaceMappingSet(ar_root, short_name)


def _parse(parser: ARXMLParser, mapping_set: PortInterfaceMappingSet, inner: str):
    element = ET.fromstring(
        f"""<PORT-INTERFACE-MAPPING-SET xmlns='{NS}'>
            <SHORT-NAME>pims</SHORT-NAME>
            {inner}
        </PORT-INTERFACE-MAPPING-SET>"""
    )
    parser.readPortInterfaceMappingSet(element, mapping_set)


class TestReadPortInterfaceMappingSet:
    """
    Test readPortInterfaceMappingSet (ARPackage.element, Table 4.19).
    """

    def test_read_field_values(self, parser):
        """
        Test that each PORT-INTERFACE-MAPPINGS child populates a typed
        PortInterfaceMapping with its short name, in document order.
        """
        mapping_set = _mapping_set()
        _parse(
            parser,
            mapping_set,
            """<PORT-INTERFACE-MAPPINGS>
                <VARIABLE-AND-PARAMETER-INTERFACE-MAPPING>
                    <SHORT-NAME>vpm</SHORT-NAME>
                </VARIABLE-AND-PARAMETER-INTERFACE-MAPPING>
                <CLIENT-SERVER-INTERFACE-MAPPING>
                    <SHORT-NAME>csim</SHORT-NAME>
                </CLIENT-SERVER-INTERFACE-MAPPING>
                <MODE-INTERFACE-MAPPING>
                    <SHORT-NAME>mim</SHORT-NAME>
                </MODE-INTERFACE-MAPPING>
            </PORT-INTERFACE-MAPPINGS>""",
        )

        mappings = mapping_set.getPortInterfaceMappings()
        assert [m.short_name for m in mappings] == ["vpm", "csim", "mim"]
        assert isinstance(mappings[0], VariableAndParameterInterfaceMapping)
        assert isinstance(mappings[1], ClientServerInterfaceMapping)
        assert isinstance(mappings[2], ModeInterfaceMapping)
        assert all(m.parent is mapping_set for m in mappings)

    def test_read_trigger_mapping(self, parser):
        """
        Test that a TRIGGER-INTERFACE-MAPPING child (with TRIGGER-MAPPINGS refs)
        is dispatched to createTriggerInterfaceMapping and populated.
        """
        mapping_set = _mapping_set()
        _parse(
            parser,
            mapping_set,
            """<PORT-INTERFACE-MAPPINGS>
                <TRIGGER-INTERFACE-MAPPING>
                    <SHORT-NAME>tim</SHORT-NAME>
                    <TRIGGER-MAPPINGS>
                        <TRIGGER-MAPPING>
                            <FIRST-TRIGGER-REF DEST='TRIGGER'>/pkg/trigger1</FIRST-TRIGGER-REF>
                            <SECOND-TRIGGER-REF DEST='TRIGGER'>/pkg/trigger2</SECOND-TRIGGER-REF>
                        </TRIGGER-MAPPING>
                    </TRIGGER-MAPPINGS>
                </TRIGGER-INTERFACE-MAPPING>
            </PORT-INTERFACE-MAPPINGS>""",
        )

        mappings = mapping_set.getPortInterfaceMappings()
        assert len(mappings) == 1
        assert mappings[0].short_name == "tim"

        trigger_mappings = mappings[0].getTriggerMappings()
        assert len(trigger_mappings) == 1
        assert trigger_mappings[0].getFirstTriggerRef().getValue() == "/pkg/trigger1"
        assert trigger_mappings[0].getSecondTriggerRef().getValue() == "/pkg/trigger2"

    def test_read_empty_wrapper_list(self, parser):
        """
        Test that a PORT-INTERFACE-MAPPING-SET without PORT-INTERFACE-MAPPINGS
        yields an empty mapping list.
        """
        mapping_set = _mapping_set()
        _parse(parser, mapping_set, "")

        assert mapping_set.getPortInterfaceMappings() == []
