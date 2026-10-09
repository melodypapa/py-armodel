"""Writer round-trip tests for SecureCommunicationAuthenticationProps (Table 6.47, p.371).

Serialized through writeSecureCommunicationAuthenticationProps (emitted by the
SecureCommunicationPropsSet AUTHENTICATION-PROPSS dispatch); the
SECURE-COMMUNICATION-AUTHENTICATION-PROPS group of AUTOSAR_00052.xsd (l.102877)
holds AUTH-INFO-TX-LENGTH (POSITIVE-INTEGER, 0..1); the group's AUTH-ALGORITHM
element carries atp.Status="removed" (4.4.0) and is not modeled. The tests
exercise writeSecureCommunicationAuthenticationProps, which must call
writeIdentifiable for the base level (UUID/CATEGORY/S/T) and emit the attribute
in XSD sequence order, plus the empty-props case (SHORT-NAME only).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationAuthenticationProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "AUTH-INFO-TX-LENGTH",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<WRAP>", "<WRAP xmlns='%s'>" % NS, 1))


def _write(props: SecureCommunicationAuthenticationProps) -> ET.Element:
    parent = ET.Element("WRAP")
    ARXMLWriter().writeSecureCommunicationAuthenticationProps(parent, props)
    return parent


def _populate(props: SecureCommunicationAuthenticationProps):
    tx_length = PositiveInteger()
    tx_length.setValue("24")
    props.setAuthInfoTxLength(tx_length)


class TestWriteSecureCommunicationAuthenticationProps:
    def test_write_empty(self):
        node = _write(SecureCommunicationAuthenticationProps(None, "auth1")).find("SECURE-COMMUNICATION-AUTHENTICATION-PROPS")

        assert [child.tag for child in node] == ["SHORT-NAME"]
        for tag in XSD_CHILD_ORDER:
            assert node.find(tag) is None

    def test_write_child_order_matches_xsd(self):
        props = SecureCommunicationAuthenticationProps(None, "auth1")
        _populate(props)

        node = _write(props).find("SECURE-COMMUNICATION-AUTHENTICATION-PROPS")
        assert [child.tag for child in node] == ["SHORT-NAME"] + XSD_CHILD_ORDER

    def test_write_full_field_values(self):
        props = SecureCommunicationAuthenticationProps(None, "auth1")
        _populate(props)

        node = _write(props).find("SECURE-COMMUNICATION-AUTHENTICATION-PROPS")
        assert node.find("AUTH-INFO-TX-LENGTH").text == "24"

    def test_round_trip_full(self):
        props = SecureCommunicationAuthenticationProps(None, "auth1")
        _populate(props)

        node = _with_ns(_write(props)).find("{%s}SECURE-COMMUNICATION-AUTHENTICATION-PROPS" % NS)
        reloaded = SecureCommunicationAuthenticationProps(None, "auth1")
        ARXMLParser().readSecureCommunicationAuthenticationProps(node, reloaded)

        assert reloaded.getShortName() == "auth1"
        assert reloaded.getAuthInfoTxLength().getValue() == 24

    def test_round_trip_base_level_attributes(self):
        props = SecureCommunicationAuthenticationProps(None, "auth1")
        props.setChecksum(String().setValue("7"))
        props.setTimestamp(DateTime().setValue("2023-01-01T00:00:00+01:00"))
        props.setUuid(String().setValue("DCE:2fac1234-31f8-11b4-a222-08002b34c003"))
        props.setCategory("DOIP")

        node = _with_ns(_write(props)).find("{%s}SECURE-COMMUNICATION-AUTHENTICATION-PROPS" % NS)
        assert node.attrib["S"] == "7"
        assert node.attrib["T"] == "2023-01-01T00:00:00+01:00"
        assert node.attrib["UUID"] == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        assert node.find("{%s}CATEGORY" % NS).text == "DOIP"

        reloaded = SecureCommunicationAuthenticationProps(None, "auth1")
        ARXMLParser().readSecureCommunicationAuthenticationProps(node, reloaded)
        assert reloaded.getChecksum().getValue() == "7"
        assert reloaded.getTimestamp().getValue() == "2023-01-01T00:00:00+01:00"
        assert reloaded.getUuid().getValue() == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        assert reloaded.getCategory().getValue() == "DOIP"
