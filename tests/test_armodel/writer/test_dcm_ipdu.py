"""Writer round-trip tests for DcmIPdu (Table 6.22, p.343).

Serialized through writeDcmIPdu; the DCM-I-PDU group of AUTOSAR_00052.xsd
(l.28516) adds one own child, DIAG-PDU-TYPE (minOccurs=0, maxOccurs=1); the
DCM-I-PDU complexType (l.28532) stacks the inherited groups AR-OBJECT .. PDU,
I-PDU, DCM-I-PDU. The tests exercise writeDcmIPdu, which must dispatch to
writeIPdu (Base = IPdu) exactly once for the inherited levels — the Pdu level
(HAS-DYNAMIC-LENGTH, LENGTH), the IPdu level (CONTAINED-I-PDU-PROPS) and the
ARObject/Identifiable base attributes (S/T, UUID) — and emit the own
DIAG-PDU-TYPE child last (XSD sequence order).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    Boolean,
    DateTime,
    PositiveInteger,
    String,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainedIPduCollectionSemanticsEnum,
    ContainedIPduProps,
    DcmIPdu,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

UUID_VALUE = "4f4a5b6c-7d8e-49a0-b1c2-3d4e5f6a7b8d"

XSD_CHILD_ORDER = [
    "HAS-DYNAMIC-LENGTH",
    "LENGTH",
    "CONTAINED-I-PDU-PROPS",
    "DIAG-PDU-TYPE",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<DCM-I-PDU>", "<DCM-I-PDU xmlns='%s'>" % NS, 1))


def _populate_props() -> ContainedIPduProps:
    props = ContainedIPduProps()
    semantics = ContainedIPduCollectionSemanticsEnum()
    semantics.setValue(ContainedIPduCollectionSemanticsEnum.QUEUED)
    props.setCollectionSemantics(semantics)

    header_id = PositiveInteger()
    header_id.setValue("4")
    props.setHeaderIdShortHeader(header_id)
    return props


def _populate(pdu: DcmIPdu):
    has_dynamic_length = Boolean()
    has_dynamic_length.setValue(True)
    pdu.setHasDynamicLength(has_dynamic_length)

    length = UnlimitedInteger()
    length.setValue("8")
    pdu.setLength(length)

    pdu.setContainedIPduProps(_populate_props())

    pdu.setDiagPduType(ARLiteral().setValue("DIAG-REQUEST"))


def _write(pdu: DcmIPdu) -> ET.Element:
    parent = ET.Element("AR-PACKAGE")
    ARXMLWriter().writeDcmIPdu(parent, pdu)
    return parent.find("DCM-I-PDU")


class TestWriteDcmIPdu:
    def test_write_empty(self):
        pdu = DcmIPdu(None, "DcmIPdu1")
        node = _write(pdu)

        for tag in XSD_CHILD_ORDER:
            assert node.find(tag) is None, tag

    def test_write_full_child_order_matches_xsd(self):
        pdu = DcmIPdu(None, "DcmIPdu1")
        _populate(pdu)

        node = _write(pdu)
        tags = [child.tag for child in node]
        assert [tag for tag in tags if tag in XSD_CHILD_ORDER] == XSD_CHILD_ORDER

    def test_write_full_field_values(self):
        pdu = DcmIPdu(None, "DcmIPdu1")
        _populate(pdu)

        node = _write(pdu)
        assert node.find("HAS-DYNAMIC-LENGTH").text == "true"
        assert node.find("LENGTH").text == "8"
        assert node.find("DIAG-PDU-TYPE").text == "DIAG-REQUEST"

        props_node = node.find("CONTAINED-I-PDU-PROPS")
        assert props_node.find("COLLECTION-SEMANTICS").text == "QUEUED"
        assert props_node.find("HEADER-ID-SHORT-HEADER").text == "4"

    def test_round_trip_full(self):
        pdu = DcmIPdu(None, "DcmIPdu1")
        _populate(pdu)

        node = _write(pdu)
        reloaded = DcmIPdu(None, "DcmIPdu1")
        ARXMLParser().readDcmIPdu(_with_ns(node), reloaded)

        assert reloaded.getShortName() == "DcmIPdu1"
        assert reloaded.getHasDynamicLength().getValue() is True
        assert reloaded.getLength().getValue() == 8

        props = reloaded.getContainedIPduProps()
        assert isinstance(props, ContainedIPduProps)
        assert props.getCollectionSemantics().getValue() == "QUEUED"
        assert props.getHeaderIdShortHeader().getValue() == 4

        assert reloaded.getDiagPduType() is not None
        assert reloaded.getDiagPduType().getValue() == "DIAG-REQUEST"

    def test_round_trip_base_level_attributes(self):
        pdu = DcmIPdu(None, "DcmIPdu1")
        pdu.setUuid(String().setValue(UUID_VALUE))
        pdu.setChecksum(String().setValue("5"))
        pdu.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))

        node = _write(pdu)
        assert node.attrib["UUID"] == UUID_VALUE
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

        reloaded = DcmIPdu(None, "DcmIPdu1")
        ARXMLParser().readDcmIPdu(_with_ns(node), reloaded)

        assert reloaded.getUuid().getValue() == UUID_VALUE
        assert reloaded.getChecksum().getValue() == "5"
        assert reloaded.getTimestamp().getValue() == "2025-04-04T00:00:00Z"

    def test_round_trip_empty(self):
        pdu = DcmIPdu(None, "DcmIPdu1")

        node = _write(pdu)
        reloaded = DcmIPdu(None, "DcmIPdu1")
        ARXMLParser().readDcmIPdu(_with_ns(node), reloaded)

        assert reloaded.getHasDynamicLength() is None
        assert reloaded.getLength() is None
        assert reloaded.getContainedIPduProps() is None
        assert reloaded.getDiagPduType() is None
