"""Tests for the readIEEE1722TpCrfConnection handler (R23-11 IEEE1722TpCrfConnection, Table 6.277, p.640)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpCrfConnection,
    IEEE1722TpCrfPullEnum,
    IEEE1722TpCrfTypeEnum,
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


class TestReadIEEE1722TpCrfConnection:
    """Tests for readIEEE1722TpCrfConnection handler (R23-11 IEEE1722TpCrfConnection, Table 6.277, p.640)."""

    def test_read_ieee_1722_tp_crf_connection_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>CrfStream</SHORT-NAME>
                <MAX-TRANSIT-TIME>0.002</MAX-TRANSIT-TIME>
                <SDU-REFS>
                    <SDU-REF DEST="PDU-TRIGGERING">/Pkgs/Pt1</SDU-REF>
                </SDU-REFS>
                <BASE-FREQUENCY>8000</BASE-FREQUENCY>
                <CRF-PULL>1-0</CRF-PULL>
                <CRF-TYPE>VIDEO-FRAME</CRF-TYPE>
                <FRAME-SYNC-ENABLED>true</FRAME-SYNC-ENABLED>
                <TIMESTAMP-INTERVAL>4</TIMESTAMP-INTERVAL>
            """,
            root_tag="IEEE-1722-TP-CRF-CONNECTION",
        )
        connection = IEEE1722TpCrfConnection(None, "CrfStream")
        parser.readIEEE1722TpCrfConnection(element, connection)
        assert connection.getShortName() == "CrfStream"
        assert connection.getMaxTransitTime().getValue() == 0.002
        assert len(connection.getSduRefs()) == 1
        assert connection.getSduRefs()[0].getValue() == "/Pkgs/Pt1"
        assert connection.getBaseFrequency().getValue() == 8000
        assert connection.getCrfPull().getValue() == IEEE1722TpCrfPullEnum.ENUM_1_0
        assert connection.getCrfType().getValue() == IEEE1722TpCrfTypeEnum.ENUM_VIDEO_FRAME
        assert connection.getFrameSyncEnabled().getValue() is True
        assert connection.getTimestampInterval().getValue() == 4

    def test_read_ieee_1722_tp_crf_connection_empty(self, parser):
        element = _snip("", root_tag="IEEE-1722-TP-CRF-CONNECTION")
        connection = IEEE1722TpCrfConnection(None, "CrfStream")
        parser.readIEEE1722TpCrfConnection(element, connection)
        assert connection.getBaseFrequency() is None
        assert connection.getCrfPull() is None
        assert connection.getCrfType() is None
        assert connection.getFrameSyncEnabled() is None
        assert connection.getTimestampInterval() is None

    def test_ar_package_dispatch(self, parser):
        element = _snip(
            """
                    <SHORT-NAME>Pkg</SHORT-NAME>
                    <ELEMENTS>
                        <IEEE-1722-TP-CRF-CONNECTION>
                            <SHORT-NAME>CrfConn</SHORT-NAME>
                            <BASE-FREQUENCY>48000</BASE-FREQUENCY>
                        </IEEE-1722-TP-CRF-CONNECTION>
                    </ELEMENTS>
            """,
            root_tag="AR-PACKAGE",
        )
        pkg = AUTOSAR.getInstance().createARPackage("TpConfigs")
        parser.readARPackage(element, pkg)
        connections = [e for e in pkg.getReferrableElements() if e.getShortName() == "CrfConn"]
        assert len(connections) == 1
        connection = connections[0]
        assert isinstance(connection, IEEE1722TpCrfConnection)
        assert connection.getBaseFrequency().getValue() == 48000
