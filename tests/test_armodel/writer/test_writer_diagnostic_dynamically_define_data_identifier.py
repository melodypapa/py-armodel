"""
Tests for writing DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER elements —
DiagnosticDynamicallyDefineDataIdentifier, Table 4.93 (p.127, R23-11).

DiagnosticDynamicallyDefineDataIdentifier (concrete ARElement, Aggregated by
ARPackage.element) defines three 0..1 attributes: dataIdentifier
(DATA-IDENTIFIER-REF), dynamicallyDefineDataIdentifierClass
(DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS-REF) and maxSourceElement
(MAX-SOURCE-ELEMENT) — AUTOSAR_00052.xsd group
DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER l.35133 / complexType l.35177.
The writer emits the children in XSD sequence order. The dispatch entry is
writeARPackageElement → writeDiagnosticDynamicallyDefineDataIdentifier.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_dynamically_define_data_identifier.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDynamicallyDefineDataIdentifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestWriteDiagnosticDynamicallyDefineDataIdentifier:
    """Tests for writeDiagnosticDynamicallyDefineDataIdentifier — own element field values (Table 4.93)."""

    def _write(self, dddi: DiagnosticDynamicallyDefineDataIdentifier) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDynamicallyDefineDataIdentifier(parent, dddi)
        return parent.find("DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticDynamicallyDefineDataIdentifier without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDynamicallyDefineDataIdentifiers")
        package.createDiagnosticDynamicallyDefineDataIdentifier("Dddi1")

        child = self._write(package.getReferrableElement("Dddi1", DiagnosticDynamicallyDefineDataIdentifier))
        assert child is not None
        assert child.find("SHORT-NAME").text == "Dddi1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_data_identifier_ref(self):
        """Test that the DATA-IDENTIFIER-REF is emitted with its DEST attribute."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDynamicallyDefineDataIdentifiers")
        dddi = package.createDiagnosticDynamicallyDefineDataIdentifier("Dddi1")
        dddi.setDataIdentifier(_ref("DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER", "/AUTOSAR/DiagnosticDynamicDataIdentifiers/Did1"))

        child = self._write(dddi)
        assert child is not None
        ref = child.find("DATA-IDENTIFIER-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticDynamicDataIdentifiers/Did1"
        assert ref.get("DEST") == "DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER"

    def test_write_dynamically_define_data_identifier_class_ref(self):
        """Test that the DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS-REF is emitted with its DEST attribute."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDynamicallyDefineDataIdentifiers")
        dddi = package.createDiagnosticDynamicallyDefineDataIdentifier("Dddi1")
        dddi.setDynamicallyDefineDataIdentifierClass(_ref("DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS", "/AUTOSAR/DiagnosticDynamicallyDefineDataIdentifiers/Class1"))

        child = self._write(dddi)
        assert child is not None
        ref = child.find("DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticDynamicallyDefineDataIdentifiers/Class1"
        assert ref.get("DEST") == "DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS"

    def test_write_max_source_element(self):
        """Test that the MAX-SOURCE-ELEMENT is emitted from maxSourceElement."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDynamicallyDefineDataIdentifiers")
        dddi = package.createDiagnosticDynamicallyDefineDataIdentifier("Dddi1")
        max_source_element = PositiveInteger()
        max_source_element.setValue("9")
        dddi.setMaxSourceElement(max_source_element)

        child = self._write(dddi)
        assert child is not None
        element = child.find("MAX-SOURCE-ELEMENT")
        assert element is not None
        assert element.text == "9"

    def test_write_children_follow_xsd_sequence(self):
        """Test that the children are emitted in XSD sequence order (DATA-IDENTIFIER-REF, DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS-REF, MAX-SOURCE-ELEMENT)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDynamicallyDefineDataIdentifiers")
        dddi = package.createDiagnosticDynamicallyDefineDataIdentifier("Dddi1")
        max_source_element = PositiveInteger()
        max_source_element.setValue("9")
        dddi.setMaxSourceElement(max_source_element)
        dddi.setDynamicallyDefineDataIdentifierClass(_ref("DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS", "/AUTOSAR/DiagnosticDynamicallyDefineDataIdentifiers/Class1"))
        dddi.setDataIdentifier(_ref("DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER", "/AUTOSAR/DiagnosticDynamicDataIdentifiers/Did1"))

        child = self._write(dddi)
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == ["DATA-IDENTIFIER-REF", "DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS-REF", "MAX-SOURCE-ELEMENT"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticDynamicallyDefineDataIdentifier to a DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDynamicallyDefineDataIdentifiers")
        package.createDiagnosticDynamicallyDefineDataIdentifier("Dddi1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("Dddi1", DiagnosticDynamicallyDefineDataIdentifier))

        child = parent.find("DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Dddi1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticDynamicallyDefineDataIdentifiers")
        dddi = package.createDiagnosticDynamicallyDefineDataIdentifier("Dddi1")
        dddi.setDataIdentifier(_ref("DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER", "/AUTOSAR/DiagnosticDynamicDataIdentifiers/Did1"))
        dddi.setDynamicallyDefineDataIdentifierClass(_ref("DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS", "/AUTOSAR/DiagnosticDynamicallyDefineDataIdentifiers/Class1"))
        max_source_element = PositiveInteger()
        max_source_element.setValue("9")
        dddi.setMaxSourceElement(max_source_element)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            dddi_2 = package_2.getReferrableElement("Dddi1", DiagnosticDynamicallyDefineDataIdentifier)
            assert dddi_2 is not None
            assert dddi_2.getShortName() == "Dddi1"
            data_identifier = dddi_2.getDataIdentifier()
            assert data_identifier is not None
            assert data_identifier.getValue() == "/AUTOSAR/DiagnosticDynamicDataIdentifiers/Did1"
            assert data_identifier.getDest() == "DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER"
            class_ref = dddi_2.getDynamicallyDefineDataIdentifierClass()
            assert class_ref is not None
            assert class_ref.getValue() == "/AUTOSAR/DiagnosticDynamicallyDefineDataIdentifiers/Class1"
            assert class_ref.getDest() == "DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS"
            assert dddi_2.getMaxSourceElement() is not None
            assert dddi_2.getMaxSourceElement().getValue() == 9
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
