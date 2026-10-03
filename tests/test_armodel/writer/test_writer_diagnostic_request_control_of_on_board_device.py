"""
Tests for writing DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE elements —
DiagnosticRequestControlOfOnBoardDevice, Table 4.141 (p.157, R23-11).

DiagnosticRequestControlOfOnBoardDevice (Base most-derived
DiagnosticServiceInstance) owns two 0..1 references —
requestControlOfOnBoardDeviceClass (REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS-REF)
and testId (TEST-ID-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE l.41602.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_control_of_on_board_device.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestControlOfOnBoardDevice
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


def _make_full_mode08() -> DiagnosticRequestControlOfOnBoardDevice:
    package = AUTOSAR.getInstance().createARPackage("OBDMode08Services")
    mode08 = package.createDiagnosticRequestControlOfOnBoardDevice("Mode08")
    mode08.setRequestControlOfOnBoardDeviceClassRef(RefType().setDest("DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS").setValue("/AUTOSAR/DiagnosticRequestControlOfOnBoardDeviceClasses/Class1"))
    mode08.setTestIdRef(RefType().setDest("DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER").setValue("/AUTOSAR/DiagnosticTestRoutineIdentifiers/Tid1"))
    return mode08


class TestWriteDiagnosticRequestControlOfOnBoardDevice:
    """Tests for writeDiagnosticRequestControlOfOnBoardDevice — own element field values (Table 4.141)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticRequestControlOfOnBoardDevice without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode08Services")
        package.createDiagnosticRequestControlOfOnBoardDevice("Mode08")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestControlOfOnBoardDevice(parent, package.getReferrableElement("Mode08", DiagnosticRequestControlOfOnBoardDevice))

        child = parent.find("DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Mode08"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        mode08 = _make_full_mode08()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestControlOfOnBoardDevice(parent, mode08)

        child = parent.find("DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE")
        assert [c.tag for c in child] == ["SHORT-NAME", "REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS-REF", "TEST-ID-REF"]
        assert child.find("REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS-REF").text == "/AUTOSAR/DiagnosticRequestControlOfOnBoardDeviceClasses/Class1"
        assert child.find("REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS-REF").get("DEST") == "DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS"
        assert child.find("TEST-ID-REF").text == "/AUTOSAR/DiagnosticTestRoutineIdentifiers/Tid1"
        assert child.find("TEST-ID-REF").get("DEST") == "DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        mode08 = _make_full_mode08()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticRequestControlOfOnBoardDevice(parent, mode08)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticRequestControlOfOnBoardDevice(AUTOSAR.getInstance(), "Mode08")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE")
        ARXMLParser().readDiagnosticRequestControlOfOnBoardDevice(element, reloaded)
        assert reloaded.getRequestControlOfOnBoardDeviceClassRef() is not None
        assert reloaded.getRequestControlOfOnBoardDeviceClassRef().getValue() == "/AUTOSAR/DiagnosticRequestControlOfOnBoardDeviceClasses/Class1"
        assert reloaded.getRequestControlOfOnBoardDeviceClassRef().getDest() == "DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS"
        assert reloaded.getTestIdRef() is not None
        assert reloaded.getTestIdRef().getValue() == "/AUTOSAR/DiagnosticTestRoutineIdentifiers/Tid1"
        assert reloaded.getTestIdRef().getDest() == "DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER"
