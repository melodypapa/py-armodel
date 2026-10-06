"""
Tests for reading the DIAGNOSTIC-EXTENDED-DATA-RECORD element —
DiagnosticExtendedDataRecord, Table 4.181 (p.190, R23-11).

DiagnosticExtendedDataRecord (Base most-derived ARElement) carries five own
Attribute rows in displayed order. The XSD group DIAGNOSTIC-EXTENDED-DATA-RECORD
(AUTOSAR_00052.xsd l.37166) fixes the element order CUSTOM-TRIGGER →
RECORD-ELEMENTS (wrapper of DIAGNOSTIC-PARAMETER) → RECORD-NUMBER → TRIGGER →
UPDATE.

TRIGGER round-trips as the typed DiagnosticRecordTriggerEnum (Table 4.182)
literal — the TRIGGER XSD token maps to the enum value.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_extended_data_record.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagnosticRecordTriggerEnum
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticExtendedDataRecord:
    """Tests for readDiagnosticExtendedDataRecord — own element field values (Table 4.181)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticExtendedDataRecord

        record = DiagnosticExtendedDataRecord(AUTOSAR.getInstance(), "Record1")
        parser.readDiagnosticExtendedDataRecord(_snip(inner, root_tag="DIAGNOSTIC-EXTENDED-DATA-RECORD"), record)
        return record

    def test_read_sets_custom_trigger(self, parser):
        """Test that CUSTOM-TRIGGER is read into customTrigger."""
        record = self._read(parser, "<SHORT-NAME>Record1</SHORT-NAME><CUSTOM-TRIGGER>custom trigger description</CUSTOM-TRIGGER>")
        assert record.getShortName() == "Record1"
        assert record.getCustomTrigger() is not None
        assert record.getCustomTrigger().getValue() == "custom trigger description"

    def test_read_sets_record_elements(self, parser):
        """Test that the RECORD-ELEMENTS wrapper items are read into the recordElements list."""
        record = self._read(
            parser,
            "<RECORD-ELEMENTS>"
            "<DIAGNOSTIC-PARAMETER><SHORT-NAME>Param1</SHORT-NAME><IDENT><SHORT-NAME>Param1</SHORT-NAME></IDENT></DIAGNOSTIC-PARAMETER>"
            "<DIAGNOSTIC-PARAMETER><SHORT-NAME>Param2</SHORT-NAME><IDENT><SHORT-NAME>Param2</SHORT-NAME></IDENT></DIAGNOSTIC-PARAMETER>"
            "</RECORD-ELEMENTS>",
        )
        record_elements = record.getRecordElements()
        assert len(record_elements) == 2
        assert record_elements[0].getIdent() is not None
        assert record_elements[0].getIdent().getShortName() == "Param1"
        assert record_elements[1].getIdent() is not None
        assert record_elements[1].getIdent().getShortName() == "Param2"

    def test_read_sets_record_number(self, parser):
        """Test that RECORD-NUMBER is read into recordNumber."""
        record = self._read(parser, "<RECORD-NUMBER>40</RECORD-NUMBER>")
        assert record.getRecordNumber() is not None
        assert record.getRecordNumber().value == 40

    def test_read_sets_trigger(self, parser):
        """Test that the TRIGGER token is read as the typed enum literal."""
        record = self._read(parser, "<TRIGGER>CONFIRMED</TRIGGER>")
        assert record.getTrigger() is not None
        assert isinstance(record.getTrigger(), DiagnosticRecordTriggerEnum)
        assert record.getTrigger().getValue() == "CONFIRMED"

    def test_read_sets_update(self, parser):
        """Test that UPDATE is read into update."""
        record = self._read(parser, "<UPDATE>true</UPDATE>")
        assert record.getUpdate() is not None
        assert record.getUpdate().value is True

    def test_read_empty_leaves_fields_unset(self, parser):
        """Test that an element without own children leaves every field unset and the list empty (empty wrapper case)."""
        record = self._read(parser, "<SHORT-NAME>Record1</SHORT-NAME>")
        assert record.getCustomTrigger() is None
        assert record.getRecordElements() == []
        assert record.getRecordNumber() is None
        assert record.getTrigger() is None
        assert record.getUpdate() is None
