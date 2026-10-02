"""Parser tests for DiagnosticEventToEnableConditionGroupMapping (Table 5.22, p.247).

XSD group DIAGNOSTIC-EVENT-TO-ENABLE-CONDITION-GROUP-MAPPING (AUTOSAR_00052.xsd l.36783) element order:
DIAGNOSTIC-EVENT-REF, ENABLE-CONDITION-GROUP-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventToEnableConditionGroupMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-EVENT-TO-ENABLE-CONDITION-GROUP-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticEventToEnableConditionGroupMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticEventToEnableConditionGroupMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<DIAGNOSTIC-EVENT-REF DEST='DEST'>/AUTOSAR/DiagnosticEvent1</DIAGNOSTIC-EVENT-REF><ENABLE-CONDITION-GROUP-REF DEST='DEST'>/AUTOSAR/EnableConditionGroup1</ENABLE-CONDITION-GROUP-REF>"
        )
        parser.readDiagnosticEventToEnableConditionGroupMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getDiagnosticEventRef() is not None
        assert mapping.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"
        assert mapping.getEnableConditionGroupRef() is not None
        assert mapping.getEnableConditionGroupRef().getValue() == "/AUTOSAR/EnableConditionGroup1"

    def test_read_empty(self, parser):
        mapping = DiagnosticEventToEnableConditionGroupMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticEventToEnableConditionGroupMapping(element, mapping)
        assert mapping.getDiagnosticEventRef() is None
        assert mapping.getEnableConditionGroupRef() is None
