"""
Tests for writing DIAGNOSTIC-ENABLE-CONDITION elements —
DiagnosticEnableCondition, Table 4.185 (p.194, R23-11).

DiagnosticEnableCondition (Base most-derived DiagnosticCondition) carries no own
Attribute rows — its XSD group DIAGNOSTIC-ENABLE-CONDITION (AUTOSAR_00052.xsd
l.35506) is an empty sequence and the INIT-VALUE child comes from the base group
DIAGNOSTIC-CONDITION (l.33411), so the writer is writeDiagnosticEnableCondition =
DIAGNOSTIC-ENABLE-CONDITION subelement + writeIdentifiable + writeDiagnosticCondition.
The dispatch entry is writeARPackageElement → writeDiagnosticEnableCondition.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_enable_condition.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEnableCondition
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset the AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticEnableCondition:
    """Tests for writeDiagnosticEnableCondition — own element field values (Table 4.185)."""

    def test_write_init_value(self):
        """Test that a set initValue is emitted as the INIT-VALUE child with the spec value."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticConditions")
        enable_condition = package.createDiagnosticEnableCondition("EnableCondition1")
        enable_condition.setInitValue(Boolean().setValue("true"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEnableCondition(parent, enable_condition)

        child = parent.find("DIAGNOSTIC-ENABLE-CONDITION")
        assert child is not None
        assert child.find("SHORT-NAME").text == "EnableCondition1"
        assert child.find("INIT-VALUE").text == "true"

    def test_write_unset_field_emits_no_init_value(self):
        """Test that an unset initValue emits no INIT-VALUE child (empty wrapper case)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticConditions")
        package.createDiagnosticEnableCondition("EnableCondition1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEnableCondition(parent, package.getReferrableElement("EnableCondition1", DiagnosticEnableCondition))

        child = parent.find("DIAGNOSTIC-ENABLE-CONDITION")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("INIT-VALUE") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticEnableCondition to a DIAGNOSTIC-ENABLE-CONDITION element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticConditions")
        enable_condition = package.createDiagnosticEnableCondition("EnableCondition1")
        enable_condition.setInitValue(Boolean().setValue("false"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, enable_condition)

        child = parent.find("DIAGNOSTIC-ENABLE-CONDITION")
        assert child is not None
        assert child.find("SHORT-NAME").text == "EnableCondition1"
        assert child.find("INIT-VALUE").text == "false"

    def test_round_trip_preserves_field_value(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticConditions")
        enable_condition = package.createDiagnosticEnableCondition("EnableCondition1")
        enable_condition.setInitValue(Boolean().setValue("true"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            enable_condition_2 = package_2.getReferrableElement("EnableCondition1", DiagnosticEnableCondition)
            assert enable_condition_2 is not None
            assert enable_condition_2.getShortName() == "EnableCondition1"
            assert enable_condition_2.getInitValue() is not None
            assert enable_condition_2.getInitValue().value is True
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticEnableCondition without initValue round-trips with None."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticConditions")
        package.createDiagnosticEnableCondition("EnableCondition1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            enable_condition_2 = package_2.getReferrableElement("EnableCondition1", DiagnosticEnableCondition)
            assert enable_condition_2 is not None
            assert enable_condition_2.getInitValue() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
