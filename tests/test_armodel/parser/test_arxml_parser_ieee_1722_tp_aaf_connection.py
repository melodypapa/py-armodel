"""Tests for the readIEEE1722TpAafConnection handler (R23-11 IEEE1722TpAafConnection, Table 6.280, p.643)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpAafAes3DataTypeEnum,
    IEEE1722TpAafConnection,
    IEEE1722TpAafFormatEnum,
    IEEE1722TpAafNominalRateEnum,
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


class TestReadIEEE1722TpAafConnection:
    """Tests for readIEEE1722TpAafConnection handler (R23-11 IEEE1722TpAafConnection, Table 6.280, p.643)."""

    def test_read_ieee_1722_tp_aaf_connection_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>AafStream</SHORT-NAME>
                <MAX-TRANSIT-TIME>0.002</MAX-TRANSIT-TIME>
                <SDU-REFS>
                    <SDU-REF DEST="PDU-TRIGGERING">/Pkgs/Pt1</SDU-REF>
                </SDU-REFS>
                <AAF-AES-3-DATA-TYPE>PCM</AAF-AES-3-DATA-TYPE>
                <AAF-FORMAT>AES-3-32-BIT</AAF-FORMAT>
                <AAF-NOMINAL-RATE>48-KHZ</AAF-NOMINAL-RATE>
                <AES-3-DATA-TYPE-H>2</AES-3-DATA-TYPE-H>
                <AES-3-DATA-TYPE-L>1</AES-3-DATA-TYPE-L>
                <CHANNELS-PER-FRAME>2</CHANNELS-PER-FRAME>
                <EVENT-DEFAULT-VALUE>0</EVENT-DEFAULT-VALUE>
                <PCM-BIT-DEPTH>24</PCM-BIT-DEPTH>
                <SPARSE-TIMESTAMP-ENABLED>true</SPARSE-TIMESTAMP-ENABLED>
                <STREAMS-PER-FRAME>4</STREAMS-PER-FRAME>
            """,
            root_tag="IEEE-1722-TP-AAF-CONNECTION",
        )
        connection = IEEE1722TpAafConnection(None, "AafStream")
        parser.readIEEE1722TpAafConnection(element, connection)
        assert connection.getShortName() == "AafStream"
        assert connection.getMaxTransitTime().getValue() == 0.002
        assert len(connection.getSduRefs()) == 1
        assert connection.getSduRefs()[0].getValue() == "/Pkgs/Pt1"
        assert connection.getAafAes3DataType().getValue() == IEEE1722TpAafAes3DataTypeEnum.ENUM_PCM
        assert connection.getAafFormat().getValue() == IEEE1722TpAafFormatEnum.AES3_32BIT
        assert connection.getAafNominalRate().getValue() == IEEE1722TpAafNominalRateEnum.ENUM_48KHZ
        assert connection.getAes3DataTypeH().getValue() == 2
        assert connection.getAes3DataTypeL().getValue() == 1
        assert connection.getChannelsPerFrame().getValue() == 2
        assert connection.getEventDefaultValue().getValue() == 0
        assert connection.getPcmBitDepth().getValue() == 24
        assert connection.getSparseTimestampEnabled().getValue() is True
        assert connection.getStreamsPerFrame().getValue() == 4

    def test_read_ieee_1722_tp_aaf_connection_empty(self, parser):
        element = _snip("", root_tag="IEEE-1722-TP-AAF-CONNECTION")
        connection = IEEE1722TpAafConnection(None, "AafStream")
        parser.readIEEE1722TpAafConnection(element, connection)
        assert connection.getAafAes3DataType() is None
        assert connection.getAafFormat() is None
        assert connection.getAafNominalRate() is None
        assert connection.getAes3DataTypeH() is None
        assert connection.getAes3DataTypeL() is None
        assert connection.getChannelsPerFrame() is None
        assert connection.getEventDefaultValue() is None
        assert connection.getPcmBitDepth() is None
        assert connection.getSparseTimestampEnabled() is None
        assert connection.getStreamsPerFrame() is None

    def test_ar_package_dispatch(self, parser):
        element = _snip(
            """
                    <SHORT-NAME>Pkg</SHORT-NAME>
                    <ELEMENTS>
                        <IEEE-1722-TP-AAF-CONNECTION>
                            <SHORT-NAME>AafConn</SHORT-NAME>
                            <AAF-NOMINAL-RATE>16-KHZ</AAF-NOMINAL-RATE>
                        </IEEE-1722-TP-AAF-CONNECTION>
                    </ELEMENTS>
            """,
            root_tag="AR-PACKAGE",
        )
        pkg = AUTOSAR.getInstance().createARPackage("TpConfigs")
        parser.readARPackage(element, pkg)
        connections = [e for e in pkg.getReferrableElements() if e.getShortName() == "AafConn"]
        assert len(connections) == 1
        connection = connections[0]
        assert isinstance(connection, IEEE1722TpAafConnection)
        assert connection.getAafNominalRate().getValue() == IEEE1722TpAafNominalRateEnum.ENUM_16KHZ
