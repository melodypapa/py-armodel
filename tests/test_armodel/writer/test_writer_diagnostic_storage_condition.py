"""
Tests for writing DIAGNOSTIC-STORAGE-CONDITION elements —
DiagnosticStorageCondition, Table 4.186 (p.194, R23-11).

DiagnosticStorageCondition (Base most-derived DiagnosticCondition) carries no own
Attribute rows — its XSD group DIAGNOSTIC-STORAGE-CONDITION (AUTOSAR_00052.xsd
l.45629) is an empty sequence and the INIT-VALUE child comes from the base group
DIAGNOSTIC-CONDITION (l.33411), so the writer is writeDiagnosticStorageCondition =
DIAGNOSTIC-STORAGE-CONDITION subelement + writeIdentifiable + writeDiagnosticCondition.
The dispatch entry is writeARPackageElement → writeDiagnosticStorageCondition.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_storage_condition.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticStorageCondition
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


class TestWriteDiagnosticStorageCondition:
    """Tests for writeDiagnosticStorageCondition — own element field values (Table 4.186)."""

    def test_write_init_value(self):
        """Test that a set initValue is emitted as the INIT-VALUE child with the spec value."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticConditions")
        storage_condition = package.createDiagnosticStorageCondition("StorageCondition1")
        storage_condition.setInitValue(Boolean().setValue("true"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticStorageCondition(parent, storage_condition)

        child = parent.find("DIAGNOSTIC-STORAGE-CONDITION")
        assert child is not None
        assert child.find("SHORT-NAME").text == "StorageCondition1"
        assert child.find("INIT-VALUE").text == "true"

    def test_write_unset_field_emits_no_init_value(self):
        """Test that an unset initValue emits no INIT-VALUE child (empty wrapper case)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticConditions")
        package.createDiagnosticStorageCondition("StorageCondition1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticStorageCondition(parent, package.getReferrableElement("StorageCondition1", DiagnosticStorageCondition))

        child = parent.find("DIAGNOSTIC-STORAGE-CONDITION")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("INIT-VALUE") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticStorageCondition to a DIAGNOSTIC-STORAGE-CONDITION element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticConditions")
        storage_condition = package.createDiagnosticStorageCondition("StorageCondition1")
        storage_condition.setInitValue(Boolean().setValue("false"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, storage_condition)

        child = parent.find("DIAGNOSTIC-STORAGE-CONDITION")
        assert child is not None
        assert child.find("SHORT-NAME").text == "StorageCondition1"
        assert child.find("INIT-VALUE").text == "false"

    def test_round_trip_preserves_field_value(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticConditions")
        storage_condition = package.createDiagnosticStorageCondition("StorageCondition1")
        storage_condition.setInitValue(Boolean().setValue("true"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            storage_condition_2 = package_2.getReferrableElement("StorageCondition1", DiagnosticStorageCondition)
            assert storage_condition_2 is not None
            assert storage_condition_2.getShortName() == "StorageCondition1"
            assert storage_condition_2.getInitValue() is not None
            assert storage_condition_2.getInitValue().value is True
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticStorageCondition without initValue round-trips with None."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticConditions")
        package.createDiagnosticStorageCondition("StorageCondition1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            storage_condition_2 = package_2.getReferrableElement("StorageCondition1", DiagnosticStorageCondition)
            assert storage_condition_2 is not None
            assert storage_condition_2.getInitValue() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
