"""
Tests for writing the (empty) DIAGNOSTIC-CONDITION-GROUP group —
DiagnosticConditionGroup, Table 4.193 (p.200, R23-11).

DiagnosticConditionGroup (spec marks it abstract) is the base of
DiagnosticEnableConditionGroup and DiagnosticStorageConditionGroup; its own XSD
group DIAGNOSTIC-CONDITION-GROUP (AUTOSAR_00052.xsd l.33439) is an empty
<xsd:sequence/> — the spec table carries no Attribute rows — embedded in each
concrete subclass element. There is no standalone DIAGNOSTIC-CONDITION-GROUP
element, so the writer is the named reusable helper writeDiagnosticConditionGroup
that the concrete subclass writers call (Rule 0001.7 abstract-XML-bearing-base
clause). The concrete subclasses are still unsynced stubs, so the tests drive
the helper directly through the stub subclass instances and assert the empty
wrapper emits no child elements.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_condition_group.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEnableConditionGroup
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticConditionGroup:
    """Tests for writeDiagnosticConditionGroup — own (empty) group emits no children (Table 4.193)."""

    def test_write_group_emits_no_children(self):
        """Test that writing the empty group emits no child element (empty wrapper case)."""
        parent = ET.Element("DIAGNOSTIC-ENABLE-CONDITION-GROUP")
        group = DiagnosticEnableConditionGroup(AUTOSAR.getInstance(), "Grp1")

        ARXMLWriter().writeDiagnosticConditionGroup(parent, group)

        assert [c.tag for c in parent] == []

    def test_round_trip_preserves_object(self):
        """Test the write → serialize → re-parse → read-back cycle leaves the group lossless."""
        group = DiagnosticEnableConditionGroup(AUTOSAR.getInstance(), "Grp1")

        parent = ET.Element("DIAGNOSTIC-ENABLE-CONDITION-GROUP", {"xmlns": NS})
        ARXMLWriter().writeDiagnosticConditionGroup(parent, group)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticEnableConditionGroup(AUTOSAR.getInstance(), "Grp1")
        element = ET.fromstring(xml_text)
        ARXMLParser().readDiagnosticConditionGroup(element, reloaded)
        assert reloaded.getShortName() == "Grp1"
