"""Tests for the readIEEE1722TpAcfCan handler (R23-11 IEEE1722TpAcfCan, Table 6.293, p.661)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfCan,
    IEEE1722TpAcfCanMessageTypeEnum,
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


class TestReadIEEE1722TpAcfCan:
    """Tests for readIEEE1722TpAcfCan handler (R23-11 IEEE1722TpAcfCan, Table 6.293, p.661)."""

    def test_read_message_type(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CanBus</SHORT-NAME>
                <MESSAGE-TYPE>CAN-BRIEF</MESSAGE-TYPE>
            """,
            root_tag="IEEE-1722-TP-ACF-CAN",
        )
        bus = IEEE1722TpAcfCan(None, "CanBus")
        parser.readIEEE1722TpAcfCan(element, bus)
        assert bus.getMessageType() is not None
        assert isinstance(bus.getMessageType(), IEEE1722TpAcfCanMessageTypeEnum)
        assert bus.getMessageType().getValue() == "CAN-BRIEF"

    def test_read_base_levels_exactly_once(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CanBus</SHORT-NAME>
                <ACF-PARTS>
                    <IEEE-1722-TP-ACF-CAN-PART>
                        <SHORT-NAME>CanPart1</SHORT-NAME>
                    </IEEE-1722-TP-ACF-CAN-PART>
                </ACF-PARTS>
                <BUS-ID>7</BUS-ID>
                <MESSAGE-TYPE>CAN</MESSAGE-TYPE>
                <VARIATION-POINT/>
            """,
            root_tag="IEEE-1722-TP-ACF-CAN",
        )
        bus = IEEE1722TpAcfCan(None, "CanBus")
        parser.readIEEE1722TpAcfCan(element, bus)
        assert bus.getShortName() == "CanBus"
        assert len(bus.getAcfParts()) == 1
        assert bus.getAcfParts()[0].getShortName() == "CanPart1"
        assert bus.getBusId().getValue() == 7
        assert bus.getVariationPoint() is not None
        assert bus.getMessageType().getValue() == "CAN"

    def test_read_message_type_absent(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CanBus</SHORT-NAME>
                <BUS-ID>3</BUS-ID>
            """,
            root_tag="IEEE-1722-TP-ACF-CAN",
        )
        bus = IEEE1722TpAcfCan(None, "CanBus")
        parser.readIEEE1722TpAcfCan(element, bus)
        assert bus.getMessageType() is None
        assert bus.getBusId().getValue() == 3

    def test_read_via_acf_connection_dispatch(self, parser):
        element = _snip(
            """
                <SHORT-NAME>AcfConnection</SHORT-NAME>
                <ACF-TRANSPORTED-BUSS>
                    <IEEE-1722-TP-ACF-CAN>
                        <SHORT-NAME>CanBus</SHORT-NAME>
                        <BUS-ID>4</BUS-ID>
                        <MESSAGE-TYPE>CAN-BRIEF</MESSAGE-TYPE>
                    </IEEE-1722-TP-ACF-CAN>
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
        assert isinstance(buses[0], IEEE1722TpAcfCan)
        assert buses[0].getBusId().getValue() == 4
        assert buses[0].getMessageType().getValue() == "CAN-BRIEF"
