"""
Tests for reading the DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER element —
DiagnosticWriteDataByIdentifier, Table 4.71 (p.113, R23-11).

DiagnosticWriteDataByIdentifier (Base most-derived DiagnosticDataByIdentifier)
owns one attribute: the 0..1 writeClass ref (WRITE-CLASS-REF, DEST
DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER--SUBTYPES-ENUM), AUTOSAR_00052.xsd group
DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER l.47169. It inherits the 0..1
dataIdentifier ref (DATA-IDENTIFIER-REF) from the abstract
DiagnosticDataByIdentifier (Table 4.73); the reader delegates the inherited
field to the Rule 0001.7 helper readDiagnosticDataByIdentifier. Per the XSD
complexType sequence (l.47194) the inherited DATA-IDENTIFIER-REF precedes the
own WRITE-CLASS-REF.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_write_data_by_identifier.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticWriteDataByIdentifier:
    """Tests for readDiagnosticWriteDataByIdentifier — own element field values (Table 4.71)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticWriteDataByIdentifier

        write_data_by_identifier = DiagnosticWriteDataByIdentifier(parent=MagicMock(), short_name="WriteDataByIdentifier")
        element = _snip(inner, root_tag="DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER")
        parser.readDiagnosticWriteDataByIdentifier(element, write_data_by_identifier)
        return write_data_by_identifier

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        write_data_by_identifier = self._read(parser, "<SHORT-NAME>WriteDataByIdentifier</SHORT-NAME>")
        assert write_data_by_identifier.getShortName() == "WriteDataByIdentifier"

    def test_read_write_class_ref(self, parser):
        """Test that the WRITE-CLASS-REF is read with its DEST attribute."""
        write_data_by_identifier = self._read(parser, '<WRITE-CLASS-REF DEST="DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS">/AUTOSAR/DiagnosticWriteDataByIdentifierClasses/WriteClass</WRITE-CLASS-REF>')
        ref = write_data_by_identifier.getWriteClass()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticWriteDataByIdentifierClasses/WriteClass"
        assert ref.getDest() == "DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS"

    def test_read_inherited_data_identifier_ref(self, parser):
        """Test that the inherited DATA-IDENTIFIER-REF is read via the base helper."""
        write_data_by_identifier = self._read(parser, '<DATA-IDENTIFIER-REF DEST="DIAGNOSTIC-DATA-IDENTIFIER">/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID</DATA-IDENTIFIER-REF>')
        ref = write_data_by_identifier.getDataIdentifier()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"
        assert ref.getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving both refs unset."""
        write_data_by_identifier = self._read(parser, "<SHORT-NAME>WriteDataByIdentifier</SHORT-NAME>")
        assert write_data_by_identifier.getDataIdentifier() is None
        assert write_data_by_identifier.getWriteClass() is None
