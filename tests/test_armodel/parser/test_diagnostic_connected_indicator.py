"""
Tests for reading the DIAGNOSTIC-CONNECTED-INDICATOR element —
DiagnosticConnectedIndicator, Table 4.152 (p.167, R23-11).

DiagnosticConnectedIndicator (confirmed queue row Base = ARObject) is a nested
container aggregated by DiagnosticEvent.connectedIndicator (XSD
CONNECTED-INDICATORS wrapper, unbounded DIAGNOSTIC-CONNECTED-INDICATOR items,
AUTOSAR_00052.xsd l.36218). Its own group DIAGNOSTIC-CONNECTED-INDICATOR
(AUTOSAR_00052.xsd l.33483) carries the 0..1 elements BEHAVIOR,
HEALING-CYCLE-COUNTER-THRESHOLD (POSITIVE-INTEGER-VALUE-VARIATION-POINT),
HEALING-CYCLE-REF, INDICATOR-FAILURE-CYCLE-COUNTER-THRESHOLD and INDICATOR-REF
in XSD sequence order. The reader is the named reusable helper
readDiagnosticConnectedIndicator; the consuming parent DiagnosticEvent
(Table 4.149, queued later in Group25) will call it.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_connected_indicator.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticConnectedIndicator

NS = "http://autosar.org/schema/r4.0"

FULL_INNER = (
    "<BEHAVIOR>BLINK-MODE</BEHAVIOR>"
    "<HEALING-CYCLE-COUNTER-THRESHOLD><POSITIVE-INTEGER-VALUE-VARIATION-POINT>3</POSITIVE-INTEGER-VALUE-VARIATION-POINT></HEALING-CYCLE-COUNTER-THRESHOLD>"
    '<HEALING-CYCLE-REF DEST="DIAGNOSTIC-OPERATION-CYCLE">/Dem/DiagnosticOperationCycle</HEALING-CYCLE-REF>'
    "<INDICATOR-FAILURE-CYCLE-COUNTER-THRESHOLD>2</INDICATOR-FAILURE-CYCLE-COUNTER-THRESHOLD>"
    '<INDICATOR-REF DEST="DIAGNOSTIC-INDICATOR">/Dem/DiagnosticIndicator</INDICATOR-REF>'
)


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-CONNECTED-INDICATOR") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticConnectedIndicator:
    """Tests for readDiagnosticConnectedIndicator — own element field values (Table 4.152)."""

    def _read(self, parser, inner):
        connected_indicator = DiagnosticConnectedIndicator()
        parser.readDiagnosticConnectedIndicator(_snip(inner), connected_indicator)
        return connected_indicator

    def test_read_sets_all_fields(self, parser):
        """Test that all five own elements are read with their values, in XSD order."""
        connected_indicator = self._read(parser, FULL_INNER)

        assert connected_indicator.getBehavior() is not None
        assert connected_indicator.getBehavior().getValue() == "BLINK-MODE"
        assert connected_indicator.getHealingCycleCounterThreshold() is not None
        assert connected_indicator.getHealingCycleCounterThreshold().getValue() == 3
        assert connected_indicator.getHealingCycleRef() is not None
        assert connected_indicator.getHealingCycleRef().getValue() == "/Dem/DiagnosticOperationCycle"
        assert connected_indicator.getHealingCycleRef().getDest() == "DIAGNOSTIC-OPERATION-CYCLE"
        assert connected_indicator.getIndicatorFailureCycleCounterThreshold() is not None
        assert connected_indicator.getIndicatorFailureCycleCounterThreshold().getValue() == 2
        assert connected_indicator.getIndicatorRef() is not None
        assert connected_indicator.getIndicatorRef().getValue() == "/Dem/DiagnosticIndicator"
        assert connected_indicator.getIndicatorRef().getDest() == "DIAGNOSTIC-INDICATOR"

    def test_read_empty(self, parser):
        """Test that an empty DIAGNOSTIC-CONNECTED-INDICATOR wrapper leaves the fields None."""
        connected_indicator = self._read(parser, "")
        assert connected_indicator.getBehavior() is None
        assert connected_indicator.getHealingCycleRef() is None
        assert connected_indicator.getHealingCycleCounterThreshold() is None
        assert connected_indicator.getIndicatorRef() is None
        assert connected_indicator.getIndicatorFailureCycleCounterThreshold() is None

    def test_read_without_avp_wrapper_leaves_threshold_none(self, parser):
        """Test that a bare HEALING-CYCLE-COUNTER-THRESHOLD without the VALUE-VARIATION-POINT wrapper is not misread."""
        connected_indicator = self._read(parser, "<HEALING-CYCLE-COUNTER-THRESHOLD></HEALING-CYCLE-COUNTER-THRESHOLD>")
        assert connected_indicator.getHealingCycleCounterThreshold() is None
