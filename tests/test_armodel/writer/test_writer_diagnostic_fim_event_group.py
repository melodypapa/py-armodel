"""
Tests for writing DIAGNOSTIC-FIM-EVENT-GROUP elements —
DiagnosticFimEventGroup, Table 4.218 (p.217, R23-11).

DiagnosticFimEventGroup (Base most-derived DiagnosticCommonElement) owns the
0..* event multi-reference (EVENT-REFS/EVENT-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-FIM-EVENT-GROUP l.37639.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_fim_event_group.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticFimEventGroup
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticFimEventGroup:
    """Tests for writeDiagnosticFimEventGroup — own element field values (Table 4.218)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticFimEventGroup without refs emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticFimEventGroups")
        package.createDiagnosticFimEventGroup("FimGroup1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticFimEventGroup(parent, package.getReferrableElement("FimGroup1", DiagnosticFimEventGroup))

        child = parent.find("DIAGNOSTIC-FIM-EVENT-GROUP")
        assert child is not None
        assert child.find("SHORT-NAME").text == "FimGroup1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_event_refs(self):
        """Test that the event multi-reference is emitted under EVENT-REFS with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticFimEventGroups")
        fim_event_group = package.createDiagnosticFimEventGroup("FimGroup1")
        ref1 = RefType()
        ref1.setDest("DIAGNOSTIC-EVENT")
        ref1.setValue("/AUTOSAR/DiagEvents/Evt1")
        ref2 = RefType()
        ref2.setDest("DIAGNOSTIC-EVENT")
        ref2.setValue("/AUTOSAR/DiagEvents/Evt2")
        fim_event_group.addEventRef(ref1)
        fim_event_group.addEventRef(ref2)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticFimEventGroup(parent, fim_event_group)

        child = parent.find("DIAGNOSTIC-FIM-EVENT-GROUP")
        refs_tag = child.find("EVENT-REFS")
        assert refs_tag is not None
        refs = refs_tag.findall("EVENT-REF")
        assert len(refs) == 2
        assert refs[0].text == "/AUTOSAR/DiagEvents/Evt1"
        assert refs[0].attrib["DEST"] == "DIAGNOSTIC-EVENT"
        assert refs[1].text == "/AUTOSAR/DiagEvents/Evt2"
        assert refs[1].attrib["DEST"] == "DIAGNOSTIC-EVENT"
