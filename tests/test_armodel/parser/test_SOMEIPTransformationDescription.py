"""Reader tests for SOMEIPTransformationDescription (Table 7.10, p.777).

XML group order per XSD complexType SOMEIP-TRANSFORMATION-DESCRIPTION:
AR-OBJECT, DESCRIBABLE, TRANSFORMATION-DESCRIPTION (VARIATION-POINT), then
ALIGNMENT, BYTE-ORDER, INTERFACE-VERSION.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    SOMEIPTransformationDescription,
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


class TestSOMEIPTransformationDescription:
    def test_read_someip_transformation_description_full(self, parser):
        xml = """
          <SOMEIP-TRANSFORMATION-DESCRIPTION>
            <CATEGORY>someipCategory</CATEGORY>
            <ALIGNMENT>8</ALIGNMENT>
            <BYTE-ORDER>MOST-SIGNIFICANT-BYTE-FIRST</BYTE-ORDER>
            <INTERFACE-VERSION>4</INTERFACE-VERSION>
          </SOMEIP-TRANSFORMATION-DESCRIPTION>
        """
        root = _snip(xml)
        element = parser.find(root, "SOMEIP-TRANSFORMATION-DESCRIPTION")
        desc = SOMEIPTransformationDescription()
        parser.readSOMEIPTransformationDescription(element, desc)

        assert isinstance(desc, SOMEIPTransformationDescription)
        assert desc.getCategory() is not None
        assert desc.getCategory().getValue() == "someipCategory"
        assert desc.getAlignment() is not None
        assert desc.getAlignment().getValue() == 8
        assert desc.getByteOrder() is not None
        assert desc.getByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-FIRST"
        assert desc.getInterfaceVersion() is not None
        assert desc.getInterfaceVersion().getValue() == 4

    def test_read_someip_transformation_description_empty(self, parser):
        root = _snip("<SOMEIP-TRANSFORMATION-DESCRIPTION></SOMEIP-TRANSFORMATION-DESCRIPTION>")
        element = parser.find(root, "SOMEIP-TRANSFORMATION-DESCRIPTION")
        desc = SOMEIPTransformationDescription()
        parser.readSOMEIPTransformationDescription(element, desc)

        assert desc.getAlignment() is None
        assert desc.getByteOrder() is None
        assert desc.getInterfaceVersion() is None

    def test_read_transformation_technology_dispatch(self, parser):
        xml = """
          <TRANSFORMATION-TECHNOLOGY>
            <SHORT-NAME>tech1</SHORT-NAME>
            <TRANSFORMATION-DESCRIPTIONS>
              <SOMEIP-TRANSFORMATION-DESCRIPTION>
                <ALIGNMENT>32</ALIGNMENT>
                <INTERFACE-VERSION>3</INTERFACE-VERSION>
              </SOMEIP-TRANSFORMATION-DESCRIPTION>
            </TRANSFORMATION-DESCRIPTIONS>
          </TRANSFORMATION-TECHNOLOGY>
        """
        root = _snip(xml)
        element = parser.find(root, "TRANSFORMATION-TECHNOLOGY")
        tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")
        parser.readTransformationTechnology(element, tech)

        desc = tech.getTransformationDescription()
        assert isinstance(desc, SOMEIPTransformationDescription)
        assert desc.getAlignment() is not None
        assert desc.getAlignment().getValue() == 32
        assert desc.getInterfaceVersion() is not None
        assert desc.getInterfaceVersion().getValue() == 3
