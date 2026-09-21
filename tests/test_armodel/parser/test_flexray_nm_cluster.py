"""Parser round-trip tests for FlexrayNmCluster (Table 6.306, p.678)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import FlexrayNmCluster, NmConfig
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
    "<FLEXRAY-NM-CLUSTER xmlns='%(ns)s'>"
    "<SHORT-NAME>Fr1</SHORT-NAME>"
    "<NM-CAR-WAKE-UP-BIT-POSITION>5</NM-CAR-WAKE-UP-BIT-POSITION>"
    "<NM-CAR-WAKE-UP-FILTER-ENABLED>true</NM-CAR-WAKE-UP-FILTER-ENABLED>"
    "<NM-CAR-WAKE-UP-FILTER-NODE-ID>120</NM-CAR-WAKE-UP-FILTER-NODE-ID>"
    "<NM-CAR-WAKE-UP-RX-ENABLED>true</NM-CAR-WAKE-UP-RX-ENABLED>"
    "<NM-DATA-CYCLE>4</NM-DATA-CYCLE>"
    "<NM-MAIN-FUNCTION-PERIOD>0.02</NM-MAIN-FUNCTION-PERIOD>"
    "<NM-REMOTE-SLEEP-INDICATION-TIME>1.5</NM-REMOTE-SLEEP-INDICATION-TIME>"
    "<NM-REPEAT-MESSAGE-TIME>0.5</NM-REPEAT-MESSAGE-TIME>"
    "<NM-REPETITION-CYCLE>2</NM-REPETITION-CYCLE>"
    "<NM-VOTING-CYCLE>1</NM-VOTING-CYCLE>"
    "</FLEXRAY-NM-CLUSTER>" % {"ns": NS}
)


class TestParseFlexrayNmCluster:
    def _parse_cluster(self):
        root = ET.fromstring(CLUSTER_XML)
        cluster = FlexrayNmCluster(MockParent(), "Fr1")
        ARXMLParser().readFlexrayNmCluster(root, cluster)
        return cluster

    def test_parse_field_values(self):
        cluster = self._parse_cluster()
        assert cluster.getNmCarWakeUpBitPosition().getValue() == 5
        assert cluster.getNmCarWakeUpFilterEnabled().getValue() is True
        assert cluster.getNmCarWakeUpFilterNodeId().getValue() == 120
        assert cluster.getNmCarWakeUpRxEnabled().getValue() is True
        assert cluster.getNmDataCycle().getValue() == 4
        assert cluster.getNmMainFunctionPeriod().getValue() == 0.02
        assert cluster.getNmRemoteSleepIndicationTime().getValue() == 1.5
        assert cluster.getNmRepeatMessageTime().getValue() == 0.5
        assert cluster.getNmRepetitionCycle().getValue() == 2
        assert cluster.getNmVotingCycle().getValue() == 1

    def test_parse_dispatch_via_nm_config(self):
        xml = "<NM-CONFIG xmlns='%s'><NM-CLUSTERS>%s</NM-CLUSTERS></NM-CONFIG>" % (NS, CLUSTER_XML)
        root = ET.fromstring(xml)
        config = NmConfig(MockParent(), "Cfg")
        ARXMLParser().readNmConfigNmClusters(root, config)
        clusters = config.getNmClusters()
        assert len(clusters) == 1
        assert isinstance(clusters[0], FlexrayNmCluster)
        assert clusters[0].short_name == "Fr1"
        assert clusters[0].getNmVotingCycle().getValue() == 1
