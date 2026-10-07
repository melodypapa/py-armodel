"""Writer/reader round-trip tests for SomeipSdClientEventGroupTimingConfig (Table 6.173, p.521)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import RequestResponseDelay, SomeipSdClientEventGroupTimingConfig
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
    config = SomeipSdClientEventGroupTimingConfig(AUTOSAR.getInstance(), "MySdTiming")
    config.setSubscribeEventgroupRetryDelay(TimeValue().setValue(5000))
    config.setSubscribeEventgroupRetryMax(PositiveInteger().setValue(3))
    config.setTimeToLive(PositiveInteger().setValue(255))
    delay = RequestResponseDelay()
    delay.setMaxValue(TimeValue().setValue(8000))
    delay.setMinValue(TimeValue().setValue(2000))
    config.setRequestResponseDelay(delay)
    return config


class TestWriteSomeipSdClientEventGroupTimingConfig:
    def test_write_all_fields(self, writer):
        parent = _parent()
        writer.writeSomeipSdClientEventGroupTimingConfig(parent, _full_config())

        el = parent.find("SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG")
        assert el is not None
        assert el.find("SHORT-NAME").text == "MySdTiming"
        assert el.find("SUBSCRIBE-EVENTGROUP-RETRY-DELAY").text == "5000.0"
        assert el.find("SUBSCRIBE-EVENTGROUP-RETRY-MAX").text == "3"
        assert el.find("TIME-TO-LIVE").text == "255"
        req = el.find("REQUEST-RESPONSE-DELAY")
        assert req is not None
        assert req.find("MAX-VALUE").text == "8000.0"
        assert req.find("MIN-VALUE").text == "2000.0"


class TestSomeipSdClientEventGroupTimingConfigRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, tmp_path):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        config = pkg.createSomeipSdClientEventGroupTimingConfig("MySdTiming")
        config.setSubscribeEventgroupRetryDelay(TimeValue().setValue(5000))
        config.setSubscribeEventgroupRetryMax(PositiveInteger().setValue(3))
        config.setTimeToLive(PositiveInteger().setValue(255))
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

        re_config = document.find("Pkg").getReferrableElement("MySdTiming", SomeipSdClientEventGroupTimingConfig)
        assert re_config is not None
        assert re_config.getSubscribeEventgroupRetryDelay().getValue() == 5000
        assert re_config.getSubscribeEventgroupRetryMax().getValue() == 3
        assert re_config.getTimeToLive().getValue() == 255
        re_delay = re_config.getRequestResponseDelay()
        assert re_delay is not None
        assert re_delay.getMaxValue().getValue() == 8000
        assert re_delay.getMinValue().getValue() == 2000

    def test_reader_empty_fields(self, parser):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        class MockParent(ARObject):
            def __init__(self):
                super().__init__()

        config = SomeipSdClientEventGroupTimingConfig(MockParent(), "cfg")
        parser.readSomeipSdClientEventGroupTimingConfig(_namespaced_snip("<SHORT-NAME>cfg</SHORT-NAME>"), config)
        assert config.getRequestResponseDelay() is None
        assert config.getSubscribeEventgroupRetryDelay() is None
        assert config.getSubscribeEventgroupRetryMax() is None
        assert config.getTimeToLive() is None

    def test_round_trip_with_consumed_event_group_ref_preserves_referenced_config_values(self, writer, tmp_path):
        """Identity-debt upgrade (Rule 0001.7): the ConsumedEventGroup sdClientTimerConfigRef
        round-trips together with the referenced config element and its field values."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import ConsumedEventGroup

        config = SomeipSdClientEventGroupTimingConfig(AUTOSAR.getInstance(), "ClientTiming1")
        config.setSubscribeEventgroupRetryDelay(TimeValue().setValue(5000))
        config.setSubscribeEventgroupRetryMax(PositiveInteger().setValue(3))
        config.setTimeToLive(PositiveInteger().setValue(255))
        delay = RequestResponseDelay()
        delay.setMinValue(TimeValue().setValue(2000))
        delay.setMaxValue(TimeValue().setValue(8000))
        config.setRequestResponseDelay(delay)

        group = ConsumedEventGroup(AUTOSAR.getInstance(), "CEG1")
        group.setSdClientTimerConfigRef(RefType().setDest("SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG").setValue("/SomeipSdTimingConfigs/ClientTiming1"))

        parent = ET.Element("ROOT")
        writer.writeSomeipSdClientEventGroupTimingConfig(parent, config)
        writer.writeConsumedEventGroup(parent, group)

        out_file = str(tmp_path / "ceg_timing.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_namespaced_wrap(parent), encoding="unicode"))

        AUTOSAR.getInstance().new()
        re_document = AUTOSAR.getInstance()
        re_document.setARRelease("R23-11")
        parser = ARXMLParser(options={"warning": True})
        root = ET.parse(out_file).getroot()

        re_config = SomeipSdClientEventGroupTimingConfig(re_document, "ClientTiming1")
        parser.readSomeipSdClientEventGroupTimingConfig(root[0][0], re_config)
        re_group = ConsumedEventGroup(re_document, "CEG1")
        parser.readConsumedEventGroup(root[0][1], re_group)

        re_ref = re_group.getSdClientTimerConfigRef()
        assert re_ref is not None
        assert re_ref.getValue() == "/SomeipSdTimingConfigs/ClientTiming1"
        assert re_ref.getDest() == "SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG"

        assert re_config.getSubscribeEventgroupRetryDelay().getValue() == 5000
        assert re_config.getSubscribeEventgroupRetryMax().getValue() == 3
        assert re_config.getTimeToLive().getValue() == 255
        re_delay = re_config.getRequestResponseDelay()
        assert re_delay is not None
        assert re_delay.getMinValue().getValue() == 2000
        assert re_delay.getMaxValue().getValue() == 8000


_NS = "http://autosar.org/schema/r4.0"


def _namespaced_snip(inner):
    return ET.fromstring(f"<SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG xmlns='{_NS}'>{inner}</SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG>")


def _namespaced_wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{_NS}'>{inner}</AUTOSAR>")
