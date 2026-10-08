"""Tests for the writeIEEE1722TpAvConnection handler (R23-11 IEEE1722TpAvConnection, Table 6.276, p.639)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import IEEE1722TpAvConnection
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "SHORT-NAME",
    "MAX-TRANSIT-TIME",
    "SDU-REFS",
]


class _AvConn(IEEE1722TpAvConnection):
    pass


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


def _time(value):
    t = TimeValue()
    t.setValue(value)
    return t


def _fill_connection(connection: IEEE1722TpAvConnection) -> IEEE1722TpAvConnection:
    connection.setMaxTransitTime(_time(0.001))
    connection.addSduRef(_ref("/Pkgs/Pt1", "PDU-TRIGGERING"))
    connection.addSduRef(_ref("/Pkgs/Pt2", "PDU-TRIGGERING"))
    return connection


class TestWriteIEEE1722TpAvConnection:
    """Tests for writeIEEE1722TpAvConnection handler (R23-11 IEEE1722TpAvConnection, Table 6.276, p.639)."""

    def test_children_in_xsd_order(self, writer):
        connection = _fill_connection(_AvConn(None, "AvStream"))

        parent = _parent()
        writer.writeIEEE1722TpAvConnection(parent, connection)
        child_tags = [element.tag for element in parent]
        assert child_tags == XSD_CHILD_ORDER

    def test_field_values_in_xml(self, writer):
        connection = _fill_connection(_AvConn(None, "AvStream"))

        parent = _parent()
        writer.writeIEEE1722TpAvConnection(parent, connection)
        assert parent.find("MAX-TRANSIT-TIME").text == "0.001"
        sdu_refs = parent.findall("SDU-REFS/SDU-REF")
        assert len(sdu_refs) == 2
        assert sdu_refs[0].text == "/Pkgs/Pt1"
        assert sdu_refs[0].get("DEST") == "PDU-TRIGGERING"
        assert sdu_refs[1].text == "/Pkgs/Pt2"

    def test_empty_connection_writes_only_short_name(self, writer):
        connection = _AvConn(None, "AvStream")

        parent = _parent()
        writer.writeIEEE1722TpAvConnection(parent, connection)
        assert [element.tag for element in parent] == ["SHORT-NAME"]
        assert parent.find("SDU-REFS") is None

    def test_round_trip(self, writer, parser):
        connection = _fill_connection(_AvConn(None, "AvStream"))

        parent = _parent()
        writer.writeIEEE1722TpAvConnection(parent, connection)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = _AvConn(None, "AvStream")
        parser.readIEEE1722TpAvConnection(element, reloaded)
        assert reloaded.getMaxTransitTime().getValue() == 0.001
        sdu_refs = reloaded.getSduRefs()
        assert len(sdu_refs) == 2
        assert sdu_refs[0].getValue() == "/Pkgs/Pt1"
        assert sdu_refs[0].getDest() == "PDU-TRIGGERING"
        assert sdu_refs[1].getValue() == "/Pkgs/Pt2"
