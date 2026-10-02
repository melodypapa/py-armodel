"""
Tests for writing DIAGNOSTIC-AUTHENTICATION-CLASS elements —
DiagnosticAuthenticationClass, Table 4.52 (p.99, R23-11).

DiagnosticAuthenticationClass (Base most-derived DiagnosticServiceClass)
defines no attributes of its own (Table 4.52 attribute row is "-") — the wire
element is an IDENTIFIABLE-only wrapper, AUTOSAR_00052.xsd complexType
DIAGNOSTIC-AUTHENTICATION-CLASS l.31963. The dispatch entry is
writeARPackageElement → writeDiagnosticAuthenticationClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_authentication_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticAuthenticationClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticAuthenticationClass:
    """Tests for writeDiagnosticAuthenticationClass — own element field values (Table 4.52)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticAuthenticationClass emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("AuthenticationClasses")
        package.createDiagnosticAuthenticationClass("AuthClass1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAuthenticationClass(parent, package.getReferrableElement("AuthClass1", DiagnosticAuthenticationClass))

        child = parent.find("DIAGNOSTIC-AUTHENTICATION-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "AuthClass1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticAuthenticationClass to a DIAGNOSTIC-AUTHENTICATION-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("AuthenticationClasses")
        package.createDiagnosticAuthenticationClass("AuthClass1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("AuthClass1", DiagnosticAuthenticationClass))

        child = parent.find("DIAGNOSTIC-AUTHENTICATION-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "AuthClass1"

    def test_round_trip(self):
        """Test the full create → save → reload → assert cycle over an ARPackage."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("AuthenticationClasses")
        package.createDiagnosticAuthenticationClass("AuthClass1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            service_class_2 = package_2.getReferrableElement("AuthClass1", DiagnosticAuthenticationClass)
            assert service_class_2 is not None
            assert service_class_2.getShortName() == "AuthClass1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
