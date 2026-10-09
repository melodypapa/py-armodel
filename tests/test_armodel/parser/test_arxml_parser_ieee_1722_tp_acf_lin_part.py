"""Tests for the readIEEE1722TpAcfLinPart handler (R23-11 IEEE1722TpAcfLinPart, Table 6.297, p.667)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
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


class TestReadIEEE1722TpAcfLinPart:
    """Tests for readIEEE1722TpAcfLinPart handler (R23-11 IEEE1722TpAcfLinPart, Table 6.297, p.667)."""

    def test_read_lin_identifier_and_sdu_ref(self, parser):
        element = _snip(
            """
                <SHORT-NAME>LinPart1</SHORT-NAME>
                <LIN-IDENTIFIER>63</LIN-IDENTIFIER>
                <SDU-REF DEST="PDU-TRIGGERING-REF">/Pkg/PduTriggering</SDU-REF>
            """,
            root_tag="IEEE-1722-TP-ACF-LIN-PART",
        )
        part = IEEE1722TpAcfLinPart(None, "LinPart1")
        parser.readIEEE1722TpAcfLinPart(element, part)
        assert part.getLinIdentifier() is not None
        assert part.getLinIdentifier().getValue() == 63
        assert part.getSduRef() is not None
        assert part.getSduRef().getValue() == "/Pkg/PduTriggering"
        assert part.getSduRef().getDest() == "PDU-TRIGGERING-REF"

    def test_read_base_levels_exactly_once(self, parser):
        element = _snip(
            """
                <SHORT-NAME>LinPart1</SHORT-NAME>
                <COLLECTION-TRIGGER>ALWAYS</COLLECTION-TRIGGER>
                <VARIATION-POINT/>
                <LIN-IDENTIFIER>7</LIN-IDENTIFIER>
            """,
            root_tag="IEEE-1722-TP-ACF-LIN-PART",
        )
        part = IEEE1722TpAcfLinPart(None, "LinPart1")
        parser.readIEEE1722TpAcfLinPart(element, part)
        assert part.getShortName() == "LinPart1"
        assert part.getCollectionTrigger() is not None
        assert part.getCollectionTrigger().getValue() == "ALWAYS"
        assert part.getVariationPoint() is not None
        assert part.getLinIdentifier().getValue() == 7

    def test_read_fields_absent(self, parser):
        element = _snip(
            """
                <SHORT-NAME>LinPart1</SHORT-NAME>
            """,
            root_tag="IEEE-1722-TP-ACF-LIN-PART",
        )
        part = IEEE1722TpAcfLinPart(None, "LinPart1")
        parser.readIEEE1722TpAcfLinPart(element, part)
        assert part.getLinIdentifier() is None
        assert part.getSduRef() is None
