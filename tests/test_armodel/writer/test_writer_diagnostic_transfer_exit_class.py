"""
Tests for writing the DIAGNOSTIC-TRANSFER-EXIT-CLASS element —
DiagnosticTransferExitClass, Table 4.118 (p.143, R23-11).

DiagnosticTransferExitClass (Base most-derived DiagnosticServiceClass) defines
no own attributes; the writer emits the IDENTIFIABLE wrapper only, and the
dispatch entry is writeARPackageElementRest → writeDiagnosticTransferExitClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_transfer_exit_class.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticTransferExitClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticTransferExitClass:
    """Tests for writeDiagnosticTransferExitClass — own element field values (Table 4.118)."""

    def test_write_emits_identifiable_wrapper(self):
        """Test that writing emits the DIAGNOSTIC-TRANSFER-EXIT-CLASS wrapper with the SHORT-NAME."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTransferExitClasses")
        package.createDiagnosticTransferExitClass("Tea1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticTransferExitClass(parent, package.getReferrableElement("Tea1", DiagnosticTransferExitClass))

        child = parent.find("DIAGNOSTIC-TRANSFER-EXIT-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Tea1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_round_trip_preserves_element(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTransferExitClasses")
        package.createDiagnosticTransferExitClass("Tea1")

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeARPackageElementRest(parent, package.getReferrableElement("Tea1", DiagnosticTransferExitClass))
        xml_text = ET.tostring(parent, encoding="unicode")

        parser = ARXMLParser()
        reloaded_package = AUTOSAR.getInstance().createARPackage("Reloaded")
        element = ET.fromstring(xml_text)
        parser.readARPackageElementsRest("DIAGNOSTIC-TRANSFER-EXIT-CLASS", element.find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-TRANSFER-EXIT-CLASS"), reloaded_package)
        reloaded = reloaded_package.getReferrableElement("Tea1", DiagnosticTransferExitClass)
        assert reloaded is not None
        assert reloaded.getShortName() == "Tea1"
