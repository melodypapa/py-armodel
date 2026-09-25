"""
Tests for reading RECEPTION-PROPS elements — ReceptionComSpecProps, Table 4.64 (p.174, R23-11).

ReceptionComSpecProps (Base = ARObject) carries the optional reception attributes
DATA-UPDATE-PERIOD and TIMEOUT (both TIME-VALUE, 0..1). It is aggregated by
ReceiverComSpec.receptionProps and read through the concrete receiver comspec
dispatch (getQueuedReceiverComSpec / getNonqueuedReceiverComSpec → readReceiverComSpec
→ getReceptionComSpecProps).

Round-trip counterpart: tests/test_armodel/writer/test_reception_com_spec_props.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestGetReceptionComSpecProps:
    """Tests for getReceptionComSpecProps — own element field values (Table 4.64)."""

    def test_with_both_elements(self, parser):
        """Test that DATA-UPDATE-PERIOD and TIMEOUT are read with their field values."""
        element = _snip(
            "<RECEPTION-PROPS>" "<DATA-UPDATE-PERIOD>0.02</DATA-UPDATE-PERIOD>" "<TIMEOUT>2.5</TIMEOUT>" "</RECEPTION-PROPS>",
            root_tag="RECEIVER-COM-SPEC",
        )
        result = parser.getReceptionComSpecProps(element, "RECEPTION-PROPS")
        assert result is not None
        assert result.getDataUpdatePeriod() is not None
        assert result.getDataUpdatePeriod().getValue() == 0.02
        assert result.getTimeout() is not None
        assert result.getTimeout().getValue() == 2.5

    def test_with_timeout_only(self, parser):
        """Test that DATA-UPDATE-PERIOD stays None when the element is absent."""
        element = _snip(
            "<RECEPTION-PROPS>" "<TIMEOUT>2.5</TIMEOUT>" "</RECEPTION-PROPS>",
            root_tag="RECEIVER-COM-SPEC",
        )
        result = parser.getReceptionComSpecProps(element, "RECEPTION-PROPS")
        assert result is not None
        assert result.getDataUpdatePeriod() is None
        assert result.getTimeout() is not None
        assert result.getTimeout().getValue() == 2.5

    def test_minimal_props(self, parser):
        """Test that both fields stay None when the wrapper carries no child elements."""
        element = _snip(
            "<RECEPTION-PROPS />",
            root_tag="RECEIVER-COM-SPEC",
        )
        result = parser.getReceptionComSpecProps(element, "RECEPTION-PROPS")
        assert result is not None
        assert result.getDataUpdatePeriod() is None
        assert result.getTimeout() is None

    def test_absent_props(self, parser):
        """Test that a missing RECEPTION-PROPS element yields None (no instance)."""
        element = _snip("", root_tag="RECEIVER-COM-SPEC")
        result = parser.getReceptionComSpecProps(element, "RECEPTION-PROPS")
        assert result is None

    def test_read_via_queued_receiver_com_spec(self, parser):
        """Test that the ReceiverComSpec aggregation reads receptionProps with field values."""
        element = _snip(
            "<RECEPTION-PROPS>" "<DATA-UPDATE-PERIOD>0.5</DATA-UPDATE-PERIOD>" "<TIMEOUT>1.0</TIMEOUT>" "</RECEPTION-PROPS>" "<QUEUE-LENGTH>10</QUEUE-LENGTH>",
            root_tag="QUEUED-RECEIVER-COM-SPEC",
        )
        com_spec = parser.getQueuedReceiverComSpec(element)
        assert com_spec is not None
        props = com_spec.getReceptionProps()
        assert props is not None
        assert props.getDataUpdatePeriod() is not None
        assert props.getDataUpdatePeriod().getValue() == 0.5
        assert props.getTimeout() is not None
        assert props.getTimeout().getValue() == 1.0
