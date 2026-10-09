"""Writer/reader round-trip tests for BinaryManifestItemPointerValue (Table 11.27, p.922)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import BinaryManifestItemPointerValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Address, String, SymbolString
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _new_value() -> BinaryManifestItemPointerValue:
    value = BinaryManifestItemPointerValue()
    value.setChecksum(String().setValue("7"))
    value.setAddress(Address().setValue("0x0000B000"))
    value.setSymbol(SymbolString().setValue("PointerTarget"))
    return value


class TestWriteBinaryManifestItemPointerValue:
    def test_write_elements_in_xsd_group_order(self, writer):
        """
        The helper writes the ARObject S attribute (via the base helper) and the Table 11.27
        elements in the XSD BINARY-MANIFEST-ITEM-POINTER-VALUE group order (ADDRESS, SYMBOL).
        """
        element = ET.Element("BINARY-MANIFEST-ITEM-POINTER-VALUE")
        writer.writeBinaryManifestItemPointerValue(element, _new_value())

        assert element.attrib["S"] == "7"
        assert [child.tag for child in element] == ["ADDRESS", "SYMBOL"]
        assert element.find("ADDRESS").text == "0x0000B000"
        assert element.find("SYMBOL").text == "PointerTarget"

    def test_write_empty_element(self, writer):
        """
        With no attribute content, no child elements and no S attribute are emitted.
        """
        element = ET.Element("BINARY-MANIFEST-ITEM-POINTER-VALUE")
        writer.writeBinaryManifestItemPointerValue(element, BinaryManifestItemPointerValue())

        assert len(element) == 0
        assert "S" not in element.attrib


class TestBinaryManifestItemPointerValueRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps the checksum and both Table 11.27 values.
        """
        element = ET.Element("BINARY-MANIFEST-ITEM-POINTER-VALUE")
        writer.writeBinaryManifestItemPointerValue(element, _new_value())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        value = parser.readBinaryManifestItemPointerValue(parsed_element, BinaryManifestItemPointerValue())

        assert value.getChecksum().getValue() == "7"
        assert value.getAddress().getValue() == "0x0000B000"
        assert value.getSymbol().getValue() == "PointerTarget"

    def test_round_trip_empty_element(self, writer, parser):
        """
        A pointer value without content round-trips unset (no ADDRESS/SYMBOL tags emitted).
        """
        element = ET.Element("BINARY-MANIFEST-ITEM-POINTER-VALUE")
        writer.writeBinaryManifestItemPointerValue(element, BinaryManifestItemPointerValue())
        xml = ET.tostring(element, encoding="unicode")

        assert "<ADDRESS>" not in xml
        assert "<SYMBOL>" not in xml

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        value = parser.readBinaryManifestItemPointerValue(parsed_element, BinaryManifestItemPointerValue())

        assert value.getAddress() is None
        assert value.getSymbol() is None
