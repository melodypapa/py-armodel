"""Reader tests for SOMEIPTransformationProps (Table 7.16, p.783)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import SOMEIPTransformationProps
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


class TestReadSOMEIPTransformationProps:
    def test_read_all_elements(self, parser):
        """
        All five SOMEIP-TRANSFORMATION-PROPS group elements plus the Identifiable level
        owned by readTransformationProps (SHORT-NAME, UUID, CATEGORY) are read into the object.
        """
        element = ET.fromstring(
            "<SOMEIP-TRANSFORMATION-PROPS xmlns='%s' UUID='1a2b3c4d-5e6f-4789-8a9b-0c1d2e3f4a5b'>"
            "<SHORT-NAME>someipProps</SHORT-NAME>"
            "<CATEGORY>someip</CATEGORY>"
            "<ALIGNMENT>8</ALIGNMENT>"
            "<SIZE-OF-ARRAY-LENGTH-FIELD>4</SIZE-OF-ARRAY-LENGTH-FIELD>"
            "<SIZE-OF-STRING-LENGTH-FIELD>4</SIZE-OF-STRING-LENGTH-FIELD>"
            "<SIZE-OF-STRUCT-LENGTH-FIELD>4</SIZE-OF-STRUCT-LENGTH-FIELD>"
            "<SIZE-OF-UNION-LENGTH-FIELD>4</SIZE-OF-UNION-LENGTH-FIELD>"
            "</SOMEIP-TRANSFORMATION-PROPS>" % NS
        )

        props = parser.readSOMEIPTransformationProps(element, SOMEIPTransformationProps(None, "someipProps"))

        assert props.getShortName() == "someipProps"
        assert props.getUuid().getValue() == "1a2b3c4d-5e6f-4789-8a9b-0c1d2e3f4a5b"
        assert props.getCategory().getValue() == "someip"
        assert props.getAlignment().getValue() == 8
        assert props.getSizeOfArrayLengthField().getValue() == 4
        assert props.getSizeOfStringLengthField().getValue() == 4
        assert props.getSizeOfStructLengthField().getValue() == 4
        assert props.getSizeOfUnionLengthField().getValue() == 4

    def test_read_empty_element(self, parser):
        """
        A SOMEIP-TRANSFORMATION-PROPS element without group content leaves the fields unset.
        """
        element = ET.fromstring("<SOMEIP-TRANSFORMATION-PROPS xmlns='%s'></SOMEIP-TRANSFORMATION-PROPS>" % NS)

        props = parser.readSOMEIPTransformationProps(element, SOMEIPTransformationProps(None, "someipProps"))

        assert props.getAlignment() is None
        assert props.getSizeOfArrayLengthField() is None
        assert props.getSizeOfStringLengthField() is None
        assert props.getSizeOfStructLengthField() is None
        assert props.getSizeOfUnionLengthField() is None
