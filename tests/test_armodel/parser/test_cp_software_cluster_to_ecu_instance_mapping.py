"""Reader tests for CpSoftwareClusterToEcuInstanceMapping (Table 5.47, p.283).

XML group CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING (AUTOSAR_00052.xsd l.24715):
ECU-INSTANCE-REF + MACHINE-ID + SW-CLUSTERS/CP-SOFTWARE-CLUSTER-REF-CONDITIONAL,
after the inherited IDENTIFIABLE group. Dispatched from the SystemMapping
SW-CLUSTER-MAPPINGS wrapper (l.119671).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import CpSoftwareClusterToEcuInstanceMapping
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


class TestReadCpSoftwareClusterToEcuInstanceMapping:
    def test_read_full(self):
        xml = (
            """
        <CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING xmlns="%s">
            <SHORT-NAME>mapping</SHORT-NAME>
            <ECU-INSTANCE-REF DEST="ECU-INSTANCE">/EcuInstances/MyEcu</ECU-INSTANCE-REF>
            <MACHINE-ID>1</MACHINE-ID>
            <SW-CLUSTERS>
                <CP-SOFTWARE-CLUSTER-REF-CONDITIONAL>
                    <CP-SOFTWARE-CLUSTER-REF DEST="CP-SOFTWARE-CLUSTER">/Clusters/MyCluster</CP-SOFTWARE-CLUSTER-REF>
                </CP-SOFTWARE-CLUSTER-REF-CONDITIONAL>
            </SW-CLUSTERS>
        </CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = CpSoftwareClusterToEcuInstanceMapping(None, "mapping")
        ARXMLParser().readCpSoftwareClusterToEcuInstanceMapping(element, mapping)

        assert mapping.getEcuInstanceRef().getValue() == "/EcuInstances/MyEcu"
        assert mapping.getEcuInstanceRef().getDest() == "ECU-INSTANCE"
        assert mapping.getMachineId().getValue() == 1
        sw_cluster_refs = mapping.getSwClusterRefs()
        assert len(sw_cluster_refs) == 1
        assert sw_cluster_refs[0].getValue() == "/Clusters/MyCluster"
        assert sw_cluster_refs[0].getDest() == "CP-SOFTWARE-CLUSTER"

    def test_read_empty(self):
        xml = '<CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING xmlns="%s"/>' % NS
        element = _parse(xml)
        mapping = CpSoftwareClusterToEcuInstanceMapping(None, "mapping")
        ARXMLParser().readCpSoftwareClusterToEcuInstanceMapping(element, mapping)

        assert mapping.getEcuInstanceRef() is None
        assert mapping.getMachineId() is None
        assert mapping.getSwClusterRefs() == []

    def test_read_via_system_mapping(self):
        xml = (
            """
        <PARENT xmlns="%s">
            <SW-CLUSTER-MAPPINGS>
                <CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING>
                    <SHORT-NAME>mapping</SHORT-NAME>
                    <ECU-INSTANCE-REF DEST="ECU-INSTANCE">/EcuInstances/MyEcu</ECU-INSTANCE-REF>
                </CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING>
            </SW-CLUSTER-MAPPINGS>
        </PARENT>
        """
            % NS
        )
        element = _parse(xml)
        system = System(parent=None, short_name="sys")
        mapping = system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingSwClusterMappings(element, mapping)

        mappings = mapping.getSwClusterMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], CpSoftwareClusterToEcuInstanceMapping)
        assert mappings[0].getEcuInstanceRef().getValue() == "/EcuInstances/MyEcu"
