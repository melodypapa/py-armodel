"""
Reader tests for MacSecLocalKayProps (CP_TPS_SystemTemplate Table 3.119, p.174, R23-11).

Covers the AR-OBJECT base level (S/T checksum/timestamp attributes), the six optional
children of the MAC-SEC-KAY-CONFIG element shape in XSD group order (DESTINATION-MAC-ADDRESS,
GLOBAL-KAY-PROPS-REF, KEY-SERVER-PRIORITY, MKA-PARTICIPANT-REFS/MKA-PARTICIPANT-REF, ROLE,
SOURCE-MAC-ADDRESS per group MAC-SEC-LOCAL-KAY-PROPS, AUTOSAR_00052.xsd), the empty-element
case and the dispatch through the aggregating MacSecProps (MAC-SEC-KAY-CONFIG child of
MAC-SEC-PROPS).

Round-trip counterpart: tests/test_armodel/writer/test_mac_sec_local_kay_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecLocalKayProps, MacSecRoleEnum
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<MAC-SEC-KAY-CONFIG xmlns='{NS}'>{inner}</MAC-SEC-KAY-CONFIG>")


def _snip_with_attrs(attrs: str, inner: str) -> ET.Element:
    return ET.fromstring(f"<MAC-SEC-KAY-CONFIG xmlns='{NS}' {attrs}>{inner}</MAC-SEC-KAY-CONFIG>")


def _full_inner() -> str:
    return (
        "<DESTINATION-MAC-ADDRESS>00-11-22-33-44-55</DESTINATION-MAC-ADDRESS>"
        "<GLOBAL-KAY-PROPS-REF DEST='MAC-SEC-GLOBAL-KAY-PROPS'>/Sec/MacSecGlobalKay</GLOBAL-KAY-PROPS-REF>"
        "<KEY-SERVER-PRIORITY>16</KEY-SERVER-PRIORITY>"
        "<MKA-PARTICIPANT-REFS>"
        "<MKA-PARTICIPANT-REF DEST='MAC-SEC-KAY-PARTICIPANT'>/Sec/MkaParticipant1</MKA-PARTICIPANT-REF>"
        "<MKA-PARTICIPANT-REF DEST='MAC-SEC-KAY-PARTICIPANT'>/Sec/MkaParticipant2</MKA-PARTICIPANT-REF>"
        "</MKA-PARTICIPANT-REFS>"
        "<ROLE>KEY-SERVER</ROLE>"
        "<SOURCE-MAC-ADDRESS>AA-BB-CC-DD-EE-FF</SOURCE-MAC-ADDRESS>"
    )


class TestReadMacSecLocalKayProps:
    def test_read_arobject_base_level(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip_with_attrs("S='chk-1' T='2009-07-23T13:38:00Z'", "")
        props = MacSecLocalKayProps()
        parser.readMacSecLocalKayProps(element, props)

        assert props.getChecksum().getValue() == "chk-1"
        assert props.getTimestamp().getValue() == "2009-07-23T13:38:00Z"
        assert props.getDestinationMacAddress() is None

    def test_read_all_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        props = MacSecLocalKayProps()
        parser.readMacSecLocalKayProps(element, props)

        assert props.getDestinationMacAddress().getValue() == "00-11-22-33-44-55"
        assert props.getGlobalKayPropsRef().getValue() == "/Sec/MacSecGlobalKay"
        assert props.getKeyServerPriority().getValue() == 16
        assert [r.getValue() for r in props.getMkaParticipantRefs()] == ["/Sec/MkaParticipant1", "/Sec/MkaParticipant2"]
        assert props.getRole().getValue() == "KEY-SERVER"
        assert props.getSourceMacAddress().getValue() == "AA-BB-CC-DD-EE-FF"

    def test_read_partial_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<DESTINATION-MAC-ADDRESS>00-11-22-33-44-55</DESTINATION-MAC-ADDRESS><SOURCE-MAC-ADDRESS>AA-BB-CC-DD-EE-FF</SOURCE-MAC-ADDRESS>")
        props = MacSecLocalKayProps()
        parser.readMacSecLocalKayProps(element, props)

        assert props.getDestinationMacAddress().getValue() == "00-11-22-33-44-55"
        assert props.getSourceMacAddress().getValue() == "AA-BB-CC-DD-EE-FF"
        assert props.getGlobalKayPropsRef() is None
        assert props.getKeyServerPriority() is None
        assert props.getMkaParticipantRefs() == []
        assert props.getRole() is None

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("")
        props = MacSecLocalKayProps()
        parser.readMacSecLocalKayProps(element, props)

        assert props.getDestinationMacAddress() is None
        assert props.getGlobalKayPropsRef() is None
        assert props.getKeyServerPriority() is None
        assert props.getMkaParticipantRefs() == []
        assert props.getRole() is None
        assert props.getSourceMacAddress() is None

    def test_read_empty_wrapper_list(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<MKA-PARTICIPANT-REFS/>")
        props = MacSecLocalKayProps()
        parser.readMacSecLocalKayProps(element, props)

        assert props.getMkaParticipantRefs() == []

    def test_get_mac_sec_local_kay_props_helper(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        props = parser.getMacSecLocalKayProps(element)

        assert props is not None
        assert props.getDestinationMacAddress().getValue() == "00-11-22-33-44-55"
        assert props.getKeyServerPriority().getValue() == 16
        assert props.getRole().getValue() == "KEY-SERVER"

    def test_get_helper_none_element(self):
        parser = ARXMLParser(options={"warning": True})

        assert parser.getMacSecLocalKayProps(None) is None


class TestMacSecPropsMacSecKayConfigDispatch:
    def test_read_mac_sec_props_dispatches_kay_config(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring("<MAC-SEC-PROPS xmlns='%s'>" "<MAC-SEC-KAY-CONFIG S='kay-chk'>%s</MAC-SEC-KAY-CONFIG>" "</MAC-SEC-PROPS>" % (NS, _full_inner()))
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecProps

        props = MacSecProps()
        parser.readMacSecProps(element, props)

        kay = props.getMacSecKayConfig()
        assert kay is not None
        assert kay.getDestinationMacAddress().getValue() == "00-11-22-33-44-55"
        assert kay.getGlobalKayPropsRef().getValue() == "/Sec/MacSecGlobalKay"
        assert kay.getKeyServerPriority().getValue() == 16
        assert [r.getValue() for r in kay.getMkaParticipantRefs()] == ["/Sec/MkaParticipant1", "/Sec/MkaParticipant2"]
        assert kay.getRole().getValue() == "KEY-SERVER"
        assert kay.getSourceMacAddress().getValue() == "AA-BB-CC-DD-EE-FF"

    def test_read_mac_sec_props_kay_config_base_level(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring(
            "<MAC-SEC-PROPS xmlns='%s'>" "<MAC-SEC-KAY-CONFIG S='kay-chk' T='2009-07-23T13:38:00Z'><KEY-SERVER-PRIORITY>16</KEY-SERVER-PRIORITY></MAC-SEC-KAY-CONFIG>" "</MAC-SEC-PROPS>" % NS
        )
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecProps

        props = MacSecProps()
        parser.readMacSecProps(element, props)

        kay = props.getMacSecKayConfig()
        assert kay is not None
        assert kay.getChecksum().getValue() == "kay-chk"
        assert kay.getTimestamp().getValue() == "2009-07-23T13:38:00Z"

    def test_read_mac_sec_props_without_kay_config(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring("<MAC-SEC-PROPS xmlns='%s'><AUTO-START>true</AUTO-START></MAC-SEC-PROPS>" % NS)
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecProps

        props = MacSecProps()
        parser.readMacSecProps(element, props)

        assert props.getMacSecKayConfig() is None

    def test_role_enum_type(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<ROLE>PEER</ROLE>")
        props = MacSecLocalKayProps()
        parser.readMacSecLocalKayProps(element, props)

        assert isinstance(props.getRole(), MacSecRoleEnum)
        assert props.getRole().getValue() == MacSecRoleEnum.PEER
