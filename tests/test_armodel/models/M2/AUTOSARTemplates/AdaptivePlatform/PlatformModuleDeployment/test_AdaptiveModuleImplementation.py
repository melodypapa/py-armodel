import pytest

from armodel import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.AdaptiveModuleImplementation import (
    PlatformModuleEndpointConfiguration,
    PlatformModuleEthernetEndpointConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    Ip6AddressString,
    RefType,
)

ENDPOINT_CONFIG_NOTE = "This meta-class defines the abstract attributes for the configuration of a " "network for a specific CommunicationConnector."
ETHERNET_ENDPOINT_CONFIG_NOTE = (
    "This meta-class defines the attributes for the configuration of a port, "
    "protocol type and IP address of the communication on a VLAN. "
    "Tags: atp.recommendedPackage=PlatformModuleEndpointConfigurations"
)
COMMUNICATION_CONNECTOR_NOTE = "Reference to the CommunicationConnector (VLAN) for which the network " "configuration is defined."
IPV4_NOTE = "Multicast IPv4 Address to which the message will be transmitted."
IPV6_NOTE = "Multicast IPv6 Address to which the message will be transmitted."


def _new_configuration(short_name: str) -> PlatformModuleEthernetEndpointConfiguration:
    document = AUTOSAR.getInstance()
    ar_root = document.createARPackage("AUTOSAR")
    return PlatformModuleEthernetEndpointConfiguration(ar_root, short_name)


class TestPlatformModuleEndpointConfiguration:
    def test_abstract_class_cannot_be_instantiated(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")

        with pytest.raises(TypeError) as err:
            _obj = PlatformModuleEndpointConfiguration(ar_root, "test_platformmoduleendpointconfiguration")
        assert str(err.value) == "PlatformModuleEndpointConfiguration is an abstract class."

    def test_class_docstring_is_spec_note(self):
        assert PlatformModuleEndpointConfiguration.__doc__.strip() == ENDPOINT_CONFIG_NOTE

    def test_init_has_no_docstring(self):
        assert PlatformModuleEndpointConfiguration.__init__.__doc__ is None


class TestPlatformModuleEthernetEndpointConfiguration:
    def test_subclass_relationships(self):
        assert issubclass(PlatformModuleEthernetEndpointConfiguration, PlatformModuleEndpointConfiguration)
        assert issubclass(PlatformModuleEthernetEndpointConfiguration, ARElement)

    def test_initialization(self):
        config = _new_configuration("test_platformmoduleethernetendpointconfiguration")

        assert config.short_name == "test_platformmoduleethernetendpointconfiguration"
        assert config.getCommunicationConnectorRef() is None
        assert config.getIpv4MulticastIpAddress() is None
        assert config.getIpv6MulticastIpAddress() is None

    def test_class_docstring_is_spec_note(self):
        assert PlatformModuleEthernetEndpointConfiguration.__doc__.strip() == ETHERNET_ENDPOINT_CONFIG_NOTE

    def test_init_has_no_docstring(self):
        assert PlatformModuleEthernetEndpointConfiguration.__init__.__doc__ is None

    def test_communication_connector_ref_round_trip(self):
        config = _new_configuration("test_platformmoduleethernetendpointconfiguration")
        ref = RefType()
        ref.setDest("ETHERNET-COMMUNICATION-CONNECTOR")
        ref.setValue("/AUTOSAR/EcuComp/EcuInst/CN_VLAN_2")

        assert config.setCommunicationConnectorRef(ref) is config
        assert config.getCommunicationConnectorRef() is ref
        assert config.setCommunicationConnectorRef(None) is config
        assert config.getCommunicationConnectorRef() is ref

    def test_communication_connector_accessor_docstrings(self):
        config = _new_configuration("test_platformmoduleethernetendpointconfiguration")
        assert config.getCommunicationConnectorRef.__doc__.strip().splitlines()[0] == COMMUNICATION_CONNECTOR_NOTE
        assert config.setCommunicationConnectorRef.__doc__.strip().splitlines()[0] == COMMUNICATION_CONNECTOR_NOTE

    def test_ipv4_multicast_ip_address_round_trip(self):
        config = _new_configuration("test_platformmoduleethernetendpointconfiguration")
        value = Ip4AddressString().setValue("239.255.0.1")

        assert config.setIpv4MulticastIpAddress(value) is config
        assert config.getIpv4MulticastIpAddress() is value
        assert config.getIpv4MulticastIpAddress().getValue() == "239.255.0.1"
        assert config.setIpv4MulticastIpAddress(None) is config
        assert config.getIpv4MulticastIpAddress() is value

    def test_ipv4_accessor_docstrings(self):
        config = _new_configuration("test_platformmoduleethernetendpointconfiguration")
        assert config.getIpv4MulticastIpAddress.__doc__.strip().splitlines()[0] == IPV4_NOTE
        assert config.setIpv4MulticastIpAddress.__doc__.strip().splitlines()[0] == IPV4_NOTE

    def test_ipv6_multicast_ip_address_round_trip(self):
        config = _new_configuration("test_platformmoduleethernetendpointconfiguration")
        value = Ip6AddressString().setValue("ff02::1")

        assert config.setIpv6MulticastIpAddress(value) is config
        assert config.getIpv6MulticastIpAddress() is value
        assert config.getIpv6MulticastIpAddress().getValue() == "ff02::1"
        assert config.setIpv6MulticastIpAddress(None) is config
        assert config.getIpv6MulticastIpAddress() is value

    def test_ipv6_accessor_docstrings(self):
        config = _new_configuration("test_platformmoduleethernetendpointconfiguration")
        assert config.getIpv6MulticastIpAddress.__doc__.strip().splitlines()[0] == IPV6_NOTE
        assert config.setIpv6MulticastIpAddress.__doc__.strip().splitlines()[0] == IPV6_NOTE
