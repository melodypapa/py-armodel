"""
Tests for writing DIAGNOSTIC-AUTH-ROLE elements —
DiagnosticAuthRole, Table 4.34 (p.77, R23-11).

DiagnosticAuthRole (Base most-derived ARElement) carries two 0..1 attr
attributes — BIT-POSITION (PositiveInteger) and IS-DEFAULT (Boolean) — XSD group
DIAGNOSTIC-AUTH-ROLE, AUTOSAR_00052.xsd l.31670. The writer reads the model via
the get* getters; the dispatch entry is writeARPackageElement →
writeDiagnosticAuthRole.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_auth_role.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticAuthRole
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


def _bit_position(value: str) -> PositiveInteger:
    bit_position = PositiveInteger()
    bit_position.setValue(value)
    return bit_position


def _is_default(value: bool) -> Boolean:
    is_default = Boolean()
    is_default.setValue(value)
    return is_default


class TestWriteDiagnosticAuthRole:
    """Tests for writeDiagnosticAuthRole — own element field values (Table 4.34)."""

    def test_write_field_values_in_xsd_order(self):
        """Test that BIT-POSITION and IS-DEFAULT are emitted with field values in XSD order."""
        package = AUTOSAR.getInstance().createARPackage("AuthRoles")
        auth_role = package.createDiagnosticAuthRole("Role1")
        auth_role.setBitPosition(_bit_position("7"))
        auth_role.setIsDefault(_is_default(True))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAuthRole(parent, auth_role)

        child = parent.find("DIAGNOSTIC-AUTH-ROLE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Role1"
        assert child.find("BIT-POSITION").text == "7"
        assert child.find("IS-DEFAULT").text == "true"
        tags = [c.tag for c in child if c.tag != "SHORT-NAME"]
        assert tags == ["BIT-POSITION", "IS-DEFAULT"]

    def test_write_unset_fields_omits_tags(self):
        """Test that unset fields emit no elements beyond SHORT-NAME."""
        package = AUTOSAR.getInstance().createARPackage("AuthRoles")
        package.createDiagnosticAuthRole("Role1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAuthRole(parent, package.getReferrableElement("Role1", DiagnosticAuthRole))

        child = parent.find("DIAGNOSTIC-AUTH-ROLE")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("BIT-POSITION") is None
        assert child.find("IS-DEFAULT") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticAuthRole to a DIAGNOSTIC-AUTH-ROLE element."""
        package = AUTOSAR.getInstance().createARPackage("AuthRoles")
        auth_role = package.createDiagnosticAuthRole("Role1")
        auth_role.setBitPosition(_bit_position("7"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, auth_role)

        child = parent.find("DIAGNOSTIC-AUTH-ROLE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Role1"
        assert child.find("BIT-POSITION").text == "7"

    def test_round_trip(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("AuthRoles")
        auth_role = package.createDiagnosticAuthRole("Role1")
        auth_role.setBitPosition(_bit_position("7"))
        auth_role.setIsDefault(_is_default(True))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            auth_role_2 = package_2.getReferrableElement("Role1", DiagnosticAuthRole)
            assert auth_role_2 is not None
            assert auth_role_2.getBitPosition() is not None
            assert auth_role_2.getBitPosition().getValue() == 7
            assert auth_role_2.getIsDefault() is not None
            assert auth_role_2.getIsDefault().getValue() is True
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticAuthRole without field values round-trips with all fields empty."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("AuthRoles")
        package.createDiagnosticAuthRole("Role1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            auth_role_2 = package_2.getReferrableElement("Role1", DiagnosticAuthRole)
            assert auth_role_2 is not None
            assert auth_role_2.getBitPosition() is None
            assert auth_role_2.getIsDefault() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
