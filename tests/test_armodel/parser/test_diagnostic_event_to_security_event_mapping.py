"""Parser tests for DiagnosticEventToSecurityEventMapping (Table 5.30, p.257).

XSD group DIAGNOSTIC-EVENT-TO-SECURITY-EVENT-MAPPING element order (AUTOSAR_00052.xsd): DIAGNOSTIC-EVENT-REF, SECURITY-EVENT-PROPS-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventToSecurityEventMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-EVENT-TO-SECURITY-EVENT-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticEventToSecurityEventMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticEventToSecurityEventMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<DIAGNOSTIC-EVENT-REF DEST='DEST'>/AUTOSAR/DiagnosticEvent1</DIAGNOSTIC-EVENT-REF><SECURITY-EVENT-PROPS-REF DEST='DEST'>/AUTOSAR/SecurityEventProps1</SECURITY-EVENT-PROPS-REF>"
        )
        parser.readDiagnosticEventToSecurityEventMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getDiagnosticEventRef() is not None
        assert mapping.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"
        assert mapping.getSecurityEventPropsRef() is not None
        assert mapping.getSecurityEventPropsRef().getValue() == "/AUTOSAR/SecurityEventProps1"

    def test_read_empty(self, parser):
        mapping = DiagnosticEventToSecurityEventMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticEventToSecurityEventMapping(element, mapping)
        assert mapping.getDiagnosticEventRef() is None
        assert mapping.getSecurityEventPropsRef() is None
