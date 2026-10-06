"""Writer/reader round-trip tests for BufferProperties (Table 4.88, p.199)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import BufferProperties, TransformationTechnology
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
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


def _full_props():
    props = BufferProperties()
    props.setHeaderLength(Integer().setValue("8"))
    props.setInPlace(Boolean().setValue(True))
    return props


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")


class TestBufferPropertiesWriter:
    def test_write_buffer_properties_full(self, writer):
        parent = ET.Element("TRANSFORMATION-TECHNOLOGY")
        writer.setBufferProperties(parent, "BUFFER-PROPERTIES", _full_props())

        el = parent.find("BUFFER-PROPERTIES")
        assert el is not None
        assert el.find("HEADER-LENGTH").text == "8"
        assert el.find("IN-PLACE").text == "true"
        assert el.find("BUFFER-COMPUTATION") is None
        children = [child.tag for child in el]
        assert children == ["HEADER-LENGTH", "IN-PLACE"]

    def test_write_buffer_properties_empty(self, writer):
        parent = ET.Element("TRANSFORMATION-TECHNOLOGY")
        writer.setBufferProperties(parent, "BUFFER-PROPERTIES", BufferProperties())

        el = parent.find("BUFFER-PROPERTIES")
        assert el is not None
        assert len(el) == 0

    def test_write_buffer_properties_none(self, writer):
        parent = ET.Element("TRANSFORMATION-TECHNOLOGY")
        writer.setBufferProperties(parent, "BUFFER-PROPERTIES", None)

        assert parent.find("BUFFER-PROPERTIES") is None


class TestBufferPropertiesRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")
        tech.setBufferProperties(_full_props())

        parent = ET.Element("PARENT")
        writer.writeTransformationTechnology(parent, tech)

        out_file = str(tmp_path / "buffer_properties.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent[0]), encoding="unicode"))

        recovered_tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")
        tree = ET.parse(out_file)
        parser.readTransformationTechnology(tree.getroot()[0], recovered_tech)

        recovered = recovered_tech.getBufferProperties()
        assert isinstance(recovered, BufferProperties)
        assert recovered.getHeaderLength() is not None
        assert recovered.getHeaderLength().getValue() == 8
        assert recovered.getInPlace() is not None
        assert recovered.getInPlace().getValue() is True
