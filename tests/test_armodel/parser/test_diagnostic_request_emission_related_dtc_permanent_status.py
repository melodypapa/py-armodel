"""Parser tests for DiagnosticRequestEmissionRelatedDTCPermanentStatus (Table 4.147, p.161).

XSD group DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS (AUTOSAR_00052.xsd l.41962)
element order after the IDENTIFIABLE content: ACCESS-PERMISSION-REF, SERVICE-CLASS-REF
(DiagnosticServiceInstance base group), REQUEST-EMISSION-RELATED-DTC-CLASS-PERMANENT-STATUS-REF.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_emission_related_dtc_permanent_status.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestEmissionRelatedDTCPermanentStatus

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticRequestEmissionRelatedDTCPermanentStatus:
    def test_read_sets_all_fields(self, parser):
        mode0a = DiagnosticRequestEmissionRelatedDTCPermanentStatus(AUTOSAR.getInstance(), "Mode0A")
        element = _snip(
            "<SHORT-NAME>Mode0A</SHORT-NAME>"
            "<ACCESS-PERMISSION-REF DEST='DIAGNOSTIC-ACCESS-PERMISSION'>/AUTOSAR/DiagnosticAccessPermissions/Perm1</ACCESS-PERMISSION-REF>"
            "<REQUEST-EMISSION-RELATED-DTC-CLASS-PERMANENT-STATUS-REF DEST='DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS-CLASS'>/AUTOSAR/DiagnosticRequestEmissionRelatedDTCPermanentStatusClasss/Class1</REQUEST-EMISSION-RELATED-DTC-CLASS-PERMANENT-STATUS-REF>"
        )
        parser.readDiagnosticRequestEmissionRelatedDTCPermanentStatus(element, mode0a)
        assert mode0a.getShortName() == "Mode0A"
        assert mode0a.getAccessPermissionRef() is not None
        assert mode0a.getAccessPermissionRef().getValue() == "/AUTOSAR/DiagnosticAccessPermissions/Perm1"
        assert mode0a.getAccessPermissionRef().getDest() == "DIAGNOSTIC-ACCESS-PERMISSION"
        assert mode0a.getRequestEmissionRelatedDtcClassPermanentStatusRef() is not None
        assert mode0a.getRequestEmissionRelatedDtcClassPermanentStatusRef().getValue() == "/AUTOSAR/DiagnosticRequestEmissionRelatedDTCPermanentStatusClasss/Class1"
        assert mode0a.getRequestEmissionRelatedDtcClassPermanentStatusRef().getDest() == "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS-CLASS"

    def test_read_empty(self, parser):
        mode0a = DiagnosticRequestEmissionRelatedDTCPermanentStatus(AUTOSAR.getInstance(), "Mode0A")
        element = _snip("<SHORT-NAME>Mode0A</SHORT-NAME>")
        parser.readDiagnosticRequestEmissionRelatedDTCPermanentStatus(element, mode0a)
        assert mode0a.getAccessPermissionRef() is None
        assert mode0a.getRequestEmissionRelatedDtcClassPermanentStatusRef() is None
