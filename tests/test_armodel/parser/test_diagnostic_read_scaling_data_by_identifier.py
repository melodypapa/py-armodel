"""
Tests for reading the DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER element —
DiagnosticReadScalingDataByIdentifier, Table 4.78 (p.116, R23-11).

DiagnosticReadScalingDataByIdentifier (Base most-derived
DiagnosticDataByIdentifier) owns one attribute: the 0..1 readScalingDataClass
ref (READ-SCALING-DATA-CLASS-REF, DEST
DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER--SUBTYPES-ENUM), AUTOSAR_00052.xsd
group DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER l.41518. It inherits the
0..1 dataIdentifier ref (DATA-IDENTIFIER-REF) from the abstract
DiagnosticDataByIdentifier (Table 4.73); the reader delegates the inherited
field to the Rule 0001.7 helper readDiagnosticDataByIdentifier. Per the XSD
complexType sequence (l.41543) the inherited DATA-IDENTIFIER-REF precedes the
own READ-SCALING-DATA-CLASS-REF.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_read_scaling_data_by_identifier.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticReadScalingDataByIdentifier:
    """Tests for readDiagnosticReadScalingDataByIdentifier — own element field values (Table 4.78)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticReadScalingDataByIdentifier

        read_scaling_data_by_identifier = DiagnosticReadScalingDataByIdentifier(parent=MagicMock(), short_name="ReadScalingDataByIdentifier")
        element = _snip(inner, root_tag="DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER")
        parser.readDiagnosticReadScalingDataByIdentifier(element, read_scaling_data_by_identifier)
        return read_scaling_data_by_identifier

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        read_scaling_data_by_identifier = self._read(parser, "<SHORT-NAME>ReadScalingDataByIdentifier</SHORT-NAME>")
        assert read_scaling_data_by_identifier.getShortName() == "ReadScalingDataByIdentifier"

    def test_read_read_scaling_data_class_ref(self, parser):
        """Test that the READ-SCALING-DATA-CLASS-REF is read with its DEST attribute."""
        read_scaling_data_by_identifier = self._read(
            parser,
            '<READ-SCALING-DATA-CLASS-REF DEST="DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS">/AUTOSAR/DiagnosticReadScalingDataByIdentifierClasses/ReadScalingClass</READ-SCALING-DATA-CLASS-REF>',
        )
        ref = read_scaling_data_by_identifier.getReadScalingDataClass()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticReadScalingDataByIdentifierClasses/ReadScalingClass"
        assert ref.getDest() == "DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS"

    def test_read_inherited_data_identifier_ref(self, parser):
        """Test that the inherited DATA-IDENTIFIER-REF is read via the base helper."""
        read_scaling_data_by_identifier = self._read(parser, '<DATA-IDENTIFIER-REF DEST="DIAGNOSTIC-DATA-IDENTIFIER">/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID</DATA-IDENTIFIER-REF>')
        ref = read_scaling_data_by_identifier.getDataIdentifier()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"
        assert ref.getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving both refs unset."""
        read_scaling_data_by_identifier = self._read(parser, "<SHORT-NAME>ReadScalingDataByIdentifier</SHORT-NAME>")
        assert read_scaling_data_by_identifier.getDataIdentifier() is None
        assert read_scaling_data_by_identifier.getReadScalingDataClass() is None
