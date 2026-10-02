"""
Tests for writing EcucParameterDef content (Table 2.14, p.57, abstract — via
concrete subclass).

Element order (XSD group ECUC-PARAMETER-DEF): DERIVATION, SYMBOLIC-NAME-VALUE,
WITH-AUTO.

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_parameter_def.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucDerivationSpecification, EcucIntegerParamDef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucParameterDef:
    """Tests for writeEcucParameterDef — own element field values (Table 2.14)."""

    def test_write_empty(self):
        """Test that a parameter without attributes emits no own-field elements."""
        element = ET.Element("ECUC-INTEGER-PARAM-DEF")
        ARXMLWriter().writeEcucParameterDef(element, EcucIntegerParamDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Param1"))

        assert element.find("DERIVATION") is None
        assert element.find("SYMBOLIC-NAME-VALUE") is None
        assert element.find("WITH-AUTO") is None

    def test_write_fields_in_xsd_order(self):
        """Test that derivation/symbolicNameValue/withAuto are emitted in XSD order with the spec values."""
        param = EcucIntegerParamDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Param1")
        param.setDerivation(EcucDerivationSpecification())
        param.setSymbolicNameValue(Boolean().setValue(True))
        param.setWithAuto(Boolean().setValue(False))

        element = ET.Element("ECUC-INTEGER-PARAM-DEF")
        ARXMLWriter().writeEcucParameterDef(element, param)

        tags = [c.tag for c in element]
        assert tags == ["SHORT-NAME", "DERIVATION", "SYMBOLIC-NAME-VALUE", "WITH-AUTO"]
        assert element.find("SYMBOLIC-NAME-VALUE").text == "true"
        assert element.find("WITH-AUTO").text == "false"
