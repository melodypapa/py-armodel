"""
Tests for writing DIAGNOSTIC-INHIBIT-SOURCE-EVENT-MAPPING elements —
DiagnosticInhibitSourceEventMapping, Table 5.33 (p.261, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_inhibit_source_event_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticInhibitSourceEventMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticInhibitSourceEventMapping:
    """Tests for writeDiagnosticInhibitSourceEventMapping — own element field values (Table 5.33)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticInhibitSourceEventMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticInhibitSourceEventMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticInhibitSourceEventMapping(parent, package.getReferrableElement("M1", DiagnosticInhibitSourceEventMapping))

        child = parent.find("DIAGNOSTIC-INHIBIT-SOURCE-EVENT-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticInhibitSourceEventMapping("M1")
        mapping.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1"))
        mapping.setEventGroupRef(RefType().setValue("/AUTOSAR/EventGroup1"))
        mapping.setInhibitionSourceRef(RefType().setValue("/AUTOSAR/InhibitionSource1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticInhibitSourceEventMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-INHIBIT-SOURCE-EVENT-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "DIAGNOSTIC-EVENT-REF", "EVENT-GROUP-REF", "INHIBITION-SOURCE-REF"]
        assert child.find("DIAGNOSTIC-EVENT-REF").text == "/AUTOSAR/DiagnosticEvent1"
        assert child.find("EVENT-GROUP-REF").text == "/AUTOSAR/EventGroup1"
        assert child.find("INHIBITION-SOURCE-REF").text == "/AUTOSAR/InhibitionSource1"
