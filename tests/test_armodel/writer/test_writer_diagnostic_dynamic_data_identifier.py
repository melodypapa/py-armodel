"""
Tests for writing DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER elements — DiagnosticDynamicDataIdentifier, Table 4.3 (p.34, R23-11).

DiagnosticDynamicDataIdentifier (Base = DiagnosticAbstractDataIdentifier) has no
own attributes (XSD group DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER, AUTOSAR_00052.xsd
l.35097, empty sequence). The writer delegates to
writeDiagnosticAbstractDataIdentifier for the inherited id; the dispatch entry is
writeARPackageElement → writeDiagnosticDynamicDataIdentifier.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_dynamic_data_identifier.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDynamicDataIdentifier
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


def _positive_integer(value: str) -> PositiveInteger:
    id_value = PositiveInteger()
    id_value.setValue(value)
    return id_value


class TestWriteDiagnosticDynamicDataIdentifier:
    """Tests for writeDiagnosticDynamicDataIdentifier — inherited base field values (Table 4.3)."""

    def test_write_inherited_id(self):
        """Test that the element is emitted with only the inherited ID group content."""
        did = DiagnosticDynamicDataIdentifier(parent=AUTOSAR.getInstance(), short_name="Ddi")
        did.setId(_positive_integer("9"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDynamicDataIdentifier(parent, did)

        child = parent.find("DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME", "ID"]
        assert child.find("ID/POSITIVE-INTEGER-VALUE-VARIATION-POINT").text == "9"

    def test_write_empty(self):
        """Test that an element without field values emits only the SHORT-NAME."""
        did = DiagnosticDynamicDataIdentifier(parent=AUTOSAR.getInstance(), short_name="Ddi")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDynamicDataIdentifier(parent, did)

        child = parent.find("DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticDynamicDataIdentifier to a DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER element."""
        package = AUTOSAR.getInstance().createARPackage("Dids")
        did = package.createDiagnosticDynamicDataIdentifier("Ddi")
        did.setId(_positive_integer("9"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, did)

        child = parent.find("DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Ddi"
        assert child.find("ID/POSITIVE-INTEGER-VALUE-VARIATION-POINT").text == "9"

    def test_round_trip(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("Dids")
        did = package.createDiagnosticDynamicDataIdentifier("Ddi")
        did.setId(_positive_integer("9"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            did_2 = package_2.getElement("Ddi", DiagnosticDynamicDataIdentifier)
            assert did_2 is not None
            assert isinstance(did_2, DiagnosticDynamicDataIdentifier)
            assert did_2.getId() is not None
            assert did_2.getId().getValue() == 9
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a dynamic DID without field values round-trips with id None."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("Dids")
        package.createDiagnosticDynamicDataIdentifier("Ddi")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            did_2 = package_2.getElement("Ddi", DiagnosticDynamicDataIdentifier)
            assert did_2 is not None
            assert did_2.getId() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
