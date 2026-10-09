"""Parser tests for SecureCommunicationFreshnessProps (Table 6.46, p.371).

The SECURE-COMMUNICATION-FRESHNESS-PROPS group of AUTOSAR_00052.xsd (l.102930)
holds the five optional attributes in sequence order -- FRESHNESS-COUNTER-SYNC-ATTEMPTS,
FRESHNESS-TIMESTAMP-TIME-PERIOD-FACTOR, FRESHNESS-VALUE-LENGTH,
FRESHNESS-VALUE-TX-LENGTH, USE-FRESHNESS-TIMESTAMP; the
SECURE-COMMUNICATION-FRESHNESS-PROPS complexType (l.102970) stacks the base
groups (AR-OBJECT, REFERRABLE, MULTILANGUAGE-REFERRABLE, IDENTIFIABLE) in front
of it. The tests exercise readSecureCommunicationFreshnessProps, which must call
readIdentifiable for the base level (UUID/CATEGORY/S/T) and read the attributes
via their mutators in XSD sequence order.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationFreshnessProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadSecureCommunicationFreshnessProps:
    def test_read_full(self):
        xml = f"""<SECURE-COMMUNICATION-FRESHNESS-PROPS xmlns='{NS}'>
            <SHORT-NAME>fresh1</SHORT-NAME>
            <FRESHNESS-COUNTER-SYNC-ATTEMPTS>3</FRESHNESS-COUNTER-SYNC-ATTEMPTS>
            <FRESHNESS-TIMESTAMP-TIME-PERIOD-FACTOR>10</FRESHNESS-TIMESTAMP-TIME-PERIOD-FACTOR>
            <FRESHNESS-VALUE-LENGTH>64</FRESHNESS-VALUE-LENGTH>
            <FRESHNESS-VALUE-TX-LENGTH>8</FRESHNESS-VALUE-TX-LENGTH>
            <USE-FRESHNESS-TIMESTAMP>true</USE-FRESHNESS-TIMESTAMP>
        </SECURE-COMMUNICATION-FRESHNESS-PROPS>"""
        element = ET.fromstring(xml)
        props = SecureCommunicationFreshnessProps(None, "fresh1")
        ARXMLParser().readSecureCommunicationFreshnessProps(element, props)

        assert props.getShortName() == "fresh1"
        assert props.getFreshnessCounterSyncAttempts().getValue() == 3
        assert props.getFreshnessTimestampTimePeriodFactor().getValue() == 10
        assert props.getFreshnessValueLength().getValue() == 64
        assert props.getFreshnessValueTxLength().getValue() == 8
        assert props.getUseFreshnessTimestamp().getValue() is True

    def test_read_empty(self):
        element = ET.fromstring(f"<SECURE-COMMUNICATION-FRESHNESS-PROPS xmlns='{NS}'><SHORT-NAME>fresh1</SHORT-NAME></SECURE-COMMUNICATION-FRESHNESS-PROPS>")
        props = SecureCommunicationFreshnessProps(None, "fresh1")
        ARXMLParser().readSecureCommunicationFreshnessProps(element, props)

        assert props.getFreshnessCounterSyncAttempts() is None
        assert props.getFreshnessTimestampTimePeriodFactor() is None
        assert props.getFreshnessValueLength() is None
        assert props.getFreshnessValueTxLength() is None
        assert props.getUseFreshnessTimestamp() is None

    def test_read_base_level_attributes(self):
        xml = (
            "<SECURE-COMMUNICATION-FRESHNESS-PROPS xmlns='%s' S='7' T='2023-01-01T00:00:00+01:00' UUID='DCE:2fac1234-31f8-11b4-a222-08002b34c003'><SHORT-NAME>fresh1</SHORT-NAME><CATEGORY>DOIP</CATEGORY></SECURE-COMMUNICATION-FRESHNESS-PROPS>"
            % NS
        )
        element = ET.fromstring(xml)
        props = SecureCommunicationFreshnessProps(None, "fresh1")
        ARXMLParser().readSecureCommunicationFreshnessProps(element, props)

        assert props.getChecksum().getValue() == "7"
        assert props.getTimestamp().getValue() == "2023-01-01T00:00:00+01:00"
        assert props.getUuid().getValue() == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        assert props.getCategory().getValue() == "DOIP"
