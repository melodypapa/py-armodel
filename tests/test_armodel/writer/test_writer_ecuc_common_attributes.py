"""
Tests for writing ECUC-COMMON-ATTRIBUTES content —
EcucCommonAttributes, Table 2.8 (p.49, R23-11).

XSD group ECUC-COMMON-ATTRIBUTES (AUTOSAR_00052.xsd) element order:
MULTIPLICITY-CONFIG-CLASSES, ORIGIN, POST-BUILD-VARIANT-MULTIPLICITY,
POST-BUILD-VARIANT-VALUE, REQUIRES-INDEX, VALUE-CONFIG-CLASSES.
(CONFIGURATION-CLASS-AFFECTION and IMPLEMENTATION-CONFIG-CLASSES are absent
from the markdown table and are not modeled — Rule 0015.)

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_common_attributes.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucCommonAttributes, EcucMultiplicityConfigurationClass, EcucValueConfigurationClass
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, String
from armodel.writer.arxml_writer import ARXMLWriter


class _Concrete(EcucCommonAttributes):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucCommonAttributes:
    """Tests for writeEcucCommonAttributes — own element field values (Table 2.8)."""

    def _make(self):
        return _Concrete(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Holder")

    def test_write_empty(self):
        """Test that an EcucCommonAttributes without own attributes emits only the inherited content."""
        element = ET.Element("ECUC-INTEGER-PARAM-DEF")
        ARXMLWriter().writeEcucCommonAttributes(element, self._make())

        assert element.find("MULTIPLICITY-CONFIG-CLASSES") is None
        assert element.find("ORIGIN") is None
        assert element.find("POST-BUILD-VARIANT-MULTIPLICITY") is None
        assert element.find("POST-BUILD-VARIANT-VALUE") is None
        assert element.find("REQUIRES-INDEX") is None
        assert element.find("VALUE-CONFIG-CLASSES") is None

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD group order with the spec values."""
        holder = self._make()
        holder.addMultiplicityConfigClass(EcucMultiplicityConfigurationClass())
        origin = String()
        origin.setValue("VENDOR")
        holder.setOrigin(origin)
        pbvm = Boolean()
        pbvm.setValue(True)
        holder.setPostBuildVariantMultiplicity(pbvm)
        pbvv = Boolean()
        pbvv.setValue(False)
        holder.setPostBuildVariantValue(pbvv)
        ri = Boolean()
        ri.setValue(True)
        holder.setRequiresIndex(ri)
        holder.addValueConfigClass(EcucValueConfigurationClass())

        element = ET.Element("ECUC-INTEGER-PARAM-DEF")
        ARXMLWriter().writeEcucCommonAttributes(element, holder)

        tags = [c.tag for c in element]
        assert tags == ["SHORT-NAME", "MULTIPLICITY-CONFIG-CLASSES", "ORIGIN", "POST-BUILD-VARIANT-MULTIPLICITY", "POST-BUILD-VARIANT-VALUE", "REQUIRES-INDEX", "VALUE-CONFIG-CLASSES"]
        assert element.find("ORIGIN").text == "VENDOR"
        assert element.find("POST-BUILD-VARIANT-MULTIPLICITY").text == "true"
        assert element.find("POST-BUILD-VARIANT-VALUE").text == "false"
        assert element.find("REQUIRES-INDEX").text == "true"
        assert element.find("MULTIPLICITY-CONFIG-CLASSES/ECUC-MULTIPLICITY-CONFIGURATION-CLASS") is not None
        assert element.find("VALUE-CONFIG-CLASSES/ECUC-VALUE-CONFIGURATION-CLASS") is not None
