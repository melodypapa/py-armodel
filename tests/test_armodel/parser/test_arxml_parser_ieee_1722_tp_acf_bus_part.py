"""Tests for the readIEEE1722TpAcfBusPart handler (R23-11 IEEE1722TpAcfBusPart, Table 6.292, p.658)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import PduCollectionTriggerEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import IEEE1722TpAcfCanPart
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


class TestReadIEEE1722TpAcfBusPart:
    """Tests for readIEEE1722TpAcfBusPart handler (R23-11 IEEE1722TpAcfBusPart, Table 6.292, p.658)."""

    def test_read_collection_trigger(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CanPart1</SHORT-NAME>
                <COLLECTION-TRIGGER>ALWAYS</COLLECTION-TRIGGER>
            """,
            root_tag="IEEE-1722-TP-ACF-CAN-PART",
        )
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        parser.readIEEE1722TpAcfCanPart(element, part)
        assert part.getShortName() == "CanPart1"
        assert part.getCollectionTrigger() is not None
        assert part.getCollectionTrigger().getValue() == PduCollectionTriggerEnum.ALWAYS

    def test_read_collection_trigger_never(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CanPart1</SHORT-NAME>
                <COLLECTION-TRIGGER>NEVER</COLLECTION-TRIGGER>
            """,
            root_tag="IEEE-1722-TP-ACF-CAN-PART",
        )
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        parser.readIEEE1722TpAcfCanPart(element, part)
        assert part.getCollectionTrigger().getValue() == PduCollectionTriggerEnum.NEVER

    def test_read_empty_part(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CanPart1</SHORT-NAME>
            """,
            root_tag="IEEE-1722-TP-ACF-CAN-PART",
        )
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        parser.readIEEE1722TpAcfCanPart(element, part)
        assert part.getCollectionTrigger() is None
        assert part.getVariationPoint() is None

    def test_read_variation_point(self, parser):
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
        assert part.getCollectionTrigger().getValue() == PduCollectionTriggerEnum.ALWAYS
        assert part.getVariationPoint() is not None
