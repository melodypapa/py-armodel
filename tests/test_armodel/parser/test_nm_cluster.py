"""Parser round-trip tests for NmCluster (Table 6.299, p.673)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmCluster, NmNode
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
    "<COMMUNICATION-CLUSTER-REF DEST='CAN-CLUSTER'>/Clusters/Can1</COMMUNICATION-CLUSTER-REF>"
    "<NM-CHANNEL-ID>3</NM-CHANNEL-ID>"
    "<NM-CHANNEL-SLEEP-MASTER>true</NM-CHANNEL-SLEEP-MASTER>"
    "<NM-NODES><CAN-NM-NODE><SHORT-NAME>Node1</SHORT-NAME></CAN-NM-NODE></NM-NODES>"
    "<NM-NODE-DETECTION-ENABLED>true</NM-NODE-DETECTION-ENABLED>"
    "<NM-NODE-ID-ENABLED>true</NM-NODE-ID-ENABLED>"
    "<NM-PNC-PARTICIPATION>false</NM-PNC-PARTICIPATION>"
    "<NM-REPEAT-MSG-IND-ENABLED>true</NM-REPEAT-MSG-IND-ENABLED>"
    "<NM-SYNCHRONIZING-NETWORK>true</NM-SYNCHRONIZING-NETWORK>"
    "<PNC-CLUSTER-VECTOR-LENGTH>16</PNC-CLUSTER-VECTOR-LENGTH>"
    "</CAN-NM-CLUSTER>" % {"ns": NS}
)


class TestParseNmCluster:
    def _parse(self, xml):
        root = ET.fromstring(xml)
        cluster = CanNmCluster(MockParent(), "C1")
        ARXMLParser().readNmCluster(root, cluster)
        return cluster

    def test_parse_field_values(self):
        cluster = self._parse(CLUSTER_XML)
        assert cluster.getCommunicationClusterRef().getValue() == "/Clusters/Can1"
        assert cluster.getCommunicationClusterRef().getDest() == "CAN-CLUSTER"
        assert cluster.getNmChannelId().getValue() == 3
        assert cluster.getNmChannelSleepMaster().getValue() is True
        nodes = cluster.getNmNodes()
        assert len(nodes) == 1
        assert isinstance(nodes[0], NmNode)
        assert nodes[0].short_name == "Node1"
        assert cluster.getNmNodeDetectionEnabled().getValue() is True
        assert cluster.getNmNodeIdEnabled().getValue() is True
        assert cluster.getNmPncParticipation().getValue() is False
        assert cluster.getNmRepeatMsgIndEnabled().getValue() is True
        assert cluster.getNmSynchronizingNetwork().getValue() is True
        assert cluster.getPncClusterVectorLength().getValue() == 16

    def test_parse_minimal_cluster(self):
        xml = "<CAN-NM-CLUSTER xmlns='%s'><SHORT-NAME>C1</SHORT-NAME></CAN-NM-CLUSTER>" % NS
        cluster = self._parse(xml)
        assert cluster.getCommunicationClusterRef() is None
        assert cluster.getNmNodes() == []
        assert cluster.getPncClusterVectorLength() is None
