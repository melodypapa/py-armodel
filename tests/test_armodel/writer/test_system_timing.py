"""
Writer tests for SYSTEM-TIMING elements — SystemTiming, Table 3.3 (p.27, R23-11).

writeSystemTiming emits <SYSTEM-TIMING> with the IDENTIFIABLE level (SHORT-NAME, UUID —
writeIdentifiable), the base TIMING-EXTENSION group (writeTimingExtension) and the
own group member SYSTEM-REF in XSD sequenceOffset order
(AUTOSAR_00052.xsd complexType SYSTEM-TIMING).

Round-trip counterpart: tests/test_armodel/parser/test_system_timing.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import SystemTiming
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


def _new_timing() -> SystemTiming:
    timing = SystemTiming(AUTOSAR.getInstance(), "SystemTiming1")
    timing.setSystemRef(RefType().setDest("SYSTEM").setValue("/Systems/MySystem"))
    return timing


class TestWriteSystemTiming:
    def test_write_emits_element_short_name_and_members(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemTiming(parent, _new_timing())
        node = parent.find("SYSTEM-TIMING")

        assert node is not None
        assert node.find("SHORT-NAME").text == "SystemTiming1"
        system_ref = node.find("SYSTEM-REF")
        assert system_ref.attrib["DEST"] == "SYSTEM"
        assert system_ref.text == "/Systems/MySystem"

    def test_write_empty_emits_identifiable_level_only(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemTiming(parent, SystemTiming(AUTOSAR.getInstance(), "Empty"))
        node = parent.find("SYSTEM-TIMING")

        assert node.find("SHORT-NAME").text == "Empty"
        assert node.find("SYSTEM-REF") is None

    def test_round_trip_preserves_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemTiming(parent, _new_timing())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = SystemTiming(AUTOSAR.getInstance(), "SystemTiming1")
        ARXMLParser().readSystemTiming(root.find("{%s}SYSTEM-TIMING" % NS), reloaded)
        assert reloaded.getShortName() == "SystemTiming1"
        assert reloaded.getSystemRef().getDest() == "SYSTEM"
        assert reloaded.getSystemRef().getValue() == "/Systems/MySystem"
