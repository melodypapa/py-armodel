"""Reader tests for BinaryManifestItemNumericalValue (Table 11.26, p.922)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import BinaryManifestItemNumericalValue
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


class TestReadBinaryManifestItemNumericalValue:
    def test_read_value_element_and_base_level(self, parser):
        """
        The Table 11.26 value attribute is read from the VALUE element and the base
        BinaryManifestItemValue helper reads the ARObject S attribute exactly once.
        """
        element = ET.fromstring("<BINARY-MANIFEST-ITEM-NUMERICAL-VALUE xmlns='%s' S='31'>" "<VALUE>4096</VALUE>" "</BINARY-MANIFEST-ITEM-NUMERICAL-VALUE>" % NS)

        value = parser.readBinaryManifestItemNumericalValue(element, BinaryManifestItemNumericalValue())

        assert value.getChecksum().getValue() == "31"
        assert value.getValue().getValue() == 4096

    def test_read_empty_element(self, parser):
        """
        An element without attribute content leaves the fields unset.
        """
        element = ET.fromstring("<BINARY-MANIFEST-ITEM-NUMERICAL-VALUE xmlns='%s'></BINARY-MANIFEST-ITEM-NUMERICAL-VALUE>" % NS)

        value = parser.readBinaryManifestItemNumericalValue(element, BinaryManifestItemNumericalValue())

        assert value.getChecksum() is None
        assert value.getValue() is None
