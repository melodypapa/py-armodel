"""
Tests for writing DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP-MAPPING elements —
DiagnosticFimAliasEventGroupMapping, Table 5.36 (p.263, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_fim_alias_event_group_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticFimAliasEventGroupMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticFimAliasEventGroupMapping:
    """Tests for writeDiagnosticFimAliasEventGroupMapping — own element field values (Table 5.36)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticFimAliasEventGroupMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticFimAliasEventGroupMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticFimAliasEventGroupMapping(parent, package.getReferrableElement("M1", DiagnosticFimAliasEventGroupMapping))

        child = parent.find("DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticFimAliasEventGroupMapping("M1")
        mapping.setActualEventRef(RefType().setValue("/AUTOSAR/ActualEvent1"))
        mapping.setAliasEventRef(RefType().setValue("/AUTOSAR/AliasEvent1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticFimAliasEventGroupMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "ACTUAL-EVENT-REF", "ALIAS-EVENT-REF"]
        assert child.find("ACTUAL-EVENT-REF").text == "/AUTOSAR/ActualEvent1"
        assert child.find("ALIAS-EVENT-REF").text == "/AUTOSAR/AliasEvent1"
