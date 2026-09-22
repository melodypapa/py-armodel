"""Parser tests for SenderRecArrayTypeMapping (Table 5.28, p.235).

Element order per XSD group SENDER-REC-ARRAY-TYPE-MAPPING: ARRAY-ELEMENT-MAPPINGS,
SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING, SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    IndexedArrayElement,
    SenderRecArrayElementMapping,
    SenderRecArrayTypeMapping,
    SenderRecCompositeTypeMapping,
    SenderReceiverToSignalGroupMapping,
    SenderRecRecordTypeMapping,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))


ARRAY_TYPE_MAPPING_XML = (
    "<SENDER-REC-ARRAY-TYPE-MAPPING>"
    "<ARRAY-ELEMENT-MAPPINGS>"
    "<SENDER-REC-ARRAY-ELEMENT-MAPPING>"
    '<SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Signals/Primitive</SYSTEM-SIGNAL-REF>'
    "<INDEXED-ARRAY-ELEMENT>"
    '<APPLICATION-ARRAY-ELEMENT-REF DEST="APPLICATION-ARRAY-ELEMENT">/Types/Array1/Elem</APPLICATION-ARRAY-ELEMENT-REF>'
    "<INDEX>0</INDEX>"
    "</INDEXED-ARRAY-ELEMENT>"
    "</SENDER-REC-ARRAY-ELEMENT-MAPPING>"
    "<SENDER-REC-ARRAY-ELEMENT-MAPPING>"
    "<COMPLEX-TYPE-MAPPING>"
    "<SENDER-REC-RECORD-TYPE-MAPPING />"
    "</COMPLEX-TYPE-MAPPING>"
    "<INDEXED-ARRAY-ELEMENT>"
    '<IMPLEMENTATION-ARRAY-ELEMENT-REF DEST="IMPLEMENTATION-ARRAY-ELEMENT">/Types/ImplArray1/Elem</IMPLEMENTATION-ARRAY-ELEMENT-REF>'
    "<INDEX>1</INDEX>"
    "</INDEXED-ARRAY-ELEMENT>"
    "</SENDER-REC-ARRAY-ELEMENT-MAPPING>"
    "</ARRAY-ELEMENT-MAPPINGS>"
    "<SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING>"
    "<IDENTICAL-MAPPING>true</IDENTICAL-MAPPING>"
    "</SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING>"
    "<SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING>"
    "<IDENTICAL-MAPPING>false</IDENTICAL-MAPPING>"
    "</SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING>"
    "</SENDER-REC-ARRAY-TYPE-MAPPING>"
)


class TestReadSenderRecArrayTypeMapping:
    def test_read_dispatch_via_group_mapping(self):
        root = _snip("<SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>" "<TYPE-MAPPING>%s</TYPE-MAPPING>" "</SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>" % ARRAY_TYPE_MAPPING_XML)
        mapping = SenderReceiverToSignalGroupMapping()
        ARXMLParser().readSenderReceiverToSignalGroupMapping(root[0], mapping)

        type_mapping = mapping.getTypeMapping()
        assert isinstance(type_mapping, SenderRecArrayTypeMapping)
        assert isinstance(type_mapping, SenderRecCompositeTypeMapping)

    def test_read_field_values(self):
        root = _snip(ARRAY_TYPE_MAPPING_XML)
        type_mapping = SenderRecArrayTypeMapping()
        ARXMLParser().readSenderRecArrayTypeMapping(root[0], type_mapping)

        array_mappings = type_mapping.getArrayElementMappings()
        assert len(array_mappings) == 2

        primitive = array_mappings[0]
        assert isinstance(primitive, SenderRecArrayElementMapping)
        assert primitive.getSystemSignalRef().getValue() == "/Signals/Primitive"
        assert primitive.getSystemSignalRef().getDest() == "SYSTEM-SIGNAL"
        assert primitive.getComplexTypeMapping() is None
        indexed = primitive.getIndexedArrayElement()
        assert isinstance(indexed, IndexedArrayElement)
        assert indexed.getApplicationArrayElementRef().getValue() == "/Types/Array1/Elem"
        assert indexed.getIndex().getValue() == 0

        composite = array_mappings[1]
        assert isinstance(composite.getComplexTypeMapping(), SenderRecRecordTypeMapping)
        assert composite.getIndexedArrayElement().getImplementationArrayElementRef().getValue() == "/Types/ImplArray1/Elem"
        assert composite.getIndexedArrayElement().getIndex().getValue() == 1

        sender_to_signal = type_mapping.getSenderToSignalTextTableMapping()
        assert sender_to_signal is not None
        assert sender_to_signal.getIdenticalMapping().getValue() is True
        signal_to_receiver = type_mapping.getSignalToReceiverTextTableMapping()
        assert signal_to_receiver is not None
        assert signal_to_receiver.getIdenticalMapping().getValue() is False

    def test_read_empty(self):
        root = _snip("<SENDER-REC-ARRAY-TYPE-MAPPING />")
        type_mapping = SenderRecArrayTypeMapping()
        ARXMLParser().readSenderRecArrayTypeMapping(root[0], type_mapping)

        assert type_mapping.getArrayElementMappings() == []
        assert type_mapping.getSenderToSignalTextTableMapping() is None
        assert type_mapping.getSignalToReceiverTextTableMapping() is None
