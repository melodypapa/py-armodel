"""
Tests for reading the DIAGNOSTIC-AGING element —
DiagnosticAging, Table 4.198 (p.202, R23-11).

DiagnosticAging (Base most-derived ARElement) carries two 0..1 attributes —
agingCycle (ref, XSD wrapper AGING-CYCLES/DIAGNOSTIC-OPERATION-CYCLE-REF-CONDITIONAL/
DIAGNOSTIC-OPERATION-CYCLE-REF) and threshold (attr, XSD element THRESHOLD of type
POSITIVE-INTEGER-VALUE-VARIATION-POINT, value carried as element text) — XSD group
DIAGNOSTIC-AGING, AUTOSAR_00052.xsd l.31615.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_aging.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticAging:
    """Tests for readDiagnosticAging — own element field values (Table 4.198)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticAging

        aging = DiagnosticAging(parent=MagicMock(), short_name="Aging1")
        element = _snip(inner, root_tag="DIAGNOSTIC-AGING")
        parser.readDiagnosticAging(element, aging)
        return aging

    def test_with_aging_cycle_ref_and_threshold(self, parser):
        """Test that AGING-CYCLES and THRESHOLD are read with field values."""
        inner = (
            "<SHORT-NAME>Aging1</SHORT-NAME>"
            "<AGING-CYCLES>"
            "<DIAGNOSTIC-OPERATION-CYCLE-REF-CONDITIONAL>"
            '<DIAGNOSTIC-OPERATION-CYCLE-REF DEST="DIAGNOSTIC-OPERATION-CYCLE">/AUTOSAR/DiagnosticOperationCycles/Cycle1</DIAGNOSTIC-OPERATION-CYCLE-REF>'
            "</DIAGNOSTIC-OPERATION-CYCLE-REF-CONDITIONAL>"
            "</AGING-CYCLES>"
            "<THRESHOLD>5</THRESHOLD>"
        )
        aging = self._read(parser, inner)
        assert aging.getShortName() == "Aging1"
        assert aging.getAgingCycleRef() is not None
        assert aging.getAgingCycleRef().getDest() == "DIAGNOSTIC-OPERATION-CYCLE"
        assert aging.getAgingCycleRef().getValue() == "/AUTOSAR/DiagnosticOperationCycles/Cycle1"
        assert aging.getThreshold() is not None
        assert aging.getThreshold().getValue() == 5

    def test_without_attributes(self, parser):
        """Test that absent AGING-CYCLES / THRESHOLD leave the fields None."""
        aging = self._read(parser, "<SHORT-NAME>Aging1</SHORT-NAME>")
        assert aging.getAgingCycleRef() is None
        assert aging.getThreshold() is None

    def test_threshold_only(self, parser):
        """Test that a THRESHOLD without the AGING-CYCLES wrapper is read."""
        inner = "<SHORT-NAME>Aging1</SHORT-NAME><THRESHOLD>12</THRESHOLD>"
        aging = self._read(parser, inner)
        assert aging.getAgingCycleRef() is None
        assert aging.getThreshold() is not None
        assert aging.getThreshold().getValue() == 12
