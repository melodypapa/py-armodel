"""Writer round-trip tests for Pdu (Table 6.17, p.340).

Serialized through the reusable writePdu helper (the PDU group of AUTOSAR_00052.xsd,
l.88521); child order per that group. Pdu is abstract: the tests exercise the helper
through a concrete subclass, the same way concrete Pdu subclasses call it.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Pdu
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "HAS-DYNAMIC-LENGTH",
    "LENGTH",
]


class ConcretePdu(Pdu):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PDU>", "<PDU xmlns='%s'>" % NS, 1))


def _populate(pdu: Pdu):
    value = Boolean()
    value.setValue(True)
    pdu.setHasDynamicLength(value)

    length = UnlimitedInteger()
    length.setValue("8")
    pdu.setLength(length)


def _write(pdu: Pdu) -> ET.Element:
    parent = ET.Element("PDU")
    ARXMLWriter().writePdu(parent, pdu)
    return parent


class TestWritePdu:
    def test_write_empty(self):
        pdu = ConcretePdu(None, "Pdu1")
        node = _write(pdu)

        for tag in XSD_CHILD_ORDER:
            assert node.find(tag) is None, tag

    def test_write_full_child_order_matches_xsd(self):
        pdu = ConcretePdu(None, "Pdu1")
        _populate(pdu)

        node = _write(pdu)
        tags = [child.tag for child in node]
        assert [tag for tag in tags if tag in XSD_CHILD_ORDER] == XSD_CHILD_ORDER

    def test_write_full_field_values(self):
        pdu = ConcretePdu(None, "Pdu1")
        _populate(pdu)

        node = _write(pdu)
        assert node.find("HAS-DYNAMIC-LENGTH").text == "true"
        assert node.find("LENGTH").text == "8"

    def test_round_trip_full(self):
        pdu = ConcretePdu(None, "Pdu1")
        _populate(pdu)

        node = _write(pdu)
        reloaded = ConcretePdu(None, "Pdu1")
        ARXMLParser().readPdu(_with_ns(node), reloaded)

        assert reloaded.getShortName() == "Pdu1"
        assert reloaded.getHasDynamicLength().getValue() is True
        assert reloaded.getLength().getValue() == 8

    def test_round_trip_empty(self):
        pdu = ConcretePdu(None, "Pdu1")

        node = _write(pdu)
        reloaded = ConcretePdu(None, "Pdu1")
        ARXMLParser().readPdu(_with_ns(node), reloaded)

        assert reloaded.getHasDynamicLength() is None
        assert reloaded.getLength() is None
