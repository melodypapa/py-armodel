"""
Writer tests for BSW-COMPOSITION-TIMING elements — BswCompositionTiming, Table 3.5,
p.29 (R23-11).

writeBswCompositionTiming emits <BSW-COMPOSITION-TIMING> with the IDENTIFIABLE level
(SHORT-NAME, UUID — writeIdentifiable), the base TIMING-EXTENSION group
(writeTimingExtension) and the own group wrapper IMPLEMENTATION-REFS/IMPLEMENTATION-REF
in XSD sequenceOffset order (AUTOSAR_00052.xsd complexType BSW-COMPOSITION-TIMING).

Round-trip counterpart: tests/test_armodel/parser/test_bsw_composition_timing.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import BswCompositionTiming
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


def _new_timing() -> BswCompositionTiming:
    timing = BswCompositionTiming(AUTOSAR.getInstance(), "BswCompositionTiming1")
    timing.addImplementationRef(RefType().setDest("BSW-IMPLEMENTATION").setValue("/BswImplementations/Impl1"))
    timing.addImplementationRef(RefType().setDest("BSW-IMPLEMENTATION").setValue("/BswImplementations/Impl2"))
    return timing


class TestWriteBswCompositionTiming:
    def test_write_emits_element_short_name_and_wrapper(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeBswCompositionTiming(parent, _new_timing())
        node = parent.find("BSW-COMPOSITION-TIMING")

        assert node is not None
        assert node.find("SHORT-NAME").text == "BswCompositionTiming1"
        wrapper = node.find("IMPLEMENTATION-REFS")
        assert wrapper is not None
        refs = wrapper.findall("IMPLEMENTATION-REF")
        assert len(refs) == 2
        assert refs[0].attrib["DEST"] == "BSW-IMPLEMENTATION"
        assert refs[0].text == "/BswImplementations/Impl1"
        assert refs[1].text == "/BswImplementations/Impl2"

    def test_write_empty_emits_identifiable_level_only(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeBswCompositionTiming(parent, BswCompositionTiming(AUTOSAR.getInstance(), "Empty"))
        node = parent.find("BSW-COMPOSITION-TIMING")

        assert node.find("SHORT-NAME").text == "Empty"
        assert node.find("IMPLEMENTATION-REFS") is None

    def test_round_trip_preserves_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeBswCompositionTiming(parent, _new_timing())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = BswCompositionTiming(AUTOSAR.getInstance(), "BswCompositionTiming1")
        ARXMLParser().readBswCompositionTiming(root.find("{%s}BSW-COMPOSITION-TIMING" % NS), reloaded)
        assert reloaded.getShortName() == "BswCompositionTiming1"
        refs = reloaded.getImplementationRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/BswImplementations/Impl1"
        assert refs[1].getValue() == "/BswImplementations/Impl2"
