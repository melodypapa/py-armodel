import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    ApplicationEndpoint,
    GenericTp,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    ConsumedServiceInstance,
    ProvidedServiceInstance,
)

CLASS_NOTE = """An application endpoint is the endpoint on an Ecu in terms of application addressing (e.g. socket). The application endpoint represents e.g. the listen socket in client-server-based communication."""


class TestApplicationEndpoint:
    """Test cases for ApplicationEndpoint (Table 6.124, p.458)."""

    def _obj(self):
        return ApplicationEndpoint(None, "AEP")

    def _ref(self, value):
        ref = RefType()
        ref.setValue(value)
        return ref

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getConsumedServiceInstances() == []
        assert obj.getMaxNumberOfConnections() is None
        assert obj.getNetworkEndpointRef() is None
        assert obj.getPriority() is None
        assert obj.getProvidedServiceInstances() == []
        assert obj.getTlsCryptoMappingRef() is None
        assert obj.getTpConfiguration() is None

    def test_get_set_max_number_of_connections(self):
        obj = self._obj()
        value = PositiveInteger().setValue("10")
        assert obj.setMaxNumberOfConnections(value) is obj
        assert obj.getMaxNumberOfConnections() is value
        obj.setMaxNumberOfConnections(None)
        assert obj.getMaxNumberOfConnections() is value

    def test_get_set_network_endpoint_ref(self):
        obj = self._obj()
        value = self._ref("/Ether/NetworkEndpoint/NE1")
        assert obj.setNetworkEndpointRef(value) is obj
        assert obj.getNetworkEndpointRef() is value
        obj.setNetworkEndpointRef(None)
        assert obj.getNetworkEndpointRef() is value

    def test_get_set_priority(self):
        obj = self._obj()
        value = PositiveInteger().setValue("4")
        assert obj.setPriority(value) is obj
        assert obj.getPriority() is value
        obj.setPriority(None)
        assert obj.getPriority() is value

    def test_get_set_tls_crypto_mapping_ref(self):
        obj = self._obj()
        value = self._ref("/Ether/TlsCryptoServiceMapping/TCSM1")
        assert obj.setTlsCryptoMappingRef(value) is obj
        assert obj.getTlsCryptoMappingRef() is value
        obj.setTlsCryptoMappingRef(None)
        assert obj.getTlsCryptoMappingRef() is value

    def test_get_set_tp_configuration(self):
        obj = self._obj()
        value = GenericTp().setTpAddress(String().setValue("10.0.0.1"))
        assert obj.setTpConfiguration(value) is obj
        assert obj.getTpConfiguration() is value
        obj.setTpConfiguration(None)
        assert obj.getTpConfiguration() is value

    def test_create_consumed_service_instance(self):
        obj = self._obj()
        first = obj.createConsumedServiceInstance("CSI1")
        assert isinstance(first, ConsumedServiceInstance)
        assert first.getShortName() == "CSI1"
        assert obj.getConsumedServiceInstances() == [first]
        duplicate = obj.createConsumedServiceInstance("CSI1")
        assert duplicate is first
        assert len(obj.getConsumedServiceInstances()) == 1

    def test_create_provided_service_instance(self):
        obj = self._obj()
        first = obj.createProvidedServiceInstance("PSI1")
        assert isinstance(first, ProvidedServiceInstance)
        assert first.getShortName() == "PSI1"
        assert obj.getProvidedServiceInstances() == [first]
        duplicate = obj.createProvidedServiceInstance("PSI1")
        assert duplicate is first
        assert len(obj.getProvidedServiceInstances()) == 1

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ApplicationEndpoint.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getMaxNumberOfConnections.__doc__) == "This attribute defines the maximal number of clients the Server is able to deal with in case of Service Discovery."
        assert (
            inspect.cleandoc(obj.setMaxNumberOfConnections.__doc__).split("\n")[0]
            == "This attribute defines the maximal number of clients the Server is able to deal with in case of Service Discovery."
        )
        assert inspect.cleandoc(obj.getNetworkEndpointRef.__doc__) == "Reference to the network address."
        assert inspect.cleandoc(obj.getPriority.__doc__) == "Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed."
        assert inspect.cleandoc(obj.getProvidedServiceInstances.__doc__) == "Provided service instances. Tags: atp.Status=obsolete"
        assert (
            inspect.cleandoc(obj.getTlsCryptoMappingRef.__doc__)
            == "This reference identifies the applicable TlsCryptoServiceMapping that adds the ability for TLS-based encryption on the enclosing ApplicationEndpoint."
        )
        assert inspect.cleandoc(obj.getTpConfiguration.__doc__) == "Configuration of the used transport protocol."
