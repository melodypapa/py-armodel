"""Parser tests for SecureCommunicationPropsSet (Table 6.45, p.370).

The SECURE-COMMUNICATION-PROPS-SET group of AUTOSAR_00052.xsd (l.103127) holds
two wrapper lists in sequence order -- AUTHENTICATION-PROPSS (unbounded choice of
SECURE-COMMUNICATION-AUTHENTICATION-PROPS) and FRESHNESS-PROPSS (unbounded choice
of SECURE-COMMUNICATION-FRESHNESS-PROPS); the SECURE-COMMUNICATION-PROPS-SET
complexType (l.103159) stacks the base groups (AR-OBJECT, REFERRABLE,
MULTILANGUAGE-REFERRABLE, IDENTIFIABLE, COLLECTABLE-ELEMENT,
PACKAGEABLE-ELEMENT, FIBEX-ELEMENT) in front of it. The tests exercise
readSecureCommunicationPropsSet, which must call readIdentifiable for the base
level (UUID/CATEGORY/S/T) and read the wrapper lists in XSD sequence order.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationPropsSet
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadSecureCommunicationPropsSet:
    def test_read_full(self):
        xml = f"""<SECURE-COMMUNICATION-PROPS-SET xmlns='{NS}'>
            <AUTHENTICATION-PROPSS>
                <SECURE-COMMUNICATION-AUTHENTICATION-PROPS><SHORT-NAME>auth1</SHORT-NAME><AUTH-INFO-TX-LENGTH>24</AUTH-INFO-TX-LENGTH></SECURE-COMMUNICATION-AUTHENTICATION-PROPS>
                <SECURE-COMMUNICATION-AUTHENTICATION-PROPS><SHORT-NAME>auth2</SHORT-NAME><AUTH-INFO-TX-LENGTH>28</AUTH-INFO-TX-LENGTH></SECURE-COMMUNICATION-AUTHENTICATION-PROPS>
            </AUTHENTICATION-PROPSS>
            <FRESHNESS-PROPSS>
                <SECURE-COMMUNICATION-FRESHNESS-PROPS><SHORT-NAME>fresh1</SHORT-NAME><FRESHNESS-VALUE-LENGTH>64</FRESHNESS-VALUE-LENGTH></SECURE-COMMUNICATION-FRESHNESS-PROPS>
            </FRESHNESS-PROPSS>
        </SECURE-COMMUNICATION-PROPS-SET>"""
        element = ET.fromstring(xml)
        props_set = SecureCommunicationPropsSet(None, "PropsSet")
        ARXMLParser().readSecureCommunicationPropsSet(element, props_set)

        auth_props = props_set.getAuthenticationProps()
        assert [props.getShortName() for props in auth_props] == ["auth1", "auth2"]
        assert auth_props[0].getAuthInfoTxLength().getValue() == 24
        assert auth_props[1].getAuthInfoTxLength().getValue() == 28

        freshness_props = props_set.getFreshnessProps()
        assert [props.getShortName() for props in freshness_props] == ["fresh1"]
        assert freshness_props[0].getFreshnessValueLength().getValue() == 64

    def test_read_empty_wrapper_lists(self):
        element = ET.fromstring(f"<SECURE-COMMUNICATION-PROPS-SET xmlns='{NS}'/>")
        props_set = SecureCommunicationPropsSet(None, "PropsSet")
        ARXMLParser().readSecureCommunicationPropsSet(element, props_set)

        assert props_set.getAuthenticationProps() == []
        assert props_set.getFreshnessProps() == []

    def test_read_base_level_attributes(self):
        xml = "<SECURE-COMMUNICATION-PROPS-SET xmlns='%s' UUID='DCE:2fac1234-31f8-11b4-a222-08002b34c003'><CATEGORY>DOIP</CATEGORY></SECURE-COMMUNICATION-PROPS-SET>" % NS
        element = ET.fromstring(xml)
        props_set = SecureCommunicationPropsSet(None, "PropsSet")
        ARXMLParser().readSecureCommunicationPropsSet(element, props_set)

        assert props_set.getUuid().getValue() == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        assert props_set.getCategory().getValue() == "DOIP"
