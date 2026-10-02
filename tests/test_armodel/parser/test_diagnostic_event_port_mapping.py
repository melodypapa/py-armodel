"""Parser tests for DiagnosticEventPortMapping (Table 5.24, p.249).

XSD group DIAGNOSTIC-EVENT-PORT-MAPPING (AUTOSAR_00052.xsd l.36577) element order (markdown-modeled
subset): BSW-SERVICE-DEPENDENCY-REF, DIAGNOSTIC-EVENT-REF, SWC-FLAT-SERVICE-DEPENDENCY-REF, SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventPortMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-EVENT-PORT-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticEventPortMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticEventPortMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<BSW-SERVICE-DEPENDENCY-REF DEST='DEST'>/AUTOSAR/BswServiceDependency1</BSW-SERVICE-DEPENDENCY-REF><DIAGNOSTIC-EVENT-REF DEST='DEST'>/AUTOSAR/DiagnosticEvent1</DIAGNOSTIC-EVENT-REF><SWC-FLAT-SERVICE-DEPENDENCY-REF DEST='DEST'>/AUTOSAR/SwcFlatServiceDependency1</SWC-FLAT-SERVICE-DEPENDENCY-REF><SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF DEST='DEST'>/AUTOSAR/SwcServiceDependencyInSystem1</SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF>"
        )
        parser.readDiagnosticEventPortMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getBswServiceDependencyRef() is not None
        assert mapping.getBswServiceDependencyRef().getValue() == "/AUTOSAR/BswServiceDependency1"
        assert mapping.getDiagnosticEventRef() is not None
        assert mapping.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"
        assert mapping.getSwcFlatServiceDependencyRef() is not None
        assert mapping.getSwcFlatServiceDependencyRef().getValue() == "/AUTOSAR/SwcFlatServiceDependency1"
        assert mapping.getSwcServiceDependencyInSystemIRef() is not None
        assert mapping.getSwcServiceDependencyInSystemIRef().getValue() == "/AUTOSAR/SwcServiceDependencyInSystem1"

    def test_read_empty(self, parser):
        mapping = DiagnosticEventPortMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticEventPortMapping(element, mapping)
        assert mapping.getBswServiceDependencyRef() is None
        assert mapping.getDiagnosticEventRef() is None
        assert mapping.getSwcFlatServiceDependencyRef() is None
        assert mapping.getSwcServiceDependencyInSystemIRef() is None
