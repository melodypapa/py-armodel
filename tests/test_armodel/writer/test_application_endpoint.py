"""Writer/reader round-trip tests for ApplicationEndpoint (Table 6.124, p.458)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import GenericTp
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import SocketAddress
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
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _pos_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _string(value):
    s = String()
    s.setValue(value)
    return s


def _full_address():
    address = SocketAddress(MockParent(), "SA1")
    end_point = address.createApplicationEndpoint("AEP1")
    consumed = end_point.createConsumedServiceInstance("CSI1")
    consumed.setServiceIdentifier(_pos_int("50"))
    end_point.setMaxNumberOfConnections(_pos_int("10"))
    end_point.setNetworkEndpointRef(_ref("NETWORK-ENDPOINT", "/Ether/NetworkEndpoint/NE1"))
    end_point.setPriority(_pos_int("4"))
    provided = end_point.createProvidedServiceInstance("PSI1")
    provided.setServiceIdentifier(_pos_int("60"))
    end_point.setTlsCryptoMappingRef(_ref("TLS-CRYPTO-SERVICE-MAPPING", "/Ether/TlsCryptoServiceMapping/TCSM1"))
    tp_config = GenericTp()
    tp_config.setTpAddress(_string("10.0.0.1"))
    tp_config.setTpTechnology(_string("someip"))
    end_point.setTpConfiguration(tp_config)
    return address


class TestWriteApplicationEndpoint:
    def test_write_all_fields(self, writer):
        parent = ET.Element("SOCKET-ADDRESS")
        writer.writeSocketAddressApplicationEndpoint(parent, _full_address())

        el = parent.find("APPLICATION-ENDPOINT")
        assert el is not None
        assert el.find("SHORT-NAME").text == "AEP1"
        csi = el.find("CONSUMED-SERVICE-INSTANCES/CONSUMED-SERVICE-INSTANCE")
        assert csi is not None
        assert csi.find("SHORT-NAME").text == "CSI1"
        assert csi.find("SERVICE-IDENTIFIER").text == "50"
        assert el.find("MAX-NUMBER-OF-CONNECTIONS").text == "10"
        assert el.find("NETWORK-ENDPOINT-REF").text == "/Ether/NetworkEndpoint/NE1"
        assert el.find("PRIORITY").text == "4"
        psi = el.find("PROVIDED-SERVICE-INSTANCES/PROVIDED-SERVICE-INSTANCE")
        assert psi is not None
        assert psi.find("SHORT-NAME").text == "PSI1"
        assert psi.find("SERVICE-IDENTIFIER").text == "60"
        assert el.find("TLS-CRYPTO-MAPPING-REF").text == "/Ether/TlsCryptoServiceMapping/TCSM1"
        tp = el.find("TP-CONFIGURATION/GENERIC-TP")
        assert tp is not None
        assert tp.find("TP-ADDRESS").text == "10.0.0.1"
        assert tp.find("TP-TECHNOLOGY").text == "someip"

    def test_write_empty_fields_omits_optional_tags(self, writer):
        address = SocketAddress(MockParent(), "SA1")
        address.createApplicationEndpoint("EmptyEndpoint")
        parent = ET.Element("SOCKET-ADDRESS")
        writer.writeSocketAddressApplicationEndpoint(parent, address)

        el = parent.find("APPLICATION-ENDPOINT")
        assert el is not None
        assert el.find("CONSUMED-SERVICE-INSTANCES") is None
        assert el.find("MAX-NUMBER-OF-CONNECTIONS") is None
        assert el.find("NETWORK-ENDPOINT-REF") is None
        assert el.find("PRIORITY") is None
        assert el.find("PROVIDED-SERVICE-INSTANCES") is None
        assert el.find("TLS-CRYPTO-MAPPING-REF") is None
        assert el.find("TP-CONFIGURATION") is None


class TestApplicationEndpointRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        address = _full_address()

        parent = ET.Element("SOCKET-ADDRESS")
        writer.writeSocketAddressApplicationEndpoint(parent, address)

        out_file = str(tmp_path / "application_endpoint.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        recovered_address = SocketAddress(MockParent(), "SA1")
        tree = ET.parse(out_file)
        parser.readSocketAddressApplicationEndpoint(tree.getroot()[0], recovered_address)

        recovered = recovered_address.getApplicationEndpoint()
        assert recovered is not None
        assert recovered.getShortName() == "AEP1"
        instances = recovered.getConsumedServiceInstances()
        assert len(instances) == 1
        assert instances[0].getShortName() == "CSI1"
        assert instances[0].getServiceIdentifier().getValue() == 50
        assert recovered.getMaxNumberOfConnections().getValue() == 10
        assert recovered.getNetworkEndpointRef().getValue() == "/Ether/NetworkEndpoint/NE1"
        assert recovered.getPriority().getValue() == 4
        provided_instances = recovered.getProvidedServiceInstances()
        assert len(provided_instances) == 1
        assert provided_instances[0].getShortName() == "PSI1"
        assert provided_instances[0].getServiceIdentifier().getValue() == 60
        assert recovered.getTlsCryptoMappingRef().getValue() == "/Ether/TlsCryptoServiceMapping/TCSM1"
        tp_config = recovered.getTpConfiguration()
        assert isinstance(tp_config, GenericTp)
        assert tp_config.getTpAddress().getValue() == "10.0.0.1"
        assert tp_config.getTpTechnology().getValue() == "someip"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring(f"<SOCKET-ADDRESS xmlns='{NS}'><APPLICATION-ENDPOINT><SHORT-NAME>AEP1</SHORT-NAME></APPLICATION-ENDPOINT></SOCKET-ADDRESS>")

        recovered_address = SocketAddress(MockParent(), "SA1")
        parser.readSocketAddressApplicationEndpoint(element, recovered_address)

        recovered = recovered_address.getApplicationEndpoint()
        assert recovered is not None
        assert recovered.getShortName() == "AEP1"
        assert recovered.getConsumedServiceInstances() == []
        assert recovered.getMaxNumberOfConnections() is None
        assert recovered.getNetworkEndpointRef() is None
        assert recovered.getPriority() is None
        assert recovered.getProvidedServiceInstances() == []
        assert recovered.getTlsCryptoMappingRef() is None
        assert recovered.getTpConfiguration() is None


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")
