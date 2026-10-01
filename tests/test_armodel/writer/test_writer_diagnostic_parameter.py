"""
Tests for writing DIAGNOSTIC-PARAMETER elements — DiagnosticParameter, Table 4.5 (p.36, R23-11).

DiagnosticParameter (Base = DiagnosticAbstractParameter, an un-synced stub queued
for a later batch) carries the IDENT and SUPPORT-INFO aggregations plus the
VARIATION-POINT slot (XSD group DIAGNOSTIC-PARAMETER, AUTOSAR_00052.xsd l.40573,
sequenceOffset=10000 → last). The writer reads the model via the
getIdent/getSupportInfo/getVariationPoint getters; DIAGNOSTIC-PARAMETER items are
emitted through the DiagnosticDataIdentifier DATA-ELEMENTS dispatch.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_parameter.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticParameter, DiagnosticParameterSupportInfo
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDataIdentifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticParameter:
    """Tests for writeDiagnosticParameter — own element field values (Table 4.5)."""

    def test_write_field_values_in_xsd_order(self):
        """Test that IDENT, SUPPORT-INFO and VARIATION-POINT are emitted in XSD order (VARIATION-POINT last)."""
        parameter = DiagnosticParameter()
        parameter.createIdent("Pid1")
        parameter.setSupportInfo(DiagnosticParameterSupportInfo())
        parameter.setVariationPoint(VariationPoint())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameter(parent, parameter)

        child = parent.find("DIAGNOSTIC-PARAMETER")
        assert child is not None
        assert child.find("IDENT/SHORT-NAME").text == "Pid1"
        assert child.find("SUPPORT-INFO") is not None
        assert child.find("VARIATION-POINT") is not None
        tags = [c.tag for c in child]
        assert tags == ["IDENT", "SUPPORT-INFO", "VARIATION-POINT"]

    def test_write_unset_fields_omits_tags(self):
        """Test that unset aggregations emit no elements."""
        parameter = DiagnosticParameter()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameter(parent, parameter)

        child = parent.find("DIAGNOSTIC-PARAMETER")
        assert child is not None
        assert [c.tag for c in child] == []

    def test_data_elements_dispatch_writes_parameter(self):
        """Test that writeDiagnosticDataIdentifier emits DIAGNOSTIC-PARAMETER items with their content."""
        did = DiagnosticDataIdentifier(parent=AUTOSAR.getInstance(), short_name="Di")
        parameter = DiagnosticParameter()
        parameter.createIdent("Pid1")
        did.addDataElement(parameter)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDataIdentifier(parent, did)

        child = parent.find("DIAGNOSTIC-DATA-IDENTIFIER")
        data_elements = child.find("DATA-ELEMENTS")
        assert data_elements is not None
        items = list(data_elements)
        assert [item.tag for item in items] == ["DIAGNOSTIC-PARAMETER"]
        assert items[0].find("IDENT/SHORT-NAME").text == "Pid1"

    def test_round_trip(self):
        """Test the full set → save → reload → assert cycle over a DiagnosticDataIdentifier aggregation."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("Dids")
        did = package.createDiagnosticDataIdentifier("Di")
        parameter = DiagnosticParameter()
        parameter.createIdent("Pid1")
        parameter.setSupportInfo(DiagnosticParameterSupportInfo())
        parameter.setVariationPoint(VariationPoint())
        did.addDataElement(parameter)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            did_2 = package_2.getElement("Di", DiagnosticDataIdentifier)
            assert did_2 is not None
            assert len(did_2.getDataElements()) == 1
            parameter_2 = did_2.getDataElements()[0]
            assert parameter_2.getIdent() is not None
            assert parameter_2.getIdent().getShortName() == "Pid1"
            assert parameter_2.getSupportInfo() is not None
            assert parameter_2.getVariationPoint() is not None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
