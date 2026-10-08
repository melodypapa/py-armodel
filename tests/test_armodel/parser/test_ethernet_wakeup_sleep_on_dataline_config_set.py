"""
Reader tests for EthernetWakeupSleepOnDatalineConfigSet (CP_TPS_SystemTemplate Table 3.116, p.159, R23-11).

Covers the IDENTIFIABLE base level (SHORT-NAME/UUID round-trip), the single optional
ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIGS wrapper (unbounded ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG
children per AUTOSAR_00052.xsd group ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG-SET), the
absent-wrapper case and the ARPackage ELEMENTS dispatch (aggregated by ARPackage.element).

Round-trip counterpart: tests/test_armodel/writer/test_ethernet_wakeup_sleep_on_dataline_config_set.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR as AutosarDocument
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetWakeupSleepOnDatalineConfig,
    EthernetWakeupSleepOnDatalineConfigSet,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _config_inner(short_name: str, local_enabled: str, repetitions: str) -> str:
    return (
        f"<ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG>"
        f"<SHORT-NAME>{short_name}</SHORT-NAME>"
        f"<WAKEUP-LOCAL-ENABLED>{local_enabled}</WAKEUP-LOCAL-ENABLED>"
        f"<WAKEUP-REPETITIONS-OF-WAKEUP-REQUEST>{repetitions}</WAKEUP-REPETITIONS-OF-WAKEUP-REQUEST>"
        f"</ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG>"
    )


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG-SET xmlns='{NS}'>{inner}</ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG-SET>")


def _full_inner() -> str:
    return (
        "<SHORT-NAME>WSD_CFG_SET</SHORT-NAME>"
        "<ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIGS>" + _config_inner("WSD_CFG_A", "true", "4") + _config_inner("WSD_CFG_B", "false", "3") + "</ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIGS>"
    )


class TestReadEthernetWakeupSleepOnDatalineConfigSet:
    def test_read_identifiable_base_level(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring(
            f"<ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG-SET xmlns='{NS}' UUID='5d3d3d0d-3c1f-4a2b-9d1a-65ab0bd89ab1'>"
            "<SHORT-NAME>WSD_CFG_SET</SHORT-NAME>"
            "</ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG-SET>"
        )
        config_set = EthernetWakeupSleepOnDatalineConfigSet(AutosarDocument.getInstance(), "Initial")
        parser.readEthernetWakeupSleepOnDatalineConfigSet(element, config_set)

        assert config_set.getUuid().getValue() == "5d3d3d0d-3c1f-4a2b-9d1a-65ab0bd89ab1"
        assert config_set.getEthernetWakeupSleepOnDatalineConfigs() == []

    def test_read_full_set_with_two_configs(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        config_set = EthernetWakeupSleepOnDatalineConfigSet(AutosarDocument.getInstance(), "Initial")
        parser.readEthernetWakeupSleepOnDatalineConfigSet(element, config_set)

        configs = config_set.getEthernetWakeupSleepOnDatalineConfigs()
        assert len(configs) == 2
        assert isinstance(configs[0], EthernetWakeupSleepOnDatalineConfig)
        assert configs[0].getShortName() == "WSD_CFG_A"
        assert configs[0].getWakeupLocalEnabled().getValue() is True
        assert configs[0].getWakeupRepetitionsOfWakeupRequest().getValue() == 4
        assert configs[1].getShortName() == "WSD_CFG_B"
        assert configs[1].getWakeupLocalEnabled().getValue() is False
        assert configs[1].getWakeupRepetitionsOfWakeupRequest().getValue() == 3

    def test_read_partial_config_children(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>WSD_CFG_SET</SHORT-NAME>"
            "<ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIGS>"
            "<ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG><SHORT-NAME>WSD_CFG_A</SHORT-NAME></ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG>"
            "</ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIGS>"
        )
        config_set = EthernetWakeupSleepOnDatalineConfigSet(AutosarDocument.getInstance(), "Initial")
        parser.readEthernetWakeupSleepOnDatalineConfigSet(element, config_set)

        configs = config_set.getEthernetWakeupSleepOnDatalineConfigs()
        assert len(configs) == 1
        assert configs[0].getShortName() == "WSD_CFG_A"
        assert configs[0].getWakeupLocalEnabled() is None
        assert configs[0].getWakeupRepetitionsOfWakeupRequest() is None

    def test_read_empty_set(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>WSD_CFG_SET</SHORT-NAME>")
        config_set = EthernetWakeupSleepOnDatalineConfigSet(AutosarDocument.getInstance(), "Initial")
        parser.readEthernetWakeupSleepOnDatalineConfigSet(element, config_set)

        assert config_set.getEthernetWakeupSleepOnDatalineConfigs() == []

    def test_load_via_ar_package(self):
        """The ARPackage ELEMENTS dispatch reads an ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG-SET."""
        content = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>AUTOSAR</SHORT-NAME>
            <ELEMENTS>
                <ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG-SET>
                    <SHORT-NAME>WsdCfgSet</SHORT-NAME>
                    <ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIGS>
                        <ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG>
                            <SHORT-NAME>WsdCfg</SHORT-NAME>
                            <SLEEP-REPETITIONS-OF-SLEEP-REQUEST>2</SLEEP-REPETITIONS-OF-SLEEP-REQUEST>
                            <WAKEUP-LOCAL-ENABLED>true</WAKEUP-LOCAL-ENABLED>
                        </ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG>
                    </ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIGS>
                </ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG-SET>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            document = AUTOSAR.getInstance()
            document.clear()
            parser = ARXMLParser(options={"warning": True})
            parser.load(file_path, document)

            pkg = document.getARPackages()[0]
            config_sets = [e for e in pkg.getReferrableElements() if isinstance(e, EthernetWakeupSleepOnDatalineConfigSet)]
            assert len(config_sets) == 1
            config_set = config_sets[0]
            assert config_set.getShortName() == "WsdCfgSet"
            configs = config_set.getEthernetWakeupSleepOnDatalineConfigs()
            assert len(configs) == 1
            assert configs[0].getShortName() == "WsdCfg"
            assert configs[0].getWakeupLocalEnabled().getValue() is True
            assert configs[0].getSleepRepetitionsOfSleepRequest().getValue() == 2
            assert configs[0].getWakeupRemoteEnabled() is None
        finally:
            os.remove(file_path)
