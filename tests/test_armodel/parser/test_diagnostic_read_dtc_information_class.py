"""
Tests for reading the DIAGNOSTIC-READ-DTC-INFORMATION-CLASS element —
DiagnosticReadDTCInformationClass, Table 4.107 (p.136, R23-11).

DiagnosticReadDTCInformationClass (Base most-derived DiagnosticServiceClass,
concrete) defines no own attributes — the R23-11 table's attribute row is `-`
and XSD group DIAGNOSTIC-READ-DTC-INFORMATION-CLASS, AUTOSAR_00052.xsd
l.41397, is an empty sequence. Only the IDENTIFIABLE wrapper is read. The
dispatch entry is readARPackageElements → readDiagnosticReadDTCInformationClass
via the ARPackage create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_read_dtc_information_class.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticReadDTCInformationClass:
    """Tests for readDiagnosticReadDTCInformationClass — own element field values (Table 4.107)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticReadDTCInformationClass

        read_dtc_information_class = DiagnosticReadDTCInformationClass(parent=parser, short_name="Rdtci")
        element = _snip(inner, root_tag="DIAGNOSTIC-READ-DTC-INFORMATION-CLASS")
        parser.readDiagnosticReadDTCInformationClass(element, read_dtc_information_class)
        return read_dtc_information_class

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        read_dtc_information_class = self._read(parser, "<SHORT-NAME>Rdtci</SHORT-NAME>")
        assert read_dtc_information_class.getShortName() == "Rdtci"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element unnamed but valid."""
        read_dtc_information_class = self._read(parser, "")
        assert read_dtc_information_class.getShortName() == "Rdtci"
