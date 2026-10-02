"""
Tests for reading the DIAGNOSTIC-PERIODIC-RATE element —
DiagnosticPeriodicRate, Table 4.99 (p.131, R23-11).

DiagnosticPeriodicRate (concrete ARObject, Aggregated by
DiagnosticReadDataByPeriodicIDClass.periodicRate) defines two 0..1 attributes:
period (TimeValue, PERIOD) and periodicRateCategory
(DiagnosticPeriodicRateCategoryEnum, PERIODIC-RATE-CATEGORY) —
AUTOSAR_00052.xsd group DIAGNOSTIC-PERIODIC-RATE l.40879. The reusable
readDiagnosticPeriodicRate helper is verified directly; the aggregator
dispatch is wired with the DiagnosticReadDataByPeriodicIDClass pass.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_periodic_rate.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticPeriodicRate:
    """Tests for readDiagnosticPeriodicRate — own element field values (Table 4.99)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticPeriodicRate

        rate = DiagnosticPeriodicRate()
        element = _snip(inner, root_tag="DIAGNOSTIC-PERIODIC-RATE")
        parser.readDiagnosticPeriodicRate(element, rate)
        return rate

    def test_read_period(self, parser):
        """Test that the PERIOD is read into period."""
        rate = self._read(parser, "<PERIOD>0.5</PERIOD>")
        assert rate.getPeriod() is not None
        assert rate.getPeriod().getValue() == 0.5

    def test_read_periodic_rate_category(self, parser):
        """Test that the PERIODIC-RATE-CATEGORY enum token is read into periodicRateCategory."""
        rate = self._read(parser, "<PERIODIC-RATE-CATEGORY>PERIODIC-RATE-MEDIUM</PERIODIC-RATE-CATEGORY>")
        assert rate.getPeriodicRateCategory() is not None
        assert rate.getPeriodicRateCategory().getValue() == "periodicRateMedium"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving all fields unset."""
        rate = self._read(parser, "")
        assert rate.getPeriod() is None
        assert rate.getPeriodicRateCategory() is None
