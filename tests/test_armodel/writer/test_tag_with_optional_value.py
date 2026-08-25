"""Writer/reader round-trip tests for TagWithOptionalValue (Table 6.159, p.478).

TagWithOptionalValue is an inline ARObject value type consumed by
AbstractServiceInstance.capabilityRecord, SdClientConfig.capabilityRecord,
SdServerConfig.capabilityRecord and the environmentVariable aggregations
(serialized as TAG-WITH-OPTIONAL-VALUE carrying KEY / SEQUENCE-OFFSET / VALUE).
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue import (
    TagWithOptionalValue,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


def _serialize_and_wrap(parent: ET.Element) -> ET.Element:
    inner = ET.tostring(parent).decode("utf-8")
    root = ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")
    return root[0]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _full_tag(key="passreq", offset="3", value=""):
    tag = TagWithOptionalValue()
    tag.setKey(String().setValue(key))
    tag.setSequenceOffset(Integer().setValue(offset))
    if value:
        tag.setValue(String().setValue(value))
    return tag


class TestWriteTagWithOptionalValue:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.setTagWithOptionalValue(parent, "TAG-WITH-OPTIONAL-VALUE", _full_tag(value="JPEG,MPEG2"))
        element = parent.find("TAG-WITH-OPTIONAL-VALUE")
        assert element is not None
        assert element.find("KEY").text == "passreq"
        assert element.find("SEQUENCE-OFFSET").text == "3"
        assert element.find("VALUE").text == "JPEG,MPEG2"

    def test_write_none_omits_element(self, writer):
        parent = ET.Element("PARENT")
        writer.setTagWithOptionalValue(parent, "TAG-WITH-OPTIONAL-VALUE", None)
        assert parent.find("TAG-WITH-OPTIONAL-VALUE") is None


class TestTagWithOptionalValueRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.setTagWithOptionalValue(parent, "TAG-WITH-OPTIONAL-VALUE", _full_tag(value="JPEG,MPEG2"))
        element = _serialize_and_wrap(parent)
        result = parser.getTagWithOptionalValue(element, "TAG-WITH-OPTIONAL-VALUE")
        assert isinstance(result, TagWithOptionalValue)
        assert result.getKey().getValue() == "passreq"
        assert result.getSequenceOffset().getValue() == 3
        assert result.getValue().getValue() == "JPEG,MPEG2"

    def test_reader_empty_fields(self, writer, parser):
        parent = ET.Element("{%s}PARENT" % NS)
        ET.SubElement(parent, "{%s}TAG-WITH-OPTIONAL-VALUE" % NS)
        result = parser.getTagWithOptionalValue(parent, "TAG-WITH-OPTIONAL-VALUE")
        assert isinstance(result, TagWithOptionalValue)
        assert result.getKey() is None
        assert result.getSequenceOffset() is None
        assert result.getValue() is None
