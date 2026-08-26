"""Parser tests for the TIMING-DESCRIPTIONS family (TDEvent occurrence expression formula)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


def _parent():
    return AUTOSAR.getInstance().createARPackage("AUTOSAR")


class TestReadTDEventOccurrenceExpressionFormula:
    def test_read_full(self, parser):
        parent = _parent()
        element = ET.fromstring(
            f"<FORMULA xmlns='{NS}'>"
            "TIMEX_count(E1) &gt; 3"
            "<SHORT-NAME>Formula1</SHORT-NAME>"
            "<ARGUMENT-REF DEST='AUTOSAR-OPERATION-ARGUMENT-INSTANCE'>/AUTOSAR/OpArg1</ARGUMENT-REF>"
            "<EVENT-REF DEST='TD-EVENT-VFB'>/AUTOSAR/TDEvent1</EVENT-REF>"
            "<MODE-REF DEST='TIMING-MODE-INSTANCE'>/AUTOSAR/Mode1</MODE-REF>"
            "<VARIABLE-REF DEST='AUTOSAR-VARIABLE-INSTANCE'>/AUTOSAR/Var1</VARIABLE-REF>"
            "</FORMULA>"
        )
        formula = parser.readTDEventOccurrenceExpressionFormula(parent, element)
        assert formula.getShortName() == "Formula1"
        assert formula.getText() == "TIMEX_count(E1) > 3"
        assert formula.getArgumentRef().getValue() == "/AUTOSAR/OpArg1"
        assert formula.getArgumentRef().getDest() == "AUTOSAR-OPERATION-ARGUMENT-INSTANCE"
        assert formula.getEventRef().getValue() == "/AUTOSAR/TDEvent1"
        assert formula.getEventRef().getDest() == "TD-EVENT-VFB"
        assert formula.getModeRef().getValue() == "/AUTOSAR/Mode1"
        assert formula.getModeRef().getDest() == "TIMING-MODE-INSTANCE"
        assert formula.getVariableRef().getValue() == "/AUTOSAR/Var1"
        assert formula.getVariableRef().getDest() == "AUTOSAR-VARIABLE-INSTANCE"

    def test_read_minimal(self, parser):
        parent = _parent()
        element = ET.fromstring(f"<FORMULA xmlns='{NS}'><SHORT-NAME>Formula1</SHORT-NAME></FORMULA>")
        formula = parser.readTDEventOccurrenceExpressionFormula(parent, element)
        assert formula.getShortName() == "Formula1"
        assert formula.getText() is None
        assert formula.getArgumentRef() is None
        assert formula.getEventRef() is None
        assert formula.getModeRef() is None
        assert formula.getVariableRef() is None
