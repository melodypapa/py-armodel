"""
Tests for reading the DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID element —
DiagnosticReadDataByPeriodicID, Table 4.97 (p.130, R23-11).

DiagnosticReadDataByPeriodicID (concrete ARElement, Aggregated by
ARPackage.element) defines one 0..1 attribute: readDataClass (ref, DEST
DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS--SUBTYPES-ENUM,
READ-DATA-CLASS-REF) — AUTOSAR_00052.xsd group
DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID l.41230. The group also carries
DATA-IDENTIFIER-REF with atp.Status="removed" — not a Table 4.97 row, not modeled.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_read_data_by_periodic_id.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticReadDataByPeriodicID:
    """Tests for readDiagnosticReadDataByPeriodicID — own element field values (Table 4.97)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticReadDataByPeriodicID

        obj = DiagnosticReadDataByPeriodicID(parent=MagicMock(), short_name="Rdbpid1")
        element = _snip(inner, root_tag="DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID")
        parser.readDiagnosticReadDataByPeriodicID(element, obj)
        return obj

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        obj = self._read(parser, "<SHORT-NAME>Rdbpid1</SHORT-NAME>")
        assert obj.getShortName() == "Rdbpid1"

    def test_read_read_data_class_ref(self, parser):
        """Test that the READ-DATA-CLASS-REF is read with its DEST attribute."""
        inner = '<READ-DATA-CLASS-REF DEST="DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS">/AUTOSAR/DiagnosticReadDataByPeriodicIds/Class1</READ-DATA-CLASS-REF>'
        obj = self._read(parser, inner)
        assert obj.getReadDataClass() is not None
        assert obj.getReadDataClass().getValue() == "/AUTOSAR/DiagnosticReadDataByPeriodicIds/Class1"
        assert obj.getReadDataClass().getDest() == "DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving all fields unset."""
        obj = self._read(parser, "<SHORT-NAME>Rdbpid1</SHORT-NAME>")
        assert obj.getReadDataClass() is None
