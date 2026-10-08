"""Tests for the readIEEE1722TpAcfBus handler (R23-11 IEEE1722TpAcfBus, Table 6.291, p.657)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    IEEE1722TpAcfCanPart,
    IEEE1722TpAcfLinPart,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import IEEE1722TpAcfBus
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


def _concrete_bus(short_name: str) -> IEEE1722TpAcfBus:
    class _Bus(IEEE1722TpAcfBus):
        pass

    return _Bus(None, short_name)


class TestReadIEEE1722TpAcfBus:
    """Tests for readIEEE1722TpAcfBus handler (R23-11 IEEE1722TpAcfBus, Table 6.291, p.657)."""

    def test_read_ieee_1722_tp_acf_bus_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CanBus</SHORT-NAME>
                <ACF-PARTS>
                    <IEEE-1722-TP-ACF-CAN-PART>
                        <SHORT-NAME>CanPart1</SHORT-NAME>
                    </IEEE-1722-TP-ACF-CAN-PART>
                    <IEEE-1722-TP-ACF-LIN-PART>
                        <SHORT-NAME>LinPart1</SHORT-NAME>
                    </IEEE-1722-TP-ACF-LIN-PART>
                </ACF-PARTS>
                <BUS-ID>7</BUS-ID>
            """,
            root_tag="IEEE-1722-TP-ACF-BUS",
        )
        bus = _concrete_bus("CanBus")
        parser.readIEEE1722TpAcfBus(element, bus)
        assert bus.getShortName() == "CanBus"
        parts = bus.getAcfParts()
        assert len(parts) == 2
        assert isinstance(parts[0], IEEE1722TpAcfCanPart)
        assert parts[0].getShortName() == "CanPart1"
        assert isinstance(parts[1], IEEE1722TpAcfLinPart)
        assert parts[1].getShortName() == "LinPart1"
        assert bus.getBusId().getValue() == 7

    def test_read_bus_id_only(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CanBus</SHORT-NAME>
                <BUS-ID>42</BUS-ID>
            """,
            root_tag="IEEE-1722-TP-ACF-BUS",
        )
        bus = _concrete_bus("CanBus")
        parser.readIEEE1722TpAcfBus(element, bus)
        assert bus.getAcfParts() == []
        assert bus.getBusId().getValue() == 42

    def test_read_acf_parts_empty_wrapper(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CanBus</SHORT-NAME>
                <ACF-PARTS/>
            """,
            root_tag="IEEE-1722-TP-ACF-BUS",
        )
        bus = _concrete_bus("CanBus")
        parser.readIEEE1722TpAcfBus(element, bus)
        assert bus.getAcfParts() == []
        assert bus.getBusId() is None

    def test_read_variation_point(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CanBus</SHORT-NAME>
                <ACF-PARTS>
                    <IEEE-1722-TP-ACF-CAN-PART>
                        <SHORT-NAME>CanPart1</SHORT-NAME>
                    </IEEE-1722-TP-ACF-CAN-PART>
                </ACF-PARTS>
                <BUS-ID>1</BUS-ID>
                <VARIATION-POINT/>
            """,
            root_tag="IEEE-1722-TP-ACF-BUS",
        )
        bus = _concrete_bus("CanBus")
        parser.readIEEE1722TpAcfBus(element, bus)
        assert bus.getVariationPoint() is not None
        assert len(bus.getAcfParts()) == 1
        assert bus.getBusId().getValue() == 1

    def test_uuid_round_trip(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CanBus</SHORT-NAME>
                <BUS-ID>3</BUS-ID>
            """,
            root_tag="IEEE-1722-TP-ACF-BUS",
        )
        element.attrib["UUID"] = "c2f4d3a1-0000-4000-8000-000000000001"
        bus = _concrete_bus("CanBus")
        parser.readIEEE1722TpAcfBus(element, bus)
        assert bus.getUuid().getValue() == "c2f4d3a1-0000-4000-8000-000000000001"
