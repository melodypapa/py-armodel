"""Parser tests for DiagnosticFimAliasEventGroup (Table 5.35, p.263).

XSD group DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP element order (AUTOSAR_00052.xsd): GROUPED-ALIAS-EVENT-REFS.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticFimAliasEventGroup

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticFimAliasEventGroup:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticFimAliasEventGroup(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<GROUPED-ALIAS-EVENT-REFS><GROUPED-ALIAS-EVENT-REF DEST='DEST'>/AUTOSAR/GroupedAliasEvent1</GROUPED-ALIAS-EVENT-REF></GROUPED-ALIAS-EVENT-REFS>"
        )
        parser.readDiagnosticFimAliasEventGroup(element, mapping)
        assert mapping.getShortName() == "M1"
        assert len(mapping.getGroupedAliasEventRefs()) == 1
        assert mapping.getGroupedAliasEventRefs()[0].getValue() == "/AUTOSAR/GroupedAliasEvent1"

    def test_read_empty(self, parser):
        mapping = DiagnosticFimAliasEventGroup(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticFimAliasEventGroup(element, mapping)
        assert mapping.getGroupedAliasEventRefs() == []
