"""Writer tests for TlvDataIdDefinition (AUTOSAR_CP_TPS_SystemTemplate, Table 7.31, p.831).

Direct writeTlvDataIdDefinition helper; wire tag TLV-DATA-ID-DEFINITION (choice member of
parent group TLV-DATA-ID-DEFINITION-SET's TLV-DATA-ID-DEFINITIONS wrapper, XSD L124857);
child order per XSD group TLV-DATA-ID-DEFINITION: ID, TLV-ARGUMENT-REF,
TLV-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF, TLV-RECORD-ELEMENT-REF; absent members are omitted.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import TlvDataIdDefinition
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def test_write_tlv_data_id_definition_full():
    tlv = TlvDataIdDefinition()
    tlv.setId(PositiveInteger().setValue(7))
    tlv.setTlvArgumentRef(_ref("/PortInterface/op/arg", "ARGUMENT-DATA-PROTOTYPE"))
    tlv.setTlvImplementationDataTypeElementRef(_ref("/DataType/element", "IMPLEMENTATION-DATA-TYPE-ELEMENT"))
    tlv.setTlvRecordElementRef(_ref("/DataType/record", "APPLICATION-RECORD-ELEMENT"))

    parent = ET.Element("ROOT")
    ARXMLWriter().writeTlvDataIdDefinition(parent, tlv)

    assert parent[0].tag == "TLV-DATA-ID-DEFINITION"
    children = list(parent[0])
    assert [c.tag for c in children] == [
        "ID",
        "TLV-ARGUMENT-REF",
        "TLV-IMPLEMENTATION-DATA-TYPE-ELEMENT-REF",
        "TLV-RECORD-ELEMENT-REF",
    ]
    assert children[0].text == "7"
    assert children[1].get("DEST") == "ARGUMENT-DATA-PROTOTYPE"
    assert children[1].text == "/PortInterface/op/arg"
    assert children[2].get("DEST") == "IMPLEMENTATION-DATA-TYPE-ELEMENT"
    assert children[2].text == "/DataType/element"
    assert children[3].get("DEST") == "APPLICATION-RECORD-ELEMENT"
    assert children[3].text == "/DataType/record"


def test_write_tlv_data_id_definition_empty_omits_children():
    tlv = TlvDataIdDefinition()
    parent = ET.Element("ROOT")
    ARXMLWriter().writeTlvDataIdDefinition(parent, tlv)

    assert parent[0].tag == "TLV-DATA-ID-DEFINITION"
    assert len(list(parent[0])) == 0
