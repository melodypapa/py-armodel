"""
Tests for reading the DIAGNOSTIC-ECU-RESET element —
DiagnosticEcuReset, Table 4.60 (p.102, R23-11).

DiagnosticEcuReset (Base most-derived ARElement, concrete) defines two 0..1
attributes: customSubFunctionNumber (PositiveInteger, CUSTOM-SUB-FUNCTION-NUMBER)
and the ecuResetClass ref (RefType, ECU-RESET-CLASS-REF, DEST
DIAGNOSTIC-ECU-RESET-CLASS) — AUTOSAR_00052.xsd group DIAGNOSTIC-ECU-RESET
l.35369 / complexType l.35406. The inherited DIAGNOSTIC-COMMON-ELEMENT and
DIAGNOSTIC-SERVICE-INSTANCE groups are empty sequences in the XSD, so the
reader delegates only to readIdentifiable. The RESPOND-TO-RESET element in the
XSD group carries atp.Status="removed" and is not a Table 4.60 attribute row.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_ecu_reset.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticEcuReset:
    """Tests for readDiagnosticEcuReset — own element field values (Table 4.60)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEcuReset

        ecu_reset = DiagnosticEcuReset(parent=MagicMock(), short_name="EcuReset")
        element = _snip(inner, root_tag="DIAGNOSTIC-ECU-RESET")
        parser.readDiagnosticEcuReset(element, ecu_reset)
        return ecu_reset

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        ecu_reset = self._read(parser, "<SHORT-NAME>EcuReset</SHORT-NAME>")
        assert ecu_reset.getShortName() == "EcuReset"

    def test_read_custom_sub_function_number(self, parser):
        """Test that CUSTOM-SUB-FUNCTION-NUMBER is read with the field value."""
        ecu_reset = self._read(parser, "<CUSTOM-SUB-FUNCTION-NUMBER>5</CUSTOM-SUB-FUNCTION-NUMBER>")
        assert ecu_reset.getCustomSubFunctionNumber() is not None
        assert ecu_reset.getCustomSubFunctionNumber().getValue() == 5

    def test_read_ecu_reset_class_ref(self, parser):
        """Test that the ECU-RESET-CLASS-REF is read with field values."""
        ecu_reset = self._read(parser, '<ECU-RESET-CLASS-REF DEST="DIAGNOSTIC-ECU-RESET-CLASS">/AUTOSAR/DiagnosticEcuResetClasses/ResetClass</ECU-RESET-CLASS-REF>')
        ref = ecu_reset.getEcuResetClass()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticEcuResetClasses/ResetClass"
        assert ref.getDest() == "DIAGNOSTIC-ECU-RESET-CLASS"

    def test_read_both_fields(self, parser):
        """Test that both attributes are read in XSD order (CUSTOM-SUB-FUNCTION-NUMBER before ECU-RESET-CLASS-REF)."""
        ecu_reset = self._read(parser, '<CUSTOM-SUB-FUNCTION-NUMBER>7</CUSTOM-SUB-FUNCTION-NUMBER><ECU-RESET-CLASS-REF DEST="DIAGNOSTIC-ECU-RESET-CLASS">/Diag/ResetClass</ECU-RESET-CLASS-REF>')
        assert ecu_reset.getCustomSubFunctionNumber().getValue() == 7
        assert ecu_reset.getEcuResetClass().getValue() == "/Diag/ResetClass"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving both attributes unset."""
        ecu_reset = self._read(parser, "")
        assert ecu_reset.getShortName() == "EcuReset"
        assert ecu_reset.getCustomSubFunctionNumber() is None
        assert ecu_reset.getEcuResetClass() is None
