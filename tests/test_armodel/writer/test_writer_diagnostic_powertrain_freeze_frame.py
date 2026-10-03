"""
Tests for writing DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME elements —
DiagnosticPowertrainFreezeFrame, Table 4.134 (p.153, R23-11).

DiagnosticPowertrainFreezeFrame (Base most-derived ARElement) owns the *
aggregation pid (PID-REFS wrapper, unbounded PID-REF items, DEST
DIAGNOSTIC-PARAMETER-IDENTIFIER--SUBTYPES-ENUM), AUTOSAR_00052.xsd group
DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME l.40923.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_powertrain_freeze_frame.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticPowertrainFreezeFrame
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


def _make_full_freeze_frame() -> DiagnosticPowertrainFreezeFrame:
    package = AUTOSAR.getInstance().createARPackage("DiagnosticPowertrainFreezeFrames")
    freeze_frame = package.createDiagnosticPowertrainFreezeFrame("Frame1")
    freeze_frame.addPidRef(RefType().setDest("DIAGNOSTIC-PARAMETER-IDENTIFIER").setValue("/AUTOSAR/DiagnosticParameterIdentifiers/Pid1"))
    freeze_frame.addPidRef(RefType().setDest("DIAGNOSTIC-PARAMETER-IDENTIFIER").setValue("/AUTOSAR/DiagnosticParameterIdentifiers/Pid2"))
    return freeze_frame


class TestWriteDiagnosticPowertrainFreezeFrame:
    """Tests for writeDiagnosticPowertrainFreezeFrame — own element field values (Table 4.134)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticPowertrainFreezeFrame without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticPowertrainFreezeFrames")
        package.createDiagnosticPowertrainFreezeFrame("Frame1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticPowertrainFreezeFrame(parent, package.getReferrableElement("Frame1", DiagnosticPowertrainFreezeFrame))

        child = parent.find("DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Frame1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_empty_pid_refs_emit_no_wrapper(self):
        """Test that an empty pidRefs list emits no PID-REFS wrapper element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticPowertrainFreezeFrames")
        freeze_frame = package.createDiagnosticPowertrainFreezeFrame("Frame1")
        freeze_frame.addPidRef(RefType().setDest("DIAGNOSTIC-PARAMETER-IDENTIFIER").setValue("/AUTOSAR/DiagnosticParameterIdentifiers/Pid0"))
        freeze_frame.pidRefs.clear()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticPowertrainFreezeFrame(parent, freeze_frame)

        child = parent.find("DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME")
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("PID-REFS") is None

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        freeze_frame = _make_full_freeze_frame()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticPowertrainFreezeFrame(parent, freeze_frame)

        child = parent.find("DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME")
        assert [c.tag for c in child] == ["SHORT-NAME", "PID-REFS"]
        pid_refs = child.find("PID-REFS")
        assert [c.tag for c in pid_refs] == ["PID-REF", "PID-REF"]
        values = [pid_ref.text for pid_ref in pid_refs.findall("PID-REF")]
        assert values == ["/AUTOSAR/DiagnosticParameterIdentifiers/Pid1", "/AUTOSAR/DiagnosticParameterIdentifiers/Pid2"]
        assert all(pid_ref.get("DEST") == "DIAGNOSTIC-PARAMETER-IDENTIFIER" for pid_ref in pid_refs.findall("PID-REF"))

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        freeze_frame = _make_full_freeze_frame()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticPowertrainFreezeFrame(parent, freeze_frame)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticPowertrainFreezeFrame(AUTOSAR.getInstance(), "Frame1")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME")
        ARXMLParser().readDiagnosticPowertrainFreezeFrame(element, reloaded)
        pid_refs = reloaded.getPidRefs()
        assert len(pid_refs) == 2
        assert pid_refs[0].getValue() == "/AUTOSAR/DiagnosticParameterIdentifiers/Pid1"
        assert pid_refs[0].getDest() == "DIAGNOSTIC-PARAMETER-IDENTIFIER"
        assert pid_refs[1].getValue() == "/AUTOSAR/DiagnosticParameterIdentifiers/Pid2"
        assert pid_refs[1].getDest() == "DIAGNOSTIC-PARAMETER-IDENTIFIER"
