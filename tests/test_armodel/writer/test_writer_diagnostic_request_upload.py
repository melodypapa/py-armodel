"""
Tests for writing DIAGNOSTIC-REQUEST-UPLOAD elements —
DiagnosticRequestUpload, Table 4.123 (p.145, R23-11).

DiagnosticRequestUpload (Base most-derived DiagnosticMemoryAddressableRangeAccess) owns one 0..1
reference requestUploadClass (REQUEST-UPLOAD-CLASS-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-REQUEST-UPLOAD l.42454: REQUEST-UPLOAD-CLASS-REF.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_upload.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestUpload
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


def _make_full_request_upload() -> DiagnosticRequestUpload:
    package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestUploadServices")
    request_upload = package.createDiagnosticRequestUpload("RequestUpload1")
    request_upload.setRequestUploadClassRef(RefType().setDest("DIAGNOSTIC-REQUEST-UPLOAD-CLASS").setValue("/AUTOSAR/DiagnosticRequestUploadClasses/Class1"))
    return request_upload


class TestWriteDiagnosticRequestUpload:
    """Tests for writeDiagnosticRequestUpload — own element field values (Table 4.123)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticRequestUpload without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestUploadServices")
        package.createDiagnosticRequestUpload("RequestUpload1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestUpload(parent, package.getReferrableElement("RequestUpload1", DiagnosticRequestUpload))

        child = parent.find("DIAGNOSTIC-REQUEST-UPLOAD")
        assert child is not None
        assert child.find("SHORT-NAME").text == "RequestUpload1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        request_upload = _make_full_request_upload()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestUpload(parent, request_upload)

        child = parent.find("DIAGNOSTIC-REQUEST-UPLOAD")
        assert [c.tag for c in child] == ["SHORT-NAME", "REQUEST-UPLOAD-CLASS-REF"]
        assert child.find("REQUEST-UPLOAD-CLASS-REF").text == "/AUTOSAR/DiagnosticRequestUploadClasses/Class1"
        assert child.find("REQUEST-UPLOAD-CLASS-REF").get("DEST") == "DIAGNOSTIC-REQUEST-UPLOAD-CLASS"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        request_upload = _make_full_request_upload()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticRequestUpload(parent, request_upload)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticRequestUpload(AUTOSAR.getInstance(), "RequestUpload1")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-UPLOAD")
        ARXMLParser().readDiagnosticRequestUpload(element, reloaded)
        assert reloaded.getRequestUploadClassRef() is not None
        assert reloaded.getRequestUploadClassRef().getValue() == "/AUTOSAR/DiagnosticRequestUploadClasses/Class1"
        assert reloaded.getRequestUploadClassRef().getDest() == "DIAGNOSTIC-REQUEST-UPLOAD-CLASS"
