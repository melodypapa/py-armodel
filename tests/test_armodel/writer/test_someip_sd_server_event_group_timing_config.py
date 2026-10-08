"""Writer/reader round-trip tests for SomeipSdServerEventGroupTimingConfig (Table 6.172, p.517).

Element tag SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG per the XSD (AUTOSAR_00052.xsd
l.5467 ARPackage element + l.110681 complexType; the XSD carries no "SOME-IP-SD" tokens).
Identity-debt upgrade (Rule 0001.7): the round-trip also serializes the EventHandler
sdServerEgTimingConfigRef together with the referenced config element and asserts the
config's field values after reload.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    EventHandler,
    RequestResponseDelay,
    SomeipSdServerEventGroupTimingConfig,
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

        el = parent.find("SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG")
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

        re_config = document.find("Pkg").getReferrableElement("MySdTiming", SomeipSdServerEventGroupTimingConfig)
        assert re_config is not None
        re_delay = re_config.getRequestResponseDelay()
        assert re_delay is not None
        assert re_delay.getMaxValue().getValue() == 8000
        assert re_delay.getMinValue().getValue() == 2000

    def test_round_trip_with_event_handler_ref_preserves_referenced_config_values(self, writer, tmp_path):
        """Identity-debt upgrade (Rule 0001.7): the EventHandler sdServerEgTimingConfigRef
        round-trips together with the referenced config element and its field values."""
        config = SomeipSdServerEventGroupTimingConfig(AUTOSAR.getInstance(), "ServerTiming1")
        delay = RequestResponseDelay()
        delay.setMinValue(TimeValue().setValue(2000))
        delay.setMaxValue(TimeValue().setValue(8000))
        config.setRequestResponseDelay(delay)

        handler = EventHandler(AUTOSAR.getInstance(), "EH1")
        handler.setSdServerEgTimingConfigRef(RefType().setDest("SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG").setValue("/SomeipSdTimingConfigs/ServerTiming1"))

        parent = ET.Element("ROOT")
        writer.writeSomeipSdServerEventGroupTimingConfig(parent, config)
        writer.writeEventHandler(parent, handler)

        out_file = str(tmp_path / "eh_timing.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_namespaced_wrap(parent), encoding="unicode"))

        AUTOSAR.getInstance().new()
        re_document = AUTOSAR.getInstance()
        re_document.setARRelease("R23-11")
        parser = ARXMLParser(options={"warning": True})
        root = ET.parse(out_file).getroot()

        re_config = SomeipSdServerEventGroupTimingConfig(re_document, "ServerTiming1")
        parser.readSomeipSdServerEventGroupTimingConfig(root[0][0], re_config)
        re_handler = EventHandler(re_document, "EH1")
        parser.readEventHandler(root[0][1], re_handler)

        re_ref = re_handler.getSdServerEgTimingConfigRef()
        assert re_ref is not None
        assert re_ref.getValue() == "/SomeipSdTimingConfigs/ServerTiming1"
        assert re_ref.getDest() == "SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG"

        re_delay = re_config.getRequestResponseDelay()
        assert re_delay is not None
        assert re_delay.getMinValue().getValue() == 2000
        assert re_delay.getMaxValue().getValue() == 8000

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
    return ET.fromstring(f"<SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG xmlns='{_NS}'>{inner}</SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG>")


def _namespaced_wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{_NS}'>{inner}</AUTOSAR>")
