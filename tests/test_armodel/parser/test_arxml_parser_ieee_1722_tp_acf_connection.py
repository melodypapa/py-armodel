"""Tests for the readIEEE1722TpAcfConnection handler (R23-11 IEEE1722TpAcfConnection, Table 6.290, p.657)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import IEEE1722TpAcfConnection
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfCan,
    IEEE1722TpAcfLin,
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


class TestReadIEEE1722TpAcfConnection:
    """Tests for readIEEE1722TpAcfConnection handler (R23-11 IEEE1722TpAcfConnection, Table 6.290, p.657)."""

    def test_read_ieee_1722_tp_acf_connection_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>AcfStream</SHORT-NAME>
                <ACF-TRANSPORTED-BUSS>
                    <IEEE-1722-TP-ACF-CAN>
                        <SHORT-NAME>CanBus</SHORT-NAME>
                    </IEEE-1722-TP-ACF-CAN>
                    <IEEE-1722-TP-ACF-LIN>
                        <SHORT-NAME>LinBus</SHORT-NAME>
                    </IEEE-1722-TP-ACF-LIN>
                </ACF-TRANSPORTED-BUSS>
                <COLLECTION-THRESHOLD>900</COLLECTION-THRESHOLD>
                <COLLECTION-TIMEOUT>0.01</COLLECTION-TIMEOUT>
                <MIXED-BUS-TYPE-COLLECTION>true</MIXED-BUS-TYPE-COLLECTION>
            """,
            root_tag="IEEE-1722-TP-ACF-CONNECTION",
        )
        connection = IEEE1722TpAcfConnection(None, "AcfStream")
        parser.readIEEE1722TpAcfConnection(element, connection)
        assert connection.getShortName() == "AcfStream"
        buses = connection.getAcfTransportedBuses()
        assert len(buses) == 2
        assert isinstance(buses[0], IEEE1722TpAcfCan)
        assert buses[0].getShortName() == "CanBus"
        assert isinstance(buses[1], IEEE1722TpAcfLin)
        assert buses[1].getShortName() == "LinBus"
        assert connection.getCollectionThreshold().getValue() == 900
        assert connection.getCollectionTimeout().getValue() == 0.01
        assert connection.getMixedBusTypeCollection().getValue() is True

    def test_read_ieee_1722_tp_acf_connection_empty(self, parser):
        element = _snip("", root_tag="IEEE-1722-TP-ACF-CONNECTION")
        connection = IEEE1722TpAcfConnection(None, "AcfStream")
        parser.readIEEE1722TpAcfConnection(element, connection)
        assert connection.getAcfTransportedBuses() == []
        assert connection.getCollectionThreshold() is None
        assert connection.getCollectionTimeout() is None
        assert connection.getMixedBusTypeCollection() is None

    def test_read_acf_transported_buss_empty_wrapper(self, parser):
        element = _snip(
            """
                <SHORT-NAME>AcfStream</SHORT-NAME>
                <ACF-TRANSPORTED-BUSS/>
            """,
            root_tag="IEEE-1722-TP-ACF-CONNECTION",
        )
        connection = IEEE1722TpAcfConnection(None, "AcfStream")
        parser.readIEEE1722TpAcfConnection(element, connection)
        assert connection.getAcfTransportedBuses() == []

    def test_ar_package_dispatch(self, parser):
        element = _snip(
            """
                    <SHORT-NAME>Pkg</SHORT-NAME>
                    <ELEMENTS>
                        <IEEE-1722-TP-ACF-CONNECTION>
                            <SHORT-NAME>AcfConn</SHORT-NAME>
                            <COLLECTION-THRESHOLD>512</COLLECTION-THRESHOLD>
                        </IEEE-1722-TP-ACF-CONNECTION>
                    </ELEMENTS>
            """,
            root_tag="AR-PACKAGE",
        )
        pkg = AUTOSAR.getInstance().createARPackage("TpConfigs")
        parser.readARPackage(element, pkg)
        connections = [e for e in pkg.getReferrableElements() if e.getShortName() == "AcfConn"]
        assert len(connections) == 1
        connection = connections[0]
        assert isinstance(connection, IEEE1722TpAcfConnection)
        assert connection.getCollectionThreshold().getValue() == 512
