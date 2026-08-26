"""Writer/reader round-trip tests for SdClientConfig (XSD SD-CLIENT-CONFIG group).

SdClientConfig is an obsolete XSD-only class (no R23-11 PDF table) aggregated by
ConsumedServiceInstance.sdClientConfig and EventHandler.sdServerConfig... (client side).
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue import TagWithOptionalValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    InitialSdDelayConfig,
    RequestResponseDelay,
    SdClientConfig,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


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


def _new_config():
    config = SdClientConfig()
    tag = TagWithOptionalValue()
    config.addCapabilityRecord(tag)
    config.setClientServiceMajorVersion(_pos_int("15"))
    config.setClientServiceMinorVersion(_pos_int("3"))
    config.setInitialFindBehavior(InitialSdDelayConfig())
    config.setRequestResponseDelay(RequestResponseDelay())
    config.setTtl(_pos_int("255"))
    return config


class TestWriteSdClientConfig:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.setSdClientConfig(parent, "SD-CLIENT-CONFIG", _new_config())

        node = parent.find("SD-CLIENT-CONFIG")
        assert node is not None
        assert node.find("CAPABILITY-RECORDS/TAG-WITH-OPTIONAL-VALUE") is not None
        assert node.find("CLIENT-SERVICE-MAJOR-VERSION").text == "15"
        assert node.find("CLIENT-SERVICE-MINOR-VERSION").text == "3"
        assert node.find("INITIAL-FIND-BEHAVIOR") is not None
        assert node.find("REQUEST-RESPONSE-DELAY") is not None
        assert node.find("TTL").text == "255"

    def test_write_empty_fields_omits_optional_tags(self, writer):
        parent = ET.Element("PARENT")
        writer.setSdClientConfig(parent, "SD-CLIENT-CONFIG", SdClientConfig())
        node = parent.find("SD-CLIENT-CONFIG")
        assert node is not None
        assert len(list(node)) == 0


class TestSdClientConfigRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.setSdClientConfig(parent, "SD-CLIENT-CONFIG", _new_config())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getSdClientConfig(root[0], "SD-CLIENT-CONFIG")

        assert isinstance(parsed, SdClientConfig)
        records = parsed.getCapabilityRecords()
        assert len(records) == 1
        assert isinstance(records[0], TagWithOptionalValue)
        assert parsed.getClientServiceMajorVersion().getValue() == 15
        assert parsed.getClientServiceMinorVersion().getValue() == 3
        assert isinstance(parsed.getInitialFindBehavior(), InitialSdDelayConfig)
        assert isinstance(parsed.getRequestResponseDelay(), RequestResponseDelay)
        assert parsed.getTtl().getValue() == 255

    def test_reader_empty_fields(self, parser):
        parent = ET.fromstring("<PARENT xmlns='%s'><SD-CLIENT-CONFIG/></PARENT>" % NS)
        parsed = parser.getSdClientConfig(parent, "SD-CLIENT-CONFIG")
        assert isinstance(parsed, SdClientConfig)
        assert parsed.getCapabilityRecords() == []
        assert parsed.getClientServiceMajorVersion() is None
        assert parsed.getTtl() is None
