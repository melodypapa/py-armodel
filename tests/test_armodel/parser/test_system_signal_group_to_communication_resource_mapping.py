"""Reader tests for SystemSignalGroupToCommunicationResourceMapping (Table 5.52, p.290).

XML group SYSTEM-SIGNAL-TO-COMMUNICATION-RESOURCE-MAPPING
(AUTOSAR_00052.xsd l.119899): SOFTWARE-CLUSTER-COM-RESOURCE-REF + SYSTEM-SIGNAL-GROUP-REF,
after the inherited IDENTIFIABLE group. Dispatched from the SystemMapping
SYSTEM-SIGNAL-GROUP-TO-COM-RESOURCE-MAPPINGS wrapper (l.119723).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import SystemSignalGroupToCommunicationResourceMapping
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


class TestReadSystemSignalGroupToCommunicationResourceMapping:
    def test_read_full(self):
        xml = (
            """
        <SYSTEM-SIGNAL-GROUP-TO-COMMUNICATION-RESOURCE-MAPPING xmlns="%s">
            <SHORT-NAME>mapping</SHORT-NAME>
            <SOFTWARE-CLUSTER-COM-RESOURCE-REF DEST="CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE">/Resources/MyComResource</SOFTWARE-CLUSTER-COM-RESOURCE-REF>
            <SYSTEM-SIGNAL-GROUP-REF DEST="SYSTEM-SIGNAL-GROUP">/SignalGroups/MySignalGroup</SYSTEM-SIGNAL-GROUP-REF>
        </SYSTEM-SIGNAL-GROUP-TO-COMMUNICATION-RESOURCE-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = SystemSignalGroupToCommunicationResourceMapping(None, "mapping")
        ARXMLParser().readSystemSignalGroupToCommunicationResourceMapping(element, mapping)

        assert mapping.getSoftwareClusterComResourceRef().getValue() == "/Resources/MyComResource"
        assert mapping.getSoftwareClusterComResourceRef().getDest() == "CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE"
        assert mapping.getSystemSignalGroupRef().getValue() == "/SignalGroups/MySignalGroup"
        assert mapping.getSystemSignalGroupRef().getDest() == "SYSTEM-SIGNAL-GROUP"

    def test_read_empty(self):
        xml = '<SYSTEM-SIGNAL-GROUP-TO-COMMUNICATION-RESOURCE-MAPPING xmlns="%s"/>' % NS
        element = _parse(xml)
        mapping = SystemSignalGroupToCommunicationResourceMapping(None, "mapping")
        ARXMLParser().readSystemSignalGroupToCommunicationResourceMapping(element, mapping)

        assert mapping.getSoftwareClusterComResourceRef() is None
        assert mapping.getSystemSignalGroupRef() is None

    def test_read_via_system_mapping(self):
        xml = (
            """
        <PARENT xmlns="%s">
            <SYSTEM-SIGNAL-GROUP-TO-COM-RESOURCE-MAPPINGS>
                <SYSTEM-SIGNAL-GROUP-TO-COMMUNICATION-RESOURCE-MAPPING>
                    <SHORT-NAME>mapping</SHORT-NAME>
                    <SYSTEM-SIGNAL-GROUP-REF DEST="SYSTEM-SIGNAL-GROUP">/SignalGroups/MySignalGroup</SYSTEM-SIGNAL-GROUP-REF>
                </SYSTEM-SIGNAL-GROUP-TO-COMMUNICATION-RESOURCE-MAPPING>
            </SYSTEM-SIGNAL-GROUP-TO-COM-RESOURCE-MAPPINGS>
        </PARENT>
        """
            % NS
        )
        element = _parse(xml)
        system = System(parent=None, short_name="sys")
        mapping = system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingSystemSignalGroupToComResourceMappings(element, mapping)

        mappings = mapping.getSystemSignalGroupToComResourceMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], SystemSignalGroupToCommunicationResourceMapping)
        assert mappings[0].getSystemSignalGroupRef().getValue() == "/SignalGroups/MySignalGroup"
