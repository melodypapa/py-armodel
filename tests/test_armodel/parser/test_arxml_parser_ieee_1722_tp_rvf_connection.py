"""Tests for the readIEEE1722TpRvfConnection handler (R23-11 IEEE1722TpRvfConnection, Table 6.285, p.650)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import (
    IEEE1722TpRvfConnection,
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


class TestReadIEEE1722TpRvfConnection:
    """Tests for readIEEE1722TpRvfConnection handler (R23-11 IEEE1722TpRvfConnection, Table 6.285, p.650)."""

    def test_read_ieee_1722_tp_rvf_connection_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>RvfStream</SHORT-NAME>
                <MAX-TRANSIT-TIME>0.002</MAX-TRANSIT-TIME>
                <SDU-REFS>
                    <SDU-REF DEST="PDU-TRIGGERING">/Pkgs/Pt1</SDU-REF>
                </SDU-REFS>
                <RVF-ACTIVE-PIXELS>1920</RVF-ACTIVE-PIXELS>
                <RVF-COLOR-SPACE>YCBCR</RVF-COLOR-SPACE>
                <RVF-EVENT-DEFAULT>8</RVF-EVENT-DEFAULT>
                <RVF-FRAME-RATE>60</RVF-FRAME-RATE>
                <RVF-INTERLACED>true</RVF-INTERLACED>
                <RVF-PIXEL-DEPTH>10</RVF-PIXEL-DEPTH>
                <RVF-PIXEL-FORMAT>4-2-0</RVF-PIXEL-FORMAT>
                <RVF-TOTAL-LINES>1080</RVF-TOTAL-LINES>
            """,
            root_tag="IEEE-1722-TP-RVF-CONNECTION",
        )
        connection = IEEE1722TpRvfConnection(None, "RvfStream")
        parser.readIEEE1722TpRvfConnection(element, connection)
        assert connection.getShortName() == "RvfStream"
        assert connection.getMaxTransitTime().getValue() == 0.002
        assert len(connection.getSduRefs()) == 1
        assert connection.getSduRefs()[0].getValue() == "/Pkgs/Pt1"
        assert connection.getRvfActivePixels().getValue() == 1920
        assert connection.getRvfColorSpace().getValue() == "YCBCR"
        assert connection.getRvfEventDefault().getValue() == 8
        assert connection.getRvfFrameRate().getValue() == "60"
        assert connection.getRvfInterlaced().getValue() is True
        assert connection.getRvfPixelDepth().getValue() == "10"
        assert connection.getRvfPixelFormat().getValue() == "4-2-0"
        assert connection.getRvfTotalLines().getValue() == 1080

    def test_read_ieee_1722_tp_rvf_connection_empty(self, parser):
        element = _snip("", root_tag="IEEE-1722-TP-RVF-CONNECTION")
        connection = IEEE1722TpRvfConnection(None, "RvfStream")
        parser.readIEEE1722TpRvfConnection(element, connection)
        assert connection.getRvfActivePixels() is None
        assert connection.getRvfColorSpace() is None
        assert connection.getRvfEventDefault() is None
        assert connection.getRvfFrameRate() is None
        assert connection.getRvfInterlaced() is None
        assert connection.getRvfPixelDepth() is None
        assert connection.getRvfPixelFormat() is None
        assert connection.getRvfTotalLines() is None

    def test_ar_package_dispatch(self, parser):
        element = _snip(
            """
                    <SHORT-NAME>Pkg</SHORT-NAME>
                    <ELEMENTS>
                        <IEEE-1722-TP-RVF-CONNECTION>
                            <SHORT-NAME>RvfConn</SHORT-NAME>
                            <RVF-ACTIVE-PIXELS>640</RVF-ACTIVE-PIXELS>
                        </IEEE-1722-TP-RVF-CONNECTION>
                    </ELEMENTS>
            """,
            root_tag="AR-PACKAGE",
        )
        pkg = AUTOSAR.getInstance().createARPackage("TpConfigs")
        parser.readARPackage(element, pkg)
        connections = [e for e in pkg.getReferrableElements() if e.getShortName() == "RvfConn"]
        assert len(connections) == 1
        connection = connections[0]
        assert isinstance(connection, IEEE1722TpRvfConnection)
        assert connection.getRvfActivePixels().getValue() == 640
