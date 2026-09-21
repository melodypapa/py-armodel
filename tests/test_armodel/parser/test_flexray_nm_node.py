"""Parser round-trip tests for FlexrayNmNode (Table 6.309, p.679)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmCluster, FlexrayNmNode, NmNode
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


CLUSTER_XML = (
    "<CAN-NM-CLUSTER xmlns='%(ns)s'>"
    "<SHORT-NAME>C1</SHORT-NAME>"
    "<NM-NODES>"
    "<FLEXRAY-NM-NODE>"
    "<SHORT-NAME>FrNode1</SHORT-NAME>"
    "<NM-NODE-ID>7</NM-NODE-ID>"
    "</FLEXRAY-NM-NODE>"
    "</NM-NODES>"
    "</CAN-NM-CLUSTER>" % {"ns": NS}
)


class TestParseFlexrayNmNode:
    def _parse_nodes(self, xml):
        root = ET.fromstring(xml)
        cluster = CanNmCluster(MockParent(), "C1")
        ARXMLParser().readNmClusterNmNodes(root, cluster)
        return cluster.getNmNodes()

    def test_parse_flexray_nm_node(self):
        nodes = self._parse_nodes(CLUSTER_XML)
        assert len(nodes) == 1
        node = nodes[0]
        assert isinstance(node, FlexrayNmNode)
        assert isinstance(node, NmNode)
        assert node.short_name == "FrNode1"
        assert node.getNmNodeId().getValue() == 7

    def test_parse_empty_nm_nodes(self):
        xml = "<CAN-NM-CLUSTER xmlns='%s'><NM-NODES></NM-NODES></CAN-NM-CLUSTER>" % NS
        assert self._parse_nodes(xml) == []
