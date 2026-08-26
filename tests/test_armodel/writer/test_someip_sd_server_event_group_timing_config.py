"""Writer/reader round-trip tests for SomeipSdServerEventGroupTimingConfig (Table 6.172, p.517)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import RequestResponseDelay
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import SomeipSdServerEventGroupTimingConfig
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
    config = SomeipSdServerEventGroupTimingConfig(AUTOSAR.getInstance(), "MySdTiming")
    delay = RequestResponseDelay()
    delay.setMaxValue(TimeValue().setValue(8000))
    delay.setMinValue(TimeValue().setValue(2000))
    config.setRequestResponseDelay(delay)
    return config


class TestWriteSomeipSdServerEventGroupTimingConfig:
    def test_write_all_fields(self, writer):
        parent = _parent()
        writer.writeSomeipSdServerEventGroupTimingConfig(parent, _full_config())

        el = parent.find("SOME-IP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG")
        assert el is not None
        assert el.find("SHORT-NAME").text == "MySdTiming"
        req = el.find("REQUEST-RESPONSE-DELAY")
        assert req is not None
        assert req.find("MAX-VALUE").text == "8000.0"
        assert req.find("MIN-VALUE").text == "2000.0"


class TestSomeipSdServerEventGroupTimingConfigRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, tmp_path):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        config = pkg.createSomeipSdServerEventGroupTimingConfig("MySdTiming")
        delay = RequestResponseDelay()
        delay.setMaxValue(TimeValue().setValue(8000))
        delay.setMinValue(TimeValue().setValue(2000))
        config.setRequestResponseDelay(delay)

        out_file = str(tmp_path / "sd.arxml")
        writer.save(out_file, AUTOSAR.getInstance())

        AUTOSAR.getInstance().new()
        parser = ARXMLParser(options={"warning": True})
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        parser.load(out_file, document)

        re_config = document.find("Pkg").getElement("MySdTiming", SomeipSdServerEventGroupTimingConfig)
        assert re_config is not None
        re_delay = re_config.getRequestResponseDelay()
        assert re_delay is not None
        assert re_delay.getMaxValue().getValue() == 8000
        assert re_delay.getMinValue().getValue() == 2000

    def test_reader_empty_fields(self, parser):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        class MockParent(ARObject):
            def __init__(self):
                super().__init__()

        config = SomeipSdServerEventGroupTimingConfig(MockParent(), "cfg")
        parser.readSomeipSdServerEventGroupTimingConfig(_namespaced_snip("<SHORT-NAME>cfg</SHORT-NAME>"), config)
        assert config.getRequestResponseDelay() is None


_NS = "http://autosar.org/schema/r4.0"


def _namespaced_snip(inner):
    return ET.fromstring(f"<SOME-IP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG xmlns='{_NS}'>{inner}</SOME-IP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG>")
