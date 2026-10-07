"""Writer round-trip tests for SenderRecArrayElementMapping (Table 5.31, p.237).

Element order per XSD group SENDER-REC-ARRAY-ELEMENT-MAPPING: COMPLEX-TYPE-MAPPING,
INDEXED-ARRAY-ELEMENT, SYSTEM-SIGNAL-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    IndexedArrayElement,
    SenderRecArrayElementMapping,
    SenderRecArrayTypeMapping,
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


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _indexed(index=2):
    indexed = IndexedArrayElement()
    indexed.setApplicationArrayElementRef(_ref("/Types/Array1/AppElem", "APPLICATION-ARRAY-ELEMENT"))
    value = Integer()
    value.setValue(str(index))
    indexed.setIndex(value)
    return indexed


def _write(mapping):
    holder = SenderRecArrayTypeMapping()
    holder.addArrayElementMapping(mapping)
    parent = ET.Element("PARENT")
    ARXMLWriter().writeSenderRecArrayTypeMapping(parent, holder)
    return parent.find("SENDER-REC-ARRAY-TYPE-MAPPING/ARRAY-ELEMENT-MAPPINGS/SENDER-REC-ARRAY-ELEMENT-MAPPING")


class TestWriteSenderRecArrayElementMapping:
    def test_write_content_in_xsd_order(self):
        mapping = SenderRecArrayElementMapping()
        mapping.setComplexTypeMapping(SenderRecRecordTypeMapping())
        mapping.setIndexedArrayElement(_indexed())
        mapping.setSystemSignalRef(_ref("/Signals/Primitive", "SYSTEM-SIGNAL"))
        element = _write(mapping)
        assert element is not None

        children = [child.tag for child in element]
        assert children == ["COMPLEX-TYPE-MAPPING", "INDEXED-ARRAY-ELEMENT", "SYSTEM-SIGNAL-REF"]
        assert element.find("COMPLEX-TYPE-MAPPING/SENDER-REC-RECORD-TYPE-MAPPING") is not None
        assert element.find("INDEXED-ARRAY-ELEMENT/APPLICATION-ARRAY-ELEMENT-REF").text == "/Types/Array1/AppElem"
        assert element.find("INDEXED-ARRAY-ELEMENT/INDEX").text == "2"
        assert element.find("SYSTEM-SIGNAL-REF").text == "/Signals/Primitive"
        assert element.find("SYSTEM-SIGNAL-REF").get("DEST") == "SYSTEM-SIGNAL"

    def test_round_trip_full(self):
        mapping = SenderRecArrayElementMapping()
        mapping.setComplexTypeMapping(SenderRecRecordTypeMapping())
        mapping.setIndexedArrayElement(_indexed())
        mapping.setSystemSignalRef(_ref("/Signals/Primitive", "SYSTEM-SIGNAL"))
        element = _write(mapping)

        reparsed = ET.fromstring(ET.tostring(element).decode("utf-8").replace("<SENDER-REC-ARRAY-ELEMENT-MAPPING>", "<SENDER-REC-ARRAY-ELEMENT-MAPPING xmlns='%s'>" % NS, 1))
        reloaded = SenderRecArrayElementMapping()
        ARXMLParser().readSenderRecArrayElementMapping(reparsed, reloaded)
        assert isinstance(reloaded.getComplexTypeMapping(), SenderRecRecordTypeMapping)
        assert reloaded.getIndexedArrayElement().getApplicationArrayElementRef().getValue() == "/Types/Array1/AppElem"
        assert reloaded.getIndexedArrayElement().getIndex().getValue() == 2
        assert reloaded.getSystemSignalRef().getValue() == "/Signals/Primitive"
        assert reloaded.getSystemSignalRef().getDest() == "SYSTEM-SIGNAL"

    def test_round_trip_empty_wrapper(self):
        mapping = SenderRecArrayElementMapping()
        element = _write(mapping)

        complex_element = element.find("COMPLEX-TYPE-MAPPING")
        assert complex_element is None
        assert element.find("INDEXED-ARRAY-ELEMENT") is None
        assert element.find("SYSTEM-SIGNAL-REF") is None

        reparsed = ET.fromstring(ET.tostring(element).decode("utf-8").replace("<SENDER-REC-ARRAY-ELEMENT-MAPPING>", "<SENDER-REC-ARRAY-ELEMENT-MAPPING xmlns='%s'>" % NS, 1))
        reloaded = SenderRecArrayElementMapping()
        ARXMLParser().readSenderRecArrayElementMapping(reparsed, reloaded)
        assert reloaded.getComplexTypeMapping() is None
        assert reloaded.getIndexedArrayElement() is None
        assert reloaded.getSystemSignalRef() is None
