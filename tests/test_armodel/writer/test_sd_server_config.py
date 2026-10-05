"""Writer/reader round-trip tests for SdServerConfig (R4.3.1 AUTOSAR_TPS_SystemTemplate, Table 6.171, p.355).

SdServerConfig has no standalone XML element: it is written inline by its aggregators
(ProvidedServiceInstance.sdServerConfig and EventHandler.sdServerConfig) through the
shared ``setSdServerConfig`` helper. XSD group ``SD-SERVER-CONFIG`` (AUTOSAR_00044.xsd
l.72991) element order: CAPABILITY-RECORDS, INITIAL-OFFER-BEHAVIOR, OFFER-CYCLIC-DELAY,
REQUEST-RESPONSE-DELAY, SERVER-SERVICE-MAJOR-VERSION, SERVER-SERVICE-MINOR-VERSION, TTL.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, PositiveInteger, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue import TagWithOptionalValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import SdServerConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import EventHandler, InitialSdDelayConfig, RequestResponseDelay
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

EXPECTED_CHILD_ORDER = [
    "CAPABILITY-RECORDS",
    "INITIAL-OFFER-BEHAVIOR",
    "OFFER-CYCLIC-DELAY",
    "REQUEST-RESPONSE-DELAY",
    "SERVER-SERVICE-MAJOR-VERSION",
    "SERVER-SERVICE-MINOR-VERSION",
    "TTL",
]


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


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _pos_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _time(text):
    val = TimeValue()
    val.setValue(text)
    return val


def _string(text):
    val = String()
    val.setValue(text)
    return val


def _record(key, value=None):
    record = TagWithOptionalValue()
    record.setKey(_string(key))
    if value is not None:
        record.setValue(_string(value))
    return record


def _new_config(records=True):
    config = SdServerConfig()
    if records:
        config.addCapabilityRecord(_record("PlugIns", "JPEG,MPEG2"))
        config.addCapabilityRecord(_record("passreq"))
    behavior = InitialSdDelayConfig()
    behavior.setInitialDelayMaxValue(_time("0.1"))
    behavior.setInitialRepetitionsMax(_pos_int("3"))
    config.setInitialOfferBehavior(behavior)
    config.setOfferCyclicDelay(_time("2.0"))
    delay = RequestResponseDelay()
    delay.setMaxValue(_time("0.5"))
    delay.setMinValue(_time("0.05"))
    delay.setChecksum(String().setValue("1234"))
    delay.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
    config.setRequestResponseDelay(delay)
    config.setServerServiceMajorVersion(_pos_int("1"))
    config.setServerServiceMinorVersion(_pos_int("2"))
    config.setTtl(_pos_int("10"))
    return config


class TestSdServerConfigWriter:
    def test_writes_all_seven_attributes_in_xsd_order(self, writer):
        parent = ET.Element("PARENT")
        writer.setSdServerConfig(parent, "SD-SERVER-CONFIG", _new_config())

        node = parent.find("SD-SERVER-CONFIG")
        assert node is not None
        assert [child.tag for child in node] == EXPECTED_CHILD_ORDER
        records = node.findall("CAPABILITY-RECORDS/TAG-WITH-OPTIONAL-VALUE")
        assert len(records) == 2
        assert records[0].find("KEY").text == "PlugIns"
        assert records[0].find("VALUE").text == "JPEG,MPEG2"
        assert records[1].find("KEY").text == "passreq"
        assert records[1].find("VALUE") is None
        assert node.find("INITIAL-OFFER-BEHAVIOR/INITIAL-DELAY-MAX-VALUE").text == "0.1"
        assert node.find("INITIAL-OFFER-BEHAVIOR/INITIAL-REPETITIONS-MAX").text == "3"
        assert node.find("OFFER-CYCLIC-DELAY").text == "2.0"
        assert node.find("REQUEST-RESPONSE-DELAY/MAX-VALUE").text == "0.5"
        assert node.find("REQUEST-RESPONSE-DELAY/MIN-VALUE").text == "0.05"
        assert node.find("SERVER-SERVICE-MAJOR-VERSION").text == "1"
        assert node.find("SERVER-SERVICE-MINOR-VERSION").text == "2"
        assert node.find("TTL").text == "10"

    def test_none_config_emits_no_element(self, writer):
        parent = ET.Element("PARENT")
        writer.setSdServerConfig(parent, "SD-SERVER-CONFIG", None)
        assert parent.find("SD-SERVER-CONFIG") is None
        assert len(list(parent)) == 0

    def test_empty_config_emits_empty_element(self, writer):
        parent = ET.Element("PARENT")
        writer.setSdServerConfig(parent, "SD-SERVER-CONFIG", SdServerConfig())
        node = parent.find("SD-SERVER-CONFIG")
        assert node is not None
        assert len(list(node)) == 0

    def test_empty_capability_records_omits_wrapper(self, writer):
        config = _new_config(records=False)
        parent = ET.Element("PARENT")
        writer.setSdServerConfig(parent, "SD-SERVER-CONFIG", config)
        node = parent.find("SD-SERVER-CONFIG")
        assert node.find("CAPABILITY-RECORDS") is None
        assert [child.tag for child in node] == EXPECTED_CHILD_ORDER[1:]

    def test_event_handler_aggregator_writes_sd_server_config(self, writer):
        handler = EventHandler(MockParent(), "MyHandler")
        handler.setSdServerConfig(_new_config())
        parent = ET.Element("PARENT")
        writer.writeEventHandler(parent, handler)

        node = parent.find("EVENT-HANDLER/SD-SERVER-CONFIG")
        assert node is not None
        assert [child.tag for child in node] == EXPECTED_CHILD_ORDER
        assert node.find("TTL").text == "10"


class TestSdServerConfigRoundTrip:
    def test_round_trip_preserves_all_seven_values(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.setSdServerConfig(parent, "SD-SERVER-CONFIG", _new_config())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getSdServerConfig(root[0], "SD-SERVER-CONFIG")

        assert isinstance(parsed, SdServerConfig)
        records = parsed.getCapabilityRecords()
        assert len(records) == 2
        assert isinstance(records[0], TagWithOptionalValue)
        assert records[0].getKey().getValue() == "PlugIns"
        assert records[0].getValue().getValue() == "JPEG,MPEG2"
        assert records[1].getKey().getValue() == "passreq"
        assert records[1].getValue() is None
        assert parsed.getInitialOfferBehavior().getInitialDelayMaxValue().getValue() == 0.1
        assert parsed.getInitialOfferBehavior().getInitialRepetitionsMax().getValue() == 3
        assert parsed.getOfferCyclicDelay().getValue() == 2.0
        assert parsed.getRequestResponseDelay().getMaxValue().getValue() == 0.5
        assert parsed.getRequestResponseDelay().getMinValue().getValue() == 0.05
        assert parsed.getRequestResponseDelay().getChecksum().getValue() == "1234"
        assert parsed.getRequestResponseDelay().getTimestamp().getValue() == "2024-01-01T00:00:00Z"
        assert parsed.getServerServiceMajorVersion().getValue() == 1
        assert parsed.getServerServiceMinorVersion().getValue() == 2
        assert parsed.getTtl().getValue() == 10

    def test_round_trip_preserves_arobject_checksum_and_timestamp(self, writer, parser):
        config = _new_config()
        checksum = String()
        checksum.setValue("1234")
        config.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2026-10-03T00:00:00Z")
        config.setTimestamp(timestamp)

        parent = ET.Element("PARENT")
        writer.setSdServerConfig(parent, "SD-SERVER-CONFIG", config)
        node = parent.find("SD-SERVER-CONFIG")
        assert node.attrib["S"] == "1234"
        assert node.attrib["T"] == "2026-10-03T00:00:00Z"

        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getSdServerConfig(root[0], "SD-SERVER-CONFIG")

        assert parsed.getChecksum().getValue() == "1234"
        assert parsed.getTimestamp().getValue() == "2026-10-03T00:00:00Z"

    def test_round_trip_empty_capability_records_yields_empty_list(self, writer, parser):
        config = _new_config(records=False)
        parent = ET.Element("PARENT")
        writer.setSdServerConfig(parent, "SD-SERVER-CONFIG", config)
        assert parent.find("SD-SERVER-CONFIG/CAPABILITY-RECORDS") is None
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getSdServerConfig(root[0], "SD-SERVER-CONFIG")

        assert parsed.getCapabilityRecords() == []
        assert parsed.getTtl().getValue() == 10
        assert parsed.getServerServiceMajorVersion().getValue() == 1

    def test_event_handler_aggregator_round_trip(self, writer, parser):
        handler = EventHandler(MockParent(), "MyHandler")
        handler.setSdServerConfig(_new_config())
        parent = ET.Element("PARENT")
        writer.writeEventHandler(parent, handler)

        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        recovered = EventHandler(MockParent(), "MyHandler")
        parser.readEventHandler(root[0][0], recovered)
        config = recovered.getSdServerConfig()

        assert isinstance(config, SdServerConfig)
        assert len(config.getCapabilityRecords()) == 2
        assert config.getCapabilityRecords()[1].getKey().getValue() == "passreq"
        assert config.getInitialOfferBehavior().getInitialDelayMaxValue().getValue() == 0.1
        assert config.getOfferCyclicDelay().getValue() == 2.0
        assert config.getRequestResponseDelay().getMaxValue().getValue() == 0.5
        assert config.getServerServiceMajorVersion().getValue() == 1
        assert config.getServerServiceMinorVersion().getValue() == 2
        assert config.getTtl().getValue() == 10
