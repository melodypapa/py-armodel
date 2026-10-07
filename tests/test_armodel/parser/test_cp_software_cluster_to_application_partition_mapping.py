"""Reader tests for CpSoftwareClusterToApplicationPartitionMapping (Table 5.50, p.287).

XML group CP-SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING
(AUTOSAR_00052.xsd l.24647): APPLICATION-PARTITION-REFS/APPLICATION-PARTITION-REF
+ SOFTWARE-CLUSTER-REF, after the inherited IDENTIFIABLE group. Dispatched from
the SystemMapping SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPINGS wrapper
(l.119647).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import CpSoftwareClusterToApplicationPartitionMapping
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


class TestReadCpSoftwareClusterToApplicationPartitionMapping:
    def test_read_full(self):
        xml = (
            """
        <CP-SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING xmlns="%s">
            <SHORT-NAME>mapping</SHORT-NAME>
            <APPLICATION-PARTITION-REFS>
                <APPLICATION-PARTITION-REF DEST="APPLICATION-PARTITION">/Partitions/Partition1</APPLICATION-PARTITION-REF>
                <APPLICATION-PARTITION-REF DEST="APPLICATION-PARTITION">/Partitions/Partition2</APPLICATION-PARTITION-REF>
            </APPLICATION-PARTITION-REFS>
            <SOFTWARE-CLUSTER-REF DEST="CP-SOFTWARE-CLUSTER">/Clusters/MyCluster</SOFTWARE-CLUSTER-REF>
        </CP-SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = CpSoftwareClusterToApplicationPartitionMapping(None, "mapping")
        ARXMLParser().readCpSoftwareClusterToApplicationPartitionMapping(element, mapping)

        refs = mapping.getApplicationPartitionRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/Partitions/Partition1"
        assert refs[0].getDest() == "APPLICATION-PARTITION"
        assert refs[1].getValue() == "/Partitions/Partition2"
        assert mapping.getSoftwareClusterRef().getValue() == "/Clusters/MyCluster"
        assert mapping.getSoftwareClusterRef().getDest() == "CP-SOFTWARE-CLUSTER"

    def test_read_empty(self):
        xml = '<CP-SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING xmlns="%s"/>' % NS
        element = _parse(xml)
        mapping = CpSoftwareClusterToApplicationPartitionMapping(None, "mapping")
        ARXMLParser().readCpSoftwareClusterToApplicationPartitionMapping(element, mapping)

        assert mapping.getApplicationPartitionRefs() == []
        assert mapping.getSoftwareClusterRef() is None

    def test_read_via_system_mapping(self):
        xml = (
            """
        <PARENT xmlns="%s">
            <SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPINGS>
                <CP-SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING>
                    <SHORT-NAME>mapping</SHORT-NAME>
                    <SOFTWARE-CLUSTER-REF DEST="CP-SOFTWARE-CLUSTER">/Clusters/MyCluster</SOFTWARE-CLUSTER-REF>
                </CP-SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING>
            </SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPINGS>
        </PARENT>
        """
            % NS
        )
        element = _parse(xml)
        system = System(parent=None, short_name="sys")
        mapping = system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingSoftwareClusterToApplicationPartitionMappings(element, mapping)

        mappings = mapping.getSoftwareClusterToApplicationPartitionMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], CpSoftwareClusterToApplicationPartitionMapping)
        assert mappings[0].getSoftwareClusterRef().getValue() == "/Clusters/MyCluster"
