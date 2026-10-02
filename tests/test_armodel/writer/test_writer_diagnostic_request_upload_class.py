"""
Tests for writing the DIAGNOSTIC-REQUEST-UPLOAD-CLASS element —
DiagnosticRequestUploadClass, Table 4.124 (p.146, R23-11).

DiagnosticRequestUploadClass (Base most-derived DiagnosticServiceClass) defines
no own attributes; the writer emits the IDENTIFIABLE wrapper only, and the
dispatch entry is writeARPackageElementRest → writeDiagnosticRequestUploadClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_upload_class.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestUploadClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticRequestUploadClass:
    """Tests for writeDiagnosticRequestUploadClass — own element field values (Table 4.124)."""

    def test_write_emits_identifiable_wrapper(self):
        """Test that writing emits the DIAGNOSTIC-REQUEST-UPLOAD-CLASS wrapper with the SHORT-NAME."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestUploadClasses")
        package.createDiagnosticRequestUploadClass("Rqu1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestUploadClass(parent, package.getReferrableElement("Rqu1", DiagnosticRequestUploadClass))

        child = parent.find("DIAGNOSTIC-REQUEST-UPLOAD-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Rqu1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_round_trip_preserves_element(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestUploadClasses")
        package.createDiagnosticRequestUploadClass("Rqu1")

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeARPackageElementRest(parent, package.getReferrableElement("Rqu1", DiagnosticRequestUploadClass))
        xml_text = ET.tostring(parent, encoding="unicode")

        parser = ARXMLParser()
        reloaded_package = AUTOSAR.getInstance().createARPackage("Reloaded")
        element = ET.fromstring(xml_text)
        parser.readARPackageElementsRest("DIAGNOSTIC-REQUEST-UPLOAD-CLASS", element.find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-UPLOAD-CLASS"), reloaded_package)
        reloaded = reloaded_package.getReferrableElement("Rqu1", DiagnosticRequestUploadClass)
        assert reloaded is not None
        assert reloaded.getShortName() == "Rqu1"
