"""Tests for the writeIEEE1722TpConfig handler (R23-11 IEEE1722TpConfig, Table 6.274, p.637)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import IEEE1722TpConfig
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "SHORT-NAME",
    "COMMUNICATION-CLUSTER-REF",
    "TP-CONNECTIONS",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _fill_config(config: IEEE1722TpConfig) -> IEEE1722TpConfig:
    config.setCommunicationClusterRef(_ref("/Clusters/EthCh", "ETHERNET-PHYSICAL-CHANNEL"))
    config.addTpConnectionRef(_ref("/Pkgs/CrfConn", "IEEE-1722-TP-CRF-CONNECTION"))
    config.addTpConnectionRef(_ref("/Pkgs/AvConn", "IEEE-1722-TP-AV-CONNECTION"))
    return config


class TestWriteIEEE1722TpConfig:
    """Tests for writeIEEE1722TpConfig handler (R23-11 IEEE1722TpConfig, Table 6.274, p.637)."""

    def test_children_in_xsd_order(self, writer):
        config = _fill_config(IEEE1722TpConfig(None, "Ieee1722Config"))

        parent = _parent()
        writer.writeIEEE1722TpConfig(parent, config)
        child = parent.find("IEEE-1722-TP-CONFIG")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER

    def test_field_values_in_xml(self, writer):
        config = _fill_config(IEEE1722TpConfig(None, "Ieee1722Config"))

        parent = _parent()
        writer.writeIEEE1722TpConfig(parent, config)
        child = parent.find("IEEE-1722-TP-CONFIG")
        assert child.find("COMMUNICATION-CLUSTER-REF").text == "/Clusters/EthCh"
        refs = child.findall("TP-CONNECTIONS/IEEE-1722-TP-CONNECTION-REF-CONDITIONAL/IEEE-1722-TP-CONNECTION-REF")
        assert len(refs) == 2
        assert refs[0].text == "/Pkgs/CrfConn"
        assert refs[0].get("DEST") == "IEEE-1722-TP-CRF-CONNECTION"
        assert refs[1].text == "/Pkgs/AvConn"

    def test_empty_config_writes_no_tp_connections(self, writer):
        config = IEEE1722TpConfig(None, "Ieee1722Config")

        parent = _parent()
        writer.writeIEEE1722TpConfig(parent, config)
        child = parent.find("IEEE-1722-TP-CONFIG")
        assert child is not None
        assert child.find("TP-CONNECTIONS") is None

    def test_round_trip(self, writer, parser):
        config = _fill_config(IEEE1722TpConfig(None, "Ieee1722Config"))

        parent = _parent()
        writer.writeIEEE1722TpConfig(parent, config)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = IEEE1722TpConfig(None, "Ieee1722Config")
        parser.readIEEE1722TpConfig(element, reloaded)
        assert reloaded.getCommunicationClusterRef() is not None
        assert reloaded.getCommunicationClusterRef().getValue() == "/Clusters/EthCh"
        refs = reloaded.getTpConnectionRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/Pkgs/CrfConn"
        assert refs[0].getDest() == "IEEE-1722-TP-CRF-CONNECTION"
        assert refs[1].getValue() == "/Pkgs/AvConn"
        assert refs[1].getDest() == "IEEE-1722-TP-AV-CONNECTION"
