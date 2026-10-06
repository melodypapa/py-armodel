"""Reader tests for BufferProperties (Table 4.88, p.199)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import BufferProperties, TransformationTechnology
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


def _tech_element(inner: str) -> ET.Element:
    return ET.fromstring(f"<TRANSFORMATION-TECHNOLOGY xmlns='{NS}'><SHORT-NAME>tech1</SHORT-NAME>{inner}</TRANSFORMATION-TECHNOLOGY>")


class TestBufferPropertiesReader:
    def test_read_buffer_properties_full(self, parser):
        element = _tech_element("<BUFFER-PROPERTIES><HEADER-LENGTH>8</HEADER-LENGTH><IN-PLACE>true</IN-PLACE></BUFFER-PROPERTIES>")
        tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")

        parser.readTransformationTechnology(element, tech)

        props = tech.getBufferProperties()
        assert isinstance(props, BufferProperties)
        assert props.getHeaderLength() is not None
        assert props.getHeaderLength().getValue() == 8
        assert props.getInPlace() is not None
        assert props.getInPlace().getValue() is True

    def test_read_buffer_properties_empty_wrapper(self, parser):
        element = _tech_element("<BUFFER-PROPERTIES></BUFFER-PROPERTIES>")
        tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")

        parser.readTransformationTechnology(element, tech)

        props = tech.getBufferProperties()
        assert isinstance(props, BufferProperties)
        assert props.getHeaderLength() is None
        assert props.getInPlace() is None

    def test_read_transformation_technology_without_buffer_properties(self, parser):
        element = _tech_element("")
        tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")

        parser.readTransformationTechnology(element, tech)

        assert tech.getBufferProperties() is None
