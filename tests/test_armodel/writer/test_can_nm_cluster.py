import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmCluster
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


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _int(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _pos_int(value):
    positive_integer = PositiveInteger()
    positive_integer.setValue(value)
    return positive_integer


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _new_cluster():
    cluster = CanNmCluster(MockParent(), "CanNmCluster")
    cluster.setNmBusloadReductionActive(_bool(True))
    cluster.setNmCarWakeUpBitPosition(_pos_int("2"))
    cluster.setNmCarWakeUpFilterNodeId(_pos_int("5"))
    cluster.setNmCbvPosition(_int("3"))
    cluster.setNmImmediateNmCycleTime(_time("0.02"))
    cluster.setNmImmediateNmTransmissions(_pos_int("5"))
    cluster.setNmMessageTimeoutTime(_time("1.0"))
    cluster.setNmMsgCycleTime(_time("0.1"))
    cluster.setNmNetworkTimeout(_time("2.0"))
    cluster.setNmNidPosition(_int("1"))
    cluster.setNmRemoteSleepIndicationTime(_time("1.5"))
    cluster.setNmRepeatMessageTime(_time("0.5"))
    cluster.setNmWaitBusSleepTime(_time("0.2"))
    return cluster


_XSD_ELEMENT_ORDER = [
    "NM-BUSLOAD-REDUCTION-ACTIVE",
    "NM-CAR-WAKE-UP-BIT-POSITION",
    "NM-CAR-WAKE-UP-FILTER-NODE-ID",
    "NM-CBV-POSITION",
    "NM-IMMEDIATE-NM-CYCLE-TIME",
    "NM-IMMEDIATE-NM-TRANSMISSIONS",
    "NM-MESSAGE-TIMEOUT-TIME",
    "NM-MSG-CYCLE-TIME",
    "NM-NETWORK-TIMEOUT",
    "NM-NID-POSITION",
    "NM-REMOTE-SLEEP-INDICATION-TIME",
    "NM-REPEAT-MESSAGE-TIME",
    "NM-WAIT-BUS-SLEEP-TIME",
]


class TestWriteCanNmCluster:
    def test_write_can_nm_cluster_element_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanNmCluster(parent, _new_cluster())
        cluster_element = parent.find("CAN-NM-CLUSTER")
        tags = [child.tag for child in cluster_element if child.tag != "SHORT-NAME"]
        assert tags == _XSD_ELEMENT_ORDER
        assert cluster_element.find("NM-CAR-WAKE-UP-RX-ENABLED") is None
        assert cluster_element.find("NM-CHANNEL-ACTIVE") is None
        assert cluster_element.find("NM-USER-DATA-LENGTH") is None
        assert cluster_element.find("NM-CAR-WAKE-UP-FILTER-ENABLED") is None

    def test_write_can_nm_cluster_empty(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanNmCluster(parent, CanNmCluster(MockParent(), "Empty"))
        cluster_element = parent.find("CAN-NM-CLUSTER")
        tags = [child.tag for child in cluster_element if child.tag != "SHORT-NAME"]
        assert tags == []

    def test_write_can_nm_cluster_round_trip_field_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanNmCluster(parent, _new_cluster())
        parent.set("xmlns", NS)
        root = ET.fromstring(ET.tostring(parent, encoding="unicode")).find("{%s}CAN-NM-CLUSTER" % NS)
        cluster = CanNmCluster(MockParent(), "CanNmCluster")
        ARXMLParser().readCanNmCluster(root, cluster)
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
