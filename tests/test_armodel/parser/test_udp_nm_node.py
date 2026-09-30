import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import UdpNmNode
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


def _parse_udp_nm_node(xml):
    root = ET.fromstring(xml)
    node = UdpNmNode(MockParent(), "UdpNmNode")
    ARXMLParser().readUdpNmNode(root, node)
    return node


class TestParseUdpNmNode:
    def test_parse_udp_nm_node_field_values(self):
        xml = "<UDP-NM-NODE xmlns='%s'>" "<ALL-NM-MESSAGES-KEEP-AWAKE>true</ALL-NM-MESSAGES-KEEP-AWAKE>" "<NM-MSG-CYCLE-OFFSET>0.02</NM-MSG-CYCLE-OFFSET>" "</UDP-NM-NODE>" % NS
        node = _parse_udp_nm_node(xml)
        assert node.getAllNmMessagesKeepAwake().getValue() is True
        assert node.getNmMsgCycleOffset().getValue() == 0.02

    def test_parse_udp_nm_node_empty(self):
        xml = "<UDP-NM-NODE xmlns='%s'/>" % NS
        node = _parse_udp_nm_node(xml)
        assert node.getAllNmMessagesKeepAwake() is None
        assert node.getNmMsgCycleOffset() is None

    def test_parse_udp_nm_node_ignores_xsd_only_tags(self):
        xml = (
            "<UDP-NM-NODE xmlns='%s'>"
            "<COMMUNICATION-CONNECTOR-REF DEST='ETHERNET-COMMUNICATION-CONNECTOR'>/connector</COMMUNICATION-CONNECTOR-REF>"
            "<NM-PN-HANDLE-MULTIPLE-NETWORK-REQUESTS>true</NM-PN-HANDLE-MULTIPLE-NETWORK-REQUESTS>"
            "<NM-MSG-CYCLE-OFFSET>0.05</NM-MSG-CYCLE-OFFSET>"
            "</UDP-NM-NODE>" % NS
        )
        node = _parse_udp_nm_node(xml)
        assert not hasattr(node, "communicationConnector")
        assert not hasattr(node, "nmPnHandleMultipleNetworkRequests")
        assert node.getNmMsgCycleOffset().getValue() == 0.05
        assert node.getAllNmMessagesKeepAwake() is None
