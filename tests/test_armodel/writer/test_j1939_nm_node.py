"""Writer round-trip tests for J1939NmNode (Table 6.320, p.691).

ADDRESS-CONFIGURATION-CAPABILITY is written in value form from the spec enum
and re-parsed into a J1939NmAddressConfigurationCapabilityEnum instance
(Rule 0001.3 isinstance pin); the NODE-NAME child round-trips all nine
J1939NodeName fields through the NM-NODES dispatch on NmCluster.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import J1939NmAddressConfigurationCapabilityEnum, J1939NmCluster, J1939NmNode, J1939NodeName
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _int(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _new_node(cluster):
    node = cluster.createJ1939NmNode("Node1")
    capability = J1939NmAddressConfigurationCapabilityEnum()
    capability.setValue(J1939NmAddressConfigurationCapabilityEnum.J1939NM_SCA)
    node.setAddressConfigurationCapability(capability)
    node_name = J1939NodeName()
    node_name.setArbitraryAddressCapable(_bool(True))
    node_name.setEcuInstance(_int(3))
    node_name.setFunction(_int(170))
    node_name.setFunctionInstance(_int(1))
    node_name.setIdentitiyNumber(_int(4660))
    node_name.setIndustryGroup(_int(4))
    node_name.setManufacturerCode(_int(221))
    node_name.setVehicleSystem(_int(4))
    node_name.setVehicleSystemInstance(_int(2))
    node.setNodeName(node_name)
    return node


class TestWriteJ1939NmNode:
    def test_write_dispatch_and_element_order(self):
        cluster = J1939NmCluster(MockParent(), "J1939NmCluster")
        _new_node(cluster)
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmClusterNmNodes(parent, cluster)
        node_element = parent.find("NM-NODES/J-1939-NM-NODE")
        assert node_element is not None
        assert [child.tag for child in node_element if child.tag in ("ADDRESS-CONFIGURATION-CAPABILITY", "NODE-NAME")] == ["ADDRESS-CONFIGURATION-CAPABILITY", "NODE-NAME"]
        assert node_element.find("ADDRESS-CONFIGURATION-CAPABILITY").text == "J-1939-NM--SCA"
        assert node_element.find("NODE-NAME/ECU-INSTANCE").text == "3"

    def test_round_trip_preserves_field_values_and_types(self):
        cluster = J1939NmCluster(MockParent(), "J1939NmCluster")
        _new_node(cluster)
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmClusterNmNodes(parent, cluster)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

        parsed_cluster = J1939NmCluster(MockParent(), "J1939NmCluster")
        ARXMLParser().readNmClusterNmNodes(root[0], parsed_cluster)
        nodes = parsed_cluster.getNmNodes()
        assert len(nodes) == 1
        parsed = nodes[0]
        assert isinstance(parsed, J1939NmNode)
        assert parsed.getShortName() == "Node1"
        capability = parsed.getAddressConfigurationCapability()
        assert isinstance(capability, J1939NmAddressConfigurationCapabilityEnum)
        assert capability.getValue() == J1939NmAddressConfigurationCapabilityEnum.J1939NM_SCA
        node_name = parsed.getNodeName()
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

    def test_round_trip_empty_node(self):
        cluster = J1939NmCluster(MockParent(), "J1939NmCluster")
        cluster.createJ1939NmNode("Node1")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmClusterNmNodes(parent, cluster)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

        parsed_cluster = J1939NmCluster(MockParent(), "J1939NmCluster")
        ARXMLParser().readNmClusterNmNodes(root[0], parsed_cluster)
        parsed = parsed_cluster.getNmNodes()[0]
        assert parsed.getAddressConfigurationCapability() is None
        assert parsed.getNodeName() is None
