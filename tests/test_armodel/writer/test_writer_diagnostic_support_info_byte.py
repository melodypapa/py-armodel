"""
Tests for writing the SUPPORT-INFO-BYTE element — DiagnosticSupportInfoByte,
Table 4.129 (p.150, R23-11).

DiagnosticSupportInfoByte (Base = ARObject) is a nested container aggregated by
DiagnosticDataIdentifier.supportInfoByte and
DiagnosticParameterIdentifier.supportInfoByte; the writer emits SUPPORT-INFO-BYTE
only when the aggregation is set, with the POSITION and SIZE children, via the
named reusable helper writeDiagnosticSupportInfoByte called from
writeDiagnosticDataIdentifier and writeDiagnosticParameterIdentifier.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_support_info_byte.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticSupportInfoByte
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDataIdentifier, DiagnosticParameterIdentifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_support_info_byte() -> DiagnosticSupportInfoByte:
    support_info_byte = DiagnosticSupportInfoByte()
    support_info_byte.setPosition(PositiveInteger().setValue("1"))
    support_info_byte.setSize(PositiveInteger().setValue("2"))
    return support_info_byte


class TestWriteDiagnosticSupportInfoByte:
    """Tests for writeDiagnosticSupportInfoByte — own element field values (Table 4.129)."""

    def test_write_fields_in_xsd_order(self):
        """Test that POSITION and SIZE are emitted in XSD order with the spec values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticSupportInfoByte(parent, _make_support_info_byte())

        child = parent.find("SUPPORT-INFO-BYTE")
        assert child is not None
        assert [c.tag for c in child] == ["POSITION", "SIZE"]
        assert child.find("POSITION").text == "1"
        assert child.find("SIZE").text == "2"

    def test_write_unset_fields_emit_no_children(self):
        """Test that unset fields emit the empty SUPPORT-INFO-BYTE wrapper only."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticSupportInfoByte(parent, DiagnosticSupportInfoByte())

        child = parent.find("SUPPORT-INFO-BYTE")
        assert child is not None
        assert [c.tag for c in child] == []

    def test_data_identifier_dispatch_writes_support_info_byte(self):
        """Test that writeDiagnosticDataIdentifier emits SUPPORT-INFO-BYTE with the values."""
        did = DiagnosticDataIdentifier(parent=AUTOSAR.getInstance(), short_name="Di")
        did.setSupportInfoByte(_make_support_info_byte())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDataIdentifier(parent, did)

        child = parent.find("DIAGNOSTIC-DATA-IDENTIFIER")
        assert child.find("SUPPORT-INFO-BYTE/POSITION").text == "1"
        assert child.find("SUPPORT-INFO-BYTE/SIZE").text == "2"

    def test_parameter_identifier_dispatch_writes_support_info_byte(self):
        """Test that writeDiagnosticParameterIdentifier emits SUPPORT-INFO-BYTE with the values."""
        parameter_identifier = DiagnosticParameterIdentifier(AUTOSAR.getInstance(), "Pid1")
        parameter_identifier.setSupportInfoByte(_make_support_info_byte())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameterIdentifier(parent, parameter_identifier)

        child = parent.find("DIAGNOSTIC-PARAMETER-IDENTIFIER")
        assert child.find("SUPPORT-INFO-BYTE/POSITION").text == "1"
        assert child.find("SUPPORT-INFO-BYTE/SIZE").text == "2"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        did = DiagnosticDataIdentifier(parent=AUTOSAR.getInstance(), short_name="Di")
        did.setSupportInfoByte(_make_support_info_byte())

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticDataIdentifier(parent, did)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticDataIdentifier(parent=AUTOSAR.getInstance(), short_name="Di")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-DATA-IDENTIFIER")
        ARXMLParser().readDiagnosticDataIdentifier(element, reloaded)
        assert reloaded.getSupportInfoByte() is not None
        assert reloaded.getSupportInfoByte().getPosition() is not None
        assert reloaded.getSupportInfoByte().getPosition().getValue() == 1
        assert reloaded.getSupportInfoByte().getSize() is not None
        assert reloaded.getSupportInfoByte().getSize().getValue() == 2
