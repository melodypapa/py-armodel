"""
Tests for writing DIAGNOSTIC-DE-AUTHENTICATION elements —
DiagnosticDeAuthentication, Table 4.56 (p.100, R23-11).

DiagnosticDeAuthentication (Base most-derived
DiagnosticAuthentication) defines no attributes of its own (Table 4.56
attribute row is "-") — it inherits the 0..1 authenticationClass ref
(AUTHENTICATION-CLASS-REF) from the abstract DiagnosticAuthentication
(Table 4.51); the wire element is an IDENTIFIABLE wrapper plus the inherited
group, AUTOSAR_00052.xsd complexType DIAGNOSTIC-DE-AUTHENTICATION
l.34659. The writer delegates the inherited field to the Rule 0001.7 helper
writeDiagnosticAuthentication and the dispatch entry is
writeARPackageElement → writeDiagnosticDeAuthentication.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_de_authentication.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDeAuthentication
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticDeAuthentication:
    """Tests for writeDiagnosticDeAuthentication — own element field values (Table 4.56)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticDeAuthentication without refs emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DeAuthentications")
        package.createDiagnosticDeAuthentication("DeAuth1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDeAuthentication(parent, package.getReferrableElement("DeAuth1", DiagnosticDeAuthentication))

        child = parent.find("DIAGNOSTIC-DE-AUTHENTICATION")
        assert child is not None
        assert child.find("SHORT-NAME").text == "DeAuth1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_authentication_class_ref(self):
        """Test that the inherited AUTHENTICATION-CLASS-REF is emitted with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DeAuthentications")
        de_authentication = package.createDiagnosticDeAuthentication("DeAuth1")
        ref = RefType()
        ref.setDest("DIAGNOSTIC-AUTHENTICATION-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass")
        de_authentication.setAuthenticationClass(ref)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDeAuthentication(parent, de_authentication)

        child = parent.find("DIAGNOSTIC-DE-AUTHENTICATION")
        assert child is not None
        ref_element = child.find("AUTHENTICATION-CLASS-REF")
        assert ref_element is not None
        assert ref_element.text == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert ref_element.get("DEST") == "DIAGNOSTIC-AUTHENTICATION-CLASS"

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticDeAuthentication to a DIAGNOSTIC-DE-AUTHENTICATION element."""
        package = AUTOSAR.getInstance().createARPackage("DeAuthentications")
        package.createDiagnosticDeAuthentication("DeAuth1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("DeAuth1", DiagnosticDeAuthentication))

        child = parent.find("DIAGNOSTIC-DE-AUTHENTICATION")
        assert child is not None
        assert child.find("SHORT-NAME").text == "DeAuth1"

    def test_round_trip(self):
        """Test the full create → save → reload → assert cycle over an ARPackage."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DeAuthentications")
        de_authentication = package.createDiagnosticDeAuthentication("DeAuth1")
        ref = RefType()
        ref.setDest("DIAGNOSTIC-AUTHENTICATION-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass")
        de_authentication.setAuthenticationClass(ref)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            de_authentication_2 = package_2.getReferrableElement("DeAuth1", DiagnosticDeAuthentication)
            assert de_authentication_2 is not None
            assert de_authentication_2.getShortName() == "DeAuth1"
            ref_2 = de_authentication_2.getAuthenticationClass()
            assert ref_2 is not None
            assert ref_2.getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
            assert ref_2.getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
