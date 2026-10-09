"""Writer round-trip tests for IPdu (Table 6.18, p.341).

Serialized through the reusable writeIPdu helper (the I-PDU group of
AUTOSAR_00052.xsd, l.66381); child order per that group, sequenced after the PDU
group. IPdu is abstract: the tests exercise the helper through a concrete subclass,
the same way concrete IPdu subclasses call it.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainedIPduCollectionSemanticsEnum,
    ContainedIPduProps,
    IPdu,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "HAS-DYNAMIC-LENGTH",
    "LENGTH",
    "CONTAINED-I-PDU-PROPS",
]


class ConcreteIPdu(IPdu):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<I-PDU>", "<I-PDU xmlns='%s'>" % NS, 1))


def _populate_props() -> ContainedIPduProps:
    props = ContainedIPduProps()
    semantics = ContainedIPduCollectionSemanticsEnum()
    semantics.setValue(ContainedIPduCollectionSemanticsEnum.QUEUED)
    props.setCollectionSemantics(semantics)

    header_id = PositiveInteger()
    header_id.setValue("4")
    props.setHeaderIdShortHeader(header_id)
    return props


def _populate(ipdu: IPdu):
    value = Boolean()
    value.setValue(True)
    ipdu.setHasDynamicLength(value)

    length = UnlimitedInteger()
    length.setValue("8")
    ipdu.setLength(length)

    ipdu.setContainedIPduProps(_populate_props())


def _write(ipdu: IPdu) -> ET.Element:
    parent = ET.Element("I-PDU")
    ARXMLWriter().writeIPdu(parent, ipdu)
    return parent


class TestWriteIPdu:
    def test_write_empty(self):
        ipdu = ConcreteIPdu(None, "IPdu1")
        node = _write(ipdu)

        for tag in XSD_CHILD_ORDER:
            assert node.find(tag) is None, tag

    def test_write_full_child_order_matches_xsd(self):
        ipdu = ConcreteIPdu(None, "IPdu1")
        _populate(ipdu)

        node = _write(ipdu)
        tags = [child.tag for child in node]
        assert [tag for tag in tags if tag in XSD_CHILD_ORDER] == XSD_CHILD_ORDER

    def test_write_full_field_values(self):
        ipdu = ConcreteIPdu(None, "IPdu1")
        _populate(ipdu)

        node = _write(ipdu)
        assert node.find("HAS-DYNAMIC-LENGTH").text == "true"
        assert node.find("LENGTH").text == "8"

        props_node = node.find("CONTAINED-I-PDU-PROPS")
        assert props_node.find("COLLECTION-SEMANTICS").text == "QUEUED"
        assert props_node.find("HEADER-ID-SHORT-HEADER").text == "4"

    def test_round_trip_full(self):
        ipdu = ConcreteIPdu(None, "IPdu1")
        _populate(ipdu)

        node = _write(ipdu)
        reloaded = ConcreteIPdu(None, "IPdu1")
        ARXMLParser().readIPdu(_with_ns(node), reloaded)

        assert reloaded.getShortName() == "IPdu1"
        assert reloaded.getHasDynamicLength().getValue() is True
        assert reloaded.getLength().getValue() == 8

        props = reloaded.getContainedIPduProps()
        assert isinstance(props, ContainedIPduProps)
        assert props.getCollectionSemantics().getValue() == "QUEUED"
        assert props.getHeaderIdShortHeader().getValue() == 4

    def test_round_trip_empty(self):
        ipdu = ConcreteIPdu(None, "IPdu1")

        node = _write(ipdu)
        reloaded = ConcreteIPdu(None, "IPdu1")
        ARXMLParser().readIPdu(_with_ns(node), reloaded)

        assert reloaded.getHasDynamicLength() is None
        assert reloaded.getLength() is None
        assert reloaded.getContainedIPduProps() is None
