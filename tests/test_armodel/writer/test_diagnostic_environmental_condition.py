"""Writer round-trip tests for DiagnosticEnvironmentalCondition (Table 4.35, p.79).

Child order per XSD complexType DIAGNOSTIC-ENVIRONMENTAL-CONDITION
(AUTOSAR_00052.xsd l.36140): SHORT-NAME (inherited), FORMULA, MODE-ELEMENTS.
FORMULA content per XSD group DIAGNOSTIC-ENV-CONDITION-FORMULA (l.35810):
NRC-VALUE, OP, PARTS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import DiagnosticEnvConditionFormula, DiagnosticEnvironmentalCondition, DiagnosticLogicalOperatorEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _new_condition():
    pkg = AUTOSAR.getInstance().createARPackage("DiagPkg")
    condition = pkg.createDiagnosticEnvironmentalCondition("Cond1")
    formula = DiagnosticEnvConditionFormula()
    formula.setNrcValue(PositiveInteger().setValue(34))
    formula.setOp(DiagnosticLogicalOperatorEnum().setValue(DiagnosticLogicalOperatorEnum.LOGICAL_AND))
    nested = DiagnosticEnvConditionFormula()
    nested.setOp(DiagnosticLogicalOperatorEnum().setValue(DiagnosticLogicalOperatorEnum.LOGICAL_OR))
    formula.addPart(nested)
    condition.setFormula(formula)
    return condition


class TestWriteDiagnosticEnvironmentalCondition:
    def test_write_all_fields_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEnvironmentalCondition(parent, _new_condition())
        node = parent.find("DIAGNOSTIC-ENVIRONMENTAL-CONDITION")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME", "FORMULA"]
        formula = node.find("FORMULA")
        assert [child.tag for child in formula] == ["NRC-VALUE", "OP", "PARTS"]
        assert formula.find("NRC-VALUE").text == "34"
        assert formula.find("OP").text == "LOGICAL-AND"
        parts = formula.findall("PARTS/DIAGNOSTIC-ENV-CONDITION-FORMULA")
        assert len(parts) == 1
        assert [child.tag for child in parts[0]] == ["OP"]
        assert parts[0].find("OP").text == "LOGICAL-OR"

    def test_write_empty_fields_omits_optional_tags(self):
        pkg = AUTOSAR.getInstance().createARPackage("DiagPkg")
        condition = pkg.createDiagnosticEnvironmentalCondition("Cond2")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEnvironmentalCondition(parent, condition)
        node = parent.find("DIAGNOSTIC-ENVIRONMENTAL-CONDITION")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME"]

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEnvironmentalCondition(parent, _new_condition())
        root = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parsed = DiagnosticEnvironmentalCondition(AUTOSAR.getInstance(), "Cond3")
        ARXMLParser().readDiagnosticEnvironmentalCondition(root[0], parsed)
        formula = parsed.getFormula()
        assert formula is not None
        assert formula.getNrcValue().getValue() == 34
        assert formula.getOp().getValue() == "LOGICAL-AND"
        parts = formula.getParts()
        assert len(parts) == 1
        assert parts[0].getOp().getValue() == "LOGICAL-OR"
