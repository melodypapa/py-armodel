"""
Tests for writing DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP elements —
DiagnosticFimAliasEventGroup, Table 5.35 (p.263, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_fim_alias_event_group.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticFimAliasEventGroup
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticFimAliasEventGroup:
    """Tests for writeDiagnosticFimAliasEventGroup — own element field values (Table 5.35)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticFimAliasEventGroup without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticFimAliasEventGroup("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticFimAliasEventGroup(parent, package.getElement("M1", DiagnosticFimAliasEventGroup))

        child = parent.find("DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticFimAliasEventGroup("M1")
        mapping.addGroupedAliasEventRef(RefType().setValue("/AUTOSAR/GroupedAliasEvent1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticFimAliasEventGroup(parent, mapping)

        child = parent.find("DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP")
        assert [c.tag for c in child] == ["SHORT-NAME", "GROUPED-ALIAS-EVENT-REFS"]
        assert child.find("GROUPED-ALIAS-EVENT-REFS/GROUPED-ALIAS-EVENT-REF").text == "/AUTOSAR/GroupedAliasEvent1"
