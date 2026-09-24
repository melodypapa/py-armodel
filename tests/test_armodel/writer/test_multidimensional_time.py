"""Writer round-trip tests for the MultidimensionalTime helper (MULTIDIMENSIONAL-TIME: CSE-CODE + CSE-CODE-FACTOR)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CseCodeType, Integer
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _mdt(cse_code: str = "100", factor: int = 360) -> MultidimensionalTime:
    mdt = MultidimensionalTime()
    mdt.setCseCode(CseCodeType().setValue(cse_code))
    mdt.setCseCodeFactor(Integer().setValue(factor))
    return mdt


def _round_trip(element: ET.Element) -> ET.Element:
    xml_str = ET.tostring(element).decode()
    if xml_str.rstrip().endswith("/>"):
        xml_str = xml_str.rstrip()[:-2].rstrip() + f' xmlns="{NS}"/>'
    else:
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + f' xmlns="{NS}"' + xml_str[idx:]
    return ET.fromstring(xml_str)


class TestWriteMultidimensionalTime:
    def test_write_element_order(self, writer):
        """Test that the written XML children are CSE-CODE then CSE-CODE-FACTOR (XSD group order)."""
        parent = ET.Element("PARENT")
        writer.setMultidimensionalTime(parent, "MAXIMUM", _mdt())
        wrapper = parent.find("MAXIMUM")
        assert wrapper is not None
        assert [child.tag for child in wrapper] == ["CSE-CODE", "CSE-CODE-FACTOR"]
        assert wrapper.find("CSE-CODE").text == "100"
        assert wrapper.find("CSE-CODE-FACTOR").text == "360"

    def test_write_empty_wrapper(self, writer):
        """Test that a MultidimensionalTime with no fields writes an empty wrapper element."""
        parent = ET.Element("PARENT")
        writer.setMultidimensionalTime(parent, "MINIMUM", MultidimensionalTime())
        wrapper = parent.find("MINIMUM")
        assert wrapper is not None
        assert len(list(wrapper)) == 0

    def test_round_trip_values_preserved(self, writer, parser):
        """Test parse -> write -> re-parse preserves field values."""
        element = ET.fromstring(f"<MAXIMUM xmlns='{NS}'>" "<CSE-CODE>100</CSE-CODE>" "<CSE-CODE-FACTOR>360</CSE-CODE-FACTOR>" "</MAXIMUM>")
        parsed = MultidimensionalTime()
        parser.readMultidimensionalTime(element, parsed)

        parent = ET.Element("PARENT")
        writer.setMultidimensionalTime(parent, "MAXIMUM", parsed)
        wrapper = parent.find("MAXIMUM")
        assert wrapper.find("CSE-CODE").text == "100"
        assert wrapper.find("CSE-CODE-FACTOR").text == "360"

        reparsed = MultidimensionalTime()
        parser.readMultidimensionalTime(_round_trip(wrapper), reparsed)
        assert reparsed.getCseCode().getValue() == "100"
        assert reparsed.getCseCodeFactor().getValue() == 360
        assert isinstance(reparsed.getCseCode(), CseCodeType)
