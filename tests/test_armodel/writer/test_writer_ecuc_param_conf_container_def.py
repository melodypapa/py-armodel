"""
Tests for writing ECUC-PARAM-CONF-CONTAINER-DEF elements —
EcucParamConfContainerDef, Table 2.4 (p.39, R23-11).

XSD group ECUC-PARAM-CONF-CONTAINER-DEF (AUTOSAR_00052.xsd) wrapper order:
PARAMETERS, REFERENCES, SUB-CONTAINERS (multipleConfigurationContainer is
atp.Status="removed" and not modeled).

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

    def test_write_empty(self):
        """Test that a container without aggregations emits no wrapper elements."""
        container = EcucParamConfContainerDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Container1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucParamConfContainerDef(parent, container)

        child = parent.find("ECUC-PARAM-CONF-CONTAINER-DEF")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Container1"
        assert child.find("PARAMETERS") is None
        assert child.find("REFERENCES") is None
        assert child.find("SUB-CONTAINERS") is None

    def test_write_wrappers_in_xsd_order(self):
        """Test that the aggregations are emitted under their wrappers in XSD order."""
        container = EcucParamConfContainerDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Container1")
        container.createEcucBooleanParamDef("Param1")
        container.createEcucReferenceDef("Ref1")
        container.createEcucParamConfContainerDef("Sub1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucParamConfContainerDef(parent, container)

        child = parent.find("ECUC-PARAM-CONF-CONTAINER-DEF")
        tags = [c.tag for c in child]
        assert tags == ["SHORT-NAME", "PARAMETERS", "REFERENCES", "SUB-CONTAINERS"]
        assert len(child.findall("PARAMETERS/ECUC-BOOLEAN-PARAM-DEF")) == 1
        assert len(child.findall("REFERENCES/ECUC-REFERENCE-DEF")) == 1
        assert len(child.findall("SUB-CONTAINERS/ECUC-PARAM-CONF-CONTAINER-DEF")) == 1
