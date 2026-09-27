"""Parser tests for HardwareConfiguration (readHardwareConfiguration)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import HardwareConfiguration
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

HARDWARE_CONFIGURATION_XML = (
    "<ROOT xmlns='{ns}'>" "<ADDITIONAL-INFORMATION>ECU configuration info</ADDITIONAL-INFORMATION>" "<PROCESSOR-MODE>NORMAL</PROCESSOR-MODE>" "<PROCESSOR-SPEED>600 MHz</PROCESSOR-SPEED>" "</ROOT>"
).format(ns=NS)


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadHardwareConfiguration:
    def test_read_field_values(self, parser):
        config = HardwareConfiguration()
        parser.readHardwareConfiguration(ET.fromstring(HARDWARE_CONFIGURATION_XML), config)
        assert config.getAdditionalInformation().getValue() == "ECU configuration info"
        assert config.getProcessorMode().getValue() == "NORMAL"
        assert config.getProcessorSpeed().getValue() == "600 MHz"

    def test_read_absent_children(self, parser):
        config = HardwareConfiguration()
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")
        parser.readHardwareConfiguration(element, config)
        assert config.getAdditionalInformation() is None
        assert config.getProcessorMode() is None
        assert config.getProcessorSpeed() is None

    def test_read_partial_children(self, parser):
        config = HardwareConfiguration()
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><PROCESSOR-MODE>FAST</PROCESSOR-MODE></ROOT>")
        parser.readHardwareConfiguration(element, config)
        assert config.getProcessorMode().getValue() == "FAST"
        assert config.getAdditionalInformation() is None
        assert config.getProcessorSpeed() is None
