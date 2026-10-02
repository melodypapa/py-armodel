"""
Tests for writing DIAGNOSTIC-FIM-ALIAS-EVENT-MAPPING elements —
DiagnosticFimAliasEventMapping, Table 5.34 (p.262, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_fim_alias_event_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticFimAliasEventMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticFimAliasEventMapping:
    """Tests for writeDiagnosticFimAliasEventMapping — own element field values (Table 5.34)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticFimAliasEventMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticFimAliasEventMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticFimAliasEventMapping(parent, package.getElement("M1", DiagnosticFimAliasEventMapping))

        child = parent.find("DIAGNOSTIC-FIM-ALIAS-EVENT-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticFimAliasEventMapping("M1")
        mapping.setActualEventRef(RefType().setValue("/AUTOSAR/ActualEvent1"))
        mapping.setAliasEventRef(RefType().setValue("/AUTOSAR/AliasEvent1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticFimAliasEventMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-FIM-ALIAS-EVENT-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "ACTUAL-EVENT-REF", "ALIAS-EVENT-REF"]
        assert child.find("ACTUAL-EVENT-REF").text == "/AUTOSAR/ActualEvent1"
        assert child.find("ALIAS-EVENT-REF").text == "/AUTOSAR/AliasEvent1"
