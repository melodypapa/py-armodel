"""
Tests for writing DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT elements —
DiagnosticControlEnableMaskBit, Table 4.83 (p.119, R23-11).

DiagnosticControlEnableMaskBit (Base most-derived ARObject) carries two
attributes — bitNumber (0..1 PositiveInteger, BIT-NUMBER) and the 0..*
controlledDataElement ref collection (CONTROLLED-DATA-ELEMENT-REFS/
CONTROLLED-DATA-ELEMENT-REF, DEST DIAGNOSTIC-DATA-ELEMENT--SUBTYPES-ENUM) —
XSD group DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT, AUTOSAR_00052.xsd l.33900. Its
aggregator DiagnosticIOControl.controlEnableMaskBit (Table 4.80) writes the
bits into the CONTROL-ENABLE-MASK-BITS wrapper; the reusable
writeDiagnosticControlEnableMaskBit helper is verified directly here
(Rule 0001.7). The writer reads the model via the get* getters in XSD element
order.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_control_enable_mask_bit.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticControlEnableMaskBit
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _positive_integer(value: str) -> PositiveInteger:
    nrc_value = PositiveInteger()
    nrc_value.setValue(value)
    return nrc_value


class TestWriteDiagnosticControlEnableMaskBit:
    """Tests for writeDiagnosticControlEnableMaskBit — own element field values (Table 4.83)."""

    def _write(self, mask_bit: DiagnosticControlEnableMaskBit) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticControlEnableMaskBit(parent, mask_bit)
        return parent.find("DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT")

    def test_write_bit_number(self):
        """Test that the BIT-NUMBER is emitted as the PositiveInteger value."""
        mask_bit = DiagnosticControlEnableMaskBit()
        mask_bit.setBitNumber(_positive_integer("7"))

        child = self._write(mask_bit)
        number = child.find("BIT-NUMBER")
        assert number is not None
        assert number.text == "7"

    def test_write_controlled_data_element_refs(self):
        """Test that the CONTROLLED-DATA-ELEMENT-REFS collection is emitted with DEST attributes."""
        mask_bit = DiagnosticControlEnableMaskBit()
        mask_bit.addControlledDataElement(_ref("DIAGNOSTIC-DATA-ELEMENT", "/AUTOSAR/DiagnosticDataIdentifiers/DID1/DataElement1"))
        mask_bit.addControlledDataElement(_ref("DIAGNOSTIC-DATA-ELEMENT", "/AUTOSAR/DiagnosticDataIdentifiers/DID1/DataElement2"))

        child = self._write(mask_bit)
        refs_wrapper = child.find("CONTROLLED-DATA-ELEMENT-REFS")
        assert refs_wrapper is not None
        refs = refs_wrapper.findall("CONTROLLED-DATA-ELEMENT-REF")
        assert len(refs) == 2
        assert refs[0].text == "/AUTOSAR/DiagnosticDataIdentifiers/DID1/DataElement1"
        assert refs[0].get("DEST") == "DIAGNOSTIC-DATA-ELEMENT"
        assert refs[1].text == "/AUTOSAR/DiagnosticDataIdentifiers/DID1/DataElement2"

    def test_element_order_matches_xsd_sequence(self):
        """Test that the emitted children follow the XSD element order (BIT-NUMBER, CONTROLLED-DATA-ELEMENT-REFS)."""
        mask_bit = DiagnosticControlEnableMaskBit()
        mask_bit.setBitNumber(_positive_integer("7"))
        mask_bit.addControlledDataElement(_ref("DIAGNOSTIC-DATA-ELEMENT", "/AUTOSAR/DiagnosticDataIdentifiers/DID1/DataElement1"))

        child = self._write(mask_bit)
        assert [c.tag for c in child] == ["BIT-NUMBER", "CONTROLLED-DATA-ELEMENT-REFS"]

    def test_empty_mask_bit_omits_all_children(self):
        """Test that an empty mask bit emits no children."""
        mask_bit = DiagnosticControlEnableMaskBit()

        child = self._write(mask_bit)
        assert child is not None
        assert len(list(child)) == 0
