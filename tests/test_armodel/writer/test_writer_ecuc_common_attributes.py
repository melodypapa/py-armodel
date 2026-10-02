"""
Tests for writing EcucCommonAttributes content (Table 2.8, p.49, abstract — via
concrete subclass).

XSD group ECUC-COMMON-ATTRIBUTES (AUTOSAR_00052.xsd l.51349) element order:
MULTIPLICITY-CONFIG-CLASSES, ORIGIN, POST-BUILD-VARIANT-MULTIPLICITY,
POST-BUILD-VARIANT-VALUE, REQUIRES-INDEX, VALUE-CONFIG-CLASSES.

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_common_attributes.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucIntegerParamDef, EcucMultiplicityConfigurationClass, EcucValueConfigurationClass
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, String
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucCommonAttributes:
    """Tests for writeEcucCommonAttributes — own element field values (Table 2.8)."""

    def _make_obj(self):
        return EcucIntegerParamDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Param1")

    def test_write_empty(self):
        """Test that common attributes without values emit no own-field elements."""
        element = ET.Element("ECUC-INTEGER-PARAM-DEF")
        ARXMLWriter().writeEcucCommonAttributes(element, self._make_obj())

        assert element.find("MULTIPLICITY-CONFIG-CLASSES") is None
        assert element.find("ORIGIN") is None
        assert element.find("POST-BUILD-VARIANT-MULTIPLICITY") is None
        assert element.find("POST-BUILD-VARIANT-VALUE") is None
        assert element.find("REQUIRES-INDEX") is None
        assert element.find("VALUE-CONFIG-CLASSES") is None

    def test_write_fields_in_xsd_order(self):
        """Test that all common attributes are emitted in XSD order with the spec values."""
        obj = self._make_obj()
        obj.addMultiplicityConfigClass(EcucMultiplicityConfigurationClass())
        obj.setOrigin(String().setValue("AUTOSAR Ecuc Definition Collection"))
        obj.setPostBuildVariantMultiplicity(Boolean().setValue(True))
        obj.setPostBuildVariantValue(Boolean().setValue(False))
        obj.setRequiresIndex(Boolean().setValue(True))
        obj.addValueConfigClass(EcucValueConfigurationClass())

        element = ET.Element("ECUC-INTEGER-PARAM-DEF")
        ARXMLWriter().writeEcucCommonAttributes(element, obj)

        tags = [c.tag for c in element]
        assert tags == ["SHORT-NAME", "MULTIPLICITY-CONFIG-CLASSES", "ORIGIN", "POST-BUILD-VARIANT-MULTIPLICITY", "POST-BUILD-VARIANT-VALUE", "REQUIRES-INDEX", "VALUE-CONFIG-CLASSES"]
        assert element.find("ORIGIN").text == "AUTOSAR Ecuc Definition Collection"
        assert element.find("POST-BUILD-VARIANT-MULTIPLICITY").text == "true"
        assert element.find("POST-BUILD-VARIANT-VALUE").text == "false"
        assert element.find("REQUIRES-INDEX").text == "true"
