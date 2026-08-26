"""Writer tests for the TIMING-DESCRIPTIONS family (TDEvent occurrence expression)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import TimingDescriptionEvent
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression import (
    TDEventOccurrenceExpression,
    TDEventOccurrenceExpressionFormula,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class ConcreteTimingDescriptionEvent(TimingDescriptionEvent):
    pass


class TestWriteTDEventOccurrenceExpressionFormula:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self, parent):
        formula = TDEventOccurrenceExpressionFormula(parent, "Formula1")
        formula.setText("TIMEX_count(E1) > 3")
        formula.setArgumentRef(RefType().setValue("/AUTOSAR/OpArg1").setDest("AUTOSAR-OPERATION-ARGUMENT-INSTANCE"))
        formula.setEventRef(RefType().setValue("/AUTOSAR/TDEvent1").setDest("TD-EVENT-VFB"))
        formula.setModeRef(RefType().setValue("/AUTOSAR/Mode1").setDest("TIMING-MODE-INSTANCE"))
        formula.setVariableRef(RefType().setValue("/AUTOSAR/Var1").setDest("AUTOSAR-VARIABLE-INSTANCE"))
        return formula

    def test_write_all_members(self):
        parent = self._parent()
        formula = self._build_full(parent)

        element = ET.Element("FORMULA")
        ARXMLWriter().writeTDEventOccurrenceExpressionFormula(element, formula)

        assert element.find("SHORT-NAME").text == "Formula1"
        assert element.text == "TIMEX_count(E1) > 3"
        argument_ref = element.find("ARGUMENT-REF")
        assert argument_ref.text == "/AUTOSAR/OpArg1"
        assert argument_ref.attrib["DEST"] == "AUTOSAR-OPERATION-ARGUMENT-INSTANCE"
        assert element.find("EVENT-REF").text == "/AUTOSAR/TDEvent1"
        assert element.find("EVENT-REF").attrib["DEST"] == "TD-EVENT-VFB"
        assert element.find("MODE-REF").text == "/AUTOSAR/Mode1"
        assert element.find("MODE-REF").attrib["DEST"] == "TIMING-MODE-INSTANCE"
        assert element.find("VARIABLE-REF").text == "/AUTOSAR/Var1"
        assert element.find("VARIABLE-REF").attrib["DEST"] == "AUTOSAR-VARIABLE-INSTANCE"

    def test_write_minimal(self):
        parent = self._parent()
        formula = TDEventOccurrenceExpressionFormula(parent, "Formula1")

        element = ET.Element("FORMULA")
        ARXMLWriter().writeTDEventOccurrenceExpressionFormula(element, formula)

        assert element.find("SHORT-NAME").text == "Formula1"
        assert element.text is None
        assert element.find("ARGUMENT-REF") is None
        assert element.find("EVENT-REF") is None
        assert element.find("MODE-REF") is None
        assert element.find("VARIABLE-REF") is None

    def test_round_trip(self):
        parent = self._parent()
        formula = self._build_full(parent)

        element = ET.Element("FORMULA")
        ARXMLWriter().writeTDEventOccurrenceExpressionFormula(element, formula)

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed = ET.fromstring(xml_str)

        formula2 = ARXMLParser().readTDEventOccurrenceExpressionFormula(parent, parsed)
        assert formula2.getShortName() == "Formula1"
        assert formula2.getText() == "TIMEX_count(E1) > 3"
        assert formula2.getArgumentRef().getValue() == "/AUTOSAR/OpArg1"
        assert formula2.getEventRef().getDest() == "TD-EVENT-VFB"
        assert formula2.getModeRef().getValue() == "/AUTOSAR/Mode1"
        assert formula2.getVariableRef().getDest() == "AUTOSAR-VARIABLE-INSTANCE"


class TestWriteTDEventOccurrenceExpression:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self, parent):
        expression = TDEventOccurrenceExpression()
        expression.createArgument(parent, "OpArg1")
        expression.createMode(parent, "Mode1")
        expression.createVariable(parent, "Var1")
        formula = TDEventOccurrenceExpressionFormula(parent, "Formula1")
        formula.setText("TIMEX_count(E1) > 3")
        expression.setFormula(formula)
        return expression

    def test_write_full(self):
        parent = self._parent()
        expression = self._build_full(parent)

        element = ET.Element("OCCURRENCE-EXPRESSION")
        ARXMLWriter().writeTDEventOccurrenceExpression(element, expression)

        arguments_tag = element.find("ARGUMENTS")
        assert arguments_tag is not None
        assert arguments_tag.find("AUTOSAR-OPERATION-ARGUMENT-INSTANCE/SHORT-NAME").text == "OpArg1"
        formula_tag = element.find("FORMULA")
        assert formula_tag is not None
        assert formula_tag.find("SHORT-NAME").text == "Formula1"
        modes_tag = element.find("MODES")
        assert modes_tag is not None
        assert modes_tag.find("TIMING-MODE-INSTANCE/SHORT-NAME").text == "Mode1"
        variables_tag = element.find("VARIABLES")
        assert variables_tag is not None
        assert variables_tag.find("AUTOSAR-VARIABLE-INSTANCE/SHORT-NAME").text == "Var1"

    def test_write_empty_omits_wrappers(self):
        element = ET.Element("OCCURRENCE-EXPRESSION")
        ARXMLWriter().writeTDEventOccurrenceExpression(element, TDEventOccurrenceExpression())

        assert element.find("ARGUMENTS") is None
        assert element.find("FORMULA") is None
        assert element.find("MODES") is None
        assert element.find("VARIABLES") is None

    def test_round_trip(self):
        parent = self._parent()
        expression = self._build_full(parent)

        element = ET.Element("OCCURRENCE-EXPRESSION")
        ARXMLWriter().writeTDEventOccurrenceExpression(element, expression)

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed = ET.fromstring(xml_str)

        expression2 = ARXMLParser().readTDEventOccurrenceExpression(parsed, self._parent())
        assert len(expression2.getArguments()) == 1
        assert expression2.getArguments()[0].getShortName() == "OpArg1"
        assert expression2.getFormula().getText() == "TIMEX_count(E1) > 3"
        assert len(expression2.getModes()) == 1
        assert expression2.getModes()[0].getShortName() == "Mode1"
        assert len(expression2.getVariables()) == 1
        assert expression2.getVariables()[0].getShortName() == "Var1"


class TestWriteTimingDescriptionEvent:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self, parent):
        event = ConcreteTimingDescriptionEvent(parent, "TDEvent1")
        event.setClockReferenceRef(RefType().setValue("/AUTOSAR/Clock1").setDest("TIMING-CLOCK"))
        expression = TDEventOccurrenceExpression()
        expression.createVariable(parent, "Var1")
        event.setOccurrenceExpression(expression)
        return event

    def test_write_full(self):
        parent = self._parent()
        event = self._build_full(parent)

        element = ET.Element("TD-EVENT-VFB")
        ARXMLWriter().writeTimingDescriptionEvent(element, event)

        assert element.find("SHORT-NAME").text == "TDEvent1"
        clock_ref = element.find("CLOCK-REFERENCE-REF")
        assert clock_ref.text == "/AUTOSAR/Clock1"
        assert clock_ref.attrib["DEST"] == "TIMING-CLOCK"
        occurrence_tag = element.find("OCCURRENCE-EXPRESSION")
        assert occurrence_tag is not None
        assert occurrence_tag.find("VARIABLES/AUTOSAR-VARIABLE-INSTANCE/SHORT-NAME").text == "Var1"

    def test_round_trip(self):
        parent = self._parent()
        event = self._build_full(parent)

        element = ET.Element("TD-EVENT-VFB")
        ARXMLWriter().writeTimingDescriptionEvent(element, event)

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed = ET.fromstring(xml_str)

        event2 = ConcreteTimingDescriptionEvent(parent, "TDEvent2")
        ARXMLParser().readTimingDescriptionEvent(parsed, event2)
        assert event2.getClockReferenceRef().getValue() == "/AUTOSAR/Clock1"
        assert event2.getClockReferenceRef().getDest() == "TIMING-CLOCK"
        assert len(event2.getOccurrenceExpression().getVariables()) == 1
        assert event2.getOccurrenceExpression().getVariables()[0].getShortName() == "Var1"
