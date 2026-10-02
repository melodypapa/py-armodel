"""
Tests for writing ECUC-CHOICE-CONTAINER-DEF elements —
EcucChoiceContainerDef, Table 2.5 (p.41, R23-11).

XSD group ECUC-CHOICE-CONTAINER-DEF (AUTOSAR_00052.xsd) wrapper order: CHOICES.

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

    def test_write_empty(self):
        """Test that a choice container without choices emits no CHOICES wrapper."""
        container = EcucChoiceContainerDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Choice1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucChoiceContainerDef(parent, container)

        child = parent.find("ECUC-CHOICE-CONTAINER-DEF")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Choice1"
        assert child.find("CHOICES") is None

    def test_write_choices(self):
        """Test that the choices aggregation is emitted under CHOICES with the spec values."""
        container = EcucChoiceContainerDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Choice1")
        container.createEcucParamConfContainerDef("ChoiceA")
        container.createEcucParamConfContainerDef("ChoiceB")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucChoiceContainerDef(parent, container)

        child = parent.find("ECUC-CHOICE-CONTAINER-DEF")
        choices_tag = child.find("CHOICES")
        assert choices_tag is not None
        choices = choices_tag.findall("ECUC-PARAM-CONF-CONTAINER-DEF")
        assert len(choices) == 2
        assert choices[0].find("SHORT-NAME").text == "ChoiceA"
        assert choices[1].find("SHORT-NAME").text == "ChoiceB"
