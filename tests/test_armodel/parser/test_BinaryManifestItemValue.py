"""Reader tests for BinaryManifestItemValue (Table 11.25, p.922)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import BinaryManifestItemValue
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


class ConcreteItemValue(BinaryManifestItemValue):
    pass


class TestReadBinaryManifestItemValue:
    def test_read_ar_object_level(self, parser):
        """
        Table 11.25 declares no Attribute rows, so the helper reads only the inherited ARObject
        level (the S checksum attribute) of the concrete subclass element.
        """
        element = ET.fromstring("<BINARY-MANIFEST-ITEM-NUMERICAL-VALUE xmlns='%s' S='31'></BINARY-MANIFEST-ITEM-NUMERICAL-VALUE>" % NS)

        value = parser.readBinaryManifestItemValue(element, ConcreteItemValue())

        assert value.getChecksum().getValue() == "31"

    def test_read_empty_element(self, parser):
        """
        An element without the ARObject level leaves the inherited state unset.
        """
        element = ET.fromstring("<BINARY-MANIFEST-ITEM-NUMERICAL-VALUE xmlns='%s'></BINARY-MANIFEST-ITEM-NUMERICAL-VALUE>" % NS)

        value = parser.readBinaryManifestItemValue(element, ConcreteItemValue())

        assert value.getChecksum() is None
