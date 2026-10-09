"""Writer round-trip tests for SecureCommunicationPropsSet (Table 6.45, p.370).

Serialized through writeSecureCommunicationPropsSet (emitted by the ARPackage
dispatch); the SECURE-COMMUNICATION-PROPS-SET group of AUTOSAR_00052.xsd
(l.103127) holds two wrapper lists in sequence order -- AUTHENTICATION-PROPSS
(unbounded choice of SECURE-COMMUNICATION-AUTHENTICATION-PROPS) and
FRESHNESS-PROPSS (unbounded choice of SECURE-COMMUNICATION-FRESHNESS-PROPS);
the SECURE-COMMUNICATION-PROPS-SET complexType (l.103159) stacks the base groups
in front of it. The tests exercise writeSecureCommunicationPropsSet, which must
call writeIdentifiable for the base level (UUID/CATEGORY/S/T), emit the wrapper
lists in XSD sequence order (wrapper only when non-empty), plus the empty
props-set case (no wrapper elements).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationPropsSet
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = ["AUTHENTICATION-PROPSS", "FRESHNESS-PROPSS"]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<WRAP>", "<WRAP xmlns='%s'>" % NS, 1))


def _write(props_set: SecureCommunicationPropsSet) -> ET.Element:
    parent = ET.Element("WRAP")
    ARXMLWriter().writeSecureCommunicationPropsSet(parent, props_set)
    return parent


def _populate(props_set: SecureCommunicationPropsSet):
    auth1 = props_set.createSecureCommunicationAuthenticationProps("auth1")
    length = PositiveInteger()
    length.setValue("24")
    auth1.setAuthInfoTxLength(length)

    auth2 = props_set.createSecureCommunicationAuthenticationProps("auth2")
    length = PositiveInteger()
    length.setValue("28")
    auth2.setAuthInfoTxLength(length)

    fresh1 = props_set.createSecureCommunicationFreshnessProps("fresh1")
    length = PositiveInteger()
    length.setValue("64")
    fresh1.setFreshnessValueLength(length)


class TestWriteSecureCommunicationPropsSet:
    def test_write_empty_wrapper_lists(self):
        node = _write(SecureCommunicationPropsSet(None, "PropsSet")).find("SECURE-COMMUNICATION-PROPS-SET")

        assert [child.tag for child in node] == ["SHORT-NAME"]
        assert node.find("AUTHENTICATION-PROPSS") is None
        assert node.find("FRESHNESS-PROPSS") is None

    def test_write_child_order_matches_xsd(self):
        props_set = SecureCommunicationPropsSet(None, "PropsSet")
        _populate(props_set)

        node = _write(props_set).find("SECURE-COMMUNICATION-PROPS-SET")
        assert [child.tag for child in node] == ["SHORT-NAME"] + XSD_CHILD_ORDER
        assert [child.tag for child in node.find("AUTHENTICATION-PROPSS")] == ["SECURE-COMMUNICATION-AUTHENTICATION-PROPS", "SECURE-COMMUNICATION-AUTHENTICATION-PROPS"]
        assert [child.tag for child in node.find("FRESHNESS-PROPSS")] == ["SECURE-COMMUNICATION-FRESHNESS-PROPS"]

    def test_write_full_field_values(self):
        props_set = SecureCommunicationPropsSet(None, "PropsSet")
        _populate(props_set)

        node = _write(props_set).find("SECURE-COMMUNICATION-PROPS-SET")
        auth_nodes = node.find("AUTHENTICATION-PROPSS").findall("SECURE-COMMUNICATION-AUTHENTICATION-PROPS")
        assert auth_nodes[0].find("AUTH-INFO-TX-LENGTH").text == "24"
        assert auth_nodes[1].find("AUTH-INFO-TX-LENGTH").text == "28"
        fresh_node = node.find("FRESHNESS-PROPSS").find("SECURE-COMMUNICATION-FRESHNESS-PROPS")
        assert fresh_node.find("FRESHNESS-VALUE-LENGTH").text == "64"

    def test_round_trip_full(self):
        props_set = SecureCommunicationPropsSet(None, "PropsSet")
        _populate(props_set)

        node = _with_ns(_write(props_set)).find("{%s}SECURE-COMMUNICATION-PROPS-SET" % NS)
        reloaded = SecureCommunicationPropsSet(None, "PropsSet")
        ARXMLParser().readSecureCommunicationPropsSet(node, reloaded)

        auth_props = reloaded.getAuthenticationProps()
        assert [props.getShortName() for props in auth_props] == ["auth1", "auth2"]
        assert auth_props[0].getAuthInfoTxLength().getValue() == 24
        assert auth_props[1].getAuthInfoTxLength().getValue() == 28

        freshness_props = reloaded.getFreshnessProps()
        assert [props.getShortName() for props in freshness_props] == ["fresh1"]
        assert freshness_props[0].getFreshnessValueLength().getValue() == 64

    def test_round_trip_base_level_attributes(self):
        props_set = SecureCommunicationPropsSet(None, "PropsSet")
        props_set.setUuid(String().setValue("DCE:2fac1234-31f8-11b4-a222-08002b34c003"))
        props_set.setCategory("DOIP")

        node = _with_ns(_write(props_set)).find("{%s}SECURE-COMMUNICATION-PROPS-SET" % NS)
        assert node.attrib["UUID"] == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        assert node.find("{%s}CATEGORY" % NS).text == "DOIP"

        reloaded = SecureCommunicationPropsSet(None, "PropsSet")
        ARXMLParser().readSecureCommunicationPropsSet(node, reloaded)
        assert reloaded.getUuid().getValue() == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        assert reloaded.getCategory().getValue() == "DOIP"
