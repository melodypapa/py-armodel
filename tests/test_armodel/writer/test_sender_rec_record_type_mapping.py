"""Writer round-trip tests for SenderRecRecordTypeMapping (Table 5.29, p.236).

Element order per XSD group SENDER-REC-RECORD-TYPE-MAPPING: the RECORD-ELEMENT-MAPPINGS
wrapper (0..1, emitted only when non-empty) holding the SENDER-REC-RECORD-ELEMENT-MAPPING
entries in list order.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import SenderRecRecordElementMapping, SenderRecRecordTypeMapping
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _new_record_element_mapping(app_elem: str, signal: str) -> SenderRecRecordElementMapping:
    mapping = SenderRecRecordElementMapping()
    mapping.setApplicationRecordElementRef(_ref(app_elem, "APPLICATION-RECORD-ELEMENT"))
    mapping.setSystemSignalRef(_ref(signal, "SYSTEM-SIGNAL"))
    return mapping


def _write(type_mapping: SenderRecRecordTypeMapping) -> ET.Element:
    parent = ET.Element("PARENT")
    ARXMLWriter().writeSenderRecRecordTypeMapping(parent, type_mapping)
    return parent


class TestWriteSenderRecRecordTypeMapping:
    def test_write_entries_in_list_order(self):
        type_mapping = SenderRecRecordTypeMapping()
        type_mapping.addRecordElementMapping(_new_record_element_mapping("/Types/Record1/One", "/Signals/One"))
        type_mapping.addRecordElementMapping(_new_record_element_mapping("/Types/Record1/Two", "/Signals/Two"))

        element = _write(type_mapping)
        assert element.find("SENDER-REC-RECORD-TYPE-MAPPING") is not None

        wrapper = element.find("SENDER-REC-RECORD-TYPE-MAPPING/RECORD-ELEMENT-MAPPINGS")
        assert wrapper is not None
        entries = list(wrapper)
        assert [entry.tag for entry in entries] == ["SENDER-REC-RECORD-ELEMENT-MAPPING", "SENDER-REC-RECORD-ELEMENT-MAPPING"]
        assert entries[0].find("APPLICATION-RECORD-ELEMENT-REF").text == "/Types/Record1/One"
        assert entries[0].find("SYSTEM-SIGNAL-REF").text == "/Signals/One"
        assert entries[1].find("APPLICATION-RECORD-ELEMENT-REF").text == "/Types/Record1/Two"
        assert entries[1].find("SYSTEM-SIGNAL-REF").text == "/Signals/Two"

    def test_write_empty_omits_wrapper(self):
        element = _write(SenderRecRecordTypeMapping())
        assert element.find("SENDER-REC-RECORD-TYPE-MAPPING") is not None
        assert element.find("SENDER-REC-RECORD-TYPE-MAPPING/RECORD-ELEMENT-MAPPINGS") is None

    def test_round_trip_preserves_all_values(self):
        type_mapping = SenderRecRecordTypeMapping()
        type_mapping.addRecordElementMapping(_new_record_element_mapping("/Types/Record1/One", "/Signals/One"))
        type_mapping.addRecordElementMapping(_new_record_element_mapping("/Types/Record1/Two", "/Signals/Two"))

        element = _write(type_mapping)
        reparsed = ET.fromstring(ET.tostring(element).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parsed_holder = SenderRecRecordTypeMapping()
        ARXMLParser().readSenderRecRecordTypeMapping(reparsed[0], parsed_holder)

        mappings = parsed_holder.getRecordElementMappings()
        assert len(mappings) == 2
        assert mappings[0].getApplicationRecordElementRef().getValue() == "/Types/Record1/One"
        assert mappings[0].getApplicationRecordElementRef().getDest() == "APPLICATION-RECORD-ELEMENT"
        assert mappings[0].getSystemSignalRef().getValue() == "/Signals/One"
        assert mappings[0].getSystemSignalRef().getDest() == "SYSTEM-SIGNAL"
        assert mappings[1].getApplicationRecordElementRef().getValue() == "/Types/Record1/Two"
        assert mappings[1].getSystemSignalRef().getValue() == "/Signals/Two"
