"""
Tests for writing DIAGNOSTIC-ENV-MODE-CONDITION elements —
DiagnosticEnvModeCondition, Table 4.43 (p.89, R23-11).

DiagnosticEnvModeCondition (Base most-derived DiagnosticEnvCompareCondition)
carries the inherited COMPARE-TYPE plus its own 0..1 MODE-ELEMENT-REF
(DEST DIAGNOSTIC-ENV-MODE-ELEMENT--SUBTYPES-ENUM) — XSD group
DIAGNOSTIC-ENV-MODE-CONDITION, AUTOSAR_00052.xsd l.36015. The writer reads the
model via the get* getters; the dispatch entries are
writeDiagnosticEnvConditionFormula (PARTS loop) → writeDiagnosticEnvModeCondition.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_env_mode_condition.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import (
    DiagnosticCompareTypeEnum,
    DiagnosticEnvConditionFormula,
    DiagnosticEnvModeCondition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _positive_integer(value: str) -> PositiveInteger:
    nrc_value = PositiveInteger()
    nrc_value.setValue(value)
    return nrc_value


class TestWriteDiagnosticEnvModeCondition:
    """Tests for writeDiagnosticEnvModeCondition — own element field values (Table 4.43)."""

    def test_write_field_values_in_xsd_order(self):
        """Test that COMPARE-TYPE (inherited) and MODE-ELEMENT-REF are emitted with field values in XSD order."""
        condition = DiagnosticEnvModeCondition()
        condition.setCompareType(DiagnosticCompareTypeEnum().setValue(DiagnosticCompareTypeEnum.IS_EQUAL))
        condition.setModeElementRef(_ref("DIAGNOSTIC-ENV-BSW-MODE-ELEMENT", "/AUTOSAR/DiagEnvConditions/Env1/ModeElements/BswMode1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEnvModeCondition(parent, condition)

        child = parent.find("DIAGNOSTIC-ENV-MODE-CONDITION")
        assert child is not None
        assert child.find("COMPARE-TYPE").text == "IS-EQUAL"
        mode_element_ref = child.find("MODE-ELEMENT-REF")
        assert mode_element_ref.attrib["DEST"] == "DIAGNOSTIC-ENV-BSW-MODE-ELEMENT"
        assert mode_element_ref.text == "/AUTOSAR/DiagEnvConditions/Env1/ModeElements/BswMode1"
        tags = [c.tag for c in child]
        assert tags == ["COMPARE-TYPE", "MODE-ELEMENT-REF"]

    def test_write_unset_fields_omits_tags(self):
        """Test that unset fields emit an empty DIAGNOSTIC-ENV-MODE-CONDITION element."""
        condition = DiagnosticEnvModeCondition()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEnvModeCondition(parent, condition)

        child = parent.find("DIAGNOSTIC-ENV-MODE-CONDITION")
        assert child is not None
        assert len(list(child)) == 0
        assert child.find("COMPARE-TYPE") is None
        assert child.find("MODE-ELEMENT-REF") is None

    def test_formula_parts_dispatch_writes_element(self):
        """Test that the formula PARTS loop dispatches a DiagnosticEnvModeCondition part to a DIAGNOSTIC-ENV-MODE-CONDITION element."""
        formula = DiagnosticEnvConditionFormula()
        condition = DiagnosticEnvModeCondition()
        condition.setCompareType(DiagnosticCompareTypeEnum().setValue(DiagnosticCompareTypeEnum.IS_NOT_EQUAL))
        condition.setModeElementRef(_ref("DIAGNOSTIC-ENV-SWC-MODE-ELEMENT", "/AUTOSAR/DiagEnvConditions/Env1/ModeElements/SwcMode1"))
        formula.addPart(condition)

        parent = ET.Element("DIAGNOSTIC-ENV-CONDITION-FORMULA")
        ARXMLWriter().writeDiagnosticEnvConditionFormula(parent, formula)

        parts = parent.find("PARTS")
        assert parts is not None
        part = parts.find("DIAGNOSTIC-ENV-MODE-CONDITION")
        assert part is not None
        assert part.find("COMPARE-TYPE").text == "IS-NOT-EQUAL"
        assert part.find("MODE-ELEMENT-REF").text == "/AUTOSAR/DiagEnvConditions/Env1/ModeElements/SwcMode1"

    def test_round_trip(self):
        """Test the full build → save → reload → assert cycle over a DiagnosticEnvironmentalCondition with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("EnvConds")
        env_condition = package.createDiagnosticEnvironmentalCondition("Env1")
        formula = DiagnosticEnvConditionFormula()
        formula.setNrcValue(_positive_integer("49"))
        condition = DiagnosticEnvModeCondition()
        condition.setCompareType(DiagnosticCompareTypeEnum().setValue(DiagnosticCompareTypeEnum.IS_EQUAL))
        condition.setModeElementRef(_ref("DIAGNOSTIC-ENV-BSW-MODE-ELEMENT", "/AUTOSAR/DiagEnvConditions/Env1/ModeElements/BswMode1"))
        formula.addPart(condition)
        env_condition.setFormula(formula)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            env_condition_2 = package_2.getReferrableElement("Env1", type(env_condition))
            assert env_condition_2 is not None
            formula_2 = env_condition_2.getFormula()
            assert formula_2 is not None
            assert formula_2.getNrcValue().getValue() == 49
            parts = formula_2.getParts()
            assert len(parts) == 1
            part = parts[0]
            assert type(part).__name__ == "DiagnosticEnvModeCondition"
            assert part.getCompareType().getValue() == "isEqual"
            assert part.getModeElementRef() is not None
            assert part.getModeElementRef().getDest() == "DIAGNOSTIC-ENV-BSW-MODE-ELEMENT"
            assert part.getModeElementRef().getValue() == "/AUTOSAR/DiagEnvConditions/Env1/ModeElements/BswMode1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
