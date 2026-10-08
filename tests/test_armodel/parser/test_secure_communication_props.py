"""Parser tests for SecureCommunicationProps (Table 6.44, p.369).

The SECURE-COMMUNICATION-PROPS group of AUTOSAR_00052.xsd (l.102992) holds 11
POSITIVE-INTEGER children (minOccurs=0, maxOccurs=1); the
SECURE-COMMUNICATION-PROPS complexType (l.103114) stacks the AR-OBJECT group in
front of it and carries the AR-OBJECT attributeGroup (S/T). The tests exercise
getSecureCommunicationProps, which must call readARObject for the base level
(S/T) and read the own children in XSD sequence order.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestGetSecureCommunicationProps:
    def test_read_full(self):
        xml = f"""<SECURE-COMMUNICATION-PROPS xmlns='{NS}'>
            <AUTH-DATA-FRESHNESS-LENGTH>24</AUTH-DATA-FRESHNESS-LENGTH>
            <AUTH-DATA-FRESHNESS-START-POSITION>16</AUTH-DATA-FRESHNESS-START-POSITION>
            <AUTHENTICATION-BUILD-ATTEMPTS>2</AUTHENTICATION-BUILD-ATTEMPTS>
            <AUTHENTICATION-RETRIES>3</AUTHENTICATION-RETRIES>
            <DATA-ID>42</DATA-ID>
            <FRESHNESS-VALUE-ID>100</FRESHNESS-VALUE-ID>
            <MESSAGE-LINK-LENGTH>32</MESSAGE-LINK-LENGTH>
            <MESSAGE-LINK-POSITION>0</MESSAGE-LINK-POSITION>
            <SECONDARY-FRESHNESS-VALUE-ID>200</SECONDARY-FRESHNESS-VALUE-ID>
            <SECURED-AREA-LENGTH>64</SECURED-AREA-LENGTH>
            <SECURED-AREA-OFFSET>8</SECURED-AREA-OFFSET>
        </SECURE-COMMUNICATION-PROPS>"""
        parent = ET.fromstring(f"<WRAP xmlns='{NS}'>{xml}</WRAP>")
        props = ARXMLParser().getSecureCommunicationProps(parent, "SECURE-COMMUNICATION-PROPS")

        assert isinstance(props, SecureCommunicationProps)
        assert props.getAuthDataFreshnessLength().getValue() == 24
        assert props.getAuthDataFreshnessStartPosition().getValue() == 16
        assert props.getAuthenticationBuildAttempts().getValue() == 2
        assert props.getAuthenticationRetries().getValue() == 3
        assert props.getDataId().getValue() == 42
        assert props.getFreshnessValueId().getValue() == 100
        assert props.getMessageLinkLength().getValue() == 32
        assert props.getMessageLinkPosition().getValue() == 0
        assert props.getSecondaryFreshnessValueId().getValue() == 200
        assert props.getSecuredAreaLength().getValue() == 64
        assert props.getSecuredAreaOffset().getValue() == 8

    def test_read_base_level_attributes(self):
        xml = "<SECURE-COMMUNICATION-PROPS xmlns='%s' S='5' T='2025-04-04T00:00:00Z'><DATA-ID>42</DATA-ID></SECURE-COMMUNICATION-PROPS>" % NS
        parent = ET.fromstring(f"<WRAP xmlns='{NS}'>{xml}</WRAP>")
        props = ARXMLParser().getSecureCommunicationProps(parent, "SECURE-COMMUNICATION-PROPS")

        assert props.getChecksum().getValue() == "5"
        assert props.getTimestamp().getValue() == "2025-04-04T00:00:00Z"

    def test_read_minimal(self):
        parent = ET.fromstring(f"<WRAP xmlns='{NS}'><SECURE-COMMUNICATION-PROPS/></WRAP>")
        props = ARXMLParser().getSecureCommunicationProps(parent, "SECURE-COMMUNICATION-PROPS")

        assert isinstance(props, SecureCommunicationProps)
        assert props.getAuthDataFreshnessLength() is None
        assert props.getAuthDataFreshnessStartPosition() is None
        assert props.getAuthenticationBuildAttempts() is None
        assert props.getAuthenticationRetries() is None
        assert props.getDataId() is None
        assert props.getFreshnessValueId() is None
        assert props.getMessageLinkLength() is None
        assert props.getMessageLinkPosition() is None
        assert props.getSecondaryFreshnessValueId() is None
        assert props.getSecuredAreaLength() is None
        assert props.getSecuredAreaOffset() is None

    def test_read_absent(self):
        parent = ET.fromstring(f"<SECURED-I-PDU xmlns='{NS}'/>")
        props = ARXMLParser().getSecureCommunicationProps(parent, "SECURE-COMMUNICATION-PROPS")

        assert props is None
