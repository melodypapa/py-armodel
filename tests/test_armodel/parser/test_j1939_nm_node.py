"""Parser tests for J1939NmNode (Table 6.320, p.691).

The markdown renders the table body above its caption at this page split
(p.691-692); the caption block below carries Table 6.321 J1939NodeName's
metadata. ADDRESS-CONFIGURATION-CAPABILITY is read in spec-typed enum form
(Rule 0001.3); coverage runs through the NM-NODES dispatch on NmCluster.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import J1939NmAddressConfigurationCapabilityEnum, J1939NmCluster, J1939NmNode
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestParseJ1939NmNode:
    def _parse_cluster(self, xml):
        root = ET.fromstring(xml)
        cluster = J1939NmCluster(MockParent(), "J1939NmCluster")
        ARXMLParser().readNmClusterNmNodes(root, cluster)
        return cluster

    def test_parse_dispatch_and_field_values(self):
        xml = (
            "<J-1939-NM-CLUSTER xmlns='%s'>"
            "<NM-NODES>"
            "<J-1939-NM-NODE><SHORT-NAME>Node1</SHORT-NAME>"
            "<ADDRESS-CONFIGURATION-CAPABILITY>J-1939-NM--SCA</ADDRESS-CONFIGURATION-CAPABILITY>"
            "<NODE-NAME>"
            "<ARBITRARY-ADDRESS-CAPABLE>true</ARBITRARY-ADDRESS-CAPABLE>"
            "<ECU-INSTANCE>3</ECU-INSTANCE>"
            "<FUNCTION>170</FUNCTION>"
            "<FUNCTION-INSTANCE>1</FUNCTION-INSTANCE>"
            "<IDENTITIY-NUMBER>4660</IDENTITIY-NUMBER>"
            "<INDUSTRY-GROUP>4</INDUSTRY-GROUP>"
            "<MANUFACTURER-CODE>221</MANUFACTURER-CODE>"
            "<VEHICLE-SYSTEM>4</VEHICLE-SYSTEM>"
            "<VEHICLE-SYSTEM-INSTANCE>2</VEHICLE-SYSTEM-INSTANCE>"
            "</NODE-NAME>"
            "</J-1939-NM-NODE>"
            "</NM-NODES>"
            "</J-1939-NM-CLUSTER>" % NS
        )
        cluster = self._parse_cluster(xml)
        nodes = cluster.getNmNodes()
        assert len(nodes) == 1
        node = nodes[0]
        assert isinstance(node, J1939NmNode)
        assert node.getShortName() == "Node1"
        capability = node.getAddressConfigurationCapability()
        assert isinstance(capability, J1939NmAddressConfigurationCapabilityEnum)
        assert capability.getValue() == J1939NmAddressConfigurationCapabilityEnum.J1939NM_SCA
        node_name = node.getNodeName()
        assert node_name is not None
        assert node_name.getArbitraryAddressCapable().getValue() is True
        assert node_name.getEcuInstance().getValue() == 3
        assert node_name.getFunction().getValue() == 170
        assert node_name.getFunctionInstance().getValue() == 1
        assert node_name.getIdentitiyNumber().getValue() == 4660
        assert node_name.getIndustryGroup().getValue() == 4
        assert node_name.getManufacturerCode().getValue() == 221
        assert node_name.getVehicleSystem().getValue() == 4
        assert node_name.getVehicleSystemInstance().getValue() == 2

    def test_parse_empty_node(self):
        xml = "<J-1939-NM-CLUSTER xmlns='%s'><NM-NODES><J-1939-NM-NODE><SHORT-NAME>Node1</SHORT-NAME></J-1939-NM-NODE></NM-NODES></J-1939-NM-CLUSTER>" % NS
        cluster = self._parse_cluster(xml)
        nodes = cluster.getNmNodes()
        assert len(nodes) == 1
        node = nodes[0]
        assert node.getAddressConfigurationCapability() is None
        assert node.getNodeName() is None
