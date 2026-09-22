"""Parser tests for DiagnosticEnvironmentalCondition (Table 4.35, p.79).

XSD group DIAGNOSTIC-ENVIRONMENTAL-CONDITION (AUTOSAR_00052.xsd l.36112)
element order: FORMULA, MODE-ELEMENTS. FORMULA content per XSD group
DIAGNOSTIC-ENV-CONDITION-FORMULA (l.35810): NRC-VALUE, OP, PARTS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import DiagnosticEnvConditionFormula, DiagnosticEnvironmentalCondition

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-ENVIRONMENTAL-CONDITION") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticEnvironmentalCondition:
    def test_read_sets_all_fields(self, parser):
        condition = DiagnosticEnvironmentalCondition(AUTOSAR.getInstance(), "Cond1")
        element = _snip(
            "<SHORT-NAME>Cond1</SHORT-NAME>"
            "<FORMULA>"
            "<NRC-VALUE>34</NRC-VALUE>"
            "<OP>LOGICAL-AND</OP>"
            "<PARTS>"
            "<DIAGNOSTIC-ENV-CONDITION-FORMULA>"
            "<OP>LOGICAL-OR</OP>"
            "</DIAGNOSTIC-ENV-CONDITION-FORMULA>"
            "</PARTS>"
            "</FORMULA>"
        )
        parser.readDiagnosticEnvironmentalCondition(element, condition)
        formula = condition.getFormula()
        assert formula is not None
        assert formula.getNrcValue().getValue() == 34
        assert formula.getOp().getValue() == "LOGICAL-AND"
        parts = formula.getParts()
        assert len(parts) == 1
        assert isinstance(parts[0], DiagnosticEnvConditionFormula)
        assert parts[0].getOp().getValue() == "LOGICAL-OR"

    def test_read_empty(self, parser):
        condition = DiagnosticEnvironmentalCondition(AUTOSAR.getInstance(), "Cond1")
        parser.readDiagnosticEnvironmentalCondition(_snip("<SHORT-NAME>Cond1</SHORT-NAME>"), condition)
        assert condition.getFormula() is None
        assert condition.getModeElements() == []


def test_arpackage_dispatch_reads_element(parser):
    package = AUTOSAR.getInstance().createARPackage("EnvConds")
    ar_package = ET.fromstring(
        "<AR-PACKAGE xmlns='%s'>"
        "<SHORT-NAME>EnvConds</SHORT-NAME>"
        "<ELEMENTS>"
        "<DIAGNOSTIC-ENVIRONMENTAL-CONDITION>"
        "<SHORT-NAME>Cond1</SHORT-NAME>"
        "<FORMULA>"
        "<NRC-VALUE>34</NRC-VALUE>"
        "</FORMULA>"
        "</DIAGNOSTIC-ENVIRONMENTAL-CONDITION>"
        "</ELEMENTS>"
        "</AR-PACKAGE>" % NS
    )
    parser.readARPackageElements(ar_package, package)

    condition = package.getElement("Cond1", DiagnosticEnvironmentalCondition)
    assert condition is not None
    assert isinstance(condition, DiagnosticEnvironmentalCondition)
    assert condition.getFormula().getNrcValue().getValue() == 34
