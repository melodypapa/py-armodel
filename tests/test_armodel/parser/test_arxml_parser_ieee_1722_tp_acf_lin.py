"""Tests for the readIEEE1722TpAcfLin handler (R23-11 IEEE1722TpAcfLin, Table 6.296, p.667)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfLin,
    IEEE1722TpAcfLinPart,
)
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


class TestReadIEEE1722TpAcfLin:
    """Tests for readIEEE1722TpAcfLin handler (R23-11 IEEE1722TpAcfLin, Table 6.296, p.667)."""

    def test_read_lin_fields(self, parser):
        element = _snip(
            """
                <SHORT-NAME>LinBus</SHORT-NAME>
                <BASE-FREQUENCY>48000</BASE-FREQUENCY>
                <FRAME-SYNC-ENABLED>true</FRAME-SYNC-ENABLED>
                <TIMESTAMP-INTERVAL>4</TIMESTAMP-INTERVAL>
            """,
            root_tag="IEEE-1722-TP-ACF-LIN",
        )
        bus = IEEE1722TpAcfLin(None, "LinBus")
        parser.readIEEE1722TpAcfLin(element, bus)
        assert bus.getBaseFrequency() is not None
        assert bus.getBaseFrequency().getValue() == 48000
        assert bus.getFrameSyncEnabled() is not None
        assert bus.getFrameSyncEnabled().getValue() is True
        assert bus.getTimestampInterval() is not None
        assert bus.getTimestampInterval().getValue() == 4

    def test_read_base_levels_exactly_once(self, parser):
        element = _snip(
            """
                <SHORT-NAME>LinBus</SHORT-NAME>
                <ACF-PARTS>
                    <IEEE-1722-TP-ACF-LIN-PART>
                        <SHORT-NAME>LinPart1</SHORT-NAME>
                        <LIN-IDENTIFIER>17</LIN-IDENTIFIER>
                    </IEEE-1722-TP-ACF-LIN-PART>
                </ACF-PARTS>
                <BUS-ID>5</BUS-ID>
                <VARIATION-POINT/>
                <BASE-FREQUENCY>48000</BASE-FREQUENCY>
                <FRAME-SYNC-ENABLED>false</FRAME-SYNC-ENABLED>
                <TIMESTAMP-INTERVAL>2</TIMESTAMP-INTERVAL>
            """,
            root_tag="IEEE-1722-TP-ACF-LIN",
        )
        bus = IEEE1722TpAcfLin(None, "LinBus")
        parser.readIEEE1722TpAcfLin(element, bus)
        assert bus.getShortName() == "LinBus"
        assert len(bus.getAcfParts()) == 1
        assert isinstance(bus.getAcfParts()[0], IEEE1722TpAcfLinPart)
        assert bus.getAcfParts()[0].getShortName() == "LinPart1"
        assert bus.getAcfParts()[0].getLinIdentifier().getValue() == 17
        assert bus.getBusId().getValue() == 5
        assert bus.getVariationPoint() is not None
        assert bus.getBaseFrequency().getValue() == 48000
        assert bus.getFrameSyncEnabled().getValue() is False
        assert bus.getTimestampInterval().getValue() == 2

    def test_read_lin_fields_absent(self, parser):
        element = _snip(
            """
                <SHORT-NAME>LinBus</SHORT-NAME>
                <BUS-ID>3</BUS-ID>
            """,
            root_tag="IEEE-1722-TP-ACF-LIN",
        )
        bus = IEEE1722TpAcfLin(None, "LinBus")
        parser.readIEEE1722TpAcfLin(element, bus)
        assert bus.getBaseFrequency() is None
        assert bus.getFrameSyncEnabled() is None
        assert bus.getTimestampInterval() is None
        assert bus.getBusId().getValue() == 3

    def test_read_via_acf_connection_dispatch(self, parser):
        element = _snip(
            """
                <SHORT-NAME>AcfConnection</SHORT-NAME>
                <ACF-TRANSPORTED-BUSS>
                    <IEEE-1722-TP-ACF-LIN>
                        <SHORT-NAME>LinBus</SHORT-NAME>
                        <BUS-ID>5</BUS-ID>
                        <BASE-FREQUENCY>48000</BASE-FREQUENCY>
                    </IEEE-1722-TP-ACF-LIN>
                </ACF-TRANSPORTED-BUSS>
            """,
            root_tag="IEEE-1722-TP-ACF-CONNECTION",
        )
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import (
            IEEE1722TpAcfConnection,
        )

        connection = IEEE1722TpAcfConnection(None, "AcfConnection")
        parser.readIEEE1722TpAcfConnection(element, connection)
        buses = connection.getAcfTransportedBuses()
        assert len(buses) == 1
        assert isinstance(buses[0], IEEE1722TpAcfLin)
        assert buses[0].getBusId().getValue() == 5
        assert buses[0].getBaseFrequency().getValue() == 48000
