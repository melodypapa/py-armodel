"""Writer round-trip tests for NmCluster (Table 6.299, p.673).

XML element order per XSD group NM-CLUSTER: COMMUNICATION-CLUSTER-REF,
NM-CHANNEL-ID (legacy), NM-CHANNEL-SLEEP-MASTER, NM-NODES,
NM-NODE-DETECTION-ENABLED, NM-NODE-ID-ENABLED, NM-PNC-PARTICIPATION,
NM-REPEAT-MSG-IND-ENABLED, NM-SYNCHRONIZING-NETWORK, PNC-CLUSTER-VECTOR-LENGTH.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmCluster, NmNode
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

NM_ELEMENT_ORDER = [
    "COMMUNICATION-CLUSTER-REF",
    "NM-CHANNEL-ID",
    "NM-CHANNEL-SLEEP-MASTER",
    "NM-NODES",
    "NM-NODE-DETECTION-ENABLED",
    "NM-NODE-ID-ENABLED",
    "NM-PNC-PARTICIPATION",
    "NM-REPEAT-MSG-IND-ENABLED",
    "NM-SYNCHRONIZING-NETWORK",
    "PNC-CLUSTER-VECTOR-LENGTH",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _new_cluster():
    cluster = CanNmCluster(MockParent(), "Cluster")

    ref = RefType()
    ref.setDest("CAN-CLUSTER")
    ref.setValue("/Clusters/Can1")
    cluster.setCommunicationClusterRef(ref)

    channel_id = Integer()
    channel_id.setValue(3)
    cluster.setNmChannelId(channel_id)

    cluster.setNmChannelSleepMaster(_bool(True))
    node = cluster.createCanNmNode("Node1")
    assert isinstance(node, NmNode)
    cluster.setNmNodeDetectionEnabled(_bool(True))
    cluster.setNmNodeIdEnabled(_bool(True))
    cluster.setNmPncParticipation(_bool(False))
    cluster.setNmRepeatMsgIndEnabled(_bool(True))
    cluster.setNmSynchronizingNetwork(_bool(True))

    vector_length = PositiveInteger()
    vector_length.setValue(16)
    cluster.setPncClusterVectorLength(vector_length)
    return cluster


class TestWriteNmCluster:
    def test_write_all_fields_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmCluster(parent, _new_cluster())
        tags = [child.tag for child in parent]
        assert tags[tags.index("COMMUNICATION-CLUSTER-REF") :] == NM_ELEMENT_ORDER

    def test_write_field_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmCluster(parent, _new_cluster())

        ref = parent.find("COMMUNICATION-CLUSTER-REF")
        assert ref.text == "/Clusters/Can1"
        assert ref.attrib["DEST"] == "CAN-CLUSTER"
        assert parent.find("NM-CHANNEL-ID").text == "3"
        assert parent.find("NM-CHANNEL-SLEEP-MASTER").text == "true"
        node = parent.find("NM-NODES/CAN-NM-NODE/SHORT-NAME")
        assert node.text == "Node1"
        assert parent.find("NM-NODE-DETECTION-ENABLED").text == "true"
        assert parent.find("NM-NODE-ID-ENABLED").text == "true"
        assert parent.find("NM-PNC-PARTICIPATION").text == "false"
        assert parent.find("NM-REPEAT-MSG-IND-ENABLED").text == "true"
        assert parent.find("NM-SYNCHRONIZING-NETWORK").text == "true"
        assert parent.find("PNC-CLUSTER-VECTOR-LENGTH").text == "16"

    def test_write_empty_cluster_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmCluster(parent, CanNmCluster(MockParent(), "Empty"))
        tags = [child.tag for child in parent]
        for element_name in NM_ELEMENT_ORDER:
            assert element_name not in tags

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmCluster(parent, _new_cluster())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

        parsed = CanNmCluster(MockParent(), "Cluster")
        ARXMLParser().readNmCluster(root[0], parsed)

        assert parsed.getCommunicationClusterRef().getValue() == "/Clusters/Can1"
        assert parsed.getCommunicationClusterRef().getDest() == "CAN-CLUSTER"
        assert parsed.getNmChannelId().getValue() == 3
        assert parsed.getNmChannelSleepMaster().getValue() is True
        assert [node.short_name for node in parsed.getNmNodes()] == ["Node1"]
        assert parsed.getNmNodeDetectionEnabled().getValue() is True
        assert parsed.getNmNodeIdEnabled().getValue() is True
        assert parsed.getNmPncParticipation().getValue() is False
        assert parsed.getNmRepeatMsgIndEnabled().getValue() is True
        assert parsed.getNmSynchronizingNetwork().getValue() is True
        assert parsed.getPncClusterVectorLength().getValue() == 16
