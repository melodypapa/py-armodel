"""
Tests for reading the SUPPORT-INFO element — DiagnosticParameterSupportInfo,
Table 4.128 (p.149, R23-11).

DiagnosticParameterSupportInfo (Base = ARObject) is a nested container aggregated
by DiagnosticParameter.supportInfo (XSD group DIAGNOSTIC-PARAMETER l.40589,
element SUPPORT-INFO type DIAGNOSTIC-PARAMETER-SUPPORT-INFO, 0..1). Its own
group DIAGNOSTIC-PARAMETER-SUPPORT-INFO (AUTOSAR_00052.xsd l.40849) carries the
single 0..1 element SUPPORT-INFO-BIT. The reader is the named reusable helper
readDiagnosticParameterSupportInfo, called from readDiagnosticParameter.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_parameter_support_info.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticParameter, DiagnosticParameterSupportInfo

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "SUPPORT-INFO") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticParameterSupportInfo:
    """Tests for readDiagnosticParameterSupportInfo — own element field values (Table 4.128)."""

    def _read(self, parser, inner):
        support_info = DiagnosticParameterSupportInfo()
        parser.readDiagnosticParameterSupportInfo(_snip(inner), support_info)
        return support_info

    def test_read_sets_all_fields(self, parser):
        """Test that SUPPORT-INFO-BIT is read with its value."""
        support_info = self._read(parser, "<SUPPORT-INFO-BIT>3</SUPPORT-INFO-BIT>")
        assert support_info.getSupportInfoBit() is not None
        assert support_info.getSupportInfoBit().getValue() == 3

    def test_read_empty(self, parser):
        """Test that an empty SUPPORT-INFO wrapper leaves the field None."""
        support_info = self._read(parser, "")
        assert support_info.getSupportInfoBit() is None

    def test_parent_dispatch_reads_support_info_bit(self, parser):
        """Test that readDiagnosticParameter wires SUPPORT-INFO through the helper, preserving the bit value."""
        parameter = DiagnosticParameter()
        element = ET.fromstring("<DIAGNOSTIC-PARAMETER xmlns='%s'><SUPPORT-INFO><SUPPORT-INFO-BIT>5</SUPPORT-INFO-BIT></SUPPORT-INFO></DIAGNOSTIC-PARAMETER>" % NS)
        parser.readDiagnosticParameter(element, parameter)
        assert parameter.getSupportInfo() is not None
        assert parameter.getSupportInfo().getSupportInfoBit() is not None
        assert parameter.getSupportInfo().getSupportInfoBit().getValue() == 5
