"""
Tests for reading the DIAGNOSTIC-IO-CONTROL element —
DiagnosticIOControl, Table 4.80 (p.118, R23-11).

DiagnosticIOControl (Base most-derived ARElement, aggregated by
ARPackage.element) owns six attributes in XSD group DIAGNOSTIC-IO-CONTROL,
AUTOSAR_00052.xsd l.38426: the 0..* controlEnableMaskBit aggregation
(CONTROL-ENABLE-MASK-BITS wrapper of DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT
elements), the 0..1 dataIdentifier ref (DATA-IDENTIFIER-REF, DEST
DIAGNOSTIC-DATA-IDENTIFIER--SUBTYPES-ENUM), freezeCurrentState and
resetToDefault / shortTermAdjustment (BOOLEAN) and the 0..1 ioControlClass
ref (IO-CONTROL-CLASS-REF, DEST DIAGNOSTIC-IO-CONTROL-CLASS--SUBTYPES-ENUM).
The reader populates the fields via the model mutators in XSD element order.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_io_control.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticIOControl:
    """Tests for readDiagnosticIOControl — own element field values (Table 4.80)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticIOControl

        io_control = DiagnosticIOControl(parent=MagicMock(), short_name="IOControl")
        element = _snip(inner, root_tag="DIAGNOSTIC-IO-CONTROL")
        parser.readDiagnosticIOControl(element, io_control)
        return io_control

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        io_control = self._read(parser, "<SHORT-NAME>IOControl</SHORT-NAME>")
        assert io_control.getShortName() == "IOControl"

    def test_read_control_enable_mask_bits(self, parser):
        """Test that the CONTROL-ENABLE-MASK-BITS wrapper is read into the aggregation list."""
        inner = (
            "<CONTROL-ENABLE-MASK-BITS>"
            "<DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT>"
            "<BIT-NUMBER>7</BIT-NUMBER>"
            "<CONTROLLED-DATA-ELEMENT-REFS>"
            '<CONTROLLED-DATA-ELEMENT-REF DEST="DIAGNOSTIC-DATA-ELEMENT">/AUTOSAR/DiagnosticDataIdentifiers/DID1/DataElement1</CONTROLLED-DATA-ELEMENT-REF>'
            "</CONTROLLED-DATA-ELEMENT-REFS>"
            "</DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT>"
            "<DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT>"
            "<BIT-NUMBER>3</BIT-NUMBER>"
            "</DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT>"
            "</CONTROL-ENABLE-MASK-BITS>"
        )
        io_control = self._read(parser, inner)
        mask_bits = io_control.getControlEnableMaskBits()
        assert len(mask_bits) == 2
        assert mask_bits[0].getBitNumber().getValue() == 7
        assert mask_bits[0].getControlledDataElements()[0].getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/DID1/DataElement1"
        assert mask_bits[1].getBitNumber().getValue() == 3

    def test_read_data_identifier_ref(self, parser):
        """Test that the DATA-IDENTIFIER-REF is read with its DEST attribute."""
        io_control = self._read(parser, '<DATA-IDENTIFIER-REF DEST="DIAGNOSTIC-DATA-IDENTIFIER">/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID</DATA-IDENTIFIER-REF>')
        ref = io_control.getDataIdentifier()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"
        assert ref.getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"

    def test_read_freeze_current_state(self, parser):
        """Test that the FREEZE-CURRENT-STATE boolean is read."""
        io_control = self._read(parser, "<FREEZE-CURRENT-STATE>true</FREEZE-CURRENT-STATE>")
        assert io_control.getFreezeCurrentState() is not None
        assert io_control.getFreezeCurrentState().getValue() is True

    def test_read_io_control_class_ref(self, parser):
        """Test that the IO-CONTROL-CLASS-REF is read with its DEST attribute."""
        io_control = self._read(parser, '<IO-CONTROL-CLASS-REF DEST="DIAGNOSTIC-IO-CONTROL-CLASS">/AUTOSAR/DiagnosticIoControlClasses/IoControlClass</IO-CONTROL-CLASS-REF>')
        ref = io_control.getIoControlClass()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticIoControlClasses/IoControlClass"
        assert ref.getDest() == "DIAGNOSTIC-IO-CONTROL-CLASS"

    def test_read_reset_to_default(self, parser):
        """Test that the RESET-TO-DEFAULT boolean is read."""
        io_control = self._read(parser, "<RESET-TO-DEFAULT>true</RESET-TO-DEFAULT>")
        assert io_control.getResetToDefault() is not None
        assert io_control.getResetToDefault().getValue() is True

    def test_read_short_term_adjustment(self, parser):
        """Test that the SHORT-TERM-ADJUSTMENT boolean is read."""
        io_control = self._read(parser, "<SHORT-TERM-ADJUSTMENT>true</SHORT-TERM-ADJUSTMENT>")
        assert io_control.getShortTermAdjustment() is not None
        assert io_control.getShortTermAdjustment().getValue() is True

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving all attributes unset."""
        io_control = self._read(parser, "<SHORT-NAME>IOControl</SHORT-NAME>")
        assert io_control.getControlEnableMaskBits() == []
        assert io_control.getDataIdentifier() is None
        assert io_control.getFreezeCurrentState() is None
        assert io_control.getIoControlClass() is None
        assert io_control.getResetToDefault() is None
        assert io_control.getShortTermAdjustment() is None
