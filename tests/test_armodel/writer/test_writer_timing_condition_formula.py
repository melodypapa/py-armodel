"""Writer tests for the TIMING-CONDITION-FORMULA element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import TimingConditionFormula
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteTimingConditionFormula:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self, parent):
        tcf = TimingConditionFormula(parent, "Formula1")
        tcf.setText("modeActive && eventFired")
        tcf.setTimingArgumentRef(RefType().setValue("/Pkg/Arg").setDest("AUTOSAR-OPERATION-ARGUMENT-INSTANCE"))
        tcf.setTimingConditionRef(RefType().setValue("/Pkg/Cond").setDest("TIMING-CONDITION"))
        tcf.setTimingEventRef(RefType().setValue("/Pkg/Event").setDest("TIMING-DESCRIPTION-EVENT"))
        tcf.setTimingModeRef(RefType().setValue("/Pkg/Mode").setDest("TIMING-MODE-INSTANCE"))
        tcf.setTimingVariableRef(RefType().setValue("/Pkg/Var").setDest("AUTOSAR-VARIABLE-INSTANCE"))
        return tcf

    def test_write_all_members(self):
        parent = self._parent()
        tcf = self._build_full(parent)

        element = ET.Element("TIMING-CONDITION-FORMULA")
        ARXMLWriter().writeTimingConditionFormula(element, tcf)

        assert element.find("SHORT-NAME").text == "Formula1"
        assert element.text == "modeActive && eventFired"
        arg_ref = element.find("TIMING-ARGUMENT-REF")
        assert arg_ref is not None
        assert arg_ref.text == "/Pkg/Arg"
        assert arg_ref.attrib["DEST"] == "AUTOSAR-OPERATION-ARGUMENT-INSTANCE"
        assert element.find("TIMING-CONDITION-REF").text == "/Pkg/Cond"
        assert element.find("TIMING-CONDITION-REF").attrib["DEST"] == "TIMING-CONDITION"
        assert element.find("TIMING-EVENT-REF").text == "/Pkg/Event"
        assert element.find("TIMING-EVENT-REF").attrib["DEST"] == "TIMING-DESCRIPTION-EVENT"
        assert element.find("TIMING-MODE-REF").text == "/Pkg/Mode"
        assert element.find("TIMING-MODE-REF").attrib["DEST"] == "TIMING-MODE-INSTANCE"
        assert element.find("TIMING-VARIABLE-REF").text == "/Pkg/Var"
        assert element.find("TIMING-VARIABLE-REF").attrib["DEST"] == "AUTOSAR-VARIABLE-INSTANCE"

    def test_write_minimal(self):
        parent = self._parent()
        tcf = TimingConditionFormula(parent, "Formula1")

        element = ET.Element("TIMING-CONDITION-FORMULA")
        ARXMLWriter().writeTimingConditionFormula(element, tcf)

        assert element.find("SHORT-NAME").text == "Formula1"
        assert element.text is None
        assert element.find("TIMING-ARGUMENT-REF") is None
        assert element.find("TIMING-CONDITION-REF") is None
        assert element.find("TIMING-EVENT-REF") is None
        assert element.find("TIMING-MODE-REF") is None
        assert element.find("TIMING-VARIABLE-REF") is None

    def test_round_trip(self):
        parent = self._parent()
        tcf = self._build_full(parent)

        element = ET.Element("TIMING-CONDITION-FORMULA")
        ARXMLWriter().writeTimingConditionFormula(element, tcf)

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed = ET.fromstring(xml_str)

        tcf2 = ARXMLParser().readTimingConditionFormula(parent, parsed)
        assert tcf2.getShortName() == "Formula1"
        assert tcf2.getText() == "modeActive && eventFired"
        assert tcf2.getTimingArgumentRef().getValue() == "/Pkg/Arg"
        assert tcf2.getTimingArgumentRef().getDest() == "AUTOSAR-OPERATION-ARGUMENT-INSTANCE"
        assert tcf2.getTimingConditionRef().getValue() == "/Pkg/Cond"
        assert tcf2.getTimingConditionRef().getDest() == "TIMING-CONDITION"
        assert tcf2.getTimingEventRef().getValue() == "/Pkg/Event"
        assert tcf2.getTimingEventRef().getDest() == "TIMING-DESCRIPTION-EVENT"
        assert tcf2.getTimingModeRef().getValue() == "/Pkg/Mode"
        assert tcf2.getTimingModeRef().getDest() == "TIMING-MODE-INSTANCE"
        assert tcf2.getTimingVariableRef().getValue() == "/Pkg/Var"
        assert tcf2.getTimingVariableRef().getDest() == "AUTOSAR-VARIABLE-INSTANCE"
