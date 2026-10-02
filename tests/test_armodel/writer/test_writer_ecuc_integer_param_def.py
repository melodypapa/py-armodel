"""
Tests for writing ECUC-INTEGER-PARAM-DEF elements —
EcucIntegerParamDef, Table 2.16 (p.60, R23-11).

Element order (XSD group ECUC-INTEGER-PARAM-DEF): DEFAULT-VALUE, MAX, MIN.

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_integer_param_def.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucIntegerParamDef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import UnlimitedInteger
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucIntegerParamDef:
    """Tests for writeEcucIntegerParamDef — own element field values (Table 2.16)."""

    def test_write_empty(self):
        """Test that a parameter without values emits no own-field elements."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucIntegerParamDef(parent, EcucIntegerParamDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Param1"))

        element = parent.find("ECUC-INTEGER-PARAM-DEF")
        assert element is not None
        assert [c.tag for c in element] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that defaultValue/max/min are emitted in XSD order with the spec values."""
        param = EcucIntegerParamDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Param1")
        param.setDefaultValue(UnlimitedInteger().setValue(10))
        param.setMax(UnlimitedInteger().setValue(100))
        param.setMin(UnlimitedInteger().setValue(1))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucIntegerParamDef(parent, param)

        element = parent.find("ECUC-INTEGER-PARAM-DEF")
        assert [c.tag for c in element] == ["SHORT-NAME", "DEFAULT-VALUE", "MAX", "MIN"]
        assert element.find("DEFAULT-VALUE").text == "10"
        assert element.find("MAX").text == "100"
        assert element.find("MIN").text == "1"
