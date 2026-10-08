"""
Writer/reader round-trip tests for EthernetWakeupSleepOnDatalineConfigSet (CP_TPS_SystemTemplate Table 3.116, p.159, R23-11).

XML element order per XSD group ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG-SET: the single optional
ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIGS wrapper (emitted only when non-empty) holding unbounded
ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG children. writeEthernetWakeupSleepOnDatalineConfigSet calls
writeIdentifiable on the ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG-SET element exactly once and
dispatches each child through writeEthernetWakeupSleepOnDatalineConfig. Also covers the ARPackage
ELEMENTS emission (aggregated by ARPackage.element) via a save→load round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_ethernet_wakeup_sleep_on_dataline_config_set.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetWakeupSleepOnDatalineConfigSet
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _flag(value):
    flag = Boolean()
    flag.setValue(value)
    return flag


def _count(value):
    count = PositiveInteger()
    count.setValue(value)
    return count


def _full_set() -> EthernetWakeupSleepOnDatalineConfigSet:
    AUTOSAR.getInstance().setARRelease("R23-11")
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    config_set = pkg.createEthernetWakeupSleepOnDatalineConfigSet("WSD_CFG_SET")
    config_a = config_set.createEthernetWakeupSleepOnDatalineConfig("WSD_CFG_A")
    config_a.setWakeupLocalEnabled(_flag("true"))
    config_a.setWakeupRepetitionsOfWakeupRequest(_count("4"))
    config_b = config_set.createEthernetWakeupSleepOnDatalineConfig("WSD_CFG_B")
    config_b.setWakeupLocalEnabled(_flag("false"))
    config_b.setWakeupRepetitionsOfWakeupRequest(_count("3"))
    return config_set


def _write_config_set(config_set):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeEthernetWakeupSleepOnDatalineConfigSet(parent, config_set)
    return parent


def _namespaced_config_set(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteEthernetWakeupSleepOnDatalineConfigSet:
    def test_entry_point_emits_short_name_and_wrapper_in_xsd_order(self):
        parent = _write_config_set(_full_set())
        config_set_element = parent.find("ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG-SET")

        assert config_set_element.find("SHORT-NAME").text == "WSD_CFG_SET"
        assert [child.tag for child in config_set_element] == [
            "SHORT-NAME",
            "ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIGS",
        ]
        configs = config_set_element.findall("ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIGS/ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG")
        assert len(configs) == 2
        assert configs[0].find("SHORT-NAME").text == "WSD_CFG_A"
        assert configs[1].find("SHORT-NAME").text == "WSD_CFG_B"

    def test_entry_point_writes_child_field_values(self):
        parent = _write_config_set(_full_set())
        config_set_element = parent.find("ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG-SET")

        configs = config_set_element.findall("ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIGS/ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG")
        assert configs[0].find("WAKEUP-LOCAL-ENABLED").text == "true"
        assert configs[0].find("WAKEUP-REPETITIONS-OF-WAKEUP-REQUEST").text == "4"
        assert configs[1].find("WAKEUP-LOCAL-ENABLED").text == "false"
        assert configs[1].find("WAKEUP-REPETITIONS-OF-WAKEUP-REQUEST").text == "3"

    def test_bare_set_emits_no_wrapper(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        config_set = pkg.createEthernetWakeupSleepOnDatalineConfigSet("WSD_CFG_SET")

        parent = _write_config_set(config_set)
        config_set_element = parent.find("ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG-SET")

        assert [child.tag for child in config_set_element] == ["SHORT-NAME"]
        assert config_set_element.find("ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIGS") is None


class TestEthernetWakeupSleepOnDatalineConfigSetRoundTrip:
    def test_round_trip_full_through_config_set(self):
        parent = _write_config_set(_full_set())
        reloaded = EthernetWakeupSleepOnDatalineConfigSet(AUTOSAR.getInstance(), "Initial")
        ARXMLParser(options={"warning": True}).readEthernetWakeupSleepOnDatalineConfigSet(_namespaced_config_set(parent), reloaded)

        assert reloaded.getUuid() is None
        configs = reloaded.getEthernetWakeupSleepOnDatalineConfigs()
        assert len(configs) == 2
        assert configs[0].getShortName() == "WSD_CFG_A"
        assert configs[0].getWakeupLocalEnabled().getValue() is True
        assert configs[0].getWakeupRepetitionsOfWakeupRequest().getValue() == 4
        assert configs[1].getShortName() == "WSD_CFG_B"
        assert configs[1].getWakeupLocalEnabled().getValue() is False
        assert configs[1].getWakeupRepetitionsOfWakeupRequest().getValue() == 3
        assert configs[0].getWakeupRemoteEnabled() is None

    def test_round_trip_through_ar_package_save_load(self):
        """The full ARPackage ELEMENTS path: writeARPackageElement emits the SET and the parser dispatch reads it back."""
        source = _full_set()
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, AUTOSAR.getInstance())

            document = AUTOSAR.getInstance()
            document.clear()
            ARXMLParser(options={"warning": True}).load(file_path, document)

            pkg = document.getARPackages()[0]
            config_sets = [e for e in pkg.getReferrableElements() if isinstance(e, EthernetWakeupSleepOnDatalineConfigSet)]
            assert len(config_sets) == 1
            config_set = config_sets[0]
            assert config_set.getShortName() == source.getShortName()
            configs = config_set.getEthernetWakeupSleepOnDatalineConfigs()
            assert len(configs) == 2
            assert configs[0].getShortName() == "WSD_CFG_A"
            assert configs[0].getWakeupLocalEnabled().getValue() is True
            assert configs[0].getWakeupRepetitionsOfWakeupRequest().getValue() == 4
            assert configs[1].getShortName() == "WSD_CFG_B"
            assert configs[1].getWakeupLocalEnabled().getValue() is False
            assert configs[1].getWakeupRepetitionsOfWakeupRequest().getValue() == 3
        finally:
            os.remove(file_path)
