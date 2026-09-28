"""Parser tests for IndexedArrayElement (Table 5.32, p.237).

Element order per XSD group INDEXED-ARRAY-ELEMENT: APPLICATION-ARRAY-ELEMENT-REF,
IMPLEMENTATION-ARRAY-ELEMENT-REF, INDEX.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    IndexedArrayElement,
    SenderRecArrayElementMapping,
)
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


class TestReadIndexedArrayElement:
    def test_read_field_values(self):
        root = _snip(
            "<SENDER-REC-ARRAY-ELEMENT-MAPPING>"
            "<INDEXED-ARRAY-ELEMENT>"
            '<APPLICATION-ARRAY-ELEMENT-REF DEST="APPLICATION-ARRAY-ELEMENT">/Types/Array1/Elem</APPLICATION-ARRAY-ELEMENT-REF>'
            '<IMPLEMENTATION-ARRAY-ELEMENT-REF DEST="IMPLEMENTATION-ARRAY-ELEMENT">/Types/ImplArray1/Elem</IMPLEMENTATION-ARRAY-ELEMENT-REF>'
            "<INDEX>3</INDEX>"
            "</INDEXED-ARRAY-ELEMENT>"
            "</SENDER-REC-ARRAY-ELEMENT-MAPPING>"
        )
        mapping = SenderRecArrayElementMapping()
        ARXMLParser().readSenderRecArrayElementMapping(root[0], mapping)

        indexed = mapping.getIndexedArrayElement()
        assert isinstance(indexed, IndexedArrayElement)
        assert indexed.getApplicationArrayElementRef().getValue() == "/Types/Array1/Elem"
        assert indexed.getApplicationArrayElementRef().getDest() == "APPLICATION-ARRAY-ELEMENT"
        assert indexed.getImplementationArrayElementRef().getValue() == "/Types/ImplArray1/Elem"
        assert indexed.getImplementationArrayElementRef().getDest() == "IMPLEMENTATION-ARRAY-ELEMENT"
        assert indexed.getIndex().getValue() == 3

    def test_read_absent_children_default_none(self):
        root = _snip("<SENDER-REC-ARRAY-ELEMENT-MAPPING>" "<INDEXED-ARRAY-ELEMENT />" "</SENDER-REC-ARRAY-ELEMENT-MAPPING>")
        mapping = SenderRecArrayElementMapping()
        ARXMLParser().readSenderRecArrayElementMapping(root[0], mapping)

        indexed = mapping.getIndexedArrayElement()
        assert isinstance(indexed, IndexedArrayElement)
        assert indexed.getApplicationArrayElementRef() is None
        assert indexed.getImplementationArrayElementRef() is None
        assert indexed.getIndex() is None

    def test_read_partial_index_only(self):
        root = _snip("<INDEXED-ARRAY-ELEMENT>" "<INDEX>7</INDEX>" "</INDEXED-ARRAY-ELEMENT>")
        indexed = IndexedArrayElement()
        ARXMLParser().readIndexedArrayElement(root[0], indexed)

        assert indexed.getApplicationArrayElementRef() is None
        assert indexed.getImplementationArrayElementRef() is None
        assert indexed.getIndex().getValue() == 7

    def test_read_absent_wrapper_leaves_field_none(self):
        root = _snip("<SENDER-REC-ARRAY-ELEMENT-MAPPING />")
        mapping = SenderRecArrayElementMapping()
        ARXMLParser().readSenderRecArrayElementMapping(root[0], mapping)

        assert mapping.getIndexedArrayElement() is None
