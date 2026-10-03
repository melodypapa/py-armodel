"""
Tests for writing ECUC-MODULE-DEF content —
EcucModuleDef, Table 2.2 (p.32, R23-11).

XSD group ECUC-MODULE-DEF (AUTOSAR_00052.xsd) element order:
API-SERVICE-PREFIX, POST-BUILD-VARIANT-SUPPORT, REFINED-MODULE-DEF-REF,
SUPPORTED-CONFIG-VARIANTS, CONTAINERS (xml.sequenceOffset=11).

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_module_def.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucConfigurationVariantEnum, EcucModuleDef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, CIdentifier, RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucModuleDef:
    """Tests for writeEcucModuleDef — own element field values (Table 2.2)."""

    def _make(self):
        return EcucModuleDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "ModuleDef")

    def _write(self, module_def) -> ET.Element:
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeEcucModuleDef(parent, module_def)
        return parent.find("ECUC-MODULE-DEF")

    def test_write_empty(self):
        """Test that an EcucModuleDef without own attributes emits only the IDENTIFIABLE content (no empty CONTAINERS wrapper)."""
        child_element = self._write(self._make())

        assert child_element.find("SHORT-NAME").text == "ModuleDef"
        assert [c.tag for c in child_element] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD group order with the spec values."""
        module_def = self._make()
        prefix = CIdentifier()
        prefix.setValue("Com")
        module_def.setApiServicePrefix(prefix)
        support = Boolean()
        support.setValue(True)
        module_def.setPostBuildVariantSupport(support)
        module_def.setRefinedModuleDefRef(RefType().setValue("/EcucModuleDefs/Standard").setDest("ECUC-MODULE-DEF"))
        variant = EcucConfigurationVariantEnum()
        variant.setValue(EcucConfigurationVariantEnum.VARIANT_POST_BUILD)
        module_def.addSupportedConfigVariant(variant)
        module_def.createEcucParamConfContainerDef("C1")

        child_element = self._write(module_def)

        tags = [c.tag for c in child_element]
        assert tags == ["SHORT-NAME", "API-SERVICE-PREFIX", "POST-BUILD-VARIANT-SUPPORT", "REFINED-MODULE-DEF-REF", "SUPPORTED-CONFIG-VARIANTS", "CONTAINERS"]
        assert child_element.find("API-SERVICE-PREFIX").text == "Com"
        assert child_element.find("POST-BUILD-VARIANT-SUPPORT").text == "true"
        refined = child_element.find("REFINED-MODULE-DEF-REF")
        assert refined.text == "/EcucModuleDefs/Standard"
        assert refined.attrib["DEST"] == "ECUC-MODULE-DEF"
        assert child_element.find("SUPPORTED-CONFIG-VARIANTS/SUPPORTED-CONFIG-VARIANT").text == "VARIANT-POST-BUILD"
        assert child_element.find("CONTAINERS/ECUC-PARAM-CONF-CONTAINER-DEF/SHORT-NAME").text == "C1"
