"""Writer round-trip tests for HwAttributeValue (AUTOSAR_CP_TPS_ECUResourceTemplate, Table 2.2, p.16).

Child order per XSD group HW-ATTRIBUTE-VALUE (AUTOSAR_00052.xsd l.65663):
ANNOTATION, HW-ATTRIBUTE-DEF-REF, V, VT, VARIATION-POINT (atpIdentityContributor,
sequenceOffset=10000). V is written as plain numerical text per the
NUMERICAL-VALUE-VARIATION-POINT mixed content model.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    Numerical,
    RefType,
    VerbatimString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _literal(value):
    literal = ARLiteral()
    literal.setValue(value)
    return literal


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _new_attribute_value():
    attribute_value = HwAttributeValue()
    annotation = Annotation()
    annotation.setAnnotationOrigin(_literal("origin text"))
    attribute_value.setAnnotation(annotation)
    attribute_value.setHwAttributeDefRef(_ref("/Hw/Cat/AttrDef", "HW-ATTRIBUTE-DEF"))
    v = Numerical()
    v.setValue("4.2")
    attribute_value.setV(v)
    vt = VerbatimString()
    vt.setValue("some textual value")
    attribute_value.setVt(vt)
    return attribute_value


def test_write_hw_attribute_value_xml():
    parent = ET.Element("ROOT")
    ARXMLWriter().writeHwAttributeValue(parent, _new_attribute_value())

    node = parent.find("HW-ATTRIBUTE-VALUE")
    assert node is not None
    assert node.find("ANNOTATION/ANNOTATION-ORIGIN").text == "origin text"
    assert node.find("HW-ATTRIBUTE-DEF-REF").text == "/Hw/Cat/AttrDef"
    assert node.find("HW-ATTRIBUTE-DEF-REF").attrib["DEST"] == "HW-ATTRIBUTE-DEF"
    assert node.find("V").text == "4.2"
    assert node.find("VT").text == "some textual value"
    assert [child.tag for child in node] == ["ANNOTATION", "HW-ATTRIBUTE-DEF-REF", "V", "VT"]


def test_write_empty_hw_attribute_value_omits_optional_tags():
    parent = ET.Element("ROOT")
    ARXMLWriter().writeHwAttributeValue(parent, HwAttributeValue())

    node = parent.find("HW-ATTRIBUTE-VALUE")
    assert node is not None
    assert len(list(node)) == 0


def test_round_trip_preserves_all_values():
    attribute_value = _new_attribute_value()
    variation_point = VariationPoint()
    variation_point.setShortLabel(_literal("vp1"))
    attribute_value.setVariationPoint(variation_point)

    parent = ET.Element("ROOT")
    ARXMLWriter().writeHwAttributeValue(parent, attribute_value)
    inner = ET.tostring(parent).decode("utf-8")
    root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

    parsed = HwAttributeValue()
    ARXMLParser().readHwAttributeValue(root[0][0], parsed)

    assert parsed.getAnnotation().getAnnotationOrigin().getValue() == "origin text"
    assert parsed.getHwAttributeDefRef().getValue() == "/Hw/Cat/AttrDef"
    assert parsed.getHwAttributeDefRef().getDest() == "HW-ATTRIBUTE-DEF"
    assert parsed.getV().getValue() == "4.2"
    assert parsed.getVt().getValue() == "some textual value"
    assert [child.tag.split("}")[-1] for child in root[0][0]] == ["ANNOTATION", "HW-ATTRIBUTE-DEF-REF", "V", "VT", "VARIATION-POINT"]
    assert parsed.getVariationPoint().getShortLabel().getValue() == "vp1"
