"""Parser tests for DiagnosticEnableConditionPortMapping (Table 5.26, p.252).

XSD group DIAGNOSTIC-ENABLE-CONDITION-PORT-MAPPING (AUTOSAR_00052.xsd l.35627) element order (markdown-modeled
subset): ENABLE-CONDITION-REF, SWC-FLAT-SERVICE-DEPENDENCY-REF, SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEnableConditionPortMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-ENABLE-CONDITION-PORT-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticEnableConditionPortMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticEnableConditionPortMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<ENABLE-CONDITION-REF DEST='DEST'>/AUTOSAR/EnableCondition1</ENABLE-CONDITION-REF><SWC-FLAT-SERVICE-DEPENDENCY-REF DEST='DEST'>/AUTOSAR/SwcFlatServiceDependency1</SWC-FLAT-SERVICE-DEPENDENCY-REF><SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF DEST='DEST'>/AUTOSAR/SwcServiceDependencyInSystem1</SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF>"
        )
        parser.readDiagnosticEnableConditionPortMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getEnableConditionRef() is not None
        assert mapping.getEnableConditionRef().getValue() == "/AUTOSAR/EnableCondition1"
        assert mapping.getSwcFlatServiceDependencyRef() is not None
        assert mapping.getSwcFlatServiceDependencyRef().getValue() == "/AUTOSAR/SwcFlatServiceDependency1"
        assert mapping.getSwcServiceDependencyInSystemIRef() is not None
        assert mapping.getSwcServiceDependencyInSystemIRef().getValue() == "/AUTOSAR/SwcServiceDependencyInSystem1"

    def test_read_empty(self, parser):
        mapping = DiagnosticEnableConditionPortMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticEnableConditionPortMapping(element, mapping)
        assert mapping.getEnableConditionRef() is None
        assert mapping.getSwcFlatServiceDependencyRef() is None
        assert mapping.getSwcServiceDependencyInSystemIRef() is None
