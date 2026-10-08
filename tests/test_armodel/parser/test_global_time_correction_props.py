"""Reader tests for GlobalTimeCorrectionProps (Table 9.7, p.862)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    GlobalTimeCorrectionProps,
)
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


class TestReadGlobalTimeCorrectionProps:
    def test_read_all_fields(self, parser):
        """
        The four rate/offset correction elements are read into their fields.
        """
        element = ET.fromstring(
            "<GLOBAL-TIME-CORRECTION-PROPS xmlns='%s'>"
            "<OFFSET-CORRECTION-ADAPTION-INTERVAL>0.005</OFFSET-CORRECTION-ADAPTION-INTERVAL>"
            "<OFFSET-CORRECTION-JUMP-THRESHOLD>0.5</OFFSET-CORRECTION-JUMP-THRESHOLD>"
            "<RATE-CORRECTION-MEASUREMENT-DURATION>2.0</RATE-CORRECTION-MEASUREMENT-DURATION>"
            "<RATE-CORRECTIONS-PER-MEASUREMENT-DURATION>3</RATE-CORRECTIONS-PER-MEASUREMENT-DURATION>"
            "</GLOBAL-TIME-CORRECTION-PROPS>" % NS
        )

        props = parser.readGlobalTimeCorrectionProps(element, GlobalTimeCorrectionProps())

        assert props.getOffsetCorrectionAdaptionInterval().getValue() == 0.005
        assert props.getOffsetCorrectionJumpThreshold().getValue() == 0.5
        assert props.getRateCorrectionMeasurementDuration().getValue() == 2.0
        assert props.getRateCorrectionsPerMeasurementDuration().getValue() == 3

    def test_read_empty_element(self, parser):
        """
        An empty GLOBAL-TIME-CORRECTION-PROPS element leaves all attributes unset.
        """
        element = ET.fromstring("<GLOBAL-TIME-CORRECTION-PROPS xmlns='%s'></GLOBAL-TIME-CORRECTION-PROPS>" % NS)

        props = parser.readGlobalTimeCorrectionProps(element, GlobalTimeCorrectionProps())

        assert props.getOffsetCorrectionAdaptionInterval() is None
        assert props.getOffsetCorrectionJumpThreshold() is None
        assert props.getRateCorrectionMeasurementDuration() is None
        assert props.getRateCorrectionsPerMeasurementDuration() is None
