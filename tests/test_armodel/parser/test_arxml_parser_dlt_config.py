"""Tests for the readDltConfig handler (R23-11 DltConfig, Table 6.335, p.722)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Dlt import DltConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test and pin the R23-11 release."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Fresh ARXMLParser instance running in strict mode."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    """Wrap an inner XML fragment in a root element bound to the AUTOSAR NS."""
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDltConfig:
    """Tests for readDltConfig handler (R23-11 DltConfig, Table 6.335, p.722)."""

    def test_read_dlt_config_full(self, parser):
        element = _snip(
            """
                <DLT-ECU-REF DEST="DLT-ECU">/LogAndTrace/DltEcus/Ecu1</DLT-ECU-REF>
                <DLT-LOG-CHANNELS>
                    <DLT-LOG-CHANNEL>
                        <SHORT-NAME>Channel1</SHORT-NAME>
                        <LOG-CHANNEL-ID>LOG1</LOG-CHANNEL-ID>
                        <NON-VERBOSE-MODE>true</NON-VERBOSE-MODE>
                    </DLT-LOG-CHANNEL>
                </DLT-LOG-CHANNELS>
                <SESSION-ID-SUPPORT>true</SESSION-ID-SUPPORT>
                <TIMESTAMP-SUPPORT>false</TIMESTAMP-SUPPORT>
            """,
            root_tag="DLT-CONFIG",
        )
        config = DltConfig()
        parser.readDltConfig(element, config)
        assert config.getDltEcuRef().getValue() == "/LogAndTrace/DltEcus/Ecu1"
        assert config.getDltEcuRef().getDest() == "DLT-ECU"
        channels = config.getDltLogChannels()
        assert len(channels) == 1
        assert channels[0].getShortName() == "Channel1"
        assert channels[0].getLogChannelId().getValue() == "LOG1"
        assert channels[0].getNonVerboseMode().getValue() is True
        assert config.getSessionIdSupport().getValue() is True
        assert config.getTimestampSupport().getValue() is False

    def test_read_dlt_config_empty(self, parser):
        element = _snip(
            """
            """,
            root_tag="DLT-CONFIG",
        )
        config = DltConfig()
        parser.readDltConfig(element, config)
        assert config.getDltEcuRef() is None
        assert config.getDltLogChannels() == []
        assert config.getSessionIdSupport() is None
        assert config.getTimestampSupport() is None

    def test_read_ecu_instance_dlt_config(self, parser):
        element = _snip(
            """
                <SHORT-NAME>ecu</SHORT-NAME>
                <DLT-CONFIG>
                    <DLT-ECU-REF DEST="DLT-ECU">/LogAndTrace/DltEcus/Ecu1</DLT-ECU-REF>
                    <DLT-LOG-CHANNELS>
                        <DLT-LOG-CHANNEL>
                            <SHORT-NAME>Channel1</SHORT-NAME>
                            <LOG-CHANNEL-ID>LOG1</LOG-CHANNEL-ID>
                        </DLT-LOG-CHANNEL>
                    </DLT-LOG-CHANNELS>
                    <SESSION-ID-SUPPORT>true</SESSION-ID-SUPPORT>
                    <TIMESTAMP-SUPPORT>false</TIMESTAMP-SUPPORT>
                </DLT-CONFIG>
            """,
            root_tag="ECU-INSTANCE",
        )
        instance = EcuInstance(parent=AUTOSAR.getInstance(), short_name="ecu")
        parser.readEcuInstance(element, instance)
        config = instance.getDltConfig()
        assert config is not None
        assert config.getDltEcuRef().getValue() == "/LogAndTrace/DltEcus/Ecu1"
        assert [channel.getShortName() for channel in config.getDltLogChannels()] == ["Channel1"]
        assert config.getDltLogChannels()[0].getLogChannelId().getValue() == "LOG1"
        assert config.getSessionIdSupport().getValue() is True
        assert config.getTimestampSupport().getValue() is False

    def test_read_ecu_instance_without_dlt_config(self, parser):
        element = _snip(
            """
                <SHORT-NAME>ecu</SHORT-NAME>
            """,
            root_tag="ECU-INSTANCE",
        )
        instance = EcuInstance(parent=AUTOSAR.getInstance(), short_name="ecu")
        parser.readEcuInstance(element, instance)
        assert instance.getDltConfig() is None
