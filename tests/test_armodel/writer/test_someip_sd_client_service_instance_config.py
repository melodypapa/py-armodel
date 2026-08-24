"""Writer/reader round-trip tests for SomeipSdClientServiceInstanceConfig (Table F.117, p.2007)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    InitialSdDelayConfig,
    SomeipSdClientServiceInstanceConfig,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _parent():
    return ET.Element("ROOT")


def _full_config():
    config = SomeipSdClientServiceInstanceConfig(AUTOSAR.getInstance(), "MySdConfig")
    config.setPriority(PositiveInteger().setValue(5))
    config.setServiceFindTimeToLive(PositiveInteger().setValue(60))
    behavior = InitialSdDelayConfig()
    behavior.setInitialDelayMaxValue(TimeValue().setValue(5000))
    behavior.setInitialDelayMinValue(TimeValue().setValue(1000))
    config.setInitialFindBehavior(behavior)
    return config


class TestWriteSomeipSdClientServiceInstanceConfig:
    def test_write_all_fields(self, writer):
        parent = _parent()
        writer.writeSomeipSdClientServiceInstanceConfig(parent, _full_config())

        el = parent.find("SOME-IP-SD-CLIENT-SERVICE-INSTANCE-CONFIG")
        assert el is not None
        assert el.find("SHORT-NAME").text == "MySdConfig"
        assert el.find("PRIORITY").text == "5"
        assert el.find("SERVICE-FIND-TIME-TO-LIVE").text == "60"
        init = el.find("INITIAL-FIND-BEHAVIOR")
        assert init is not None
        assert init.find("INITIAL-DELAY-MAX-VALUE").text == "5000.0"
        assert init.find("INITIAL-DELAY-MIN-VALUE").text == "1000.0"


class TestSomeipSdClientServiceInstanceConfigRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, tmp_path):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        config = pkg.createSomeipSdClientServiceInstanceConfig("MySdConfig")
        config.setPriority(PositiveInteger().setValue(5))
        config.setServiceFindTimeToLive(PositiveInteger().setValue(60))
        behavior = InitialSdDelayConfig()
        behavior.setInitialDelayMaxValue(TimeValue().setValue(5000))
        behavior.setInitialDelayMinValue(TimeValue().setValue(1000))
        config.setInitialFindBehavior(behavior)

        out_file = str(tmp_path / "sd.arxml")
        writer.save(out_file, AUTOSAR.getInstance())

        AUTOSAR.getInstance().new()
        parser = ARXMLParser(options={"warning": True})
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        parser.load(out_file, document)

        re_config = document.find("Pkg").getElement("MySdConfig", SomeipSdClientServiceInstanceConfig)
        assert re_config is not None
        assert re_config.getPriority().getValue() == 5
        assert re_config.getServiceFindTimeToLive().getValue() == 60
        re_behavior = re_config.getInitialFindBehavior()
        assert re_behavior is not None
        assert re_behavior.getInitialDelayMaxValue().getValue() == 5000
        assert re_behavior.getInitialDelayMinValue().getValue() == 1000
        assert re_behavior.getInitialRepetitionsBaseDelay() is None
        assert re_behavior.getInitialRepetitionsMax() is None

    def test_reader_empty_fields(self, parser):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        class MockParent(ARObject):
            def __init__(self):
                super().__init__()

        config = SomeipSdClientServiceInstanceConfig(MockParent(), "cfg")
        parser.readSomeipSdClientServiceInstanceConfig(_namespaced_snip("<SHORT-NAME>cfg</SHORT-NAME>"), config)
        assert config.getPriority() is None
        assert config.getServiceFindTimeToLive() is None
        assert config.getInitialFindBehavior() is None


_NS = "http://autosar.org/schema/r4.0"


def _namespaced_snip(inner):
    return ET.fromstring(f"<SOME-IP-SD-CLIENT-SERVICE-INSTANCE-CONFIG xmlns='{_NS}'>{inner}</SOME-IP-SD-CLIENT-SERVICE-INSTANCE-CONFIG>")
