"""
Tests for writing the enumeration-param family (Tables 2.23/2.24/2.25, R23-11).

Element orders (XSD groups): ECUC-ENUMERATION-PARAM-DEF → DEFAULT-VALUE,
LITERALS; ECUC-ENUMERATION-LITERAL-DEF → ECUC-COND, ORIGIN;
ECUC-ADD-INFO-PARAM-DEF → parameter-def content only.

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_enum_param_family.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucAddInfoParamDef, EcucEnumerationLiteralDef, EcucEnumerationParamDef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, String
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucEnumerationParamDef:
    def test_write_wrappers_in_xsd_order(self):
        """Test that defaultValue and literals are emitted under their wrappers in XSD order."""
        param = EcucEnumerationParamDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Param1")
        param.setDefaultValue(Identifier().setValue("LITERAL_1"))
        param.createLiteral("Literal1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucEnumerationParamDef(parent, param)

        child = parent.find("ECUC-ENUMERATION-PARAM-DEF")
        assert child.find("DEFAULT-VALUE").text == "LITERAL_1"
        literals = child.findall("LITERALS/ECUC-ENUMERATION-LITERAL-DEF")
        assert len(literals) == 1
        assert literals[0].find("SHORT-NAME").text == "Literal1"


class TestWriteEcucEnumerationLiteralDef:
    def test_write_origin(self):
        """Test that origin is emitted with the spec value."""
        literal = EcucEnumerationLiteralDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Literal1")
        literal.setOrigin(String().setValue("AUTOSAR Ecuc Definition Collection"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucEnumerationLiteralDef(parent, literal)

        child = parent.find("ECUC-ENUMERATION-LITERAL-DEF")
        assert child.find("SHORT-NAME").text == "Literal1"
        assert child.find("ORIGIN").text == "AUTOSAR Ecuc Definition Collection"


class TestWriteEcucAddInfoParamDef:
    def test_write_wrapper(self):
        """Test that the attribute-less param emits its wrapper with inherited content only."""
        param = EcucAddInfoParamDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Param1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucAddInfoParamDef(parent, param)

        child = parent.find("ECUC-ADD-INFO-PARAM-DEF")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Param1"
