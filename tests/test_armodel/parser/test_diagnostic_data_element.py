"""
Tests for reading DIAGNOSTIC-DATA-ELEMENT elements — DiagnosticDataElement, Table 4.9 (p.41, R23-11).

DiagnosticDataElement (Base = Identifiable, VP-capable per Rule 0020) owns the
ARRAY-SIZE-SEMANTICS / MAX-NUMBER-OF-ELEMENTS / SCALING-INFO-SIZE /
SW-DATA-DEF-PROPS / VARIATION-POINT group (XSD group DIAGNOSTIC-DATA-ELEMENT,
AUTOSAR_00052.xsd l.34124 — VARIATION-POINT last, sequenceOffset=10000). The
reader populates the model via the set mutators; DIAGNOSTIC-DATA-ELEMENT items are
reached through the DiagnosticAbstractParameter DATA-ELEMENTS dispatch, which
replaces the former identity-only SHORT-NAME read.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_data_element.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticParameter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticDataElement

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DIAGNOSTIC-DATA-ELEMENT xmlns='{NS}'>{inner}</DIAGNOSTIC-DATA-ELEMENT>")


class TestReadDiagnosticDataElement:
    """Tests for readDiagnosticDataElement — own element field values (Table 4.9)."""

    def _read(self, parser, inner):
        parent = AUTOSAR.getInstance()
        data_element = DiagnosticDataElement(parent, "De1")
        parser.readDiagnosticDataElement(_snip(inner), data_element)
        return data_element

    def test_read_sets_all_fields(self, parser):
        """Test that all four attributes plus VARIATION-POINT are read with their field values."""
        data_element = self._read(
            parser,
            "<SHORT-NAME>De1</SHORT-NAME>"
            "<ARRAY-SIZE-SEMANTICS>FIXED-SIZE</ARRAY-SIZE-SEMANTICS>"
            "<MAX-NUMBER-OF-ELEMENTS>4</MAX-NUMBER-OF-ELEMENTS>"
            "<SCALING-INFO-SIZE>8</SCALING-INFO-SIZE>"
            "<SW-DATA-DEF-PROPS><SW-DATA-DEF-PROPS-VARIANTS><SW-DATA-DEF-PROPS-CONDITIONAL>"
            "<BASE-TYPE-REF DEST='SW-BASE-TYPE-REF'>/Base/uint8</BASE-TYPE-REF>"
            "</SW-DATA-DEF-PROPS-CONDITIONAL></SW-DATA-DEF-PROPS-VARIANTS></SW-DATA-DEF-PROPS>"
            "<VARIATION-POINT />",
        )
        assert data_element.getArraySizeSemantics() is not None
        assert data_element.getArraySizeSemantics().getValue() == "FIXED-SIZE"
        assert data_element.getMaxNumberOfElements() is not None
        assert data_element.getMaxNumberOfElements().getValue() == 4
        assert data_element.getScalingInfoSize() is not None
        assert data_element.getScalingInfoSize().getValue() == 8
        assert data_element.getSwDataDefProps() is not None
        assert data_element.getSwDataDefProps().getBaseTypeRef().getValue() == "/Base/uint8"
        assert data_element.getVariationPoint() is not None

    def test_read_empty(self, parser):
        """Test that absent elements leave the fields at their defaults."""
        data_element = self._read(parser, "<SHORT-NAME>De1</SHORT-NAME>")
        assert data_element.getArraySizeSemantics() is None
        assert data_element.getMaxNumberOfElements() is None
        assert data_element.getScalingInfoSize() is None
        assert data_element.getSwDataDefProps() is None
        assert data_element.getVariationPoint() is None


def test_data_elements_dispatch_reads_diagnostic_data_element(parser):
    """Test that readDiagnosticAbstractParameter dispatches DIAGNOSTIC-DATA-ELEMENT items with field values."""
    parameter = DiagnosticParameter()
    element = ET.fromstring(
        "<DIAGNOSTIC-PARAMETER xmlns='%s'>"
        "<DATA-ELEMENTS>"
        "<DIAGNOSTIC-DATA-ELEMENT><SHORT-NAME>De1</SHORT-NAME><MAX-NUMBER-OF-ELEMENTS>4</MAX-NUMBER-OF-ELEMENTS></DIAGNOSTIC-DATA-ELEMENT>"
        "</DATA-ELEMENTS>"
        "</DIAGNOSTIC-PARAMETER>" % NS
    )
    parser.readDiagnosticAbstractParameter(element, parameter)

    data_element = parameter.getDataElement()
    assert isinstance(data_element, DiagnosticDataElement)
    assert data_element.getShortName() == "De1"
    assert data_element.getMaxNumberOfElements() is not None
    assert data_element.getMaxNumberOfElements().getValue() == 4
