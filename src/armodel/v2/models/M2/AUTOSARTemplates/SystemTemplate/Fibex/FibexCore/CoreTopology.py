from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class CommunicationCluster(ARObject, ABC):
    """
    The CommunicationCluster is the main element to describe the topological
    connection of communicating ECUs. A cluster describes the ensemble of ECUs,
    which are linked by a communication medium of arbitrary topology (bus, star,
    ring, ...). The nodes within the cluster share the same communication
    protocol, which may be event-triggered, time-triggered or a combination of
    both. A CommunicationCluster aggregates one or more physical channels. Tags:
    vh.latestBindingTime=postBuild

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 107, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 57, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is CommunicationCluster:
            raise TypeError("CommunicationCluster is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Channels speed in bits/s.
        self._baudrate: Optional["PositiveUnlimitedInteger"] = None

    @property
    def baudrate(self) -> Optional["PositiveUnlimitedInteger"]:
        """Get baudrate (Pythonic accessor)."""
        return self._baudrate

    @baudrate.setter
    def baudrate(self, value: Optional["PositiveUnlimitedInteger"]) -> None:
        """
        Set baudrate with validation.

        Args:
            value: The baudrate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._baudrate = None
            return

        if not isinstance(value, PositiveUnlimitedInteger):
            raise TypeError(
                f"baudrate must be PositiveUnlimitedInteger or None, got {type(value).__name__}"
            )
        self._baudrate = value
        # This relationship defines which channel element belongs which cluster.
        # A channel shall be assigned to exactly whereas a cluster may have one or more
                # atpSplitable property has no atp.
        # Splitkey due (PropertySetPattern).
        # atpVariation.
        self._physical: List["PhysicalChannel"] = []

    @property
    def physical(self) -> List["PhysicalChannel"]:
        """Get physical (Pythonic accessor)."""
        return self._physical
        # The name of the protocol used.
        self._protocolName: Optional["String"] = None

    @property
    def protocol_name(self) -> Optional["String"]:
        """Get protocolName (Pythonic accessor)."""
        return self._protocolName

    @protocol_name.setter
    def protocol_name(self, value: Optional["String"]) -> None:
        """
        Set protocolName with validation.

        Args:
            value: The protocolName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._protocolName = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"protocolName must be String or None, got {type(value).__name__}"
            )
        self._protocolName = value
        # The version of the protocol used.
        self._protocolVersion: Optional["String"] = None

    @property
    def protocol_version(self) -> Optional["String"]:
        """Get protocolVersion (Pythonic accessor)."""
        return self._protocolVersion

    @protocol_version.setter
    def protocol_version(self, value: Optional["String"]) -> None:
        """
        Set protocolVersion with validation.

        Args:
            value: The protocolVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._protocolVersion = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"protocolVersion must be String or None, got {type(value).__name__}"
            )
        self._protocolVersion = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBaudrate(self) -> "PositiveUnlimitedInteger":
        """
        AUTOSAR-compliant getter for baudrate.

        Returns:
            The baudrate value

        Note:
            Delegates to baudrate property (CODING_RULE_V2_00017)
        """
        return self.baudrate  # Delegates to property

    def setBaudrate(self, value: "PositiveUnlimitedInteger") -> "CommunicationCluster":
        """
        AUTOSAR-compliant setter for baudrate with method chaining.

        Args:
            value: The baudrate to set

        Returns:
            self for method chaining

        Note:
            Delegates to baudrate property setter (gets validation automatically)
        """
        self.baudrate = value  # Delegates to property setter
        return self

    def getPhysical(self) -> List["PhysicalChannel"]:
        """
        AUTOSAR-compliant getter for physical.

        Returns:
            The physical value

        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    def getProtocolName(self) -> "String":
        """
        AUTOSAR-compliant getter for protocolName.

        Returns:
            The protocolName value

        Note:
            Delegates to protocol_name property (CODING_RULE_V2_00017)
        """
        return self.protocol_name  # Delegates to property

    def setProtocolName(self, value: "String") -> "CommunicationCluster":
        """
        AUTOSAR-compliant setter for protocolName with method chaining.

        Args:
            value: The protocolName to set

        Returns:
            self for method chaining

        Note:
            Delegates to protocol_name property setter (gets validation automatically)
        """
        self.protocol_name = value  # Delegates to property setter
        return self

    def getProtocolVersion(self) -> "String":
        """
        AUTOSAR-compliant getter for protocolVersion.

        Returns:
            The protocolVersion value

        Note:
            Delegates to protocol_version property (CODING_RULE_V2_00017)
        """
        return self.protocol_version  # Delegates to property

    def setProtocolVersion(self, value: "String") -> "CommunicationCluster":
        """
        AUTOSAR-compliant setter for protocolVersion with method chaining.

        Args:
            value: The protocolVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to protocol_version property setter (gets validation automatically)
        """
        self.protocol_version = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_baudrate(self, value: Optional["PositiveUnlimitedInteger"]) -> "CommunicationCluster":
        """
        Set baudrate and return self for chaining.

        Args:
            value: The baudrate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_baudrate("value")
        """
        self.baudrate = value  # Use property setter (gets validation)
        return self

    def with_protocol_name(self, value: Optional["String"]) -> "CommunicationCluster":
        """
        Set protocolName and return self for chaining.

        Args:
            value: The protocolName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_protocol_name("value")
        """
        self.protocol_name = value  # Use property setter (gets validation)
        return self

    def with_protocol_version(self, value: Optional["String"]) -> "CommunicationCluster":
        """
        Set protocolVersion and return self for chaining.

        Args:
            value: The protocolVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_protocol_version("value")
        """
        self.protocol_version = value  # Use property setter (gets validation)
        return self

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement

    RefType,
)


class EcuInstance(FibexElement):
    """
    ECUInstances are used to define the ECUs used in the topology. The type of
    the ECU is defined by a reference to an ECU specified with the ECU resource
    description.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 312, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 985, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 50, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 59, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # With this reference it is possible to identify which ISignal are applicable
                # for which Communication level ISignalIPduGroups shall be referenced by If an
                # ISignalIPduGroup contains other these contained ISignalIPdu not be referenced
                # by the EcuInstance.
        # are associated to an Ecu the top level ISignalIPduGroup.
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
                # R23-11.
        self._associatedCom: List[RefType] = []

    @property
    def associated_com(self) -> List[RefType]:
        """Get associatedCom (Pythonic accessor)."""
        return self._associatedCom
        # With this reference it is possible to identify which
                # ConsumedProvidedServiceInstanceGroups are for which ECUInstance.
        # atpSplitable; atpVariation Group Tags:.
        self._associated: List["ConsumedProvided"] = []

    @property
    def associated(self) -> List["ConsumedProvided"]:
        """Get associated (Pythonic accessor)."""
        return self._associated
        # With this reference it is possible to identify which PduR Groups are
        # applicable for which Communication.
        self._associatedPdur: List[RefType] = []

    @property
    def associated_pdur(self) -> List[RefType]:
        """Get associatedPdur (Pythonic accessor)."""
        return self._associatedPdur
        # If this parameter is available and set to true, then all channels will be
                # woken up as soon as at least channel wakeup occurs.
        # If PNCs are configured, then will be requested upon a channel wakeup.
        self._channel: Optional["Boolean"] = None

    @property
    def channel(self) -> Optional["Boolean"]:
        """Get channel (Pythonic accessor)."""
        return self._channel

    @channel.setter
    def channel(self, value: Optional["Boolean"]) -> None:
        """
        Set channel with validation.

        Args:
            value: The channel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._channel = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"channel must be Boolean or None, got {type(value).__name__}"
            )
        self._channel = value
        # Restriction of the Client Identifier for this Ecu to an of numerical values.
        # The Client Identifier of handle is generated by the client RTE for
                # communication.
        self._clientIdRange: Optional["ClientIdRange"] = None

    @property
    def client_id_range(self) -> Optional["ClientIdRange"]:
        """Get clientIdRange (Pythonic accessor)."""
        return self._clientIdRange

    @client_id_range.setter
    def client_id_range(self, value: Optional["ClientIdRange"]) -> None:
        """
        Set clientIdRange with validation.

        Args:
            value: The clientIdRange to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clientIdRange = None
            return

        if not isinstance(value, ClientIdRange):
            raise TypeError(
                f"clientIdRange must be ClientIdRange or None, got {type(value).__name__}"
            )
        self._clientIdRange = value
        # The period between successive calls to Com_Main of the AUTOSAR COM module in
        # seconds.
        self._com: Optional["TimeValue"] = None

    @property
    def com(self) -> Optional["TimeValue"]:
        """Get com (Pythonic accessor)."""
        return self._com

    @com.setter
    def com(self, value: Optional["TimeValue"]) -> None:
        """
        Set com with validation.

        Args:
            value: The com to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._com = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"com must be TimeValue or None, got {type(value).__name__}"
            )
        self._com = value
        # Enables for the Com module of this EcuInstance the delay time monitoring for
        # cyclic and repeated (TransmissionModeTiming has cyclic or
        # eventControlledTiming with numberOf 0).
        self._comEnable: Optional["Boolean"] = None

    @property
    def com_enable(self) -> Optional["Boolean"]:
        """Get comEnable (Pythonic accessor)."""
        return self._comEnable

    @com_enable.setter
    def com_enable(self, value: Optional["Boolean"]) -> None:
        """
        Set comEnable with validation.

        Args:
            value: The comEnable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._comEnable = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"comEnable must be Boolean or None, got {type(value).__name__}"
            )
        self._comEnable = value
        # CommunicationControllers of the ECU.
        # atpSplitable; atpVariation.
        self._commController: List["Communication"] = []

    @property
    def comm_controller(self) -> List["Communication"]:
        """Get commController (Pythonic accessor)."""
        return self._commController
        # All channels controlled by a single controller.
        # atpSplitable; atpVariation.
        self._connector: List["Communication"] = []

    @property
    def connector(self) -> List["Communication"]:
        """Get connector (Pythonic accessor)."""
        return self._connector
        # Describes the Dlt configuration on this EcuInstance.
        self._dltConfig: Optional["DltConfig"] = None

    @property
    def dlt_config(self) -> Optional["DltConfig"]:
        """Get dltConfig (Pythonic accessor)."""
        return self._dltConfig

    @dlt_config.setter
    def dlt_config(self, value: Optional["DltConfig"]) -> None:
        """
        Set dltConfig with validation.

        Args:
            value: The dltConfig to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dltConfig = None
            return

        if not isinstance(value, DltConfig):
            raise TypeError(
                f"dltConfig must be DltConfig or None, got {type(value).__name__}"
            )
        self._dltConfig = value
        # DoIp configuration on this EcuInstance.
        self._doIpConfig: Optional["DoIpConfig"] = None

    @property
    def do_ip_config(self) -> Optional["DoIpConfig"]:
        """Get doIpConfig (Pythonic accessor)."""
        return self._doIpConfig

    @do_ip_config.setter
    def do_ip_config(self, value: Optional["DoIpConfig"]) -> None:
        """
        Set doIpConfig with validation.

        Args:
            value: The doIpConfig to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._doIpConfig = None
            return

        if not isinstance(value, DoIpConfig):
            raise TypeError(
                f"doIpConfig must be DoIpConfig or None, got {type(value).__name__}"
            )
        self._doIpConfig = value
        # Reference to OsTaskProxies assigned to the Ecu 719 Document ID 673:
        # AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template R23-11.
        self._ecuTaskProxy: List["OsTaskProxy"] = []

    @property
    def ecu_task_proxy(self) -> List["OsTaskProxy"]:
        """Get ecuTaskProxy (Pythonic accessor)."""
        return self._ecuTaskProxy
        # Defines whether the derivation of SwitchPortGroups on VLAN and/or
                # CouplingPort.
        # pncMapping shall be for this EcuInstance.
        # If not defined the not be done.
        self._ethSwitchPort: Optional["Boolean"] = None

    @property
    def eth_switch_port(self) -> Optional["Boolean"]:
        """Get ethSwitchPort (Pythonic accessor)."""
        return self._ethSwitchPort

    @eth_switch_port.setter
    def eth_switch_port(self, value: Optional["Boolean"]) -> None:
        """
        Set ethSwitchPort with validation.

        Args:
            value: The ethSwitchPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ethSwitchPort = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"ethSwitchPort must be Boolean or None, got {type(value).__name__}"
            )
        self._ethSwitchPort = value
        # Firewall rules defined in the context of an EcuInstance.
        self._firewallRule: List["StateDependentFirewall"] = []

    @property
    def firewall_rule(self) -> List["StateDependentFirewall"]:
        """Get firewallRule (Pythonic accessor)."""
        return self._firewallRule
        # Optional definition of Partitions within an Ecu.
        self._partition: List["EcuPartition"] = []

    @property
    def partition(self) -> List["EcuPartition"]:
        """Get partition (Pythonic accessor)."""
        return self._partition
        # Defines if this EcuInstance shall request Nm on all its have Nm variant set
        # to FULL a PNC is requested.
        self._pncNmRequest: Optional["Boolean"] = None

    @property
    def pnc_nm_request(self) -> Optional["Boolean"]:
        """Get pncNmRequest (Pythonic accessor)."""
        return self._pncNmRequest

    @pnc_nm_request.setter
    def pnc_nm_request(self, value: Optional["Boolean"]) -> None:
        """
        Set pncNmRequest with validation.

        Args:
            value: The pncNmRequest to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pncNmRequest = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"pncNmRequest must be Boolean or None, got {type(value).__name__}"
            )
        self._pncNmRequest = value
        # Time in seconds the PNC state machine shall wait in.
        self._pncPrepare: Optional["TimeValue"] = None

    @property
    def pnc_prepare(self) -> Optional["TimeValue"]:
        """Get pncPrepare (Pythonic accessor)."""
        return self._pncPrepare

    @pnc_prepare.setter
    def pnc_prepare(self, value: Optional["TimeValue"]) -> None:
        """
        Set pncPrepare with validation.

        Args:
            value: The pncPrepare to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pncPrepare = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"pncPrepare must be TimeValue or None, got {type(value).__name__}"
            )
        self._pncPrepare = value
        # If this parameter is available and set to true then all PNCs will be woken up
                # as soon as a channel occurs.
        # This is ensured by adding all PNCs to all sources during upstream mapping.
        self._pnc: Optional["Boolean"] = None

    @property
    def pnc(self) -> Optional["Boolean"]:
        """Get pnc (Pythonic accessor)."""
        return self._pnc

    @pnc.setter
    def pnc(self, value: Optional["Boolean"]) -> None:
        """
        Set pnc with validation.

        Args:
            value: The pnc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pnc = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"pnc must be Boolean or None, got {type(value).__name__}"
            )
        self._pnc = value
        # Specifies the runtime of the reset timer in seconds.
        # This is valid for the reset of PN requests in the EIRA the ERA.
        self._pnResetTime: Optional["TimeValue"] = None

    @property
    def pn_reset_time(self) -> Optional["TimeValue"]:
        """Get pnResetTime (Pythonic accessor)."""
        return self._pnResetTime

    @pn_reset_time.setter
    def pn_reset_time(self, value: Optional["TimeValue"]) -> None:
        """
        Set pnResetTime with validation.

        Args:
            value: The pnResetTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pnResetTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"pnResetTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._pnResetTime = value
        # Specifies whether the ECU instance may be put to a "low mode" sleep mode is
        # supported sleep mode is not supported flag may only be set to "true" if the
        # feature is both hardware and basic software.
        self._sleepMode: Optional["Boolean"] = None

    @property
    def sleep_mode(self) -> Optional["Boolean"]:
        """Get sleepMode (Pythonic accessor)."""
        return self._sleepMode

    @sleep_mode.setter
    def sleep_mode(self, value: Optional["Boolean"]) -> None:
        """
        Set sleepMode with validation.

        Args:
            value: The sleepMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sleepMode = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"sleepMode must be Boolean or None, got {type(value).__name__}"
            )
        self._sleepMode = value
        # EcuInstance specific ICMP (Internet Control Message.
        self._tcpIpIcmpProps: Optional["EthTcpIpIcmpProps"] = None

    @property
    def tcp_ip_icmp_props(self) -> Optional["EthTcpIpIcmpProps"]:
        """Get tcpIpIcmpProps (Pythonic accessor)."""
        return self._tcpIpIcmpProps

    @tcp_ip_icmp_props.setter
    def tcp_ip_icmp_props(self, value: Optional["EthTcpIpIcmpProps"]) -> None:
        """
        Set tcpIpIcmpProps with validation.

        Args:
            value: The tcpIpIcmpProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIcmpProps = None
            return

        if not isinstance(value, EthTcpIpIcmpProps):
            raise TypeError(
                f"tcpIpIcmpProps must be EthTcpIpIcmpProps or None, got {type(value).__name__}"
            )
        self._tcpIpIcmpProps = value
        # EcuInstance specific TcpIp Stack attributes.
        self._tcpIpProps: Optional["EthTcpIpProps"] = None

    @property
    def tcp_ip_props(self) -> Optional["EthTcpIpProps"]:
        """Get tcpIpProps (Pythonic accessor)."""
        return self._tcpIpProps

    @tcp_ip_props.setter
    def tcp_ip_props(self, value: Optional["EthTcpIpProps"]) -> None:
        """
        Set tcpIpProps with validation.

        Args:
            value: The tcpIpProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpProps = None
            return

        if not isinstance(value, EthTcpIpProps):
            raise TypeError(
                f"tcpIpProps must be EthTcpIpProps or None, got {type(value).__name__}"
            )
        self._tcpIpProps = value
        # This attribute is used to control the existence of the V2X the given
        # EcuInstance.
        self._v2xSupported: Optional["V2xSupportEnum"] = None

    @property
    def v2x_supported(self) -> Optional["V2xSupportEnum"]:
        """Get v2xSupported (Pythonic accessor)."""
        return self._v2xSupported

    @v2x_supported.setter
    def v2x_supported(self, value: Optional["V2xSupportEnum"]) -> None:
        """
        Set v2xSupported with validation.

        Args:
            value: The v2xSupported to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._v2xSupported = None
            return

        if not isinstance(value, V2xSupportEnum):
            raise TypeError(
                f"v2xSupported must be V2xSupportEnum or None, got {type(value).__name__}"
            )
        self._v2xSupported = value
        # Driver support for wakeup over Bus.
        self._wakeUpOverBusSupported: Optional["Boolean"] = None

    @property
    def wake_up_over_bus_supported(self) -> Optional["Boolean"]:
        """Get wakeUpOverBusSupported (Pythonic accessor)."""
        return self._wakeUpOverBusSupported

    @wake_up_over_bus_supported.setter
    def wake_up_over_bus_supported(self, value: Optional["Boolean"]) -> None:
        """
        Set wakeUpOverBusSupported with validation.

        Args:
            value: The wakeUpOverBusSupported to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeUpOverBusSupported = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"wakeUpOverBusSupported must be Boolean or None, got {type(value).__name__}"
            )
        self._wakeUpOverBusSupported = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssociatedCom(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for associatedCom.

        Returns:
            The associatedCom value

        Note:
            Delegates to associated_com property (CODING_RULE_V2_00017)
        """
        return self.associated_com  # Delegates to property

    def getAssociated(self) -> List["ConsumedProvided"]:
        """
        AUTOSAR-compliant getter for associated.

        Returns:
            The associated value

        Note:
            Delegates to associated property (CODING_RULE_V2_00017)
        """
        return self.associated  # Delegates to property

    def getAssociatedPdur(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for associatedPdur.

        Returns:
            The associatedPdur value

        Note:
            Delegates to associated_pdur property (CODING_RULE_V2_00017)
        """
        return self.associated_pdur  # Delegates to property

    def getChannel(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for channel.

        Returns:
            The channel value

        Note:
            Delegates to channel property (CODING_RULE_V2_00017)
        """
        return self.channel  # Delegates to property

    def setChannel(self, value: "Boolean") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for channel with method chaining.

        Args:
            value: The channel to set

        Returns:
            self for method chaining

        Note:
            Delegates to channel property setter (gets validation automatically)
        """
        self.channel = value  # Delegates to property setter
        return self

    def getClientIdRange(self) -> "ClientIdRange":
        """
        AUTOSAR-compliant getter for clientIdRange.

        Returns:
            The clientIdRange value

        Note:
            Delegates to client_id_range property (CODING_RULE_V2_00017)
        """
        return self.client_id_range  # Delegates to property

    def setClientIdRange(self, value: "ClientIdRange") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for clientIdRange with method chaining.

        Args:
            value: The clientIdRange to set

        Returns:
            self for method chaining

        Note:
            Delegates to client_id_range property setter (gets validation automatically)
        """
        self.client_id_range = value  # Delegates to property setter
        return self

    def getCom(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for com.

        Returns:
            The com value

        Note:
            Delegates to com property (CODING_RULE_V2_00017)
        """
        return self.com  # Delegates to property

    def setCom(self, value: "TimeValue") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for com with method chaining.

        Args:
            value: The com to set

        Returns:
            self for method chaining

        Note:
            Delegates to com property setter (gets validation automatically)
        """
        self.com = value  # Delegates to property setter
        return self

    def getComEnable(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for comEnable.

        Returns:
            The comEnable value

        Note:
            Delegates to com_enable property (CODING_RULE_V2_00017)
        """
        return self.com_enable  # Delegates to property

    def setComEnable(self, value: "Boolean") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for comEnable with method chaining.

        Args:
            value: The comEnable to set

        Returns:
            self for method chaining

        Note:
            Delegates to com_enable property setter (gets validation automatically)
        """
        self.com_enable = value  # Delegates to property setter
        return self

    def getCommController(self) -> List["Communication"]:
        """
        AUTOSAR-compliant getter for commController.

        Returns:
            The commController value

        Note:
            Delegates to comm_controller property (CODING_RULE_V2_00017)
        """
        return self.comm_controller  # Delegates to property

    def getConnector(self) -> List["Communication"]:
        """
        AUTOSAR-compliant getter for connector.

        Returns:
            The connector value

        Note:
            Delegates to connector property (CODING_RULE_V2_00017)
        """
        return self.connector  # Delegates to property

    def getDltConfig(self) -> "DltConfig":
        """
        AUTOSAR-compliant getter for dltConfig.

        Returns:
            The dltConfig value

        Note:
            Delegates to dlt_config property (CODING_RULE_V2_00017)
        """
        return self.dlt_config  # Delegates to property

    def setDltConfig(self, value: "DltConfig") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for dltConfig with method chaining.

        Args:
            value: The dltConfig to set

        Returns:
            self for method chaining

        Note:
            Delegates to dlt_config property setter (gets validation automatically)
        """
        self.dlt_config = value  # Delegates to property setter
        return self

    def getDoIpConfig(self) -> "DoIpConfig":
        """
        AUTOSAR-compliant getter for doIpConfig.

        Returns:
            The doIpConfig value

        Note:
            Delegates to do_ip_config property (CODING_RULE_V2_00017)
        """
        return self.do_ip_config  # Delegates to property

    def setDoIpConfig(self, value: "DoIpConfig") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for doIpConfig with method chaining.

        Args:
            value: The doIpConfig to set

        Returns:
            self for method chaining

        Note:
            Delegates to do_ip_config property setter (gets validation automatically)
        """
        self.do_ip_config = value  # Delegates to property setter
        return self

    def getEcuTaskProxy(self) -> List["OsTaskProxy"]:
        """
        AUTOSAR-compliant getter for ecuTaskProxy.

        Returns:
            The ecuTaskProxy value

        Note:
            Delegates to ecu_task_proxy property (CODING_RULE_V2_00017)
        """
        return self.ecu_task_proxy  # Delegates to property

    def getEthSwitchPort(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for ethSwitchPort.

        Returns:
            The ethSwitchPort value

        Note:
            Delegates to eth_switch_port property (CODING_RULE_V2_00017)
        """
        return self.eth_switch_port  # Delegates to property

    def setEthSwitchPort(self, value: "Boolean") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for ethSwitchPort with method chaining.

        Args:
            value: The ethSwitchPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to eth_switch_port property setter (gets validation automatically)
        """
        self.eth_switch_port = value  # Delegates to property setter
        return self

    def getFirewallRule(self) -> List["StateDependentFirewall"]:
        """
        AUTOSAR-compliant getter for firewallRule.

        Returns:
            The firewallRule value

        Note:
            Delegates to firewall_rule property (CODING_RULE_V2_00017)
        """
        return self.firewall_rule  # Delegates to property

    def getPartition(self) -> List["EcuPartition"]:
        """
        AUTOSAR-compliant getter for partition.

        Returns:
            The partition value

        Note:
            Delegates to partition property (CODING_RULE_V2_00017)
        """
        return self.partition  # Delegates to property

    def getPncNmRequest(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for pncNmRequest.

        Returns:
            The pncNmRequest value

        Note:
            Delegates to pnc_nm_request property (CODING_RULE_V2_00017)
        """
        return self.pnc_nm_request  # Delegates to property

    def setPncNmRequest(self, value: "Boolean") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for pncNmRequest with method chaining.

        Args:
            value: The pncNmRequest to set

        Returns:
            self for method chaining

        Note:
            Delegates to pnc_nm_request property setter (gets validation automatically)
        """
        self.pnc_nm_request = value  # Delegates to property setter
        return self

    def getPncPrepare(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for pncPrepare.

        Returns:
            The pncPrepare value

        Note:
            Delegates to pnc_prepare property (CODING_RULE_V2_00017)
        """
        return self.pnc_prepare  # Delegates to property

    def setPncPrepare(self, value: "TimeValue") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for pncPrepare with method chaining.

        Args:
            value: The pncPrepare to set

        Returns:
            self for method chaining

        Note:
            Delegates to pnc_prepare property setter (gets validation automatically)
        """
        self.pnc_prepare = value  # Delegates to property setter
        return self

    def getPnc(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for pnc.

        Returns:
            The pnc value

        Note:
            Delegates to pnc property (CODING_RULE_V2_00017)
        """
        return self.pnc  # Delegates to property

    def setPnc(self, value: "Boolean") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for pnc with method chaining.

        Args:
            value: The pnc to set

        Returns:
            self for method chaining

        Note:
            Delegates to pnc property setter (gets validation automatically)
        """
        self.pnc = value  # Delegates to property setter
        return self

    def getPnResetTime(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for pnResetTime.

        Returns:
            The pnResetTime value

        Note:
            Delegates to pn_reset_time property (CODING_RULE_V2_00017)
        """
        return self.pn_reset_time  # Delegates to property

    def setPnResetTime(self, value: "TimeValue") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for pnResetTime with method chaining.

        Args:
            value: The pnResetTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to pn_reset_time property setter (gets validation automatically)
        """
        self.pn_reset_time = value  # Delegates to property setter
        return self

    def getSleepMode(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for sleepMode.

        Returns:
            The sleepMode value

        Note:
            Delegates to sleep_mode property (CODING_RULE_V2_00017)
        """
        return self.sleep_mode  # Delegates to property

    def setSleepMode(self, value: "Boolean") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for sleepMode with method chaining.

        Args:
            value: The sleepMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to sleep_mode property setter (gets validation automatically)
        """
        self.sleep_mode = value  # Delegates to property setter
        return self

    def getTcpIpIcmpProps(self) -> "EthTcpIpIcmpProps":
        """
        AUTOSAR-compliant getter for tcpIpIcmpProps.

        Returns:
            The tcpIpIcmpProps value

        Note:
            Delegates to tcp_ip_icmp_props property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_icmp_props  # Delegates to property

    def setTcpIpIcmpProps(self, value: "EthTcpIpIcmpProps") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for tcpIpIcmpProps with method chaining.

        Args:
            value: The tcpIpIcmpProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_icmp_props property setter (gets validation automatically)
        """
        self.tcp_ip_icmp_props = value  # Delegates to property setter
        return self

    def getTcpIpProps(self) -> "EthTcpIpProps":
        """
        AUTOSAR-compliant getter for tcpIpProps.

        Returns:
            The tcpIpProps value

        Note:
            Delegates to tcp_ip_props property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_props  # Delegates to property

    def setTcpIpProps(self, value: "EthTcpIpProps") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for tcpIpProps with method chaining.

        Args:
            value: The tcpIpProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_props property setter (gets validation automatically)
        """
        self.tcp_ip_props = value  # Delegates to property setter
        return self

    def getV2xSupported(self) -> "V2xSupportEnum":
        """
        AUTOSAR-compliant getter for v2xSupported.

        Returns:
            The v2xSupported value

        Note:
            Delegates to v2x_supported property (CODING_RULE_V2_00017)
        """
        return self.v2x_supported  # Delegates to property

    def setV2xSupported(self, value: "V2xSupportEnum") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for v2xSupported with method chaining.

        Args:
            value: The v2xSupported to set

        Returns:
            self for method chaining

        Note:
            Delegates to v2x_supported property setter (gets validation automatically)
        """
        self.v2x_supported = value  # Delegates to property setter
        return self

    def getWakeUpOverBusSupported(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for wakeUpOverBusSupported.

        Returns:
            The wakeUpOverBusSupported value

        Note:
            Delegates to wake_up_over_bus_supported property (CODING_RULE_V2_00017)
        """
        return self.wake_up_over_bus_supported  # Delegates to property

    def setWakeUpOverBusSupported(self, value: "Boolean") -> "EcuInstance":
        """
        AUTOSAR-compliant setter for wakeUpOverBusSupported with method chaining.

        Args:
            value: The wakeUpOverBusSupported to set

        Returns:
            self for method chaining

        Note:
            Delegates to wake_up_over_bus_supported property setter (gets validation automatically)
        """
        self.wake_up_over_bus_supported = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_channel(self, value: Optional["Boolean"]) -> "EcuInstance":
        """
        Set channel and return self for chaining.

        Args:
            value: The channel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_channel("value")
        """
        self.channel = value  # Use property setter (gets validation)
        return self

    def with_client_id_range(self, value: Optional["ClientIdRange"]) -> "EcuInstance":
        """
        Set clientIdRange and return self for chaining.

        Args:
            value: The clientIdRange to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_id_range("value")
        """
        self.client_id_range = value  # Use property setter (gets validation)
        return self

    def with_com(self, value: Optional["TimeValue"]) -> "EcuInstance":
        """
        Set com and return self for chaining.

        Args:
            value: The com to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_com("value")
        """
        self.com = value  # Use property setter (gets validation)
        return self

    def with_com_enable(self, value: Optional["Boolean"]) -> "EcuInstance":
        """
        Set comEnable and return self for chaining.

        Args:
            value: The comEnable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_com_enable("value")
        """
        self.com_enable = value  # Use property setter (gets validation)
        return self

    def with_dlt_config(self, value: Optional["DltConfig"]) -> "EcuInstance":
        """
        Set dltConfig and return self for chaining.

        Args:
            value: The dltConfig to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dlt_config("value")
        """
        self.dlt_config = value  # Use property setter (gets validation)
        return self

    def with_do_ip_config(self, value: Optional["DoIpConfig"]) -> "EcuInstance":
        """
        Set doIpConfig and return self for chaining.

        Args:
            value: The doIpConfig to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_do_ip_config("value")
        """
        self.do_ip_config = value  # Use property setter (gets validation)
        return self

    def with_eth_switch_port(self, value: Optional["Boolean"]) -> "EcuInstance":
        """
        Set ethSwitchPort and return self for chaining.

        Args:
            value: The ethSwitchPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_eth_switch_port("value")
        """
        self.eth_switch_port = value  # Use property setter (gets validation)
        return self

    def with_pnc_nm_request(self, value: Optional["Boolean"]) -> "EcuInstance":
        """
        Set pncNmRequest and return self for chaining.

        Args:
            value: The pncNmRequest to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_nm_request("value")
        """
        self.pnc_nm_request = value  # Use property setter (gets validation)
        return self

    def with_pnc_prepare(self, value: Optional["TimeValue"]) -> "EcuInstance":
        """
        Set pncPrepare and return self for chaining.

        Args:
            value: The pncPrepare to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_prepare("value")
        """
        self.pnc_prepare = value  # Use property setter (gets validation)
        return self

    def with_pnc(self, value: Optional["Boolean"]) -> "EcuInstance":
        """
        Set pnc and return self for chaining.

        Args:
            value: The pnc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc("value")
        """
        self.pnc = value  # Use property setter (gets validation)
        return self

    def with_pn_reset_time(self, value: Optional["TimeValue"]) -> "EcuInstance":
        """
        Set pnResetTime and return self for chaining.

        Args:
            value: The pnResetTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pn_reset_time("value")
        """
        self.pn_reset_time = value  # Use property setter (gets validation)
        return self

    def with_sleep_mode(self, value: Optional["Boolean"]) -> "EcuInstance":
        """
        Set sleepMode and return self for chaining.

        Args:
            value: The sleepMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sleep_mode("value")
        """
        self.sleep_mode = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_icmp_props(self, value: Optional["EthTcpIpIcmpProps"]) -> "EcuInstance":
        """
        Set tcpIpIcmpProps and return self for chaining.

        Args:
            value: The tcpIpIcmpProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_icmp_props("value")
        """
        self.tcp_ip_icmp_props = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_props(self, value: Optional["EthTcpIpProps"]) -> "EcuInstance":
        """
        Set tcpIpProps and return self for chaining.

        Args:
            value: The tcpIpProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_props("value")
        """
        self.tcp_ip_props = value  # Use property setter (gets validation)
        return self

    def with_v2x_supported(self, value: Optional["V2xSupportEnum"]) -> "EcuInstance":
        """
        Set v2xSupported and return self for chaining.

        Args:
            value: The v2xSupported to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_v2x_supported("value")
        """
        self.v2x_supported = value  # Use property setter (gets validation)
        return self

    def with_wake_up_over_bus_supported(self, value: Optional["Boolean"]) -> "EcuInstance":
        """
        Set wakeUpOverBusSupported and return self for chaining.

        Args:
            value: The wakeUpOverBusSupported to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wake_up_over_bus_supported("value")
        """
        self.wake_up_over_bus_supported = value  # Use property setter (gets validation)
        return self

from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class PhysicalChannel(Identifiable, ABC):
    """
    A physical channel is the transmission medium that is used to send and
    receive information between communicating ECUs. Each CommunicationCluster
    has at least one physical channel. Bus systems like CAN and LIN only have
    exactly one PhysicalChannel. A FlexRay cluster may have more than one
    PhysicalChannels that may be used in parallel for redundant communication.
    An ECU is part of a cluster if it contains at least one controller that is
    connected to at least one channel of the cluster.#

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 325, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 58, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 235, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is PhysicalChannel:
            raise TypeError("PhysicalChannel is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the ECUInstance via a Communication Connector to which the
                # channel is connected.
        # assignment of Physical Channels to is expressed with atpVariation.
        self._comm: List["Communication"] = []

    @property
    def comm(self) -> List["Communication"]:
        """Get comm (Pythonic accessor)."""
        return self._comm
        # One frame triggering is defined for exactly one channel.
        # have assigned an arbitrary number of signals/PDUs/frames are variable, the
                # shall be variable, too.
        # atpVariation.
        self._frameTriggering: List[RefType] = []

    @property
    def frame_triggering(self) -> List[RefType]:
        """Get frameTriggering (Pythonic accessor)."""
        return self._frameTriggering
        # One ISignalTriggering is defined for exactly one channel.
        # may have assigned an arbitrary number of signals/PDUs/frames are variable,
                # the shall be variable, too.
        # atpVariation 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate
                # Template R23-11.
        self._iSignal: List[RefType] = []

    @property
    def i_signal(self) -> List[RefType]:
        """Get iSignal (Pythonic accessor)."""
        return self._iSignal
        # Reference between a channel with role managing and a channel with role
        # managed channel.
        self._managed: List["PhysicalChannel"] = []

    @property
    def managed(self) -> List["PhysicalChannel"]:
        """Get managed (Pythonic accessor)."""
        return self._managed
        # One PduTriggering is defined for exactly one channel.
        # have assigned an arbitrary number of signals/PDUs/frames are variable, the
                # shall be variable, too.
        # atpVariation.
        self._pduTriggering: List[RefType] = []

    @property
    def pdu_triggering(self) -> List[RefType]:
        """Get pduTriggering (Pythonic accessor)."""
        return self._pduTriggering

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComm(self) -> List["Communication"]:
        """
        AUTOSAR-compliant getter for comm.

        Returns:
            The comm value

        Note:
            Delegates to comm property (CODING_RULE_V2_00017)
        """
        return self.comm  # Delegates to property

    def getFrameTriggering(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for frameTriggering.

        Returns:
            The frameTriggering value

        Note:
            Delegates to frame_triggering property (CODING_RULE_V2_00017)
        """
        return self.frame_triggering  # Delegates to property

    def getISignal(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for iSignal.

        Returns:
            The iSignal value

        Note:
            Delegates to i_signal property (CODING_RULE_V2_00017)
        """
        return self.i_signal  # Delegates to property

    def getManaged(self) -> List["PhysicalChannel"]:
        """
        AUTOSAR-compliant getter for managed.

        Returns:
            The managed value

        Note:
            Delegates to managed property (CODING_RULE_V2_00017)
        """
        return self.managed  # Delegates to property

    def getPduTriggering(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for pduTriggering.

        Returns:
            The pduTriggering value

        Note:
            Delegates to pdu_triggering property (CODING_RULE_V2_00017)
        """
        return self.pdu_triggering  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class ClientIdRange(ARObject):
    """
    With this element it is possible to restrict the Client Identifier of the
    transaction handle that is generated by the client RTE for inter-Ecu
    Client/Server communication to an allowed range of numerical values.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 52, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the lower limit of the ClientIdRange.
        self._lowerLimit: Optional["Limit"] = None

    @property
    def lower_limit(self) -> Optional["Limit"]:
        """Get lowerLimit (Pythonic accessor)."""
        return self._lowerLimit

    @lower_limit.setter
    def lower_limit(self, value: Optional["Limit"]) -> None:
        """
        Set lowerLimit with validation.

        Args:
            value: The lowerLimit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lowerLimit = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"lowerLimit must be Limit or None, got {type(value).__name__}"
            )
        self._lowerLimit = value
        # This specifies the upper limit of the ClientIdRange.
        self._upperLimit: Optional["Limit"] = None

    @property
    def upper_limit(self) -> Optional["Limit"]:
        """Get upperLimit (Pythonic accessor)."""
        return self._upperLimit

    @upper_limit.setter
    def upper_limit(self, value: Optional["Limit"]) -> None:
        """
        Set upperLimit with validation.

        Args:
            value: The upperLimit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upperLimit = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"upperLimit must be Limit or None, got {type(value).__name__}"
            )
        self._upperLimit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLowerLimit(self) -> "Limit":
        """
        AUTOSAR-compliant getter for lowerLimit.

        Returns:
            The lowerLimit value

        Note:
            Delegates to lower_limit property (CODING_RULE_V2_00017)
        """
        return self.lower_limit  # Delegates to property

    def setLowerLimit(self, value: "Limit") -> "ClientIdRange":
        """
        AUTOSAR-compliant setter for lowerLimit with method chaining.

        Args:
            value: The lowerLimit to set

        Returns:
            self for method chaining

        Note:
            Delegates to lower_limit property setter (gets validation automatically)
        """
        self.lower_limit = value  # Delegates to property setter
        return self

    def getUpperLimit(self) -> "Limit":
        """
        AUTOSAR-compliant getter for upperLimit.

        Returns:
            The upperLimit value

        Note:
            Delegates to upper_limit property (CODING_RULE_V2_00017)
        """
        return self.upper_limit  # Delegates to property

    def setUpperLimit(self, value: "Limit") -> "ClientIdRange":
        """
        AUTOSAR-compliant setter for upperLimit with method chaining.

        Args:
            value: The upperLimit to set

        Returns:
            self for method chaining

        Note:
            Delegates to upper_limit property setter (gets validation automatically)
        """
        self.upper_limit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_lower_limit(self, value: Optional["Limit"]) -> "ClientIdRange":
        """
        Set lowerLimit and return self for chaining.

        Args:
            value: The lowerLimit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lower_limit("value")
        """
        self.lower_limit = value  # Use property setter (gets validation)
        return self

    def with_upper_limit(self, value: Optional["Limit"]) -> "ClientIdRange":
        """
        Set upperLimit and return self for chaining.

        Args:
            value: The upperLimit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_upper_limit("value")
        """
        self.upper_limit = value  # Use property setter (gets validation)
        return self

from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class CommunicationController(ARObject, ABC):
    """
    The communication controller is a dedicated hardware device by means of
    which hosts are sending frames to and receiving frames from the
    communication medium. Tags: vh.latestBindingTime=postBuild

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 53, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is CommunicationController:
            raise TypeError("CommunicationController is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether the ECU shall be woken up by this wake up is possible up is
        # not supported wakeUpByControllerSupported is set to TRUE shall be supported
        # by both hardware and.
        self._wakeUpBy: Optional["Boolean"] = None

    @property
    def wake_up_by(self) -> Optional["Boolean"]:
        """Get wakeUpBy (Pythonic accessor)."""
        return self._wakeUpBy

    @wake_up_by.setter
    def wake_up_by(self, value: Optional["Boolean"]) -> None:
        """
        Set wakeUpBy with validation.

        Args:
            value: The wakeUpBy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeUpBy = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"wakeUpBy must be Boolean or None, got {type(value).__name__}"
            )
        self._wakeUpBy = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getWakeUpBy(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for wakeUpBy.

        Returns:
            The wakeUpBy value

        Note:
            Delegates to wake_up_by property (CODING_RULE_V2_00017)
        """
        return self.wake_up_by  # Delegates to property

    def setWakeUpBy(self, value: "Boolean") -> "CommunicationController":
        """
        AUTOSAR-compliant setter for wakeUpBy with method chaining.

        Args:
            value: The wakeUpBy to set

        Returns:
            self for method chaining

        Note:
            Delegates to wake_up_by property setter (gets validation automatically)
        """
        self.wake_up_by = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_wake_up_by(self, value: Optional["Boolean"]) -> "CommunicationController":
        """
        Set wakeUpBy and return self for chaining.

        Args:
            value: The wakeUpBy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wake_up_by("value")
        """
        self.wake_up_by = value  # Use property setter (gets validation)
        return self

from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class CommunicationConnector(Identifiable, ABC):
    """
    The connection between the referencing ECU and the referenced channel via
    the referenced controller. Connectors are used to describe the bus
    interfaces of the ECUs and to specify the sending/receiving behavior. Each
    CommunicationConnector has a reference to exactly one
    communicationController. Note: Several CommunicationConnectors can be
    assigned to one PhysicalChannel in the scope of one ECU Instance.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 54, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 57, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is CommunicationConnector:
            raise TypeError("CommunicationConnector is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the communication controller.
        # The and referenced be aggregated by the can be referenced by elements.
        # This is the FlexRay Bus.
        # FlexRay communicates physical channels.
        # But only one controller in an responsible for both channels.
        # Thus, two channel A and for channel B) shall the same controller.
        self._commController: Optional["Communication"] = None

    @property
    def comm_controller(self) -> Optional["Communication"]:
        """Get commController (Pythonic accessor)."""
        return self._commController

    @comm_controller.setter
    def comm_controller(self, value: Optional["Communication"]) -> None:
        """
        Set commController with validation.

        Args:
            value: The commController to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._commController = None
            return

        if not isinstance(value, Communication):
            raise TypeError(
                f"commController must be Communication or None, got {type(value).__name__}"
            )
        self._commController = value
        # If this parameter is available and set to true then a wakeup source shall be
        # created for the Physical this CommunicationConnector.
        self._createEcu: Optional["Boolean"] = None

    @property
    def create_ecu(self) -> Optional["Boolean"]:
        """Get createEcu (Pythonic accessor)."""
        return self._createEcu

    @create_ecu.setter
    def create_ecu(self, value: Optional["Boolean"]) -> None:
        """
        Set createEcu with validation.

        Args:
            value: The createEcu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._createEcu = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"createEcu must be Boolean or None, got {type(value).__name__}"
            )
        self._createEcu = value
        # Defines if this EcuInstance shall implement the dynamic functionality on this
        # and its respective Physical.
        self._dynamicPncTo: Optional["Boolean"] = None

    @property
    def dynamic_pnc_to(self) -> Optional["Boolean"]:
        """Get dynamicPncTo (Pythonic accessor)."""
        return self._dynamicPncTo

    @dynamic_pnc_to.setter
    def dynamic_pnc_to(self, value: Optional["Boolean"]) -> None:
        """
        Set dynamicPncTo with validation.

        Args:
            value: The dynamicPncTo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamicPncTo = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"dynamicPncTo must be Boolean or None, got {type(value).__name__}"
            )
        self._dynamicPncTo = value
        # An ECUs reception or send ports.
        # If signals/PDUs/frames are variable, the shall be variable, too.
        # atpVariation.
        self._ecuCommPort: List["CommConnectorPort"] = []

    @property
    def ecu_comm_port(self) -> List["CommConnectorPort"]:
        """Get ecuCommPort (Pythonic accessor)."""
        return self._ecuCommPort
        # Bit mask for NM-Pdu Payload used to configure the NM filter mask for the
        # Network Management.
        self._pncFilterArray: List["PositiveInteger"] = []

    @property
    def pnc_filter_array(self) -> List["PositiveInteger"]:
        """Get pncFilterArray (Pythonic accessor)."""
        return self._pncFilterArray
        # Defines if this EcuInstance shall implement the Pnc functionality on this
                # CommunicationConnector respective PhysicalChannel.
        # Several Ecu the same PhysicalChannel can have the enabled, but only one of
                # them the pncGatewayType "active".
        self._pncGateway: Optional["PncGatewayTypeEnum"] = None

    @property
    def pnc_gateway(self) -> Optional["PncGatewayTypeEnum"]:
        """Get pncGateway (Pythonic accessor)."""
        return self._pncGateway

    @pnc_gateway.setter
    def pnc_gateway(self, value: Optional["PncGatewayTypeEnum"]) -> None:
        """
        Set pncGateway with validation.

        Args:
            value: The pncGateway to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pncGateway = None
            return

        if not isinstance(value, PncGatewayTypeEnum):
            raise TypeError(
                f"pncGateway must be PncGatewayTypeEnum or None, got {type(value).__name__}"
            )
        self._pncGateway = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommController(self) -> "Communication":
        """
        AUTOSAR-compliant getter for commController.

        Returns:
            The commController value

        Note:
            Delegates to comm_controller property (CODING_RULE_V2_00017)
        """
        return self.comm_controller  # Delegates to property

    def setCommController(self, value: "Communication") -> "CommunicationConnector":
        """
        AUTOSAR-compliant setter for commController with method chaining.

        Args:
            value: The commController to set

        Returns:
            self for method chaining

        Note:
            Delegates to comm_controller property setter (gets validation automatically)
        """
        self.comm_controller = value  # Delegates to property setter
        return self

    def getCreateEcu(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for createEcu.

        Returns:
            The createEcu value

        Note:
            Delegates to create_ecu property (CODING_RULE_V2_00017)
        """
        return self.create_ecu  # Delegates to property

    def setCreateEcu(self, value: "Boolean") -> "CommunicationConnector":
        """
        AUTOSAR-compliant setter for createEcu with method chaining.

        Args:
            value: The createEcu to set

        Returns:
            self for method chaining

        Note:
            Delegates to create_ecu property setter (gets validation automatically)
        """
        self.create_ecu = value  # Delegates to property setter
        return self

    def getDynamicPncTo(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for dynamicPncTo.

        Returns:
            The dynamicPncTo value

        Note:
            Delegates to dynamic_pnc_to property (CODING_RULE_V2_00017)
        """
        return self.dynamic_pnc_to  # Delegates to property

    def setDynamicPncTo(self, value: "Boolean") -> "CommunicationConnector":
        """
        AUTOSAR-compliant setter for dynamicPncTo with method chaining.

        Args:
            value: The dynamicPncTo to set

        Returns:
            self for method chaining

        Note:
            Delegates to dynamic_pnc_to property setter (gets validation automatically)
        """
        self.dynamic_pnc_to = value  # Delegates to property setter
        return self

    def getEcuCommPort(self) -> List["CommConnectorPort"]:
        """
        AUTOSAR-compliant getter for ecuCommPort.

        Returns:
            The ecuCommPort value

        Note:
            Delegates to ecu_comm_port property (CODING_RULE_V2_00017)
        """
        return self.ecu_comm_port  # Delegates to property

    def getPncFilterArray(self) -> List["PositiveInteger"]:
        """
        AUTOSAR-compliant getter for pncFilterArray.

        Returns:
            The pncFilterArray value

        Note:
            Delegates to pnc_filter_array property (CODING_RULE_V2_00017)
        """
        return self.pnc_filter_array  # Delegates to property

    def getPncGateway(self) -> "PncGatewayTypeEnum":
        """
        AUTOSAR-compliant getter for pncGateway.

        Returns:
            The pncGateway value

        Note:
            Delegates to pnc_gateway property (CODING_RULE_V2_00017)
        """
        return self.pnc_gateway  # Delegates to property

    def setPncGateway(self, value: "PncGatewayTypeEnum") -> "CommunicationConnector":
        """
        AUTOSAR-compliant setter for pncGateway with method chaining.

        Args:
            value: The pncGateway to set

        Returns:
            self for method chaining

        Note:
            Delegates to pnc_gateway property setter (gets validation automatically)
        """
        self.pnc_gateway = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_comm_controller(self, value: Optional["Communication"]) -> "CommunicationConnector":
        """
        Set commController and return self for chaining.

        Args:
            value: The commController to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_comm_controller("value")
        """
        self.comm_controller = value  # Use property setter (gets validation)
        return self

    def with_create_ecu(self, value: Optional["Boolean"]) -> "CommunicationConnector":
        """
        Set createEcu and return self for chaining.

        Args:
            value: The createEcu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_create_ecu("value")
        """
        self.create_ecu = value  # Use property setter (gets validation)
        return self

    def with_dynamic_pnc_to(self, value: Optional["Boolean"]) -> "CommunicationConnector":
        """
        Set dynamicPncTo and return self for chaining.

        Args:
            value: The dynamicPncTo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dynamic_pnc_to("value")
        """
        self.dynamic_pnc_to = value  # Use property setter (gets validation)
        return self

    def with_pnc_gateway(self, value: Optional["PncGatewayTypeEnum"]) -> "CommunicationConnector":
        """
        Set pncGateway and return self for chaining.

        Args:
            value: The pncGateway to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_gateway("value")
        """
        self.pnc_gateway = value  # Use property setter (gets validation)
        return self

from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class CommConnectorPort(Identifiable, ABC):
    """
    The Ecu communication relationship defines which signals, Pdus and frames
    are actually received and transmitted by this ECU. For each signal, Pdu or
    Frame that is transmitted or received and used by the Ecu an association
    between an ISignalPort, IPduPort or FramePort with the corresponding
    Triggering shall be created. An ISignalPort shall be created only if the
    corresponding signal is handled by COM (RTE or Signal Gateway). If a Pdu
    Gateway ECU only routes the Pdu without being interested in the content only
    a FramePort and an IPduPort needs to be created.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 303, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is CommConnectorPort:
            raise TypeError("CommConnectorPort is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Communication Direction of the Connector Port (input or output Port).
        self._communication: Optional["Communication"] = None

    @property
    def communication(self) -> Optional["Communication"]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional["Communication"]) -> None:
        """
        Set communication with validation.

        Args:
            value: The communication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._communication = None
            return

        if not isinstance(value, Communication):
            raise TypeError(
                f"communication must be Communication or None, got {type(value).__name__}"
            )
        self._communication = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> "Communication":
        """
        AUTOSAR-compliant getter for communication.

        Returns:
            The communication value

        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "Communication") -> "CommConnectorPort":
        """
        AUTOSAR-compliant setter for communication with method chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Note:
            Delegates to communication property setter (gets validation automatically)
        """
        self.communication = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional["Communication"]) -> "CommConnectorPort":
        """
        Set communication and return self for chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_communication("value")
        """
        self.communication = value  # Use property setter (gets validation)
        return self

from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class CommunicationCycle(ARObject, ABC):
    """
    The communication cycle where the frame is sent.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 424, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is CommunicationCycle:
            raise TypeError("CommunicationCycle is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommunicationCycle,
)


class CycleCounter(CommunicationCycle):
    """
    The communication cycle where the frame is send is described by the
    attribute "cycleCounter".

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 424, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The communication cycle where the frame described by is sent.
        # If a timing is given in this way the shall specify the cycleCount upper bound
                # and point of total repetition.
        # This incremented at the beginning of each new cycle, 0 to cycleCountMax, and
                # is reset to 0 after a cycleCountMax+1 cycles.
        self._CycleCounter: Optional["Integer"] = None

    @property
    def cycle_counter(self) -> Optional["Integer"]:
        """Get CycleCounter (Pythonic accessor)."""
        return self._CycleCounter

    @cycle_counter.setter
    def cycle_counter(self, value: Optional["Integer"]) -> None:
        """
        Set CycleCounter with validation.

        Args:
            value: The CycleCounter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._CycleCounter = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"CycleCounter must be Integer or None, got {type(value).__name__}"
            )
        self._CycleCounter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCycleCounter(self) -> "Integer":
        """
        AUTOSAR-compliant getter for CycleCounter.

        Returns:
            The CycleCounter value

        Note:
            Delegates to cycle_counter property (CODING_RULE_V2_00017)
        """
        return self.cycle_counter  # Delegates to property

    def setCycleCounter(self, value: "Integer") -> "CycleCounter":
        """
        AUTOSAR-compliant setter for CycleCounter with method chaining.

        Args:
            value: The CycleCounter to set

        Returns:
            self for method chaining

        Note:
            Delegates to cycle_counter property setter (gets validation automatically)
        """
        self.cycle_counter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cycle_counter(self, value: Optional["Integer"]) -> "CycleCounter":
        """
        Set CycleCounter and return self for chaining.

        Args:
            value: The CycleCounter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cycle_counter("value")
        """
        self.cycle_counter = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommunicationCycle,
)


class CycleRepetition(CommunicationCycle):
    """
    The communication cycle where the frame is send is described by the
    attributes baseCycle and cycle Repetition. (cid:53) 424 of 2090 Document ID
    63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 424, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The first communication cycle where the frame is sent.
        # is incremented at the beginning of each new from 0 to 63, and is reset to 0
                # after a 64 cycles.
        self._BaseCycle: Optional["Integer"] = None

    @property
    def base_cycle(self) -> Optional["Integer"]:
        """Get BaseCycle (Pythonic accessor)."""
        return self._BaseCycle

    @base_cycle.setter
    def base_cycle(self, value: Optional["Integer"]) -> None:
        """
        Set BaseCycle with validation.

        Args:
            value: The BaseCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._BaseCycle = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"BaseCycle must be Integer or None, got {type(value).__name__}"
            )
        self._BaseCycle = value
        # The number of communication cycles (after the first cycle) frame described by
        # this timing is sent again.
        self._CycleRepetition: Optional["CycleRepetitionType"] = None

    @property
    def cycle_repetition(self) -> Optional["CycleRepetitionType"]:
        """Get CycleRepetition (Pythonic accessor)."""
        return self._CycleRepetition

    @cycle_repetition.setter
    def cycle_repetition(self, value: Optional["CycleRepetitionType"]) -> None:
        """
        Set CycleRepetition with validation.

        Args:
            value: The CycleRepetition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._CycleRepetition = None
            return

        if not isinstance(value, CycleRepetitionType):
            raise TypeError(
                f"CycleRepetition must be CycleRepetitionType or None, got {type(value).__name__}"
            )
        self._CycleRepetition = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBaseCycle(self) -> "Integer":
        """
        AUTOSAR-compliant getter for BaseCycle.

        Returns:
            The BaseCycle value

        Note:
            Delegates to base_cycle property (CODING_RULE_V2_00017)
        """
        return self.base_cycle  # Delegates to property

    def setBaseCycle(self, value: "Integer") -> "CycleRepetition":
        """
        AUTOSAR-compliant setter for BaseCycle with method chaining.

        Args:
            value: The BaseCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to base_cycle property setter (gets validation automatically)
        """
        self.base_cycle = value  # Delegates to property setter
        return self

    def getCycleRepetition(self) -> "CycleRepetitionType":
        """
        AUTOSAR-compliant getter for CycleRepetition.

        Returns:
            The CycleRepetition value

        Note:
            Delegates to cycle_repetition property (CODING_RULE_V2_00017)
        """
        return self.cycle_repetition  # Delegates to property

    def setCycleRepetition(self, value: "CycleRepetitionType") -> "CycleRepetition":
        """
        AUTOSAR-compliant setter for CycleRepetition with method chaining.

        Args:
            value: The CycleRepetition to set

        Returns:
            self for method chaining

        Note:
            Delegates to cycle_repetition property setter (gets validation automatically)
        """
        self.cycle_repetition = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base_cycle(self, value: Optional["Integer"]) -> "CycleRepetition":
        """
        Set BaseCycle and return self for chaining.

        Args:
            value: The BaseCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base_cycle("value")
        """
        self.base_cycle = value  # Use property setter (gets validation)
        return self

    def with_cycle_repetition(self, value: Optional["CycleRepetitionType"]) -> "CycleRepetition":
        """
        Set CycleRepetition and return self for chaining.

        Args:
            value: The CycleRepetition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cycle_repetition("value")
        """
        self.cycle_repetition = value  # Use property setter (gets validation)
        return self
