"""Tests for the writeJ1939TpPg handler (R23-11 J1939TpPg, Table 6.269, p.626)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import J1939TpPg
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "DIRECT-PDU-REF",
    "PGN",
    "REQUESTABLE",
    "SDU-REFS",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _int(value):
    integer = Integer()
    integer.setValue(str(value))
    return integer


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


def _fill_pg(pg: J1939TpPg) -> J1939TpPg:
    pg.setDirectPduRef(_ref("/Pdus/Direct"))
    pg.setPgn(_int(61444))
    pg.setRequestable(_bool(True))
    pg.addSduRef(_ref("/Pdus/Sdu1"))
    pg.addSduRef(_ref("/Pdus/Sdu2"))
    return pg


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteJ1939TpPg:
    def test_children_in_xsd_order(self):
        pg = _fill_pg(J1939TpPg())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939TpPg(parent, pg)

        child = parent.find("J-1939-TP-PG")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER
        assert len(child.findall("SDU-REFS/SDU-REF")) == 2

    def test_empty_pg_writes_no_wrappers(self):
        pg = J1939TpPg()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939TpPg(parent, pg)

        child = parent.find("J-1939-TP-PG")
        assert child is not None
        assert [element.tag for element in child] == []

    def test_round_trip(self):
        pg = _fill_pg(J1939TpPg())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939TpPg(parent, pg)

        reloaded = J1939TpPg()
        ARXMLParser().readJ1939TpPg(_with_ns(parent)[0], reloaded)

        assert reloaded.getDirectPduRef().getValue() == "/Pdus/Direct"
        assert reloaded.getPgn().getValue() == 61444
        assert reloaded.getRequestable().getValue() is True
        sdu_refs = reloaded.getSduRefs()
        assert len(sdu_refs) == 2
        assert sdu_refs[0].getValue() == "/Pdus/Sdu1"
        assert sdu_refs[1].getValue() == "/Pdus/Sdu2"

    def test_round_trip_empty(self):
        pg = J1939TpPg()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939TpPg(parent, pg)

        reloaded = J1939TpPg()
        ARXMLParser().readJ1939TpPg(_with_ns(parent)[0], reloaded)

        assert reloaded.getDirectPduRef() is None
        assert reloaded.getPgn() is None
        assert reloaded.getRequestable() is None
        assert reloaded.getSduRefs() == []
