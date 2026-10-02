"""
Tests for reading the DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT element —
DiagnosticControlEnableMaskBit, Table 4.83 (p.119, R23-11).

DiagnosticControlEnableMaskBit (Base most-derived ARObject) carries two
attributes — bitNumber (0..1 PositiveInteger, BIT-NUMBER) and the 0..*
controlledDataElement ref collection (CONTROLLED-DATA-ELEMENT-REFS/
CONTROLLED-DATA-ELEMENT-REF, DEST DIAGNOSTIC-DATA-ELEMENT--SUBTYPES-ENUM) —
XSD group DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT, AUTOSAR_00052.xsd l.33900. Its
aggregator DiagnosticIOControl.controlEnableMaskBit (Table 4.80) reads the
bits via the CONTROL-ENABLE-MASK-BITS wrapper; the reusable
readDiagnosticControlEnableMaskBit helper is verified directly here
(Rule 0001.7).

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_control_enable_mask_bit.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticControlEnableMaskBit:
    """Tests for readDiagnosticControlEnableMaskBit — own element field values (Table 4.83)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticControlEnableMaskBit

        mask_bit = DiagnosticControlEnableMaskBit()
        element = _snip(inner, root_tag="DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT")
        parser.readDiagnosticControlEnableMaskBit(element, mask_bit)
        return mask_bit

    def test_read_bit_number(self, parser):
        """Test that the BIT-NUMBER is read as a PositiveInteger value."""
        mask_bit = self._read(parser, "<BIT-NUMBER>7</BIT-NUMBER>")
        assert mask_bit.getBitNumber() is not None
        assert mask_bit.getBitNumber().getValue() == 7

    def test_read_controlled_data_element_refs(self, parser):
        """Test that the CONTROLLED-DATA-ELEMENT-REFS collection is read with DEST attributes."""
        inner = (
            "<CONTROLLED-DATA-ELEMENT-REFS>"
            '<CONTROLLED-DATA-ELEMENT-REF DEST="DIAGNOSTIC-DATA-ELEMENT">/AUTOSAR/DiagnosticDataIdentifiers/DID1/DataElement1</CONTROLLED-DATA-ELEMENT-REF>'
            '<CONTROLLED-DATA-ELEMENT-REF DEST="DIAGNOSTIC-DATA-ELEMENT">/AUTOSAR/DiagnosticDataIdentifiers/DID1/DataElement2</CONTROLLED-DATA-ELEMENT-REF>'
            "</CONTROLLED-DATA-ELEMENT-REFS>"
        )
        mask_bit = self._read(parser, inner)
        refs = mask_bit.getControlledDataElements()
        assert len(refs) == 2
        assert refs[0].getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/DID1/DataElement1"
        assert refs[0].getDest() == "DIAGNOSTIC-DATA-ELEMENT"
        assert refs[1].getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/DID1/DataElement2"

    def test_empty_element_reads_nothing(self, parser):
        """Test that an empty element leaves bitNumber None and the ref collection empty."""
        mask_bit = self._read(parser, "")
        assert mask_bit.getBitNumber() is None
        assert mask_bit.getControlledDataElements() == []
