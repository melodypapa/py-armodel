"""Writer round-trip tests for DdsCpISignalToDdsTopicMapping (Table 5.53, p.293).

Serialized through the DDS-CP-I-SIGNAL-TO-DDS-TOPIC-MAPPING element
(AUTOSAR_00052.xsd l.28810) and the DDS-I-SIGNAL-TO-TOPIC-MAPPINGS wrapper
of SystemMapping (l.119511).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import DdsCpISignalToDdsTopicMapping
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestWriteDdsCpISignalToDdsTopicMapping:
    def test_empty(self):
        mapping = DdsCpISignalToDdsTopicMapping()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpISignalToDdsTopicMapping(parent, mapping)

        node = parent.find("DDS-CP-I-SIGNAL-TO-DDS-TOPIC-MAPPING")
        assert node is not None
        assert node.find("DDS-TOPIC-REF") is None
        assert node.find("I-SIGNAL-REF") is None

    def test_full(self):
        mapping = DdsCpISignalToDdsTopicMapping()
        mapping.setDdsTopicRef(_ref("/Dds/MyTopic", "DDS-CP-TOPIC"))
        mapping.setISignalRef(_ref("/ISignals/MySignal", "I-SIGNAL"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpISignalToDdsTopicMapping(parent, mapping)

        node = parent.find("DDS-CP-I-SIGNAL-TO-DDS-TOPIC-MAPPING")
        assert node.find("DDS-TOPIC-REF").text == "/Dds/MyTopic"
        assert node.find("DDS-TOPIC-REF").get("DEST") == "DDS-CP-TOPIC"
        assert node.find("I-SIGNAL-REF").text == "/ISignals/MySignal"
        assert node.find("I-SIGNAL-REF").get("DEST") == "I-SIGNAL"

    def test_round_trip_full(self):
        mapping = DdsCpISignalToDdsTopicMapping()
        mapping.setDdsTopicRef(_ref("/Dds/MyTopic", "DDS-CP-TOPIC"))
        mapping.setISignalRef(_ref("/ISignals/MySignal", "I-SIGNAL"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpISignalToDdsTopicMapping(parent, mapping)

        reloaded = DdsCpISignalToDdsTopicMapping()
        ARXMLParser().readDdsCpISignalToDdsTopicMapping(_with_ns(parent)[0], reloaded)

        assert reloaded.getDdsTopicRef().getValue() == "/Dds/MyTopic"
        assert reloaded.getDdsTopicRef().getDest() == "DDS-CP-TOPIC"
        assert reloaded.getISignalRef().getValue() == "/ISignals/MySignal"

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = DdsCpISignalToDdsTopicMapping()
        mapping.setISignalRef(_ref("/ISignals/MySignal", "I-SIGNAL"))
        system_mapping.addDdsISignalToTopicMapping(mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingDdsISignalToTopicMappings(parent, system_mapping)

        wrapper = parent.find("DDS-I-SIGNAL-TO-TOPIC-MAPPINGS")
        assert wrapper is not None
        assert wrapper.find("DDS-CP-I-SIGNAL-TO-DDS-TOPIC-MAPPING") is not None

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingDdsISignalToTopicMappings(_with_ns(parent), reloaded_mapping)
        mappings = reloaded_mapping.getDdsISignalToTopicMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], DdsCpISignalToDdsTopicMapping)
        assert mappings[0].getISignalRef().getValue() == "/ISignals/MySignal"
