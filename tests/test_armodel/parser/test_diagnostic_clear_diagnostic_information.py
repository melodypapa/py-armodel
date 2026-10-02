"""
Tests for reading the DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION element —
DiagnosticClearDiagnosticInformation, Table 4.108 (p.137, R23-11).

DiagnosticClearDiagnosticInformation (Base most-derived ARElement, aggregated
by ARPackage.element) owns a single attribute in XSD group
DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION, AUTOSAR_00052.xsd l.32349: the 0..1
clearDiagnosticInformationClass ref (CLEAR-DIAGNOSTIC-INFORMATION-CLASS-REF,
DEST DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS--SUBTYPES-ENUM). The reader
populates the field via the model mutator in XSD element order.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_clear_diagnostic_information.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticClearDiagnosticInformation:
    """Tests for readDiagnosticClearDiagnosticInformation — own element field values (Table 4.108)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticClearDiagnosticInformation

        clear_diagnostic_information = DiagnosticClearDiagnosticInformation(parent=MagicMock(), short_name="ClearDiagnosticInformation")
        element = _snip(inner, root_tag="DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION")
        parser.readDiagnosticClearDiagnosticInformation(element, clear_diagnostic_information)
        return clear_diagnostic_information

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        clear_diagnostic_information = self._read(parser, "<SHORT-NAME>ClearDiagnosticInformation</SHORT-NAME>")
        assert clear_diagnostic_information.getShortName() == "ClearDiagnosticInformation"

    def test_read_clear_diagnostic_information_class_ref(self, parser):
        """Test that the CLEAR-DIAGNOSTIC-INFORMATION-CLASS-REF is read with its DEST attribute."""
        inner = '<CLEAR-DIAGNOSTIC-INFORMATION-CLASS-REF DEST="DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS">/AUTOSAR/DiagnosticClearDiagnosticInformations/ClearDiagnosticInformationClass</CLEAR-DIAGNOSTIC-INFORMATION-CLASS-REF>'
        clear_diagnostic_information = self._read(parser, inner)
        ref = clear_diagnostic_information.getClearDiagnosticInformationClass()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticClearDiagnosticInformations/ClearDiagnosticInformationClass"
        assert ref.getDest() == "DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the attribute unset."""
        clear_diagnostic_information = self._read(parser, "<SHORT-NAME>ClearDiagnosticInformation</SHORT-NAME>")
        assert clear_diagnostic_information.getClearDiagnosticInformationClass() is None
