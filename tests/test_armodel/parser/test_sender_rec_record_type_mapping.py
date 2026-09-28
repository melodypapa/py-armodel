"""Parser tests for SenderRecRecordTypeMapping (Table 5.29, p.236).

Element order per XSD group SENDER-REC-RECORD-TYPE-MAPPING: the RECORD-ELEMENT-MAPPINGS
wrapper (0..1) holding an unbounded choice of SENDER-REC-RECORD-ELEMENT-MAPPING entries.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import SenderRecRecordElementMapping, SenderRecRecordTypeMapping
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))


def _record_element_mapping(signal_path: str) -> str:
    return (
        "<SENDER-REC-RECORD-ELEMENT-MAPPING>"
        '<APPLICATION-RECORD-ELEMENT-REF DEST="APPLICATION-RECORD-ELEMENT">/Types/Record1/%s</APPLICATION-RECORD-ELEMENT-REF>'
        '<SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">%s</SYSTEM-SIGNAL-REF>'
        "</SENDER-REC-RECORD-ELEMENT-MAPPING>" % (signal_path.split("/")[-1], signal_path)
    )


class TestReadSenderRecRecordTypeMapping:
    def test_read_multi_entry_field_values(self):
        root = _snip(
            "<SENDER-REC-RECORD-TYPE-MAPPING>"
            "<RECORD-ELEMENT-MAPPINGS>%s%s</RECORD-ELEMENT-MAPPINGS>"
            "</SENDER-REC-RECORD-TYPE-MAPPING>" % (_record_element_mapping("/Signals/One"), _record_element_mapping("/Signals/Two"))
        )
        type_mapping = SenderRecRecordTypeMapping()
        ARXMLParser().readSenderRecRecordTypeMapping(root[0], type_mapping)

        mappings = type_mapping.getRecordElementMappings()
        assert len(mappings) == 2
        assert isinstance(mappings[0], SenderRecRecordElementMapping)
        assert isinstance(mappings[1], SenderRecRecordElementMapping)
        assert mappings[0].getApplicationRecordElementRef().getValue() == "/Types/Record1/One"
        assert mappings[0].getSystemSignalRef().getValue() == "/Signals/One"
        assert mappings[1].getApplicationRecordElementRef().getValue() == "/Types/Record1/Two"
        assert mappings[1].getSystemSignalRef().getValue() == "/Signals/Two"

    def test_read_empty_element(self):
        root = _snip("<SENDER-REC-RECORD-TYPE-MAPPING />")
        type_mapping = SenderRecRecordTypeMapping()
        ARXMLParser().readSenderRecRecordTypeMapping(root[0], type_mapping)

        assert type_mapping.getRecordElementMappings() == []

    def test_read_empty_wrapper(self):
        root = _snip("<SENDER-REC-RECORD-TYPE-MAPPING><RECORD-ELEMENT-MAPPINGS /></SENDER-REC-RECORD-TYPE-MAPPING>")
        type_mapping = SenderRecRecordTypeMapping()
        ARXMLParser().readSenderRecRecordTypeMapping(root[0], type_mapping)

        assert type_mapping.getRecordElementMappings() == []

    def test_read_nested_record_type_mapping(self):
        root = _snip(
            "<SENDER-REC-RECORD-ELEMENT-MAPPING>"
            "<COMPLEX-TYPE-MAPPING>"
            "<SENDER-REC-RECORD-TYPE-MAPPING>"
            "<RECORD-ELEMENT-MAPPINGS>%s</RECORD-ELEMENT-MAPPINGS>"
            "</SENDER-REC-RECORD-TYPE-MAPPING>"
            "</COMPLEX-TYPE-MAPPING>"
            '<SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Signals/Outer</SYSTEM-SIGNAL-REF>'
            "</SENDER-REC-RECORD-ELEMENT-MAPPING>" % _record_element_mapping("/Signals/Inner")
        )
        mapping = SenderRecRecordElementMapping()
        ARXMLParser().readSenderRecRecordElementMapping(root[0], mapping)

        assert mapping.getSystemSignalRef().getValue() == "/Signals/Outer"
        nested = mapping.getComplexTypeMapping()
        assert isinstance(nested, SenderRecRecordTypeMapping)
        nested_mappings = nested.getRecordElementMappings()
        assert len(nested_mappings) == 1
        assert nested_mappings[0].getSystemSignalRef().getValue() == "/Signals/Inner"
