# This module contains AUTOSAR System Template classes for DoIP (Diagnostics over IP)
# It defines logic address properties and configurations for DoIP communication

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType, TimeValue


class AbstractDoIpLogicAddressProps(Identifiable, ABC):
    """
    Abstract base class for DoIP (Diagnostics over IP) logic address properties.
    This class defines the common properties for DoIP address configurations,
    serving as the foundation for specific DoIP address types in the system.
    """

    # AbstractDoIpLogicAddressProps method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractDoIpLogicAddressProps:
            raise TypeError("AbstractDoIpLogicAddressProps is an abstract class.")

        super().__init__(parent, short_name)


class DoIpLogicTargetAddressProps(AbstractDoIpLogicAddressProps):
    """
    Defines properties for DoIP (Diagnostics over IP) logic target addresses,
    specifying how diagnostic messages should be addressed to target ECUs
    in the IP-based diagnostic communication system.
    """

    # DoIpLogicTargetAddressProps method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class DoIpLogicTesterAddressProps(AbstractDoIpLogicAddressProps):
    """
    Defines properties for DoIP (Diagnostics over IP) logic tester addresses,
    specifying how diagnostic tools and testers are addressed in the IP-based
    diagnostic communication system, including routing activation references.
    """

    # DoIpLogicTesterAddressProps method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDoIpTesterRoutingActivationRef [x] impl  [ ] docstring  [ ] test
    # [ ] setDoIpTesterRoutingActivationRef [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.doIpTesterRoutingActivationRef: RefType = None

    def getDoIpTesterRoutingActivationRef(self):
        return self.doIpTesterRoutingActivationRef

    def setDoIpTesterRoutingActivationRef(self, value):
        if value is not None:
            self.doIpTesterRoutingActivationRef = value
        return self


class DoIpRoutingActivation(Identifiable):
    """
    This meta-class defines a DoIP routing activation possibility that activates the routing to the referenced doIPTargetAddress. This means that the diagnostic request messages related to the specified doIPTargetAddress received by socketConnections that are referenced by the same DoIpInterface that aggregates this DoIpRoutingActivation are activated.
    """

    # DoIpRoutingActivation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.204, p.553
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addDoIpTargetAddressRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDoIpTargetAddressRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to DoIPTargetAddress which is activated on this DoIpRoutingActivation.
        self.doIpTargetAddressRefs: List[RefType] = []

    def addDoIpTargetAddressRef(self, value: Optional[RefType]) -> "DoIpRoutingActivation":
        """
        Reference to DoIPTargetAddress which is activated on this DoIpRoutingActivation.
        A None value is a no-op and does not add to doIpTargetAddressRefs.
        """
        if value is not None:
            self.doIpTargetAddressRefs.append(value)
        return self

    def getDoIpTargetAddressRefs(self) -> List[RefType]:
        """
        Reference to DoIPTargetAddress which is activated on this DoIpRoutingActivation.
        """
        return self.doIpTargetAddressRefs


