"""
Tests for writing ARPackage PORT-INTERFACE-MAPPING-SET elements — Table 4.19 (portInterfaceMapping aggr).

Round-trip counterpart: tests/test_armodel/parser/test_ar_package_port_interface_mapping_set.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import TriggerMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    PortInterfaceMappingSet,
)
from armodel.writer.arxml_writer import ARXMLWriter


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
