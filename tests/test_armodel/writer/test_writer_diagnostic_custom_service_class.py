"""
Tests for writing DIAGNOSTIC-CUSTOM-SERVICE-CLASS elements —
DiagnosticCustomServiceClass, Table 4.28 (p.71, R23-11).

DiagnosticCustomServiceClass (Base chain reaches DiagnosticServiceClass) carries
its own 0..1 CUSTOM-SERVICE-ID (PositiveInteger) — XSD group
DIAGNOSTIC-CUSTOM-SERVICE-CLASS, AUTOSAR_00052.xsd l.33976. The writer reads
the model via the get* getters; the dispatch entry is writeARPackageElement →
writeDiagnosticCustomServiceClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_custom_service_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticCustomServiceClass
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
    custom_service_id = PositiveInteger()
    custom_service_id.setValue(value)
    return custom_service_id


class TestWriteDiagnosticCustomServiceClass:
    """Tests for writeDiagnosticCustomServiceClass — own element field values (Table 4.28)."""

    def test_write_custom_service_id(self):
        """Test that CUSTOM-SERVICE-ID is emitted with the spec value."""
        package = AUTOSAR.getInstance().createARPackage("CustomServiceClasses")
        service_class = package.createDiagnosticCustomServiceClass("Csc")
        service_class.setCustomServiceId(_positive_integer("5"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticCustomServiceClass(parent, service_class)

        child = parent.find("DIAGNOSTIC-CUSTOM-SERVICE-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Csc"
        assert child.find("CUSTOM-SERVICE-ID").text == "5"
        tags = [c.tag for c in child if c.tag != "SHORT-NAME"]
        assert tags == ["CUSTOM-SERVICE-ID"]

    def test_write_unset_field_omits_tag(self):
        """Test that an unset customServiceId emits no elements beyond SHORT-NAME."""
        package = AUTOSAR.getInstance().createARPackage("CustomServiceClasses")
        package.createDiagnosticCustomServiceClass("Csc")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticCustomServiceClass(parent, package.getElement("Csc", DiagnosticCustomServiceClass))

        child = parent.find("DIAGNOSTIC-CUSTOM-SERVICE-CLASS")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("CUSTOM-SERVICE-ID") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticCustomServiceClass to a DIAGNOSTIC-CUSTOM-SERVICE-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("CustomServiceClasses")
        service_class = package.createDiagnosticCustomServiceClass("Csc")
        service_class.setCustomServiceId(_positive_integer("5"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, service_class)

        child = parent.find("DIAGNOSTIC-CUSTOM-SERVICE-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Csc"
        assert child.find("CUSTOM-SERVICE-ID").text == "5"

    def test_round_trip(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("CustomServiceClasses")
        service_class = package.createDiagnosticCustomServiceClass("Csc")
        service_class.setCustomServiceId(_positive_integer("5"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            service_class_2 = package_2.getElement("Csc", DiagnosticCustomServiceClass)
            assert service_class_2 is not None
            assert service_class_2.getCustomServiceId() is not None
            assert service_class_2.getCustomServiceId().getValue() == 5
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticCustomServiceClass without field values round-trips with all fields empty."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("CustomServiceClasses")
        package.createDiagnosticCustomServiceClass("Csc")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            service_class_2 = package_2.getElement("Csc", DiagnosticCustomServiceClass)
            assert service_class_2 is not None
            assert service_class_2.getCustomServiceId() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
