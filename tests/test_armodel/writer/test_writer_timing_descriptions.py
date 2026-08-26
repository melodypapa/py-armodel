"""Writer tests for the TIMING-DESCRIPTIONS family (TDEvent occurrence expression formula)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression import (
    TDEventOccurrenceExpressionFormula,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


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
