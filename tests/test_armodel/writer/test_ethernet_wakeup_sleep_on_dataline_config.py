"""
Writer tests for EthernetWakeupSleepOnDatalineConfig (CP_TPS_SystemTemplate Table 3.115, p.159, R23-11).

Checks the IDENTIFIABLE base level (SHORT-NAME emission), the child element values and the
XSD sequence order (SLEEP-MODE-EXECUTION-DELAY .. WAKEUP-REPETITIONS-OF-WAKEUP-REQUEST per
group ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG — dispatched by the aggregating
EthernetWakeupSleepOnDatalineConfigSet once that class syncs), the partial-emission case
and the write→parse round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_ethernet_wakeup_sleep_on_dataline_config.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetWakeupSleepOnDatalineConfig
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _count(value):
    count = PositiveInteger()
    count.setValue(value)
    return count


def _flag(value):
    flag = Boolean()
    flag.setValue(value)
    return flag


def _full_config() -> EthernetWakeupSleepOnDatalineConfig:
    config = EthernetWakeupSleepOnDatalineConfig(MockParent(), "WSD_CFG")
    config.setSleepModeExecutionDelay(_time("0.05"))
    config.setSleepRepetitionDelayOfSleepRequest(_time("1.0"))
    config.setSleepRepetitionsOfSleepRequest(_count("4"))
    config.setWakeupForwardLocalEnabled(_flag("true"))
    config.setWakeupForwardRemoteEnabled(_flag("true"))
    config.setWakeupLocalDetectionTime(_time("0.5"))
    config.setWakeupLocalDurationTime(_time("2.0"))
    config.setWakeupLocalEnabled(_flag("true"))
    config.setWakeupRemoteEnabled(_flag("true"))
    config.setWakeupRepetitionDelayOfWakeupRequest(_time("0.2"))
    config.setWakeupRepetitionsOfWakeupRequest(_count("3"))
    return config


def _write(config):
    element = ET.Element("ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG")
    ARXMLWriter().writeEthernetWakeupSleepOnDatalineConfig(element, config)
    return element


class TestWriteEthernetWakeupSleepOnDatalineConfig:
    def test_write_identifiable_base_level(self):
        element = _write(EthernetWakeupSleepOnDatalineConfig(MockParent(), "WSD_CFG"))

        assert element.find("SHORT-NAME").text == "WSD_CFG"

    def test_write_all_children_in_xsd_order(self):
        element = _write(_full_config())

        assert [child.tag for child in element] == [
            "SHORT-NAME",
            "SLEEP-MODE-EXECUTION-DELAY",
            "SLEEP-REPETITION-DELAY-OF-SLEEP-REQUEST",
            "SLEEP-REPETITIONS-OF-SLEEP-REQUEST",
            "WAKEUP-FORWARD-LOCAL-ENABLED",
            "WAKEUP-FORWARD-REMOTE-ENABLED",
            "WAKEUP-LOCAL-DETECTION-TIME",
            "WAKEUP-LOCAL-DURATION-TIME",
            "WAKEUP-LOCAL-ENABLED",
            "WAKEUP-REMOTE-ENABLED",
            "WAKEUP-REPETITION-DELAY-OF-WAKEUP-REQUEST",
            "WAKEUP-REPETITIONS-OF-WAKEUP-REQUEST",
        ]
        assert element.find("SLEEP-MODE-EXECUTION-DELAY").text == "0.05"
        assert element.find("SLEEP-REPETITION-DELAY-OF-SLEEP-REQUEST").text == "1.0"
        assert element.find("SLEEP-REPETITIONS-OF-SLEEP-REQUEST").text == "4"
        assert element.find("WAKEUP-FORWARD-LOCAL-ENABLED").text == "true"
        assert element.find("WAKEUP-FORWARD-REMOTE-ENABLED").text == "true"
        assert element.find("WAKEUP-LOCAL-DETECTION-TIME").text == "0.5"
        assert element.find("WAKEUP-LOCAL-DURATION-TIME").text == "2.0"
        assert element.find("WAKEUP-LOCAL-ENABLED").text == "true"
        assert element.find("WAKEUP-REMOTE-ENABLED").text == "true"
        assert element.find("WAKEUP-REPETITION-DELAY-OF-WAKEUP-REQUEST").text == "0.2"
        assert element.find("WAKEUP-REPETITIONS-OF-WAKEUP-REQUEST").text == "3"

    def test_write_partial_emission(self):
        config = EthernetWakeupSleepOnDatalineConfig(MockParent(), "WSD_CFG")
        config.setWakeupLocalEnabled(_flag("false"))
        config.setWakeupRepetitionsOfWakeupRequest(_count("3"))

        element = _write(config)

        assert [child.tag for child in element] == ["SHORT-NAME", "WAKEUP-LOCAL-ENABLED", "WAKEUP-REPETITIONS-OF-WAKEUP-REQUEST"]
        assert element.find("WAKEUP-LOCAL-ENABLED").text == "false"
        assert element.find("WAKEUP-REPETITIONS-OF-WAKEUP-REQUEST").text == "3"

    def test_write_empty_emits_no_config_children(self):
        element = _write(EthernetWakeupSleepOnDatalineConfig(MockParent(), "WSD_CFG"))

        assert [child.tag for child in element] == ["SHORT-NAME"]

    def test_write_and_reparse_round_trip(self):
        element = _write(_full_config())

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))

        recovered = EthernetWakeupSleepOnDatalineConfig(MockParent(), "Initial")
        ARXMLParser(options={"warning": True}).readEthernetWakeupSleepOnDatalineConfig(namespaced, recovered)

        assert element.find("SHORT-NAME").text == "WSD_CFG"
        assert recovered.getSleepModeExecutionDelay().getValue() == 0.05
        assert recovered.getSleepRepetitionDelayOfSleepRequest().getValue() == 1.0
        assert recovered.getSleepRepetitionsOfSleepRequest().getValue() == 4
        assert recovered.getWakeupForwardLocalEnabled().getValue() is True
        assert recovered.getWakeupForwardRemoteEnabled().getValue() is True
        assert recovered.getWakeupLocalDetectionTime().getValue() == 0.5
        assert recovered.getWakeupLocalDurationTime().getValue() == 2.0
        assert recovered.getWakeupLocalEnabled().getValue() is True
        assert recovered.getWakeupRemoteEnabled().getValue() is True
        assert recovered.getWakeupRepetitionDelayOfWakeupRequest().getValue() == 0.2
        assert recovered.getWakeupRepetitionsOfWakeupRequest().getValue() == 3
