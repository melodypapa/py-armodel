"""Parser tests for DiagnosticInhibitSourceEventMapping (Table 5.33, p.261).

XSD group DIAGNOSTIC-INHIBIT-SOURCE-EVENT-MAPPING element order (AUTOSAR_00052.xsd): DIAGNOSTIC-EVENT-REF, EVENT-GROUP-REF, INHIBITION-SOURCE-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticInhibitSourceEventMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-INHIBIT-SOURCE-EVENT-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticInhibitSourceEventMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticInhibitSourceEventMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<DIAGNOSTIC-EVENT-REF DEST='DEST'>/AUTOSAR/DiagnosticEvent1</DIAGNOSTIC-EVENT-REF><EVENT-GROUP-REF DEST='DEST'>/AUTOSAR/EventGroup1</EVENT-GROUP-REF><INHIBITION-SOURCE-REF DEST='DEST'>/AUTOSAR/InhibitionSource1</INHIBITION-SOURCE-REF>"
        )
        parser.readDiagnosticInhibitSourceEventMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getDiagnosticEventRef() is not None
        assert mapping.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"
        assert mapping.getEventGroupRef() is not None
        assert mapping.getEventGroupRef().getValue() == "/AUTOSAR/EventGroup1"
        assert mapping.getInhibitionSourceRef() is not None
        assert mapping.getInhibitionSourceRef().getValue() == "/AUTOSAR/InhibitionSource1"

    def test_read_empty(self, parser):
        mapping = DiagnosticInhibitSourceEventMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticInhibitSourceEventMapping(element, mapping)
        assert mapping.getDiagnosticEventRef() is None
        assert mapping.getEventGroupRef() is None
        assert mapping.getInhibitionSourceRef() is None
