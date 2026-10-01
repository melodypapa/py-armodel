"""Parser tests for DiagnosticEventToStorageConditionGroupMapping (Table 5.23, p.248).

XSD group DIAGNOSTIC-EVENT-TO-STORAGE-CONDITION-GROUP-MAPPING (AUTOSAR_00052.xsd l.36957) element order:
DIAGNOSTIC-EVENT-REF, STORAGE-CONDITION-GROUP-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventToStorageConditionGroupMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-EVENT-TO-STORAGE-CONDITION-GROUP-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticEventToStorageConditionGroupMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticEventToStorageConditionGroupMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<DIAGNOSTIC-EVENT-REF DEST='DEST'>/AUTOSAR/DiagnosticEvent1</DIAGNOSTIC-EVENT-REF><STORAGE-CONDITION-GROUP-REF DEST='DEST'>/AUTOSAR/StorageConditionGroup1</STORAGE-CONDITION-GROUP-REF>"
        )
        parser.readDiagnosticEventToStorageConditionGroupMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getDiagnosticEventRef() is not None
        assert mapping.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"
        assert mapping.getStorageConditionGroupRef() is not None
        assert mapping.getStorageConditionGroupRef().getValue() == "/AUTOSAR/StorageConditionGroup1"

    def test_read_empty(self, parser):
        mapping = DiagnosticEventToStorageConditionGroupMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticEventToStorageConditionGroupMapping(element, mapping)
        assert mapping.getDiagnosticEventRef() is None
        assert mapping.getStorageConditionGroupRef() is None

