"""Writer round-trip tests for FlexrayNmNode (Table 6.309, p.679).

FlexrayNmNode has zero own attribute rows (XSD group FLEXRAY-NM-NODE carries
only the removed NM-INSTANCE-ID), so coverage is the inherited NmNode content
written through the NM-NODES wrapper dispatch.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmCluster, FlexrayNmNode, NmNode
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


def _new_cluster_with_node():
    cluster = CanNmCluster(MockParent(), "Cluster")
    node = cluster.createFlexrayNmNode("FrNode1")
    ref = RefType()
    ref.setDest("COMMUNICATION-CONTROLLER")
    ref.setValue("/Topology/Ctrl1")
    node.setControllerRef(ref)
    node_id = Integer()
    node_id.setValue(7)
    node.setNmNodeId(node_id)
    return cluster


class TestWriteFlexrayNmNode:
    def test_write_nm_nodes_wrapper_contains_flexray_node(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmClusterNmNodes(parent, _new_cluster_with_node())
        node = parent.find("NM-NODES/FLEXRAY-NM-NODE")
        assert node is not None
        assert node.find("SHORT-NAME").text == "FrNode1"

    def test_write_nm_node_content(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmClusterNmNodes(parent, _new_cluster_with_node())
        node = parent.find("NM-NODES/FLEXRAY-NM-NODE")
        controller = node.find("CONTROLLER-REF")
        assert controller.text == "/Topology/Ctrl1"
        assert controller.attrib["DEST"] == "COMMUNICATION-CONTROLLER"
        assert node.find("NM-NODE-ID").text == "7"

    def test_round_trip_preserves_node(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmClusterNmNodes(parent, _new_cluster_with_node())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

        parsed_cluster = CanNmCluster(MockParent(), "Cluster")
        ARXMLParser().readNmClusterNmNodes(root[0], parsed_cluster)
        nodes = parsed_cluster.getNmNodes()
        assert len(nodes) == 1
        parsed = nodes[0]
        assert isinstance(parsed, FlexrayNmNode)
        assert isinstance(parsed, NmNode)
        assert parsed.short_name == "FrNode1"
        assert parsed.getControllerRef().getValue() == "/Topology/Ctrl1"
        assert parsed.getNmNodeId().getValue() == 7
