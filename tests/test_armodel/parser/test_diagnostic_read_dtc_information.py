"""
Tests for reading the DIAGNOSTIC-READ-DTC-INFORMATION element —
DiagnosticReadDTCInformation, Table 4.106 (p.136, R23-11).

DiagnosticReadDTCInformation (Base most-derived ARElement, aggregated by
ARPackage.element) owns a single attribute in XSD group
DIAGNOSTIC-READ-DTC-INFORMATION, AUTOSAR_00052.xsd l.41350: the 0..1
readDTCInformationClass ref (READ-DTC-INFORMATION-CLASS-REF, DEST
DIAGNOSTIC-READ-DTC-INFORMATION-CLASS--SUBTYPES-ENUM). The reader populates
the field via the model mutator in XSD element order.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_read_dtc_information.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticReadDTCInformation:
    """Tests for readDiagnosticReadDTCInformation — own element field values (Table 4.106)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticReadDTCInformation

        read_dtc_information = DiagnosticReadDTCInformation(parent=MagicMock(), short_name="ReadDTCInformation")
        element = _snip(inner, root_tag="DIAGNOSTIC-READ-DTC-INFORMATION")
        parser.readDiagnosticReadDTCInformation(element, read_dtc_information)
        return read_dtc_information

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        read_dtc_information = self._read(parser, "<SHORT-NAME>ReadDTCInformation</SHORT-NAME>")
        assert read_dtc_information.getShortName() == "ReadDTCInformation"

    def test_read_read_dtc_information_class_ref(self, parser):
        """Test that the READ-DTC-INFORMATION-CLASS-REF is read with its DEST attribute."""
        inner = '<READ-DTC-INFORMATION-CLASS-REF DEST="DIAGNOSTIC-READ-DTC-INFORMATION-CLASS">/AUTOSAR/DiagnosticReadDtcInformations/ReadDTCInformationClass</READ-DTC-INFORMATION-CLASS-REF>'
        read_dtc_information = self._read(parser, inner)
        ref = read_dtc_information.getReadDTCInformationClass()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticReadDtcInformations/ReadDTCInformationClass"
        assert ref.getDest() == "DIAGNOSTIC-READ-DTC-INFORMATION-CLASS"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the attribute unset."""
        read_dtc_information = self._read(parser, "<SHORT-NAME>ReadDTCInformation</SHORT-NAME>")
        assert read_dtc_information.getReadDTCInformationClass() is None
