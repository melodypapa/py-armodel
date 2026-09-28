"""Parser tests for DefaultValueElement (AUTOSAR_CP_TPS_SystemTemplate Table 8.6, p.841).

Aggregated by PduMappingDefaultValue.defaultValueElement. Element order per XSD
group DEFAULT-VALUE-ELEMENT (00052.xsd L30881): ELEMENT-BYTE-VALUE,
ELEMENT-POSITION; complexType = AR-OBJECT group + own group.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import DefaultValueElement
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


class TestReadDefaultValueElement:
    def _parse(self, inner: str) -> DefaultValueElement:
        root = _snip(inner)
        node = ARXMLParser().find(root, "DEFAULT-VALUE-ELEMENT")
        element = DefaultValueElement()
        ARXMLParser().readDefaultValueElement(node, element)
        return element

    def test_read_field_values(self):
        element = self._parse("<DEFAULT-VALUE-ELEMENT><ELEMENT-BYTE-VALUE>171</ELEMENT-BYTE-VALUE><ELEMENT-POSITION>0</ELEMENT-POSITION></DEFAULT-VALUE-ELEMENT>")

        assert element.getElementByteValue() is not None
        assert element.getElementByteValue().getValue() == 171
        assert element.getElementPosition() is not None
        assert element.getElementPosition().getValue() == 0

    def test_read_partial_element(self):
        element = self._parse("<DEFAULT-VALUE-ELEMENT><ELEMENT-POSITION>3</ELEMENT-POSITION></DEFAULT-VALUE-ELEMENT>")

        assert element.getElementByteValue() is None
        assert element.getElementPosition().getValue() == 3

    def test_read_absent_elements_yields_none(self):
        element = self._parse("<DEFAULT-VALUE-ELEMENT/>")

        assert element.getElementByteValue() is None
        assert element.getElementPosition() is None

    def test_read_arobject_attributes(self):
        element = self._parse('<DEFAULT-VALUE-ELEMENT S="17" T="2023-11-02T12:00:00+01:00"><ELEMENT-BYTE-VALUE>1</ELEMENT-BYTE-VALUE></DEFAULT-VALUE-ELEMENT>')

        assert element.getChecksum().getValue() == "17"
        assert element.getTimestamp().getValue() == "2023-11-02T12:00:00+01:00"
        assert element.getElementByteValue().getValue() == 1

    def test_dispatch_via_target_ipdu_ref(self):
        root = _snip(
            "<TARGET-I-PDU>"
            "<DEFAULT-VALUE>"
            "<DEFAULT-VALUE-ELEMENTS>"
            "<DEFAULT-VALUE-ELEMENT><ELEMENT-BYTE-VALUE>255</ELEMENT-BYTE-VALUE><ELEMENT-POSITION>2</ELEMENT-POSITION></DEFAULT-VALUE-ELEMENT>"
            "</DEFAULT-VALUE-ELEMENTS>"
            "</DEFAULT-VALUE>"
            '<TARGET-I-PDU-REF DEST="PDU-TRIGGERING">/Cluster/PT_Target</TARGET-I-PDU-REF>'
            "</TARGET-I-PDU>"
        )
        target = ARXMLParser().getTargetIPduRef(root, "TARGET-I-PDU")

        elements = target.getDefaultValue().getDefaultValueElements()
        assert len(elements) == 1
        assert elements[0].getElementByteValue().getValue() == 255
        assert elements[0].getElementPosition().getValue() == 2
