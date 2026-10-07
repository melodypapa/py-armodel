"""
Writer/reader round-trip tests for MacSecCipherSuiteConfig (Table 3.124, p.176).

MacSecCipherSuiteConfig is an ARObject aggregated by
MacSecCryptoAlgoConfig.cipherSuiteConfig (0..4). It carries the optional attributes
cipherSuite (String, element CIPHER-SUITE) and cipherSuitePriority (PositiveInteger,
element CIPHER-SUITE-PRIORITY), plus the AR-OBJECT base level (S/T attributes) carried
by writeARObject/readARObject. The item element inside the CIPHER-SUITE-CONFIGS wrapper
is the type name MAC-SEC-CIPHER-SUITE-CONFIG (AUTOSAR_00052.xsd line 78994); the XSD
group (line 78937) fixes the child order CIPHER-SUITE -> CIPHER-SUITE-PRIORITY.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecCipherSuiteConfig
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
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")


def _string(value):
    s = String()
    s.setValue(value)
    return s


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(str(value))
    return p


def _date_time(value):
    dt = DateTime()
    dt.setValue(value)
    return dt


def _new_config(cipher_suite="GCM-AES-128", priority=1):
    config = MacSecCipherSuiteConfig()
    config.setCipherSuite(_string(cipher_suite))
    config.setCipherSuitePriority(_pos_int(priority))
    return config


class TestWriteMacSecCipherSuiteConfig:
    def test_write_all_fields(self, writer):
        config = _new_config()
        parent = ET.Element("CONFIGS")
        writer.writeMacSecCipherSuiteConfig(parent, config)

        node = parent.find("MAC-SEC-CIPHER-SUITE-CONFIG")
        assert node is not None
        assert node.find("CIPHER-SUITE").text == "GCM-AES-128"
        assert node.find("CIPHER-SUITE-PRIORITY").text == "1"

    def test_write_empty_omits_fields(self, writer):
        config = MacSecCipherSuiteConfig()
        parent = ET.Element("CONFIGS")
        writer.writeMacSecCipherSuiteConfig(parent, config)

        node = parent.find("MAC-SEC-CIPHER-SUITE-CONFIG")
        assert node is not None
        assert node.find("CIPHER-SUITE") is None
        assert node.find("CIPHER-SUITE-PRIORITY") is None

    def test_write_xsd_child_order(self, writer):
        config = _new_config(cipher_suite="GCM-AES-XPN-128", priority=3)
        parent = ET.Element("CONFIGS")
        writer.writeMacSecCipherSuiteConfig(parent, config)

        node = parent.find("MAC-SEC-CIPHER-SUITE-CONFIG")
        children = [child.tag for child in node]
        assert children == ["CIPHER-SUITE", "CIPHER-SUITE-PRIORITY"]

    def test_write_arobject_base_level(self, writer):
        config = _new_config()
        config.setChecksum(_string("chk-777"))
        config.setTimestamp(_date_time("2011-07-08T09:10:11Z"))
        parent = ET.Element("CONFIGS")
        writer.writeMacSecCipherSuiteConfig(parent, config)

        node = parent.find("MAC-SEC-CIPHER-SUITE-CONFIG")
        assert node is not None
        assert node.attrib["S"] == "chk-777"
        assert node.attrib["T"] == "2011-07-08T09:10:11Z"


class TestMacSecCipherSuiteConfigRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        config = _new_config()

        parent = ET.Element("CONFIGS")
        writer.writeMacSecCipherSuiteConfig(parent, config)

        out_file = str(tmp_path / "mac_sec_cipher_suite_config.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = MacSecCipherSuiteConfig()
        parser.readMacSecCipherSuiteConfig(tree.getroot()[0][0], recovered)

        assert recovered.getCipherSuite().getValue() == "GCM-AES-128"
        assert recovered.getCipherSuitePriority().getValue() == 1

    def test_round_trip_preserves_base_level(self, writer, parser, tmp_path):
        config = _new_config(cipher_suite="GCM-AES-256", priority=2)
        config.setChecksum(_string("chk-888"))
        config.setTimestamp(_date_time("2012-01-02T03:04:05Z"))

        parent = ET.Element("CONFIGS")
        writer.writeMacSecCipherSuiteConfig(parent, config)

        out_file = str(tmp_path / "mac_sec_cipher_suite_config_base.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = MacSecCipherSuiteConfig()
        parser.readMacSecCipherSuiteConfig(tree.getroot()[0][0], recovered)

        assert recovered.getChecksum().getValue() == "chk-888"
        assert recovered.getTimestamp().getValue() == "2012-01-02T03:04:05Z"
        assert recovered.getCipherSuite().getValue() == "GCM-AES-256"
        assert recovered.getCipherSuitePriority().getValue() == 2

    def test_reader_empty_fields(self, parser):
        xml = "<AUTOSAR xmlns='%s'>" "<CONFIGS><MAC-SEC-CIPHER-SUITE-CONFIG/></CONFIGS>" "</AUTOSAR>" % NS
        root = ET.fromstring(xml)
        recovered = MacSecCipherSuiteConfig()
        parser.readMacSecCipherSuiteConfig(root[0][0], recovered)

        assert recovered.getCipherSuite() is None
        assert recovered.getCipherSuitePriority() is None
        assert recovered.getChecksum() is None
        assert recovered.getTimestamp() is None
