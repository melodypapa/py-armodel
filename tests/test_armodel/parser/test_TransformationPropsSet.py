"""Reader tests for TransformationPropsSet (Table 7.14, p.782)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import TransformationPropsSet
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    SOMEIPTransformationProps,
    UserDefinedTransformationProps,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    autosar = AUTOSAR.getInstance()
    autosar.new()
    autosar.setARRelease("R23-11")
    yield
    autosar.new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadTransformationPropsSet:
    def test_read_all_elements(self, parser):
        """
        The TRANSFORMATION-PROPSS wrapper children (SOMEIP-TRANSFORMATION-PROPS,
        USER-DEFINED-TRANSFORMATION-PROPS) are dispatched to their concrete subtypes
        and read into the transformationProps list, together with the Identifiable
        base group of the set itself.
        """
        element = ET.fromstring(
            "<TRANSFORMATION-PROPS-SET xmlns='%s' UUID='5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f'>"
            "<SHORT-NAME>tps</SHORT-NAME>"
            "<TRANSFORMATION-PROPSS>"
            "<SOMEIP-TRANSFORMATION-PROPS>"
            "<SHORT-NAME>someipProps</SHORT-NAME>"
            "<ALIGNMENT>8</ALIGNMENT>"
            "<SIZE-OF-ARRAY-LENGTH-FIELD>4</SIZE-OF-ARRAY-LENGTH-FIELD>"
            "</SOMEIP-TRANSFORMATION-PROPS>"
            "<USER-DEFINED-TRANSFORMATION-PROPS>"
            "<SHORT-NAME>userProps</SHORT-NAME>"
            "</USER-DEFINED-TRANSFORMATION-PROPS>"
            "</TRANSFORMATION-PROPSS>"
            "</TRANSFORMATION-PROPS-SET>" % NS
        )

        props_set = parser.readTransformationPropsSet(element, TransformationPropsSet(None, "tps"))

        assert props_set.getShortName() == "tps"
        assert props_set.getUuid().getValue() == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        props_list = props_set.getTransformationProps()
        assert len(props_list) == 2
        assert isinstance(props_list[0], SOMEIPTransformationProps)
        assert props_list[0].getShortName() == "someipProps"
        assert props_list[0].getAlignment().getValue() == 8
        assert props_list[0].getSizeOfArrayLengthField().getValue() == 4
        assert isinstance(props_list[1], UserDefinedTransformationProps)
        assert props_list[1].getShortName() == "userProps"

    def test_read_empty_wrapper(self, parser):
        """
        A TRANSFORMATION-PROPS-SET element without a TRANSFORMATION-PROPSS wrapper
        leaves the transformationProps list empty.
        """
        element = ET.fromstring("<TRANSFORMATION-PROPS-SET xmlns='%s'></TRANSFORMATION-PROPS-SET>" % NS)

        props_set = parser.readTransformationPropsSet(element, TransformationPropsSet(None, "tps"))

        assert props_set.getTransformationProps() == []
