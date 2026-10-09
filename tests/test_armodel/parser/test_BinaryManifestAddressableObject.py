"""Reader tests for BinaryManifestAddressableObject (Table 11.24, p.921)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import BinaryManifestAddressableObject
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


class ConcreteAddressableObject(BinaryManifestAddressableObject):
    pass


class TestReadBinaryManifestAddressableObject:
    def test_read_address_and_symbol(self, parser):
        """
        The two Table 11.24 attributes are read from the concrete subclass element in the XSD
        BINARY-MANIFEST-ADDRESSABLE-OBJECT group order (ADDRESS, SYMBOL) and the inherited
        Identifiable helper reads SHORT-NAME.
        """
        element = ET.fromstring(
            "<BINARY-MANIFEST-META-DATA-FIELD xmlns='%s'>" "<SHORT-NAME>Field1</SHORT-NAME>" "<ADDRESS>0x0000A000</ADDRESS>" "<SYMBOL>HandleSymbol</SYMBOL>" "</BINARY-MANIFEST-META-DATA-FIELD>" % NS
        )

        obj = ConcreteAddressableObject(AUTOSAR.getInstance(), "Field1")
        parser.readBinaryManifestAddressableObject(element, obj)

        assert obj.getShortName() == "Field1"
        assert obj.getAddress().getValue() == "0x0000A000"
        assert obj.getSymbol().getValue() == "HandleSymbol"

    def test_read_empty_element(self, parser):
        """
        An element without attribute content leaves both fields unset.
        """
        element = ET.fromstring("<BINARY-MANIFEST-META-DATA-FIELD xmlns='%s'><SHORT-NAME>Field1</SHORT-NAME></BINARY-MANIFEST-META-DATA-FIELD>" % NS)

        obj = ConcreteAddressableObject(AUTOSAR.getInstance(), "Field1")
        parser.readBinaryManifestAddressableObject(element, obj)

        assert obj.getAddress() is None
        assert obj.getSymbol() is None
