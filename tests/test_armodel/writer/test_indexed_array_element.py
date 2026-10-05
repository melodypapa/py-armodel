"""Writer round-trip tests for IndexedArrayElement (Table 5.32, p.237).

Element order per XSD group INDEXED-ARRAY-ELEMENT: APPLICATION-ARRAY-ELEMENT-REF,
IMPLEMENTATION-ARRAY-ELEMENT-REF, INDEX.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Integer, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import IndexedArrayElement, SenderRecArrayElementMapping
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


def _indexed(application_ref=None, implementation_ref=None, index=None):
    indexed = IndexedArrayElement()
    indexed.setChecksum(String().setValue("1234"))
    indexed.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
    if application_ref is not None:
        indexed.setApplicationArrayElementRef(_ref(application_ref, "APPLICATION-ARRAY-ELEMENT"))
    if implementation_ref is not None:
        indexed.setImplementationArrayElementRef(_ref(implementation_ref, "IMPLEMENTATION-ARRAY-ELEMENT"))
    if index is not None:
        idx = Integer()
        idx.setValue(index)
        indexed.setIndex(idx)
    return indexed


def _write(mapping):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeSenderRecArrayElementMapping(parent, mapping)
    return parent.find("SENDER-REC-ARRAY-ELEMENT-MAPPING/INDEXED-ARRAY-ELEMENT")


class TestWriteIndexedArrayElement:
    def test_write_content_in_xsd_order(self):
        mapping = SenderRecArrayElementMapping()
        mapping.setIndexedArrayElement(_indexed("/Types/Array1/Elem", "/Types/ImplArray1/Elem", 3))

        element = _write(mapping)
        assert element is not None
        children = [child.tag for child in element]
        assert children == ["APPLICATION-ARRAY-ELEMENT-REF", "IMPLEMENTATION-ARRAY-ELEMENT-REF", "INDEX"]
        assert element.find("APPLICATION-ARRAY-ELEMENT-REF").text == "/Types/Array1/Elem"
        assert element.find("APPLICATION-ARRAY-ELEMENT-REF").attrib["DEST"] == "APPLICATION-ARRAY-ELEMENT"
        assert element.find("IMPLEMENTATION-ARRAY-ELEMENT-REF").text == "/Types/ImplArray1/Elem"
        assert element.find("IMPLEMENTATION-ARRAY-ELEMENT-REF").attrib["DEST"] == "IMPLEMENTATION-ARRAY-ELEMENT"
        assert element.find("INDEX").text == "3"
        assert element.get("S") == "1234"
        assert element.get("T") == "2024-01-01T00:00:00Z"

    def test_write_partial_omits_absent_tags(self):
        mapping = SenderRecArrayElementMapping()
        mapping.setIndexedArrayElement(_indexed(index=7))

        element = _write(mapping)
        assert element is not None
        children = [child.tag for child in element]
        assert children == ["INDEX"]
        assert element.find("INDEX").text == "7"

    def test_write_none_omits_wrapper(self):
        mapping = SenderRecArrayElementMapping()
        mapping.setIndexedArrayElement(None)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSenderRecArrayElementMapping(parent, mapping)
        assert parent.find("SENDER-REC-ARRAY-ELEMENT-MAPPING/INDEXED-ARRAY-ELEMENT") is None

    def test_round_trip_preserves_all_values(self):
        mapping = SenderRecArrayElementMapping()
        mapping.setIndexedArrayElement(_indexed("/Types/Array1/Elem", "/Types/ImplArray1/Elem", 3))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSenderRecArrayElementMapping(parent, mapping)
        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parsed = SenderRecArrayElementMapping()
        ARXMLParser().readSenderRecArrayElementMapping(reparsed[0], parsed)

        indexed = parsed.getIndexedArrayElement()
        assert isinstance(indexed, IndexedArrayElement)
        assert indexed.getApplicationArrayElementRef().getValue() == "/Types/Array1/Elem"
        assert indexed.getApplicationArrayElementRef().getDest() == "APPLICATION-ARRAY-ELEMENT"
        assert indexed.getImplementationArrayElementRef().getValue() == "/Types/ImplArray1/Elem"
        assert indexed.getImplementationArrayElementRef().getDest() == "IMPLEMENTATION-ARRAY-ELEMENT"
        assert indexed.getIndex().getValue() == 3
        assert indexed.getChecksum().getValue() == "1234"
        assert indexed.getTimestamp().getValue() == "2024-01-01T00:00:00Z"
