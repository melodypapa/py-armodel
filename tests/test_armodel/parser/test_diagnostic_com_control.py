"""
Tests for reading the DIAGNOSTIC-COM-CONTROL element —
DiagnosticComControl, Table 4.64 (p.108, R23-11).

DiagnosticComControl (Base most-derived ARElement, concrete) defines two 0..1
attributes: the comControlClass ref (RefType, COM-CONTROL-CLASS-REF, DEST
DIAGNOSTIC-COM-CONTROL-CLASS) and customSubFunctionNumber (PositiveInteger,
CUSTOM-SUB-FUNCTION-NUMBER) — AUTOSAR_00052.xsd group DIAGNOSTIC-COM-CONTROL
l.32515 / complexType l.32546. The inherited DIAGNOSTIC-COMMON-ELEMENT and
DIAGNOSTIC-SERVICE-INSTANCE groups are empty sequences in the XSD, so the
reader delegates only to readIdentifiable.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_com_control.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticComControl:
    """Tests for readDiagnosticComControl — own element field values (Table 4.64)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticComControl

        com_control = DiagnosticComControl(parent=MagicMock(), short_name="ComControl")
        element = _snip(inner, root_tag="DIAGNOSTIC-COM-CONTROL")
        parser.readDiagnosticComControl(element, com_control)
        return com_control

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        com_control = self._read(parser, "<SHORT-NAME>ComControl</SHORT-NAME>")
        assert com_control.getShortName() == "ComControl"

    def test_read_com_control_class_ref(self, parser):
        """Test that the COM-CONTROL-CLASS-REF is read with field values."""
        com_control = self._read(parser, '<COM-CONTROL-CLASS-REF DEST="DIAGNOSTIC-COM-CONTROL-CLASS">/AUTOSAR/DiagnosticCommunicationControls/ComControlClass</COM-CONTROL-CLASS-REF>')
        ref = com_control.getComControlClass()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticCommunicationControls/ComControlClass"
        assert ref.getDest() == "DIAGNOSTIC-COM-CONTROL-CLASS"

    def test_read_custom_sub_function_number(self, parser):
        """Test that CUSTOM-SUB-FUNCTION-NUMBER is read with the field value."""
        com_control = self._read(parser, "<CUSTOM-SUB-FUNCTION-NUMBER>5</CUSTOM-SUB-FUNCTION-NUMBER>")
        assert com_control.getCustomSubFunctionNumber() is not None
        assert com_control.getCustomSubFunctionNumber().getValue() == 5

    def test_read_both_fields(self, parser):
        """Test that both attributes are read in XSD order (COM-CONTROL-CLASS-REF before CUSTOM-SUB-FUNCTION-NUMBER)."""
        com_control = self._read(
            parser, '<COM-CONTROL-CLASS-REF DEST="DIAGNOSTIC-COM-CONTROL-CLASS">/Diag/ComControlClass</COM-CONTROL-CLASS-REF><CUSTOM-SUB-FUNCTION-NUMBER>7</CUSTOM-SUB-FUNCTION-NUMBER>'
        )
        assert com_control.getComControlClass().getValue() == "/Diag/ComControlClass"
        assert com_control.getCustomSubFunctionNumber().getValue() == 7

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving both attributes unset."""
        com_control = self._read(parser, "")
        assert com_control.getShortName() == "ComControl"
        assert com_control.getComControlClass() is None
        assert com_control.getCustomSubFunctionNumber() is None
