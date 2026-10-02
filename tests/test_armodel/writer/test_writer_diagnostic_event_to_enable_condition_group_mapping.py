"""
Tests for writing DIAGNOSTIC-EVENT-TO-ENABLE-CONDITION-GROUP-MAPPING elements —
DiagnosticEventToEnableConditionGroupMapping, Table 5.22 (p.247, R23-11).

DiagnosticEventToEnableConditionGroupMapping (Base most-derived DiagnosticMapping) owns 2 0..1 references
(diagnosticEventRef, enableConditionGroupRef), AUTOSAR_00052.xsd group DIAGNOSTIC-EVENT-TO-ENABLE-CONDITION-GROUP-MAPPING
l.36783.

Round-trip counterpart: tests/test_armodel/parser/test_diagnosticeventtoenableconditiongroupmapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventToEnableConditionGroupMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticEventToEnableConditionGroupMapping:
    """Tests for writeDiagnosticEventToEnableConditionGroupMapping — own element field values (Table 5.22)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticEventToEnableConditionGroupMapping without references emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticEventToEnableConditionGroupMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventToEnableConditionGroupMapping(parent, package.getReferrableElement("M1", DiagnosticEventToEnableConditionGroupMapping))

        child = parent.find("DIAGNOSTIC-EVENT-TO-ENABLE-CONDITION-GROUP-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_refs_in_xsd_order(self):
        """Test that all references are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticEventToEnableConditionGroupMapping("M1")
        mapping.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1").setDest("DEST"))
        mapping.setEnableConditionGroupRef(RefType().setValue("/AUTOSAR/EnableConditionGroup1").setDest("DEST"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventToEnableConditionGroupMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-EVENT-TO-ENABLE-CONDITION-GROUP-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "DIAGNOSTIC-EVENT-REF", "ENABLE-CONDITION-GROUP-REF"]
        assert child.find("DIAGNOSTIC-EVENT-REF").text == "/AUTOSAR/DiagnosticEvent1"
        assert child.find("ENABLE-CONDITION-GROUP-REF").text == "/AUTOSAR/EnableConditionGroup1"
