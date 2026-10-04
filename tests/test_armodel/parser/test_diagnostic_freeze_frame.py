"""
Tests for reading the DIAGNOSTIC-FREEZE-FRAME element —
DiagnosticFreezeFrame, Table 4.183 (p.192, R23-11).

DiagnosticFreezeFrame (Base most-derived ARElement) carries four own
Attribute rows in displayed order. The XSD group DIAGNOSTIC-FREEZE-FRAME
(AUTOSAR_00052.xsd l.37772) fixes the element order CUSTOM-TRIGGER →
RECORD-NUMBER (wrapper of POSITIVE-INTEGER-VALUE-VARIATION-POINT) →
TRIGGER → UPDATE.

recordNumber — markdown Type PositiveInteger wins over the XSD element type
POSITIVE-INTEGER-VALUE-VARIATION-POINT (Rule 0015); the value is read through
the wrapper element (DiagnosticConnectedIndicator HEALING-CYCLE-COUNTER-THRESHOLD
precedent).

TRIGGER round-trips as a raw literal until DiagnosticRecordTriggerEnum
(Table 4.182, queued in Group25) gains its literals.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_freeze_frame.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticFreezeFrame:
    """Tests for readDiagnosticFreezeFrame — own element field values (Table 4.183)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticFreezeFrame

        freeze_frame = DiagnosticFreezeFrame(AUTOSAR.getInstance(), "FreezeFrame1")
        parser.readDiagnosticFreezeFrame(_snip(inner, root_tag="DIAGNOSTIC-FREEZE-FRAME"), freeze_frame)
        return freeze_frame

    def test_read_sets_custom_trigger(self, parser):
        """Test that CUSTOM-TRIGGER is read into customTrigger."""
        freeze_frame = self._read(parser, "<SHORT-NAME>FreezeFrame1</SHORT-NAME><CUSTOM-TRIGGER>custom trigger description</CUSTOM-TRIGGER>")
        assert freeze_frame.getShortName() == "FreezeFrame1"
        assert freeze_frame.getCustomTrigger() is not None
        assert freeze_frame.getCustomTrigger().getValue() == "custom trigger description"

    def test_read_sets_record_number(self, parser):
        """Test that RECORD-NUMBER is read through the POSITIVE-INTEGER-VALUE-VARIATION-POINT wrapper into recordNumber."""
        freeze_frame = self._read(parser, "<RECORD-NUMBER><POSITIVE-INTEGER-VALUE-VARIATION-POINT>40</POSITIVE-INTEGER-VALUE-VARIATION-POINT></RECORD-NUMBER>")
        assert freeze_frame.getRecordNumber() is not None
        assert freeze_frame.getRecordNumber().value == 40

    def test_read_sets_trigger_as_raw_literal(self, parser):
        """Test that TRIGGER is read as a raw literal while DiagnosticRecordTriggerEnum is a stub."""
        freeze_frame = self._read(parser, "<TRIGGER>confirmed</TRIGGER>")
        assert freeze_frame.getTrigger() is not None
        assert isinstance(freeze_frame.getTrigger(), ARLiteral)
        assert freeze_frame.getTrigger().getValue() == "confirmed"

    def test_read_sets_update(self, parser):
        """Test that UPDATE is read into update."""
        freeze_frame = self._read(parser, "<UPDATE>true</UPDATE>")
        assert freeze_frame.getUpdate() is not None
        assert freeze_frame.getUpdate().value is True

    def test_read_empty_leaves_fields_unset(self, parser):
        """Test that an element without own children leaves every field unset (empty wrapper case)."""
        freeze_frame = self._read(parser, "<SHORT-NAME>FreezeFrame1</SHORT-NAME>")
        assert freeze_frame.getCustomTrigger() is None
        assert freeze_frame.getRecordNumber() is None
        assert freeze_frame.getTrigger() is None
        assert freeze_frame.getUpdate() is None
