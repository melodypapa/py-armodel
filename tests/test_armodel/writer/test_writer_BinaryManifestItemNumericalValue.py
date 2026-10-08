"""Writer/reader round-trip tests for BinaryManifestItemNumericalValue (Table 11.26, p.922)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import BinaryManifestItemNumericalValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, String
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


def _new_value() -> BinaryManifestItemNumericalValue:
    value = BinaryManifestItemNumericalValue()
    value.setChecksum(String().setValue("31"))
    value.setValue(Numerical().setValue("4096"))
    return value


class TestWriteBinaryManifestItemNumericalValue:
    def test_write_value_element_in_xsd_order(self, writer):
        """
        The helper writes the ARObject S attribute (via the base helper) and the Table 11.26 VALUE
        element in the XSD BINARY-MANIFEST-ITEM-NUMERICAL-VALUE group order.
        """
        element = ET.Element("BINARY-MANIFEST-ITEM-NUMERICAL-VALUE")
        writer.writeBinaryManifestItemNumericalValue(element, _new_value())

        assert element.attrib["S"] == "31"
        assert [child.tag for child in element] == ["VALUE"]
        assert element.find("VALUE").text == "4096"

    def test_write_empty_element(self, writer):
        """
        With no attribute content, no child elements and no S attribute are emitted.
        """
        element = ET.Element("BINARY-MANIFEST-ITEM-NUMERICAL-VALUE")
        writer.writeBinaryManifestItemNumericalValue(element, BinaryManifestItemNumericalValue())

        assert len(element) == 0
        assert "S" not in element.attrib


class TestBinaryManifestItemNumericalValueRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps the checksum and the numerical value.
        """
        element = ET.Element("BINARY-MANIFEST-ITEM-NUMERICAL-VALUE")
        writer.writeBinaryManifestItemNumericalValue(element, _new_value())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        value = parser.readBinaryManifestItemNumericalValue(parsed_element, BinaryManifestItemNumericalValue())

        assert value.getChecksum().getValue() == "31"
        assert value.getValue().getValue() == 4096

    def test_round_trip_empty_element(self, writer, parser):
        """
        A numerical value without content round-trips unset (no VALUE tag emitted).
        """
        element = ET.Element("BINARY-MANIFEST-ITEM-NUMERICAL-VALUE")
        writer.writeBinaryManifestItemNumericalValue(element, BinaryManifestItemNumericalValue())
        xml = ET.tostring(element, encoding="unicode")

        assert "<VALUE>" not in xml

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        value = parser.readBinaryManifestItemNumericalValue(parsed_element, BinaryManifestItemNumericalValue())

        assert value.getValue() is None
