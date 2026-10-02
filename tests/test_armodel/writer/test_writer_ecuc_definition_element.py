"""
Tests for writing ECUC-DEFINITION-ELEMENT content —
EcucDefinitionElement, Table 2.6 (p.46, R23-11).

XSD group ECUC-DEFINITION-ELEMENT (AUTOSAR_00052.xsd l.51829) element order:
RELATED-TRACE-ITEM-REF, ECUC-VALIDATION-CONDS, ECUC-COND, LOWER-MULTIPLICITY,
UPPER-MULTIPLICITY, UPPER-MULTIPLICITY-INFINITE, SCOPE.

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_definition_element.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucConditionSpecification, EcucDefinitionElement, EcucScopeEnum, EcucValidationCondition
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
from armodel.writer.arxml_writer import ARXMLWriter


class _Concrete(EcucDefinitionElement):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucDefinitionElement:
    """Tests for writeEcucDefinitionElement — own element field values (Table 2.6)."""

    def _make(self):
        return _Concrete(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Holder")

    def test_write_empty(self):
        """Test that an EcucDefinitionElement without attributes emits only the IDENTIFIABLE content."""
        element = ET.Element("ECUC-VALIDATION-CONDITION")
        ARXMLWriter().writeEcucDefinitionElement(element, self._make())

        assert element.find("SHORT-NAME").text == "Holder"
        assert [c.tag for c in element] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        holder = self._make()
        holder.setRelatedTraceItemRef(RefType().setValue("/EcucId/Trace").setDest("TRACEABLE"))
        val_cond = EcucValidationCondition(AUTOSAR.getInstance(), "C1")
        holder.addEcucValidationCond(val_cond)
        ecuc_cond = EcucConditionSpecification()
        holder.setEcucCond(ecuc_cond)
        lower = PositiveInteger()
        lower.setValue("1")
        holder.setLowerMultiplicity(lower)
        upper = PositiveInteger()
        upper.setValue("4")
        holder.setUpperMultiplicity(upper)
        infinite = Boolean()
        infinite.setValue(True)
        holder.setUpperMultiplicityInfinite(infinite)
        holder.setScope(EcucScopeEnum().setValue(EcucScopeEnum.LOCAL))

        element = ET.Element("ECUC-VALIDATION-CONDITION")
        ARXMLWriter().writeEcucDefinitionElement(element, holder)

        assert [c.tag for c in element] == [
            "SHORT-NAME",
            "RELATED-TRACE-ITEM-REF",
            "ECUC-VALIDATION-CONDS",
            "ECUC-COND",
            "LOWER-MULTIPLICITY",
            "UPPER-MULTIPLICITY",
            "UPPER-MULTIPLICITY-INFINITE",
            "SCOPE",
        ]
        assert element.find("RELATED-TRACE-ITEM-REF").text == "/EcucId/Trace"
        assert element.find("LOWER-MULTIPLICITY").text == "1"
        assert element.find("UPPER-MULTIPLICITY").text == "4"
        assert element.find("UPPER-MULTIPLICITY-INFINITE").text == "true"
        assert element.find("SCOPE").text == "local"
