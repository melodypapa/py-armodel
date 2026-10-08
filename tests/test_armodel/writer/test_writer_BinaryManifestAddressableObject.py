"""Writer/reader round-trip tests for BinaryManifestAddressableObject (Table 11.24, p.921)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import BinaryManifestAddressableObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Address, SymbolString
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


class ConcreteAddressableObject(BinaryManifestAddressableObject):
    pass


def _new_object() -> BinaryManifestAddressableObject:
    obj = ConcreteAddressableObject(AUTOSAR.getInstance(), "Field1")
    obj.setAddress(Address().setValue("0x0000A000"))
    obj.setSymbol(SymbolString().setValue("HandleSymbol"))
    return obj


class TestWriteBinaryManifestAddressableObject:
    def test_write_address_and_symbol_in_xsd_group_order(self, writer):
        """
        The helper writes the Identifiable level (SHORT-NAME) and the Table 11.24 attributes in
        the XSD BINARY-MANIFEST-ADDRESSABLE-OBJECT group order (ADDRESS, SYMBOL).
        """
        element = ET.Element("BINARY-MANIFEST-META-DATA-FIELD")
        writer.writeBinaryManifestAddressableObject(element, _new_object())

        assert [child.tag for child in element] == ["SHORT-NAME", "ADDRESS", "SYMBOL"]
        assert element.find("ADDRESS").text == "0x0000A000"
        assert element.find("SYMBOL").text == "HandleSymbol"

    def test_write_empty_element(self, writer):
        """
        With no attribute content, only the Identifiable level is emitted.
        """
        element = ET.Element("BINARY-MANIFEST-META-DATA-FIELD")
        writer.writeBinaryManifestAddressableObject(element, ConcreteAddressableObject(AUTOSAR.getInstance(), "Field1"))

        assert [child.tag for child in element] == ["SHORT-NAME"]


class TestBinaryManifestAddressableObjectRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps the Identifiable level and both Table 11.24 values.
        """
        element = ET.Element("BINARY-MANIFEST-META-DATA-FIELD")
        writer.writeBinaryManifestAddressableObject(element, _new_object())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        obj = ConcreteAddressableObject(AUTOSAR.getInstance(), "Field1")
        parser.readBinaryManifestAddressableObject(parsed_element, obj)

        assert obj.getShortName() == "Field1"
        assert obj.getAddress().getValue() == "0x0000A000"
        assert obj.getSymbol().getValue() == "HandleSymbol"

    def test_round_trip_empty_element(self, writer, parser):
        """
        An addressable object without attributes round-trips unset (no ADDRESS/SYMBOL tags).
        """
        element = ET.Element("BINARY-MANIFEST-META-DATA-FIELD")
        writer.writeBinaryManifestAddressableObject(element, ConcreteAddressableObject(AUTOSAR.getInstance(), "Field1"))
        xml = ET.tostring(element, encoding="unicode")

        assert "ADDRESS" not in xml
        assert "SYMBOL" not in xml

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        obj = ConcreteAddressableObject(AUTOSAR.getInstance(), "Field1")
        parser.readBinaryManifestAddressableObject(parsed_element, obj)

        assert obj.getAddress() is None
        assert obj.getSymbol() is None
