"""
Tests for writing ECUC-CHOICE-CONTAINER-DEF content —
EcucChoiceContainerDef, Table 2.5 (p.41, R23-11).

XSD group ECUC-CHOICE-CONTAINER-DEF (AUTOSAR_00052.xsd) element order:
CHOICES (wrapper, ECUC-PARAM-CONF-CONTAINER-DEF).

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_choice_container_def.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucChoiceContainerDef
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucChoiceContainerDef:
    """Tests for writeEcucChoiceContainerDef — own element field values (Table 2.5)."""

    def _make(self):
        return EcucChoiceContainerDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Choice")

    def _write(self, container) -> ET.Element:
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeEcucChoiceContainerDef(parent, container)
        return parent.find("ECUC-CHOICE-CONTAINER-DEF")

    def test_write_empty(self):
        """Test that an EcucChoiceContainerDef without choices emits only the inherited content."""
        child_element = self._write(self._make())

        assert child_element.find("SHORT-NAME").text == "Choice"
        assert child_element.find("CHOICES") is None

    def test_write_choices_in_xsd_order(self):
        """Test that choices are wrapped in CHOICES in list order."""
        container = self._make()
        container.createEcucParamConfContainerDef("C1")
        container.createEcucParamConfContainerDef("C2")

        child_element = self._write(container)

        choices = child_element.find("CHOICES")
        assert choices is not None
        defs = choices.findall("ECUC-PARAM-CONF-CONTAINER-DEF")
        assert [d.find("SHORT-NAME").text for d in defs] == ["C1", "C2"]
