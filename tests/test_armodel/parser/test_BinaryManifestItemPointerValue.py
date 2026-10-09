"""Reader tests for BinaryManifestItemPointerValue (Table 11.27, p.922)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import BinaryManifestItemPointerValue
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


class TestReadBinaryManifestItemPointerValue:
    def test_read_address_and_symbol_and_base_level(self, parser):
        """
        The Table 11.27 attributes are read from the element in the XSD
        BINARY-MANIFEST-ITEM-POINTER-VALUE group order (ADDRESS, SYMBOL) and the base
        BinaryManifestItemValue helper reads the ARObject S attribute exactly once.
        """
        element = ET.fromstring("<BINARY-MANIFEST-ITEM-POINTER-VALUE xmlns='%s' S='7'>" "<ADDRESS>0x0000B000</ADDRESS>" "<SYMBOL>PointerTarget</SYMBOL>" "</BINARY-MANIFEST-ITEM-POINTER-VALUE>" % NS)

        value = parser.readBinaryManifestItemPointerValue(element, BinaryManifestItemPointerValue())

        assert value.getChecksum().getValue() == "7"
        assert value.getAddress().getValue() == "0x0000B000"
        assert value.getSymbol().getValue() == "PointerTarget"

    def test_read_empty_element(self, parser):
        """
        An element without attribute content leaves the fields unset.
        """
        element = ET.fromstring("<BINARY-MANIFEST-ITEM-POINTER-VALUE xmlns='%s'></BINARY-MANIFEST-ITEM-POINTER-VALUE>" % NS)

        value = parser.readBinaryManifestItemPointerValue(element, BinaryManifestItemPointerValue())

        assert value.getChecksum() is None
        assert value.getAddress() is None
        assert value.getSymbol() is None
