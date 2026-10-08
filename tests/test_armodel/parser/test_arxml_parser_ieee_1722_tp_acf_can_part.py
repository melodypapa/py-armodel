"""Tests for the readIEEE1722TpAcfCanPart handler (R23-11 IEEE1722TpAcfCanPart, Table 6.294, p.661)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfCanPart,
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


class TestReadIEEE1722TpAcfCanPart:
    """Tests for readIEEE1722TpAcfCanPart handler (R23-11 IEEE1722TpAcfCanPart, Table 6.294, p.661)."""

    def test_read_all_fields(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CanPart1</SHORT-NAME>
                <CAN-ADDRESSING-MODE>EXTENDED</CAN-ADDRESSING-MODE>
                <CAN-BIT-RATE-SWITCH>true</CAN-BIT-RATE-SWITCH>
                <CAN-FRAME-TX-BEHAVIOR>CAN-FD</CAN-FRAME-TX-BEHAVIOR>
                <CAN-IDENTIFIER>23</CAN-IDENTIFIER>
                <CAN-IDENTIFIER-MASK>4095</CAN-IDENTIFIER-MASK>
                <CAN-IDENTIFIER-RANGE>
                    <LOWER-CAN-ID>0</LOWER-CAN-ID>
                    <UPPER-CAN-ID>3000</UPPER-CAN-ID>
                </CAN-IDENTIFIER-RANGE>
                <SDU-REF DEST="PDU-TRIGGERING-REF">/Pkg/PduTriggering</SDU-REF>
            """,
            root_tag="IEEE-1722-TP-ACF-CAN-PART",
        )
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        parser.readIEEE1722TpAcfCanPart(element, part)
        assert part.getCanAddressingMode() is not None
        assert part.getCanAddressingMode().getValue() == "EXTENDED"
        assert part.getCanBitRateSwitch() is not None
        assert part.getCanBitRateSwitch().getValue() is True
        assert part.getCanFrameTxBehavior() is not None
        assert part.getCanFrameTxBehavior().getValue() == "CAN-FD"
        assert part.getCanIdentifier() is not None
        assert part.getCanIdentifier().getValue() == 23
        assert part.getCanIdentifierMask() is not None
        assert part.getCanIdentifierMask().getValue() == 4095
        assert part.getCanIdentifierRange() is not None
        assert part.getCanIdentifierRange().getLowerCanId().getValue() == 0
        assert part.getCanIdentifierRange().getUpperCanId().getValue() == 3000
        assert part.getSduRef() is not None
        assert part.getSduRef().getValue() == "/Pkg/PduTriggering"
        assert part.getSduRef().getDest() == "PDU-TRIGGERING-REF"

    def test_read_base_level(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CanPart1</SHORT-NAME>
                <COLLECTION-TRIGGER>ALWAYS</COLLECTION-TRIGGER>
                <VARIATION-POINT/>
            """,
            root_tag="IEEE-1722-TP-ACF-CAN-PART",
        )
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        parser.readIEEE1722TpAcfCanPart(element, part)
        assert part.getCollectionTrigger() is not None
        assert part.getCollectionTrigger().getValue() == "ALWAYS"
        assert part.getVariationPoint() is not None
        assert part.getCanAddressingMode() is None

    def test_read_empty_part(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CanPart1</SHORT-NAME>
            """,
            root_tag="IEEE-1722-TP-ACF-CAN-PART",
        )
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        parser.readIEEE1722TpAcfCanPart(element, part)
        assert part.getCanAddressingMode() is None
        assert part.getCanBitRateSwitch() is None
        assert part.getCanFrameTxBehavior() is None
        assert part.getCanIdentifier() is None
        assert part.getCanIdentifierMask() is None
        assert part.getCanIdentifierRange() is None
        assert part.getSduRef() is None

    def test_read_via_acf_bus_dispatch(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CanBus</SHORT-NAME>
                <ACF-PARTS>
                    <IEEE-1722-TP-ACF-CAN-PART>
                        <SHORT-NAME>CanPart1</SHORT-NAME>
                        <CAN-IDENTIFIER>23</CAN-IDENTIFIER>
                        <SDU-REF DEST="PDU-TRIGGERING-REF">/Pkg/PduTriggering</SDU-REF>
                    </IEEE-1722-TP-ACF-CAN-PART>
                </ACF-PARTS>
                <BUS-ID>4</BUS-ID>
            """,
            root_tag="IEEE-1722-TP-ACF-BUS",
        )
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
            IEEE1722TpAcfBus,
        )

        class _Bus(IEEE1722TpAcfBus):
            pass

        bus = _Bus(None, "CanBus")
        parser.readIEEE1722TpAcfBus(element, bus)
        parts = bus.getAcfParts()
        assert len(parts) == 1
        assert isinstance(parts[0], IEEE1722TpAcfCanPart)
        assert parts[0].getCanIdentifier().getValue() == 23
        assert parts[0].getSduRef().getValue() == "/Pkg/PduTriggering"
