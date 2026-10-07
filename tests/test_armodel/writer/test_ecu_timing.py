"""
Writer tests for ECU-TIMING elements — EcuTiming, Table 3.6, p.30 (R23-11).

writeEcuTiming emits <ECU-TIMING> with the IDENTIFIABLE level (SHORT-NAME, UUID —
writeIdentifiable), the base TIMING-EXTENSION group (writeTimingExtension) and the
own group member ECU-CONFIGURATION-REF in XSD sequenceOffset order
(AUTOSAR_00052.xsd complexType ECU-TIMING).

Round-trip counterpart: tests/test_armodel/parser/test_ecu_timing.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import EcuTiming
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


def _new_timing() -> EcuTiming:
    timing = EcuTiming(AUTOSAR.getInstance(), "EcuTiming1")
    timing.setEcuConfigurationRef(RefType().setDest("ECUC-VALUE-COLLECTION").setValue("/EcuExtract/EcuConfigValues"))
    return timing


class TestWriteEcuTiming:
    def test_write_emits_element_short_name_and_members(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcuTiming(parent, _new_timing())
        node = parent.find("ECU-TIMING")

        assert node is not None
        assert node.find("SHORT-NAME").text == "EcuTiming1"
        ecu_configuration_ref = node.find("ECU-CONFIGURATION-REF")
        assert ecu_configuration_ref.attrib["DEST"] == "ECUC-VALUE-COLLECTION"
        assert ecu_configuration_ref.text == "/EcuExtract/EcuConfigValues"

    def test_write_empty_emits_identifiable_level_only(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcuTiming(parent, EcuTiming(AUTOSAR.getInstance(), "Empty"))
        node = parent.find("ECU-TIMING")

        assert node.find("SHORT-NAME").text == "Empty"
        assert node.find("ECU-CONFIGURATION-REF") is None

    def test_round_trip_preserves_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcuTiming(parent, _new_timing())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = EcuTiming(AUTOSAR.getInstance(), "EcuTiming1")
        ARXMLParser().readEcuTiming(root.find("{%s}ECU-TIMING" % NS), reloaded)
        assert reloaded.getShortName() == "EcuTiming1"
        assert reloaded.getEcuConfigurationRef().getDest() == "ECUC-VALUE-COLLECTION"
        assert reloaded.getEcuConfigurationRef().getValue() == "/EcuExtract/EcuConfigValues"
