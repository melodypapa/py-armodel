"""Parser tests for SenderRecCompositeTypeMapping (Table 5.27, p.235).

Abstract class with zero attribute rows (XSD group SENDER-REC-COMPOSITE-TYPE-MAPPING
is an empty sequence) — exercised through its concrete subclass
SenderRecRecordTypeMapping inside the TYPE-MAPPING choice.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
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


class TestReadSenderRecCompositeTypeMapping:
    def test_read_via_record_type_mapping(self):
        root = _snip(
            "<SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>"
            "<TYPE-MAPPING><SENDER-REC-RECORD-TYPE-MAPPING>"
            "<RECORD-ELEMENT-MAPPINGS><SENDER-REC-RECORD-ELEMENT-MAPPING>"
            '<SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Signals/Signal1</SYSTEM-SIGNAL-REF>'
            "</SENDER-REC-RECORD-ELEMENT-MAPPING></RECORD-ELEMENT-MAPPINGS>"
            "</SENDER-REC-RECORD-TYPE-MAPPING></TYPE-MAPPING>"
            "</SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>"
        )
        mapping = SenderReceiverToSignalGroupMapping()
        ARXMLParser().readSenderReceiverToSignalGroupMapping(root[0], mapping)

        type_mapping = mapping.getTypeMapping()
        assert isinstance(type_mapping, SenderRecRecordTypeMapping)
        assert isinstance(type_mapping, SenderRecCompositeTypeMapping)
        assert len(type_mapping.getRecordElementMappings()) == 1
        assert type_mapping.getRecordElementMappings()[0].getSystemSignalRef().getValue() == "/Signals/Signal1"
