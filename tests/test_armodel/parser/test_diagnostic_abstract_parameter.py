"""
Tests for reading DIAGNOSTIC-ABSTRACT-PARAMETER group elements — DiagnosticAbstractParameter, Table 4.8 (p.37, R23-11).

DiagnosticAbstractParameter (abstract, Base = ARObject) owns the BIT-OFFSET /
DATA-ELEMENTS / PARAMETER-SIZE XML group (XSD group DIAGNOSTIC-ABSTRACT-PARAMETER,
AUTOSAR_00052.xsd l.31435). The PDF multiplicity of dataElement is 0..1 — the XSD
resolves the atpVariation/atpSplitable stereotypes into the DATA-ELEMENTS wrapper
with an unbounded choice, which the reusable helper absorbs into the single
optional field (Rule 0001.4; extra items warn). The child DIAGNOSTIC-DATA-ELEMENT
items are dispatched to readDiagnosticDataElement since the Table 4.9 sync.
The group is reached through the concrete subclasses: readDiagnosticParameter
(Table 4.5) and readDiagnosticParameterElement (Table 4.6).

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_abstract_parameter.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticAbstractParameter, DiagnosticParameter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticParameterElement

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-PARAMETER") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticAbstractParameter:
    """Tests for readDiagnosticAbstractParameter — own group field values (Table 4.8)."""

    def _read(self, parser, inner):
        parameter = DiagnosticParameter()
        parser.readDiagnosticAbstractParameter(_snip(inner), parameter)
        return parameter

    def test_read_sets_all_fields(self, parser):
        """Test that BIT-OFFSET, DATA-ELEMENTS and PARAMETER-SIZE are read with their field values."""
        parameter = self._read(
            parser,
            "<BIT-OFFSET>8</BIT-OFFSET>" "<DATA-ELEMENTS><DIAGNOSTIC-DATA-ELEMENT><SHORT-NAME>De1</SHORT-NAME></DIAGNOSTIC-DATA-ELEMENT></DATA-ELEMENTS>" "<PARAMETER-SIZE>16</PARAMETER-SIZE>",
        )
        assert parameter.getBitOffset() is not None
        assert parameter.getBitOffset().getValue() == 8
        assert parameter.getDataElement() is not None
        assert parameter.getDataElement().getShortName() == "De1"
        assert parameter.getParameterSize() is not None
        assert parameter.getParameterSize().getValue() == 16

    def test_read_empty(self, parser):
        """Test that absent elements leave the fields None."""
        parameter = self._read(parser, "")
        assert parameter.getBitOffset() is None
        assert parameter.getDataElement() is None
        assert parameter.getParameterSize() is None


def test_diagnostic_parameter_dispatch_reads_base_group(parser):
    """Test that readDiagnosticParameter reads the base group with field values."""
    parameter = DiagnosticParameter()
    parser.readDiagnosticParameter(
        _snip("<BIT-OFFSET>8</BIT-OFFSET><PARAMETER-SIZE>16</PARAMETER-SIZE><IDENT><SHORT-NAME>Pid1</SHORT-NAME></IDENT>"),
        parameter,
    )
    assert parameter.getBitOffset() is not None
    assert parameter.getBitOffset().getValue() == 8
    assert parameter.getParameterSize() is not None
    assert parameter.getParameterSize().getValue() == 16
    assert parameter.getIdent() is not None


def test_diagnostic_parameter_element_dispatch_reads_base_group(parser):
    """Test that readDiagnosticParameterElement reads the inherited base group with field values."""
    parent = AUTOSAR.getInstance()
    parameter_element = DiagnosticParameterElement(parent, "Elem1")
    parser.readDiagnosticParameterElement(
        _snip(
            "<SHORT-NAME>Elem1</SHORT-NAME>" "<BIT-OFFSET>8</BIT-OFFSET>" "<PARAMETER-SIZE>16</PARAMETER-SIZE>" "<ARRAY-SIZE>4</ARRAY-SIZE>",
            "DIAGNOSTIC-PARAMETER-ELEMENT",
        ),
        parameter_element,
    )
    assert parameter_element.getBitOffset() is not None
    assert parameter_element.getBitOffset().getValue() == 8
    assert parameter_element.getParameterSize() is not None
    assert parameter_element.getParameterSize().getValue() == 16
    assert parameter_element.getArraySize() is not None
    assert parameter_element.getArraySize().getValue() == 4


def test_abstract_parameter_not_instantiable():
    """Test the abstract guard (Table 4.8 renders the class as abstract)."""
    with pytest.raises(TypeError):
        DiagnosticAbstractParameter()
