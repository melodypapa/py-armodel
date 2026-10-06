"""
Tests for reading the DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS element —
DiagnosticReadDataByPeriodicIDClass, Table 4.98 (p.130, R23-11).

DiagnosticReadDataByPeriodicIDClass (concrete DiagnosticServiceClass, Aggregated
by ARPackage.element) defines three attributes in displayed order:
maxPeriodicDidToRead (PositiveInteger 0..1, MAX-PERIODIC-DID-TO-READ),
periodicRate (DiagnosticPeriodicRate *, PERIODIC-RATES wrapper of
DIAGNOSTIC-PERIODIC-RATE) and schedulerMaxNumber (PositiveInteger 0..1,
SCHEDULER-MAX-NUMBER) — AUTOSAR_00052.xsd group
DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS l.41290.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_read_data_by_periodic_id_class.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticReadDataByPeriodicIDClass:
    """Tests for readDiagnosticReadDataByPeriodicIDClass — own element field values (Table 4.98)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticReadDataByPeriodicIDClass

        cls = DiagnosticReadDataByPeriodicIDClass(parent=MagicMock(), short_name="Rdbpidc1")
        element = _snip(inner, root_tag="DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS")
        parser.readDiagnosticReadDataByPeriodicIDClass(element, cls)
        return cls

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        cls = self._read(parser, "<SHORT-NAME>Rdbpidc1</SHORT-NAME>")
        assert cls.getShortName() == "Rdbpidc1"

    def test_read_max_periodic_did_to_read(self, parser):
        """Test that the MAX-PERIODIC-DID-TO-READ is read into maxPeriodicDidToRead."""
        cls = self._read(parser, "<MAX-PERIODIC-DID-TO-READ>42</MAX-PERIODIC-DID-TO-READ>")
        assert cls.getMaxPeriodicDidToRead() is not None
        assert cls.getMaxPeriodicDidToRead().getValue() == 42

    def test_read_periodic_rates(self, parser):
        """Test that the PERIODIC-RATES wrapper DIAGNOSTIC-PERIODIC-RATE elements are read in document order."""
        inner = (
            "<PERIODIC-RATES>"
            "<DIAGNOSTIC-PERIODIC-RATE><PERIOD>0.5</PERIOD><PERIODIC-RATE-CATEGORY>PERIODIC-RATE-FAST</PERIODIC-RATE-CATEGORY></DIAGNOSTIC-PERIODIC-RATE>"
            "<DIAGNOSTIC-PERIODIC-RATE><PERIODIC-RATE-CATEGORY>PERIODIC-RATE-SLOW</PERIODIC-RATE-CATEGORY></DIAGNOSTIC-PERIODIC-RATE>"
            "</PERIODIC-RATES>"
        )
        cls = self._read(parser, inner)
        rates = cls.getPeriodicRates()
        assert len(rates) == 2
        assert rates[0].getPeriod() is not None
        assert rates[0].getPeriod().getValue() == 0.5
        assert rates[0].getPeriodicRateCategory().getValue() == "PERIODIC-RATE-FAST"
        assert rates[1].getPeriod() is None
        assert rates[1].getPeriodicRateCategory().getValue() == "PERIODIC-RATE-SLOW"

    def test_read_scheduler_max_number(self, parser):
        """Test that the SCHEDULER-MAX-NUMBER is read into schedulerMaxNumber."""
        cls = self._read(parser, "<SCHEDULER-MAX-NUMBER>3</SCHEDULER-MAX-NUMBER>")
        assert cls.getSchedulerMaxNumber() is not None
        assert cls.getSchedulerMaxNumber().getValue() == 3

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving all fields unset."""
        cls = self._read(parser, "<SHORT-NAME>Rdbpidc1</SHORT-NAME>")
        assert cls.getMaxPeriodicDidToRead() is None
        assert cls.getPeriodicRates() == []
        assert cls.getSchedulerMaxNumber() is None
