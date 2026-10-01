"""
Tests for writing DIAGNOSTIC-ENV-DATA-CONDITION elements —
DiagnosticEnvDataCondition, Table 4.41 (p.84, R23-11).

DiagnosticEnvDataCondition (Base most-derived DiagnosticEnvCompareCondition)
carries the inherited COMPARE-TYPE plus its own 0..1 COMPARE-VALUE (choice of 12
ValueSpecification alternatives) and 0..1 DATA-ELEMENT-REF — XSD group
DIAGNOSTIC-ENV-DATA-CONDITION, AUTOSAR_00052.xsd l.35873. The writer reads the
model via the get* getters; the dispatch entries are writeDiagnosticEnvConditionFormula
(PARTS loop) → writeDiagnosticEnvDataCondition.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_env_data_condition.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import (
    DiagnosticCompareTypeEnum,
    DiagnosticEnvConditionFormula,
    DiagnosticEnvDataCondition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, PositiveInteger, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _text_value_specification(text: str) -> TextValueSpecification:
    value_spec = TextValueSpecification()
    literal = ARLiteral()
    literal.setValue(text)
    value_spec.setValue(literal)
    return value_spec


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _positive_integer(value: str) -> PositiveInteger:
    nrc_value = PositiveInteger()
    nrc_value.setValue(value)
    return nrc_value


class TestWriteDiagnosticEnvDataCondition:
    """Tests for writeDiagnosticEnvDataCondition — own element field values (Table 4.41)."""

    def test_write_field_values_in_xsd_order(self):
        """Test that COMPARE-TYPE (inherited), COMPARE-VALUE and DATA-ELEMENT-REF are emitted with field values in XSD order."""
        condition = DiagnosticEnvDataCondition()
        condition.setCompareType(DiagnosticCompareTypeEnum().setValue(DiagnosticCompareTypeEnum.IS_LESS_OR_EQUAL))
        condition.setCompareValue(_text_value_specification("42"))
        condition.setDataElementRef(_ref("DIAGNOSTIC-DATA-ELEMENT", "/AUTOSAR/DiagDataElements/Dde1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEnvDataCondition(parent, condition)

        child = parent.find("DIAGNOSTIC-ENV-DATA-CONDITION")
        assert child is not None
        assert child.find("COMPARE-TYPE").text == "IS-LESS-OR-EQUAL"
        text_spec = child.find("COMPARE-VALUE/TEXT-VALUE-SPECIFICATION")
        assert text_spec is not None
        assert text_spec.find("VALUE").text == "42"
        data_element_ref = child.find("DATA-ELEMENT-REF")
        assert data_element_ref.attrib["DEST"] == "DIAGNOSTIC-DATA-ELEMENT"
        assert data_element_ref.text == "/AUTOSAR/DiagDataElements/Dde1"
        tags = [c.tag for c in child]
        assert tags == ["COMPARE-TYPE", "COMPARE-VALUE", "DATA-ELEMENT-REF"]

    def test_write_unset_fields_omits_tags(self):
        """Test that unset fields emit an empty DIAGNOSTIC-ENV-DATA-CONDITION element."""
        condition = DiagnosticEnvDataCondition()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEnvDataCondition(parent, condition)

        child = parent.find("DIAGNOSTIC-ENV-DATA-CONDITION")
        assert child is not None
        assert len(list(child)) == 0
        assert child.find("COMPARE-TYPE") is None
        assert child.find("COMPARE-VALUE") is None
        assert child.find("DATA-ELEMENT-REF") is None

    def test_formula_parts_dispatch_writes_element(self):
        """Test that the formula PARTS loop dispatches a DiagnosticEnvDataCondition part to a DIAGNOSTIC-ENV-DATA-CONDITION element."""
        formula = DiagnosticEnvConditionFormula()
        condition = DiagnosticEnvDataCondition()
        condition.setCompareType(DiagnosticCompareTypeEnum().setValue(DiagnosticCompareTypeEnum.IS_EQUAL))
        condition.setDataElementRef(_ref("DIAGNOSTIC-DATA-ELEMENT", "/AUTOSAR/DiagDataElements/Dde2"))
        formula.addPart(condition)

        parent = ET.Element("DIAGNOSTIC-ENV-CONDITION-FORMULA")
        ARXMLWriter().writeDiagnosticEnvConditionFormula(parent, formula)

        parts = parent.find("PARTS")
        assert parts is not None
        part = parts.find("DIAGNOSTIC-ENV-DATA-CONDITION")
        assert part is not None
        assert part.find("COMPARE-TYPE").text == "IS-EQUAL"
        assert part.find("DATA-ELEMENT-REF").text == "/AUTOSAR/DiagDataElements/Dde2"

    def test_round_trip(self):
        """Test the full build → save → reload → assert cycle over a DiagnosticEnvironmentalCondition with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("EnvConds")
        env_condition = package.createDiagnosticEnvironmentalCondition("Env1")
        formula = DiagnosticEnvConditionFormula()
        formula.setNrcValue(_positive_integer("49"))
        condition = DiagnosticEnvDataCondition()
        condition.setCompareType(DiagnosticCompareTypeEnum().setValue(DiagnosticCompareTypeEnum.IS_LESS_OR_EQUAL))
        condition.setCompareValue(_text_value_specification("42"))
        condition.setDataElementRef(_ref("DIAGNOSTIC-DATA-ELEMENT", "/AUTOSAR/DiagDataElements/Dde1"))
        formula.addPart(condition)
        env_condition.setFormula(formula)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            env_condition_2 = package_2.getElement("Env1", type(env_condition))
            assert env_condition_2 is not None
            formula_2 = env_condition_2.getFormula()
            assert formula_2 is not None
            assert formula_2.getNrcValue().getValue() == 49
            parts = formula_2.getParts()
            assert len(parts) == 1
            part = parts[0]
            assert type(part).__name__ == "DiagnosticEnvDataCondition"
            assert part.getCompareType().getValue() == "isLessOrEqual"
            assert part.getCompareValue() is not None
            assert part.getCompareValue().getValue().getValue() == "42"
            assert part.getDataElementRef() is not None
            assert part.getDataElementRef().getDest() == "DIAGNOSTIC-DATA-ELEMENT"
            assert part.getDataElementRef().getValue() == "/AUTOSAR/DiagDataElements/Dde1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
