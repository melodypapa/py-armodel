"""Reader tests for CpSoftwareClusterResourceToApplicationPartitionMapping (Table 5.48, p.284).

XML group CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING
(AUTOSAR_00052.xsd l.24533): APPLICATION-PARTITION-REF + RESOURCE-REF, after the
inherited IDENTIFIABLE group. Dispatched from the SystemMapping
RESOURCE-TO-APPLICATION-PARTITION-MAPPINGS wrapper (l.119598).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import CpSoftwareClusterResourceToApplicationPartitionMapping
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


class TestReadCpSoftwareClusterResourceToApplicationPartitionMapping:
    def test_read_full(self):
        xml = (
            """
        <CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING xmlns="%s">
            <SHORT-NAME>mapping</SHORT-NAME>
            <APPLICATION-PARTITION-REF DEST="APPLICATION-PARTITION">/Partitions/MyPartition</APPLICATION-PARTITION-REF>
            <RESOURCE-REF DEST="CP-SOFTWARE-CLUSTER-RESOURCE">/Resources/MyResource</RESOURCE-REF>
        </CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = CpSoftwareClusterResourceToApplicationPartitionMapping(None, "mapping")
        ARXMLParser().readCpSoftwareClusterResourceToApplicationPartitionMapping(element, mapping)

        assert mapping.getApplicationPartitionRef().getValue() == "/Partitions/MyPartition"
        assert mapping.getApplicationPartitionRef().getDest() == "APPLICATION-PARTITION"
        assert mapping.getResourceRef().getValue() == "/Resources/MyResource"
        assert mapping.getResourceRef().getDest() == "CP-SOFTWARE-CLUSTER-RESOURCE"

    def test_read_empty(self):
        xml = '<CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING xmlns="%s"/>' % NS
        element = _parse(xml)
        mapping = CpSoftwareClusterResourceToApplicationPartitionMapping(None, "mapping")
        ARXMLParser().readCpSoftwareClusterResourceToApplicationPartitionMapping(element, mapping)

        assert mapping.getApplicationPartitionRef() is None
        assert mapping.getResourceRef() is None

    def test_read_via_system_mapping(self):
        xml = (
            """
        <PARENT xmlns="%s">
            <RESOURCE-TO-APPLICATION-PARTITION-MAPPINGS>
                <CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING>
                    <SHORT-NAME>mapping</SHORT-NAME>
                    <RESOURCE-REF DEST="CP-SOFTWARE-CLUSTER-RESOURCE">/Resources/MyResource</RESOURCE-REF>
                </CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING>
            </RESOURCE-TO-APPLICATION-PARTITION-MAPPINGS>
        </PARENT>
        """
            % NS
        )
        element = _parse(xml)
        system = System(parent=None, short_name="sys")
        mapping = system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingResourceToApplicationPartitionMappings(element, mapping)

        mappings = mapping.getResourceToApplicationPartitionMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], CpSoftwareClusterResourceToApplicationPartitionMapping)
        assert mappings[0].getResourceRef().getValue() == "/Resources/MyResource"
