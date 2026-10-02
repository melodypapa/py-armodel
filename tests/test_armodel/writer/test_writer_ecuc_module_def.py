"""
Tests for writing ECUC-MODULE-DEF elements —
EcucModuleDef, Table 2.2 (p.32, R23-11).

EcucModuleDef (Base most-derived EcucDefinitionElement) owns apiServicePrefix,
postBuildVariantSupport, refinedModuleDefRef, supportedConfigVariants and the
atpSplitable containers aggregation; AUTOSAR_00052.xsd group ECUC-MODULE-DEF
element order: API-SERVICE-PREFIX, POST-BUILD-VARIANT-SUPPORT,
REFINED-MODULE-DEF-REF, SUPPORTED-CONFIG-VARIANTS, CONTAINERS.

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

    def test_write_empty_wrapper(self):
        """Test that an EcucModuleDef without attributes emits no own-field elements."""
        module_def = EcucModuleDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Module1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucModuleDef(parent, module_def)

        child = parent.find("ECUC-MODULE-DEF")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Module1"
        assert child.find("API-SERVICE-PREFIX") is None
        assert child.find("POST-BUILD-VARIANT-SUPPORT") is None
        assert child.find("REFINED-MODULE-DEF-REF") is None
        assert child.find("SUPPORTED-CONFIG-VARIANTS") is None
        assert len(child.find("CONTAINERS")) == 0  # wrapper may be present, but empty

    def test_write_fields_in_xsd_order(self):
        """Test that all own attributes are emitted in XSD order with the spec values."""
        module_def = EcucModuleDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Module1")
        module_def.setApiServicePrefix(CIdentifier().setValue("Cdd"))
        module_def.setPostBuildVariantSupport(Boolean().setValue(True))
        ref = RefType()
        ref.setDest("ECUC-MODULE-DEF")
        ref.setValue("/AUTOSAR/EcucModuleDefs/Standard")
        module_def.setRefinedModuleDefRef(ref)
        module_def.addSupportedConfigVariant(EcucConfigurationVariantEnum().setValue(EcucConfigurationVariantEnum.VARIANT_POST_BUILD))
        module_def.createEcucParamConfContainerDef("TopContainer")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucModuleDef(parent, module_def)

        child = parent.find("ECUC-MODULE-DEF")
        tags = [c.tag for c in child]
        assert tags == ["SHORT-NAME", "API-SERVICE-PREFIX", "POST-BUILD-VARIANT-SUPPORT", "REFINED-MODULE-DEF-REF", "SUPPORTED-CONFIG-VARIANTS", "CONTAINERS"]
        assert child.find("API-SERVICE-PREFIX").text == "Cdd"
        assert child.find("POST-BUILD-VARIANT-SUPPORT").text == "true"
        assert child.find("REFINED-MODULE-DEF-REF").text == "/AUTOSAR/EcucModuleDefs/Standard"
        assert child.find("REFINED-MODULE-DEF-REF").attrib["DEST"] == "ECUC-MODULE-DEF"
        variants = child.find("SUPPORTED-CONFIG-VARIANTS").findall("SUPPORTED-CONFIG-VARIANT")
        assert len(variants) == 1
        assert variants[0].text == "VARIANT-POST-BUILD"
        containers = child.find("CONTAINERS")
        assert len(containers.findall("ECUC-PARAM-CONF-CONTAINER-DEF")) == 1
