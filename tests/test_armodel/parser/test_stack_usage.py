"""Parser tests for the StackUsage family (readStackUsages polymorphic dispatch)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import ResourceConsumption
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import (
    MeasuredStackUsage,
    RoughEstimateStackUsage,
    WorstCaseStackUsage,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

STACK_USAGES_XML = (
    "<ROOT xmlns='{ns}'>"
    "<STACK-USAGES>"
    "<MEASURED-STACK-USAGE>"
    "<SHORT-NAME>MSU</SHORT-NAME>"
    "<EXECUTABLE-ENTITY-REF DEST='EXECUTABLE-ENTITY'>/Pkg/EE</EXECUTABLE-ENTITY-REF>"
    "<HARDWARE-CONFIGURATION>"
    "<ADDITIONAL-INFORMATION>ECU configuration info</ADDITIONAL-INFORMATION>"
    "<PROCESSOR-MODE>NORMAL</PROCESSOR-MODE>"
    "<PROCESSOR-SPEED>600 MHz</PROCESSOR-SPEED>"
    "</HARDWARE-CONFIGURATION>"
    "<HW-ELEMENT-REF DEST='HW-ELEMENT'>/Pkg/Hw</HW-ELEMENT-REF>"
    "<SOFTWARE-CONTEXT><INPUT>in1</INPUT><STATE>RUN</STATE></SOFTWARE-CONTEXT>"
    "<VARIATION-POINT><SHORT-LABEL>VP1</SHORT-LABEL></VARIATION-POINT>"
    "<AVERAGE-MEMORY-CONSUMPTION>100</AVERAGE-MEMORY-CONSUMPTION>"
    "<MAXIMUM-MEMORY-CONSUMPTION>200</MAXIMUM-MEMORY-CONSUMPTION>"
    "<MINIMUM-MEMORY-CONSUMPTION>50</MINIMUM-MEMORY-CONSUMPTION>"
    "<TEST-PATTERN>patternA</TEST-PATTERN>"
    "</MEASURED-STACK-USAGE>"
    "<ROUGH-ESTIMATE-STACK-USAGE>"
    "<SHORT-NAME>RSU</SHORT-NAME>"
    "<MEMORY-CONSUMPTION>300</MEMORY-CONSUMPTION>"
    "</ROUGH-ESTIMATE-STACK-USAGE>"
    "<WORST-CASE-STACK-USAGE>"
    "<SHORT-NAME>WSU</SHORT-NAME>"
    "<EXECUTABLE-ENTITY-REF DEST='EXECUTABLE-ENTITY'>/Pkg/EE2</EXECUTABLE-ENTITY-REF>"
    "<MEMORY-CONSUMPTION>400</MEMORY-CONSUMPTION>"
    "</WORST-CASE-STACK-USAGE>"
    "</STACK-USAGES>"
    "</ROOT>"
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


def _consumption():
    return ResourceConsumption(AUTOSAR.getInstance().createARPackage("Pkg"), "RC")


def _read_all(parser):
    consumption = _consumption()
    parser.readStackUsages(ET.fromstring(STACK_USAGES_XML), consumption)
    return consumption


class TestReadStackUsages:
    def test_read_polymorphic_dispatch(self, parser):
        consumption = _read_all(parser)
        usages = consumption.getStackUsages()
        assert [type(usage) for usage in usages] == [MeasuredStackUsage, RoughEstimateStackUsage, WorstCaseStackUsage]
        assert [usage.getShortName() for usage in usages] == ["MSU", "RSU", "WSU"]

    def test_read_measured_field_values(self, parser):
        consumption = _read_all(parser)
        measured = consumption.getStackUsages()[0]
        assert measured.getExecutableEntityRef().getValue() == "/Pkg/EE"
        assert measured.getExecutableEntityRef().getDest() == "EXECUTABLE-ENTITY"
        assert measured.getHardwareConfiguration().getAdditionalInformation().getValue() == "ECU configuration info"
        assert measured.getHardwareConfiguration().getProcessorMode().getValue() == "NORMAL"
        assert measured.getHardwareConfiguration().getProcessorSpeed().getValue() == "600 MHz"
        assert measured.getHwElementRef().getValue() == "/Pkg/Hw"
        assert measured.getHwElementRef().getDest() == "HW-ELEMENT"
        assert measured.getSoftwareContext().getInput().getValue() == "in1"
        assert measured.getSoftwareContext().getState().getValue() == "RUN"
        assert measured.getVariationPoint().getShortLabel().getValue() == "VP1"
        assert measured.getAverageMemoryConsumption().getValue() == 100
        assert measured.getMaximumMemoryConsumption().getValue() == 200
        assert measured.getMinimumMemoryConsumption().getValue() == 50
        assert measured.getTestPattern().getValue() == "patternA"

    def test_read_rough_and_worst_field_values(self, parser):
        consumption = _read_all(parser)
        rough = consumption.getStackUsages()[1]
        worst = consumption.getStackUsages()[2]
        assert rough.getMemoryConsumption().getValue() == 300
        assert rough.getExecutableEntityRef() is None
        assert worst.getMemoryConsumption().getValue() == 400
        assert worst.getExecutableEntityRef().getValue() == "/Pkg/EE2"
        assert worst.getHwElementRef() is None

    def test_read_empty_wrapper(self, parser):
        consumption = _consumption()
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><STACK-USAGES/></ROOT>")
        parser.readStackUsages(element, consumption)
        assert consumption.getStackUsages() == []

    def test_read_absent_wrapper(self, parser):
        consumption = _consumption()
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")
        parser.readStackUsages(element, consumption)
        assert consumption.getStackUsages() == []
