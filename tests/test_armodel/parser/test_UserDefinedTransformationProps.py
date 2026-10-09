"""Reader tests for UserDefinedTransformationProps (Table 7.29, p.829)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import UserDefinedTransformationProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadUserDefinedTransformationProps:
    def test_read_identifiable_level(self, parser):
        """
        The XSD USER-DEFINED-TRANSFORMATION-PROPS group (AUTOSAR_00052.xsd l.129197) has an
        empty sequence, so the reader owns only the Identifiable level reached through
        readTransformationProps: SHORT-NAME, UUID and CATEGORY are read into the object.
        """
        element = ET.fromstring(
            "<USER-DEFINED-TRANSFORMATION-PROPS xmlns='%s' UUID='2b3c4d5e-6f7a-4899-baab-1d2e3f4a5b6c'>"
            "<SHORT-NAME>userDefinedProps</SHORT-NAME>"
            "<CATEGORY>custom</CATEGORY>"
            "</USER-DEFINED-TRANSFORMATION-PROPS>" % NS
        )

        props = parser.readUserDefinedTransformationProps(element, UserDefinedTransformationProps(None, "userDefinedProps"))

        assert props.getShortName() == "userDefinedProps"
        assert props.getUuid().getValue() == "2b3c4d5e-6f7a-4899-baab-1d2e3f4a5b6c"
        assert props.getCategory().getValue() == "custom"

    def test_read_empty_element(self, parser):
        """
        A USER-DEFINED-TRANSFORMATION-PROPS element without Identifiable-level content
        leaves the state unset.
        """
        element = ET.fromstring("<USER-DEFINED-TRANSFORMATION-PROPS xmlns='%s'></USER-DEFINED-TRANSFORMATION-PROPS>" % NS)

        props = parser.readUserDefinedTransformationProps(element, UserDefinedTransformationProps(None, "userDefinedProps"))

        assert props.getUuid() is None
        assert props.getCategory() is None
        assert props.getDesc() is None
