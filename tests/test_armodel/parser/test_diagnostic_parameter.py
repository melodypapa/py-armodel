"""
Tests for reading DIAGNOSTIC-PARAMETER elements — DiagnosticParameter, Table 4.5 (p.36, R23-11).

DiagnosticParameter (Base = DiagnosticAbstractParameter, an un-synced stub queued
for a later batch) carries the IDENT and SUPPORT-INFO aggregations plus the
VARIATION-POINT slot (XSD group DIAGNOSTIC-PARAMETER, AUTOSAR_00052.xsd l.40573,
sequenceOffset=10000 → last). The reader populates the model via the
createIdent/setSupportInfo/setVariationPoint mutators; DIAGNOSTIC-PARAMETER items
are reached through the DiagnosticDataIdentifier DATA-ELEMENTS dispatch.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_parameter.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticParameter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDataIdentifier

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-PARAMETER") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticParameter:
    """Tests for readDiagnosticParameter — own element field values (Table 4.5)."""

    def _read(self, parser, inner):
        parameter = DiagnosticParameter()
        parser.readDiagnosticParameter(_snip(inner), parameter)
        return parameter

    def test_read_sets_all_fields(self, parser):
        """Test that IDENT, SUPPORT-INFO and VARIATION-POINT are read with their field values."""
        parameter = self._read(
            parser,
            "<IDENT><SHORT-NAME>Pid1</SHORT-NAME></IDENT>" "<SUPPORT-INFO><SUPPORT-INFO-BIT>3</SUPPORT-INFO-BIT></SUPPORT-INFO>" "<VARIATION-POINT />",
        )
        assert parameter.getIdent() is not None
        assert parameter.getIdent().getShortName() == "Pid1"
        assert parameter.getSupportInfo() is not None
        assert parameter.getVariationPoint() is not None

    def test_read_empty(self, parser):
        """Test that absent elements leave the fields None."""
        parameter = self._read(parser, "")
        assert parameter.getIdent() is None
        assert parameter.getSupportInfo() is None
        assert parameter.getVariationPoint() is None


def test_data_elements_dispatch_reads_diagnostic_parameter(parser):
    """Test that readDiagnosticDataIdentifier dispatches DIAGNOSTIC-PARAMETER items with field values."""
    did = DiagnosticDataIdentifier(parent=AUTOSAR.getInstance(), short_name="Di")
    element = ET.fromstring(
        "<DIAGNOSTIC-DATA-IDENTIFIER xmlns='%s'>"
        "<SHORT-NAME>Di</SHORT-NAME>"
        "<DATA-ELEMENTS>"
        "<DIAGNOSTIC-PARAMETER>"
        "<IDENT><SHORT-NAME>Pid1</SHORT-NAME></IDENT>"
        "<SUPPORT-INFO />"
        "</DIAGNOSTIC-PARAMETER>"
        "</DATA-ELEMENTS>"
        "</DIAGNOSTIC-DATA-IDENTIFIER>" % NS
    )
    parser.readDiagnosticDataIdentifier(element, did)

    assert len(did.getDataElements()) == 1
    data_element = did.getDataElements()[0]
    assert isinstance(data_element, DiagnosticParameter)
    assert data_element.getIdent() is not None
    assert data_element.getIdent().getShortName() == "Pid1"
    assert data_element.getSupportInfo() is not None
