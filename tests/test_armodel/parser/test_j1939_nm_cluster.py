"""Parser round-trip tests for J1939NmCluster (Table 6.319, p.691)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import J1939NmCluster, NmConfig
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
    "<J-1939-NM-CLUSTER xmlns='%(ns)s'>"
    "<SHORT-NAME>J1939Cluster1</SHORT-NAME>"
    "<ADDRESS-CLAIM-ENABLED>true</ADDRESS-CLAIM-ENABLED>"
    "<USES-DYNAMIC-ADDRESSING>false</USES-DYNAMIC-ADDRESSING>"
    "</J-1939-NM-CLUSTER>" % {"ns": NS}
)


class TestParseJ1939NmCluster:
    def _parse_cluster(self):
        root = ET.fromstring(CLUSTER_XML)
        cluster = J1939NmCluster(MockParent(), "J1939Cluster1")
        ARXMLParser().readJ1939NmCluster(root, cluster)
        return cluster

    def test_parse_field_values(self):
        cluster = self._parse_cluster()
        assert cluster.getAddressClaimEnabled().getValue() is True
        assert cluster.getUsesDynamicAddressing().getValue() is False

    def test_parse_dispatch_via_nm_config(self):
        xml = "<NM-CONFIG xmlns='%s'><NM-CLUSTERS>%s</NM-CLUSTERS></NM-CONFIG>" % (NS, CLUSTER_XML)
        root = ET.fromstring(xml)
        config = NmConfig(MockParent(), "Cfg")
        ARXMLParser().readNmConfigNmClusters(root, config)
        clusters = config.getNmClusters()
        assert len(clusters) == 1
        assert isinstance(clusters[0], J1939NmCluster)
        assert clusters[0].short_name == "J1939Cluster1"
        assert clusters[0].getAddressClaimEnabled().getValue() is True
