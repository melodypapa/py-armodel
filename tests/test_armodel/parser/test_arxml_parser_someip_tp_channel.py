"""Tests for the readSomeipTpChannel handler (R23-11 SomeipTpChannel, Table 6.266, p.620)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import SomeipTpChannel
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadSomeipTpChannel:
    """Tests for readSomeipTpChannel handler (R23-11 SomeipTpChannel, Table 6.266, p.620)."""

    def test_read_someip_tp_channel_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>ChanIdent</SHORT-NAME>
                <BURST-SIZE>8</BURST-SIZE>
                <RX-TIMEOUT-TIME>0.5</RX-TIMEOUT-TIME>
                <SEPARATION-TIME>0.02</SEPARATION-TIME>
            """,
            root_tag="SOMEIP-TP-CHANNEL",
        )
        channel = SomeipTpChannel(None, "Chan1")
        parser.readSomeipTpChannel(element, channel)
        assert channel.getShortName() == "Chan1"
        assert channel.getBurstSize() is not None
        assert channel.getBurstSize().getValue() == 8
        assert channel.getRxTimeoutTime() is not None
        assert channel.getRxTimeoutTime().getValue() == 0.5
        assert channel.getSeparationTime() is not None
        assert channel.getSeparationTime().getValue() == 0.02

    def test_read_someip_tp_channel_partial(self, parser):
        element = _snip(
            """
                <BURST-SIZE>4</BURST-SIZE>
            """,
            root_tag="SOMEIP-TP-CHANNEL",
        )
        channel = SomeipTpChannel(None, "Chan1")
        parser.readSomeipTpChannel(element, channel)
        assert channel.getBurstSize().getValue() == 4
        assert channel.getRxTimeoutTime() is None
        assert channel.getSeparationTime() is None

    def test_read_someip_tp_channel_empty(self, parser):
        element = _snip("", root_tag="SOMEIP-TP-CHANNEL")
        channel = SomeipTpChannel(None, "Chan1")
        parser.readSomeipTpChannel(element, channel)
        assert channel.getBurstSize() is None
        assert channel.getRxTimeoutTime() is None
        assert channel.getSeparationTime() is None
