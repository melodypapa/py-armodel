import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import UdpNmCluster
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


def _parse_udp_nm_cluster(xml):
    root = ET.fromstring(xml)
    cluster = UdpNmCluster(MockParent(), "UdpNmCluster")
    ARXMLParser().readUdpNmCluster(root, cluster)
    return cluster


class TestParseUdpNmCluster:
    def test_parse_udp_nm_cluster_field_values(self):
        xml = (
            "<UDP-NM-CLUSTER xmlns='%s'>"
            "<NM-CBV-POSITION>3</NM-CBV-POSITION>"
            "<NM-IMMEDIATE-NM-CYCLE-TIME>0.02</NM-IMMEDIATE-NM-CYCLE-TIME>"
            "<NM-IMMEDIATE-NM-TRANSMISSIONS>5</NM-IMMEDIATE-NM-TRANSMISSIONS>"
            "<NM-MESSAGE-TIMEOUT-TIME>1.0</NM-MESSAGE-TIMEOUT-TIME>"
            "<NM-MSG-CYCLE-TIME>0.1</NM-MSG-CYCLE-TIME>"
            "<NM-NETWORK-TIMEOUT>2.0</NM-NETWORK-TIMEOUT>"
            "<NM-NID-POSITION>1</NM-NID-POSITION>"
            "<NM-REMOTE-SLEEP-INDICATION-TIME>1.5</NM-REMOTE-SLEEP-INDICATION-TIME>"
            "<NM-REPEAT-MESSAGE-TIME>0.5</NM-REPEAT-MESSAGE-TIME>"
            "<NM-WAIT-BUS-SLEEP-TIME>0.2</NM-WAIT-BUS-SLEEP-TIME>"
            "<VLAN-REF DEST='ETHERNET-PHYSICAL-CHANNEL'>/Topology/Vlan1</VLAN-REF>"
            "</UDP-NM-CLUSTER>" % NS
        )
        cluster = _parse_udp_nm_cluster(xml)
        assert cluster.getNmCbvPosition().getValue() == 3
        assert cluster.getNmImmediateNmCycleTime().getValue() == 0.02
        assert cluster.getNmImmediateNmTransmissions().getValue() == 5
        assert cluster.getNmMessageTimeoutTime().getValue() == 1.0
        assert cluster.getNmMsgCycleTime().getValue() == 0.1
        assert cluster.getNmNetworkTimeout().getValue() == 2.0
        assert cluster.getNmNidPosition().getValue() == 1
        assert cluster.getNmRemoteSleepIndicationTime().getValue() == 1.5
        assert cluster.getNmRepeatMessageTime().getValue() == 0.5
        assert cluster.getNmWaitBusSleepTime().getValue() == 0.2
        assert cluster.getVlanRef().getDest() == "ETHERNET-PHYSICAL-CHANNEL"
        assert cluster.getVlanRef().getValue() == "/Topology/Vlan1"

    def test_parse_udp_nm_cluster_empty(self):
        xml = "<UDP-NM-CLUSTER xmlns='%s'/>" % NS
        cluster = _parse_udp_nm_cluster(xml)
        assert cluster.getNmCbvPosition() is None
        assert cluster.getNmImmediateNmCycleTime() is None
        assert cluster.getNmImmediateNmTransmissions() is None
        assert cluster.getNmMessageTimeoutTime() is None
        assert cluster.getNmMsgCycleTime() is None
        assert cluster.getNmNetworkTimeout() is None
        assert cluster.getNmNidPosition() is None
        assert cluster.getNmRemoteSleepIndicationTime() is None
        assert cluster.getNmRepeatMessageTime() is None
        assert cluster.getNmWaitBusSleepTime() is None
        assert cluster.getVlanRef() is None

    def test_parse_udp_nm_cluster_ignores_xsd_only_tags(self):
        xml = (
            "<UDP-NM-CLUSTER xmlns='%s'>"
            "<NM-CHANNEL-ACTIVE>true</NM-CHANNEL-ACTIVE>"
            "<NM-USER-DATA-LENGTH>8</NM-USER-DATA-LENGTH>"
            "<NM-USER-DATA-OFFSET>4</NM-USER-DATA-OFFSET>"
            "</UDP-NM-CLUSTER>" % NS
        )
        cluster = _parse_udp_nm_cluster(xml)
        assert not hasattr(cluster, "nmChannelActive")
        assert cluster.getNmCbvPosition() is None
        assert cluster.getVlanRef() is None
