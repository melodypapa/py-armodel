"""
Tests for writing the DIAGNOSTIC-CONNECTED-INDICATOR element —
DiagnosticConnectedIndicator, Table 4.152 (p.167, R23-11).

DiagnosticConnectedIndicator (confirmed queue row Base = ARObject) is a nested
container aggregated by DiagnosticEvent.connectedIndicator; the writer emits one
DIAGNOSTIC-CONNECTED-INDICATOR item element per aggregation entry via the named
reusable helper writeDiagnosticConnectedIndicator. The children follow the XSD
group sequence (AUTOSAR_00052.xsd l.33483): BEHAVIOR,
HEALING-CYCLE-COUNTER-THRESHOLD (POSITIVE-INTEGER-VALUE-VARIATION-POINT),
HEALING-CYCLE-REF, INDICATOR-FAILURE-CYCLE-COUNTER-THRESHOLD, INDICATOR-REF.
The consuming parent DiagnosticEvent (Table 4.149, queued later in Group25)
will call the helper.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_connected_indicator.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticConnectedIndicator
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagnosticConnectedIndicatorBehaviorEnum, PositiveInteger, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = ["BEHAVIOR", "HEALING-CYCLE-COUNTER-THRESHOLD", "HEALING-CYCLE-REF", "INDICATOR-FAILURE-CYCLE-COUNTER-THRESHOLD", "INDICATOR-REF"]


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_connected_indicator() -> DiagnosticConnectedIndicator:
    connected_indicator = DiagnosticConnectedIndicator()
    connected_indicator.setBehavior(DiagnosticConnectedIndicatorBehaviorEnum().setValue(DiagnosticConnectedIndicatorBehaviorEnum.BLINK_MODE))
    connected_indicator.setHealingCycleCounterThreshold(PositiveInteger().setValue("3"))
    healing_cycle_ref = RefType().setValue("/Dem/DiagnosticOperationCycle")
    healing_cycle_ref.setDest("DIAGNOSTIC-OPERATION-CYCLE")
    connected_indicator.setHealingCycleRef(healing_cycle_ref)
    connected_indicator.setIndicatorFailureCycleCounterThreshold(PositiveInteger().setValue("2"))
    indicator_ref = RefType().setValue("/Dem/DiagnosticIndicator")
    indicator_ref.setDest("DIAGNOSTIC-INDICATOR")
    connected_indicator.setIndicatorRef(indicator_ref)
    return connected_indicator


class TestWriteDiagnosticConnectedIndicator:
    """Tests for writeDiagnosticConnectedIndicator — own element field values (Table 4.152)."""

    def test_write_fields_in_xsd_order(self):
        """Test that the five own elements are emitted in XSD sequence order with the spec values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticConnectedIndicator(parent, _make_connected_indicator())

        child = parent.find("DIAGNOSTIC-CONNECTED-INDICATOR")
        assert child is not None
        assert [c.tag for c in child] == XSD_CHILD_ORDER
        assert child.find("BEHAVIOR").text == "BLINK-MODE"
        assert child.find("HEALING-CYCLE-COUNTER-THRESHOLD/POSITIVE-INTEGER-VALUE-VARIATION-POINT").text == "3"
        assert child.find("HEALING-CYCLE-REF").text == "/Dem/DiagnosticOperationCycle"
        assert child.find("HEALING-CYCLE-REF").attrib["DEST"] == "DIAGNOSTIC-OPERATION-CYCLE"
        assert child.find("INDICATOR-FAILURE-CYCLE-COUNTER-THRESHOLD").text == "2"
        assert child.find("INDICATOR-REF").text == "/Dem/DiagnosticIndicator"
        assert child.find("INDICATOR-REF").attrib["DEST"] == "DIAGNOSTIC-INDICATOR"

    def test_write_unset_fields_emit_no_children(self):
        """Test that unset fields emit the empty DIAGNOSTIC-CONNECTED-INDICATOR wrapper only."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticConnectedIndicator(parent, DiagnosticConnectedIndicator())

        child = parent.find("DIAGNOSTIC-CONNECTED-INDICATOR")
        assert child is not None
        assert [c.tag for c in child] == []

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        parent = ET.Element("PARENT", {"xmlns": NS})
        ARXMLWriter().writeDiagnosticConnectedIndicator(parent, _make_connected_indicator())
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticConnectedIndicator()
        element = ET.fromstring(xml_text).find("{%s}DIAGNOSTIC-CONNECTED-INDICATOR" % NS)
        ARXMLParser().readDiagnosticConnectedIndicator(element, reloaded)

        assert reloaded.getBehavior() is not None
        assert isinstance(reloaded.getBehavior(), DiagnosticConnectedIndicatorBehaviorEnum)
        assert reloaded.getBehavior().getValue() == "blinkMode"
        assert reloaded.getHealingCycleCounterThreshold() is not None
        assert reloaded.getHealingCycleCounterThreshold().getValue() == 3
        assert reloaded.getHealingCycleRef() is not None
        assert reloaded.getHealingCycleRef().getValue() == "/Dem/DiagnosticOperationCycle"
        assert reloaded.getHealingCycleRef().getDest() == "DIAGNOSTIC-OPERATION-CYCLE"
        assert reloaded.getIndicatorFailureCycleCounterThreshold() is not None
        assert reloaded.getIndicatorFailureCycleCounterThreshold().getValue() == 2
        assert reloaded.getIndicatorRef() is not None
        assert reloaded.getIndicatorRef().getValue() == "/Dem/DiagnosticIndicator"
        assert reloaded.getIndicatorRef().getDest() == "DIAGNOSTIC-INDICATOR"
