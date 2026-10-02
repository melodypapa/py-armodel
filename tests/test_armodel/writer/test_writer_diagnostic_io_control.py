"""
Tests for writing DIAGNOSTIC-IO-CONTROL elements —
DiagnosticIOControl, Table 4.80 (p.118, R23-11).

DiagnosticIOControl (Base most-derived ARElement, aggregated by
ARPackage.element) owns six attributes in XSD group DIAGNOSTIC-IO-CONTROL,
AUTOSAR_00052.xsd l.38426: the 0..* controlEnableMaskBit aggregation
(CONTROL-ENABLE-MASK-BITS wrapper of DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT
elements), the 0..1 dataIdentifier ref (DATA-IDENTIFIER-REF, DEST
DIAGNOSTIC-DATA-IDENTIFIER--SUBTYPES-ENUM), freezeCurrentState and
resetToDefault / shortTermAdjustment (BOOLEAN) and the 0..1 ioControlClass
ref (IO-CONTROL-CLASS-REF, DEST DIAGNOSTIC-IO-CONTROL-CLASS--SUBTYPES-ENUM).
The writer reads the model via the get* getters in XSD element order. The
dispatch entry is writeARPackageElement → writeDiagnosticIOControl.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_io_control.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticControlEnableMaskBit
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticIOControl
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _boolean(value: str) -> Boolean:
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _positive_integer(value: str) -> PositiveInteger:
    nrc_value = PositiveInteger()
    nrc_value.setValue(value)
    return nrc_value


class TestWriteDiagnosticIOControl:
    """Tests for writeDiagnosticIOControl — own element field values (Table 4.80)."""

    def _write(self, io_control: DiagnosticIOControl) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticIOControl(parent, io_control)
        return parent.find("DIAGNOSTIC-IO-CONTROL")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticIOControl without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIoControls")
        package.createDiagnosticIOControl("IOControl1")

        child = self._write(package.getReferrableElement("IOControl1", DiagnosticIOControl))
        assert child is not None
        assert child.find("SHORT-NAME").text == "IOControl1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_control_enable_mask_bits(self):
        """Test that the CONTROL-ENABLE-MASK-BITS wrapper is emitted with the nested mask bits."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIoControls")
        io_control = package.createDiagnosticIOControl("IOControl1")
        mask_bit = DiagnosticControlEnableMaskBit()
        mask_bit.setBitNumber(_positive_integer("7"))
        io_control.addControlEnableMaskBit(mask_bit)

        child = self._write(io_control)
        wrapper = child.find("CONTROL-ENABLE-MASK-BITS")
        assert wrapper is not None
        nested_bit = wrapper.findall("DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT")[0]
        assert nested_bit.find("BIT-NUMBER").text == "7"

    def test_write_data_identifier_ref(self):
        """Test that the DATA-IDENTIFIER-REF is emitted with its DEST attribute."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIoControls")
        io_control = package.createDiagnosticIOControl("IOControl1")
        io_control.setDataIdentifier(_ref("DIAGNOSTIC-DATA-IDENTIFIER", "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"))

        child = self._write(io_control)
        ref = child.find("DATA-IDENTIFIER-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"
        assert ref.get("DEST") == "DIAGNOSTIC-DATA-IDENTIFIER"

    def test_write_freeze_current_state(self):
        """Test that the FREEZE-CURRENT-STATE boolean is emitted."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIoControls")
        io_control = package.createDiagnosticIOControl("IOControl1")
        io_control.setFreezeCurrentState(_boolean("true"))

        child = self._write(io_control)
        flag = child.find("FREEZE-CURRENT-STATE")
        assert flag is not None
        assert flag.text == "true"

    def test_write_io_control_class_ref(self):
        """Test that the IO-CONTROL-CLASS-REF is emitted with its DEST attribute."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIoControls")
        io_control = package.createDiagnosticIOControl("IOControl1")
        io_control.setIoControlClass(_ref("DIAGNOSTIC-IO-CONTROL-CLASS", "/AUTOSAR/DiagnosticIoControlClasses/IoControlClass"))

        child = self._write(io_control)
        ref = child.find("IO-CONTROL-CLASS-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticIoControlClasses/IoControlClass"
        assert ref.get("DEST") == "DIAGNOSTIC-IO-CONTROL-CLASS"

    def test_write_reset_to_default(self):
        """Test that the RESET-TO-DEFAULT boolean is emitted."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIoControls")
        io_control = package.createDiagnosticIOControl("IOControl1")
        io_control.setResetToDefault(_boolean("true"))

        child = self._write(io_control)
        flag = child.find("RESET-TO-DEFAULT")
        assert flag is not None
        assert flag.text == "true"

    def test_write_short_term_adjustment(self):
        """Test that the SHORT-TERM-ADJUSTMENT boolean is emitted."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIoControls")
        io_control = package.createDiagnosticIOControl("IOControl1")
        io_control.setShortTermAdjustment(_boolean("true"))

        child = self._write(io_control)
        flag = child.find("SHORT-TERM-ADJUSTMENT")
        assert flag is not None
        assert flag.text == "true"

    def test_write_element_order_matches_xsd_sequence(self):
        """Test that the emitted children follow the XSD element order (l.38426)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIoControls")
        io_control = package.createDiagnosticIOControl("IOControl1")
        io_control.addControlEnableMaskBit(DiagnosticControlEnableMaskBit())
        io_control.setDataIdentifier(_ref("DIAGNOSTIC-DATA-IDENTIFIER", "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"))
        io_control.setFreezeCurrentState(_boolean("true"))
        io_control.setIoControlClass(_ref("DIAGNOSTIC-IO-CONTROL-CLASS", "/AUTOSAR/DiagnosticIoControlClasses/IoControlClass"))
        io_control.setResetToDefault(_boolean("true"))
        io_control.setShortTermAdjustment(_boolean("true"))

        child = self._write(io_control)
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == [
            "CONTROL-ENABLE-MASK-BITS",
            "DATA-IDENTIFIER-REF",
            "FREEZE-CURRENT-STATE",
            "IO-CONTROL-CLASS-REF",
            "RESET-TO-DEFAULT",
            "SHORT-TERM-ADJUSTMENT",
        ]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticIOControl to a DIAGNOSTIC-IO-CONTROL element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIoControls")
        package.createDiagnosticIOControl("IOControl1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("IOControl1", DiagnosticIOControl))

        child = parent.find("DIAGNOSTIC-IO-CONTROL")
        assert child is not None
        assert child.find("SHORT-NAME").text == "IOControl1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticIoControls")
        io_control = package.createDiagnosticIOControl("IOControl1")
        mask_bit = DiagnosticControlEnableMaskBit()
        mask_bit.setBitNumber(_positive_integer("7"))
        mask_bit.addControlledDataElement(_ref("DIAGNOSTIC-DATA-ELEMENT", "/AUTOSAR/DiagnosticDataIdentifiers/DID1/DataElement1"))
        io_control.addControlEnableMaskBit(mask_bit)
        io_control.setDataIdentifier(_ref("DIAGNOSTIC-DATA-IDENTIFIER", "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"))
        io_control.setFreezeCurrentState(_boolean("true"))
        io_control.setIoControlClass(_ref("DIAGNOSTIC-IO-CONTROL-CLASS", "/AUTOSAR/DiagnosticIoControlClasses/IoControlClass"))
        io_control.setResetToDefault(_boolean("true"))
        io_control.setShortTermAdjustment(_boolean("true"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            io_control_2 = package_2.getReferrableElement("IOControl1", DiagnosticIOControl)
            assert io_control_2 is not None
            assert io_control_2.getShortName() == "IOControl1"
            mask_bits_2 = io_control_2.getControlEnableMaskBits()
            assert len(mask_bits_2) == 1
            assert mask_bits_2[0].getBitNumber().getValue() == 7
            assert mask_bits_2[0].getControlledDataElements()[0].getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/DID1/DataElement1"
            data_identifier = io_control_2.getDataIdentifier()
            assert data_identifier is not None
            assert data_identifier.getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"
            assert data_identifier.getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"
            assert io_control_2.getFreezeCurrentState().getValue() is True
            io_control_class = io_control_2.getIoControlClass()
            assert io_control_class is not None
            assert io_control_class.getValue() == "/AUTOSAR/DiagnosticIoControlClasses/IoControlClass"
            assert io_control_class.getDest() == "DIAGNOSTIC-IO-CONTROL-CLASS"
            assert io_control_2.getResetToDefault().getValue() is True
            assert io_control_2.getShortTermAdjustment().getValue() is True
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
