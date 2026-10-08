"""Tests for the readIEEE1722TpConfig handler (R23-11 IEEE1722TpConfig, Table 6.274, p.637)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import IEEE1722TpConfig
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


class TestReadIEEE1722TpConfig:
    """Tests for readIEEE1722TpConfig handler (R23-11 IEEE1722TpConfig, Table 6.274, p.637)."""

    def test_read_ieee_1722_tp_config_full(self, parser):
        element = _snip(
            """
                <IDENT>
                    <SHORT-NAME>Ieee1722Config</SHORT-NAME>
                </IDENT>
                <COMMUNICATION-CLUSTER-REF DEST="ETHERNET-PHYSICAL-CHANNEL">/Clusters/EthCh</COMMUNICATION-CLUSTER-REF>
                <TP-CONNECTIONS>
                    <IEEE-1722-TP-CONNECTION-REF-CONDITIONAL>
                        <IEEE-1722-TP-CONNECTION-REF DEST="IEEE-1722-TP-CRF-CONNECTION">/Pkgs/CrfConn</IEEE-1722-TP-CONNECTION-REF>
                    </IEEE-1722-TP-CONNECTION-REF-CONDITIONAL>
                    <IEEE-1722-TP-CONNECTION-REF-CONDITIONAL>
                        <IEEE-1722-TP-CONNECTION-REF DEST="IEEE-1722-TP-AV-CONNECTION">/Pkgs/AvConn</IEEE-1722-TP-CONNECTION-REF>
                    </IEEE-1722-TP-CONNECTION-REF-CONDITIONAL>
                </TP-CONNECTIONS>
            """,
            root_tag="IEEE-1722-TP-CONFIG",
        )
        config = IEEE1722TpConfig(None, "Ieee1722Config")
        parser.readIEEE1722TpConfig(element, config)
        assert config.getCommunicationClusterRef() is not None
        assert config.getCommunicationClusterRef().getValue() == "/Clusters/EthCh"
        refs = config.getTpConnectionRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/Pkgs/CrfConn"
        assert refs[0].getDest() == "IEEE-1722-TP-CRF-CONNECTION"
        assert refs[1].getValue() == "/Pkgs/AvConn"

    def test_read_ieee_1722_tp_config_empty(self, parser):
        element = _snip("", root_tag="IEEE-1722-TP-CONFIG")
        config = IEEE1722TpConfig(None, "Ieee1722Config")
        parser.readIEEE1722TpConfig(element, config)
        assert config.getCommunicationClusterRef() is None
        assert config.getTpConnectionRefs() == []
