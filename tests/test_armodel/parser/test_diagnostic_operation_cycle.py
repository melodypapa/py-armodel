"""
Tests for reading the DIAGNOSTIC-OPERATION-CYCLE element —
DiagnosticOperationCycle, Table 4.196 (p.201, R23-11).

DiagnosticOperationCycle (Base most-derived ARElement) carries one own Attribute
row — type (DiagnosticOperationCycleTypeEnum, 0..1, attr) — read as the single
TYPE child (AUTOSAR_00052.xsd l.40330; the group's AUTOMATIC-END,
CYCLE-AUTOSTART and CYCLE-STATUS-STORAGE elements carry atp.Status="removed" and
are not modeled). type round-trips as the typed DiagnosticOperationCycleTypeEnum
(Table 4.197) literal — the TYPE XSD token maps to the enum value.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_operation_cycle.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagnosticOperationCycleTypeEnum
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticOperationCycle:
    """Tests for readDiagnosticOperationCycle — own element field values (Table 4.196)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticOperationCycle

        cycle = DiagnosticOperationCycle(AUTOSAR.getInstance(), "OperationCycle1")
        parser.readDiagnosticOperationCycle(_snip(inner, root_tag="DIAGNOSTIC-OPERATION-CYCLE"), cycle)
        return cycle

    def test_read_sets_short_name(self, parser):
        """Test that the SHORT-NAME child is read into the Identifiable chain."""
        cycle = self._read(parser, "<SHORT-NAME>OperationCycle1</SHORT-NAME>")
        assert cycle.getShortName() == "OperationCycle1"

    def test_read_sets_type_token(self, parser):
        """Test that the TYPE token is read as the typed enum literal."""
        cycle = self._read(parser, "<TYPE>IGNITION</TYPE>")
        assert cycle.getType() is not None
        assert isinstance(cycle.getType(), DiagnosticOperationCycleTypeEnum)
        assert cycle.getType().getValue() == "ignition"

    def test_read_empty_leaves_fields_none(self, parser):
        """Test that an element without own children leaves every field None (empty wrapper case)."""
        cycle = self._read(parser, "<SHORT-NAME>OperationCycle1</SHORT-NAME>")
        assert cycle.getType() is None
