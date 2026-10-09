"""Writer round-trip tests for SecureCommunicationFreshnessProps (Table 6.46, p.371).

Serialized through writeSecureCommunicationFreshnessProps (emitted by the
SecureCommunicationPropsSet FRESHNESS-PROPSS dispatch); the
SECURE-COMMUNICATION-FRESHNESS-PROPS group of AUTOSAR_00052.xsd (l.102930) holds
the five optional attributes in sequence order -- FRESHNESS-COUNTER-SYNC-ATTEMPTS,
FRESHNESS-TIMESTAMP-TIME-PERIOD-FACTOR, FRESHNESS-VALUE-LENGTH,
FRESHNESS-VALUE-TX-LENGTH, USE-FRESHNESS-TIMESTAMP; the
SECURE-COMMUNICATION-FRESHNESS-PROPS complexType (l.102970) stacks the base
groups (AR-OBJECT, REFERRABLE, MULTILANGUAGE-REFERRABLE, IDENTIFIABLE) in front
of it. The tests exercise writeSecureCommunicationFreshnessProps, which must
call writeIdentifiable for the base level (UUID/CATEGORY/S/T), emit the
attributes in XSD sequence order, plus the empty-props case (SHORT-NAME only).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, DateTime, PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationFreshnessProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "FRESHNESS-COUNTER-SYNC-ATTEMPTS",
    "FRESHNESS-TIMESTAMP-TIME-PERIOD-FACTOR",
    "FRESHNESS-VALUE-LENGTH",
    "FRESHNESS-VALUE-TX-LENGTH",
    "USE-FRESHNESS-TIMESTAMP",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<WRAP>", "<WRAP xmlns='%s'>" % NS, 1))


def _write(props: SecureCommunicationFreshnessProps) -> ET.Element:
    parent = ET.Element("WRAP")
    ARXMLWriter().writeSecureCommunicationFreshnessProps(parent, props)
    return parent


def _populate(props: SecureCommunicationFreshnessProps):
    attempts = PositiveInteger()
    attempts.setValue("3")
    props.setFreshnessCounterSyncAttempts(attempts)

    factor = PositiveInteger()
    factor.setValue("10")
    props.setFreshnessTimestampTimePeriodFactor(factor)

    length = PositiveInteger()
    length.setValue("64")
    props.setFreshnessValueLength(length)

    tx_length = PositiveInteger()
    tx_length.setValue("8")
    props.setFreshnessValueTxLength(tx_length)

    use_timestamp = Boolean()
    use_timestamp.setValue("true")
    props.setUseFreshnessTimestamp(use_timestamp)


class TestWriteSecureCommunicationFreshnessProps:
    def test_write_empty(self):
        node = _write(SecureCommunicationFreshnessProps(None, "fresh1")).find("SECURE-COMMUNICATION-FRESHNESS-PROPS")

        assert [child.tag for child in node] == ["SHORT-NAME"]
        for tag in XSD_CHILD_ORDER:
            assert node.find(tag) is None

    def test_write_child_order_matches_xsd(self):
        props = SecureCommunicationFreshnessProps(None, "fresh1")
        _populate(props)

        node = _write(props).find("SECURE-COMMUNICATION-FRESHNESS-PROPS")
        assert [child.tag for child in node] == ["SHORT-NAME"] + XSD_CHILD_ORDER

    def test_write_full_field_values(self):
        props = SecureCommunicationFreshnessProps(None, "fresh1")
        _populate(props)

        node = _write(props).find("SECURE-COMMUNICATION-FRESHNESS-PROPS")
        assert node.find("FRESHNESS-COUNTER-SYNC-ATTEMPTS").text == "3"
        assert node.find("FRESHNESS-TIMESTAMP-TIME-PERIOD-FACTOR").text == "10"
        assert node.find("FRESHNESS-VALUE-LENGTH").text == "64"
        assert node.find("FRESHNESS-VALUE-TX-LENGTH").text == "8"
        assert node.find("USE-FRESHNESS-TIMESTAMP").text == "true"

    def test_round_trip_full(self):
        props = SecureCommunicationFreshnessProps(None, "fresh1")
        _populate(props)

        node = _with_ns(_write(props)).find("{%s}SECURE-COMMUNICATION-FRESHNESS-PROPS" % NS)
        reloaded = SecureCommunicationFreshnessProps(None, "fresh1")
        ARXMLParser().readSecureCommunicationFreshnessProps(node, reloaded)

        assert reloaded.getShortName() == "fresh1"
        assert reloaded.getFreshnessCounterSyncAttempts().getValue() == 3
        assert reloaded.getFreshnessTimestampTimePeriodFactor().getValue() == 10
        assert reloaded.getFreshnessValueLength().getValue() == 64
        assert reloaded.getFreshnessValueTxLength().getValue() == 8
        assert reloaded.getUseFreshnessTimestamp().getValue() is True

    def test_round_trip_base_level_attributes(self):
        props = SecureCommunicationFreshnessProps(None, "fresh1")
        props.setChecksum(String().setValue("7"))
        props.setTimestamp(DateTime().setValue("2023-01-01T00:00:00+01:00"))
        props.setUuid(String().setValue("DCE:2fac1234-31f8-11b4-a222-08002b34c003"))
        props.setCategory("DOIP")

        node = _with_ns(_write(props)).find("{%s}SECURE-COMMUNICATION-FRESHNESS-PROPS" % NS)
        assert node.attrib["S"] == "7"
        assert node.attrib["T"] == "2023-01-01T00:00:00+01:00"
        assert node.attrib["UUID"] == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        assert node.find("{%s}CATEGORY" % NS).text == "DOIP"

        reloaded = SecureCommunicationFreshnessProps(None, "fresh1")
        ARXMLParser().readSecureCommunicationFreshnessProps(node, reloaded)
        assert reloaded.getChecksum().getValue() == "7"
        assert reloaded.getTimestamp().getValue() == "2023-01-01T00:00:00+01:00"
        assert reloaded.getUuid().getValue() == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        assert reloaded.getCategory().getValue() == "DOIP"
