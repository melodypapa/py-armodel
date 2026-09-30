"""
Tests for reading DIAGNOSTIC-PARAMETER-IDENT elements — DiagnosticParameterIdent, Table 4.7 (p.37, R23-11).

DiagnosticParameterIdent (Base = IdentCaption) carries the top-level SUB-ELEMENTS
aggregation (XSD group DIAGNOSTIC-PARAMETER-IDENT, AUTOSAR_00052.xsd l.40735 —
choice of DIAGNOSTIC-PARAMETER-ELEMENT; the ATP-CLASSIFIER/ATP-FEATURE/
ATP-STRUCTURE-ELEMENT/IDENT-CAPTION/DIAGNOSTIC-SERVICE-MAPPING-DIAG-TARGET groups
are empty sequences). The reader populates the model via the createSubElement
mutator; DIAGNOSTIC-PARAMETER-IDENT is reached through the DiagnosticParameter
IDENT dispatch, which replaces the former identity-only SHORT-NAME read.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_parameter_ident.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDataIdentifier
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import DiagnosticParameterIdent

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DIAGNOSTIC-PARAMETER-IDENT xmlns='{NS}'>{inner}</DIAGNOSTIC-PARAMETER-IDENT>")


class TestReadDiagnosticParameterIdent:
    """Tests for readDiagnosticParameterIdent — own element field values (Table 4.7)."""

    def _read(self, parser, inner):
        ident = DiagnosticParameterIdent(AUTOSAR.getInstance(), "Pid1")
        parser.readDiagnosticParameterIdent(_snip(inner), ident)
        return ident

    def test_read_sets_sub_elements(self, parser):
        """Test that SUB-ELEMENTS items are read with their field values."""
        ident = self._read(
            parser,
            "<SHORT-NAME>Pid1</SHORT-NAME>" "<SUB-ELEMENTS>" "<DIAGNOSTIC-PARAMETER-ELEMENT><SHORT-NAME>Sub1</SHORT-NAME><ARRAY-SIZE>4</ARRAY-SIZE></DIAGNOSTIC-PARAMETER-ELEMENT>" "</SUB-ELEMENTS>",
        )
        assert ident.getShortName() == "Pid1"
        assert len(ident.getSubElements()) == 1
        sub_element = ident.getSubElements()[0]
        assert sub_element.getShortName() == "Sub1"
        assert sub_element.getArraySize() is not None
        assert sub_element.getArraySize().getValue() == 4

    def test_read_empty(self, parser):
        """Test that absent SUB-ELEMENTS leaves the aggregation empty."""
        ident = self._read(parser, "<SHORT-NAME>Pid1</SHORT-NAME>")
        assert ident.getSubElements() == []


def test_ident_dispatch_reads_sub_elements(parser):
    """Test that readDiagnosticParameter dispatches IDENT/SUB-ELEMENTS with field values."""
    did = DiagnosticDataIdentifier(parent=AUTOSAR.getInstance(), short_name="Di")
    element = ET.fromstring(
        "<DIAGNOSTIC-DATA-IDENTIFIER xmlns='%s'>"
        "<SHORT-NAME>Di</SHORT-NAME>"
        "<DATA-ELEMENTS>"
        "<DIAGNOSTIC-PARAMETER>"
        "<IDENT><SHORT-NAME>Pid1</SHORT-NAME>"
        "<SUB-ELEMENTS><DIAGNOSTIC-PARAMETER-ELEMENT><SHORT-NAME>Sub1</SHORT-NAME><ARRAY-SIZE>4</ARRAY-SIZE></DIAGNOSTIC-PARAMETER-ELEMENT></SUB-ELEMENTS>"
        "</IDENT>"
        "</DIAGNOSTIC-PARAMETER>"
        "</DATA-ELEMENTS>"
        "</DIAGNOSTIC-DATA-IDENTIFIER>" % NS
    )
    parser.readDiagnosticDataIdentifier(element, did)

    parameter = did.getDataElements()[0]
    ident = parameter.getIdent()
    assert ident is not None
    assert isinstance(ident, DiagnosticParameterIdent)
    assert ident.getShortName() == "Pid1"
    assert len(ident.getSubElements()) == 1
    assert ident.getSubElements()[0].getShortName() == "Sub1"
    assert ident.getSubElements()[0].getArraySize() is not None
    assert ident.getSubElements()[0].getArraySize().getValue() == 4
