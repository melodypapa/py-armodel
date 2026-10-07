"""
Reader tests for EthernetWakeupSleepOnDatalineConfig (CP_TPS_SystemTemplate Table 3.115, p.159, R23-11).

Covers the IDENTIFIABLE base level (SHORT-NAME round-trip) and the 11 optional
SLEEP-*/WAKEUP-* children of the ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG element shape
(AUTOSAR_00052.xsd group ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG — dispatched by the
aggregating EthernetWakeupSleepOnDatalineConfigSet once that class syncs), the absent-element
case and the empty-element case.

Round-trip counterpart: tests/test_armodel/writer/test_ethernet_wakeup_sleep_on_dataline_config.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetWakeupSleepOnDatalineConfig
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG xmlns='{NS}'>{inner}</ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG>")


def _snip_with_attrs(attrs: str, inner: str) -> ET.Element:
    return ET.fromstring(f"<ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG xmlns='{NS}' {attrs}>{inner}</ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG>")


def _full_inner() -> str:
    return (
        "<SHORT-NAME>WSD_CFG</SHORT-NAME>"
        "<SLEEP-MODE-EXECUTION-DELAY>0.05</SLEEP-MODE-EXECUTION-DELAY>"
        "<SLEEP-REPETITION-DELAY-OF-SLEEP-REQUEST>1.0</SLEEP-REPETITION-DELAY-OF-SLEEP-REQUEST>"
        "<SLEEP-REPETITIONS-OF-SLEEP-REQUEST>4</SLEEP-REPETITIONS-OF-SLEEP-REQUEST>"
        "<WAKEUP-FORWARD-LOCAL-ENABLED>true</WAKEUP-FORWARD-LOCAL-ENABLED>"
        "<WAKEUP-FORWARD-REMOTE-ENABLED>true</WAKEUP-FORWARD-REMOTE-ENABLED>"
        "<WAKEUP-LOCAL-DETECTION-TIME>0.5</WAKEUP-LOCAL-DETECTION-TIME>"
        "<WAKEUP-LOCAL-DURATION-TIME>2.0</WAKEUP-LOCAL-DURATION-TIME>"
        "<WAKEUP-LOCAL-ENABLED>true</WAKEUP-LOCAL-ENABLED>"
        "<WAKEUP-REMOTE-ENABLED>true</WAKEUP-REMOTE-ENABLED>"
        "<WAKEUP-REPETITION-DELAY-OF-WAKEUP-REQUEST>0.2</WAKEUP-REPETITION-DELAY-OF-WAKEUP-REQUEST>"
        "<WAKEUP-REPETITIONS-OF-WAKEUP-REQUEST>3</WAKEUP-REPETITIONS-OF-WAKEUP-REQUEST>"
    )


class TestReadEthernetWakeupSleepOnDatalineConfig:
    def test_read_identifiable_base_level(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip_with_attrs("UUID='5d3d3d0d-3c1f-4a2b-9d1a-65ab0bd89ab1'", "")
        config = EthernetWakeupSleepOnDatalineConfig(MockParent(), "Initial")
        parser.readEthernetWakeupSleepOnDatalineConfig(element, config)

        assert config.getUuid().getValue() == "5d3d3d0d-3c1f-4a2b-9d1a-65ab0bd89ab1"
        assert config.getSleepModeExecutionDelay() is None
        assert config.getWakeupRepetitionsOfWakeupRequest() is None

    def test_read_all_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        config = EthernetWakeupSleepOnDatalineConfig(MockParent(), "Initial")
        parser.readEthernetWakeupSleepOnDatalineConfig(element, config)

        assert config.getSleepModeExecutionDelay().getValue() == 0.05
        assert config.getSleepRepetitionDelayOfSleepRequest().getValue() == 1.0
        assert config.getSleepRepetitionsOfSleepRequest().getValue() == 4
        assert config.getWakeupForwardLocalEnabled().getValue() is True
        assert config.getWakeupForwardRemoteEnabled().getValue() is True
        assert config.getWakeupLocalDetectionTime().getValue() == 0.5
        assert config.getWakeupLocalDurationTime().getValue() == 2.0
        assert config.getWakeupLocalEnabled().getValue() is True
        assert config.getWakeupRemoteEnabled().getValue() is True
        assert config.getWakeupRepetitionDelayOfWakeupRequest().getValue() == 0.2
        assert config.getWakeupRepetitionsOfWakeupRequest().getValue() == 3

    def test_read_partial_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>WSD_CFG</SHORT-NAME><WAKEUP-LOCAL-ENABLED>false</WAKEUP-LOCAL-ENABLED><WAKEUP-REMOTE-ENABLED>true</WAKEUP-REMOTE-ENABLED>")
        config = EthernetWakeupSleepOnDatalineConfig(MockParent(), "Initial")
        parser.readEthernetWakeupSleepOnDatalineConfig(element, config)

        assert config.getWakeupLocalEnabled().getValue() is False
        assert config.getWakeupRemoteEnabled().getValue() is True
        assert config.getSleepModeExecutionDelay() is None
        assert config.getWakeupLocalDetectionTime() is None

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("")
        config = EthernetWakeupSleepOnDatalineConfig(MockParent(), "Initial")
        parser.readEthernetWakeupSleepOnDatalineConfig(element, config)

        assert config.getSleepModeExecutionDelay() is None
        assert config.getSleepRepetitionDelayOfSleepRequest() is None
        assert config.getSleepRepetitionsOfSleepRequest() is None
        assert config.getWakeupForwardLocalEnabled() is None
        assert config.getWakeupForwardRemoteEnabled() is None
        assert config.getWakeupLocalDetectionTime() is None
        assert config.getWakeupLocalDurationTime() is None
        assert config.getWakeupLocalEnabled() is None
        assert config.getWakeupRemoteEnabled() is None
        assert config.getWakeupRepetitionDelayOfWakeupRequest() is None
        assert config.getWakeupRepetitionsOfWakeupRequest() is None
