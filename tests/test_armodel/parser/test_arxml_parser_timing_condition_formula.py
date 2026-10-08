"""Parser tests for the TIMING-CONDITION-FORMULA element."""

import re
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
    xml_str = re.sub(r"^(<[A-Za-z][\w.-]*)", r'\1 xmlns="http://autosar.org/schema/r4.0"', xml_str)
    return ET.fromstring(xml_str)


class TestReadTimingConditionFormula:
    def test_read_all_members(self):
        element = ET.Element("TIMING-CONDITION-FORMULA")
        element.text = "modeActive && eventFired"
        arg_ref = ET.SubElement(element, "TIMING-ARGUMENT-REF")
        arg_ref.attrib["DEST"] = "AUTOSAR-OPERATION-ARGUMENT-INSTANCE"
        arg_ref.text = "/Pkg/Arg"
        mode_ref = ET.SubElement(element, "TIMING-MODE-REF")
        mode_ref.attrib["DEST"] = "TIMING-MODE-INSTANCE"
        mode_ref.text = "/Pkg/Mode"

        tcf = ARXMLParser().readTimingConditionFormula(_round_trip(element))
        assert tcf.getMixedString() == "modeActive && eventFired"
        assert tcf.getTimingArgumentRef().getValue() == "/Pkg/Arg"
        assert tcf.getTimingArgumentRef().getDest() == "AUTOSAR-OPERATION-ARGUMENT-INSTANCE"
        assert tcf.getTimingModeRef().getValue() == "/Pkg/Mode"
        assert tcf.getTimingModeRef().getDest() == "TIMING-MODE-INSTANCE"
        assert tcf.getTimingConditionRef() is None
        assert tcf.getTimingEventRef() is None
        assert tcf.getTimingVariableRef() is None

    def test_read_minimal(self):
        element = ET.Element("TIMING-CONDITION-FORMULA")

        tcf = ARXMLParser().readTimingConditionFormula(_round_trip(element))
        assert tcf.getMixedString() is None
        assert tcf.getTimingArgumentRef() is None
        assert tcf.getTimingConditionRef() is None
        assert tcf.getTimingEventRef() is None
        assert tcf.getTimingModeRef() is None
        assert tcf.getTimingVariableRef() is None


class TestTimingConditionFormulaSTAttributes:
    def test_round_trip_preserves_s_t_attributes(self):
        """The reader/writer must call readARObject/writeARObject (Rule 0025) so the AR-OBJECT
        attributeGroup S/T checksum/timestamp attributes survive a write→parse round-trip."""
        element = ET.Element("TIMING-CONDITION-FORMULA")
        element.attrib["S"] = "CHECKSUM-1"
        element.attrib["T"] = "2026-10-08T12:00:00+01:00"

        from armodel.writer.arxml_writer import ARXMLWriter

        parsed = ARXMLParser().readTimingConditionFormula(_round_trip(element))
        assert parsed.getChecksum() is not None
        assert parsed.getChecksum().getValue() == "CHECKSUM-1"
        assert parsed.getTimestamp() is not None

        out = ET.Element("TIMING-CONDITION-FORMULA")
        ARXMLWriter().writeTimingConditionFormula(out, parsed)
        assert out.attrib["S"] == "CHECKSUM-1"
        assert out.attrib["T"] == "2026-10-08T12:00:00+01:00"
