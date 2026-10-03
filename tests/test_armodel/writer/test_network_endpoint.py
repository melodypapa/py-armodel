"""Writer round-trip tests for NetworkEndpoint (Table 6.134, p.463)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String
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
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _pkg():
    return AUTOSAR.getInstance().createARPackage("Pkg")


def _endpoint():
    from armodel.models import NetworkEndpoint

    return NetworkEndpoint(_pkg(), "Ep")


class TestNetworkEndpointWriter:
    def test_write_fully_qualified_domain_name_value(self, writer):
        ep = _endpoint()
        ep.setFullyQualifiedDomainName(String().setValue("some.example.host"))
        parent = _parent()
        writer.writeNetworkEndPoint(parent, ep)
        ne = parent.find("NETWORK-ENDPOINT")
        assert ne is not None
        fqdn = ne.find("FULLY-QUALIFIED-DOMAIN-NAME")
        assert fqdn is not None
        assert fqdn.text == "some.example.host"

    def test_write_absent_optional_attributes_emit_nothing(self, writer):
        ep = _endpoint()
        parent = _parent()
        writer.writeNetworkEndPoint(parent, ep)
        ne = parent.find("NETWORK-ENDPOINT")
        assert ne.find("FULLY-QUALIFIED-DOMAIN-NAME") is None
        assert ne.find("INFRASTRUCTURE-SERVICES") is None
        assert ne.find("IP-SEC-CONFIG") is None
        assert ne.find("NETWORK-ENDPOINT-ADDRESSES") is None
        assert ne.find("PRIORITY") is None

    def test_round_trip_preserves_field_values(self, writer):
        ep = _endpoint()
        ep.setFullyQualifiedDomainName(String().setValue("host.example.com"))
        ep.setPriority(PositiveInteger().setValue("4"))
        parent = _parent()
        writer.writeNetworkEndPoint(parent, ep)
        xml = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(xml.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        ne = root.find("{%s}NETWORK-ENDPOINT" % NS)

        reloaded = _endpoint()
        ARXMLParser().readNetworkEndPoint(ne, reloaded)
        assert reloaded.getFullyQualifiedDomainName() is not None
        assert reloaded.getFullyQualifiedDomainName().getValue() == "host.example.com"
        assert reloaded.getPriority() is not None
        assert reloaded.getPriority().getValue() == 4
