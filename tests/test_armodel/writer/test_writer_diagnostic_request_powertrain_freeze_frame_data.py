"""
Tests for writing DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA elements —
DiagnosticRequestPowertrainFreezeFrameData, Table 4.132 (p.152, R23-11).

DiagnosticRequestPowertrainFreezeFrameData (Base most-derived
DiagnosticServiceInstance) owns two 0..1 references — freezeFrame
(FREEZE-FRAME-REF) and requestPowertrainFreezeFrameData
(REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA l.42306.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_powertrain_freeze_frame_data.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestPowertrainFreezeFrameData
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


def _make_full_mode02() -> DiagnosticRequestPowertrainFreezeFrameData:
    package = AUTOSAR.getInstance().createARPackage("OBDMode02Services")
    mode02 = package.createDiagnosticRequestPowertrainFreezeFrameData("Mode02")
    mode02.setFreezeFrameRef(RefType().setDest("DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME").setValue("/AUTOSAR/DiagnosticPowertrainFreezeFrames/Frame1"))
    mode02.setRequestPowertrainFreezeFrameDataRef(
        RefType().setDest("DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS").setValue("/AUTOSAR/DiagnosticRequestPowertrainFreezeFrameDataClasses/Class1")
    )
    return mode02


class TestWriteDiagnosticRequestPowertrainFreezeFrameData:
    """Tests for writeDiagnosticRequestPowertrainFreezeFrameData — own element field values (Table 4.132)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticRequestPowertrainFreezeFrameData without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode02Services")
        package.createDiagnosticRequestPowertrainFreezeFrameData("Mode02")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestPowertrainFreezeFrameData(parent, package.getReferrableElement("Mode02", DiagnosticRequestPowertrainFreezeFrameData))

        child = parent.find("DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Mode02"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        mode02 = _make_full_mode02()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestPowertrainFreezeFrameData(parent, mode02)

        child = parent.find("DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA")
        assert [c.tag for c in child] == ["SHORT-NAME", "FREEZE-FRAME-REF", "REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-REF"]
        assert child.find("FREEZE-FRAME-REF").text == "/AUTOSAR/DiagnosticPowertrainFreezeFrames/Frame1"
        assert child.find("FREEZE-FRAME-REF").get("DEST") == "DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME"
        assert child.find("REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-REF").text == "/AUTOSAR/DiagnosticRequestPowertrainFreezeFrameDataClasses/Class1"
        assert child.find("REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-REF").get("DEST") == "DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        mode02 = _make_full_mode02()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticRequestPowertrainFreezeFrameData(parent, mode02)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticRequestPowertrainFreezeFrameData(AUTOSAR.getInstance(), "Mode02")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA")
        ARXMLParser().readDiagnosticRequestPowertrainFreezeFrameData(element, reloaded)
        assert reloaded.getFreezeFrameRef() is not None
        assert reloaded.getFreezeFrameRef().getValue() == "/AUTOSAR/DiagnosticPowertrainFreezeFrames/Frame1"
        assert reloaded.getFreezeFrameRef().getDest() == "DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME"
        assert reloaded.getRequestPowertrainFreezeFrameDataRef() is not None
        assert reloaded.getRequestPowertrainFreezeFrameDataRef().getValue() == "/AUTOSAR/DiagnosticRequestPowertrainFreezeFrameDataClasses/Class1"
        assert reloaded.getRequestPowertrainFreezeFrameDataRef().getDest() == "DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS"
