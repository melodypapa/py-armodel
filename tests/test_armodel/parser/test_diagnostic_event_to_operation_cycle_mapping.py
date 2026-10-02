"""Parser tests for DiagnosticEventToOperationCycleMapping (Table 5.20, p.245).

XSD group DIAGNOSTIC-EVENT-TO-OPERATION-CYCLE-MAPPING (AUTOSAR_00052.xsd l.36841) element order:
DIAGNOSTIC-EVENT-REF, OPERATION-CYCLE-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventToOperationCycleMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-EVENT-TO-OPERATION-CYCLE-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticEventToOperationCycleMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticEventToOperationCycleMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<DIAGNOSTIC-EVENT-REF DEST='DEST'>/AUTOSAR/DiagnosticEvent1</DIAGNOSTIC-EVENT-REF><OPERATION-CYCLE-REF DEST='DEST'>/AUTOSAR/OperationCycle1</OPERATION-CYCLE-REF>"
        )
        parser.readDiagnosticEventToOperationCycleMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getDiagnosticEventRef() is not None
        assert mapping.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"
        assert mapping.getOperationCycleRef() is not None
        assert mapping.getOperationCycleRef().getValue() == "/AUTOSAR/OperationCycle1"

    def test_read_empty(self, parser):
        mapping = DiagnosticEventToOperationCycleMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticEventToOperationCycleMapping(element, mapping)
        assert mapping.getDiagnosticEventRef() is None
        assert mapping.getOperationCycleRef() is None
