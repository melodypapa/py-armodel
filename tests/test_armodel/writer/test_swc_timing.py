"""
Writer tests for SWC-TIMING elements — SwcTiming, Table 3.2 (p.25, R23-11).

writeSwcTiming emits <SWC-TIMING> with the IDENTIFIABLE level (SHORT-NAME, UUID —
writeIdentifiable), the base TIMING-EXTENSION group (writeTimingExtension) and the
own group member BEHAVIOR-REF in XSD sequenceOffset order
(AUTOSAR_00052.xsd complexType SWC-TIMING).

Round-trip counterpart: tests/test_armodel/parser/test_swc_timing.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import SwcTiming
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_timing() -> SwcTiming:
    timing = SwcTiming(AUTOSAR.getInstance(), "SwcTiming1")
    timing.setBehaviorRef(RefType().setDest("SWC-INTERNAL-BEHAVIOR").setValue("/Swc/InternalBehavior/Behav1"))
    return timing


class TestWriteSwcTiming:
    def test_write_emits_element_short_name_and_members(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcTiming(parent, _new_timing())
        node = parent.find("SWC-TIMING")

        assert node is not None
        assert node.find("SHORT-NAME").text == "SwcTiming1"
        behavior_ref = node.find("BEHAVIOR-REF")
        assert behavior_ref.attrib["DEST"] == "SWC-INTERNAL-BEHAVIOR"
        assert behavior_ref.text == "/Swc/InternalBehavior/Behav1"

    def test_write_empty_emits_identifiable_level_only(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcTiming(parent, SwcTiming(AUTOSAR.getInstance(), "Empty"))
        node = parent.find("SWC-TIMING")

        assert node.find("SHORT-NAME").text == "Empty"
        assert node.find("BEHAVIOR-REF") is None

    def test_round_trip_preserves_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcTiming(parent, _new_timing())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = SwcTiming(AUTOSAR.getInstance(), "SwcTiming1")
        ARXMLParser().readSwcTiming(root.find("{%s}SWC-TIMING" % NS), reloaded)
        assert reloaded.getShortName() == "SwcTiming1"
        assert reloaded.getBehaviorRef().getDest() == "SWC-INTERNAL-BEHAVIOR"
        assert reloaded.getBehaviorRef().getValue() == "/Swc/InternalBehavior/Behav1"
