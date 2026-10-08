"""Parser tests for SecureCommunicationAuthenticationProps (Table 6.47, p.371).

The SECURE-COMMUNICATION-AUTHENTICATION-PROPS group of AUTOSAR_00052.xsd (l.102877)
holds AUTH-INFO-TX-LENGTH (POSITIVE-INTEGER, 0..1); the group's AUTH-ALGORITHM
element carries atp.Status="removed" (4.4.0) and is not modeled. The
SECURE-COMMUNICATION-AUTHENTICATION-PROPS complexType (l.102899) stacks the base
groups (AR-OBJECT, REFERRABLE, MULTILANGUAGE-REFERRABLE, IDENTIFIABLE) in front
of it. The tests exercise readSecureCommunicationAuthenticationProps, which must
call readIdentifiable for the base level (UUID/CATEGORY/S/T) and read the
attribute via its mutator.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationAuthenticationProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadSecureCommunicationAuthenticationProps:
    def test_read_full(self):
        xml = f"""<SECURE-COMMUNICATION-AUTHENTICATION-PROPS xmlns='{NS}'>
            <SHORT-NAME>auth1</SHORT-NAME>
            <AUTH-INFO-TX-LENGTH>24</AUTH-INFO-TX-LENGTH>
        </SECURE-COMMUNICATION-AUTHENTICATION-PROPS>"""
        element = ET.fromstring(xml)
        props = SecureCommunicationAuthenticationProps(None, "auth1")
        ARXMLParser().readSecureCommunicationAuthenticationProps(element, props)

        assert props.getShortName() == "auth1"
        assert props.getAuthInfoTxLength().getValue() == 24

    def test_read_empty(self):
        element = ET.fromstring(f"<SECURE-COMMUNICATION-AUTHENTICATION-PROPS xmlns='{NS}'><SHORT-NAME>auth1</SHORT-NAME></SECURE-COMMUNICATION-AUTHENTICATION-PROPS>")
        props = SecureCommunicationAuthenticationProps(None, "auth1")
        ARXMLParser().readSecureCommunicationAuthenticationProps(element, props)

        assert props.getAuthInfoTxLength() is None

    def test_read_base_level_attributes(self):
        xml = (
            "<SECURE-COMMUNICATION-AUTHENTICATION-PROPS xmlns='%s' S='7' T='2023-01-01T00:00:00+01:00' UUID='DCE:2fac1234-31f8-11b4-a222-08002b34c003'><SHORT-NAME>auth1</SHORT-NAME><CATEGORY>DOIP</CATEGORY></SECURE-COMMUNICATION-AUTHENTICATION-PROPS>"
            % NS
        )
        element = ET.fromstring(xml)
        props = SecureCommunicationAuthenticationProps(None, "auth1")
        ARXMLParser().readSecureCommunicationAuthenticationProps(element, props)

        assert props.getChecksum().getValue() == "7"
        assert props.getTimestamp().getValue() == "2023-01-01T00:00:00+01:00"
        assert props.getUuid().getValue() == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        assert props.getCategory().getValue() == "DOIP"
