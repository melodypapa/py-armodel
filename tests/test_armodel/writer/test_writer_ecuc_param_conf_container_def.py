"""
Tests for writing ECUC-PARAM-CONF-CONTAINER-DEF content —
EcucParamConfContainerDef, Table 2.4 (p.39, R23-11).

XSD group ECUC-PARAM-CONF-CONTAINER-DEF (AUTOSAR_00052.xsd l.53080) element order
(after the inherited ECUC-CONTAINER-DEF group): PARAMETERS, REFERENCES,
SUB-CONTAINERS.

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_param_conf_container_def.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucParamConfContainerDef:
    """Tests for writeEcucParamConfContainerDef — own element field values (Table 2.4)."""

    def _make(self):
        return EcucParamConfContainerDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Container")

    def _write(self, container) -> ET.Element:
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeEcucParamConfContainerDef(parent, container)
        return parent.find("ECUC-PARAM-CONF-CONTAINER-DEF")

    def test_write_empty(self):
        """Test that an EcucParamConfContainerDef without aggregations emits only the inherited content."""
        child_element = self._write(self._make())

        assert child_element.find("SHORT-NAME").text == "Container"
        assert child_element.find("PARAMETERS") is None
        assert child_element.find("REFERENCES") is None
        assert child_element.find("SUB-CONTAINERS") is None

    def test_write_parameters_references_subcontainers_in_xsd_order(self):
        """Test that the three aggregations are emitted in XSD group order."""
        container = self._make()
        container.createEcucIntegerParamDef("P1")
        container.createEcucReferenceDef("R1")
        container.createEcucParamConfContainerDef("S1")

        child_element = self._write(container)

        tags = [c.tag for c in child_element]
        assert tags == ["SHORT-NAME", "PARAMETERS", "REFERENCES", "SUB-CONTAINERS"]
        assert child_element.find("PARAMETERS/ECUC-INTEGER-PARAM-DEF/SHORT-NAME").text == "P1"
        assert child_element.find("REFERENCES/ECUC-REFERENCE-DEF/SHORT-NAME").text == "R1"
        assert child_element.find("SUB-CONTAINERS/ECUC-PARAM-CONF-CONTAINER-DEF/SHORT-NAME").text == "S1"
