"""Parser tests for DiagnosticStorageConditionPortMapping (Table 5.27, p.253).

XSD group DIAGNOSTIC-STORAGE-CONDITION-PORT-MAPPING (AUTOSAR_00052.xsd l.45750) element order (markdown-modeled
subset): DIAGNOSTIC-STORAGE-CONDITION-REF, SWC-FLAT-SERVICE-DEPENDENCY-REF, SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticStorageConditionPortMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-STORAGE-CONDITION-PORT-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticStorageConditionPortMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticStorageConditionPortMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<DIAGNOSTIC-STORAGE-CONDITION-REF DEST='DEST'>/AUTOSAR/DiagnosticStorageCondition1</DIAGNOSTIC-STORAGE-CONDITION-REF><SWC-FLAT-SERVICE-DEPENDENCY-REF DEST='DEST'>/AUTOSAR/SwcFlatServiceDependency1</SWC-FLAT-SERVICE-DEPENDENCY-REF><SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF DEST='DEST'>/AUTOSAR/SwcServiceDependencyInSystem1</SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF>"
        )
        parser.readDiagnosticStorageConditionPortMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getDiagnosticStorageConditionRef() is not None
        assert mapping.getDiagnosticStorageConditionRef().getValue() == "/AUTOSAR/DiagnosticStorageCondition1"
        assert mapping.getSwcFlatServiceDependencyRef() is not None
        assert mapping.getSwcFlatServiceDependencyRef().getValue() == "/AUTOSAR/SwcFlatServiceDependency1"
        assert mapping.getSwcServiceDependencyInSystemIRef() is not None
        assert mapping.getSwcServiceDependencyInSystemIRef().getValue() == "/AUTOSAR/SwcServiceDependencyInSystem1"

    def test_read_empty(self, parser):
        mapping = DiagnosticStorageConditionPortMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticStorageConditionPortMapping(element, mapping)
        assert mapping.getDiagnosticStorageConditionRef() is None
        assert mapping.getSwcFlatServiceDependencyRef() is None
        assert mapping.getSwcServiceDependencyInSystemIRef() is None
