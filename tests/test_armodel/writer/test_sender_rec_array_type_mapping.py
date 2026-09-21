"""Writer round-trip tests for SenderRecArrayTypeMapping (Table 5.28, p.235).

Element order per XSD group SENDER-REC-ARRAY-TYPE-MAPPING: ARRAY-ELEMENT-MAPPINGS,
SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING, SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TextTableMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    IndexedArrayElement,
    SenderRecArrayElementMapping,
    SenderRecArrayTypeMapping,
    SenderRecCompositeTypeMapping,
    SenderReceiverToSignalGroupMapping,
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


def _indexed(application_ref, implementation_ref, index):
    indexed = IndexedArrayElement()
    if application_ref is not None:
        indexed.setApplicationArrayElementRef(_ref(application_ref, "APPLICATION-ARRAY-ELEMENT"))
    if implementation_ref is not None:
        indexed.setImplementationArrayElementRef(_ref(implementation_ref, "IMPLEMENTATION-ARRAY-ELEMENT"))
    idx = Integer()
    idx.setValue(index)
    indexed.setIndex(idx)
    return indexed


def _new_type_mapping():
    type_mapping = SenderRecArrayTypeMapping()

    primitive = SenderRecArrayElementMapping()
    primitive.setSystemSignalRef(_ref("/Signals/Primitive", "SYSTEM-SIGNAL"))
    primitive.setIndexedArrayElement(_indexed("/Types/Array1/Elem", None, 0))
    type_mapping.addArrayElementMapping(primitive)

    sender_to_signal = TextTableMapping()
    sender_to_signal.setIdenticalMapping(BooleanTrue())
    type_mapping.setSenderToSignalTextTableMapping(sender_to_signal)
    return type_mapping


def BooleanTrue():
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean

    value = Boolean()
    value.setValue(True)
    return value


def _new_group_mapping():
    mapping = SenderReceiverToSignalGroupMapping()
    mapping.setTypeMapping(_new_type_mapping())
    return mapping


class TestWriteSenderRecArrayTypeMapping:
    def test_write_content_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSenderReceiverToSignalGroupMapping(parent, _new_group_mapping())
        type_mapping = parent.find("SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING/TYPE-MAPPING/SENDER-REC-ARRAY-TYPE-MAPPING")
        assert type_mapping is not None
        children = [child.tag for child in type_mapping]
        assert children == ["ARRAY-ELEMENT-MAPPINGS", "SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING"]

        element = type_mapping.find("ARRAY-ELEMENT-MAPPINGS/SENDER-REC-ARRAY-ELEMENT-MAPPING")
        element_children = [child.tag for child in element]
        assert element_children == ["INDEXED-ARRAY-ELEMENT", "SYSTEM-SIGNAL-REF"]
        assert element.find("SYSTEM-SIGNAL-REF").text == "/Signals/Primitive"
        assert element.find("SYSTEM-SIGNAL-REF").attrib["DEST"] == "SYSTEM-SIGNAL"
        assert element.find("INDEXED-ARRAY-ELEMENT/APPLICATION-ARRAY-ELEMENT-REF").text == "/Types/Array1/Elem"
        assert element.find("INDEXED-ARRAY-ELEMENT/INDEX").text == "0"
        assert type_mapping.find("SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING/IDENTICAL-MAPPING").text == "true"

    def test_write_empty_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSenderReceiverToSignalGroupMapping(parent, SenderReceiverToSignalGroupMapping())
        assert parent.find("SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING/TYPE-MAPPING") is None

    def test_round_trip_preserves_all_values(self):
        mapping = _new_group_mapping()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSenderReceiverToSignalGroupMapping(parent, mapping)
        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parsed = SenderReceiverToSignalGroupMapping()
        ARXMLParser().readSenderReceiverToSignalGroupMapping(reparsed[0], parsed)

        type_mapping = parsed.getTypeMapping()
        assert isinstance(type_mapping, SenderRecArrayTypeMapping)
        assert isinstance(type_mapping, SenderRecCompositeTypeMapping)
        array_mappings = type_mapping.getArrayElementMappings()
        assert len(array_mappings) == 1
        assert array_mappings[0].getSystemSignalRef().getValue() == "/Signals/Primitive"
        assert array_mappings[0].getIndexedArrayElement().getApplicationArrayElementRef().getValue() == "/Types/Array1/Elem"
        assert array_mappings[0].getIndexedArrayElement().getIndex().getValue() == 0
        assert type_mapping.getSenderToSignalTextTableMapping().getIdenticalMapping().getValue() is True
        assert type_mapping.getSignalToReceiverTextTableMapping() is None
