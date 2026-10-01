"""Parser tests for DiagnosticOperationCyclePortMapping (Table 5.25, p.250).

XSD group DIAGNOSTIC-OPERATION-CYCLE-PORT-MAPPING (AUTOSAR_00052.xsd l.40438) element order (markdown-modeled
subset): OPERATION-CYCLE-REF, SWC-FLAT-SERVICE-DEPENDENCY-REF, SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticOperationCyclePortMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-OPERATION-CYCLE-PORT-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticOperationCyclePortMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticOperationCyclePortMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<OPERATION-CYCLE-REF DEST='DEST'>/AUTOSAR/OperationCycle1</OPERATION-CYCLE-REF><SWC-FLAT-SERVICE-DEPENDENCY-REF DEST='DEST'>/AUTOSAR/SwcFlatServiceDependency1</SWC-FLAT-SERVICE-DEPENDENCY-REF><SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF DEST='DEST'>/AUTOSAR/SwcServiceDependencyInSystem1</SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF>"
        )
        parser.readDiagnosticOperationCyclePortMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getOperationCycleRef() is not None
        assert mapping.getOperationCycleRef().getValue() == "/AUTOSAR/OperationCycle1"
        assert mapping.getSwcFlatServiceDependencyRef() is not None
        assert mapping.getSwcFlatServiceDependencyRef().getValue() == "/AUTOSAR/SwcFlatServiceDependency1"
        assert mapping.getSwcServiceDependencyInSystemIRef() is not None
        assert mapping.getSwcServiceDependencyInSystemIRef().getValue() == "/AUTOSAR/SwcServiceDependencyInSystem1"

    def test_read_empty(self, parser):
        mapping = DiagnosticOperationCyclePortMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticOperationCyclePortMapping(element, mapping)
        assert mapping.getOperationCycleRef() is None
        assert mapping.getSwcFlatServiceDependencyRef() is None
        assert mapping.getSwcServiceDependencyInSystemIRef() is None
