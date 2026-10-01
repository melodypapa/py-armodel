"""
Tests for reading DIAG-EVENT-DEBOUNCE-TIME-BASED elements — DiagEventDebounceTimeBased, Table 12.34 (p.260, R23-11).

DiagEventDebounceTimeBased (Base = DiagEventDebounceAlgorithm) carries the optional
time attributes TIME-BASED-FDC-THRESHOLD-STORAGE-VALUE, TIME-FAILED-THRESHOLD and
TIME-PASSED-THRESHOLD (all TIME-VALUE, 0..1, XSD group order). The reader populates
the model via the setTime* mutators; the dispatch entry is
readDiagEventDebounceAlgorithm → readDiagEventDebounceTimeBased.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diag_event_debounce_time_based.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagEventDebounceTimeBased:
    """Tests for readDiagEventDebounceTimeBased — own element field values (Table 12.34)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagEventDebounceTimeBased

        algorithm = DiagEventDebounceTimeBased(parent=MagicMock(), short_name="Di")
        element = _snip(inner, root_tag="DIAG-EVENT-DEBOUNCE-TIME-BASED")
        parser.readDiagEventDebounceTimeBased(element, algorithm)
        return algorithm

    def test_with_all_elements(self, parser):
        """Test that all three TIME-* elements are read with their field values."""
        algorithm = self._read(
            parser,
            "<SHORT-NAME>Di</SHORT-NAME>"
            "<TIME-BASED-FDC-THRESHOLD-STORAGE-VALUE>0.005</TIME-BASED-FDC-THRESHOLD-STORAGE-VALUE>"
            "<TIME-FAILED-THRESHOLD>1.5</TIME-FAILED-THRESHOLD>"
            "<TIME-PASSED-THRESHOLD>2.0</TIME-PASSED-THRESHOLD>",
        )
        assert algorithm.getTimeBasedFdcThresholdStorageValue() is not None
        assert algorithm.getTimeBasedFdcThresholdStorageValue().getValue() == 0.005
        assert algorithm.getTimeFailedThreshold() is not None
        assert algorithm.getTimeFailedThreshold().getValue() == 1.5
        assert algorithm.getTimePassedThreshold() is not None
        assert algorithm.getTimePassedThreshold().getValue() == 2.0

    def test_with_partial_elements(self, parser):
        """Test that absent TIME-* elements leave their fields None."""
        algorithm = self._read(
            parser,
            "<SHORT-NAME>Di</SHORT-NAME>" "<TIME-FAILED-THRESHOLD>1.5</TIME-FAILED-THRESHOLD>",
        )
        assert algorithm.getTimeBasedFdcThresholdStorageValue() is None
        assert algorithm.getTimeFailedThreshold() is not None
        assert algorithm.getTimeFailedThreshold().getValue() == 1.5
        assert algorithm.getTimePassedThreshold() is None

    def test_empty_wrapper(self, parser):
        """Test that an element without any TIME-* child leaves all fields None."""
        algorithm = self._read(parser, "<SHORT-NAME>Di</SHORT-NAME>")
        assert algorithm.getTimeBasedFdcThresholdStorageValue() is None
        assert algorithm.getTimeFailedThreshold() is None
        assert algorithm.getTimePassedThreshold() is None

    def test_read_via_algorithm_dispatch(self, parser):
        """Test that readDiagEventDebounceAlgorithm dispatches DIAG-EVENT-DEBOUNCE-TIME-BASED with field values."""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticEventNeeds

        needs = DiagnosticEventNeeds(parent=MagicMock(), short_name="Den")
        element = _snip(
            "<DIAG-EVENT-DEBOUNCE-ALGORITHM>"
            "<DIAG-EVENT-DEBOUNCE-TIME-BASED>"
            "<SHORT-NAME>Di</SHORT-NAME>"
            "<TIME-BASED-FDC-THRESHOLD-STORAGE-VALUE>0.005</TIME-BASED-FDC-THRESHOLD-STORAGE-VALUE>"
            "<TIME-FAILED-THRESHOLD>1.5</TIME-FAILED-THRESHOLD>"
            "<TIME-PASSED-THRESHOLD>2.0</TIME-PASSED-THRESHOLD>"
            "</DIAG-EVENT-DEBOUNCE-TIME-BASED>"
            "</DIAG-EVENT-DEBOUNCE-ALGORITHM>"
        )
        parser.readDiagEventDebounceAlgorithm(element, needs)
        algorithm = needs.getDiagEventDebounceAlgorithm()
        assert algorithm is not None
        assert algorithm.getShortName() == "Di"
        assert algorithm.getTimeBasedFdcThresholdStorageValue().getValue() == 0.005
        assert algorithm.getTimeFailedThreshold().getValue() == 1.5
        assert algorithm.getTimePassedThreshold().getValue() == 2.0
