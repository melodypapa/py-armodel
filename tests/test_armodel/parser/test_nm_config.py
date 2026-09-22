"""Parser round-trip tests for NmConfig (Table 6.298, p.672)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    CanNmClusterCoupling,
    FlexrayNmCluster,
    J1939NmCluster,
    NmConfig,
    NmEcu,
    UdpNmClusterCoupling,
)
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


CONFIG_XML = (
    "<NM-CONFIG xmlns='%(ns)s'>"
    "<SHORT-NAME>NmConfig1</SHORT-NAME>"
    "<NM-CLUSTERS>"
    "<CAN-NM-CLUSTER><SHORT-NAME>CanCluster1</SHORT-NAME><NM-CHANNEL-SLEEP-MASTER>true</NM-CHANNEL-SLEEP-MASTER></CAN-NM-CLUSTER>"
    "<FLEXRAY-NM-CLUSTER><SHORT-NAME>FrCluster1</SHORT-NAME><NM-VOTING-CYCLE>1</NM-VOTING-CYCLE></FLEXRAY-NM-CLUSTER>"
    "<J-1939-NM-CLUSTER><SHORT-NAME>J1939Cluster1</SHORT-NAME><ADDRESS-CLAIM-ENABLED>true</ADDRESS-CLAIM-ENABLED></J-1939-NM-CLUSTER>"
    "</NM-CLUSTERS>"
    "<NM-CLUSTER-COUPLINGS>"
    "<CAN-NM-CLUSTER-COUPLING>"
    "<COUPLED-CLUSTER-REFS><COUPLED-CLUSTER-REF DEST='CAN-CLUSTER'>/Clusters/Can1</COUPLED-CLUSTER-REF></COUPLED-CLUSTER-REFS>"
    "<NM-BUSLOAD-REDUCTION-ENABLED>true</NM-BUSLOAD-REDUCTION-ENABLED>"
    "</CAN-NM-CLUSTER-COUPLING>"
    "<UDP-NM-CLUSTER-COUPLING>"
    "<COUPLED-CLUSTER-REFS><COUPLED-CLUSTER-REF DEST='ETHERNET-CLUSTER'>/Clusters/Eth1</COUPLED-CLUSTER-REF></COUPLED-CLUSTER-REFS>"
    "</UDP-NM-CLUSTER-COUPLING>"
    "</NM-CLUSTER-COUPLINGS>"
    "<NM-IF-ECUS>"
    "<NM-ECU><SHORT-NAME>NmEcu1</SHORT-NAME><NM-COM-CONTROL-ENABLED>true</NM-COM-CONTROL-ENABLED></NM-ECU>"
    "</NM-IF-ECUS>"
    "</NM-CONFIG>" % {"ns": NS}
)


class TestParseNmConfig:
    def _parse(self, xml):
        root = ET.fromstring(xml)
        config = NmConfig(MockParent(), "NmConfig1")
        ARXMLParser().readNmConfig(root, config)
        return config

    def test_parse_clusters(self):
        config = self._parse(CONFIG_XML)
        clusters = config.getNmClusters()
        assert [cluster.short_name for cluster in clusters] == ["CanCluster1", "FrCluster1", "J1939Cluster1"]
        assert isinstance(clusters[1], FlexrayNmCluster)
        assert clusters[1].getNmVotingCycle().getValue() == 1
        assert isinstance(clusters[2], J1939NmCluster)
        assert clusters[2].getAddressClaimEnabled().getValue() is True

    def test_parse_couplings(self):
        config = self._parse(CONFIG_XML)
        couplings = config.getNmClusterCouplings()
        assert len(couplings) == 2
        assert isinstance(couplings[0], CanNmClusterCoupling)
        assert isinstance(couplings[1], UdpNmClusterCoupling)
        assert couplings[0].getNmBusloadReductionEnabled().getValue() is True
        assert couplings[1].getCoupledClusterRefs()[0].getValue() == "/Clusters/Eth1"

    def test_parse_nm_if_ecus(self):
        config = self._parse(CONFIG_XML)
        ecus = config.getNmIfEcus()
        assert len(ecus) == 1
        assert isinstance(ecus[0], NmEcu)
        assert ecus[0].short_name == "NmEcu1"
        assert ecus[0].getNmComControlEnabled().getValue() is True

    def test_parse_empty_config(self):
        xml = "<NM-CONFIG xmlns='%s'><SHORT-NAME>NmConfig1</SHORT-NAME></NM-CONFIG>" % NS
        config = self._parse(xml)
        assert config.getNmClusters() == []
        assert config.getNmClusterCouplings() == []
        assert config.getNmIfEcus() == []
