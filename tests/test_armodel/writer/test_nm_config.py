"""Writer round-trip tests for NmConfig (Table 6.298, p.672).

XML element order per XSD group NM-CONFIG: NM-CLUSTERS, NM-CLUSTER-COUPLINGS,
NM-IF-ECUS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    CanNmCluster,
    CanNmClusterCoupling,
    FlexrayNmCluster,
    J1939NmCluster,
    NmConfig,
    NmEcu,
    UdpNmClusterCoupling,
)
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


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _int(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _new_config(short_name="NmConfig1"):
    config = NmConfig(MockParent(), short_name)

    can_cluster = config.createCanNmCluster("CanCluster1")
    can_cluster.setNmChannelSleepMaster(_bool(True))
    flexray_cluster = config.createFlexrayNmCluster("FrCluster1")
    flexray_cluster.setNmVotingCycle(_int(1))
    j1939_cluster = config.createJ1939NmCluster("J1939Cluster1")
    j1939_cluster.setAddressClaimEnabled(_bool(True))

    can_coupling = CanNmClusterCoupling()
    can_coupling.addCoupledClusterRef(_ref("CAN-CLUSTER", "/Clusters/Can1"))
    can_coupling.setNmBusloadReductionEnabled(_bool(True))
    config.addNmClusterCouplings(can_coupling)

    udp_coupling = UdpNmClusterCoupling()
    udp_coupling.addCoupledClusterRef(_ref("ETHERNET-CLUSTER", "/Clusters/Eth1"))
    config.addNmClusterCouplings(udp_coupling)

    ecu = config.createNmEcu("NmEcu1")
    ecu.setNmComControlEnabled(_bool(True))
    return config


class TestWriteNmConfig:
    def test_write_wrapper_order_matches_xsd(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmConfig(parent, _new_config())
        node = parent.find("NM-CONFIG")
        assert node is not None
        tags = [child.tag for child in node]
        assert tags[tags.index("NM-CLUSTERS") :] == ["NM-CLUSTERS", "NM-CLUSTER-COUPLINGS", "NM-IF-ECUS"]

    def test_write_clusters_of_all_modeled_subtypes(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmConfig(parent, _new_config())
        clusters = parent.find("NM-CONFIG/NM-CLUSTERS")
        assert clusters.find("CAN-NM-CLUSTER/SHORT-NAME").text == "CanCluster1"
        assert clusters.find("FLEXRAY-NM-CLUSTER/SHORT-NAME").text == "FrCluster1"
        assert clusters.find("J-1939-NM-CLUSTER/SHORT-NAME").text == "J1939Cluster1"

    def test_write_empty_config_omits_wrappers(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmConfig(parent, NmConfig(MockParent(), "Empty"))
        node = parent.find("NM-CONFIG")
        assert node is not None
        tags = [child.tag for child in node]
        for wrapper in ("NM-CLUSTERS", "NM-CLUSTER-COUPLINGS", "NM-IF-ECUS"):
            assert wrapper not in tags

    def test_round_trip_preserves_config(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmConfig(parent, _new_config())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

        parsed = NmConfig(MockParent(), "NmConfig1")
        ARXMLParser().readNmConfig(root[0][0], parsed)

        cluster_names = [cluster.short_name for cluster in parsed.getNmClusters()]
        assert cluster_names == ["CanCluster1", "FrCluster1", "J1939Cluster1"]
        assert isinstance(parsed.getNmClusters()[0], CanNmCluster)
        assert isinstance(parsed.getNmClusters()[1], FlexrayNmCluster)
        assert isinstance(parsed.getNmClusters()[2], J1939NmCluster)

        couplings = parsed.getNmClusterCouplings()
        assert len(couplings) == 2
        assert isinstance(couplings[0], CanNmClusterCoupling)
        assert isinstance(couplings[1], UdpNmClusterCoupling)
        assert couplings[0].getCoupledClusterRefs()[0].getValue() == "/Clusters/Can1"

        ecus = parsed.getNmIfEcus()
        assert len(ecus) == 1
        assert isinstance(ecus[0], NmEcu)
        assert ecus[0].short_name == "NmEcu1"
        assert ecus[0].getNmComControlEnabled().getValue() is True
