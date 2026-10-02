"""
Tests for writing the DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS element —
DiagnosticRequestDownloadClass, Table 4.122 (p.145, R23-11).

DiagnosticRequestDownloadClass (Base most-derived DiagnosticServiceClass) defines
no own attributes; the writer emits the IDENTIFIABLE wrapper only, and the
dispatch entry is writeARPackageElementRest → writeDiagnosticRequestDownloadClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_download_class.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestDownloadClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticRequestDownloadClass:
    """Tests for writeDiagnosticRequestDownloadClass — own element field values (Table 4.122)."""

    def test_write_emits_identifiable_wrapper(self):
        """Test that writing emits the DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS wrapper with the SHORT-NAME."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestDownloadClasses")
        package.createDiagnosticRequestDownloadClass("Rqd1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestDownloadClass(parent, package.getReferrableElement("Rqd1", DiagnosticRequestDownloadClass))

        child = parent.find("DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Rqd1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_round_trip_preserves_element(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestDownloadClasses")
        package.createDiagnosticRequestDownloadClass("Rqd1")

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeARPackageElementRest(parent, package.getReferrableElement("Rqd1", DiagnosticRequestDownloadClass))
        xml_text = ET.tostring(parent, encoding="unicode")

        parser = ARXMLParser()
        reloaded_package = AUTOSAR.getInstance().createARPackage("Reloaded")
        element = ET.fromstring(xml_text)
        parser.readARPackageElementsRest("DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS", element.find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS"), reloaded_package)
        reloaded = reloaded_package.getReferrableElement("Rqd1", DiagnosticRequestDownloadClass)
        assert reloaded is not None
        assert reloaded.getShortName() == "Rqd1"