class DoIpInterface(Identifiable):
    """
    A logical interface over which the DoIP Node is able to communicate via DoIP independently from other existing DoIpInterfaces.
    """

    # DoIpInterface method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.203, p.552
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAliveCheckResponseTimeout         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAliveCheckResponseTimeout         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDoipChannelCollectionRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDoipChannelCollectionRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addDoipConnectionRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDoipConnectionRefs                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createDoIpRoutingActivation          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDoIpRoutingActivations            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getGeneralInactivityTime             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setGeneralInactivityTime             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInitialInactivityTime             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInitialInactivityTime             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInitialVehicleAnnouncementTime    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInitialVehicleAnnouncementTime    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIsActivationLineDependent         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIsActivationLineDependent         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxTesterConnections              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxTesterConnections              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addSocketConnectionRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSocketConnectionRefs              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getUseMacAddressForIdentification    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUseMacAddressForIdentification    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUseVehicleIdentificationSyncStatus [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUseVehicleIdentificationSyncStatus [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVehicleAnnouncementCount          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVehicleAnnouncementCount          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVehicleAnnouncementInterval       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVehicleAnnouncementInterval       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute defines the timeout in seconds for waiting for response to an Alive Check request before the connection is considered to be disconnected. Represents parameter T_TCP_AliveCheck of ISO 13400-2:2012.
        self.aliveCheckResponseTimeout: Optional[TimeValue] = None

        # Configuration of DoIPChannels available in an DoIpInterface. Each DoIPChannel describes a connection between a doIpSourceAddress and a doIpTargetAddress and the exchange of DcmIPdus between the PduR and DoIP. A DoIP channel is constituted by the set of all DoIpTpConnection elements via which the configured EcuInstance sends or receives SDUs that are sharing the same local diagnosis address and tester address.
        self.doipChannelCollectionRef: Optional[RefType] = None

        # DoIP Connections in the DoIpInterface that define the DoIP Pdus that are sent and received via SoAd over TCP or UDP.
        self.doipConnectionRefs: List[RefType] = []

        # Collection of DoIpRoutingActivation possibilities defined in the DoIpInterface.
        self.doIpRoutingActivations: List[DoIpRoutingActivation] = []

        # This attribute defines the timeout in seconds for maximum inactivity of a TCP socket connection before the DoIP module will close the according socket connection. Represents parameter T_TCP_General_Inactivity of ISO 13400-2:2012
        self.generalInactivityTime: Optional[TimeValue] = None

        # This attribute defines the timeout in seconds used for initial inactivity of a connected TCP socket connection directly after socket connection. Represents parameter T_TCP_Initial_Inactivity of ISO 13400-2:2012
        self.initialInactivityTime: Optional[TimeValue] = None

        # This attribute defines the waiting time in seconds for sending first vehicle announcement message after IP address assignment. Represents parameter A_DoIP_Announce_Wait of ISO 13400-2:2012
        self.initialVehicleAnnouncementTime: Optional[TimeValue] = None

        # This attribute defines whether the network interface • is started "on-demand" when an activation line is sensed or • is always available.
        self.isActivationLineDependent: Optional[Boolean] = None

        # Maximum amount of tester connections that shall be maintained at one time before alive check is performed.
        self.maxTesterConnections: Optional[PositiveInteger] = None

        # DoIP Connections in the DoIpInterface that define the DoIP Pdus that are sent and received via SoAd over TCP or UDP.
        self.socketConnectionRefs: List[RefType] = []

        # This attribute defines whether a configured EID at vehicle identification response/vehicle announcement is used or the MAC address. TRUE: Use MAC Address instead of EID for Vehicle identification/announcement. FALSE: Use configured EID for vehicle identification/announcement.
        self.useMacAddressForIdentification: Optional[Boolean] = None

        # This attribute defines if the optional VIN/GID synchronization status is used additionally in the vehicle identification/announcement.
        self.useVehicleIdentificationSyncStatus: Optional[Boolean] = None

        # This attribute defines the number of vehicle announcement messages on IP address assignment. Represents parameter A_DoIP_Announce_Num of ISO 13400-2:2012.
        self.vehicleAnnouncementCount: Optional[PositiveInteger] = None

        # This attribute defines the waiting time in seconds for sending subsequent vehicle announcement messages. Represents parameter A_DoIP_Announce_Interval of ISO 13400-2:2012
        self.vehicleAnnouncementInterval: Optional[TimeValue] = None

    def getAliveCheckResponseTimeout(self) -> Optional[TimeValue]:
        """
        This attribute defines the timeout in seconds for waiting for response to an Alive Check request before the connection is considered to be disconnected. Represents parameter T_TCP_AliveCheck of ISO 13400-2:2012.
        """
        return self.aliveCheckResponseTimeout

    def setAliveCheckResponseTimeout(self, value: Optional[TimeValue]) -> "DoIpInterface":
        """
        This attribute defines the timeout in seconds for waiting for response to an Alive Check request before the connection is considered to be disconnected. Represents parameter T_TCP_AliveCheck of ISO 13400-2:2012.
        A None value is a no-op and does not overwrite an existing aliveCheckResponseTimeout.
        """
        if value is not None:
            self.aliveCheckResponseTimeout = value
        return self

    def getDoipChannelCollectionRef(self) -> Optional[RefType]:
        """
        Configuration of DoIPChannels available in an DoIpInterface. Each DoIPChannel describes a connection between a doIpSourceAddress and a doIpTargetAddress and the exchange of DcmIPdus between the PduR and DoIP. A DoIP channel is constituted by the set of all DoIpTpConnection elements via which the configured EcuInstance sends or receives SDUs that are sharing the same local diagnosis address and tester address.
        """
        return self.doipChannelCollectionRef

    def setDoipChannelCollectionRef(self, value: Optional[RefType]) -> "DoIpInterface":
        """
        Configuration of DoIPChannels available in an DoIpInterface. Each DoIPChannel describes a connection between a doIpSourceAddress and a doIpTargetAddress and the exchange of DcmIPdus between the PduR and DoIP. A DoIP channel is constituted by the set of all DoIpTpConnection elements via which the configured EcuInstance sends or receives SDUs that are sharing the same local diagnosis address and tester address.
        A None value is a no-op and does not overwrite an existing doipChannelCollectionRef.
        """
        if value is not None:
            self.doipChannelCollectionRef = value
        return self

    def addDoipConnectionRef(self, value: Optional[RefType]) -> "DoIpInterface":
        """
        DoIP Connections in the DoIpInterface that define the DoIP Pdus that are sent and received via SoAd over TCP or UDP.
        A None value is a no-op and does not add to doipConnectionRefs.
        """
        if value is not None:
            self.doipConnectionRefs.append(value)
        return self

    def getDoipConnectionRefs(self) -> List[RefType]:
        """
        DoIP Connections in the DoIpInterface that define the DoIP Pdus that are sent and received via SoAd over TCP or UDP.
        """
        return self.doipConnectionRefs

    def createDoIpRoutingActivation(self, short_name: str) -> DoIpRoutingActivation:
        """
        Collection of DoIpRoutingActivation possibilities defined in the DoIpInterface.
        """
        if not self.IsElementExists(short_name, DoIpRoutingActivation):
            activation = DoIpRoutingActivation(self, short_name)
            self.addElement(activation)
            self.doIpRoutingActivations.append(activation)
        return self.getElement(short_name, DoIpRoutingActivation)

    def getDoIpRoutingActivations(self) -> List[DoIpRoutingActivation]:
        """
        Collection of DoIpRoutingActivation possibilities defined in the DoIpInterface.
        """
        return self.doIpRoutingActivations

    def getGeneralInactivityTime(self) -> Optional[TimeValue]:
        """
        This attribute defines the timeout in seconds for maximum inactivity of a TCP socket connection before the DoIP module will close the according socket connection. Represents parameter T_TCP_General_Inactivity of ISO 13400-2:2012
        """
        return self.generalInactivityTime

    def setGeneralInactivityTime(self, value: Optional[TimeValue]) -> "DoIpInterface":
        """
        This attribute defines the timeout in seconds for maximum inactivity of a TCP socket connection before the DoIP module will close the according socket connection. Represents parameter T_TCP_General_Inactivity of ISO 13400-2:2012
        A None value is a no-op and does not overwrite an existing generalInactivityTime.
        """
        if value is not None:
            self.generalInactivityTime = value
        return self

    def getInitialInactivityTime(self) -> Optional[TimeValue]:
        """
        This attribute defines the timeout in seconds used for initial inactivity of a connected TCP socket connection directly after socket connection. Represents parameter T_TCP_Initial_Inactivity of ISO 13400-2:2012
        """
        return self.initialInactivityTime

    def setInitialInactivityTime(self, value: Optional[TimeValue]) -> "DoIpInterface":
        """
        This attribute defines the timeout in seconds used for initial inactivity of a connected TCP socket connection directly after socket connection. Represents parameter T_TCP_Initial_Inactivity of ISO 13400-2:2012
        A None value is a no-op and does not overwrite an existing initialInactivityTime.
        """
        if value is not None:
            self.initialInactivityTime = value
        return self

    def getInitialVehicleAnnouncementTime(self) -> Optional[TimeValue]:
        """
        This attribute defines the waiting time in seconds for sending first vehicle announcement message after IP address assignment. Represents parameter A_DoIP_Announce_Wait of ISO 13400-2:2012
        """
        return self.initialVehicleAnnouncementTime

    def setInitialVehicleAnnouncementTime(self, value: Optional[TimeValue]) -> "DoIpInterface":
        """
        This attribute defines the waiting time in seconds for sending first vehicle announcement message after IP address assignment. Represents parameter A_DoIP_Announce_Wait of ISO 13400-2:2012
        A None value is a no-op and does not overwrite an existing initialVehicleAnnouncementTime.
        """
        if value is not None:
            self.initialVehicleAnnouncementTime = value
        return self

    def getIsActivationLineDependent(self) -> Optional[Boolean]:
        """
        This attribute defines whether the network interface • is started "on-demand" when an activation line is sensed or • is always available.
        """
        return self.isActivationLineDependent

    def setIsActivationLineDependent(self, value: Optional[Boolean]) -> "DoIpInterface":
        """
        This attribute defines whether the network interface • is started "on-demand" when an activation line is sensed or • is always available.
        A None value is a no-op and does not overwrite an existing isActivationLineDependent.
        """
        if value is not None:
            self.isActivationLineDependent = value
        return self

    def getMaxTesterConnections(self) -> Optional[PositiveInteger]:
        """
        Maximum amount of tester connections that shall be maintained at one time before alive check is performed.
        """
        return self.maxTesterConnections

    def setMaxTesterConnections(self, value: Optional[PositiveInteger]) -> "DoIpInterface":
        """
        Maximum amount of tester connections that shall be maintained at one time before alive check is performed.
        A None value is a no-op and does not overwrite an existing maxTesterConnections.
        """
        if value is not None:
            self.maxTesterConnections = value
        return self

    def addSocketConnectionRef(self, value: Optional[RefType]) -> "DoIpInterface":
        """
        DoIP Connections in the DoIpInterface that define the DoIP Pdus that are sent and received via SoAd over TCP or UDP.
        A None value is a no-op and does not add to socketConnectionRefs.
        """
        if value is not None:
            self.socketConnectionRefs.append(value)
        return self

    def getSocketConnectionRefs(self) -> List[RefType]:
        """
        DoIP Connections in the DoIpInterface that define the DoIP Pdus that are sent and received via SoAd over TCP or UDP.
        """
        return self.socketConnectionRefs

    def getUseMacAddressForIdentification(self) -> Optional[Boolean]:
        """
        This attribute defines whether a configured EID at vehicle identification response/vehicle announcement is used or the MAC address. TRUE: Use MAC Address instead of EID for Vehicle identification/announcement. FALSE: Use configured EID for vehicle identification/announcement.
        """
        return self.useMacAddressForIdentification

    def setUseMacAddressForIdentification(self, value: Optional[Boolean]) -> "DoIpInterface":
        """
        This attribute defines whether a configured EID at vehicle identification response/vehicle announcement is used or the MAC address. TRUE: Use MAC Address instead of EID for Vehicle identification/announcement. FALSE: Use configured EID for vehicle identification/announcement.
        A None value is a no-op and does not overwrite an existing useMacAddressForIdentification.
        """
        if value is not None:
            self.useMacAddressForIdentification = value
        return self

    def getUseVehicleIdentificationSyncStatus(self) -> Optional[Boolean]:
        """
        This attribute defines if the optional VIN/GID synchronization status is used additionally in the vehicle identification/announcement.
        """
        return self.useVehicleIdentificationSyncStatus

    def setUseVehicleIdentificationSyncStatus(self, value: Optional[Boolean]) -> "DoIpInterface":
        """
        This attribute defines if the optional VIN/GID synchronization status is used additionally in the vehicle identification/announcement.
        A None value is a no-op and does not overwrite an existing useVehicleIdentificationSyncStatus.
        """
        if value is not None:
            self.useVehicleIdentificationSyncStatus = value
        return self

    def getVehicleAnnouncementCount(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the number of vehicle announcement messages on IP address assignment. Represents parameter A_DoIP_Announce_Num of ISO 13400-2:2012.
        """
        return self.vehicleAnnouncementCount

    def setVehicleAnnouncementCount(self, value: Optional[PositiveInteger]) -> "DoIpInterface":
        """
        This attribute defines the number of vehicle announcement messages on IP address assignment. Represents parameter A_DoIP_Announce_Num of ISO 13400-2:2012.
        A None value is a no-op and does not overwrite an existing vehicleAnnouncementCount.
        """
        if value is not None:
            self.vehicleAnnouncementCount = value
        return self

    def getVehicleAnnouncementInterval(self) -> Optional[TimeValue]:
        """
        This attribute defines the waiting time in seconds for sending subsequent vehicle announcement messages. Represents parameter A_DoIP_Announce_Interval of ISO 13400-2:2012
        """
        return self.vehicleAnnouncementInterval

    def setVehicleAnnouncementInterval(self, value: Optional[TimeValue]) -> "DoIpInterface":
        """
        This attribute defines the waiting time in seconds for sending subsequent vehicle announcement messages. Represents parameter A_DoIP_Announce_Interval of ISO 13400-2:2012
        A None value is a no-op and does not overwrite an existing vehicleAnnouncementInterval.
        """
        if value is not None:
            self.vehicleAnnouncementInterval = value
        return self
