"""
Tests for writing DIAGNOSTIC-DATA-IDENTIFIER elements — DiagnosticDataIdentifier, Table 4.2 (p.34, R23-11).

DiagnosticDataIdentifier (Base = DiagnosticAbstractDataIdentifier) carries the
DATA-ELEMENTS wrapper list (DIAGNOSTIC-PARAMETER items), DID-SIZE,
REPRESENTS-VIN and SUPPORT-INFO-BYTE (XSD group DIAGNOSTIC-DATA-IDENTIFIER,
AUTOSAR_00052.xsd l.34234). The writer reads the model via the
getDataElements/get* getters; the dispatch entry is writeARPackageElement →
writeDiagnosticDataIdentifier.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_data_identifier.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticParameter, DiagnosticSupportInfoByte
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDataIdentifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _positive_integer(value: str) -> PositiveInteger:
    id_value = PositiveInteger()
    id_value.setValue(value)
    return id_value


def _represents_vin() -> Boolean:
    represents_vin = Boolean()
    represents_vin.setValue(True)
    return represents_vin


class TestWriteDiagnosticDataIdentifier:
    """Tests for writeDiagnosticDataIdentifier — own element field values (Table 4.2)."""

    def test_write_field_values_in_xsd_order(self):
        """Test that DATA-ELEMENTS, DID-SIZE, REPRESENTS-VIN and SUPPORT-INFO-BYTE are emitted with field values in XSD order."""
        did = DiagnosticDataIdentifier(parent=AUTOSAR.getInstance(), short_name="Di")
        did.setId(_positive_integer("4"))
        did.addDataElement(DiagnosticParameter())
        did.addDataElement(DiagnosticParameter())
        did.setDidSize(_positive_integer("8"))
        did.setRepresentsVin(_represents_vin())
        did.setSupportInfoByte(DiagnosticSupportInfoByte())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDataIdentifier(parent, did)

        child = parent.find("DIAGNOSTIC-DATA-IDENTIFIER")
        assert child is not None
        assert child.find("ID/POSITIVE-INTEGER-VALUE-VARIATION-POINT").text == "4"
        data_elements = child.find("DATA-ELEMENTS")
        assert data_elements is not None
        assert [item.tag for item in data_elements] == ["DIAGNOSTIC-PARAMETER", "DIAGNOSTIC-PARAMETER"]
        assert child.find("DID-SIZE").text == "8"
        assert child.find("REPRESENTS-VIN").text == "true"
        assert child.find("SUPPORT-INFO-BYTE") is not None
        tags = [c.tag for c in child if c.tag != "SHORT-NAME"]
        assert tags == ["ID", "DATA-ELEMENTS", "DID-SIZE", "REPRESENTS-VIN", "SUPPORT-INFO-BYTE"]

    def test_write_unset_fields_omits_tags(self):
        """Test that unset fields and an empty dataElements list emit no elements."""
        did = DiagnosticDataIdentifier(parent=AUTOSAR.getInstance(), short_name="Di")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDataIdentifier(parent, did)

        child = parent.find("DIAGNOSTIC-DATA-IDENTIFIER")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("DATA-ELEMENTS") is None
        assert child.find("DID-SIZE") is None
        assert child.find("REPRESENTS-VIN") is None
        assert child.find("SUPPORT-INFO-BYTE") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticDataIdentifier to a DIAGNOSTIC-DATA-IDENTIFIER element."""
        package = AUTOSAR.getInstance().createARPackage("Dids")
        did = package.createDiagnosticDataIdentifier("Di")
        did.setDidSize(_positive_integer("8"))
        did.setRepresentsVin(_represents_vin())

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, did)

        child = parent.find("DIAGNOSTIC-DATA-IDENTIFIER")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Di"
        assert child.find("DID-SIZE").text == "8"
        assert child.find("REPRESENTS-VIN").text == "true"

    def test_round_trip(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("Dids")
        did = package.createDiagnosticDataIdentifier("Di")
        did.setId(_positive_integer("4"))
        did.addDataElement(DiagnosticParameter())
        did.addDataElement(DiagnosticParameter())
        did.setDidSize(_positive_integer("8"))
        did.setRepresentsVin(_represents_vin())
        did.setSupportInfoByte(DiagnosticSupportInfoByte())

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            did_2 = package_2.getReferrableElement("Di", DiagnosticDataIdentifier)
            assert did_2 is not None
            assert did_2.getId() is not None
            assert did_2.getId().getValue() == 4
            assert len(did_2.getDataElements()) == 2
            assert did_2.getDidSize() is not None
            assert did_2.getDidSize().getValue() == 8
            assert did_2.getRepresentsVin() is not None
            assert did_2.getRepresentsVin().getValue() is True
            assert did_2.getSupportInfoByte() is not None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DID without field values round-trips with all fields empty."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("Dids")
        package.createDiagnosticDataIdentifier("Di")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            did_2 = package_2.getReferrableElement("Di", DiagnosticDataIdentifier)
            assert did_2 is not None
            assert did_2.getId() is None
            assert did_2.getDataElements() == []
            assert did_2.getDidSize() is None
            assert did_2.getRepresentsVin() is None
            assert did_2.getSupportInfoByte() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
