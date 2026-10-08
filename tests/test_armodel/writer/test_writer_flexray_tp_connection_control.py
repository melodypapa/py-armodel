"""Tests for the writeFlexrayTpConnectionControl handler (R23-11 FlexrayTpConnectionControl, Table 6.240, p.593)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayTpConfig, FlexrayTpConnectionControl, TpAckType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "ACK-TYPE",
    "MAX-FC-WAIT",
    "MAX-NUMBER-OF-NPDU-PER-CYCLE",
    "MAX-RETRIES",
    "SEPARATION-CYCLE-EXPONENT",
    "TIME-BR",
    "TIME-BUFFER",
    "TIME-CS",
    "TIMEOUT-AR",
    "TIMEOUT-AS",
    "TIMEOUT-BS",
    "TIMEOUT-CR",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _integer(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _fill_control(control: FlexrayTpConnectionControl) -> FlexrayTpConnectionControl:
    control.setAckType(TpAckType().setValue(TpAckType.ENUM_ACK_WITH_RT))
    control.setMaxFcWait(_integer(5))
    control.setMaxNumberOfNpduPerCycle(_integer(2))
    control.setMaxRetries(_integer(3))
    control.setSeparationCycleExponent(_integer(1))
    control.setTimeBr(_time(0.01))
    control.setTimeBuffer(_time(0.02))
    control.setTimeCs(_time(0.03))
    control.setTimeoutAr(_time(0.04))
    control.setTimeoutAs(_time(0.05))
    control.setTimeoutBs(_time(0.06))
    control.setTimeoutCr(_time(0.07))
    return control


class TestWriteFlexrayTpConnectionControl:
    """Tests for writeFlexrayTpConnectionControl (R23-11 FlexrayTpConnectionControl, Table 6.240, p.593)."""

    def test_children_in_xsd_order(self, writer):
        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = _fill_control(FlexrayTpConnectionControl(package, "Control1"))
        parent = _parent()
        writer.writeFlexrayTpConnectionControl(parent, control)
        child = parent.find("FLEXRAY-TP-CONNECTION-CONTROL")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == XSD_CHILD_ORDER
        assert child.find("ACK-TYPE").text == "ACK-WITH-RT"
        assert child.find("MAX-FC-WAIT").text == "5"
        assert child.find("TIMEOUT-CR").text == "0.07"

    def test_empty_control_writes_no_attributes(self, writer):
        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        parent = _parent()
        writer.writeFlexrayTpConnectionControl(parent, control)
        child = parent.find("FLEXRAY-TP-CONNECTION-CONTROL")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == []

    def test_round_trip_via_config(self, writer, parser):
        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        config = FlexrayTpConfig(package, "Config1")
        control = _fill_control(config.createFlexrayTpConnectionControl("Control1"))
        assert control is not None

        parent = ET.Element("PARENT")
        writer.writeFlexrayTpConfig(parent, config)
        xml_text = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        assert "TP-CONNECTION-CONTROLS" in xml_text
        assert "ACK-WITH-RT" in xml_text

        reparsed = ET.fromstring(xml_text)[0]
        config2 = FlexrayTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "Config1")
        parser.readFlexrayTpConfig(reparsed, config2)
        controls = config2.getTpConnectionControls()
        assert len(controls) == 1
        loaded = controls[0]
        assert loaded.getShortName() == "Control1"
        assert loaded.getAckType() is not None
        assert loaded.getAckType().getValue() == TpAckType.ENUM_ACK_WITH_RT
        assert loaded.getMaxFcWait().getValue() == 5
        assert loaded.getMaxNumberOfNpduPerCycle().getValue() == 2
        assert loaded.getMaxRetries().getValue() == 3
        assert loaded.getSeparationCycleExponent().getValue() == 1
        assert loaded.getTimeBr().getValue() == 0.01
        assert loaded.getTimeBuffer().getValue() == 0.02
        assert loaded.getTimeCs().getValue() == 0.03
        assert loaded.getTimeoutAr().getValue() == 0.04
        assert loaded.getTimeoutAs().getValue() == 0.05
        assert loaded.getTimeoutBs().getValue() == 0.06
        assert loaded.getTimeoutCr().getValue() == 0.07
