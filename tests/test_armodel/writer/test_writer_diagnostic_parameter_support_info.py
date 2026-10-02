"""
Tests for writing the SUPPORT-INFO element — DiagnosticParameterSupportInfo,
Table 4.128 (p.149, R23-11).

DiagnosticParameterSupportInfo (Base = ARObject) is a nested container aggregated
by DiagnosticParameter.supportInfo; the writer emits SUPPORT-INFO only when the
aggregation is set, with the SUPPORT-INFO-BIT child, via the named reusable helper
writeDiagnosticParameterSupportInfo called from writeDiagnosticParameter.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_parameter_support_info.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticParameter, DiagnosticParameterSupportInfo
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


class TestWriteDiagnosticParameterSupportInfo:
    """Tests for writeDiagnosticParameterSupportInfo — own element field values (Table 4.128)."""

    def test_write_fields_in_xsd_order(self):
        """Test that SUPPORT-INFO-BIT is emitted with the spec value."""
        support_info = DiagnosticParameterSupportInfo()
        support_info.setSupportInfoBit(PositiveInteger().setValue("3"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameterSupportInfo(parent, support_info)

        child = parent.find("SUPPORT-INFO")
        assert child is not None
        assert [c.tag for c in child] == ["SUPPORT-INFO-BIT"]
        assert child.find("SUPPORT-INFO-BIT").text == "3"

    def test_write_unset_fields_emit_no_children(self):
        """Test that an unset supportInfoBit emits the empty SUPPORT-INFO wrapper only."""
        support_info = DiagnosticParameterSupportInfo()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameterSupportInfo(parent, support_info)

        child = parent.find("SUPPORT-INFO")
        assert child is not None
        assert [c.tag for c in child] == []

    def test_parent_dispatch_writes_support_info_bit(self):
        """Test that writeDiagnosticParameter emits SUPPORT-INFO with the bit value."""
        parameter = DiagnosticParameter()
        support_info = DiagnosticParameterSupportInfo()
        support_info.setSupportInfoBit(PositiveInteger().setValue("5"))
        parameter.setSupportInfo(support_info)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameter(parent, parameter)

        child = parent.find("DIAGNOSTIC-PARAMETER")
        assert child.find("SUPPORT-INFO/SUPPORT-INFO-BIT").text == "5"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        parameter = DiagnosticParameter()
        support_info = DiagnosticParameterSupportInfo()
        support_info.setSupportInfoBit(PositiveInteger().setValue("3"))
        parameter.setSupportInfo(support_info)

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticParameter(parent, parameter)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticParameter()
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-PARAMETER")
        ARXMLParser().readDiagnosticParameter(element, reloaded)
        assert reloaded.getSupportInfo() is not None
        assert reloaded.getSupportInfo().getSupportInfoBit() is not None
        assert reloaded.getSupportInfo().getSupportInfoBit().getValue() == 3
