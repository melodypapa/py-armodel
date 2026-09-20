"""Tests for the writeDltConfig handler (R23-11 DltConfig, Table 6.335, p.722)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Dlt import DltConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

XSD_CHILD_ORDER = [
    "DLT-ECU-REF",
    "DLT-LOG-CHANNELS",
    "SESSION-ID-SUPPORT",
    "TIMESTAMP-SUPPORT",
]

NS = "http://autosar.org/schema/r4.0"


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


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _boolean(value: str) -> Boolean:
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _fill_config(config: DltConfig) -> DltConfig:
    config.setDltEcuRef(_ref("/LogAndTrace/DltEcus/Ecu1", "DLT-ECU"))
    channel = config.createDltLogChannel("Channel1")
    channel.setLogChannelId(_string("LOG1"))
    channel.setNonVerboseMode(_boolean("true"))
    config.setSessionIdSupport(_boolean("true"))
    config.setTimestampSupport(_boolean("false"))
    return config


def _string(value: str) -> String:
    text = String()
    text.setValue(value)
    return text


class TestWriteDltConfig:
    """Tests for writeDltConfig handler (R23-11 DltConfig, Table 6.335, p.722)."""

    def test_children_in_xsd_order(self, writer):
        parent = _parent()
        writer.writeDltConfig(parent, _fill_config(DltConfig()))
        child = parent.find("DLT-CONFIG")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER
        ecu_ref = child.find("DLT-ECU-REF")
        assert ecu_ref.text == "/LogAndTrace/DltEcus/Ecu1"
        assert ecu_ref.get("DEST") == "DLT-ECU"
        channels_element = child.find("DLT-LOG-CHANNELS")
        channel_tags = channels_element.findall("DLT-LOG-CHANNEL")
        assert len(channel_tags) == 1
        assert channel_tags[0].find("SHORT-NAME").text == "Channel1"
        assert channel_tags[0].find("LOG-CHANNEL-ID").text == "LOG1"
        assert channel_tags[0].find("NON-VERBOSE-MODE").text == "true"
        assert child.find("SESSION-ID-SUPPORT").text == "true"
        assert child.find("TIMESTAMP-SUPPORT").text == "false"

    def test_empty_children_omitted(self, writer):
        parent = _parent()
        writer.writeDltConfig(parent, DltConfig())
        child = parent.find("DLT-CONFIG")
        assert child is not None
        for tag in XSD_CHILD_ORDER:
            assert child.find(tag) is None

    def test_write_ecu_instance_dlt_config(self, writer):
        instance = EcuInstance(parent=AUTOSAR.getInstance(), short_name="ecu")
        instance.setDltConfig(_fill_config(DltConfig()))

        parent = _parent()
        writer.writeEcuInstance(parent, instance)
        ecu = parent.find("ECU-INSTANCE")
        assert ecu is not None
        config_element = ecu.find("DLT-CONFIG")
        assert config_element is not None
        child_tags = [element.tag for element in config_element]
        assert child_tags == XSD_CHILD_ORDER
        assert config_element.find("DLT-ECU-REF").text == "/LogAndTrace/DltEcus/Ecu1"
        channels = config_element.findall("DLT-LOG-CHANNELS/DLT-LOG-CHANNEL")
        assert len(channels) == 1
        assert channels[0].find("SHORT-NAME").text == "Channel1"
        assert config_element.find("SESSION-ID-SUPPORT").text == "true"
        assert config_element.find("TIMESTAMP-SUPPORT").text == "false"

    def test_write_ecu_instance_without_dlt_config_omits_element(self, writer):
        instance = EcuInstance(parent=AUTOSAR.getInstance(), short_name="ecu")
        parent = _parent()
        writer.writeEcuInstance(parent, instance)
        ecu = parent.find("ECU-INSTANCE")
        assert ecu.find("DLT-CONFIG") is None

    def test_round_trip_write_then_read(self, writer, parser):
        parent = _parent()
        writer.writeDltConfig(parent, _fill_config(DltConfig()))
        child = parent.find("DLT-CONFIG")
        fragment = ET.tostring(child, encoding="unicode")

        reloaded = ET.fromstring(f"<ROOT xmlns='{NS}'>{fragment}</ROOT>")
        parsed = DltConfig()
        parser.readDltConfig(reloaded.find(f"{{{NS}}}DLT-CONFIG"), parsed)
        assert parsed.getDltEcuRef().getValue() == "/LogAndTrace/DltEcus/Ecu1"
        assert parsed.getDltEcuRef().getDest() == "DLT-ECU"
        channels = parsed.getDltLogChannels()
        assert len(channels) == 1
        assert channels[0].getShortName() == "Channel1"
        assert channels[0].getLogChannelId().getValue() == "LOG1"
        assert channels[0].getNonVerboseMode().getValue() is True
        assert parsed.getSessionIdSupport().getValue() is True
        assert parsed.getTimestampSupport().getValue() is False
