"""
Tests for writing DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS elements —
DiagnosticRequestEmissionRelatedDTCPermanentStatus, Table 4.147 (p.161, R23-11).

DiagnosticRequestEmissionRelatedDTCPermanentStatus (Base most-derived DiagnosticServiceInstance)
owns the 0..1 class reference requestEmissionRelatedDtcClassPermanentStatus
(REQUEST-EMISSION-RELATED-DTC-CLASS-PERMANENT-STATUS-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS l.41962.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_emission_related_dtc_permanent_status.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestEmissionRelatedDTCPermanentStatus
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_full_mode0a() -> DiagnosticRequestEmissionRelatedDTCPermanentStatus:
    package = AUTOSAR.getInstance().createARPackage("OBDMode0AServices")
    mode0a = package.createDiagnosticRequestEmissionRelatedDTCPermanentStatus("Mode0A")
    mode0a.setAccessPermissionRef(RefType().setDest("DIAGNOSTIC-ACCESS-PERMISSION").setValue("/AUTOSAR/DiagnosticAccessPermissions/Perm1"))
    mode0a.setRequestEmissionRelatedDtcClassPermanentStatusRef(
        RefType().setDest("DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS-CLASS").setValue("/AUTOSAR/DiagnosticRequestEmissionRelatedDTCPermanentStatusClasss/Class1")
    )
    return mode0a


class TestWriteDiagnosticRequestEmissionRelatedDTCPermanentStatus:
    """Tests for writeDiagnosticRequestEmissionRelatedDTCPermanentStatus — own element field values (Table 4.147)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticRequestEmissionRelatedDTCPermanentStatus without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode0AServices")
        package.createDiagnosticRequestEmissionRelatedDTCPermanentStatus("Mode0A")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestEmissionRelatedDTCPermanentStatus(parent, package.getReferrableElement("Mode0A", DiagnosticRequestEmissionRelatedDTCPermanentStatus))

        child = parent.find("DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Mode0A"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        mode0a = _make_full_mode0a()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestEmissionRelatedDTCPermanentStatus(parent, mode0a)

        child = parent.find("DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS")
        assert [c.tag for c in child] == ["SHORT-NAME", "ACCESS-PERMISSION-REF", "REQUEST-EMISSION-RELATED-DTC-CLASS-PERMANENT-STATUS-REF"]
        assert child.find("ACCESS-PERMISSION-REF").text == "/AUTOSAR/DiagnosticAccessPermissions/Perm1"
        assert child.find("ACCESS-PERMISSION-REF").get("DEST") == "DIAGNOSTIC-ACCESS-PERMISSION"
        assert child.find("REQUEST-EMISSION-RELATED-DTC-CLASS-PERMANENT-STATUS-REF").text == "/AUTOSAR/DiagnosticRequestEmissionRelatedDTCPermanentStatusClasss/Class1"
        assert child.find("REQUEST-EMISSION-RELATED-DTC-CLASS-PERMANENT-STATUS-REF").get("DEST") == "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS-CLASS"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        mode0a = _make_full_mode0a()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticRequestEmissionRelatedDTCPermanentStatus(parent, mode0a)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticRequestEmissionRelatedDTCPermanentStatus(AUTOSAR.getInstance(), "Mode0A")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS")
        ARXMLParser().readDiagnosticRequestEmissionRelatedDTCPermanentStatus(element, reloaded)
        assert reloaded.getAccessPermissionRef() is not None
        assert reloaded.getAccessPermissionRef().getValue() == "/AUTOSAR/DiagnosticAccessPermissions/Perm1"
        assert reloaded.getAccessPermissionRef().getDest() == "DIAGNOSTIC-ACCESS-PERMISSION"
        assert reloaded.getRequestEmissionRelatedDtcClassPermanentStatusRef() is not None
        assert reloaded.getRequestEmissionRelatedDtcClassPermanentStatusRef().getValue() == "/AUTOSAR/DiagnosticRequestEmissionRelatedDTCPermanentStatusClasss/Class1"
        assert reloaded.getRequestEmissionRelatedDtcClassPermanentStatusRef().getDest() == "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS-CLASS"
