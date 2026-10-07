"""Reader tests for DdsCpISignalToDdsTopicMapping (Table 5.53, p.293).

XML group DDS-CP-I-SIGNAL-TO-DDS-TOPIC-MAPPING (AUTOSAR_00052.xsd l.28766):
DDS-TOPIC-REF + I-SIGNAL-REF, after the inherited AR-OBJECT group. Dispatched
from the SystemMapping DDS-I-SIGNAL-TO-TOPIC-MAPPINGS wrapper (l.119511).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import DdsCpISignalToDdsTopicMapping
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _parse(xml: str) -> ET.Element:
    return ET.fromstring(xml)


class TestReadDdsCpISignalToDdsTopicMapping:
    def test_read_full(self):
        xml = (
            """
        <DDS-CP-I-SIGNAL-TO-DDS-TOPIC-MAPPING xmlns="%s">
            <DDS-TOPIC-REF DEST="DDS-CP-TOPIC">/Dds/MyTopic</DDS-TOPIC-REF>
            <I-SIGNAL-REF DEST="I-SIGNAL">/ISignals/MySignal</I-SIGNAL-REF>
        </DDS-CP-I-SIGNAL-TO-DDS-TOPIC-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = DdsCpISignalToDdsTopicMapping()
        ARXMLParser().readDdsCpISignalToDdsTopicMapping(element, mapping)

        assert mapping.getDdsTopicRef().getValue() == "/Dds/MyTopic"
        assert mapping.getDdsTopicRef().getDest() == "DDS-CP-TOPIC"
        assert mapping.getISignalRef().getValue() == "/ISignals/MySignal"
        assert mapping.getISignalRef().getDest() == "I-SIGNAL"

    def test_read_empty(self):
        xml = '<DDS-CP-I-SIGNAL-TO-DDS-TOPIC-MAPPING xmlns="%s"/>' % NS
        element = _parse(xml)
        mapping = DdsCpISignalToDdsTopicMapping()
        ARXMLParser().readDdsCpISignalToDdsTopicMapping(element, mapping)

        assert mapping.getDdsTopicRef() is None
        assert mapping.getISignalRef() is None

    def test_read_via_system_mapping(self):
        xml = (
            """
        <PARENT xmlns="%s">
            <DDS-I-SIGNAL-TO-TOPIC-MAPPINGS>
                <DDS-CP-I-SIGNAL-TO-DDS-TOPIC-MAPPING>
                    <I-SIGNAL-REF DEST="I-SIGNAL">/ISignals/MySignal</I-SIGNAL-REF>
                </DDS-CP-I-SIGNAL-TO-DDS-TOPIC-MAPPING>
            </DDS-I-SIGNAL-TO-TOPIC-MAPPINGS>
        </PARENT>
        """
            % NS
        )
        element = _parse(xml)
        system = System(parent=None, short_name="sys")
        mapping = system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingDdsISignalToTopicMappings(element, mapping)

        mappings = mapping.getDdsISignalToTopicMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], DdsCpISignalToDdsTopicMapping)
        assert mappings[0].getISignalRef().getValue() == "/ISignals/MySignal"
