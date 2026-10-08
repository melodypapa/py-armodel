"""
Writer tests for BSW-MODULE-TIMING elements — BswModuleTiming, Table 3.4, p.28 (R23-11).

writeBswModuleTiming emits <BSW-MODULE-TIMING> with the IDENTIFIABLE level (SHORT-NAME,
UUID — writeIdentifiable), the base TIMING-EXTENSION group (writeTimingExtension) and the
own group member BEHAVIOR-REF in XSD sequenceOffset order
(AUTOSAR_00052.xsd complexType BSW-MODULE-TIMING).

Round-trip counterpart: tests/test_armodel/parser/test_bsw_module_timing.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import BswModuleTiming
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


def _new_timing() -> BswModuleTiming:
    timing = BswModuleTiming(AUTOSAR.getInstance(), "BswModuleTiming1")
    timing.setBehaviorRef(RefType().setDest("BSW-INTERNAL-BEHAVIOR").setValue("/BswModule/InternalBehavior/Behav1"))
    return timing


class TestWriteBswModuleTiming:
    def test_write_emits_element_short_name_and_members(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeBswModuleTiming(parent, _new_timing())
        node = parent.find("BSW-MODULE-TIMING")

        assert node is not None
        assert node.find("SHORT-NAME").text == "BswModuleTiming1"
        behavior_ref = node.find("BEHAVIOR-REF")
        assert behavior_ref.attrib["DEST"] == "BSW-INTERNAL-BEHAVIOR"
        assert behavior_ref.text == "/BswModule/InternalBehavior/Behav1"

    def test_write_empty_emits_identifiable_level_only(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeBswModuleTiming(parent, BswModuleTiming(AUTOSAR.getInstance(), "Empty"))
        node = parent.find("BSW-MODULE-TIMING")

        assert node.find("SHORT-NAME").text == "Empty"
        assert node.find("BEHAVIOR-REF") is None

    def test_round_trip_preserves_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeBswModuleTiming(parent, _new_timing())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = BswModuleTiming(AUTOSAR.getInstance(), "BswModuleTiming1")
        ARXMLParser().readBswModuleTiming(root.find("{%s}BSW-MODULE-TIMING" % NS), reloaded)
        assert reloaded.getShortName() == "BswModuleTiming1"
        assert reloaded.getBehaviorRef().getDest() == "BSW-INTERNAL-BEHAVIOR"
        assert reloaded.getBehaviorRef().getValue() == "/BswModule/InternalBehavior/Behav1"
