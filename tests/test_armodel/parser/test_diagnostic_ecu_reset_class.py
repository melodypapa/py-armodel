"""
Tests for reading the DIAGNOSTIC-ECU-RESET-CLASS element —
DiagnosticEcuResetClass, Table 4.61 (p.102, R23-11).

DiagnosticEcuResetClass (Base most-derived DiagnosticServiceClass, concrete)
defines one 0..1 attribute: respondToReset (DiagnosticResponseToEcuResetEnum,
RESPOND-TO-RESET) — AUTOSAR_00052.xsd group DIAGNOSTIC-ECU-RESET-CLASS
l.35423 / complexType l.35442. The element text is one of the
AR:DIAGNOSTIC-RESPONSE-TO-ECU-RESET-ENUM--SIMPLE tokens (RESPOND-AFTER-RESET,
RESPOND-BEFORE-RESET) and is mapped via DIAGNOSTIC_RESPONSE_TO_ECU_RESET_XML_MAP.
The RESPOND-TO-RESET field-value read tests land with the
DiagnosticResponseToEcuResetEnum sync (enum literals), which extends this file.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_ecu_reset_class.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticEcuResetClass:
    """Tests for readDiagnosticEcuResetClass — own element field values (Table 4.61)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticEcuResetClass

        ecu_reset_class = DiagnosticEcuResetClass(parent=MagicMock(), short_name="EcuResetClass")
        element = _snip(inner, root_tag="DIAGNOSTIC-ECU-RESET-CLASS")
        parser.readDiagnosticEcuResetClass(element, ecu_reset_class)
        return ecu_reset_class

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        ecu_reset_class = self._read(parser, "<SHORT-NAME>EcuResetClass</SHORT-NAME>")
        assert ecu_reset_class.getShortName() == "EcuResetClass"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving respondToReset unset."""
        ecu_reset_class = self._read(parser, "")
        assert ecu_reset_class.getShortName() == "EcuResetClass"
        assert ecu_reset_class.getRespondToReset() is None
