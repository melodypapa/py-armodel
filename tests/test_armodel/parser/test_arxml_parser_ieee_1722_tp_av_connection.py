"""Tests for the readIEEE1722TpAvConnection handler (R23-11 IEEE1722TpAvConnection, Table 6.276, p.639)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import IEEE1722TpAvConnection
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class _AvConn(IEEE1722TpAvConnection):
    pass


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


class TestReadIEEE1722TpAvConnection:
    """Tests for readIEEE1722TpAvConnection handler (R23-11 IEEE1722TpAvConnection, Table 6.276, p.639)."""

    def test_read_ieee_1722_tp_av_connection_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>AvStream</SHORT-NAME>
                <MAX-TRANSIT-TIME>0.001</MAX-TRANSIT-TIME>
                <SDU-REFS>
                    <SDU-REF DEST="PDU-TRIGGERING">/Pkgs/Pt1</SDU-REF>
                    <SDU-REF DEST="PDU-TRIGGERING">/Pkgs/Pt2</SDU-REF>
                </SDU-REFS>
            """,
            root_tag="IEEE-1722-TP-AV-CONNECTION",
        )
        connection = _AvConn(None, "AvStream")
        parser.readIEEE1722TpAvConnection(element, connection)
        assert connection.getShortName() == "AvStream"
        assert connection.getMaxTransitTime().getValue() == 0.001
        sdu_refs = connection.getSduRefs()
        assert len(sdu_refs) == 2
        assert sdu_refs[0].getValue() == "/Pkgs/Pt1"
        assert sdu_refs[0].getDest() == "PDU-TRIGGERING"
        assert sdu_refs[1].getValue() == "/Pkgs/Pt2"

    def test_read_ieee_1722_tp_av_connection_empty(self, parser):
        element = _snip("", root_tag="IEEE-1722-TP-AV-CONNECTION")
        connection = _AvConn(None, "AvStream")
        parser.readIEEE1722TpAvConnection(element, connection)
        assert connection.getMaxTransitTime() is None
        assert connection.getSduRefs() == []
