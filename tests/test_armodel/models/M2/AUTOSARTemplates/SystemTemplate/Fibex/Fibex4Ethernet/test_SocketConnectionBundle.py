import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    SocketConnectionBundle,
    SocketConnectionIpduIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel import SocketConnection
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    UdpChecksumCalculationEnum,
)

CLASS_NOTE = """This elements groups SocketConnections, i.e. specifies socket connections belonging to the bundle and describes properties which are common for all socket connections in the bundle."""


class TestSocketConnectionBundle:
    """Test cases for SocketConnectionBundle (R4.3.1 Table 6.118, p.316)."""

    def _obj(self):
        return SocketConnectionBundle(None, "Bundle")

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getBundledConnections() == []
        assert obj.getDifferentiatedServiceField() is None
        assert obj.getFlowLabel() is None
        assert obj.getPathMtuDiscoveryEnabled() is None
        assert obj.getPdus() == []
        assert obj.getServerPortRef() is None
        assert obj.getUdpChecksumHandling() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()
        connection = SocketConnection()
        assert obj.addBundledConnection(connection) is obj
        assert obj.getBundledConnections() == [connection]
        obj.addBundledConnection(None)
        assert obj.getBundledConnections() == [connection]

        service_field = PositiveInteger()
        service_field.setValue(3)
        assert obj.setDifferentiatedServiceField(service_field) is obj
        assert obj.getDifferentiatedServiceField() is service_field
        obj.setDifferentiatedServiceField(None)
        assert obj.getDifferentiatedServiceField() is service_field

        flow_label = PositiveInteger()
        flow_label.setValue(100)
        assert obj.setFlowLabel(flow_label) is obj
        assert obj.getFlowLabel() is flow_label
        obj.setFlowLabel(None)
        assert obj.getFlowLabel() is flow_label

        flag = Boolean()
        flag.setValue(True)
        assert obj.setPathMtuDiscoveryEnabled(flag) is obj
        assert obj.getPathMtuDiscoveryEnabled() is flag
        obj.setPathMtuDiscoveryEnabled(None)
        assert obj.getPathMtuDiscoveryEnabled() is flag

        identifier = SocketConnectionIpduIdentifier()
        assert obj.addPdu(identifier) is obj
        assert obj.getPdus() == [identifier]
        obj.addPdu(None)
        assert obj.getPdus() == [identifier]

        ref = RefType()
        ref.value = "/socket"
        assert obj.setServerPortRef(ref) is obj
        assert obj.getServerPortRef() is ref
        obj.setServerPortRef(None)
        assert obj.getServerPortRef() is ref

        checksum = UdpChecksumCalculationEnum()
        checksum.setValue(UdpChecksumCalculationEnum.UDP_CHECKSUM_ENABLED)
        assert obj.setUdpChecksumHandling(checksum) is obj
        assert obj.getUdpChecksumHandling() is checksum
        obj.setUdpChecksumHandling(None)
        assert obj.getUdpChecksumHandling() is checksum

    def test_variation_point_capable_mixin(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint

        obj = self._obj()
        assert isinstance(obj, VariationPointCapable)
        assert obj.getVariationPoint() is None
        point = VariationPoint()
        assert obj.setVariationPoint(point) is obj
        assert obj.getVariationPoint() is point
        obj.setVariationPoint(None)
        assert obj.getVariationPoint() is point

    def test_list_pairs_are_mutator_first_in_source(self):
        source = inspect.getsource(SocketConnectionBundle)
        assert source.index("def addBundledConnection") < source.index("def getBundledConnections")
        assert source.index("def addPdu") < source.index("def getPdus")

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SocketConnectionBundle.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()

        assert inspect.cleandoc(obj.getBundledConnections.__doc__) == "Collection of SocketConnections in the connectionGroup."
        assert (
            inspect.cleandoc(obj.getDifferentiatedServiceField.__doc__)
            == "The 6-bit Differentiated Service Field in the IP headers may be used for classifying network traffic. If not set a value of zero is used to indicate packets that have not been classified."
        )
        assert (
            inspect.cleandoc(obj.getFlowLabel.__doc__)
            == "The 20-bit Flow Label field in the IPv6 header may be used by a source to label sequences of packets for which it requests special handling by the IPv6 routers, such as non-default quality of service. If not set a Flow Label of zero is used to indicate packets that have not been labeled."
        )
        assert inspect.cleandoc(obj.getPathMtuDiscoveryEnabled.__doc__) == "Defines whether the Path MTU Discovery shall be performed for the related socket."
        assert (
            inspect.cleandoc(obj.getPdus.__doc__)
            == "With this aggregation SocketConnectionIpduIdentifier elements are assigned to all SocketConnections that are available in this SocketConnetionBundle."
        )
        assert (
            inspect.cleandoc(obj.getServerPortRef.__doc__)
            == "Server Port for TCP/UDP connection in an abstract communication sense. The server is the major provider of the communication. Please note that the server may also consume data."
        )
        assert (
            inspect.cleandoc(obj.getUdpChecksumHandling.__doc__)
            == "Specifies if UDP checksum handling shall be enabled (udpChecksumEnabled) or skipped (udpChecksumDisabled) on the related socket connection."
        )
