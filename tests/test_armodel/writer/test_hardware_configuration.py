"""Writer tests for HardwareConfiguration (setHardwareConfiguration) and the write→parse round-trip."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import HardwareConfiguration
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
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


def _full_config():
    config = HardwareConfiguration()
    config.setAdditionalInformation(String().setValue("ECU configuration info"))
    config.setProcessorMode(String().setValue("NORMAL"))
    config.setProcessorSpeed(String().setValue("600 MHz"))
    return config


def _qualify_namespaces(element):
    """Qualify every plain tag with the AUTOSAR namespace so the namespace-aware parser can read it back."""
    for el in element.iter():
        if not el.tag.startswith("{"):
            el.tag = "{%s}%s" % (NS, el.tag)
    return element


class TestWriteHardwareConfiguration:
    def test_write_field_values(self, writer):
        parent = ET.Element("PARENT")
        writer.setHardwareConfiguration(parent, _full_config())
        assert len(parent) == 1
        element = parent[0]
        assert element.tag == "HARDWARE-CONFIGURATION"
        assert element.find("ADDITIONAL-INFORMATION").text == "ECU configuration info"
        assert element.find("PROCESSOR-MODE").text == "NORMAL"
        assert element.find("PROCESSOR-SPEED").text == "600 MHz"

    def test_write_xsd_element_order(self, writer):
        """Children follow the XSD sequence of group HARDWARE-CONFIGURATION (AUTOSAR_00052.xsd L65234)."""
        parent = ET.Element("PARENT")
        writer.setHardwareConfiguration(parent, _full_config())
        tags = [child.tag for child in parent[0]]
        assert tags == ["ADDITIONAL-INFORMATION", "PROCESSOR-MODE", "PROCESSOR-SPEED"]

    def test_write_none_config(self, writer):
        parent = ET.Element("PARENT")
        writer.setHardwareConfiguration(parent, None)
        assert len(parent) == 0

    def test_round_trip(self, writer):
        parent = ET.Element("PARENT")
        writer.setHardwareConfiguration(parent, _full_config())
        parsed_parent = ET.fromstring(ET.tostring(_qualify_namespaces(parent), default_namespace=NS))
        config_2 = HardwareConfiguration()
        ARXMLParser().readHardwareConfiguration(parsed_parent[0], config_2)
        assert config_2.getAdditionalInformation().getValue() == "ECU configuration info"
        assert config_2.getProcessorMode().getValue() == "NORMAL"
        assert config_2.getProcessorSpeed().getValue() == "600 MHz"
