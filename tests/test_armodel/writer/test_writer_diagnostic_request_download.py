"""
Tests for writing DIAGNOSTIC-REQUEST-DOWNLOAD elements —
DiagnosticRequestDownload, Table 4.121 (p.144, R23-11).

DiagnosticRequestDownload (Base most-derived DiagnosticMemoryAddressableRangeAccess) owns one 0..1
reference requestDownloadClass (REQUEST-DOWNLOAD-CLASS-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-REQUEST-DOWNLOAD l.41794: REQUEST-DOWNLOAD-CLASS-REF.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_download.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestDownload
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


def _make_full_request_download() -> DiagnosticRequestDownload:
    package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestDownloadServices")
    request_download = package.createDiagnosticRequestDownload("RequestDownload1")
    request_download.setRequestDownloadClassRef(RefType().setDest("DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS").setValue("/AUTOSAR/DiagnosticRequestDownloadClasses/Class1"))
    return request_download


class TestWriteDiagnosticRequestDownload:
    """Tests for writeDiagnosticRequestDownload — own element field values (Table 4.121)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticRequestDownload without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestDownloadServices")
        package.createDiagnosticRequestDownload("RequestDownload1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestDownload(parent, package.getReferrableElement("RequestDownload1", DiagnosticRequestDownload))

        child = parent.find("DIAGNOSTIC-REQUEST-DOWNLOAD")
        assert child is not None
        assert child.find("SHORT-NAME").text == "RequestDownload1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        request_download = _make_full_request_download()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestDownload(parent, request_download)

        child = parent.find("DIAGNOSTIC-REQUEST-DOWNLOAD")
        assert [c.tag for c in child] == ["SHORT-NAME", "REQUEST-DOWNLOAD-CLASS-REF"]
        assert child.find("REQUEST-DOWNLOAD-CLASS-REF").text == "/AUTOSAR/DiagnosticRequestDownloadClasses/Class1"
        assert child.find("REQUEST-DOWNLOAD-CLASS-REF").get("DEST") == "DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        request_download = _make_full_request_download()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticRequestDownload(parent, request_download)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticRequestDownload(AUTOSAR.getInstance(), "RequestDownload1")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-DOWNLOAD")
        ARXMLParser().readDiagnosticRequestDownload(element, reloaded)
        assert reloaded.getRequestDownloadClassRef() is not None
        assert reloaded.getRequestDownloadClassRef().getValue() == "/AUTOSAR/DiagnosticRequestDownloadClasses/Class1"
        assert reloaded.getRequestDownloadClassRef().getDest() == "DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS"
