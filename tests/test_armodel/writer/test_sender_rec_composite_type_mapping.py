"""Writer round-trip tests for SenderRecCompositeTypeMapping (Table 5.27, p.235).

Abstract class with zero attribute rows — exercised through its concrete
subclass SenderRecRecordTypeMapping inside the TYPE-MAPPING choice.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    SenderRecCompositeTypeMapping,
    SenderReceiverToSignalGroupMapping,
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


def _new_group_mapping():
    mapping = SenderReceiverToSignalGroupMapping()

    record_mapping = SenderRecRecordTypeMapping()
    record_element = SenderRecRecordElementMapping()
    signal_ref = RefType()
    signal_ref.setDest("SYSTEM-SIGNAL")
    signal_ref.setValue("/Signals/Signal1")
    record_element.setSystemSignalRef(signal_ref)
    record_mapping.addRecordElementMapping(record_element)

    mapping.setTypeMapping(record_mapping)
    return mapping


class TestWriteSenderRecCompositeTypeMapping:
    def test_write_via_record_type_mapping(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSenderReceiverToSignalGroupMapping(parent, _new_group_mapping())
        node = parent.find("SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING")
        assert node is not None
        type_mapping = node.find("TYPE-MAPPING/SENDER-REC-RECORD-TYPE-MAPPING")
        assert type_mapping is not None
        signal_ref = type_mapping.find("RECORD-ELEMENT-MAPPINGS/SENDER-REC-RECORD-ELEMENT-MAPPING/SYSTEM-SIGNAL-REF")
        assert signal_ref.text == "/Signals/Signal1"
        assert signal_ref.attrib["DEST"] == "SYSTEM-SIGNAL"

    def test_round_trip_preserves_values(self):
        mapping = _new_group_mapping()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSenderReceiverToSignalGroupMapping(parent, mapping)
        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parsed = SenderReceiverToSignalGroupMapping()
        ARXMLParser().readSenderReceiverToSignalGroupMapping(reparsed[0], parsed)

        type_mapping = parsed.getTypeMapping()
        assert isinstance(type_mapping, SenderRecCompositeTypeMapping)
        assert isinstance(type_mapping, SenderRecRecordTypeMapping)
        assert type_mapping.getRecordElementMappings()[0].getSystemSignalRef().getValue() == "/Signals/Signal1"
        assert type_mapping.getRecordElementMappings()[0].getSystemSignalRef().getDest() == "SYSTEM-SIGNAL"
