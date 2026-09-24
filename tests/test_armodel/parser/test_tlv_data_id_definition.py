"""Parser tests for TlvDataIdDefinition (AUTOSAR_CP_TPS_SystemTemplate, Table 7.31, p.831).

Direct readTlvDataIdDefinition helper; XML element order per XSD group
TLV-DATA-ID-DEFINITION: ID, TLV-ARGUMENT-REF, TLV-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF,
TLV-RECORD-ELEMENT-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import TlvDataIdDefinition
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _definition_fragment():
    return (
        "<TLV-DATA-ID-DEFINITION xmlns='%s'>"
        "<ID>7</ID>"
        '<TLV-ARGUMENT-REF DEST="ARGUMENT-DATA-PROTOTYPE">/PortInterface/op/arg</TLV-ARGUMENT-REF>'
        '<TLV-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF DEST="IMPLEMENTATION-DATA-TYPE-ELEMENT">/DataType/element</TLV-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF>'
        '<TLV-RECORD-ELEMENT-REF DEST="APPLICATION-RECORD-ELEMENT">/DataType/record</TLV-RECORD-ELEMENT-REF>'
        "</TLV-DATA-ID-DEFINITION>" % NS
    )


def test_parse_tlv_data_id_definition():
    tlv = TlvDataIdDefinition()
    root = ET.fromstring(_definition_fragment())
    ARXMLParser().readTlvDataIdDefinition(root, tlv)

    assert tlv.getId().getValue() == 7
    ref = tlv.getTlvArgumentRef()
    assert ref is not None
    assert ref.getValue() == "/PortInterface/op/arg"
    assert ref.getDest() == "ARGUMENT-DATA-PROTOTYPE"
    impl_ref = tlv.getTlvImplementationDataTypeElementRef()
    assert impl_ref is not None
    assert impl_ref.getValue() == "/DataType/element"
    assert impl_ref.getDest() == "IMPLEMENTATION-DATA-TYPE-ELEMENT"
    record_ref = tlv.getTlvRecordElementRef()
    assert record_ref is not None
    assert record_ref.getValue() == "/DataType/record"
    assert record_ref.getDest() == "APPLICATION-RECORD-ELEMENT"


def test_parse_tlv_data_id_definition_empty_element():
    tlv = TlvDataIdDefinition()
    root = ET.fromstring("<TLV-DATA-ID-DEFINITION xmlns='%s'/>" % NS)
    ARXMLParser().readTlvDataIdDefinition(root, tlv)

    assert tlv.getId() is None
    assert tlv.getTlvArgumentRef() is None
    assert tlv.getTlvImplementationDataTypeElementRef() is None
    assert tlv.getTlvRecordElementRef() is None


def test_parse_tlv_data_id_definition_round_trip():
    from armodel.writer.arxml_writer import ARXMLWriter

    tlv = TlvDataIdDefinition()
    root = ET.fromstring(_definition_fragment())
    ARXMLParser().readTlvDataIdDefinition(root, tlv)

    parent = ET.Element("ROOT")
    ARXMLWriter().writeTlvDataIdDefinition(parent, tlv)
    reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1))
    tlv2 = TlvDataIdDefinition()
    ARXMLParser().readTlvDataIdDefinition(reparsed[0], tlv2)

    assert tlv2.getId().getValue() == 7
    assert tlv2.getTlvArgumentRef().getValue() == "/PortInterface/op/arg"
    assert tlv2.getTlvArgumentRef().getDest() == "ARGUMENT-DATA-PROTOTYPE"
    assert tlv2.getTlvImplementationDataTypeElementRef().getValue() == "/DataType/element"
    assert tlv2.getTlvImplementationDataTypeElementRef().getDest() == "IMPLEMENTATION-DATA-TYPE-ELEMENT"
    assert tlv2.getTlvRecordElementRef().getValue() == "/DataType/record"
    assert tlv2.getTlvRecordElementRef().getDest() == "APPLICATION-RECORD-ELEMENT"
