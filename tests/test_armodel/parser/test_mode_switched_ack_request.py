"""
Tests for reading MODE-SWITCHED-ACK elements — ModeSwitchedAckRequest, Table 4.80 (p.190, R23-11).

ModeSwitchedAckRequest (Base = ARObject) carries the optional TIMEOUT attribute
(TIME-VALUE, 0..1). It is aggregated by ModeSwitchSenderComSpec.modeSwitchedAck and
read through getModeSwitchSenderComSpec → getModeSwitchedAckRequest.

Round-trip counterpart: tests/test_armodel/writer/test_mode_switched_ack_request.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestGetModeSwitchedAckRequest:
    """Tests for getModeSwitchedAckRequest — own element field values (Table 4.80)."""

    def test_with_timeout_field_value(self, parser):
        """Test that TIMEOUT is read with its field value."""
        element = _snip("<MODE-SWITCHED-ACK><TIMEOUT>0.5</TIMEOUT></MODE-SWITCHED-ACK>")
        result = parser.getModeSwitchedAckRequest(element, "MODE-SWITCHED-ACK")
        assert result is not None
        assert result.getTimeout() is not None
        assert result.getTimeout().getValue() == 0.5

    def test_empty_element(self, parser):
        """Test that an empty MODE-SWITCHED-ACK element yields an instance with timeout None."""
        element = _snip("<MODE-SWITCHED-ACK />")
        result = parser.getModeSwitchedAckRequest(element, "MODE-SWITCHED-ACK")
        assert result is not None
        assert result.getTimeout() is None

    def test_absent_element(self, parser):
        """Test that a missing MODE-SWITCHED-ACK element yields None (no instance)."""
        element = _snip("")
        result = parser.getModeSwitchedAckRequest(element, "MODE-SWITCHED-ACK")
        assert result is None

    def test_ar_object_attributes_read(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read."""
        element = _snip('<MODE-SWITCHED-ACK S="abc123" T="2024-01-01T12:00:00+00:00"><TIMEOUT>0.5</TIMEOUT></MODE-SWITCHED-ACK>')
        result = parser.getModeSwitchedAckRequest(element, "MODE-SWITCHED-ACK")
        assert result is not None
        assert result.getChecksum() is not None
        assert result.getChecksum().getValue() == "abc123"
        assert result.getTimestamp() is not None

    def test_read_via_mode_switch_sender_com_spec(self, parser):
        """Test that the ModeSwitchSenderComSpec aggregation reads modeSwitchedAck with field values."""
        element = _snip(
            "<MODE-SWITCHED-ACK><TIMEOUT>1.0</TIMEOUT></MODE-SWITCHED-ACK><QUEUE-LENGTH>5</QUEUE-LENGTH>",
            root_tag="MODE-SWITCH-SENDER-COM-SPEC",
        )
        com_spec = parser.getModeSwitchSenderComSpec(element)
        assert com_spec is not None
        ack = com_spec.getModeSwitchedAck()
        assert ack is not None
        assert ack.getTimeout() is not None
        assert ack.getTimeout().getValue() == 1.0
