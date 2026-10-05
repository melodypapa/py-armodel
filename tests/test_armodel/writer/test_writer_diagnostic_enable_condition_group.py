"""
Tests for writing DIAGNOSTIC-ENABLE-CONDITION-GROUP elements —
DiagnosticEnableConditionGroup, Table 4.194 (p.200, R23-11).

DiagnosticEnableConditionGroup (Base most-derived DiagnosticConditionGroup) carries a
single Attribute row: enableCondition (DiagnosticEnableCondition, *, ref). The XSD
serializes it as the ENABLE-CONDITIONS wrapper (AUTOSAR_00052.xsd l.35542) holding
unbounded DIAGNOSTIC-ENABLE-CONDITION-REF-CONDITIONAL items, each with a
DIAGNOSTIC-ENABLE-CONDITION-REF — the RefConditional wrapper class is not modeled, so
the writer flattens enableConditionRefs through the wrapper path (precedent
writeBswModuleEntityIssuedTriggerRefs). The writer is writeDiagnosticEnableConditionGroup =
DIAGNOSTIC-ENABLE-CONDITION-GROUP subelement + writeIdentifiable +
writeDiagnosticConditionGroup + the enableConditionRefs flatten. The dispatch entry is
writeARPackageElement → writeDiagnosticEnableConditionGroup.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_enable_condition_group.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEnableConditionGroup
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


class TestWriteDiagnosticEnableConditionGroup:
    """Tests for writeDiagnosticEnableConditionGroup — own element field values (Table 4.194)."""

    def _enable_condition_ref(self, value: str) -> RefType:
        ref = RefType()
        ref.setDest("DIAGNOSTIC-ENABLE-CONDITION")
        ref.setValue(value)
        return ref

    def test_write_enable_condition_refs(self):
        """Test that set enableConditionRefs are emitted as ENABLE-CONDITIONS conditional refs with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticConditions")
        group = package.createDiagnosticEnableConditionGroup("EnableConditionGroup1")
        group.addEnableConditionRef(self._enable_condition_ref("/DiagnosticConditions/EnableCondition1"))
        group.addEnableConditionRef(self._enable_condition_ref("/DiagnosticConditions/EnableCondition2"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEnableConditionGroup(parent, group)

        child = parent.find("DIAGNOSTIC-ENABLE-CONDITION-GROUP")
        assert child is not None
        assert child.find("SHORT-NAME").text == "EnableConditionGroup1"
        wrapper = child.find("ENABLE-CONDITIONS")
        assert wrapper is not None
        conditionals = wrapper.findall("DIAGNOSTIC-ENABLE-CONDITION-REF-CONDITIONAL")
        assert len(conditionals) == 2
        ref1 = conditionals[0].find("DIAGNOSTIC-ENABLE-CONDITION-REF")
        assert ref1 is not None
        assert ref1.text == "/DiagnosticConditions/EnableCondition1"
        assert ref1.get("DEST") == "DIAGNOSTIC-ENABLE-CONDITION"
        ref2 = conditionals[1].find("DIAGNOSTIC-ENABLE-CONDITION-REF")
        assert ref2 is not None
        assert ref2.text == "/DiagnosticConditions/EnableCondition2"

    def test_write_unset_field_emits_no_wrapper(self):
        """Test that an unset enableConditionRefs emits no ENABLE-CONDITIONS child (empty wrapper case)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticConditions")
        package.createDiagnosticEnableConditionGroup("EnableConditionGroup1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEnableConditionGroup(parent, package.getReferrableElement("EnableConditionGroup1", DiagnosticEnableConditionGroup))

        child = parent.find("DIAGNOSTIC-ENABLE-CONDITION-GROUP")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("ENABLE-CONDITIONS") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticEnableConditionGroup to a DIAGNOSTIC-ENABLE-CONDITION-GROUP element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticConditions")
        group = package.createDiagnosticEnableConditionGroup("EnableConditionGroup1")
        group.addEnableConditionRef(self._enable_condition_ref("/DiagnosticConditions/EnableCondition1"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, group)

        child = parent.find("DIAGNOSTIC-ENABLE-CONDITION-GROUP")
        assert child is not None
        assert child.find("SHORT-NAME").text == "EnableConditionGroup1"
        assert child.find("ENABLE-CONDITIONS") is not None

    def test_round_trip_preserves_field_value(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticConditions")
        group = package.createDiagnosticEnableConditionGroup("EnableConditionGroup1")
        group.addEnableConditionRef(self._enable_condition_ref("/DiagnosticConditions/EnableCondition1"))
        group.addEnableConditionRef(self._enable_condition_ref("/DiagnosticConditions/EnableCondition2"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            group_2 = package_2.getReferrableElement("EnableConditionGroup1", DiagnosticEnableConditionGroup)
            assert group_2 is not None
            assert group_2.getShortName() == "EnableConditionGroup1"
            refs = group_2.getEnableConditionRefs()
            assert len(refs) == 2
            assert refs[0].getValue() == "/DiagnosticConditions/EnableCondition1"
            assert refs[0].getDest() == "DIAGNOSTIC-ENABLE-CONDITION"
            assert refs[1].getValue() == "/DiagnosticConditions/EnableCondition2"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticEnableConditionGroup without enableConditionRefs round-trips with an empty list."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticConditions")
        package.createDiagnosticEnableConditionGroup("EnableConditionGroup1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            group_2 = package_2.getReferrableElement("EnableConditionGroup1", DiagnosticEnableConditionGroup)
            assert group_2 is not None
            assert group_2.getEnableConditionRefs() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
