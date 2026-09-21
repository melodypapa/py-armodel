"""Parser tests for PduMappingDefaultValue (Table 8.5, p.841).

Aggregated by TargetIPduRef.defaultValue. Element order per XSD groups
TARGET-I-PDU-REF and PDU-MAPPING-DEFAULT-VALUE: TARGET-I-PDU-REF,
DEFAULT-VALUE-ELEMENTS (choice of DEFAULT-VALUE-ELEMENT with
ELEMENT-BYTE-VALUE, ELEMENT-POSITION).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import DefaultValueElement, PduMappingDefaultValue, TargetIPduRef
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


TARGET_IPDU_XML = (
    "<TARGET-I-PDU>"
    '<TARGET-I-PDU-REF DEST="PDU-TRIGGERING">/Cluster/PT_Target</TARGET-I-PDU-REF>'
    "<DEFAULT-VALUE-ELEMENTS>"
    "<DEFAULT-VALUE-ELEMENT><ELEMENT-BYTE-VALUE>171</ELEMENT-BYTE-VALUE><ELEMENT-POSITION>0</ELEMENT-POSITION></DEFAULT-VALUE-ELEMENT>"
    "<DEFAULT-VALUE-ELEMENT><ELEMENT-BYTE-VALUE>204</ELEMENT-BYTE-VALUE><ELEMENT-POSITION>1</ELEMENT-POSITION></DEFAULT-VALUE-ELEMENT>"
    "</DEFAULT-VALUE-ELEMENTS>"
    "</TARGET-I-PDU>"
)


class TestReadPduMappingDefaultValue:
    def test_read_field_values(self):
        root = _snip(TARGET_IPDU_XML)
        parser = ARXMLParser()
        target = parser.getTargetIPduRef(root, "TARGET-I-PDU")

        assert isinstance(target, TargetIPduRef)
        assert target.getTargetIPduRef().getValue() == "/Cluster/PT_Target"
        assert target.getTargetIPduRef().getDest() == "PDU-TRIGGERING"

        default_value = target.getDefaultValue()
        assert isinstance(default_value, PduMappingDefaultValue)
        elements = default_value.getDefaultValueElements()
        assert len(elements) == 2
        assert all(isinstance(element, DefaultValueElement) for element in elements)
        assert elements[0].getElementByteValue().getValue() == 171
        assert elements[0].getElementPosition().getValue() == 0
        assert elements[1].getElementByteValue().getValue() == 204
        assert elements[1].getElementPosition().getValue() == 1

    def test_read_without_default_value(self):
        root = _snip("<TARGET-I-PDU>" '<TARGET-I-PDU-REF DEST="PDU-TRIGGERING">/Cluster/PT_Target</TARGET-I-PDU-REF>' "</TARGET-I-PDU>")
        parser = ARXMLParser()
        target = parser.getTargetIPduRef(root, "TARGET-I-PDU")

        assert target.getDefaultValue() is None
        assert target.getTargetIPduRef().getValue() == "/Cluster/PT_Target"
