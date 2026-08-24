"""Parser tests for the TIMING-CONDITION-FORMULA element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser


def _parent():
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    return document.createARPackage("AUTOSAR")


def _round_trip(element: ET.Element) -> ET.Element:
    xml_str = ET.tostring(element).decode()
    idx = xml_str.find(">")
    xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
    return ET.fromstring(xml_str)


class TestReadTimingConditionFormula:
    def test_read_all_members(self):
        parent = _parent()
        element = ET.Element("TIMING-CONDITION-FORMULA")
        ET.SubElement(element, "SHORT-NAME").text = "Formula1"
        element.text = "modeActive && eventFired"
        arg_ref = ET.SubElement(element, "TIMING-ARGUMENT-REF")
        arg_ref.attrib["DEST"] = "AUTOSAR-OPERATION-ARGUMENT-INSTANCE"
        arg_ref.text = "/Pkg/Arg"
        mode_ref = ET.SubElement(element, "TIMING-MODE-REF")
        mode_ref.attrib["DEST"] = "TIMING-MODE-INSTANCE"
        mode_ref.text = "/Pkg/Mode"

        tcf = ARXMLParser().readTimingConditionFormula(parent, _round_trip(element))
        assert tcf.getShortName() == "Formula1"
        assert tcf.getText() == "modeActive && eventFired"
        assert tcf.getTimingArgumentRef().getValue() == "/Pkg/Arg"
        assert tcf.getTimingArgumentRef().getDest() == "AUTOSAR-OPERATION-ARGUMENT-INSTANCE"
        assert tcf.getTimingModeRef().getValue() == "/Pkg/Mode"
        assert tcf.getTimingModeRef().getDest() == "TIMING-MODE-INSTANCE"
        assert tcf.getTimingConditionRef() is None
        assert tcf.getTimingEventRef() is None
        assert tcf.getTimingVariableRef() is None

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("TIMING-CONDITION-FORMULA")
        ET.SubElement(element, "SHORT-NAME").text = "Formula1"

        tcf = ARXMLParser().readTimingConditionFormula(parent, _round_trip(element))
        assert tcf.getShortName() == "Formula1"
        assert tcf.getText() is None
        assert tcf.getTimingArgumentRef() is None
        assert tcf.getTimingConditionRef() is None
        assert tcf.getTimingEventRef() is None
        assert tcf.getTimingModeRef() is None
        assert tcf.getTimingVariableRef() is None
