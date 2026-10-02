"""
Tests for writing DIAGNOSTIC-EVENT-TO-STORAGE-CONDITION-GROUP-MAPPING elements —
DiagnosticEventToStorageConditionGroupMapping, Table 5.23 (p.248, R23-11).

DiagnosticEventToStorageConditionGroupMapping (Base most-derived DiagnosticMapping) owns 2 0..1 references
(diagnosticEventRef, storageConditionGroupRef), AUTOSAR_00052.xsd group DIAGNOSTIC-EVENT-TO-STORAGE-CONDITION-GROUP-MAPPING
l.36957.

Round-trip counterpart: tests/test_armodel/parser/test_diagnosticeventtostorageconditiongroupmapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventToStorageConditionGroupMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticEventToStorageConditionGroupMapping:
    """Tests for writeDiagnosticEventToStorageConditionGroupMapping — own element field values (Table 5.23)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticEventToStorageConditionGroupMapping without references emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticEventToStorageConditionGroupMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventToStorageConditionGroupMapping(parent, package.getElement("M1", DiagnosticEventToStorageConditionGroupMapping))

        child = parent.find("DIAGNOSTIC-EVENT-TO-STORAGE-CONDITION-GROUP-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_refs_in_xsd_order(self):
        """Test that all references are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticEventToStorageConditionGroupMapping("M1")
        mapping.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1").setDest("DEST"))
        mapping.setStorageConditionGroupRef(RefType().setValue("/AUTOSAR/StorageConditionGroup1").setDest("DEST"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventToStorageConditionGroupMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-EVENT-TO-STORAGE-CONDITION-GROUP-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "DIAGNOSTIC-EVENT-REF", "STORAGE-CONDITION-GROUP-REF"]
        assert child.find("DIAGNOSTIC-EVENT-REF").text == "/AUTOSAR/DiagnosticEvent1"
        assert child.find("STORAGE-CONDITION-GROUP-REF").text == "/AUTOSAR/StorageConditionGroup1"
