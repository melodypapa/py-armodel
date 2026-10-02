"""Parser tests for DiagnosticSecurityEventReportingModeMapping (Table 5.18, p.243).

XSD group DIAGNOSTIC-SECURITY-EVENT-REPORTING-MODE-MAPPING element order (AUTOSAR_00052.xsd): DATA-ELEMENT-REF, SECURITY-EVENT-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticSecurityEventReportingModeMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-SECURITY-EVENT-REPORTING-MODE-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticSecurityEventReportingModeMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticSecurityEventReportingModeMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<DATA-ELEMENT-REF DEST='DEST'>/AUTOSAR/DataElement1</DATA-ELEMENT-REF><SECURITY-EVENT-REF DEST='DEST'>/AUTOSAR/SecurityEvent1</SECURITY-EVENT-REF>"
        )
        parser.readDiagnosticSecurityEventReportingModeMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getDataElementRef() is not None
        assert mapping.getDataElementRef().getValue() == "/AUTOSAR/DataElement1"
        assert mapping.getSecurityEventRef() is not None
        assert mapping.getSecurityEventRef().getValue() == "/AUTOSAR/SecurityEvent1"

    def test_read_empty(self, parser):
        mapping = DiagnosticSecurityEventReportingModeMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticSecurityEventReportingModeMapping(element, mapping)
        assert mapping.getDataElementRef() is None
        assert mapping.getSecurityEventRef() is None
