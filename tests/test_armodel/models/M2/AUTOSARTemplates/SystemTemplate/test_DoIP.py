import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import AbstractDoIpLogicAddressProps, DoIpInterface, DoIpLogicTargetAddressProps, DoIpLogicTesterAddressProps, DoIpRoutingActivation


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_DoIp:
    """Test cases for DoIP-related classes."""

    def test_AbstractDoIpLogicAddressProps(self):
        """Test AbstractDoIpLogicAddressProps abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(TypeError):
            AbstractDoIpLogicAddressProps(parent, "test_abstract")

    def test_DoIpLogicTargetAddressProps(self):
        """Test DoIpLogicTargetAddressProps class functionality."""
        parent = MockParent()
        props = DoIpLogicTargetAddressProps(parent, "test_target_addr")

        assert isinstance(props, Identifiable)
        assert isinstance(props, AbstractDoIpLogicAddressProps)

        # Test default values
        assert props.getShortName() == "test_target_addr"

    def test_DoIpLogicTesterAddressProps(self):
        """Test DoIpLogicTesterAddressProps class functionality."""
        parent = MockParent()
        props = DoIpLogicTesterAddressProps(parent, "test_tester_addr")

        assert isinstance(props, Identifiable)
        assert isinstance(props, AbstractDoIpLogicAddressProps)

        # Test default values
        assert props.getDoIpTesterRoutingActivationRef() is None

        # Test setter/getter
        mock_ref = "mock_ref"
        props.setDoIpTesterRoutingActivationRef(mock_ref)
        assert props.getDoIpTesterRoutingActivationRef() == mock_ref


@pytest.fixture(autouse=True)
def reset_autosar_for_doip_routing_activation():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class Test_DoIpRoutingActivation:
    """Test cases for DoIpRoutingActivation (Table 6.204, p.553)."""

    MEMBERS = [
        "doIpTargetAddressRefs",
    ]

    def _create(self, short_name: str) -> DoIpRoutingActivation:
        parent = AUTOSAR.getInstance().createARPackage("DoIpRoutingActivationPkg")
        return DoIpRoutingActivation(parent, short_name)

    def test_inheritance(self):
        assert issubclass(DoIpRoutingActivation, Identifiable)

    def test_class_docstring_note(self):
        expected = "This meta-class defines a DoIP routing activation possibility that activates the routing to the referenced doIPTargetAddress. This means that the diagnostic request messages related to the specified doIPTargetAddress received by socketConnections that are referenced by the same DoIpInterface that aggregates this DoIpRoutingActivation are activated."
        assert inspect.cleandoc(DoIpRoutingActivation.__doc__) == expected

    def test_initialization_defaults(self):
        activation = self._create("Activation1")
        assert activation.getShortName() == "Activation1"
        assert activation.getDoIpTargetAddressRefs() == []

    def test_member_order(self):
        activation = self._create("Activation1")
        members = [k for k in vars(activation) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_add_do_ip_target_address_ref(self):
        activation = self._create("Activation1")
        ref = RefType()
        ref.setValue("/DoIp/DoIpLogicTargetAddressProps1")
        ref.setDest("DO-IP-LOGIC-TARGET-ADDRESS-PROPS")
        result = activation.addDoIpTargetAddressRef(ref)
        assert result is activation
        assert activation.getDoIpTargetAddressRefs() == [ref]
        activation.addDoIpTargetAddressRef(None)
        assert activation.getDoIpTargetAddressRefs() == [ref]


@pytest.fixture(autouse=True)
def reset_autosar_for_doip_interface():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class Test_DoIpInterface:
    """Test cases for DoIpInterface (Table 6.203, p.552)."""

    MEMBERS = [
        "aliveCheckResponseTimeout",
        "doipChannelCollectionRef",
        "doipConnectionRefs",
        "doIpRoutingActivations",
        "generalInactivityTime",
        "initialInactivityTime",
        "initialVehicleAnnouncementTime",
        "isActivationLineDependent",
        "maxTesterConnections",
        "socketConnectionRefs",
        "useMacAddressForIdentification",
        "useVehicleIdentificationSyncStatus",
        "vehicleAnnouncementCount",
        "vehicleAnnouncementInterval",
    ]

    def _create(self, short_name: str) -> DoIpInterface:
        parent = AUTOSAR.getInstance().createARPackage("DoIpInterfacePkg")
        return DoIpInterface(parent, short_name)

    def test_inheritance(self):
        assert issubclass(DoIpInterface, Identifiable)

    def test_class_docstring_note(self):
        expected = "A logical interface over which the DoIP Node is able to communicate via DoIP independently from other existing DoIpInterfaces."
        assert inspect.cleandoc(DoIpInterface.__doc__) == expected

    def test_initialization_defaults(self):
        interface = self._create("Interface1")
        assert interface.getShortName() == "Interface1"
        assert interface.getAliveCheckResponseTimeout() is None
        assert interface.getDoipChannelCollectionRef() is None
        assert interface.getDoipConnectionRefs() == []
        assert interface.getDoIpRoutingActivations() == []
        assert interface.getGeneralInactivityTime() is None
        assert interface.getInitialInactivityTime() is None
        assert interface.getInitialVehicleAnnouncementTime() is None
        assert interface.getIsActivationLineDependent() is None
        assert interface.getMaxTesterConnections() is None
        assert interface.getSocketConnectionRefs() == []
        assert interface.getUseMacAddressForIdentification() is None
        assert interface.getUseVehicleIdentificationSyncStatus() is None
        assert interface.getVehicleAnnouncementCount() is None
        assert interface.getVehicleAnnouncementInterval() is None

    def test_member_order(self):
        interface = self._create("Interface1")
        members = [k for k in vars(interface) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_alive_check_response_timeout(self):
        interface = self._create("Interface1")
        value = TimeValue()
        value.setValue("60.0")
        result = interface.setAliveCheckResponseTimeout(value)
        assert result is interface
        assert interface.getAliveCheckResponseTimeout() is value
        interface.setAliveCheckResponseTimeout(None)
        assert interface.getAliveCheckResponseTimeout() is value

    def test_get_set_doip_channel_collection_ref(self):
        interface = self._create("Interface1")
        ref = RefType()
        ref.setValue("/DoIp/TpConfigs/DoIpTpConfig1")
        ref.setDest("DO-IP-TP-CONFIG")
        result = interface.setDoipChannelCollectionRef(ref)
        assert result is interface
        assert interface.getDoipChannelCollectionRef() is ref
        interface.setDoipChannelCollectionRef(None)
        assert interface.getDoipChannelCollectionRef() is ref

    def test_get_set_general_inactivity_time(self):
        interface = self._create("Interface1")
        value = TimeValue()
        value.setValue("50.0")
        interface.setGeneralInactivityTime(value)
        assert interface.getGeneralInactivityTime() is value
        interface.setGeneralInactivityTime(None)
        assert interface.getGeneralInactivityTime() is value

    def test_get_set_initial_inactivity_time(self):
        interface = self._create("Interface1")
        value = TimeValue()
        value.setValue("1.0")
        interface.setInitialInactivityTime(value)
        assert interface.getInitialInactivityTime() is value
        interface.setInitialInactivityTime(None)
        assert interface.getInitialInactivityTime() is value

    def test_get_set_initial_vehicle_announcement_time(self):
        interface = self._create("Interface1")
        value = TimeValue()
        value.setValue("0.5")
        interface.setInitialVehicleAnnouncementTime(value)
        assert interface.getInitialVehicleAnnouncementTime() is value
        interface.setInitialVehicleAnnouncementTime(None)
        assert interface.getInitialVehicleAnnouncementTime() is value

    def test_get_set_is_activation_line_dependent(self):
        interface = self._create("Interface1")
        value = Boolean()
        value.setValue("true")
        interface.setIsActivationLineDependent(value)
        assert interface.getIsActivationLineDependent() is value
        interface.setIsActivationLineDependent(None)
        assert interface.getIsActivationLineDependent() is value

    def test_get_set_max_tester_connections(self):
        interface = self._create("Interface1")
        value = PositiveInteger()
        value.setValue("4")
        interface.setMaxTesterConnections(value)
        assert interface.getMaxTesterConnections() is value
        interface.setMaxTesterConnections(None)
        assert interface.getMaxTesterConnections() is value

    def test_get_set_use_mac_address_for_identification(self):
        interface = self._create("Interface1")
        value = Boolean()
        value.setValue("false")
        interface.setUseMacAddressForIdentification(value)
        assert interface.getUseMacAddressForIdentification() is value
        interface.setUseMacAddressForIdentification(None)
        assert interface.getUseMacAddressForIdentification() is value

    def test_get_set_use_vehicle_identification_sync_status(self):
        interface = self._create("Interface1")
        value = Boolean()
        value.setValue("true")
        interface.setUseVehicleIdentificationSyncStatus(value)
        assert interface.getUseVehicleIdentificationSyncStatus() is value
        interface.setUseVehicleIdentificationSyncStatus(None)
        assert interface.getUseVehicleIdentificationSyncStatus() is value

    def test_get_set_vehicle_announcement_count(self):
        interface = self._create("Interface1")
        value = PositiveInteger()
        value.setValue("3")
        interface.setVehicleAnnouncementCount(value)
        assert interface.getVehicleAnnouncementCount() is value
        interface.setVehicleAnnouncementCount(None)
        assert interface.getVehicleAnnouncementCount() is value

    def test_get_set_vehicle_announcement_interval(self):
        interface = self._create("Interface1")
        value = TimeValue()
        value.setValue("2.0")
        interface.setVehicleAnnouncementInterval(value)
        assert interface.getVehicleAnnouncementInterval() is value
        interface.setVehicleAnnouncementInterval(None)
        assert interface.getVehicleAnnouncementInterval() is value

    def test_add_doip_connection_ref(self):
        interface = self._create("Interface1")
        ref = RefType()
        ref.setValue("/Ethernet/SocketConnectionBundle1")
        ref.setDest("SOCKET-CONNECTION-BUNDLE")
        result = interface.addDoipConnectionRef(ref)
        assert result is interface
        assert interface.getDoipConnectionRefs() == [ref]
        interface.addDoipConnectionRef(None)
        assert interface.getDoipConnectionRefs() == [ref]

    def test_add_socket_connection_ref(self):
        interface = self._create("Interface1")
        ref = RefType()
        ref.setValue("/Ethernet/StaticSocketConnection1")
        ref.setDest("STATIC-SOCKET-CONNECTION")
        result = interface.addSocketConnectionRef(ref)
        assert result is interface
        assert interface.getSocketConnectionRefs() == [ref]
        interface.addSocketConnectionRef(None)
        assert interface.getSocketConnectionRefs() == [ref]

    def test_create_do_ip_routing_activation(self):
        interface = self._create("Interface1")
        activation = interface.createDoIpRoutingActivation("RoutingActivation1")
        assert activation.getShortName() == "RoutingActivation1"
        assert isinstance(activation, DoIpRoutingActivation)
        assert interface.getDoIpRoutingActivations() == [activation]
        assert interface.createDoIpRoutingActivation("RoutingActivation1") is activation
        assert interface.getDoIpRoutingActivations() == [activation]
