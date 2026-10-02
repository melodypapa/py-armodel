"""
Tests for writing EcucAbstractStringParamDef content (Table 2.18, p.63,
abstract — via concrete subclass).

Element order (XSD group ECUC-ABSTRACT-STRING-PARAM-DEF): DEFAULT-VALUE,
MAX-LENGTH, MIN-LENGTH, REGULAR-EXPRESSION.

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_abstract_string_param_def.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucStringParamDef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RegularExpression, VerbatimString
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucAbstractStringParamDef:
    """Tests for writeEcucAbstractStringParamDef — own element field values (Table 2.18)."""

    def test_write_empty(self):
        """Test that a string param without values emits no own-field elements."""
        element = ET.Element("ECUC-STRING-PARAM-DEF")
        ARXMLWriter().writeEcucAbstractStringParamDef(element, EcucStringParamDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Param1"))

        assert [c.tag for c in element if c.tag != "SHORT-NAME"] == []

    def test_write_fields_in_xsd_order(self):
        """Test that defaultValue/maxLength/minLength/regularExpression are emitted in XSD order with the spec values."""
        param = EcucStringParamDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Param1")
        param.setDefaultValue(VerbatimString().setValue("default"))
        param.setMaxLength(PositiveInteger().setValue(32))
        param.setMinLength(PositiveInteger().setValue(1))
        param.setRegularExpression(RegularExpression().setValue("[a-z]+"))

        element = ET.Element("ECUC-STRING-PARAM-DEF")
        ARXMLWriter().writeEcucAbstractStringParamDef(element, param)

        assert [c.tag for c in element] == ["SHORT-NAME", "DEFAULT-VALUE", "MAX-LENGTH", "MIN-LENGTH", "REGULAR-EXPRESSION"]
        assert element.find("DEFAULT-VALUE").text == "default"
        assert element.find("MAX-LENGTH").text == "32"
        assert element.find("MIN-LENGTH").text == "1"
        assert element.find("REGULAR-EXPRESSION").text == "[a-z]+"
