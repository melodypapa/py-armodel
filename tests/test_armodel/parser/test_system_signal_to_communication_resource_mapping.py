"""Reader tests for SystemSignalToCommunicationResourceMapping (Table 5.51, p.289).

XML group SYSTEM-SIGNAL-TO-COMMUNICATION-RESOURCE-MAPPING
(AUTOSAR_00052.xsd l.119960): SOFTWARE-CLUSTER-COM-RESOURCE-REF + SYSTEM-SIGNAL-REF,
after the inherited IDENTIFIABLE group. Dispatched from the SystemMapping
SYSTEM-SIGNAL-TO-COM-RESOURCE-MAPPINGS wrapper (l.119735).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import SystemSignalToCommunicationResourceMapping
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


class TestReadSystemSignalToCommunicationResourceMapping:
    def test_read_full(self):
        xml = (
            """
        <SYSTEM-SIGNAL-TO-COMMUNICATION-RESOURCE-MAPPING xmlns="%s">
            <SHORT-NAME>mapping</SHORT-NAME>
            <SOFTWARE-CLUSTER-COM-RESOURCE-REF DEST="CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE">/Resources/MyComResource</SOFTWARE-CLUSTER-COM-RESOURCE-REF>
            <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Signals/MySignal</SYSTEM-SIGNAL-REF>
        </SYSTEM-SIGNAL-TO-COMMUNICATION-RESOURCE-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = SystemSignalToCommunicationResourceMapping(None, "mapping")
        ARXMLParser().readSystemSignalToCommunicationResourceMapping(element, mapping)

        assert mapping.getSoftwareClusterComResourceRef().getValue() == "/Resources/MyComResource"
        assert mapping.getSoftwareClusterComResourceRef().getDest() == "CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE"
        assert mapping.getSystemSignalRef().getValue() == "/Signals/MySignal"
        assert mapping.getSystemSignalRef().getDest() == "SYSTEM-SIGNAL"

    def test_read_empty(self):
        xml = '<SYSTEM-SIGNAL-TO-COMMUNICATION-RESOURCE-MAPPING xmlns="%s"/>' % NS
        element = _parse(xml)
        mapping = SystemSignalToCommunicationResourceMapping(None, "mapping")
        ARXMLParser().readSystemSignalToCommunicationResourceMapping(element, mapping)

        assert mapping.getSoftwareClusterComResourceRef() is None
        assert mapping.getSystemSignalRef() is None

    def test_read_via_system_mapping(self):
        xml = (
            """
        <PARENT xmlns="%s">
            <SYSTEM-SIGNAL-TO-COM-RESOURCE-MAPPINGS>
                <SYSTEM-SIGNAL-TO-COMMUNICATION-RESOURCE-MAPPING>
                    <SHORT-NAME>mapping</SHORT-NAME>
                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Signals/MySignal</SYSTEM-SIGNAL-REF>
                </SYSTEM-SIGNAL-TO-COMMUNICATION-RESOURCE-MAPPING>
            </SYSTEM-SIGNAL-TO-COM-RESOURCE-MAPPINGS>
        </PARENT>
        """
            % NS
        )
        element = _parse(xml)
        system = System(parent=None, short_name="sys")
        mapping = system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingSystemSignalToComResourceMappings(element, mapping)

        mappings = mapping.getSystemSignalToComResourceMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], SystemSignalToCommunicationResourceMapping)
        assert mappings[0].getSystemSignalRef().getValue() == "/Signals/MySignal"
