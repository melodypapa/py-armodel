"""
Tests for writing ARPackage PORT-INTERFACE-MAPPING-SET elements — Table 4.19 (portInterfaceMapping aggr).

Round-trip counterpart: tests/test_armodel/parser/test_ar_package_port_interface_mapping_set.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototypeMapping
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import TriggerMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    PortInterfaceMappingSet,
)
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


def _mapping_set() -> PortInterfaceMappingSet:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return PortInterfaceMappingSet(ar_root, "pims")


def _ref(value: str) -> RefType:
    return RefType().setValue(value)


class TestWritePortInterfaceMappingSet:
    """
    Test writePortInterfaceMappingSet (ARPackage.element, Table 4.19).
    """

    def test_write_field_values(self, writer):
        """
        Test that each created mapping is written under PORT-INTERFACE-MAPPINGS
        with its own tag and SHORT-NAME, in list order.
        """
        mapping_set = _mapping_set()
        mapping_set.createVariableAndParameterInterfaceMapping("vpm")
        mapping_set.createClientServerInterfaceMapping("csim")
        mapping_set.createModeInterfaceMapping("mim")

        element = ET.Element("PARENT")
        writer.writePortInterfaceMappingSet(element, mapping_set)

        set_tag = element.find("PORT-INTERFACE-MAPPING-SET")
        assert set_tag is not None
        assert set_tag.find("SHORT-NAME").text == "pims"

        wrapper = set_tag.find("PORT-INTERFACE-MAPPINGS")
        assert wrapper is not None
        children = list(wrapper)
        assert [c.tag for c in children] == [
            "VARIABLE-AND-PARAMETER-INTERFACE-MAPPING",
            "CLIENT-SERVER-INTERFACE-MAPPING",
            "MODE-INTERFACE-MAPPING",
        ]
        assert [c.find("SHORT-NAME").text for c in children] == ["vpm", "csim", "mim"]

    def test_write_trigger_mapping(self, writer):
        """
        Test that a TriggerInterfaceMapping in the list is written as a
        TRIGGER-INTERFACE-MAPPING element with its TRIGGER-MAPPINGS refs.
        """
        mapping_set = _mapping_set()
        tim = mapping_set.createTriggerInterfaceMapping("tim")

        trigger_mapping = TriggerMapping()
        trigger_mapping.setFirstTriggerRef(_ref("/pkg/trigger1"))
        trigger_mapping.setSecondTriggerRef(_ref("/pkg/trigger2"))
        tim.addTriggerMapping(trigger_mapping)

        element = ET.Element("PARENT")
        writer.writePortInterfaceMappingSet(element, mapping_set)

        wrapper = element.find("PORT-INTERFACE-MAPPING-SET/PORT-INTERFACE-MAPPINGS")
        assert wrapper is not None
        tim_tag = wrapper.find("TRIGGER-INTERFACE-MAPPING")
        assert tim_tag is not None
        assert tim_tag.find("SHORT-NAME").text == "tim"

        trigger_mapping_tag = tim_tag.find("TRIGGER-MAPPINGS/TRIGGER-MAPPING")
        assert trigger_mapping_tag is not None
        assert trigger_mapping_tag.find("FIRST-TRIGGER-REF").text == "/pkg/trigger1"
        assert trigger_mapping_tag.find("SECOND-TRIGGER-REF").text == "/pkg/trigger2"

    def test_write_empty_wrapper_list(self, writer):
        """
        Test that no PORT-INTERFACE-MAPPINGS wrapper is written when the
        mapping list is empty.
        """
        mapping_set = _mapping_set()

        element = ET.Element("PARENT")
        writer.writePortInterfaceMappingSet(element, mapping_set)

        set_tag = element.find("PORT-INTERFACE-MAPPING-SET")
        assert set_tag is not None
        assert set_tag.find("PORT-INTERFACE-MAPPINGS") is None


class TestWriteModeInterfaceMappingModeMapping:
    """
    Test the MODE-MAPPING child of MODE-INTERFACE-MAPPING —
    ModeDeclarationGroupPrototypeMapping (SWC TPS Table 4.27, all attrs 0..1 refs).
    """

    @staticmethod
    def _mode_mapping() -> ModeDeclarationGroupPrototypeMapping:
        mm = ModeDeclarationGroupPrototypeMapping()
        mm.setFirstModeGroupRef(RefType().setValue("/pkg/first").setDest("MODE-GROUP"))
        mm.setModeDeclarationMappingSetRef(RefType().setValue("/pkg/set1").setDest("MODE-DECLARATION-MAPPING-SET"))
        mm.setSecondModeGroupRef(RefType().setValue("/pkg/second").setDest("MODE-GROUP"))
        return mm

    def test_write_mode_mapping_field_values(self, writer):
        """
        Test that all three refs are written with value and DEST, in XSD
        element order (FIRST, MODE-DECLARATION-MAPPING-SET, SECOND).
        """
        mapping_set = _mapping_set()
        mim = mapping_set.createModeInterfaceMapping("mim")
        mim.setModeMapping(self._mode_mapping())

        element = ET.Element("PARENT")
        writer.writePortInterfaceMappingSet(element, mapping_set)

        mm_tag = element.find("PORT-INTERFACE-MAPPING-SET/PORT-INTERFACE-MAPPINGS/MODE-INTERFACE-MAPPING/MODE-MAPPING")
        assert mm_tag is not None
        children = list(mm_tag)
        assert [c.tag for c in children] == [
            "FIRST-MODE-GROUP-REF",
            "MODE-DECLARATION-MAPPING-SET-REF",
            "SECOND-MODE-GROUP-REF",
        ]
        assert children[0].text == "/pkg/first"
        assert children[0].attrib["DEST"] == "MODE-GROUP"
        assert children[1].text == "/pkg/set1"
        assert children[1].attrib["DEST"] == "MODE-DECLARATION-MAPPING-SET"
        assert children[2].text == "/pkg/second"
        assert children[2].attrib["DEST"] == "MODE-GROUP"

    def test_write_mode_mapping_absent_refs(self, writer):
        """
        Test that unset refs emit no elements (0..1) and no MODE-MAPPING is
        written when the mapping itself is absent.
        """
        mapping_set = _mapping_set()
        mim = mapping_set.createModeInterfaceMapping("mim")
        mm = ModeDeclarationGroupPrototypeMapping()
        mm.setFirstModeGroupRef(RefType().setValue("/pkg/first").setDest("MODE-GROUP"))
        mim.setModeMapping(mm)

        mapping_set.createModeInterfaceMapping("mim2")

        element = ET.Element("PARENT")
        writer.writePortInterfaceMappingSet(element, mapping_set)

        wrapper = element.find("PORT-INTERFACE-MAPPING-SET/PORT-INTERFACE-MAPPINGS")
        mim_tag = wrapper.find("MODE-INTERFACE-MAPPING")
        mm_tag = mim_tag.find("MODE-MAPPING")
        assert mm_tag is not None
        assert [c.tag for c in mm_tag] == ["FIRST-MODE-GROUP-REF"]
        assert mm_tag.find("FIRST-MODE-GROUP-REF").text == "/pkg/first"

        mim2_tag = list(wrapper)[1]
        assert mim2_tag.find("MODE-MAPPING") is None

    def test_round_trip_field_values(self, writer):
        """
        Test write → read round-trip preserves all three ref values and DESTs.
        """
        mapping_set = _mapping_set()
        mim = mapping_set.createModeInterfaceMapping("mim")
        mim.setModeMapping(self._mode_mapping())

        parent = ET.Element("PARENT")
        writer.writeModeInterfaceMapping(parent, mim)

        xml_text = ET.tostring(parent, encoding="unicode")
        reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

        mapping_set2 = _mapping_set()
        mim2 = mapping_set2.createModeInterfaceMapping("mim")
        ARXMLParser().readModeInterfaceMapping(reparsed[0], mim2)

        mm2 = mim2.getModeMapping()
        assert isinstance(mm2, ModeDeclarationGroupPrototypeMapping)
        assert mm2.getFirstModeGroupRef().getValue() == "/pkg/first"
        assert mm2.getFirstModeGroupRef().getDest() == "MODE-GROUP"
        assert mm2.getModeDeclarationMappingSetRef().getValue() == "/pkg/set1"
        assert mm2.getModeDeclarationMappingSetRef().getDest() == "MODE-DECLARATION-MAPPING-SET"
        assert mm2.getSecondModeGroupRef().getValue() == "/pkg/second"
        assert mm2.getSecondModeGroupRef().getDest() == "MODE-GROUP"
