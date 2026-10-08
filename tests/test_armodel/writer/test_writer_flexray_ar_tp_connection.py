"""Tests for the writeFlexrayArTpConnection handler (R23-11 FlexrayArTpConnection, Table 6.248, p.603)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayArTpConnection
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "IDENT",
    "CONNECTION-PRIO-PDUS",
    "DIRECT-TP-SDU-REF",
    "MULTICAST-REF",
    "REVERSED-TP-SDU-REF",
    "SOURCE-REF",
    "TARGET-REFS",
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


def _fill_connection(connection: FlexrayArTpConnection) -> FlexrayArTpConnection:
    connection.createTpConnectionIdent("FrArConnIdent")
    priority = Integer()
    priority.setValue("8")
    connection.setConnectionPrioPdus(priority)
    connection.setDirectTpSduRef(_ref("/Pdus/DirectSdu", "I-PDU"))
    connection.setMulticastRef(_ref("/TpAddresses/Mcast", "TP-ADDRESS"))
    connection.setReversedTpSduRef(_ref("/Pdus/ReversedSdu", "I-PDU"))
    connection.setSourceRef(_ref("/TpNodes/Src", "FLEXRAY-AR-TP-NODE"))
    connection.addTargetRef(_ref("/TpNodes/Tgt1", "FLEXRAY-AR-TP-NODE"))
    connection.addTargetRef(_ref("/TpNodes/Tgt2", "FLEXRAY-AR-TP-NODE"))
    return connection


class TestWriteFlexrayArTpConnection:
    """Tests for writeFlexrayArTpConnection handler (R23-11 FlexrayArTpConnection, Table 6.248, p.603)."""

    def test_children_in_xsd_order(self, writer):
        connection = _fill_connection(FlexrayArTpConnection())

        parent = _parent()
        writer.writeFlexrayArTpConnection(parent, connection)
        child = parent.find("FLEXRAY-AR-TP-CONNECTION")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER

    def test_field_values_in_xml(self, writer):
        connection = _fill_connection(FlexrayArTpConnection())

        parent = _parent()
        writer.writeFlexrayArTpConnection(parent, connection)
        child = parent.find("FLEXRAY-AR-TP-CONNECTION")
        assert child.find("IDENT/SHORT-NAME").text == "FrArConnIdent"
        assert child.find("CONNECTION-PRIO-PDUS").text == "8"
        direct_ref = child.find("DIRECT-TP-SDU-REF")
        assert direct_ref.text == "/Pdus/DirectSdu"
        assert direct_ref.get("DEST") == "I-PDU"
        assert child.find("MULTICAST-REF").text == "/TpAddresses/Mcast"
        assert child.find("MULTICAST-REF").get("DEST") == "TP-ADDRESS"
        assert child.find("REVERSED-TP-SDU-REF").text == "/Pdus/ReversedSdu"
        assert child.find("SOURCE-REF").text == "/TpNodes/Src"
        assert child.find("SOURCE-REF").get("DEST") == "FLEXRAY-AR-TP-NODE"
        targets = child.findall("TARGET-REFS/TARGET-REF")
        assert len(targets) == 2
        assert targets[0].text == "/TpNodes/Tgt1"
        assert targets[0].get("DEST") == "FLEXRAY-AR-TP-NODE"
        assert targets[1].text == "/TpNodes/Tgt2"

    def test_empty_connection_writes_no_own_elements(self, writer):
        connection = FlexrayArTpConnection()

        parent = _parent()
        writer.writeFlexrayArTpConnection(parent, connection)
        child = parent.find("FLEXRAY-AR-TP-CONNECTION")
        assert child is not None
        assert len(list(child)) == 0

    def test_round_trip(self, writer, parser):
        connection = _fill_connection(FlexrayArTpConnection())

        parent = _parent()
        writer.writeFlexrayArTpConnection(parent, connection)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = FlexrayArTpConnection()
        parser.readFlexrayArTpConnection(element, reloaded)
        assert reloaded.getIdent() is not None
        assert reloaded.getIdent().getShortName() == "FrArConnIdent"
        assert reloaded.getConnectionPrioPdus().getValue() == 8
        assert reloaded.getDirectTpSduRef().getValue() == "/Pdus/DirectSdu"
        assert reloaded.getDirectTpSduRef().getDest() == "I-PDU"
        assert reloaded.getMulticastRef().getValue() == "/TpAddresses/Mcast"
        assert reloaded.getReversedTpSduRef().getValue() == "/Pdus/ReversedSdu"
        assert reloaded.getSourceRef().getValue() == "/TpNodes/Src"
        assert len(reloaded.getTargetRefs()) == 2
        assert reloaded.getTargetRefs()[0].getValue() == "/TpNodes/Tgt1"
        assert reloaded.getTargetRefs()[1].getValue() == "/TpNodes/Tgt2"
