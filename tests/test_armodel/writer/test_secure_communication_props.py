"""Writer round-trip tests for SecureCommunicationProps (Table 6.44, p.369).

Serialized through setSecureCommunicationProps (emitted by writeSecuredIPdu);
the SECURE-COMMUNICATION-PROPS group of AUTOSAR_00052.xsd (l.102992) holds 11
POSITIVE-INTEGER children (minOccurs=0, maxOccurs=1); the
SECURE-COMMUNICATION-PROPS complexType (l.103114) stacks the AR-OBJECT group in
front of it and carries the AR-OBJECT attributeGroup (S/T). The tests exercise
setSecureCommunicationProps, which must call writeARObject for the base level
(S/T) and emit the own children in XSD sequence order, plus the absent-props
case (no SECURE-COMMUNICATION-PROPS element).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "AUTH-DATA-FRESHNESS-LENGTH",
    "AUTH-DATA-FRESHNESS-START-POSITION",
    "AUTHENTICATION-BUILD-ATTEMPTS",
    "AUTHENTICATION-RETRIES",
    "DATA-ID",
    "FRESHNESS-VALUE-ID",
    "MESSAGE-LINK-LENGTH",
    "MESSAGE-LINK-POSITION",
    "SECONDARY-FRESHNESS-VALUE-ID",
    "SECURED-AREA-LENGTH",
    "SECURED-AREA-OFFSET",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<WRAP>", "<WRAP xmlns='%s'>" % NS, 1))


def _write(props: SecureCommunicationProps) -> ET.Element:
    parent = ET.Element("WRAP")
    ARXMLWriter().setSecureCommunicationProps(parent, "SECURE-COMMUNICATION-PROPS", props)
    return parent


def _populate(props: SecureCommunicationProps):
    value = PositiveInteger()
    value.setValue("24")
    props.setAuthDataFreshnessLength(value)

    value = PositiveInteger()
    value.setValue("16")
    props.setAuthDataFreshnessStartPosition(value)

    value = PositiveInteger()
    value.setValue("2")
    props.setAuthenticationBuildAttempts(value)

    value = PositiveInteger()
    value.setValue("3")
    props.setAuthenticationRetries(value)

    value = PositiveInteger()
    value.setValue("42")
    props.setDataId(value)

    value = PositiveInteger()
    value.setValue("100")
    props.setFreshnessValueId(value)

    value = PositiveInteger()
    value.setValue("32")
    props.setMessageLinkLength(value)

    value = PositiveInteger()
    value.setValue("0")
    props.setMessageLinkPosition(value)

    value = PositiveInteger()
    value.setValue("200")
    props.setSecondaryFreshnessValueId(value)

    value = PositiveInteger()
    value.setValue("64")
    props.setSecuredAreaLength(value)

    value = PositiveInteger()
    value.setValue("8")
    props.setSecuredAreaOffset(value)


class TestSetSecureCommunicationProps:
    def test_write_empty(self):
        node = _write(SecureCommunicationProps()).find("SECURE-COMMUNICATION-PROPS")

        for tag in XSD_CHILD_ORDER:
            assert node.find(tag) is None, tag

    def test_write_full_child_order_matches_xsd(self):
        props = SecureCommunicationProps()
        _populate(props)

        node = _write(props).find("SECURE-COMMUNICATION-PROPS")
        tags = [child.tag for child in node]
        assert tags == XSD_CHILD_ORDER

    def test_write_full_field_values(self):
        props = SecureCommunicationProps()
        _populate(props)

        node = _write(props).find("SECURE-COMMUNICATION-PROPS")
        assert node.find("AUTH-DATA-FRESHNESS-LENGTH").text == "24"
        assert node.find("AUTH-DATA-FRESHNESS-START-POSITION").text == "16"
        assert node.find("AUTHENTICATION-BUILD-ATTEMPTS").text == "2"
        assert node.find("AUTHENTICATION-RETRIES").text == "3"
        assert node.find("DATA-ID").text == "42"
        assert node.find("FRESHNESS-VALUE-ID").text == "100"
        assert node.find("MESSAGE-LINK-LENGTH").text == "32"
        assert node.find("MESSAGE-LINK-POSITION").text == "0"
        assert node.find("SECONDARY-FRESHNESS-VALUE-ID").text == "200"
        assert node.find("SECURED-AREA-LENGTH").text == "64"
        assert node.find("SECURED-AREA-OFFSET").text == "8"

    def test_round_trip_full(self):
        props = SecureCommunicationProps()
        _populate(props)

        wrapper = _with_ns(_write(props))
        reloaded = ARXMLParser().getSecureCommunicationProps(wrapper, "SECURE-COMMUNICATION-PROPS")

        assert reloaded.getAuthDataFreshnessLength().getValue() == 24
        assert reloaded.getAuthDataFreshnessStartPosition().getValue() == 16
        assert reloaded.getAuthenticationBuildAttempts().getValue() == 2
        assert reloaded.getAuthenticationRetries().getValue() == 3
        assert reloaded.getDataId().getValue() == 42
        assert reloaded.getFreshnessValueId().getValue() == 100
        assert reloaded.getMessageLinkLength().getValue() == 32
        assert reloaded.getMessageLinkPosition().getValue() == 0
        assert reloaded.getSecondaryFreshnessValueId().getValue() == 200
        assert reloaded.getSecuredAreaLength().getValue() == 64
        assert reloaded.getSecuredAreaOffset().getValue() == 8

    def test_round_trip_base_level_attributes(self):
        props = SecureCommunicationProps()
        props.setChecksum(String().setValue("5"))
        props.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))

        wrapper = _with_ns(_write(props))
        node = wrapper.find("{%s}SECURE-COMMUNICATION-PROPS" % NS)
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

        reloaded = ARXMLParser().getSecureCommunicationProps(wrapper, "SECURE-COMMUNICATION-PROPS")
        assert reloaded.getChecksum().getValue() == "5"
        assert reloaded.getTimestamp().getValue() == "2025-04-04T00:00:00Z"

    def test_round_trip_absent_props(self):
        parent = ET.Element("WRAP")
        ARXMLWriter().setSecureCommunicationProps(parent, "SECURE-COMMUNICATION-PROPS", None)

        assert parent.find("SECURE-COMMUNICATION-PROPS") is None

        reloaded = ARXMLParser().getSecureCommunicationProps(_with_ns(parent), "SECURE-COMMUNICATION-PROPS")
        assert reloaded is None
