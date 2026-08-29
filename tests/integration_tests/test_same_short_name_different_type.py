"""Integration test: same short name coexisting across different element types.

AUTOSAR allows sibling elements with identical short names as long as their
types differ. This test generates an ARXML containing an ETHERNET-PHYSICAL-CHANNEL
with an ISignalTriggering and a PduTriggering that share the same short name,
then verifies that the name/type pairs survive the load -> save -> load round trip.
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Tuple

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCluster
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalTriggering, PduTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EthernetPhysicalChannel
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

SHORT_NAME = "Triggering"
PACKAGE_NAME = "SameShortNamePkg"
CLUSTER_NAME = "EthCluster"
CHANNEL_NAME = "PhysChannel"


if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def build_document() -> AUTOSAR:
    """Build a minimal document containing a physical channel with two
    triggerings (ISignalTriggering / PduTriggering) that share one short name."""
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    document.clear()
    package = document.createARPackage(PACKAGE_NAME)
    cluster = package.createEthernetCluster(CLUSTER_NAME)
    channel = cluster.createEthernetPhysicalChannel(CHANNEL_NAME)
    channel.createISignalTriggering(SHORT_NAME)
    channel.createPduTriggering(SHORT_NAME)
    return document


def load_channel(file_path: Path) -> EthernetPhysicalChannel:
    """Parse an ARXML file and navigate to the physical channel."""
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    document.clear()
    ARXMLParser().load(str(file_path), document)

    package = document.getARPackages()[0]
    cluster = package.getElement(CLUSTER_NAME, EthernetCluster)
    assert cluster is not None, "EthernetCluster '%s' not found" % CLUSTER_NAME
    channel = cluster.getElement(CHANNEL_NAME, EthernetPhysicalChannel)
    assert channel is not None, "EthernetPhysicalChannel '%s' not found" % CHANNEL_NAME
    return channel


def assert_coexistence(channel: EthernetPhysicalChannel) -> Tuple[ISignalTriggering, PduTriggering]:
    """Assert that the same short name is kept for the two different types."""
    isignal = channel.getElement(SHORT_NAME, ISignalTriggering)
    pdu = channel.getElement(SHORT_NAME, PduTriggering)

    assert isignal is not None, "ISignalTriggering '%s' lost" % SHORT_NAME
    assert pdu is not None, "PduTriggering '%s' lost" % SHORT_NAME
    assert type(isignal) is ISignalTriggering
    assert type(pdu) is PduTriggering
    assert isignal is not pdu
    assert isignal.getShortName() == SHORT_NAME
    assert pdu.getShortName() == SHORT_NAME
    assert len(channel.iSignalTriggerings) == 1
    assert len(channel.pduTriggerings) == 1
    return isignal, pdu


def assert_xml_structure(file_path: Path) -> None:
    """Assert the generated XML keeps one SHORT-NAME 'Triggering' under each
    of I-SIGNAL-TRIGGERING and PDU-TRIGGERING inside ETHERNET-PHYSICAL-CHANNEL
    (element layout per the AUTOSAR XSD / serialization rules)."""
    root = ET.parse(str(file_path)).getroot()

    def find_by_tag(element: ET.Element, tag: str):
        return [child for child in element.iter() if child.tag.endswith("}" + tag)]

    channels = find_by_tag(root, "ETHERNET-PHYSICAL-CHANNEL")
    assert len(channels) == 1, "expected exactly one ETHERNET-PHYSICAL-CHANNEL"
    channel = channels[0]

    isignal_names = [sn.text for node in find_by_tag(channel, "I-SIGNAL-TRIGGERING") for sn in find_by_tag(node, "SHORT-NAME")]
    pdu_names = [sn.text for node in find_by_tag(channel, "PDU-TRIGGERING") for sn in find_by_tag(node, "SHORT-NAME")]

    assert isignal_names == [SHORT_NAME], "I-SIGNAL-TRIGGERING short names: %s" % isignal_names
    assert pdu_names == [SHORT_NAME], "PDU-TRIGGERING short names: %s" % pdu_names


class TestSameShortNameDifferentType:
    """Round-trip of coexisting same-short-name elements of different types."""

    @pytest.mark.integration
    def test_same_short_name_different_type_round_trip(self, autosar_reset, tmp_path: Path) -> None:
        """Generate ARXML with same short name / different types, then verify
        the pairs survive load -> save -> load."""
        document = build_document()
        first_file = tmp_path / "same_short_name.arxml"
        ARXMLWriter().save(str(first_file), document)

        assert_xml_structure(first_file)

        channel = load_channel(first_file)
        isignal, pdu = assert_coexistence(channel)

        second_file = tmp_path / "same_short_name_resaved.arxml"
        ARXMLWriter().save(str(second_file), document)

        channel = load_channel(second_file)
        reparsed_isignal, reparsed_pdu = assert_coexistence(channel)

        assert reparsed_isignal.getShortName() == isignal.getShortName()
        assert reparsed_pdu.getShortName() == pdu.getShortName()
        assert_xml_structure(second_file)
