import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmCluster
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


def _parse_can_nm_cluster(xml):
    root = ET.fromstring(xml)
    cluster = CanNmCluster(MockParent(), "CanNmCluster")
    ARXMLParser().readCanNmCluster(root, cluster)
    return cluster


class TestParseCanNmCluster:
    def test_parse_can_nm_cluster_field_values(self):
        xml = (
            "<CAN-NM-CLUSTER xmlns='%s'>"
            "<NM-BUSLOAD-REDUCTION-ACTIVE>true</NM-BUSLOAD-REDUCTION-ACTIVE>"
            "<NM-CAR-WAKE-UP-BIT-POSITION>2</NM-CAR-WAKE-UP-BIT-POSITION>"
            "<NM-CAR-WAKE-UP-FILTER-NODE-ID>5</NM-CAR-WAKE-UP-FILTER-NODE-ID>"
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
            "</CAN-NM-CLUSTER>" % NS
        )
        cluster = _parse_can_nm_cluster(xml)
        assert cluster.getNmBusloadReductionActive().getValue() is True
        assert cluster.getNmCarWakeUpBitPosition().getValue() == 2
        assert cluster.getNmCarWakeUpFilterNodeId().getValue() == 5
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

    def test_parse_can_nm_cluster_empty(self):
        xml = "<CAN-NM-CLUSTER xmlns='%s'/>" % NS
        cluster = _parse_can_nm_cluster(xml)
        assert cluster.getNmBusloadReductionActive() is None
        assert cluster.getNmCarWakeUpBitPosition() is None
        assert cluster.getNmCarWakeUpFilterNodeId() is None
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

    def test_parse_can_nm_cluster_ignores_xsd_only_tags(self):
        xml = (
            "<CAN-NM-CLUSTER xmlns='%s'>"
            "<NM-CAR-WAKE-UP-FILTER-ENABLED>true</NM-CAR-WAKE-UP-FILTER-ENABLED>"
            "<NM-CAR-WAKE-UP-RX-ENABLED>true</NM-CAR-WAKE-UP-RX-ENABLED>"
            "<NM-CHANNEL-ACTIVE>true</NM-CHANNEL-ACTIVE>"
            "<NM-USER-DATA-LENGTH>8</NM-USER-DATA-LENGTH>"
            "</CAN-NM-CLUSTER>" % NS
        )
        cluster = _parse_can_nm_cluster(xml)
        assert not hasattr(cluster, "nmCarWakeUpRxEnabled")
        assert not hasattr(cluster, "nmChannelActive")
        assert not hasattr(cluster, "nmUserDataLength")
        assert cluster.getNmBusloadReductionActive() is None
