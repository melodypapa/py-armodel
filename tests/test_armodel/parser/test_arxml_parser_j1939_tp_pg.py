"""Tests for the readJ1939TpPg handler (R23-11 J1939TpPg, Table 6.269, p.626).

XSD element order (J-1939-TP-PG group, AUTOSAR_00052.xsd l.75976): DIRECT-PDU-REF, PGN,
REQUESTABLE, SDU-REFS (XSD-only TP-SDU-REF carries atp.Status="removed" — not modeled).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import J1939TpPg
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

PG_XML = (
    "<J-1939-TP-PG>"
    '<DIRECT-PDU-REF DEST="N-PDU">/Pdus/Direct</DIRECT-PDU-REF>'
    "<PGN>61444</PGN>"
    "<REQUESTABLE>true</REQUESTABLE>"
    "<SDU-REFS>"
    '<SDU-REF DEST="I-PDU">/Pdus/Sdu1</SDU-REF>'
    '<SDU-REF DEST="I-PDU">/Pdus/Sdu2</SDU-REF>'
    "</SDU-REFS>"
    "</J-1939-TP-PG>"
)

EMPTY_PG_XML = "<J-1939-TP-PG />"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    xml = "<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner)
    return ET.fromstring(xml)


class TestReadJ1939TpPg:
    def test_read_full(self):
        pg = J1939TpPg()
        root = _snip(PG_XML)
        ARXMLParser().readJ1939TpPg(root[0], pg)

        direct_pdu_ref = pg.getDirectPduRef()
        assert direct_pdu_ref.getValue() == "/Pdus/Direct"
        assert direct_pdu_ref.getDest() == "N-PDU"

        assert pg.getPgn() is not None
        assert pg.getPgn().getValue() == 61444

        assert pg.getRequestable() is not None
        assert pg.getRequestable().getValue() is True

        sdu_refs = pg.getSduRefs()
        assert len(sdu_refs) == 2
        assert sdu_refs[0].getValue() == "/Pdus/Sdu1"
        assert sdu_refs[0].getDest() == "I-PDU"
        assert sdu_refs[1].getValue() == "/Pdus/Sdu2"

    def test_read_empty(self):
        pg = J1939TpPg()
        root = _snip(EMPTY_PG_XML)
        ARXMLParser().readJ1939TpPg(root[0], pg)

        assert pg.getDirectPduRef() is None
        assert pg.getPgn() is None
        assert pg.getRequestable() is None
        assert pg.getSduRefs() == []
