import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, Integer, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import UdpNmCluster
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


def _pos_int(value):
    positive_integer = PositiveInteger()
    positive_integer.setValue(value)
    return positive_integer


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _vp(label):
    vp = VariationPoint()
    vp.setShortLabel(Identifier().setValue(label))
    return vp


def _new_cluster():
    cluster = UdpNmCluster(MockParent(), "UdpNmCluster")
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
    cluster.setVlanRef(_ref("ETHERNET-PHYSICAL-CHANNEL", "/Topology/Vlan1"))
    return cluster


_XSD_ELEMENT_ORDER = [
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
    "VLAN-REF",
]


class TestWriteUdpNmCluster:
    def test_write_udp_nm_cluster_element_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeUdpNmCluster(parent, _new_cluster())
        cluster_element = parent.find("UDP-NM-CLUSTER")
        tags = [child.tag for child in cluster_element if child.tag != "SHORT-NAME"]
        assert tags == _XSD_ELEMENT_ORDER
        assert cluster_element.find("NM-CHANNEL-ACTIVE") is None
        assert cluster_element.find("NM-USER-DATA-LENGTH") is None
        assert cluster_element.find("NM-USER-DATA-OFFSET") is None
        assert cluster_element.find("NETWORK-CONFIGURATION") is None

    def test_write_udp_nm_cluster_empty(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeUdpNmCluster(parent, UdpNmCluster(MockParent(), "Empty"))
        cluster_element = parent.find("UDP-NM-CLUSTER")
        tags = [child.tag for child in cluster_element if child.tag != "SHORT-NAME"]
        assert tags == []

    def test_write_udp_nm_cluster_round_trip_field_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeUdpNmCluster(parent, _new_cluster())
        parent.set("xmlns", NS)
        root = ET.fromstring(ET.tostring(parent, encoding="unicode")).find("{%s}UDP-NM-CLUSTER" % NS)
        cluster = UdpNmCluster(MockParent(), "UdpNmCluster")
        ARXMLParser().readUdpNmCluster(root, cluster)
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
        assert cluster.getVlanRef().getValue() == "/Topology/Vlan1"

    def test_write_udp_nm_cluster_writes_variation_point_last(self):
        cluster = _new_cluster()
        cluster.setVariationPoint(_vp("VP1"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeUdpNmCluster(parent, cluster)
        cluster_element = parent.find("UDP-NM-CLUSTER")
        tags = [child.tag for child in cluster_element if child.tag != "SHORT-NAME"]
        assert tags == _XSD_ELEMENT_ORDER + ["VARIATION-POINT"]
        assert cluster_element.find("VARIATION-POINT/SHORT-LABEL").text == "VP1"

    def test_write_udp_nm_cluster_round_trips_variation_point(self):
        cluster = _new_cluster()
        cluster.setVariationPoint(_vp("VP1"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeUdpNmCluster(parent, cluster)
        parent.set("xmlns", NS)
        root = ET.fromstring(ET.tostring(parent, encoding="unicode")).find("{%s}UDP-NM-CLUSTER" % NS)
        parsed = UdpNmCluster(MockParent(), "UdpNmCluster")
        ARXMLParser().readUdpNmCluster(root, parsed)
        assert parsed.getVariationPoint() is not None
        assert parsed.getVariationPoint().getShortLabel().getValue() == "VP1"
