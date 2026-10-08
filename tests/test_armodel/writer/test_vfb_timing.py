"""
Writer tests for VFB-TIMING elements — VfbTiming, Table 3.1 (p.24, R23-11).

writeVfbTiming emits <VFB-TIMING> with the IDENTIFIABLE level (SHORT-NAME, UUID —
writeIdentifiable), the base TIMING-EXTENSION group (writeTimingExtension) and the
own group member COMPONENT-REF in XSD sequenceOffset order
(AUTOSAR_00052.xsd complexType VFB-TIMING).

Round-trip counterpart: tests/test_armodel/parser/test_vfb_timing.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import VfbTiming
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


def _new_timing() -> VfbTiming:
    timing = VfbTiming(AUTOSAR.getInstance(), "VfbTiming1")
    timing.setComponentRef(RefType().setDest("SW-COMPONENT-TYPE").setValue("/SwComponentTypes/MySwc"))
    return timing


class TestWriteVfbTiming:
    def test_write_emits_element_short_name_and_members(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeVfbTiming(parent, _new_timing())
        node = parent.find("VFB-TIMING")

        assert node is not None
        assert node.find("SHORT-NAME").text == "VfbTiming1"
        component_ref = node.find("COMPONENT-REF")
        assert component_ref.attrib["DEST"] == "SW-COMPONENT-TYPE"
        assert component_ref.text == "/SwComponentTypes/MySwc"

    def test_write_empty_emits_identifiable_level_only(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeVfbTiming(parent, VfbTiming(AUTOSAR.getInstance(), "Empty"))
        node = parent.find("VFB-TIMING")

        assert node.find("SHORT-NAME").text == "Empty"
        assert node.find("COMPONENT-REF") is None

    def test_round_trip_preserves_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeVfbTiming(parent, _new_timing())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = VfbTiming(AUTOSAR.getInstance(), "VfbTiming1")
        ARXMLParser().readVfbTiming(root.find("{%s}VFB-TIMING" % NS), reloaded)
        assert reloaded.getShortName() == "VfbTiming1"
        assert reloaded.getComponentRef().getDest() == "SW-COMPONENT-TYPE"
        assert reloaded.getComponentRef().getValue() == "/SwComponentTypes/MySwc"
