"""Reader tests for BinaryManifestItem (Table 11.22, p.919)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    BinaryManifestItemNumericalValue,
    BinaryManifestItemPointerValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import BinaryManifestItem
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadBinaryManifestItem:
    def test_read_elements_in_xsd_group_order(self, parser):
        """
        The Table 11.22 attributes are read in the XSD BINARY-MANIFEST-ITEM group order
        (IS-UNUSED, VALUE, DEFAULT-VALUE, AUXILIARY-FIELDS) after the inherited
        BinaryManifestAddressableObject helper reads SHORT-NAME / ADDRESS / SYMBOL.
        """
        element = ET.fromstring(
            "<BINARY-MANIFEST-ITEM xmlns='%s'>"
            "<SHORT-NAME>Handle1</SHORT-NAME>"
            "<ADDRESS>0x1000</ADDRESS>"
            "<SYMBOL>HANDLE_1</SYMBOL>"
            "<IS-UNUSED>true</IS-UNUSED>"
            "<VALUE><BINARY-MANIFEST-ITEM-NUMERICAL-VALUE><VALUE>4096</VALUE></BINARY-MANIFEST-ITEM-NUMERICAL-VALUE></VALUE>"
            "<DEFAULT-VALUE><BINARY-MANIFEST-ITEM-POINTER-VALUE><ADDRESS>0x2000</ADDRESS></BINARY-MANIFEST-ITEM-POINTER-VALUE></DEFAULT-VALUE>"
            "<AUXILIARY-FIELDS>"
            "<BINARY-MANIFEST-ITEM><SHORT-NAME>Field1</SHORT-NAME><IS-UNUSED>false</IS-UNUSED></BINARY-MANIFEST-ITEM>"
            "</AUXILIARY-FIELDS>"
            "</BINARY-MANIFEST-ITEM>" % NS
        )

        item = BinaryManifestItem(AUTOSAR.getInstance(), "Handle1")
        parser.readBinaryManifestItem(element, item)

        assert item.getShortName() == "Handle1"
        assert item.getAddress().getValue() == "0x1000"
        assert item.getSymbol().getValue() == "HANDLE_1"
        assert item.getIsUnused().getValue() is True
        assert isinstance(item.getValue(), BinaryManifestItemNumericalValue)
        assert item.getValue().getValue().getValue() == 4096
        assert isinstance(item.getDefaultValue(), BinaryManifestItemPointerValue)
        assert item.getDefaultValue().getAddress().getValue() == "0x2000"
        assert [field.getShortName() for field in item.getAuxiliaryFields()] == ["Field1"]
        assert item.getAuxiliaryFields()[0].getIsUnused().getValue() is False

    def test_read_empty_element(self, parser):
        """
        An element without attribute content leaves the fields unset and the auxiliary
        field list empty.
        """
        element = ET.fromstring("<BINARY-MANIFEST-ITEM xmlns='%s'><SHORT-NAME>Handle2</SHORT-NAME></BINARY-MANIFEST-ITEM>" % NS)

        item = BinaryManifestItem(AUTOSAR.getInstance(), "Handle2")
        parser.readBinaryManifestItem(element, item)

        assert item.getIsUnused() is None
        assert item.getValue() is None
        assert item.getDefaultValue() is None
        assert item.getAuxiliaryFields() == []
