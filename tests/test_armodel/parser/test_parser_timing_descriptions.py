"""Parser tests for the TIMING-DESCRIPTIONS family (TDEvent occurrence expression)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression import (
    AutosarOperationArgumentInstance,
    AutosarVariableInstance,
    TDEventOccurrenceExpressionFormula,
)
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


class TestReadTDEventOccurrenceExpression:
    def test_read_full(self, parser):
        parent = _parent()
        element = ET.fromstring(
            f"<OCCURRENCE-EXPRESSION xmlns='{NS}'>"
            "<ARGUMENTS>"
            "<AUTOSAR-OPERATION-ARGUMENT-INSTANCE>"
            "<SHORT-NAME>OpArg1</SHORT-NAME>"
            "<OPERATION-ARGUMENT-INSTANCE-IREF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/AUTOSAR/Comp</CONTEXT-COMPONENT-REF>"
            "<ROOT-ARGUMENT-DATA-PROTOTYPE-REF DEST='AUTOSAR-OPERATION-ARGUMENT-INSTANCE'>/AUTOSAR/Arg</ROOT-ARGUMENT-DATA-PROTOTYPE-REF>"
            "</OPERATION-ARGUMENT-INSTANCE-IREF>"
            "</AUTOSAR-OPERATION-ARGUMENT-INSTANCE>"
            "</ARGUMENTS>"
            "<FORMULA>"
            "TIMEX_count(E1) &gt; 3"
            "<SHORT-NAME>Formula1</SHORT-NAME>"
            "</FORMULA>"
            "<MODES>"
            "<TIMING-MODE-INSTANCE>"
            "<SHORT-NAME>Mode1</SHORT-NAME>"
            "<MODE-INSTANCE><MODE-IN-SWC-INSTANCE-REF><CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/AUTOSAR/Comp</CONTEXT-COMPONENT-REF><TARGET-MODE-DECLARATION-REF DEST='MODE-DECLARATION'>/AUTOSAR/MD</TARGET-MODE-DECLARATION-REF></MODE-IN-SWC-INSTANCE-REF></MODE-INSTANCE>"
            "</TIMING-MODE-INSTANCE>"
            "</MODES>"
            "<VARIABLES>"
            "<AUTOSAR-VARIABLE-INSTANCE>"
            "<SHORT-NAME>Var1</SHORT-NAME>"
            "<VARIABLE-INSTANCE-IREF>"
            "<ROOT-VARIABLE-DATA-PROTOTYPE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/AUTOSAR/Var</ROOT-VARIABLE-DATA-PROTOTYPE-REF>"
            "</VARIABLE-INSTANCE-IREF>"
            "</AUTOSAR-VARIABLE-INSTANCE>"
            "</VARIABLES>"
            "</OCCURRENCE-EXPRESSION>"
        )
        expression = parser.readTDEventOccurrenceExpression(element, parent)
        arguments = expression.getArguments()
        assert len(arguments) == 1
        assert isinstance(arguments[0], AutosarOperationArgumentInstance)
        assert arguments[0].getShortName() == "OpArg1"
        assert arguments[0].getOperationArgumentInstanceIRef().getRootArgumentDataPrototypeRef().getValue() == "/AUTOSAR/Arg"
        formula = expression.getFormula()
        assert isinstance(formula, TDEventOccurrenceExpressionFormula)
        assert formula.getText() == "TIMEX_count(E1) > 3"
        modes = expression.getModes()
        assert len(modes) == 1
        assert modes[0].getShortName() == "Mode1"
        assert modes[0].getModeInstance().getTargetModeDeclarationRef().getValue() == "/AUTOSAR/MD"
        assert modes[0].getModeInstance().getContextComponentRefs()[0].getValue() == "/AUTOSAR/Comp"
        variables = expression.getVariables()
        assert len(variables) == 1
        assert isinstance(variables[0], AutosarVariableInstance)
        assert variables[0].getVariableInstanceIRef().getRootVariableDataPrototypeRef().getValue() == "/AUTOSAR/Var"

    def test_read_empty(self, parser):
        element = ET.fromstring(f"<OCCURRENCE-EXPRESSION xmlns='{NS}'/>")
        expression = parser.readTDEventOccurrenceExpression(element, _parent())
        assert expression.getArguments() == []
        assert expression.getFormula() is None
        assert expression.getModes() == []
        assert expression.getVariables() == []
