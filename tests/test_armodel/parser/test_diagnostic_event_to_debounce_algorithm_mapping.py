"""Parser tests for DiagnosticEventToDebounceAlgorithmMapping (Table 5.21, p.246).

XSD group DIAGNOSTIC-EVENT-TO-DEBOUNCE-ALGORITHM-MAPPING (AUTOSAR_00052.xsd l.36725) element order:
DEBOUNCE-ALGORITHM-REF, DIAGNOSTIC-EVENT-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventToDebounceAlgorithmMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-EVENT-TO-DEBOUNCE-ALGORITHM-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticEventToDebounceAlgorithmMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticEventToDebounceAlgorithmMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<DEBOUNCE-ALGORITHM-REF DEST='DEST'>/AUTOSAR/DebounceAlgorithm1</DEBOUNCE-ALGORITHM-REF><DIAGNOSTIC-EVENT-REF DEST='DEST'>/AUTOSAR/DiagnosticEvent1</DIAGNOSTIC-EVENT-REF>"
        )
        parser.readDiagnosticEventToDebounceAlgorithmMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getDebounceAlgorithmRef() is not None
        assert mapping.getDebounceAlgorithmRef().getValue() == "/AUTOSAR/DebounceAlgorithm1"
        assert mapping.getDiagnosticEventRef() is not None
        assert mapping.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"

    def test_read_empty(self, parser):
        mapping = DiagnosticEventToDebounceAlgorithmMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticEventToDebounceAlgorithmMapping(element, mapping)
        assert mapping.getDebounceAlgorithmRef() is None
        assert mapping.getDiagnosticEventRef() is None
