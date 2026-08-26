"""Writer/reader round-trip tests for EthernetCluster (Table 3.47, p.103)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetCluster,
    MacMulticastGroup,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class MockPackage(MockParent):
    def getShortName(self):
        return "Pkg"


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")


class TestWriteEthernetCluster:
    def test_write_timing_and_multicast_groups(self, writer):
        cluster = EthernetCluster(MockPackage(), "EC1")
        startup = TimeValue().setValue(5)
        cluster.setCouplingPortStartupActiveTime(startup)
        switchoff = TimeValue().setValue(10)
        cluster.setCouplingPortSwitchoffDelay(switchoff)
        cluster.createMacMulticastGroup("MMG1")

        parent = ET.Element("ELEMENTS")
        writer.writeEthernetCluster(parent, cluster)

        node = parent.find("ETHERNET-CLUSTER/ETHERNET-CLUSTER-VARIANTS/ETHERNET-CLUSTER-CONDITIONAL")
        assert node is not None
        assert node.find("COUPLING-PORT-STARTUP-ACTIVE-TIME").text == "5.0"
        assert node.find("COUPLING-PORT-SWITCHOFF-DELAY").text == "10.0"
        assert node.find("MAC-MULTICAST-GROUPS/MAC-MULTICAST-GROUP/SHORT-NAME").text == "MMG1"


class TestEthernetClusterRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        cluster = EthernetCluster(MockPackage(), "EC1")
        cluster.setCouplingPortStartupActiveTime(TimeValue().setValue(5))
        cluster.setCouplingPortSwitchoffDelay(TimeValue().setValue(10))
        cluster.createMacMulticastGroup("MMG1")

        parent = ET.Element("ELEMENTS")
        writer.writeEthernetCluster(parent, cluster)

        out_file = str(tmp_path / "ethernet_cluster.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = EthernetCluster(MockParent(), "EC1")
        parser.readEthernetCluster(tree.getroot()[0][0], recovered)

        assert recovered.getShortName() == "EC1"
        assert recovered.getCouplingPortStartupActiveTime().getValue() == 5
        assert recovered.getCouplingPortSwitchoffDelay().getValue() == 10
        groups = recovered.getMacMulticastGroups()
        assert len(groups) == 1
        assert isinstance(groups[0], MacMulticastGroup)
        assert groups[0].getShortName() == "MMG1"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<ETHERNET-CLUSTER xmlns='%s'><SHORT-NAME>Empty</SHORT-NAME></ETHERNET-CLUSTER>" % NS)
        recovered = EthernetCluster(MockParent(), "Empty")
        parser.readEthernetCluster(element, recovered)

        assert recovered.getMacMulticastGroups() == []
        assert recovered.getCouplingPortStartupActiveTime() is None
        assert recovered.getCouplingPortSwitchoffDelay() is None
