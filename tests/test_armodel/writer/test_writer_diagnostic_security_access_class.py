"""
Tests for writing DIAGNOSTIC-SECURITY-ACCESS-CLASS elements —
DiagnosticSecurityAccessClass, Table 4.50 (p.96, R23-11).

DiagnosticSecurityAccessClass (Base most-derived DiagnosticServiceClass, stamped
abstract in the chain) defines no attributes of its own (Table 4.50 attribute
row is "-"; the XSD group DIAGNOSTIC-SECURITY-ACCESS-CLASS carries only the
AP-restricted SHARED-TIMER, out of CP scope) — the wire element is an
IDENTIFIABLE-only wrapper, AUTOSAR_00052.xsd complexType
DIAGNOSTIC-SECURITY-ACCESS-CLASS l.43331. The dispatch entry is
writeARPackageElement → writeDiagnosticSecurityAccessClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_security_access_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticSecurityAccessClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticSecurityAccessClass:
    """Tests for writeDiagnosticSecurityAccessClass — own element field values (Table 4.50)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticSecurityAccessClass emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("SecAccessClasses")
        package.createDiagnosticSecurityAccessClass("SecAccessClass1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticSecurityAccessClass(parent, package.getReferrableElement("SecAccessClass1", DiagnosticSecurityAccessClass))

        child = parent.find("DIAGNOSTIC-SECURITY-ACCESS-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "SecAccessClass1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticSecurityAccessClass to a DIAGNOSTIC-SECURITY-ACCESS-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("SecAccessClasses")
        package.createDiagnosticSecurityAccessClass("SecAccessClass1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("SecAccessClass1", DiagnosticSecurityAccessClass))

        child = parent.find("DIAGNOSTIC-SECURITY-ACCESS-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "SecAccessClass1"

    def test_round_trip(self):
        """Test the full create → save → reload → assert cycle over an ARPackage."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("SecAccessClasses")
        package.createDiagnosticSecurityAccessClass("SecAccessClass1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            service_class_2 = package_2.getReferrableElement("SecAccessClass1", DiagnosticSecurityAccessClass)
            assert service_class_2 is not None
            assert service_class_2.getShortName() == "SecAccessClass1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
