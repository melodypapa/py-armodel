"""
Tests for writing DIAGNOSTIC-STORAGE-CONDITION-GROUP elements —
DiagnosticStorageConditionGroup, Table 4.195 (p.200, R23-11).

DiagnosticStorageConditionGroup (Base most-derived DiagnosticConditionGroup) carries a
single Attribute row: storageCondition (DiagnosticStorageCondition, *, ref). The XSD
serializes it as the STORAGE-CONDITIONS wrapper (AUTOSAR_00052.xsd l.45675) holding
unbounded DIAGNOSTIC-STORAGE-CONDITION-REF-CONDITIONAL items, each with a
DIAGNOSTIC-STORAGE-CONDITION-REF — the RefConditional wrapper class is not modeled, so
the writer flattens storageConditionRefs through the wrapper path (precedent
writeBswModuleEntityIssuedTriggerRefs). The writer is writeDiagnosticStorageConditionGroup =
DIAGNOSTIC-STORAGE-CONDITION-GROUP subelement + writeIdentifiable +
writeDiagnosticConditionGroup + the storageConditionRefs flatten. The dispatch entry is
writeARPackageElement → writeDiagnosticStorageConditionGroup.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_storage_condition_group.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticStorageConditionGroup
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset the AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticStorageConditionGroup:
    """Tests for writeDiagnosticStorageConditionGroup — own element field values (Table 4.195)."""

    def _storage_condition_ref(self, value: str) -> RefType:
        ref = RefType()
        ref.setDest("DIAGNOSTIC-STORAGE-CONDITION")
        ref.setValue(value)
        return ref

    def test_write_storage_condition_refs(self):
        """Test that set storageConditionRefs are emitted as STORAGE-CONDITIONS conditional refs with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticConditions")
        group = package.createDiagnosticStorageConditionGroup("StorageConditionGroup1")
        group.addStorageConditionRef(self._storage_condition_ref("/DiagnosticConditions/StorageCondition1"))
        group.addStorageConditionRef(self._storage_condition_ref("/DiagnosticConditions/StorageCondition2"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticStorageConditionGroup(parent, group)

        child = parent.find("DIAGNOSTIC-STORAGE-CONDITION-GROUP")
        assert child is not None
        assert child.find("SHORT-NAME").text == "StorageConditionGroup1"
        wrapper = child.find("STORAGE-CONDITIONS")
        assert wrapper is not None
        conditionals = wrapper.findall("DIAGNOSTIC-STORAGE-CONDITION-REF-CONDITIONAL")
        assert len(conditionals) == 2
        ref1 = conditionals[0].find("DIAGNOSTIC-STORAGE-CONDITION-REF")
        assert ref1 is not None
        assert ref1.text == "/DiagnosticConditions/StorageCondition1"
        assert ref1.get("DEST") == "DIAGNOSTIC-STORAGE-CONDITION"
        ref2 = conditionals[1].find("DIAGNOSTIC-STORAGE-CONDITION-REF")
        assert ref2 is not None
        assert ref2.text == "/DiagnosticConditions/StorageCondition2"

    def test_write_unset_field_emits_no_wrapper(self):
        """Test that an unset storageConditionRefs emits no STORAGE-CONDITIONS child (empty wrapper case)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticConditions")
        package.createDiagnosticStorageConditionGroup("StorageConditionGroup1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticStorageConditionGroup(parent, package.getReferrableElement("StorageConditionGroup1", DiagnosticStorageConditionGroup))

        child = parent.find("DIAGNOSTIC-STORAGE-CONDITION-GROUP")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("STORAGE-CONDITIONS") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticStorageConditionGroup to a DIAGNOSTIC-STORAGE-CONDITION-GROUP element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticConditions")
        group = package.createDiagnosticStorageConditionGroup("StorageConditionGroup1")
        group.addStorageConditionRef(self._storage_condition_ref("/DiagnosticConditions/StorageCondition1"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, group)

        child = parent.find("DIAGNOSTIC-STORAGE-CONDITION-GROUP")
        assert child is not None
        assert child.find("SHORT-NAME").text == "StorageConditionGroup1"
        assert child.find("STORAGE-CONDITIONS") is not None

    def test_round_trip_preserves_field_value(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticConditions")
        group = package.createDiagnosticStorageConditionGroup("StorageConditionGroup1")
        group.addStorageConditionRef(self._storage_condition_ref("/DiagnosticConditions/StorageCondition1"))
        group.addStorageConditionRef(self._storage_condition_ref("/DiagnosticConditions/StorageCondition2"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            group_2 = package_2.getReferrableElement("StorageConditionGroup1", DiagnosticStorageConditionGroup)
            assert group_2 is not None
            assert group_2.getShortName() == "StorageConditionGroup1"
            refs = group_2.getStorageConditionRefs()
            assert len(refs) == 2
            assert refs[0].getValue() == "/DiagnosticConditions/StorageCondition1"
            assert refs[0].getDest() == "DIAGNOSTIC-STORAGE-CONDITION"
            assert refs[1].getValue() == "/DiagnosticConditions/StorageCondition2"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticStorageConditionGroup without storageConditionRefs round-trips with an empty list."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticConditions")
        package.createDiagnosticStorageConditionGroup("StorageConditionGroup1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            group_2 = package_2.getReferrableElement("StorageConditionGroup1", DiagnosticStorageConditionGroup)
            assert group_2 is not None
            assert group_2.getStorageConditionRefs() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
