"""Reader tests for the TransformationProps reusable helper (Table 7.15, p.783)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import TransformationProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class ConcreteTransformationProps(TransformationProps):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadTransformationProps:
    def test_read_identifiable_level(self, parser):
        """
        The XSD TRANSFORMATION-PROPS group (AUTOSAR_00052.xsd l.125529) has an empty sequence,
        so the helper owns the Identifiable level of the concrete subclass element: SHORT-NAME,
        UUID and CATEGORY are read into the object.
        """
        element = ET.fromstring(
            "<SOMEIP-TRANSFORMATION-PROPS xmlns='%s' UUID='8b2f4e10-1f2a-4d3e-9c5b-0a1b2c3d4e5f'>"
            "<SHORT-NAME>someipProps</SHORT-NAME>"
            "<CATEGORY>someip</CATEGORY>"
            "</SOMEIP-TRANSFORMATION-PROPS>" % NS
        )

        props = parser.readTransformationProps(element, ConcreteTransformationProps(None, "someipProps"))

        assert props.getShortName() == "someipProps"
        assert props.getUuid().getValue() == "8b2f4e10-1f2a-4d3e-9c5b-0a1b2c3d4e5f"
        assert props.getCategory().getValue() == "someip"

    def test_read_empty_element(self, parser):
        """
        A concrete subclass element without Identifiable-level content leaves the state unset.
        """
        element = ET.fromstring("<USER-DEFINED-TRANSFORMATION-PROPS xmlns='%s'></USER-DEFINED-TRANSFORMATION-PROPS>" % NS)

        props = parser.readTransformationProps(element, ConcreteTransformationProps(None, "userDefinedProps"))

        assert props.getUuid() is None
        assert props.getCategory() is None
        assert props.getDesc() is None
