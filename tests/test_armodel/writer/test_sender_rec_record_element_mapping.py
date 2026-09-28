"""Writer round-trip tests for SenderRecRecordElementMapping (Table 5.30, p.236).

Element order per XSD group SENDER-REC-RECORD-ELEMENT-MAPPING: APPLICATION-RECORD-ELEMENT-REF,
COMPLEX-TYPE-MAPPING, IMPLEMENTATION-RECORD-ELEMENT-REF, SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING,
SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING, SYSTEM-SIGNAL-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TextTableMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    SenderRecCompositeTypeMapping,
    SenderRecRecordElementMapping,
    SenderRecRecordTypeMapping,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

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


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _boolean(value):
    result = Boolean()
    result.setValue(value)
    return result


def _new_record_element_mapping():
    mapping = SenderRecRecordElementMapping()
    mapping.setApplicationRecordElementRef(_ref("/Types/Record1/AppElem", "APPLICATION-RECORD-ELEMENT"))
    mapping.setComplexTypeMapping(SenderRecRecordTypeMapping())
    mapping.setImplementationRecordElementRef(_ref("/Types/Impl1/Elem", "IMPLEMENTATION-DATA-TYPE-ELEMENT"))
    sender_to_signal = TextTableMapping()
    sender_to_signal.setIdenticalMapping(_boolean(True))
    mapping.setSenderToSignalTextTableMapping(sender_to_signal)
    signal_to_receiver = TextTableMapping()
    signal_to_receiver.setIdenticalMapping(_boolean(False))
    mapping.setSignalToReceiverTextTableMapping(signal_to_receiver)
    mapping.setSystemSignalRef(_ref("/Signals/Primitive", "SYSTEM-SIGNAL"))
    return mapping


def _write(holder, mapping):
    holder.addRecordElementMapping(mapping)
    parent = ET.Element("PARENT")
    ARXMLWriter().writeSenderRecRecordTypeMapping(parent, holder)
    return parent.find("SENDER-REC-RECORD-TYPE-MAPPING/RECORD-ELEMENT-MAPPINGS/SENDER-REC-RECORD-ELEMENT-MAPPING")


def _write_parent(holder, mapping):
    holder.addRecordElementMapping(mapping)
    parent = ET.Element("PARENT")
    ARXMLWriter().writeSenderRecRecordTypeMapping(parent, holder)
    return parent


class TestWriteSenderRecRecordElementMapping:
    def test_write_content_in_xsd_order(self):
        element = _write(SenderRecRecordTypeMapping(), _new_record_element_mapping())
        assert element is not None

        children = [child.tag for child in element]
        assert children == [
            "APPLICATION-RECORD-ELEMENT-REF",
            "COMPLEX-TYPE-MAPPING",
            "IMPLEMENTATION-RECORD-ELEMENT-REF",
            "SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING",
            "SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING",
            "SYSTEM-SIGNAL-REF",
        ]

        assert element.find("APPLICATION-RECORD-ELEMENT-REF").text == "/Types/Record1/AppElem"
        assert element.find("APPLICATION-RECORD-ELEMENT-REF").attrib["DEST"] == "APPLICATION-RECORD-ELEMENT"
        assert element.find("COMPLEX-TYPE-MAPPING/SENDER-REC-RECORD-TYPE-MAPPING") is not None
        assert element.find("IMPLEMENTATION-RECORD-ELEMENT-REF").text == "/Types/Impl1/Elem"
        assert element.find("IMPLEMENTATION-RECORD-ELEMENT-REF").attrib["DEST"] == "IMPLEMENTATION-DATA-TYPE-ELEMENT"
        assert element.find("SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING/IDENTICAL-MAPPING").text == "true"
        assert element.find("SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING/IDENTICAL-MAPPING").text == "false"
        assert element.find("SYSTEM-SIGNAL-REF").text == "/Signals/Primitive"
        assert element.find("SYSTEM-SIGNAL-REF").attrib["DEST"] == "SYSTEM-SIGNAL"

    def test_write_empty_omits_optional_tags(self):
        element = _write(SenderRecRecordTypeMapping(), SenderRecRecordElementMapping())
        assert element is not None
        assert len(list(element)) == 0

    def test_round_trip_preserves_all_values(self):
        parent = _write_parent(SenderRecRecordTypeMapping(), _new_record_element_mapping())
        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parsed_holder = SenderRecRecordTypeMapping()
        ARXMLParser().readSenderRecRecordTypeMapping(reparsed[0], parsed_holder)

        mappings = parsed_holder.getRecordElementMappings()
        assert len(mappings) == 1
        mapping = mappings[0]
        assert isinstance(mapping, SenderRecRecordElementMapping)
        assert mapping.getApplicationRecordElementRef().getValue() == "/Types/Record1/AppElem"
        assert mapping.getApplicationRecordElementRef().getDest() == "APPLICATION-RECORD-ELEMENT"

        complex_type_mapping = mapping.getComplexTypeMapping()
        assert isinstance(complex_type_mapping, SenderRecRecordTypeMapping)
        assert isinstance(complex_type_mapping, SenderRecCompositeTypeMapping)
        assert complex_type_mapping.getRecordElementMappings() == []

        assert mapping.getImplementationRecordElementRef().getValue() == "/Types/Impl1/Elem"
        assert mapping.getSenderToSignalTextTableMapping().getIdenticalMapping().getValue() is True
        assert mapping.getSignalToReceiverTextTableMapping().getIdenticalMapping().getValue() is False
        assert mapping.getSystemSignalRef().getValue() == "/Signals/Primitive"
        assert mapping.getSystemSignalRef().getDest() == "SYSTEM-SIGNAL"
