"""Reader tests for SenderRecArrayElementMapping (Table 5.31, p.237).

XML group SENDER-REC-ARRAY-ELEMENT-MAPPING (AUTOSAR_00052.xsd l.104342):
COMPLEX-TYPE-MAPPING (choice of SENDER-REC-ARRAY-TYPE-MAPPING /
SENDER-REC-RECORD-TYPE-MAPPING) + INDEXED-ARRAY-ELEMENT + SYSTEM-SIGNAL-REF.
Dispatched from SenderRecArrayTypeMapping ARRAY-ELEMENT-MAPPINGS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    IndexedArrayElement,
    SenderRecArrayElementMapping,
    SenderRecArrayTypeMapping,
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


def _parse(xml: str) -> ET.Element:
    return ET.fromstring(xml)


class TestReadSenderRecArrayElementMapping:
    def test_read_full_with_array_type_mapping(self):
        xml = (
            """
        <SENDER-REC-ARRAY-ELEMENT-MAPPING xmlns="%s">
            <COMPLEX-TYPE-MAPPING>
                <SENDER-REC-ARRAY-TYPE-MAPPING>
                    <SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING>
                        <IDENTICAL-MAPPING>true</IDENTICAL-MAPPING>
                    </SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING>
                </SENDER-REC-ARRAY-TYPE-MAPPING>
            </COMPLEX-TYPE-MAPPING>
            <INDEXED-ARRAY-ELEMENT>
                <APPLICATION-ARRAY-ELEMENT-REF DEST="APPLICATION-ARRAY-ELEMENT">/Types/Array1/AppElem</APPLICATION-ARRAY-ELEMENT-REF>
                <INDEX>2</INDEX>
            </INDEXED-ARRAY-ELEMENT>
            <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Signals/Primitive</SYSTEM-SIGNAL-REF>
        </SENDER-REC-ARRAY-ELEMENT-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = SenderRecArrayElementMapping()
        ARXMLParser().readSenderRecArrayElementMapping(element, mapping)

        complex_type_mapping = mapping.getComplexTypeMapping()
        assert isinstance(complex_type_mapping, SenderRecArrayTypeMapping)
        assert complex_type_mapping.getSenderToSignalTextTableMapping() is not None
        indexed = mapping.getIndexedArrayElement()
        assert isinstance(indexed, IndexedArrayElement)
        assert indexed.getApplicationArrayElementRef().getValue() == "/Types/Array1/AppElem"
        assert indexed.getApplicationArrayElementRef().getDest() == "APPLICATION-ARRAY-ELEMENT"
        assert indexed.getIndex().getValue() == 2
        assert mapping.getSystemSignalRef().getValue() == "/Signals/Primitive"
        assert mapping.getSystemSignalRef().getDest() == "SYSTEM-SIGNAL"

    def test_read_with_record_type_mapping(self):
        xml = (
            """
        <SENDER-REC-ARRAY-ELEMENT-MAPPING xmlns="%s">
            <COMPLEX-TYPE-MAPPING>
                <SENDER-REC-RECORD-TYPE-MAPPING/>
            </COMPLEX-TYPE-MAPPING>
            <INDEXED-ARRAY-ELEMENT>
                <IMPLEMENTATION-ARRAY-ELEMENT-REF DEST="IMPLEMENTATION-DATA-TYPE-ELEMENT">/Types/Impl1/Elem</IMPLEMENTATION-ARRAY-ELEMENT-REF>
                <INDEX>0</INDEX>
            </INDEXED-ARRAY-ELEMENT>
        </SENDER-REC-ARRAY-ELEMENT-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = SenderRecArrayElementMapping()
        ARXMLParser().readSenderRecArrayElementMapping(element, mapping)

        assert isinstance(mapping.getComplexTypeMapping(), SenderRecRecordTypeMapping)
        assert mapping.getIndexedArrayElement().getImplementationArrayElementRef().getValue() == "/Types/Impl1/Elem"
        assert mapping.getSystemSignalRef() is None

    def test_read_empty_wrapper(self):
        xml = (
            """
        <SENDER-REC-ARRAY-ELEMENT-MAPPING xmlns="%s">
            <COMPLEX-TYPE-MAPPING/>
        </SENDER-REC-ARRAY-ELEMENT-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = SenderRecArrayElementMapping()
        ARXMLParser().readSenderRecArrayElementMapping(element, mapping)

        assert mapping.getComplexTypeMapping() is None
        assert mapping.getIndexedArrayElement() is None
        assert mapping.getSystemSignalRef() is None

    def test_read_via_array_type_mapping(self):
        xml = (
            """
        <SENDER-REC-ARRAY-TYPE-MAPPING xmlns="%s">
            <ARRAY-ELEMENT-MAPPINGS>
                <SENDER-REC-ARRAY-ELEMENT-MAPPING>
                    <INDEXED-ARRAY-ELEMENT>
                        <INDEX>1</INDEX>
                    </INDEXED-ARRAY-ELEMENT>
                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Signals/Primitive</SYSTEM-SIGNAL-REF>
                </SENDER-REC-ARRAY-ELEMENT-MAPPING>
            </ARRAY-ELEMENT-MAPPINGS>
        </SENDER-REC-ARRAY-TYPE-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        type_mapping = SenderRecArrayTypeMapping()
        ARXMLParser().readSenderRecArrayTypeMapping(element, type_mapping)

        mappings = type_mapping.getArrayElementMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], SenderRecArrayElementMapping)
        assert mappings[0].getIndexedArrayElement().getIndex().getValue() == 1
        assert mappings[0].getSystemSignalRef().getValue() == "/Signals/Primitive"
