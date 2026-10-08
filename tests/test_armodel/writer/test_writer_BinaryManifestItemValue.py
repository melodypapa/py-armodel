"""Writer/reader round-trip tests for BinaryManifestItemValue (Table 11.25, p.922)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import BinaryManifestItemValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
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


class ConcreteItemValue(BinaryManifestItemValue):
    pass


class TestWriteBinaryManifestItemValue:
    def test_write_ar_object_level(self, writer):
        """
        The helper writes the ARObject S attribute into the concrete subclass element created by
        the caller (Table 11.25 declares no Attribute rows of its own).
        """
        element = ET.Element("BINARY-MANIFEST-ITEM-NUMERICAL-VALUE")
        value = ConcreteItemValue()
        value.setChecksum(String().setValue("31"))
        writer.writeBinaryManifestItemValue(element, value)

        assert element.attrib["S"] == "31"

    def test_write_empty_element(self, writer):
        """
        With no inherited state, no attributes are emitted.
        """
        element = ET.Element("BINARY-MANIFEST-ITEM-NUMERICAL-VALUE")
        writer.writeBinaryManifestItemValue(element, ConcreteItemValue())

        assert len(element.attrib) == 0
        assert len(element) == 0


class TestBinaryManifestItemValueRoundTrip:
    def test_round_trip_preserves_checksum(self, writer, parser):
        """
        Write -> serialize -> parse keeps the inherited ARObject checksum.
        """
        element = ET.Element("BINARY-MANIFEST-ITEM-NUMERICAL-VALUE")
        value = ConcreteItemValue()
        value.setChecksum(String().setValue("31"))
        writer.writeBinaryManifestItemValue(element, value)
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        parsed = parser.readBinaryManifestItemValue(parsed_element, ConcreteItemValue())

        assert parsed.getChecksum().getValue() == "31"
