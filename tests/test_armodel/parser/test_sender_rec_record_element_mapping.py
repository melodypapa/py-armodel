"""Parser tests for SenderRecRecordElementMapping (Table 5.30, p.236).

Element order per XSD group SENDER-REC-RECORD-ELEMENT-MAPPING: APPLICATION-RECORD-ELEMENT-REF,
COMPLEX-TYPE-MAPPING, IMPLEMENTATION-RECORD-ELEMENT-REF, SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING,
SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING, SYSTEM-SIGNAL-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    SenderRecCompositeTypeMapping,
    SenderRecRecordElementMapping,
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


RECORD_ELEMENT_MAPPING_XML = (
    "<SENDER-REC-RECORD-ELEMENT-MAPPING>"
    '<APPLICATION-RECORD-ELEMENT-REF DEST="APPLICATION-RECORD-ELEMENT">/Types/Record1/AppElem</APPLICATION-RECORD-ELEMENT-REF>'
    "<COMPLEX-TYPE-MAPPING>"
    "<SENDER-REC-RECORD-TYPE-MAPPING />"
    "</COMPLEX-TYPE-MAPPING>"
    '<IMPLEMENTATION-RECORD-ELEMENT-REF DEST="IMPLEMENTATION-DATA-TYPE-ELEMENT">/Types/Impl1/Elem</IMPLEMENTATION-RECORD-ELEMENT-REF>'
    "<SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING>"
    "<IDENTICAL-MAPPING>true</IDENTICAL-MAPPING>"
    "</SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING>"
    "<SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING>"
    "<IDENTICAL-MAPPING>false</IDENTICAL-MAPPING>"
    "</SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING>"
    '<SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Signals/Primitive</SYSTEM-SIGNAL-REF>'
    "</SENDER-REC-RECORD-ELEMENT-MAPPING>"
)


class TestReadSenderRecRecordElementMapping:
    def test_read_field_values(self):
        root = _snip(RECORD_ELEMENT_MAPPING_XML)
        mapping = SenderRecRecordElementMapping()
        ARXMLParser().readSenderRecRecordElementMapping(root[0], mapping)

        assert mapping.getApplicationRecordElementRef().getValue() == "/Types/Record1/AppElem"
        assert mapping.getApplicationRecordElementRef().getDest() == "APPLICATION-RECORD-ELEMENT"

        complex_type_mapping = mapping.getComplexTypeMapping()
        assert isinstance(complex_type_mapping, SenderRecRecordTypeMapping)
        assert isinstance(complex_type_mapping, SenderRecCompositeTypeMapping)

        assert mapping.getImplementationRecordElementRef().getValue() == "/Types/Impl1/Elem"
        assert mapping.getImplementationRecordElementRef().getDest() == "IMPLEMENTATION-DATA-TYPE-ELEMENT"

        sender_to_signal = mapping.getSenderToSignalTextTableMapping()
        assert sender_to_signal is not None
        assert sender_to_signal.getIdenticalMapping().getValue() is True
        signal_to_receiver = mapping.getSignalToReceiverTextTableMapping()
        assert signal_to_receiver is not None
        assert signal_to_receiver.getIdenticalMapping().getValue() is False

        assert mapping.getSystemSignalRef().getValue() == "/Signals/Primitive"
        assert mapping.getSystemSignalRef().getDest() == "SYSTEM-SIGNAL"

    def test_read_empty(self):
        root = _snip("<SENDER-REC-RECORD-ELEMENT-MAPPING />")
        mapping = SenderRecRecordElementMapping()
        ARXMLParser().readSenderRecRecordElementMapping(root[0], mapping)

        assert mapping.getApplicationRecordElementRef() is None
        assert mapping.getComplexTypeMapping() is None
        assert mapping.getImplementationRecordElementRef() is None
        assert mapping.getSenderToSignalTextTableMapping() is None
        assert mapping.getSignalToReceiverTextTableMapping() is None
        assert mapping.getSystemSignalRef() is None

    def test_read_dispatch_via_record_type_mapping(self):
        root = _snip("<SENDER-REC-RECORD-TYPE-MAPPING>" "<RECORD-ELEMENT-MAPPINGS>%s</RECORD-ELEMENT-MAPPINGS>" "</SENDER-REC-RECORD-TYPE-MAPPING>" % RECORD_ELEMENT_MAPPING_XML)
        type_mapping = SenderRecRecordTypeMapping()
        ARXMLParser().readSenderRecRecordTypeMapping(root[0], type_mapping)

        mappings = type_mapping.getRecordElementMappings()
        assert len(mappings) == 1
        record_element_mapping = mappings[0]
        assert isinstance(record_element_mapping, SenderRecRecordElementMapping)
        assert record_element_mapping.getApplicationRecordElementRef().getValue() == "/Types/Record1/AppElem"
        assert isinstance(record_element_mapping.getComplexTypeMapping(), SenderRecRecordTypeMapping)
        assert record_element_mapping.getSystemSignalRef().getValue() == "/Signals/Primitive"
