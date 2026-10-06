"""Reader tests for TransformationDescription (Table 4.89, p.199).

Abstract class (Base = ARObject, Describable) — exercised through its concrete
subclass EndToEndTransformationDescription. XML group order per XSD complexType
END-TO-END-TRANSFORMATION-DESCRIPTION: AR-OBJECT, DESCRIBABLE (DESC, CATEGORY,
INTRODUCTION, ADMIN-DATA), TRANSFORMATION-DESCRIPTION (VARIATION-POINT), then the
subclass's own group.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    EndToEndTransformationDescription,
    TransformationDescription,
    TransformationTechnology,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str) -> ET.Element:
    xml = "<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner)
    return ET.fromstring(xml)


def _e2e_desc_element(inner: str) -> ET.Element:
    return _snip("<END-TO-END-TRANSFORMATION-DESCRIPTION>%s</END-TO-END-TRANSFORMATION-DESCRIPTION>" % inner)[0]


def _tech_element(inner: str) -> ET.Element:
    return _snip("<TRANSFORMATION-TECHNOLOGY><SHORT-NAME>tech1</SHORT-NAME>%s</TRANSFORMATION-TECHNOLOGY>" % inner)[0]


class TestTransformationDescriptionReader:
    def test_read_transformation_description_full(self, parser):
        element = _e2e_desc_element("<CATEGORY>myCategory</CATEGORY>" "<VARIATION-POINT><SHORT-LABEL>vp1</SHORT-LABEL></VARIATION-POINT>" "<COUNTER-OFFSET>8</COUNTER-OFFSET>")
        desc = EndToEndTransformationDescription()

        parser.readTransformationDescription(element, desc)

        assert isinstance(desc, TransformationDescription)
        assert desc.getCategory() is not None
        assert desc.getCategory().getValue() == "myCategory"

        variation_point = desc.getVariationPoint()
        assert variation_point is not None
        assert variation_point.getShortLabel() is not None
        assert variation_point.getShortLabel().getValue() == "vp1"

    def test_read_transformation_description_without_variation_point(self, parser):
        element = _e2e_desc_element("<CATEGORY>myCategory</CATEGORY><COUNTER-OFFSET>8</COUNTER-OFFSET>")
        desc = EndToEndTransformationDescription()

        parser.readTransformationDescription(element, desc)

        assert desc.getVariationPoint() is None
        assert desc.getCategory() is not None
        assert desc.getCategory().getValue() == "myCategory"

    def test_read_transformation_technology_dispatch_with_variation_point(self, parser):
        element = _tech_element(
            "<TRANSFORMATION-DESCRIPTIONS>"
            "<END-TO-END-TRANSFORMATION-DESCRIPTION>"
            "<VARIATION-POINT><SHORT-LABEL>tech1-vp</SHORT-LABEL></VARIATION-POINT>"
            "<COUNTER-OFFSET>16</COUNTER-OFFSET>"
            "</END-TO-END-TRANSFORMATION-DESCRIPTION>"
            "</TRANSFORMATION-DESCRIPTIONS>"
        )
        tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")

        parser.readTransformationTechnology(element, tech)

        desc = tech.getTransformationDescription()
        assert isinstance(desc, EndToEndTransformationDescription)
        assert desc.getCounterOffset() is not None
        assert desc.getCounterOffset().getValue() == 16

        variation_point = desc.getVariationPoint()
        assert variation_point is not None
        assert variation_point.getShortLabel() is not None
        assert variation_point.getShortLabel().getValue() == "tech1-vp"

    def test_read_transformation_technology_without_transformation_description(self, parser):
        element = _tech_element("")
        tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")

        parser.readTransformationTechnology(element, tech)

        assert tech.getTransformationDescription() is None
