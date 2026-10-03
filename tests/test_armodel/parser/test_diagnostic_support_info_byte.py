"""
Tests for reading the SUPPORT-INFO-BYTE element — DiagnosticSupportInfoByte,
Table 4.129 (p.150, R23-11).

DiagnosticSupportInfoByte (Base = ARObject) is a nested container aggregated by
DiagnosticDataIdentifier.supportInfoByte and
DiagnosticParameterIdentifier.supportInfoByte (XSD SUPPORT-INFO-BYTE, 0..1
each). Its own group DIAGNOSTIC-SUPPORT-INFO-BYTE (AUTOSAR_00052.xsd l.45864)
carries the 0..1 elements POSITION and SIZE. The reader is the named reusable
helper readDiagnosticSupportInfoByte, called from readDiagnosticDataIdentifier
and readDiagnosticParameterIdentifier.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_support_info_byte.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticSupportInfoByte
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDataIdentifier, DiagnosticParameterIdentifier

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "SUPPORT-INFO-BYTE") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticSupportInfoByte:
    """Tests for readDiagnosticSupportInfoByte — own element field values (Table 4.129)."""

    def _read(self, parser, inner):
        support_info_byte = DiagnosticSupportInfoByte()
        parser.readDiagnosticSupportInfoByte(_snip(inner), support_info_byte)
        return support_info_byte

    def test_read_sets_all_fields(self, parser):
        """Test that POSITION and SIZE are read with their values."""
        support_info_byte = self._read(parser, "<POSITION>1</POSITION><SIZE>2</SIZE>")
        assert support_info_byte.getPosition() is not None
        assert support_info_byte.getPosition().getValue() == 1
        assert support_info_byte.getSize() is not None
        assert support_info_byte.getSize().getValue() == 2

    def test_read_empty(self, parser):
        """Test that an empty SUPPORT-INFO-BYTE wrapper leaves the fields None."""
        support_info_byte = self._read(parser, "")
        assert support_info_byte.getPosition() is None
        assert support_info_byte.getSize() is None

    def test_data_identifier_dispatch_reads_support_info_byte(self, parser):
        """Test that readDiagnosticDataIdentifier wires SUPPORT-INFO-BYTE through the helper, preserving the values."""
        did = DiagnosticDataIdentifier(parent=AUTOSAR.getInstance(), short_name="Di")
        element = ET.fromstring(
            "<DIAGNOSTIC-DATA-IDENTIFIER xmlns='%s'><SHORT-NAME>Di</SHORT-NAME><SUPPORT-INFO-BYTE><POSITION>1</POSITION><SIZE>2</SIZE></SUPPORT-INFO-BYTE></DIAGNOSTIC-DATA-IDENTIFIER>" % NS
        )
        parser.readDiagnosticDataIdentifier(element, did)
        assert did.getSupportInfoByte() is not None
        assert did.getSupportInfoByte().getPosition() is not None
        assert did.getSupportInfoByte().getPosition().getValue() == 1
        assert did.getSupportInfoByte().getSize() is not None
        assert did.getSupportInfoByte().getSize().getValue() == 2

    def test_parameter_identifier_dispatch_reads_support_info_byte(self, parser):
        """Test that readDiagnosticParameterIdentifier wires SUPPORT-INFO-BYTE through the helper, preserving the values."""
        parameter_identifier = DiagnosticParameterIdentifier(AUTOSAR.getInstance(), "Pid1")
        element = ET.fromstring(
            "<DIAGNOSTIC-PARAMETER-IDENTIFIER xmlns='%s'><SHORT-NAME>Pid1</SHORT-NAME><SUPPORT-INFO-BYTE><POSITION>3</POSITION><SIZE>4</SIZE></SUPPORT-INFO-BYTE></DIAGNOSTIC-PARAMETER-IDENTIFIER>"
            % NS
        )
        parser.readDiagnosticParameterIdentifier(element, parameter_identifier)
        assert parameter_identifier.getSupportInfoByte() is not None
        assert parameter_identifier.getSupportInfoByte().getPosition() is not None
        assert parameter_identifier.getSupportInfoByte().getPosition().getValue() == 3
        assert parameter_identifier.getSupportInfoByte().getSize() is not None
        assert parameter_identifier.getSupportInfoByte().getSize().getValue() == 4
