"""Tests for the writeIEEE1722TpAcfConnection handler (R23-11 IEEE1722TpAcfConnection, Table 6.290, p.657)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import IEEE1722TpAcfConnection
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "SHORT-NAME",
    "ACF-TRANSPORTED-BUSS",
    "COLLECTION-THRESHOLD",
    "COLLECTION-TIMEOUT",
    "MIXED-BUS-TYPE-COLLECTION",
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


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _time(value):
    t = TimeValue()
    t.setValue(value)
    return t


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _fill_connection(connection: IEEE1722TpAcfConnection) -> IEEE1722TpAcfConnection:
    connection.createIEEE1722TpAcfCan("CanBus")
    connection.createIEEE1722TpAcfLin("LinBus")
    connection.setCollectionThreshold(_pos_int(900))
    connection.setCollectionTimeout(_time(0.01))
    connection.setMixedBusTypeCollection(_bool(True))
    return connection


class TestWriteIEEE1722TpAcfConnection:
    """Tests for writeIEEE1722TpAcfConnection handler (R23-11 IEEE1722TpAcfConnection, Table 6.290, p.657)."""

    def test_children_in_xsd_order(self, writer):
        connection = _fill_connection(IEEE1722TpAcfConnection(None, "AcfStream"))

        parent = _parent()
        writer.writeIEEE1722TpAcfConnection(parent, connection)
        child = parent.find("IEEE-1722-TP-ACF-CONNECTION")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER

    def test_field_values_in_xml(self, writer):
        connection = _fill_connection(IEEE1722TpAcfConnection(None, "AcfStream"))

        parent = _parent()
        writer.writeIEEE1722TpAcfConnection(parent, connection)
        child = parent.find("IEEE-1722-TP-ACF-CONNECTION")
        buses = child.find("ACF-TRANSPORTED-BUSS")
        assert buses is not None
        bus_tags = [(element.tag, element.find("SHORT-NAME").text) for element in buses]
        assert bus_tags == [
            ("IEEE-1722-TP-ACF-CAN", "CanBus"),
            ("IEEE-1722-TP-ACF-LIN", "LinBus"),
        ]
        assert child.find("COLLECTION-THRESHOLD").text == "900"
        assert child.find("COLLECTION-TIMEOUT").text == "0.01"
        assert child.find("MIXED-BUS-TYPE-COLLECTION").text == "true"

    def test_empty_connection_writes_only_identifiable(self, writer):
        connection = IEEE1722TpAcfConnection(None, "AcfStream")

        parent = _parent()
        writer.writeIEEE1722TpAcfConnection(parent, connection)
        child = parent.find("IEEE-1722-TP-ACF-CONNECTION")
        assert child is not None
        assert [element.tag for element in child] == ["SHORT-NAME"]

    def test_round_trip(self, writer, parser):
        connection = _fill_connection(IEEE1722TpAcfConnection(None, "AcfStream"))

        parent = _parent()
        writer.writeIEEE1722TpAcfConnection(parent, connection)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = IEEE1722TpAcfConnection(None, "AcfStream")
        parser.readIEEE1722TpAcfConnection(element, reloaded)
        buses = reloaded.getAcfTransportedBuses()
        assert len(buses) == 2
        assert buses[0].getShortName() == "CanBus"
        assert buses[1].getShortName() == "LinBus"
        assert reloaded.getCollectionThreshold().getValue() == 900
        assert reloaded.getCollectionTimeout().getValue() == 0.01
        assert reloaded.getMixedBusTypeCollection().getValue() is True

    def test_ar_package_round_trip(self, writer, parser):
        pkg = AUTOSAR.getInstance().createARPackage("TpConfigs")
        connection = pkg.createIEEE1722TpAcfConnection("AcfConn")
        connection.setCollectionThreshold(_pos_int(512))

        root = ET.Element("ROOT")
        writer.writeARPackage(root, pkg)
        raw = ET.tostring(root).decode("utf-8").replace("<AR-PACKAGE>", "<AR-PACKAGE xmlns='%s'>" % NS, 1)
        element = ET.fromstring(raw)[0]

        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        reloaded_pkg = AUTOSAR.getInstance().createARPackage("TpConfigs")
        parser.readARPackage(element, reloaded_pkg)
        connections = [e for e in reloaded_pkg.getReferrableElements() if e.getShortName() == "AcfConn"]
        assert len(connections) == 1
        reloaded = connections[0]
        assert isinstance(reloaded, IEEE1722TpAcfConnection)
        assert reloaded.getCollectionThreshold().getValue() == 512
