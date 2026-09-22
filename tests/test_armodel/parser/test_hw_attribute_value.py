"""Parser tests for HwAttributeValue (AUTOSAR_CP_TPS_ECUResourceTemplate, Table 2.2, p.16).

The reader helper is exercised directly on a HW-ATTRIBUTE-VALUE fragment (the class
has no ARPackage-level dispatch; it nests inside HwDescriptionEntity's
HW-ATTRIBUTE-VALUES wrapper). XML element order per XSD group HW-ATTRIBUTE-VALUE
(AUTOSAR_00052.xsd l.65663): ANNOTATION, HW-ATTRIBUTE-DEF-REF, V, VT, VARIATION-POINT.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeValue
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _attribute_value_fragment():
    return (
        "<HW-ATTRIBUTE-VALUE xmlns='%s'>"
        "<ANNOTATION><ANNOTATION-ORIGIN>origin text</ANNOTATION-ORIGIN></ANNOTATION>"
        "<HW-ATTRIBUTE-DEF-REF DEST='HW-ATTRIBUTE-DEF'>/Hw/Cat/AttrDef</HW-ATTRIBUTE-DEF-REF>"
        "<V>4.2</V>"
        "<VT>some textual value</VT>"
        "</HW-ATTRIBUTE-VALUE>" % NS
    )


def test_parse_hw_attribute_value():
    attribute_value = HwAttributeValue()
    root = ET.fromstring(_attribute_value_fragment())
    ARXMLParser().readHwAttributeValue(root, attribute_value)

    assert attribute_value.getAnnotation().getAnnotationOrigin().getValue() == "origin text"
    assert attribute_value.getHwAttributeDefRef().getValue() == "/Hw/Cat/AttrDef"
    assert attribute_value.getHwAttributeDefRef().getDest() == "HW-ATTRIBUTE-DEF"
    assert attribute_value.getV().getValue() == "4.2"
    assert attribute_value.getVt().getValue() == "some textual value"


def test_parse_hw_attribute_value_empty():
    attribute_value = HwAttributeValue()
    root = ET.fromstring("<HW-ATTRIBUTE-VALUE xmlns='%s'/>" % NS)
    ARXMLParser().readHwAttributeValue(root, attribute_value)

    assert attribute_value.getAnnotation() is None
    assert attribute_value.getHwAttributeDefRef() is None
    assert attribute_value.getV() is None
    assert attribute_value.getVt() is None
    assert attribute_value.getVariationPoint() is None


def test_round_trip_preserves_all_values():
    attribute_value = HwAttributeValue()
    root = ET.fromstring(_attribute_value_fragment())
    ARXMLParser().readHwAttributeValue(root, attribute_value)

    parent = ET.Element("ROOT")
    from armodel.writer.arxml_writer import ARXMLWriter

    ARXMLWriter().writeHwAttributeValue(parent, attribute_value)
    inner = ET.tostring(parent).decode("utf-8")
    reparsed_root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

    parsed = HwAttributeValue()
    ARXMLParser().readHwAttributeValue(reparsed_root[0][0], parsed)

    assert parsed.getAnnotation().getAnnotationOrigin().getValue() == "origin text"
    assert parsed.getHwAttributeDefRef().getValue() == "/Hw/Cat/AttrDef"
    assert parsed.getHwAttributeDefRef().getDest() == "HW-ATTRIBUTE-DEF"
    assert parsed.getV().getValue() == "4.2"
    assert parsed.getVt().getValue() == "some textual value"
