"""Writer/reader round-trip tests for InitialSdDelayConfig (R23-11 AUTOSAR_CP_TPS_SystemTemplate, Table 6.170, p.514).

InitialSdDelayConfig has no standalone XML element: it is written inline by its
aggregators through the shared ``setInitialSdDelayConfig`` helper. XSD element order
(``AUTOSAR_00052.xsd`` group ``INITIAL-SD-DELAY-CONFIG`` l.72399): INITIAL-DELAY-MAX-VALUE,
INITIAL-DELAY-MIN-VALUE, INITIAL-REPETITIONS-BASE-DELAY, INITIAL-REPETITIONS-MAX. The
class is an ``ARObject``, so the element also carries the ``AR:AR-OBJECT`` attributes
(``S`` checksum / ``T`` timestamp, XSD l.4900).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, PositiveInteger, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import InitialSdDelayConfig
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

EXPECTED_CHILD_ORDER = [
    "INITIAL-DELAY-MAX-VALUE",
    "INITIAL-DELAY-MIN-VALUE",
    "INITIAL-REPETITIONS-BASE-DELAY",
    "INITIAL-REPETITIONS-MAX",
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


def _full_config():
    config = InitialSdDelayConfig()
    config.setInitialDelayMaxValue(TimeValue().setValue("0.1"))
    config.setInitialDelayMinValue(TimeValue().setValue("0.01"))
    config.setInitialRepetitionsBaseDelay(TimeValue().setValue("0.05"))
    config.setInitialRepetitionsMax(PositiveInteger().setValue("3"))
    return config


class TestInitialSdDelayConfigWriter:
    def test_writes_all_four_attributes_in_xsd_order(self, writer):
        parent = ET.Element("PARENT")
        writer.setInitialSdDelayConfig(parent, "INITIAL-FIND-BEHAVIOR", _full_config())

        node = parent.find("INITIAL-FIND-BEHAVIOR")
        assert node is not None
        assert [child.tag for child in node] == EXPECTED_CHILD_ORDER
        assert node.find("INITIAL-DELAY-MAX-VALUE").text == "0.1"
        assert node.find("INITIAL-DELAY-MIN-VALUE").text == "0.01"
        assert node.find("INITIAL-REPETITIONS-BASE-DELAY").text == "0.05"
        assert node.find("INITIAL-REPETITIONS-MAX").text == "3"

    def test_none_config_emits_no_element(self, writer):
        parent = ET.Element("PARENT")
        writer.setInitialSdDelayConfig(parent, "INITIAL-FIND-BEHAVIOR", None)
        assert parent.find("INITIAL-FIND-BEHAVIOR") is None
        assert len(list(parent)) == 0

    def test_empty_config_emits_empty_element(self, writer):
        parent = ET.Element("PARENT")
        writer.setInitialSdDelayConfig(parent, "INITIAL-FIND-BEHAVIOR", InitialSdDelayConfig())
        node = parent.find("INITIAL-FIND-BEHAVIOR")
        assert node is not None
        assert len(list(node)) == 0
        assert node.attrib == {}

    def test_writes_arobject_checksum_and_timestamp(self, writer):
        config = _full_config()
        config.setChecksum(String().setValue("1234"))
        config.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
        parent = ET.Element("PARENT")
        writer.setInitialSdDelayConfig(parent, "INITIAL-FIND-BEHAVIOR", config)
        node = parent.find("INITIAL-FIND-BEHAVIOR")
        assert node.attrib["S"] == "1234"
        assert node.attrib["T"] == "2024-01-01T00:00:00Z"


class TestInitialSdDelayConfigRoundTrip:
    def test_round_trip_preserves_all_four_values(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.setInitialSdDelayConfig(parent, "INITIAL-FIND-BEHAVIOR", _full_config())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getInitialSdDelayConfig(root[0], "INITIAL-FIND-BEHAVIOR")

        assert isinstance(parsed, InitialSdDelayConfig)
        assert parsed.getInitialDelayMaxValue().getValue() == 0.1
        assert parsed.getInitialDelayMinValue().getValue() == 0.01
        assert parsed.getInitialRepetitionsBaseDelay().getValue() == 0.05
        assert parsed.getInitialRepetitionsMax().getValue() == 3

    def test_round_trip_preserves_arobject_checksum_and_timestamp(self, writer, parser):
        config = _full_config()
        config.setChecksum(String().setValue("1234"))
        config.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
        parent = ET.Element("PARENT")
        writer.setInitialSdDelayConfig(parent, "INITIAL-FIND-BEHAVIOR", config)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getInitialSdDelayConfig(root[0], "INITIAL-FIND-BEHAVIOR")

        assert parsed.getChecksum().getValue() == "1234"
        assert parsed.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_file_round_trip_through_someip_sd_client_aggregator(self, writer, parser, tmp_path):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        config = pkg.createSomeipSdClientServiceInstanceConfig("MySdConfig")
        config.setInitialFindBehavior(_full_config())

        out_file = str(tmp_path / "initial_sd_delay_config.arxml")
        writer.save(out_file, AUTOSAR.getInstance())

        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        parser.load(out_file, document)

        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import SomeipSdClientServiceInstanceConfig

        re_config = document.find("Pkg").getReferrableElement("MySdConfig", SomeipSdClientServiceInstanceConfig)
        behavior = re_config.getInitialFindBehavior()
        assert isinstance(behavior, InitialSdDelayConfig)
        assert behavior.getInitialDelayMaxValue().getValue() == 0.1
        assert behavior.getInitialDelayMinValue().getValue() == 0.01
        assert behavior.getInitialRepetitionsBaseDelay().getValue() == 0.05
        assert behavior.getInitialRepetitionsMax().getValue() == 3
