"""
Tests for writing the DIAGNOSTIC-DATA-TRANSFER-CLASS element —
DiagnosticDataTransferClass, Table 4.120 (p.143, R23-11).

DiagnosticDataTransferClass (Base most-derived DiagnosticServiceClass) defines
no own attributes; the writer emits the IDENTIFIABLE wrapper only, and the
dispatch entry is writeARPackageElementRest → writeDiagnosticDataTransferClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_data_transfer_class.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticDataTransferClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticDataTransferClass:
    """Tests for writeDiagnosticDataTransferClass — own element field values (Table 4.118)."""

    def test_write_emits_identifiable_wrapper(self):
        """Test that writing emits the DIAGNOSTIC-DATA-TRANSFER-CLASS wrapper with the SHORT-NAME."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDataTransferClasses")
        package.createDiagnosticDataTransferClass("Tea1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDataTransferClass(parent, package.getReferrableElement("Tea1", DiagnosticDataTransferClass))

        child = parent.find("DIAGNOSTIC-DATA-TRANSFER-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Tea1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_round_trip_preserves_element(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDataTransferClasses")
        package.createDiagnosticDataTransferClass("Tea1")

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeARPackageElementRest(parent, package.getReferrableElement("Tea1", DiagnosticDataTransferClass))
        xml_text = ET.tostring(parent, encoding="unicode")

        parser = ARXMLParser()
        reloaded_package = AUTOSAR.getInstance().createARPackage("Reloaded")
        element = ET.fromstring(xml_text)
        parser.readARPackageElementsRest("DIAGNOSTIC-DATA-TRANSFER-CLASS", element.find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-DATA-TRANSFER-CLASS"), reloaded_package)
        reloaded = reloaded_package.getReferrableElement("Tea1", DiagnosticDataTransferClass)
        assert reloaded is not None
        assert reloaded.getShortName() == "Tea1"
