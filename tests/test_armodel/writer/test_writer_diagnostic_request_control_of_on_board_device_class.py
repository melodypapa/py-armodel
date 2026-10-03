"""
Tests for writing the DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS
element — DiagnosticRequestControlOfOnBoardDeviceClass, Table 4.142 (p.158,
R23-11).

DiagnosticRequestControlOfOnBoardDeviceClass (Base most-derived
DiagnosticServiceClass) defines no own attributes; the writer emits the
IDENTIFIABLE wrapper only, and the dispatch entry is writeARPackageElementRest →
writeDiagnosticRequestControlOfOnBoardDeviceClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_control_of_on_board_device_class.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestControlOfOnBoardDeviceClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticRequestControlOfOnBoardDeviceClass:
    """Tests for writeDiagnosticRequestControlOfOnBoardDeviceClass — own element field values (Table 4.142)."""

    def test_write_emits_identifiable_wrapper(self):
        """Test that writing emits the DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS wrapper with the SHORT-NAME."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode08Classes")
        package.createDiagnosticRequestControlOfOnBoardDeviceClass("Coob1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestControlOfOnBoardDeviceClass(parent, package.getReferrableElement("Coob1", DiagnosticRequestControlOfOnBoardDeviceClass))

        child = parent.find("DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Coob1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_round_trip_preserves_element(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the element."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode08Classes")
        package.createDiagnosticRequestControlOfOnBoardDeviceClass("Coob1")

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeARPackageElementRest(parent, package.getReferrableElement("Coob1", DiagnosticRequestControlOfOnBoardDeviceClass))
        xml_text = ET.tostring(parent, encoding="unicode")

        parser = ARXMLParser()
        reloaded_package = AUTOSAR.getInstance().createARPackage("Reloaded")
        element = ET.fromstring(xml_text)
        parser.readARPackageElementsRest(
            "DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS", element.find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS"), reloaded_package
        )
        reloaded = reloaded_package.getReferrableElement("Coob1", DiagnosticRequestControlOfOnBoardDeviceClass)
        assert reloaded is not None
        assert reloaded.getShortName() == "Coob1"
