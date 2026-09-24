"""Writer round-trip tests for the LifeCyclePeriod helper (LIFE-CYCLE-PERIOD: DATE + AR-RELEASE-VERSION + PRODUCT-RELEASE)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, RevisionLabelString
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import LifeCyclePeriod
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


def _period() -> LifeCyclePeriod:
    period = LifeCyclePeriod()
    period.setDate(DateTime().setValue("2023-06-15T12:00:00+01:00"))
    period.setArReleaseVersion(RevisionLabelString().setValue("4.3.1"))
    period.setProductRelease(RevisionLabelString().setValue("1.2.3"))
    return period


def _round_trip(element: ET.Element) -> ET.Element:
    xml_str = ET.tostring(element).decode()
    if xml_str.rstrip().endswith("/>"):
        xml_str = xml_str.rstrip()[:-2].rstrip() + f' xmlns="{NS}"/>'
    else:
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + f' xmlns="{NS}"' + xml_str[idx:]
    return ET.fromstring(xml_str)


class TestSetLifeCyclePeriod:
    def test_write_element_order(self, writer):
        """Test that the written XML children are DATE, AR-RELEASE-VERSION then PRODUCT-RELEASE (XSD sequenceOffset 10/20/30)."""
        parent = ET.Element("PARENT")
        writer.setLifeCyclePeriod(parent, "PERIOD-BEGIN", _period())
        wrapper = parent.find("PERIOD-BEGIN")
        assert wrapper is not None
        assert [child.tag for child in wrapper] == ["DATE", "AR-RELEASE-VERSION", "PRODUCT-RELEASE"]
        assert wrapper.find("DATE").text == "2023-06-15T12:00:00+01:00"
        assert wrapper.find("AR-RELEASE-VERSION").text == "4.3.1"
        assert wrapper.find("PRODUCT-RELEASE").text == "1.2.3"

    def test_write_none(self, writer):
        """Test that a None period writes no element."""
        parent = ET.Element("PARENT")
        writer.setLifeCyclePeriod(parent, "PERIOD-BEGIN", None)
        assert len(parent) == 0

    def test_write_empty_wrapper(self, writer):
        """Test that a LifeCyclePeriod with no fields writes an empty wrapper element."""
        parent = ET.Element("PARENT")
        writer.setLifeCyclePeriod(parent, "PERIOD-END", LifeCyclePeriod())
        wrapper = parent.find("PERIOD-END")
        assert wrapper is not None
        assert len(list(wrapper)) == 0

    def test_round_trip_values_preserved(self, writer, parser):
        """Test parse -> write -> re-parse preserves field values and types."""
        parent_element = ET.fromstring(
            f"<PARENT xmlns='{NS}'>"
            "<PERIOD-BEGIN>"
            "<DATE>2023-06-15T12:00:00+01:00</DATE>"
            "<AR-RELEASE-VERSION>4.3.1</AR-RELEASE-VERSION>"
            "<PRODUCT-RELEASE>1.2.3</PRODUCT-RELEASE>"
            "</PERIOD-BEGIN>"
            "</PARENT>"
        )
        parsed = parser.getLifeCyclePeriod(parent_element, "PERIOD-BEGIN")
        assert parsed is not None

        parent = ET.Element("PARENT")
        writer.setLifeCyclePeriod(parent, "PERIOD-BEGIN", parsed)
        wrapper = parent.find("PERIOD-BEGIN")
        assert wrapper.find("DATE").text == "2023-06-15T12:00:00+01:00"
        assert wrapper.find("AR-RELEASE-VERSION").text == "4.3.1"
        assert wrapper.find("PRODUCT-RELEASE").text == "1.2.3"

        reparsed = parser.getLifeCyclePeriod(_round_trip(parent), "PERIOD-BEGIN")
        assert reparsed is not None
        assert isinstance(reparsed.getDate(), DateTime)
        assert reparsed.getDate().getValue() == "2023-06-15T12:00:00+01:00"
        assert isinstance(reparsed.getArReleaseVersion(), RevisionLabelString)
        assert reparsed.getArReleaseVersion().getValue() == "4.3.1"
        assert isinstance(reparsed.getProductRelease(), RevisionLabelString)
        assert reparsed.getProductRelease().getValue() == "1.2.3"
