"""
Tests for reading the DIAGNOSTIC-READ-DATA-BY-IDENTIFIER element —
DiagnosticReadDataByIdentifier, Table 4.70 (p.112, R23-11).

DiagnosticReadDataByIdentifier (Base most-derived DiagnosticDataByIdentifier)
owns one attribute: the 0..1 readClass ref (READ-CLASS-REF, DEST
DIAGNOSTIC-READ-DATA-BY-IDENTIFIER--SUBTYPES-ENUM), AUTOSAR_00052.xsd group
DIAGNOSTIC-READ-DATA-BY-IDENTIFIER l.41139. It inherits the 0..1
dataIdentifier ref (DATA-IDENTIFIER-REF) from the abstract
DiagnosticDataByIdentifier (Table 4.73); the reader delegates the inherited
field to the Rule 0001.7 helper readDiagnosticDataByIdentifier. Per the XSD
complexType sequence (l.41164) the inherited DATA-IDENTIFIER-REF precedes the
own READ-CLASS-REF.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_read_data_by_identifier.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticReadDataByIdentifier:
    """Tests for readDiagnosticReadDataByIdentifier — own element field values (Table 4.70)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticReadDataByIdentifier

        read_data_by_identifier = DiagnosticReadDataByIdentifier(parent=MagicMock(), short_name="ReadDataByIdentifier")
        element = _snip(inner, root_tag="DIAGNOSTIC-READ-DATA-BY-IDENTIFIER")
        parser.readDiagnosticReadDataByIdentifier(element, read_data_by_identifier)
        return read_data_by_identifier

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        read_data_by_identifier = self._read(parser, "<SHORT-NAME>ReadDataByIdentifier</SHORT-NAME>")
        assert read_data_by_identifier.getShortName() == "ReadDataByIdentifier"

    def test_read_read_class_ref(self, parser):
        """Test that the READ-CLASS-REF is read with its DEST attribute."""
        read_data_by_identifier = self._read(parser, '<READ-CLASS-REF DEST="DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS">/AUTOSAR/DiagnosticReadDataByIdentifierClasses/ReadClass</READ-CLASS-REF>')
        ref = read_data_by_identifier.getReadClass()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticReadDataByIdentifierClasses/ReadClass"
        assert ref.getDest() == "DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS"

    def test_read_inherited_data_identifier_ref(self, parser):
        """Test that the inherited DATA-IDENTIFIER-REF is read via the base helper."""
        read_data_by_identifier = self._read(parser, '<DATA-IDENTIFIER-REF DEST="DIAGNOSTIC-DATA-IDENTIFIER">/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID</DATA-IDENTIFIER-REF>')
        ref = read_data_by_identifier.getDataIdentifier()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"
        assert ref.getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving both refs unset."""
        read_data_by_identifier = self._read(parser, "<SHORT-NAME>ReadDataByIdentifier</SHORT-NAME>")
        assert read_data_by_identifier.getDataIdentifier() is None
        assert read_data_by_identifier.getReadClass() is None
