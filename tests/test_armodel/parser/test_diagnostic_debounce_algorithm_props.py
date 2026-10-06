"""
Tests for reading the DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS element —
DiagnosticDebounceAlgorithmProps, Table 4.187 (p.196, R23-11).

DiagnosticDebounceAlgorithmProps (Base most-derived Identifiable) aggregates one
polymorphic 0..1 debounceAlgorithm (XSD wrapper DEBOUNCE-ALGORITHM holding a choice of
DIAG-EVENT-DEBOUNCE-COUNTER-BASED / DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL /
DIAG-EVENT-DEBOUNCE-TIME-BASED — XSD group DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS,
AUTOSAR_00052.xsd l.34682) plus the 0..1 debounceBehavior enum token and the 0..1
debounceCounterStorage boolean.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_debounce_algorithm_props.py
"""

from unittest.mock import MagicMock

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagEventDebounceCounterBased, DiagEventDebounceMonitorInternal, DiagEventDebounceTimeBased
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticCommonProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticDebounceAlgorithmProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagnosticDebounceBehaviorEnum
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticDebounceAlgorithmProps:
    """Tests for readDiagnosticDebounceAlgorithmProps — own element field values (Table 4.187)."""

    def _read(self, parser, inner):
        debounce_props = DiagnosticDebounceAlgorithmProps(parent=MagicMock(), short_name="DebounceProps1")
        element = _snip(inner, root_tag="DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS")
        parser.readDiagnosticDebounceAlgorithmProps(element, debounce_props)
        return debounce_props

    def test_with_counter_based_algorithm(self, parser):
        """Test that the DEBOUNCE-ALGORITHM choice reads a DIAG-EVENT-DEBOUNCE-COUNTER-BASED with field values."""
        inner = (
            "<SHORT-NAME>DebounceProps1</SHORT-NAME>"
            "<DEBOUNCE-ALGORITHM>"
            "<DIAG-EVENT-DEBOUNCE-COUNTER-BASED>"
            "<SHORT-NAME>CounterBased</SHORT-NAME>"
            "<COUNTER-FAILED-THRESHOLD>3</COUNTER-FAILED-THRESHOLD>"
            "<COUNTER-JUMP-DOWN>true</COUNTER-JUMP-DOWN>"
            "</DIAG-EVENT-DEBOUNCE-COUNTER-BASED>"
            "</DEBOUNCE-ALGORITHM>"
        )
        debounce_props = self._read(parser, inner)
        assert debounce_props.getShortName() == "DebounceProps1"
        algorithm = debounce_props.getDebounceAlgorithm()
        assert isinstance(algorithm, DiagEventDebounceCounterBased)
        assert algorithm.getShortName() == "CounterBased"
        assert algorithm.getCounterFailedThreshold().getValue() == 3
        assert algorithm.getCounterJumpDown().getValue() is True

    def test_with_monitor_internal_algorithm(self, parser):
        """Test that the DEBOUNCE-ALGORITHM choice reads a DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL."""
        inner = (
            "<SHORT-NAME>DebounceProps1</SHORT-NAME>"
            "<DEBOUNCE-ALGORITHM>"
            "<DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL>"
            "<SHORT-NAME>MonitorInternal</SHORT-NAME>"
            "</DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL>"
            "</DEBOUNCE-ALGORITHM>"
        )
        debounce_props = self._read(parser, inner)
        algorithm = debounce_props.getDebounceAlgorithm()
        assert isinstance(algorithm, DiagEventDebounceMonitorInternal)
        assert algorithm.getShortName() == "MonitorInternal"

    def test_with_time_based_algorithm(self, parser):
        """Test that the DEBOUNCE-ALGORITHM choice reads a DIAG-EVENT-DEBOUNCE-TIME-BASED with field values."""
        inner = (
            "<SHORT-NAME>DebounceProps1</SHORT-NAME>"
            "<DEBOUNCE-ALGORITHM>"
            "<DIAG-EVENT-DEBOUNCE-TIME-BASED>"
            "<SHORT-NAME>TimeBased</SHORT-NAME>"
            "<TIME-FAILED-THRESHOLD>0.5</TIME-FAILED-THRESHOLD>"
            "</DIAG-EVENT-DEBOUNCE-TIME-BASED>"
            "</DEBOUNCE-ALGORITHM>"
        )
        debounce_props = self._read(parser, inner)
        algorithm = debounce_props.getDebounceAlgorithm()
        assert isinstance(algorithm, DiagEventDebounceTimeBased)
        assert algorithm.getShortName() == "TimeBased"
        assert algorithm.getTimeFailedThreshold().getValue() == 0.5

    def test_with_debounce_counter_storage(self, parser):
        """Test that DEBOUNCE-COUNTER-STORAGE is read as a Boolean value."""
        inner = "<SHORT-NAME>DebounceProps1</SHORT-NAME>" "<DEBOUNCE-COUNTER-STORAGE>true</DEBOUNCE-COUNTER-STORAGE>"
        debounce_props = self._read(parser, inner)
        assert debounce_props.getDebounceCounterStorage() is not None
        assert debounce_props.getDebounceCounterStorage().getValue() is True

    def test_with_debounce_behavior(self, parser):
        """Test that the DEBOUNCE-BEHAVIOR token is read into the DiagnosticDebounceBehaviorEnum."""
        inner = "<SHORT-NAME>DebounceProps1</SHORT-NAME>" "<DEBOUNCE-BEHAVIOR>FREEZE</DEBOUNCE-BEHAVIOR>"
        debounce_props = self._read(parser, inner)
        assert debounce_props.getDebounceBehavior() is not None
        assert debounce_props.getDebounceBehavior().getValue() == DiagnosticDebounceBehaviorEnum.FREEZE

    def test_empty_wrapper(self, parser):
        """Test that a props element without own children leaves all fields unset."""
        debounce_props = self._read(parser, "<SHORT-NAME>DebounceProps1</SHORT-NAME>")
        assert debounce_props.getDebounceAlgorithm() is None
        assert debounce_props.getDebounceBehavior() is None
        assert debounce_props.getDebounceCounterStorage() is None

    def test_aggregated_through_common_props(self, parser):
        """Test that readDiagnosticCommonProps wires the DEBOUNCE-ALGORITHM-PROPSS items through the helper."""
        inner = (
            "<DIAGNOSTIC-COMMON-PROPS-VARIANTS>"
            "<DIAGNOSTIC-COMMON-PROPS-CONDITIONAL>"
            "<DEBOUNCE-ALGORITHM-PROPSS>"
            "<DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS>"
            "<SHORT-NAME>DebounceProps1</SHORT-NAME>"
            "<DEBOUNCE-ALGORITHM>"
            "<DIAG-EVENT-DEBOUNCE-COUNTER-BASED>"
            "<SHORT-NAME>CounterBased</SHORT-NAME>"
            "<COUNTER-PASSED-THRESHOLD>126</COUNTER-PASSED-THRESHOLD>"
            "</DIAG-EVENT-DEBOUNCE-COUNTER-BASED>"
            "</DEBOUNCE-ALGORITHM>"
            "<DEBOUNCE-COUNTER-STORAGE>false</DEBOUNCE-COUNTER-STORAGE>"
            "</DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS>"
            "</DEBOUNCE-ALGORITHM-PROPSS>"
            "</DIAGNOSTIC-COMMON-PROPS-CONDITIONAL>"
            "</DIAGNOSTIC-COMMON-PROPS-VARIANTS>"
        )
        common_props = DiagnosticCommonProps()
        element = _snip(inner, root_tag="COMMON-PROPERTIES")
        parser.readDiagnosticCommonProps(element, common_props)
        debounce_props = common_props.getDebounceAlgorithmProps()
        assert len(debounce_props) == 1
        assert debounce_props[0].getShortName() == "DebounceProps1"
        algorithm = debounce_props[0].getDebounceAlgorithm()
        assert isinstance(algorithm, DiagEventDebounceCounterBased)
        assert algorithm.getCounterPassedThreshold().getValue() == 126
        assert debounce_props[0].getDebounceCounterStorage().getValue() is False
