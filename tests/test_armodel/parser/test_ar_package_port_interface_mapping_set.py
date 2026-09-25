"""
Tests for parsing ARPackage PORT-INTERFACE-MAPPING-SET elements — Table 4.19 (portInterfaceMapping aggr).

Round-trip counterpart: tests/test_armodel/writer/test_ar_package_port_interface_mapping_set.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototypeMapping
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ClientServerApplicationErrorMapping,
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
    element = ET.fromstring(f"""<PORT-INTERFACE-MAPPING-SET xmlns='{NS}'>
            <SHORT-NAME>pims</SHORT-NAME>
            {inner}
        </PORT-INTERFACE-MAPPING-SET>""")
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


class TestReadModeInterfaceMappingModeMapping:
    """
    Test the MODE-MAPPING child of MODE-INTERFACE-MAPPING —
    ModeDeclarationGroupPrototypeMapping (SWC TPS Table 4.27, all attrs 0..1 refs).
    """

    def test_read_mode_mapping_field_values(self, parser):
        """
        Test that all three MODE-MAPPING refs populate the mapping with
        value and DEST preserved, in XSD element order.
        """
        mapping_set = _mapping_set()
        _parse(
            parser,
            mapping_set,
            """<PORT-INTERFACE-MAPPINGS>
                <MODE-INTERFACE-MAPPING>
                    <SHORT-NAME>mim</SHORT-NAME>
                    <MODE-MAPPING>
                        <FIRST-MODE-GROUP-REF DEST='MODE-GROUP'>/pkg/first</FIRST-MODE-GROUP-REF>
                        <MODE-DECLARATION-MAPPING-SET-REF DEST='MODE-DECLARATION-MAPPING-SET'>/pkg/set1</MODE-DECLARATION-MAPPING-SET-REF>
                        <SECOND-MODE-GROUP-REF DEST='MODE-GROUP'>/pkg/second</SECOND-MODE-GROUP-REF>
                    </MODE-MAPPING>
                </MODE-INTERFACE-MAPPING>
            </PORT-INTERFACE-MAPPINGS>""",
        )

        mim = mapping_set.getPortInterfaceMappings()[0]
        assert isinstance(mim, ModeInterfaceMapping)
        mm = mim.getModeMapping()
        assert isinstance(mm, ModeDeclarationGroupPrototypeMapping)
        assert mm.getFirstModeGroupRef().getValue() == "/pkg/first"
        assert mm.getFirstModeGroupRef().getDest() == "MODE-GROUP"
        assert mm.getModeDeclarationMappingSetRef().getValue() == "/pkg/set1"
        assert mm.getModeDeclarationMappingSetRef().getDest() == "MODE-DECLARATION-MAPPING-SET"
        assert mm.getSecondModeGroupRef().getValue() == "/pkg/second"
        assert mm.getSecondModeGroupRef().getDest() == "MODE-GROUP"

    def test_read_mode_mapping_absent_refs(self, parser):
        """
        Test that omitted MODE-MAPPING ref elements stay None (0..1).
        """
        mapping_set = _mapping_set()
        _parse(
            parser,
            mapping_set,
            """<PORT-INTERFACE-MAPPINGS>
                <MODE-INTERFACE-MAPPING>
                    <SHORT-NAME>mim</SHORT-NAME>
                    <MODE-MAPPING>
                        <FIRST-MODE-GROUP-REF DEST='MODE-GROUP'>/pkg/first</FIRST-MODE-GROUP-REF>
                    </MODE-MAPPING>
                </MODE-INTERFACE-MAPPING>
            </PORT-INTERFACE-MAPPINGS>""",
        )

        mm = mapping_set.getPortInterfaceMappings()[0].getModeMapping()
        assert mm.getFirstModeGroupRef().getValue() == "/pkg/first"
        assert mm.getModeDeclarationMappingSetRef() is None
        assert mm.getSecondModeGroupRef() is None

    def test_read_no_mode_mapping(self, parser):
        """
        Test that a MODE-INTERFACE-MAPPING without MODE-MAPPING leaves
        getModeMapping() as None.
        """
        mapping_set = _mapping_set()
        _parse(
            parser,
            mapping_set,
            """<PORT-INTERFACE-MAPPINGS>
                <MODE-INTERFACE-MAPPING>
                    <SHORT-NAME>mim</SHORT-NAME>
                </MODE-INTERFACE-MAPPING>
            </PORT-INTERFACE-MAPPINGS>""",
        )

        assert mapping_set.getPortInterfaceMappings()[0].getModeMapping() is None


class TestReadClientServerInterfaceMappingErrorMappings:
    """
    Test the ERROR-MAPPINGS children of CLIENT-SERVER-INTERFACE-MAPPING —
    ClientServerApplicationErrorMapping (SWC TPS Table 4.25, all attrs 0..1 refs).
    """

    def test_read_error_mappings_field_values(self, parser):
        """
        Test that both refs of a CLIENT-SERVER-APPLICATION-ERROR-MAPPING
        populate the mapping with value and DEST preserved, in XSD element order.
        """
        mapping_set = _mapping_set()
        _parse(
            parser,
            mapping_set,
            """<PORT-INTERFACE-MAPPINGS>
                <CLIENT-SERVER-INTERFACE-MAPPING>
                    <SHORT-NAME>csim</SHORT-NAME>
                    <ERROR-MAPPINGS>
                        <CLIENT-SERVER-APPLICATION-ERROR-MAPPING>
                            <FIRST-APPLICATION-ERROR-REF DEST='APPLICATION-ERROR'>/ifc1/err1</FIRST-APPLICATION-ERROR-REF>
                            <SECOND-APPLICATION-ERROR-REF DEST='APPLICATION-ERROR'>/ifc2/err2</SECOND-APPLICATION-ERROR-REF>
                        </CLIENT-SERVER-APPLICATION-ERROR-MAPPING>
                    </ERROR-MAPPINGS>
                </CLIENT-SERVER-INTERFACE-MAPPING>
            </PORT-INTERFACE-MAPPINGS>""",
        )

        csim = mapping_set.getPortInterfaceMappings()[0]
        assert isinstance(csim, ClientServerInterfaceMapping)
        error_mappings = csim.getErrorMappings()
        assert len(error_mappings) == 1
        em = error_mappings[0]
        assert isinstance(em, ClientServerApplicationErrorMapping)
        assert em.getFirstApplicationErrorRef().getValue() == "/ifc1/err1"
        assert em.getFirstApplicationErrorRef().getDest() == "APPLICATION-ERROR"
        assert em.getSecondApplicationErrorRef().getValue() == "/ifc2/err2"
        assert em.getSecondApplicationErrorRef().getDest() == "APPLICATION-ERROR"

    def test_read_multiple_error_mappings_document_order(self, parser):
        """
        Test that multiple CLIENT-SERVER-APPLICATION-ERROR-MAPPING items are
        appended in document order with their field values.
        """
        mapping_set = _mapping_set()
        _parse(
            parser,
            mapping_set,
            """<PORT-INTERFACE-MAPPINGS>
                <CLIENT-SERVER-INTERFACE-MAPPING>
                    <SHORT-NAME>csim</SHORT-NAME>
                    <ERROR-MAPPINGS>
                        <CLIENT-SERVER-APPLICATION-ERROR-MAPPING>
                            <FIRST-APPLICATION-ERROR-REF DEST='APPLICATION-ERROR'>/ifc1/errA</FIRST-APPLICATION-ERROR-REF>
                            <SECOND-APPLICATION-ERROR-REF DEST='APPLICATION-ERROR'>/ifc2/errB</SECOND-APPLICATION-ERROR-REF>
                        </CLIENT-SERVER-APPLICATION-ERROR-MAPPING>
                        <CLIENT-SERVER-APPLICATION-ERROR-MAPPING>
                            <FIRST-APPLICATION-ERROR-REF DEST='APPLICATION-ERROR'>/ifc3/errC</FIRST-APPLICATION-ERROR-REF>
                            <SECOND-APPLICATION-ERROR-REF DEST='APPLICATION-ERROR'>/ifc4/errD</SECOND-APPLICATION-ERROR-REF>
                        </CLIENT-SERVER-APPLICATION-ERROR-MAPPING>
                    </ERROR-MAPPINGS>
                </CLIENT-SERVER-INTERFACE-MAPPING>
            </PORT-INTERFACE-MAPPINGS>""",
        )

        error_mappings = mapping_set.getPortInterfaceMappings()[0].getErrorMappings()
        assert [em.getFirstApplicationErrorRef().getValue() for em in error_mappings] == ["/ifc1/errA", "/ifc3/errC"]
        assert [em.getSecondApplicationErrorRef().getValue() for em in error_mappings] == ["/ifc2/errB", "/ifc4/errD"]

    def test_read_error_mapping_absent_refs(self, parser):
        """
        Test that omitted ref elements stay None (0..1).
        """
        mapping_set = _mapping_set()
        _parse(
            parser,
            mapping_set,
            """<PORT-INTERFACE-MAPPINGS>
                <CLIENT-SERVER-INTERFACE-MAPPING>
                    <SHORT-NAME>csim</SHORT-NAME>
                    <ERROR-MAPPINGS>
                        <CLIENT-SERVER-APPLICATION-ERROR-MAPPING>
                            <FIRST-APPLICATION-ERROR-REF DEST='APPLICATION-ERROR'>/ifc1/err1</FIRST-APPLICATION-ERROR-REF>
                        </CLIENT-SERVER-APPLICATION-ERROR-MAPPING>
                    </ERROR-MAPPINGS>
                </CLIENT-SERVER-INTERFACE-MAPPING>
            </PORT-INTERFACE-MAPPINGS>""",
        )

        em = mapping_set.getPortInterfaceMappings()[0].getErrorMappings()[0]
        assert em.getFirstApplicationErrorRef().getValue() == "/ifc1/err1"
        assert em.getSecondApplicationErrorRef() is None

    def test_read_no_error_mappings(self, parser):
        """
        Test that a CLIENT-SERVER-INTERFACE-MAPPING without ERROR-MAPPINGS
        leaves the error mapping list empty.
        """
        mapping_set = _mapping_set()
        _parse(
            parser,
            mapping_set,
            """<PORT-INTERFACE-MAPPINGS>
                <CLIENT-SERVER-INTERFACE-MAPPING>
                    <SHORT-NAME>csim</SHORT-NAME>
                </CLIENT-SERVER-INTERFACE-MAPPING>
            </PORT-INTERFACE-MAPPINGS>""",
        )

        assert mapping_set.getPortInterfaceMappings()[0].getErrorMappings() == []
