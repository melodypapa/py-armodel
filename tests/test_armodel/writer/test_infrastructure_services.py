"""Writer/reader round-trip tests for InfrastructureServices (Table 6.144, p.469)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    DoIpEntity,
    InfrastructureServices,
    TimeSynchronization,
)
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


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")


class TestWriteInfrastructureServices:
    def test_write_all_fields(self, writer):
        services = InfrastructureServices()
        services.setDoIpEntity(DoIpEntity())
        sync = TimeSynchronization()
        services.setTimeSynchronization(sync)

        parent = ET.Element("NETWORK-ENDPOINT")
        writer.setInfrastructureServices(parent, "INFRASTRUCTURE-SERVICES", services)
        node = parent.find("INFRASTRUCTURE-SERVICES")
        assert node is not None
        assert node.find("DO-IP-ENTITY") is not None
        assert node.find("TIME-SYNCHRONIZATION") is not None

    def test_removed_dhcp_server_configuration_not_written(self, writer):
        """dhcpServerConfiguration is atp.Status=removed since 4.3.1, absent from Table 6.144 (Rule 0015)."""
        services = InfrastructureServices()
        parent = ET.Element("NETWORK-ENDPOINT")
        writer.setInfrastructureServices(parent, "INFRASTRUCTURE-SERVICES", services)
        node = parent.find("INFRASTRUCTURE-SERVICES")
        assert node.find("DHCP-SERVER-CONFIGURATION") is None


class TestInfrastructureServicesRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        services = InfrastructureServices()
        services.setDoIpEntity(DoIpEntity())
        services.setTimeSynchronization(TimeSynchronization())

        parent = ET.Element("NETWORK-ENDPOINT")
        writer.setInfrastructureServices(parent, "INFRASTRUCTURE-SERVICES", services)
        element = _wrap(parent)[0]
        parsed = parser.getInfrastructureServices(element, "INFRASTRUCTURE-SERVICES")

        assert isinstance(parsed, InfrastructureServices)
        assert isinstance(parsed.getDoIpEntity(), DoIpEntity)
        assert isinstance(parsed.getTimeSynchronization(), TimeSynchronization)

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<NETWORK-ENDPOINT xmlns='%s'></NETWORK-ENDPOINT>" % NS)
        parsed = parser.getInfrastructureServices(element, "INFRASTRUCTURE-SERVICES")
        assert parsed is None
