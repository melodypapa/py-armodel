"""Reader tests for UserDefinedTransformationDescription (Table 7.7, p.771).

Zero own attributes (XSD group USER-DEFINED-TRANSFORMATION-DESCRIPTION has an
empty sequence); the class carries only the Describable content and the
TRANSFORMATION-DESCRIPTION group (VARIATION-POINT).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    TransformationTechnology,
    UserDefinedTransformationDescription,
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


class TestUserDefinedTransformationDescription:
    def test_read_user_defined_transformation_description_with_category(self, parser):
        root = _snip("<USER-DEFINED-TRANSFORMATION-DESCRIPTION><CATEGORY>custom</CATEGORY></USER-DEFINED-TRANSFORMATION-DESCRIPTION>")
        element = parser.find(root, "USER-DEFINED-TRANSFORMATION-DESCRIPTION")
        desc = UserDefinedTransformationDescription()
        parser.readUserDefinedTransformationDescription(element, desc)

        assert isinstance(desc, UserDefinedTransformationDescription)
        assert desc.getCategory() is not None
        assert desc.getCategory().getValue() == "custom"

    def test_read_user_defined_transformation_description_empty(self, parser):
        root = _snip("<USER-DEFINED-TRANSFORMATION-DESCRIPTION></USER-DEFINED-TRANSFORMATION-DESCRIPTION>")
        element = parser.find(root, "USER-DEFINED-TRANSFORMATION-DESCRIPTION")
        desc = UserDefinedTransformationDescription()
        parser.readUserDefinedTransformationDescription(element, desc)

        assert desc.getCategory() is None
        assert desc.getDesc() is None

    def test_read_transformation_technology_dispatch(self, parser):
        xml = """
          <TRANSFORMATION-TECHNOLOGY>
            <SHORT-NAME>tech1</SHORT-NAME>
            <TRANSFORMATION-DESCRIPTIONS>
              <USER-DEFINED-TRANSFORMATION-DESCRIPTION>
                <CATEGORY>custom</CATEGORY>
              </USER-DEFINED-TRANSFORMATION-DESCRIPTION>
            </TRANSFORMATION-DESCRIPTIONS>
          </TRANSFORMATION-TECHNOLOGY>
        """
        root = _snip(xml)
        element = parser.find(root, "TRANSFORMATION-TECHNOLOGY")
        tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")
        parser.readTransformationTechnology(element, tech)

        desc = tech.getTransformationDescription()
        assert isinstance(desc, UserDefinedTransformationDescription)
        assert desc.getCategory() is not None
        assert desc.getCategory().getValue() == "custom"
