"""Writer round-trip tests for FlexrayNmCluster (Table 6.306, p.678).

XML element order per XSD group FLEXRAY-NM-CLUSTER (active elements):
NM-CAR-WAKE-UP-BIT-POSITION, NM-CAR-WAKE-UP-FILTER-ENABLED,
NM-CAR-WAKE-UP-FILTER-NODE-ID, NM-CAR-WAKE-UP-RX-ENABLED, NM-DATA-CYCLE,
NM-MAIN-FUNCTION-PERIOD, NM-REMOTE-SLEEP-INDICATION-TIME,
NM-REPEAT-MESSAGE-TIME, NM-REPETITION-CYCLE, NM-VOTING-CYCLE.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import FlexrayNmCluster, NmConfig
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

ELEMENT_ORDER = [
    "NM-CAR-WAKE-UP-BIT-POSITION",
    "NM-CAR-WAKE-UP-FILTER-ENABLED",
    "NM-CAR-WAKE-UP-FILTER-NODE-ID",
    "NM-CAR-WAKE-UP-RX-ENABLED",
    "NM-DATA-CYCLE",
    "NM-MAIN-FUNCTION-PERIOD",
    "NM-REMOTE-SLEEP-INDICATION-TIME",
    "NM-REPEAT-MESSAGE-TIME",
    "NM-REPETITION-CYCLE",
    "NM-VOTING-CYCLE",
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


def _int(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _pint(value):
    positive = PositiveInteger()
    positive.setValue(value)
    return positive


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _new_cluster(short_name="FrCluster"):
    cluster = FlexrayNmCluster(MockParent(), short_name)
    cluster.setNmCarWakeUpBitPosition(_pint(5))
    cluster.setNmCarWakeUpFilterEnabled(_bool(True))
    cluster.setNmCarWakeUpFilterNodeId(_pint(120))
    cluster.setNmCarWakeUpRxEnabled(_bool(True))
    cluster.setNmDataCycle(_int(4))
    cluster.setNmMainFunctionPeriod(_time(0.02))
    cluster.setNmRemoteSleepIndicationTime(_time(1.5))
    cluster.setNmRepeatMessageTime(_time(0.5))
    cluster.setNmRepetitionCycle(_int(2))
    cluster.setNmVotingCycle(_int(1))
    return cluster


class TestWriteFlexrayNmCluster:
    def test_write_all_fields_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeFlexrayNmCluster(parent, _new_cluster())
        node = parent.find("FLEXRAY-NM-CLUSTER")
        assert node is not None
        tags = [child.tag for child in node]
        assert tags[tags.index("NM-CAR-WAKE-UP-BIT-POSITION") :] == ELEMENT_ORDER

    def test_write_field_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeFlexrayNmCluster(parent, _new_cluster())
        node = parent.find("FLEXRAY-NM-CLUSTER")
        assert node.find("NM-CAR-WAKE-UP-BIT-POSITION").text == "5"
        assert node.find("NM-CAR-WAKE-UP-FILTER-ENABLED").text == "true"
        assert node.find("NM-CAR-WAKE-UP-FILTER-NODE-ID").text == "120"
        assert node.find("NM-CAR-WAKE-UP-RX-ENABLED").text == "true"
        assert node.find("NM-DATA-CYCLE").text == "4"
        assert node.find("NM-MAIN-FUNCTION-PERIOD").text == "0.02"
        assert node.find("NM-REMOTE-SLEEP-INDICATION-TIME").text == "1.5"
        assert node.find("NM-REPEAT-MESSAGE-TIME").text == "0.5"
        assert node.find("NM-REPETITION-CYCLE").text == "2"
        assert node.find("NM-VOTING-CYCLE").text == "1"

    def test_write_empty_cluster_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeFlexrayNmCluster(parent, FlexrayNmCluster(MockParent(), "Empty"))
        node = parent.find("FLEXRAY-NM-CLUSTER")
        assert node is not None
        tags = [child.tag for child in node]
        for element_name in ELEMENT_ORDER:
            assert element_name not in tags

    def test_write_dispatch_via_nm_config(self):
        config = NmConfig(MockParent(), "Cfg")
        config.createFlexrayNmCluster("Fr1")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmConfigNmClusters(parent, config)
        assert parent.find("NM-CLUSTERS/FLEXRAY-NM-CLUSTER") is not None

    def test_round_trip_preserves_all_values(self):
        config = NmConfig(MockParent(), "Cfg")
        cluster = config.createFlexrayNmCluster("Fr1")
        cluster.setNmCarWakeUpBitPosition(_pint(5))
        cluster.setNmCarWakeUpFilterEnabled(_bool(True))
        cluster.setNmCarWakeUpFilterNodeId(_pint(120))
        cluster.setNmCarWakeUpRxEnabled(_bool(True))
        cluster.setNmDataCycle(_int(4))
        cluster.setNmMainFunctionPeriod(_time(0.02))
        cluster.setNmRemoteSleepIndicationTime(_time(1.5))
        cluster.setNmRepeatMessageTime(_time(0.5))
        cluster.setNmRepetitionCycle(_int(2))
        cluster.setNmVotingCycle(_int(1))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmConfigNmClusters(parent, config)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

        parsed_config = NmConfig(MockParent(), "Cfg")
        ARXMLParser().readNmConfigNmClusters(root[0], parsed_config)
        clusters = parsed_config.getNmClusters()
        assert len(clusters) == 1
        parsed = clusters[0]
        assert isinstance(parsed, FlexrayNmCluster)
        assert parsed.short_name == "Fr1"
        assert parsed.getNmCarWakeUpBitPosition().getValue() == 5
        assert parsed.getNmCarWakeUpFilterEnabled().getValue() is True
        assert parsed.getNmCarWakeUpFilterNodeId().getValue() == 120
        assert parsed.getNmCarWakeUpRxEnabled().getValue() is True
        assert parsed.getNmDataCycle().getValue() == 4
        assert parsed.getNmMainFunctionPeriod().getValue() == 0.02
        assert parsed.getNmRemoteSleepIndicationTime().getValue() == 1.5
        assert parsed.getNmRepeatMessageTime().getValue() == 0.5
        assert parsed.getNmRepetitionCycle().getValue() == 2
        assert parsed.getNmVotingCycle().getValue() == 1
