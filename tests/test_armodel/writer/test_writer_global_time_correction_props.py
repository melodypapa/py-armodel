"""Writer/reader round-trip tests for GlobalTimeCorrectionProps (Table 9.7, p.862)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    GlobalTimeCorrectionProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
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


def _time_value(text):
    value = TimeValue()
    value.setValue(text)
    return value


def _positive_integer(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


def _new_props():
    props = GlobalTimeCorrectionProps()
    props.setOffsetCorrectionAdaptionInterval(_time_value("0.005"))
    props.setOffsetCorrectionJumpThreshold(_time_value("0.5"))
    props.setRateCorrectionMeasurementDuration(_time_value("2.0"))
    props.setRateCorrectionsPerMeasurementDuration(_positive_integer("3"))
    return props


class TestWriteGlobalTimeCorrectionProps:
    def test_write_all_fields(self, writer):
        """
        The helper emits the GLOBAL-TIME-CORRECTION-PROPS element in the XSD sequence order.
        """
        parent = ET.Element("GLOBAL-TIME-DOMAIN")
        writer.writeGlobalTimeCorrectionProps(parent, _new_props())

        node = parent.find("GLOBAL-TIME-CORRECTION-PROPS")
        assert node is not None
        assert [child.tag for child in node] == [
            "OFFSET-CORRECTION-ADAPTION-INTERVAL",
            "OFFSET-CORRECTION-JUMP-THRESHOLD",
            "RATE-CORRECTION-MEASUREMENT-DURATION",
            "RATE-CORRECTIONS-PER-MEASUREMENT-DURATION",
        ]
        assert node.find("OFFSET-CORRECTION-ADAPTION-INTERVAL").text == "0.005"
        assert node.find("RATE-CORRECTIONS-PER-MEASUREMENT-DURATION").text == "3"

    def test_write_empty_fields(self, writer):
        """
        An unset attribute set emits an empty element.
        """
        parent = ET.Element("GLOBAL-TIME-DOMAIN")
        writer.writeGlobalTimeCorrectionProps(parent, GlobalTimeCorrectionProps())

        node = parent.find("GLOBAL-TIME-CORRECTION-PROPS")
        assert node is not None
        assert len(node) == 0


class TestGlobalTimeCorrectionPropsRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every attribute value.
        """
        parent = ET.Element("GLOBAL-TIME-DOMAIN")
        writer.writeGlobalTimeCorrectionProps(parent, _new_props())
        xml = ET.tostring(parent, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readGlobalTimeCorrectionProps(parsed_element[0], GlobalTimeCorrectionProps())

        assert props.getOffsetCorrectionAdaptionInterval().getValue() == 0.005
        assert props.getOffsetCorrectionJumpThreshold().getValue() == 0.5
        assert props.getRateCorrectionMeasurementDuration().getValue() == 2.0
        assert props.getRateCorrectionsPerMeasurementDuration().getValue() == 3
