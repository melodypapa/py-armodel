"""Parser tests for EcucModuleDef (Table 2.2, p.32).

XSD group ECUC-MODULE-DEF (AUTOSAR_00052.xsd) element order:
API-SERVICE-PREFIX, POST-BUILD-VARIANT-SUPPORT, REFINED-MODULE-DEF-REF,
SUPPORTED-CONFIG-VARIANTS, CONTAINERS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucModuleDef

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "ECUC-MODULE-DEF") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadEcucModuleDef:
    def test_read_sets_all_fields(self, parser):
        module_def = EcucModuleDef(AUTOSAR.getInstance(), "Module")
        element = _snip(
            "<SHORT-NAME>Module</SHORT-NAME>"
            "<API-SERVICE-PREFIX>Cdd</API-SERVICE-PREFIX>"
            "<POST-BUILD-VARIANT-SUPPORT>true</POST-BUILD-VARIANT-SUPPORT>"
            '<REFINED-MODULE-DEF-REF DEST="ECUC-MODULE-DEF">/AUTOSAR/EcucModuleDefs/Standard</REFINED-MODULE-DEF-REF>'
            "<SUPPORTED-CONFIG-VARIANTS>"
            "<SUPPORTED-CONFIG-VARIANT>VARIANT-POST-BUILD</SUPPORTED-CONFIG-VARIANT>"
            "<SUPPORTED-CONFIG-VARIANT>VARIANT-LINK-TIME</SUPPORTED-CONFIG-VARIANT>"
            "</SUPPORTED-CONFIG-VARIANTS>"
        )
        parser.readEcucModuleDef(element, module_def)
        assert module_def.getShortName() == "Module"
        assert module_def.getApiServicePrefix().getValue() == "Cdd"
        assert module_def.getPostBuildVariantSupport().getValue() is True
        assert module_def.getRefinedModuleDefRef().getValue() == "/AUTOSAR/EcucModuleDefs/Standard"
        assert module_def.getRefinedModuleDefRef().getDest() == "ECUC-MODULE-DEF"
        variants = module_def.getSupportedConfigVariants()
        assert len(variants) == 2
        assert variants[0].getValue() == "VARIANT-POST-BUILD"
        assert variants[1].getValue() == "VARIANT-LINK-TIME"

    def test_read_empty(self, parser):
        module_def = EcucModuleDef(AUTOSAR.getInstance(), "Module")
        element = _snip("")
        parser.readEcucModuleDef(element, module_def)
        assert module_def.getApiServicePrefix() is None
        assert module_def.getPostBuildVariantSupport() is None
        assert module_def.getRefinedModuleDefRef() is None
        assert module_def.getSupportedConfigVariants() == []
        assert module_def.getContainers() == []
