"""Parser tests for DiagnosticFimAliasEventGroupMapping (Table 5.36, p.263).

XSD group DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP-MAPPING element order (AUTOSAR_00052.xsd): ACTUAL-EVENT-REF, ALIAS-EVENT-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticFimAliasEventGroupMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticFimAliasEventGroupMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticFimAliasEventGroupMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<ACTUAL-EVENT-REF DEST='DEST'>/AUTOSAR/ActualEvent1</ACTUAL-EVENT-REF><ALIAS-EVENT-REF DEST='DEST'>/AUTOSAR/AliasEvent1</ALIAS-EVENT-REF>"
        )
        parser.readDiagnosticFimAliasEventGroupMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getActualEventRef() is not None
        assert mapping.getActualEventRef().getValue() == "/AUTOSAR/ActualEvent1"
        assert mapping.getAliasEventRef() is not None
        assert mapping.getAliasEventRef().getValue() == "/AUTOSAR/AliasEvent1"

    def test_read_empty(self, parser):
        mapping = DiagnosticFimAliasEventGroupMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticFimAliasEventGroupMapping(element, mapping)
        assert mapping.getActualEventRef() is None
        assert mapping.getAliasEventRef() is None
