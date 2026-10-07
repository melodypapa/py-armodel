"""Writer tests for the StackUsage family (writeStackUsage dispatch) and the write→parse round-trip."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import (
    HardwareConfiguration,
    ResourceConsumption,
    SoftwareContext,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    PositiveInteger,
    RefType,
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
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


def _make_ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _make_positive_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _make_vp(label):
    vp = VariationPoint()
    vp.setShortLabel(Identifier().setValue(label))
    return vp


def _fill_measured(usage):
    usage.setExecutableEntityRef(_make_ref("EXECUTABLE-ENTITY", "/Pkg/EE"))
    config = HardwareConfiguration()
    config.setAdditionalInformation(String().setValue("ECU configuration info"))
    config.setProcessorMode(String().setValue("NORMAL"))
    config.setProcessorSpeed(String().setValue("600 MHz"))
    usage.setHardwareConfiguration(config)
    usage.setHwElementRef(_make_ref("HW-ELEMENT", "/Pkg/Hw"))
    context = SoftwareContext()
    context.setInput(String().setValue("in1"))
    context.setState(String().setValue("RUN"))
    usage.setSoftwareContext(context)
    usage.setVariationPoint(_make_vp("VP1"))
    usage.setAverageMemoryConsumption(_make_positive_int("100"))
    usage.setMaximumMemoryConsumption(_make_positive_int("200"))
    usage.setMinimumMemoryConsumption(_make_positive_int("50"))
    usage.setTestPattern(String().setValue("patternA"))
    return usage


def _full_measured():
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import MeasuredStackUsage

    return _fill_measured(MeasuredStackUsage(AUTOSAR.getInstance().createARPackage("Pkg"), "MSU"))


def _consumption_with_all_three():
    consumption = ResourceConsumption(AUTOSAR.getInstance().createARPackage("Pkg"), "RC")
    _fill_measured(consumption.createMeasuredStackUsage("MSU"))
    rough = consumption.createRoughEstimateStackUsage("RSU")
    rough.setMemoryConsumption(_make_positive_int("300"))
    worst = consumption.createWorstCaseStackUsage("WSU")
    worst.setMemoryConsumption(_make_positive_int("400"))
    worst.setExecutableEntityRef(_make_ref("EXECUTABLE-ENTITY", "/Pkg/EE2"))
    return consumption


def _qualify_namespaces(element):
    """Qualify every plain tag with the AUTOSAR namespace so the namespace-aware parser can read it back."""
    for el in element.iter():
        if not el.tag.startswith("{"):
            el.tag = "{%s}%s" % (NS, el.tag)
    return element


class TestWriteStackUsages:
    def test_write_field_values(self, writer):
        consumption = _consumption_with_all_three()
        parent = ET.Element("PARENT")
        writer.writeStackUsages(parent, consumption.getStackUsages())
        assert len(parent) == 1
        wrapper = parent[0]
        assert wrapper.tag == "STACK-USAGES"
        assert [child.tag for child in wrapper] == ["MEASURED-STACK-USAGE", "ROUGH-ESTIMATE-STACK-USAGE", "WORST-CASE-STACK-USAGE"]
        measured = wrapper[0]
        assert measured.find("SHORT-NAME").text == "MSU"
        assert measured.find("EXECUTABLE-ENTITY-REF").get("DEST") == "EXECUTABLE-ENTITY"
        assert measured.find("EXECUTABLE-ENTITY-REF").text == "/Pkg/EE"
        assert measured.find("HARDWARE-CONFIGURATION/PROCESSOR-MODE").text == "NORMAL"
        assert measured.find("HW-ELEMENT-REF").text == "/Pkg/Hw"
        assert measured.find("SOFTWARE-CONTEXT/STATE").text == "RUN"
        assert measured.find("AVERAGE-MEMORY-CONSUMPTION").text == "100"
        assert measured.find("MAXIMUM-MEMORY-CONSUMPTION").text == "200"
        assert measured.find("MINIMUM-MEMORY-CONSUMPTION").text == "50"
        assert measured.find("TEST-PATTERN").text == "patternA"
        assert wrapper[1].find("SHORT-NAME").text == "RSU"
        assert wrapper[1].find("MEMORY-CONSUMPTION").text == "300"
        assert wrapper[2].find("SHORT-NAME").text == "WSU"
        assert wrapper[2].find("MEMORY-CONSUMPTION").text == "400"

    def test_write_xsd_element_order(self, writer):
        """Children follow the XSD sequence of complexType MEASURED-STACK-USAGE (AUTOSAR_00052.xsd L80881):
        IDENTIFIABLE group, STACK-USAGE group (VARIATION-POINT last, seqOffset 10000), subclass group."""
        parent = ET.Element("PARENT")
        writer.writeMeasuredStackUsage(parent, _full_measured())
        usage = parent[0]
        assert [c.tag for c in usage] == [
            "SHORT-NAME",
            "EXECUTABLE-ENTITY-REF",
            "HARDWARE-CONFIGURATION",
            "HW-ELEMENT-REF",
            "SOFTWARE-CONTEXT",
            "VARIATION-POINT",
            "AVERAGE-MEMORY-CONSUMPTION",
            "MAXIMUM-MEMORY-CONSUMPTION",
            "MINIMUM-MEMORY-CONSUMPTION",
            "TEST-PATTERN",
        ]

    def test_write_variation_point(self, writer):
        parent = ET.Element("PARENT")
        writer.writeMeasuredStackUsage(parent, _full_measured())
        vp = parent[0].find("VARIATION-POINT")
        assert vp is not None
        assert vp.find("SHORT-LABEL").text == "VP1"

    def test_write_empty_usage_omits_optionals(self, writer):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import WorstCaseStackUsage

        usage = WorstCaseStackUsage(AUTOSAR.getInstance().createARPackage("Pkg"), "WSU")
        parent = ET.Element("PARENT")
        writer.writeWorstCaseStackUsage(parent, usage)
        assert [c.tag for c in parent[0]] == ["SHORT-NAME"]

    def test_write_empty_list(self, writer):
        parent = ET.Element("PARENT")
        writer.writeStackUsages(parent, [])
        assert len(parent) == 0

    def test_round_trip(self, writer):
        consumption = _consumption_with_all_three()
        parent = ET.Element("PARENT")
        writer.writeStackUsages(parent, consumption.getStackUsages())
        parsed_root = ET.fromstring(ET.tostring(_qualify_namespaces(parent)))
        consumption_2 = ResourceConsumption(AUTOSAR.getInstance().createARPackage("Pkg"), "RC2")
        ARXMLParser().readStackUsages(parsed_root, consumption_2)
        usages = consumption_2.getStackUsages()
        assert [type(usage) for usage in usages] == [type(usage) for usage in consumption.getStackUsages()]
        measured = usages[0]
        assert measured.getShortName() == "MSU"
        assert measured.getExecutableEntityRef().getValue() == "/Pkg/EE"
        assert measured.getExecutableEntityRef().getDest() == "EXECUTABLE-ENTITY"
        assert measured.getHardwareConfiguration().getProcessorSpeed().getValue() == "600 MHz"
        assert measured.getHwElementRef().getValue() == "/Pkg/Hw"
        assert measured.getSoftwareContext().getState().getValue() == "RUN"
        assert measured.getVariationPoint().getShortLabel().getValue() == "VP1"
        assert measured.getAverageMemoryConsumption().getValue() == 100
        assert measured.getMaximumMemoryConsumption().getValue() == 200
        assert measured.getMinimumMemoryConsumption().getValue() == 50
        assert measured.getTestPattern().getValue() == "patternA"
        assert usages[1].getMemoryConsumption().getValue() == 300
        assert usages[2].getMemoryConsumption().getValue() == 400
        assert usages[2].getExecutableEntityRef().getValue() == "/Pkg/EE2"
