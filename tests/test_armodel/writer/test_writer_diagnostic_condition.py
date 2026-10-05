"""
Tests for writing the INIT-VALUE element of the DIAGNOSTIC-CONDITION group —
DiagnosticCondition, Table 4.184 (p.194, R23-11).

DiagnosticCondition (spec marks it abstract) is the base of
DiagnosticEnableCondition and DiagnosticStorageCondition; its own XSD group
DIAGNOSTIC-CONDITION (AUTOSAR_00052.xsd l.33411) carries the single 0..1 element
INIT-VALUE, embedded in each concrete subclass element. There is no standalone
DIAGNOSTIC-CONDITION element, so the writer is the named reusable helper
writeDiagnosticCondition that the concrete subclass writers call
(Rule 0001.7 abstract-XML-bearing-base clause). The concrete subclasses are
still unsynced stubs, so the tests drive the helper directly through the stub
subclass instances.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_condition.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEnableCondition
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticCondition:
    """Tests for writeDiagnosticCondition — own group field values (Table 4.184)."""

    def test_write_init_value(self):
        """Test that a set initValue is emitted as the single INIT-VALUE child with the spec value."""
        parent = ET.Element("DIAGNOSTIC-ENABLE-CONDITION")
        condition = DiagnosticEnableCondition(AUTOSAR.getInstance(), "Cond1")
        condition.setInitValue(Boolean().setValue("true"))

        ARXMLWriter().writeDiagnosticCondition(parent, condition)

        assert [c.tag for c in parent] == ["INIT-VALUE"]
        assert parent.find("INIT-VALUE").text == "true"

    def test_write_unset_field_emits_no_child(self):
        """Test that an unset initValue emits no child element (empty wrapper case)."""
        parent = ET.Element("DIAGNOSTIC-ENABLE-CONDITION")
        condition = DiagnosticEnableCondition(AUTOSAR.getInstance(), "Cond1")

        ARXMLWriter().writeDiagnosticCondition(parent, condition)

        assert [c.tag for c in parent] == []

    def test_round_trip_preserves_field_value(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the initValue."""
        condition = DiagnosticEnableCondition(AUTOSAR.getInstance(), "Cond1")
        condition.setInitValue(Boolean().setValue("false"))

        parent = ET.Element("DIAGNOSTIC-ENABLE-CONDITION", {"xmlns": NS})
        ARXMLWriter().writeDiagnosticCondition(parent, condition)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticEnableCondition(AUTOSAR.getInstance(), "Cond1")
        element = ET.fromstring(xml_text)
        ARXMLParser().readDiagnosticCondition(element, reloaded)
        assert reloaded.getInitValue() is not None
        assert reloaded.getInitValue().value is False
