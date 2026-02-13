"""
AUTOSAR Package - ETH

Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    MacAddressString,
    PositiveInteger,
    TimeValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.__init__ import (
    AbstractGlobalTimeDomainProps,
    GlobalTimeMaster,
    GlobalTimeSlave,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH import (
    CouplingPort,
    EthGlobalTime,
    EthGlobalTimeMessage,
    GlobalTimeCrc,
    GlobalTimeCrcSupport,
    GlobalTimePortRole,
)


class GlobalTimeEthMaster(GlobalTimeMaster):
    """
    This represents the specialization of the GlobalTimeMaster for Ethernet
    communication.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH::GlobalTimeEthMaster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 866, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of whether or not CRC is supported.
        # This is relevant for selected bus systems.
        self._crcSecured: Optional[GlobalTimeCrcSupport] = None

    @property
    def crc_secured(self) -> Optional[GlobalTimeCrcSupport]:
        """Get crcSecured (Pythonic accessor)."""
        return self._crcSecured

    @crc_secured.setter
    def crc_secured(self, value: Optional[GlobalTimeCrcSupport]) -> None:
        """
        Set crcSecured with validation.

        Args:
            value: The crcSecured to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcSecured = None
            return

        if not isinstance(value, GlobalTimeCrcSupport):
            raise TypeError(
                f"crcSecured must be GlobalTimeCrcSupport or None, got {type(value).__name__}"
            )
        self._crcSecured = value
        # Master ports in absence of Sync and Follow_Up messages on Slave.
        self._holdOverTime: Optional[TimeValue] = None

    @property
    def hold_over_time(self) -> Optional[TimeValue]:
        """Get holdOverTime (Pythonic accessor)."""
        return self._holdOverTime

    @hold_over_time.setter
    def hold_over_time(self, value: Optional[TimeValue]) -> None:
        """
        Set holdOverTime with validation.

        Args:
            value: The holdOverTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._holdOverTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"holdOverTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._holdOverTime = value
        self._subTlvConfig: Optional[EthTSynSubTlvConfig] = None

    @property
    def sub_tlv_config(self) -> Optional[EthTSynSubTlvConfig]:
        """Get subTlvConfig (Pythonic accessor)."""
        return self._subTlvConfig

    @sub_tlv_config.setter
    def sub_tlv_config(self, value: Optional[EthTSynSubTlvConfig]) -> None:
        """
        Set subTlvConfig with validation.

        Args:
            value: The subTlvConfig to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._subTlvConfig = None
            return

        if not isinstance(value, EthTSynSubTlvConfig):
            raise TypeError(
                f"subTlvConfig must be EthTSynSubTlvConfig or None, got {type(value).__name__}"
            )
        self._subTlvConfig = value

    def with_managed(self, value):
        """
        Set managed and return self for chaining.

        Args:
            value: The managed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_managed("value")
        """
        self.managed = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCrcSecured(self) -> GlobalTimeCrcSupport:
        """
        AUTOSAR-compliant getter for crcSecured.

        Returns:
            The crcSecured value

        Note:
            Delegates to crc_secured property (CODING_RULE_V2_00017)
        """
        return self.crc_secured  # Delegates to property

    def setCrcSecured(self, value: GlobalTimeCrcSupport) -> GlobalTimeEthMaster:
        """
        AUTOSAR-compliant setter for crcSecured with method chaining.

        Args:
            value: The crcSecured to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_secured property setter (gets validation automatically)
        """
        self.crc_secured = value  # Delegates to property setter
        return self

    def getHoldOverTime(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for holdOverTime.

        Returns:
            The holdOverTime value

        Note:
            Delegates to hold_over_time property (CODING_RULE_V2_00017)
        """
        return self.hold_over_time  # Delegates to property

    def setHoldOverTime(self, value: TimeValue) -> GlobalTimeEthMaster:
        """
        AUTOSAR-compliant setter for holdOverTime with method chaining.

        Args:
            value: The holdOverTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to hold_over_time property setter (gets validation automatically)
        """
        self.hold_over_time = value  # Delegates to property setter
        return self

    def getSubTlvConfig(self) -> EthTSynSubTlvConfig:
        """
        AUTOSAR-compliant getter for subTlvConfig.

        Returns:
            The subTlvConfig value

        Note:
            Delegates to sub_tlv_config property (CODING_RULE_V2_00017)
        """
        return self.sub_tlv_config  # Delegates to property

    def setSubTlvConfig(self, value: EthTSynSubTlvConfig) -> GlobalTimeEthMaster:
        """
        AUTOSAR-compliant setter for subTlvConfig with method chaining.

        Args:
            value: The subTlvConfig to set

        Returns:
            self for method chaining

        Note:
            Delegates to sub_tlv_config property setter (gets validation automatically)
        """
        self.sub_tlv_config = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_crc_secured(self, value: Optional[GlobalTimeCrcSupport]) -> GlobalTimeEthMaster:
        """
        Set crcSecured and return self for chaining.

        Args:
            value: The crcSecured to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_secured("value")
        """
        self.crc_secured = value  # Use property setter (gets validation)
        return self

    def with_hold_over_time(self, value: Optional[TimeValue]) -> GlobalTimeEthMaster:
        """
        Set holdOverTime and return self for chaining.

        Args:
            value: The holdOverTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_hold_over_time("value")
        """
        self.hold_over_time = value  # Use property setter (gets validation)
        return self

    def with_sub_tlv_config(self, value: Optional[EthTSynSubTlvConfig]) -> GlobalTimeEthMaster:
        """
        Set subTlvConfig and return self for chaining.

        Args:
            value: The subTlvConfig to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_tlv_config("value")
        """
        self.sub_tlv_config = value  # Use property setter (gets validation)
        return self



class EthTSynSubTlvConfig(ARObject):
    """
    Defines the subTLV fields which shall be included in the time sync message.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH::EthTSynSubTlvConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 867, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether an AUTOSAR Follow_Up TLV OFS used.
        self._ofsSubTlv: Optional[Boolean] = None

    @property
    def ofs_sub_tlv(self) -> Optional[Boolean]:
        """Get ofsSubTlv (Pythonic accessor)."""
        return self._ofsSubTlv

    @ofs_sub_tlv.setter
    def ofs_sub_tlv(self, value: Optional[Boolean]) -> None:
        """
        Set ofsSubTlv with validation.

        Args:
            value: The ofsSubTlv to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ofsSubTlv = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"ofsSubTlv must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._ofsSubTlv = value
        self._statusSubTlv: Optional[Boolean] = None

    @property
    def status_sub_tlv(self) -> Optional[Boolean]:
        """Get statusSubTlv (Pythonic accessor)."""
        return self._statusSubTlv

    @status_sub_tlv.setter
    def status_sub_tlv(self, value: Optional[Boolean]) -> None:
        """
        Set statusSubTlv with validation.

        Args:
            value: The statusSubTlv to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._statusSubTlv = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"statusSubTlv must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._statusSubTlv = value
        self._timeSubTlv: Optional[Boolean] = None

    @property
    def time_sub_tlv(self) -> Optional[Boolean]:
        """Get timeSubTlv (Pythonic accessor)."""
        return self._timeSubTlv

    @time_sub_tlv.setter
    def time_sub_tlv(self, value: Optional[Boolean]) -> None:
        """
        Set timeSubTlv with validation.

        Args:
            value: The timeSubTlv to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSubTlv = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"timeSubTlv must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._timeSubTlv = value
        self._userDataSubTlv: Optional[Boolean] = None

    @property
    def user_data_sub_tlv(self) -> Optional[Boolean]:
        """Get userDataSubTlv (Pythonic accessor)."""
        return self._userDataSubTlv

    @user_data_sub_tlv.setter
    def user_data_sub_tlv(self, value: Optional[Boolean]) -> None:
        """
        Set userDataSubTlv with validation.

        Args:
            value: The userDataSubTlv to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._userDataSubTlv = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"userDataSubTlv must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._userDataSubTlv = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOfsSubTlv(self) -> Boolean:
        """
        AUTOSAR-compliant getter for ofsSubTlv.

        Returns:
            The ofsSubTlv value

        Note:
            Delegates to ofs_sub_tlv property (CODING_RULE_V2_00017)
        """
        return self.ofs_sub_tlv  # Delegates to property

    def setOfsSubTlv(self, value: Boolean) -> EthTSynSubTlvConfig:
        """
        AUTOSAR-compliant setter for ofsSubTlv with method chaining.

        Args:
            value: The ofsSubTlv to set

        Returns:
            self for method chaining

        Note:
            Delegates to ofs_sub_tlv property setter (gets validation automatically)
        """
        self.ofs_sub_tlv = value  # Delegates to property setter
        return self

    def getStatusSubTlv(self) -> Boolean:
        """
        AUTOSAR-compliant getter for statusSubTlv.

        Returns:
            The statusSubTlv value

        Note:
            Delegates to status_sub_tlv property (CODING_RULE_V2_00017)
        """
        return self.status_sub_tlv  # Delegates to property

    def setStatusSubTlv(self, value: Boolean) -> EthTSynSubTlvConfig:
        """
        AUTOSAR-compliant setter for statusSubTlv with method chaining.

        Args:
            value: The statusSubTlv to set

        Returns:
            self for method chaining

        Note:
            Delegates to status_sub_tlv property setter (gets validation automatically)
        """
        self.status_sub_tlv = value  # Delegates to property setter
        return self

    def getTimeSubTlv(self) -> Boolean:
        """
        AUTOSAR-compliant getter for timeSubTlv.

        Returns:
            The timeSubTlv value

        Note:
            Delegates to time_sub_tlv property (CODING_RULE_V2_00017)
        """
        return self.time_sub_tlv  # Delegates to property

    def setTimeSubTlv(self, value: Boolean) -> EthTSynSubTlvConfig:
        """
        AUTOSAR-compliant setter for timeSubTlv with method chaining.

        Args:
            value: The timeSubTlv to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_sub_tlv property setter (gets validation automatically)
        """
        self.time_sub_tlv = value  # Delegates to property setter
        return self

    def getUserDataSubTlv(self) -> Boolean:
        """
        AUTOSAR-compliant getter for userDataSubTlv.

        Returns:
            The userDataSubTlv value

        Note:
            Delegates to user_data_sub_tlv property (CODING_RULE_V2_00017)
        """
        return self.user_data_sub_tlv  # Delegates to property

    def setUserDataSubTlv(self, value: Boolean) -> EthTSynSubTlvConfig:
        """
        AUTOSAR-compliant setter for userDataSubTlv with method chaining.

        Args:
            value: The userDataSubTlv to set

        Returns:
            self for method chaining

        Note:
            Delegates to user_data_sub_tlv property setter (gets validation automatically)
        """
        self.user_data_sub_tlv = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ofs_sub_tlv(self, value: Optional[Boolean]) -> EthTSynSubTlvConfig:
        """
        Set ofsSubTlv and return self for chaining.

        Args:
            value: The ofsSubTlv to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ofs_sub_tlv("value")
        """
        self.ofs_sub_tlv = value  # Use property setter (gets validation)
        return self

    def with_status_sub_tlv(self, value: Optional[Boolean]) -> EthTSynSubTlvConfig:
        """
        Set statusSubTlv and return self for chaining.

        Args:
            value: The statusSubTlv to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_status_sub_tlv("value")
        """
        self.status_sub_tlv = value  # Use property setter (gets validation)
        return self

    def with_time_sub_tlv(self, value: Optional[Boolean]) -> EthTSynSubTlvConfig:
        """
        Set timeSubTlv and return self for chaining.

        Args:
            value: The timeSubTlv to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_sub_tlv("value")
        """
        self.time_sub_tlv = value  # Use property setter (gets validation)
        return self

    def with_user_data_sub_tlv(self, value: Optional[Boolean]) -> EthTSynSubTlvConfig:
        """
        Set userDataSubTlv and return self for chaining.

        Args:
            value: The userDataSubTlv to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_user_data_sub_tlv("value")
        """
        self.user_data_sub_tlv = value  # Use property setter (gets validation)
        return self



class GlobalTimeEthSlave(GlobalTimeSlave):
    """
    This represents the specialization of the GlobalTimeSlave for Ethernet
    communication.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH::GlobalTimeEthSlave

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 867, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of whether or not validation of the CRC is.
        self._crcValidated: Optional[GlobalTimeCrc] = None

    @property
    def crc_validated(self) -> Optional[GlobalTimeCrc]:
        """Get crcValidated (Pythonic accessor)."""
        return self._crcValidated

    @crc_validated.setter
    def crc_validated(self, value: Optional[GlobalTimeCrc]) -> None:
        """
        Set crcValidated with validation.

        Args:
            value: The crcValidated to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcValidated = None
            return

        if not isinstance(value, GlobalTimeCrc):
            raise TypeError(
                f"crcValidated must be GlobalTimeCrc or None, got {type(value).__name__}"
            )
        self._crcValidated = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCrcValidated(self) -> GlobalTimeCrc:
        """
        AUTOSAR-compliant getter for crcValidated.

        Returns:
            The crcValidated value

        Note:
            Delegates to crc_validated property (CODING_RULE_V2_00017)
        """
        return self.crc_validated  # Delegates to property

    def setCrcValidated(self, value: GlobalTimeCrc) -> GlobalTimeEthSlave:
        """
        AUTOSAR-compliant setter for crcValidated with method chaining.

        Args:
            value: The crcValidated to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_validated property setter (gets validation automatically)
        """
        self.crc_validated = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_crc_validated(self, value: Optional[GlobalTimeCrc]) -> GlobalTimeEthSlave:
        """
        Set crcValidated and return self for chaining.

        Args:
            value: The crcValidated to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_validated("value")
        """
        self.crc_validated = value  # Use property setter (gets validation)
        return self



class EthGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """
    Enables the definition of Ethernet Global Time specific properties.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH::EthGlobalTimeDomainProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 867, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the fields of the message which shall be taken for CRC calculation
        # and verification.
        self._crcFlags: Optional[EthTSynCrcFlags] = None

    @property
    def crc_flags(self) -> Optional[EthTSynCrcFlags]:
        """Get crcFlags (Pythonic accessor)."""
        return self._crcFlags

    @crc_flags.setter
    def crc_flags(self, value: Optional[EthTSynCrcFlags]) -> None:
        """
        Set crcFlags with validation.

        Args:
            value: The crcFlags to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcFlags = None
            return

        if not isinstance(value, EthTSynCrcFlags):
            raise TypeError(
                f"crcFlags must be EthTSynCrcFlags or None, got {type(value).__name__}"
            )
        self._crcFlags = value
        # on.
        self._destination: Optional[MacAddressString] = None

    @property
    def destination(self) -> Optional[MacAddressString]:
        """Get destination (Pythonic accessor)."""
        return self._destination

    @destination.setter
    def destination(self, value: Optional[MacAddressString]) -> None:
        """
        Set destination with validation.

        Args:
            value: The destination to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destination = None
            return

        if not isinstance(value, MacAddressString):
            raise TypeError(
                f"destination must be MacAddressString or None, got {type(value).__name__}"
            )
        self._destination = value

    @property
    def fup_data_id_list(self) -> PositiveInteger:
        """Get fupDataIDList (Pythonic accessor)."""
        return self._fupDataIDList

    @fup_data_id_list.setter
    def fup_data_id_list(self, value: PositiveInteger) -> None:
        """
        Set fupDataIDList with validation.

        Args:
            value: The fupDataIDList to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"fupDataIDList must be PositiveInteger or str, got {type(value).__name__}"
            )
        self._fupDataIDList = value
        # GlobalTimeDomain.
        self._managed: List[EthGlobalTime] = []

    @property
    def managed(self) -> List[EthGlobalTime]:
        """Get managed (Pythonic accessor)."""
        return self._managed
        # Defines the compliance of the Ethernet time sync messages to specific
        # standards.
        self._message: Optional[EthGlobalTimeMessage] = None

    @property
    def message(self) -> Optional[EthGlobalTimeMessage]:
        """Get message (Pythonic accessor)."""
        return self._message

    @message.setter
    def message(self, value: Optional[EthGlobalTimeMessage]) -> None:
        """
        Set message with validation.

        Args:
            value: The message to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._message = None
            return

        if not isinstance(value, EthGlobalTimeMessage):
            raise TypeError(
                f"message must be EthGlobalTimeMessage or None, got {type(value).__name__}"
            )
        self._message = value
        # is sent using a VLAN.
        self._vlanPriority: Optional[PositiveInteger] = None

    @property
    def vlan_priority(self) -> Optional[PositiveInteger]:
        """Get vlanPriority (Pythonic accessor)."""
        return self._vlanPriority

    @vlan_priority.setter
    def vlan_priority(self, value: Optional[PositiveInteger]) -> None:
        """
        Set vlanPriority with validation.

        Args:
            value: The vlanPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlanPriority = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"vlanPriority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._vlanPriority = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCrcFlags(self) -> EthTSynCrcFlags:
        """
        AUTOSAR-compliant getter for crcFlags.

        Returns:
            The crcFlags value

        Note:
            Delegates to crc_flags property (CODING_RULE_V2_00017)
        """
        return self.crc_flags  # Delegates to property

    def setCrcFlags(self, value: EthTSynCrcFlags) -> EthGlobalTimeDomainProps:
        """
        AUTOSAR-compliant setter for crcFlags with method chaining.

        Args:
            value: The crcFlags to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_flags property setter (gets validation automatically)
        """
        self.crc_flags = value  # Delegates to property setter
        return self

    def getDestination(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for destination.

        Returns:
            The destination value

        Note:
            Delegates to destination property (CODING_RULE_V2_00017)
        """
        return self.destination  # Delegates to property

    def setDestination(self, value: "MacAddressString") -> EthGlobalTimeDomainProps:
        """
        AUTOSAR-compliant setter for destination with method chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination property setter (gets validation automatically)
        """
        self.destination = value  # Delegates to property setter
        return self

    def getFupDataIDList(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for fupDataIDList.

        Returns:
            The fupDataIDList value

        Note:
            Delegates to fup_data_id_list property (CODING_RULE_V2_00017)
        """
        return self.fup_data_id_list  # Delegates to property

    def setFupDataIDList(self, value: PositiveInteger) -> EthGlobalTimeDomainProps:
        """
        AUTOSAR-compliant setter for fupDataIDList with method chaining.

        Args:
            value: The fupDataIDList to set

        Returns:
            self for method chaining

        Note:
            Delegates to fup_data_id_list property setter (gets validation automatically)
        """
        self.fup_data_id_list = value  # Delegates to property setter
        return self

    def getManaged(self) -> List[EthGlobalTime]:
        """
        AUTOSAR-compliant getter for managed.

        Returns:
            The managed value

        Note:
            Delegates to managed property (CODING_RULE_V2_00017)
        """
        return self.managed  # Delegates to property

    def getMessage(self) -> "EthGlobalTimeMessage":
        """
        AUTOSAR-compliant getter for message.

        Returns:
            The message value

        Note:
            Delegates to message property (CODING_RULE_V2_00017)
        """
        return self.message  # Delegates to property

    def setMessage(self, value: "EthGlobalTimeMessage") -> EthGlobalTimeDomainProps:
        """
        AUTOSAR-compliant setter for message with method chaining.

        Args:
            value: The message to set

        Returns:
            self for method chaining

        Note:
            Delegates to message property setter (gets validation automatically)
        """
        self.message = value  # Delegates to property setter
        return self

    def getVlanPriority(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for vlanPriority.

        Returns:
            The vlanPriority value

        Note:
            Delegates to vlan_priority property (CODING_RULE_V2_00017)
        """
        return self.vlan_priority  # Delegates to property

    def setVlanPriority(self, value: PositiveInteger) -> EthGlobalTimeDomainProps:
        """
        AUTOSAR-compliant setter for vlanPriority with method chaining.

        Args:
            value: The vlanPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan_priority property setter (gets validation automatically)
        """
        self.vlan_priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_crc_flags(self, value: Optional[EthTSynCrcFlags]) -> EthGlobalTimeDomainProps:
        """
        Set crcFlags and return self for chaining.

        Args:
            value: The crcFlags to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_flags("value")
        """
        self.crc_flags = value  # Use property setter (gets validation)
        return self

    def with_destination(self, value: Optional[MacAddressString]) -> EthGlobalTimeDomainProps:
        """
        Set destination and return self for chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination("value")
        """
        self.destination = value  # Use property setter (gets validation)
        return self

    def with_fup_data_id_list(self, value: PositiveInteger) -> EthGlobalTimeDomainProps:
        """
        Set fupDataIDList and return self for chaining.

        Args:
            value: The fupDataIDList to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fup_data_id_list("value")
        """
        self.fup_data_id_list = value  # Use property setter (gets validation)
        return self

    def with_message(self, value: Optional[EthGlobalTimeMessage]) -> EthGlobalTimeDomainProps:
        """
        Set message and return self for chaining.

        Args:
            value: The message to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_message("value")
        """
        self.message = value  # Use property setter (gets validation)
        return self

    def with_vlan_priority(self, value: Optional[PositiveInteger]) -> EthGlobalTimeDomainProps:
        """
        Set vlanPriority and return self for chaining.

        Args:
            value: The vlanPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan_priority("value")
        """
        self.vlan_priority = value  # Use property setter (gets validation)
        return self



class EthTSynCrcFlags(ARObject):
    """
    Defines the fields of the message which shall be taken into account for CRC
    calculation and verification.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH::EthTSynCrcFlags

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 868, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # CorrectionField from the Follow_Up Message Header be included in CRC
        # calculation.
        self._crcCorrection: Optional[Boolean] = None

    @property
    def crc_correction(self) -> Optional[Boolean]:
        """Get crcCorrection (Pythonic accessor)."""
        return self._crcCorrection

    @crc_correction.setter
    def crc_correction(self, value: Optional[Boolean]) -> None:
        """
        Set crcCorrection with validation.

        Args:
            value: The crcCorrection to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcCorrection = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"crcCorrection must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._crcCorrection = value
        # calculation.
        self._crcDomain: Optional[Boolean] = None

    @property
    def crc_domain(self) -> Optional[Boolean]:
        """Get crcDomain (Pythonic accessor)."""
        return self._crcDomain

    @crc_domain.setter
    def crc_domain(self, value: Optional[Boolean]) -> None:
        """
        Set crcDomain with validation.

        Args:
            value: The crcDomain to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcDomain = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"crcDomain must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._crcDomain = value
        # calculation.
        self._crcMessage: Optional[Boolean] = None

    @property
    def crc_message(self) -> Optional[Boolean]:
        """Get crcMessage (Pythonic accessor)."""
        return self._crcMessage

    @crc_message.setter
    def crc_message(self, value: Optional[Boolean]) -> None:
        """
        Set crcMessage with validation.

        Args:
            value: The crcMessage to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcMessage = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"crcMessage must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._crcMessage = value
        # calculation.
        self._crcPrecise: Optional[Boolean] = None

    @property
    def crc_precise(self) -> Optional[Boolean]:
        """Get crcPrecise (Pythonic accessor)."""
        return self._crcPrecise

    @crc_precise.setter
    def crc_precise(self, value: Optional[Boolean]) -> None:
        """
        Set crcPrecise with validation.

        Args:
            value: The crcPrecise to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcPrecise = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"crcPrecise must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._crcPrecise = value
        self._crcSequenceId: Optional[Boolean] = None

    @property
    def crc_sequence_id(self) -> Optional[Boolean]:
        """Get crcSequenceId (Pythonic accessor)."""
        return self._crcSequenceId

    @crc_sequence_id.setter
    def crc_sequence_id(self, value: Optional[Boolean]) -> None:
        """
        Set crcSequenceId with validation.

        Args:
            value: The crcSequenceId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcSequenceId = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"crcSequenceId must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._crcSequenceId = value
        # calculation.
        self._crcSourcePort: Optional[Boolean] = None

    @property
    def crc_source_port(self) -> Optional[Boolean]:
        """Get crcSourcePort (Pythonic accessor)."""
        return self._crcSourcePort

    @crc_source_port.setter
    def crc_source_port(self, value: Optional[Boolean]) -> None:
        """
        Set crcSourcePort with validation.

        Args:
            value: The crcSourcePort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcSourcePort = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"crcSourcePort must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._crcSourcePort = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCrcCorrection(self) -> Boolean:
        """
        AUTOSAR-compliant getter for crcCorrection.

        Returns:
            The crcCorrection value

        Note:
            Delegates to crc_correction property (CODING_RULE_V2_00017)
        """
        return self.crc_correction  # Delegates to property

    def setCrcCorrection(self, value: Boolean) -> EthTSynCrcFlags:
        """
        AUTOSAR-compliant setter for crcCorrection with method chaining.

        Args:
            value: The crcCorrection to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_correction property setter (gets validation automatically)
        """
        self.crc_correction = value  # Delegates to property setter
        return self

    def getCrcDomain(self) -> Boolean:
        """
        AUTOSAR-compliant getter for crcDomain.

        Returns:
            The crcDomain value

        Note:
            Delegates to crc_domain property (CODING_RULE_V2_00017)
        """
        return self.crc_domain  # Delegates to property

    def setCrcDomain(self, value: Boolean) -> EthTSynCrcFlags:
        """
        AUTOSAR-compliant setter for crcDomain with method chaining.

        Args:
            value: The crcDomain to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_domain property setter (gets validation automatically)
        """
        self.crc_domain = value  # Delegates to property setter
        return self

    def getCrcMessage(self) -> Boolean:
        """
        AUTOSAR-compliant getter for crcMessage.

        Returns:
            The crcMessage value

        Note:
            Delegates to crc_message property (CODING_RULE_V2_00017)
        """
        return self.crc_message  # Delegates to property

    def setCrcMessage(self, value: Boolean) -> EthTSynCrcFlags:
        """
        AUTOSAR-compliant setter for crcMessage with method chaining.

        Args:
            value: The crcMessage to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_message property setter (gets validation automatically)
        """
        self.crc_message = value  # Delegates to property setter
        return self

    def getCrcPrecise(self) -> Boolean:
        """
        AUTOSAR-compliant getter for crcPrecise.

        Returns:
            The crcPrecise value

        Note:
            Delegates to crc_precise property (CODING_RULE_V2_00017)
        """
        return self.crc_precise  # Delegates to property

    def setCrcPrecise(self, value: Boolean) -> EthTSynCrcFlags:
        """
        AUTOSAR-compliant setter for crcPrecise with method chaining.

        Args:
            value: The crcPrecise to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_precise property setter (gets validation automatically)
        """
        self.crc_precise = value  # Delegates to property setter
        return self

    def getCrcSequenceId(self) -> Boolean:
        """
        AUTOSAR-compliant getter for crcSequenceId.

        Returns:
            The crcSequenceId value

        Note:
            Delegates to crc_sequence_id property (CODING_RULE_V2_00017)
        """
        return self.crc_sequence_id  # Delegates to property

    def setCrcSequenceId(self, value: Boolean) -> EthTSynCrcFlags:
        """
        AUTOSAR-compliant setter for crcSequenceId with method chaining.

        Args:
            value: The crcSequenceId to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_sequence_id property setter (gets validation automatically)
        """
        self.crc_sequence_id = value  # Delegates to property setter
        return self

    def getCrcSourcePort(self) -> Boolean:
        """
        AUTOSAR-compliant getter for crcSourcePort.

        Returns:
            The crcSourcePort value

        Note:
            Delegates to crc_source_port property (CODING_RULE_V2_00017)
        """
        return self.crc_source_port  # Delegates to property

    def setCrcSourcePort(self, value: Boolean) -> EthTSynCrcFlags:
        """
        AUTOSAR-compliant setter for crcSourcePort with method chaining.

        Args:
            value: The crcSourcePort to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_source_port property setter (gets validation automatically)
        """
        self.crc_source_port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_crc_correction(self, value: Optional[Boolean]) -> EthTSynCrcFlags:
        """
        Set crcCorrection and return self for chaining.

        Args:
            value: The crcCorrection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_correction("value")
        """
        self.crc_correction = value  # Use property setter (gets validation)
        return self

    def with_crc_domain(self, value: Optional[Boolean]) -> EthTSynCrcFlags:
        """
        Set crcDomain and return self for chaining.

        Args:
            value: The crcDomain to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_domain("value")
        """
        self.crc_domain = value  # Use property setter (gets validation)
        return self

    def with_crc_message(self, value: Optional[Boolean]) -> EthTSynCrcFlags:
        """
        Set crcMessage and return self for chaining.

        Args:
            value: The crcMessage to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_message("value")
        """
        self.crc_message = value  # Use property setter (gets validation)
        return self

    def with_crc_precise(self, value: Optional[Boolean]) -> EthTSynCrcFlags:
        """
        Set crcPrecise and return self for chaining.

        Args:
            value: The crcPrecise to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_precise("value")
        """
        self.crc_precise = value  # Use property setter (gets validation)
        return self

    def with_crc_sequence_id(self, value: Optional[Boolean]) -> EthTSynCrcFlags:
        """
        Set crcSequenceId and return self for chaining.

        Args:
            value: The crcSequenceId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_sequence_id("value")
        """
        self.crc_sequence_id = value  # Use property setter (gets validation)
        return self

    def with_crc_source_port(self, value: Optional[Boolean]) -> EthTSynCrcFlags:
        """
        Set crcSourcePort and return self for chaining.

        Args:
            value: The crcSourcePort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_source_port("value")
        """
        self.crc_source_port = value  # Use property setter (gets validation)
        return self



class EthGlobalTimeManagedCouplingPort(ARObject):
    """
    Specifies a CouplingPort which is managed by an Ethernet Global Time Domain.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH::EthGlobalTimeManagedCouplingPort

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 874, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines which CouplingPort is managed by this EthGlobal.
        self._couplingPort: Optional[CouplingPort] = None

    @property
    def coupling_port(self) -> Optional[CouplingPort]:
        """Get couplingPort (Pythonic accessor)."""
        return self._couplingPort

    @coupling_port.setter
    def coupling_port(self, value: Optional[CouplingPort]) -> None:
        """
        Set couplingPort with validation.

        Args:
            value: The couplingPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._couplingPort = None
            return

        if not isinstance(value, CouplingPort):
            raise TypeError(
                f"couplingPort must be CouplingPort or None, got {type(value).__name__}"
            )
        self._couplingPort = value
        self._globalTimePort: Optional[GlobalTimePortRole] = None

    @property
    def global_time_port(self) -> Optional[GlobalTimePortRole]:
        """Get globalTimePort (Pythonic accessor)."""
        return self._globalTimePort

    @global_time_port.setter
    def global_time_port(self, value: Optional[GlobalTimePortRole]) -> None:
        """
        Set globalTimePort with validation.

        Args:
            value: The globalTimePort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._globalTimePort = None
            return

        if not isinstance(value, GlobalTimePortRole):
            raise TypeError(
                f"globalTimePort must be GlobalTimePortRole or None, got {type(value).__name__}"
            )
        self._globalTimePort = value
        # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._globalTimeTxPeriod: Optional[TimeValue] = None

    @property
    def global_time_tx_period(self) -> Optional[TimeValue]:
        """Get globalTimeTxPeriod (Pythonic accessor)."""
        return self._globalTimeTxPeriod

    @global_time_tx_period.setter
    def global_time_tx_period(self, value: Optional[TimeValue]) -> None:
        """
        Set globalTimeTxPeriod with validation.

        Args:
            value: The globalTimeTxPeriod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._globalTimeTxPeriod = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"globalTimeTxPeriod must be TimeValue or None, got {type(value).__name__}"
            )
        self._globalTimeTxPeriod = value
        # If a measured Pdelay pdelayLatencyThreshold, the measured Pdelay discarded.
        self._pdelayLatency: Optional[TimeValue] = None

    @property
    def pdelay_latency(self) -> Optional[TimeValue]:
        """Get pdelayLatency (Pythonic accessor)."""
        return self._pdelayLatency

    @pdelay_latency.setter
    def pdelay_latency(self, value: Optional[TimeValue]) -> None:
        """
        Set pdelayLatency with validation.

        Args:
            value: The pdelayLatency to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pdelayLatency = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"pdelayLatency must be TimeValue or None, got {type(value).__name__}"
            )
        self._pdelayLatency = value
        self._pdelayRequest: Optional[TimeValue] = None

    @property
    def pdelay_request(self) -> Optional[TimeValue]:
        """Get pdelayRequest (Pythonic accessor)."""
        return self._pdelayRequest

    @pdelay_request.setter
    def pdelay_request(self, value: Optional[TimeValue]) -> None:
        """
        Set pdelayRequest with validation.

        Args:
            value: The pdelayRequest to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pdelayRequest = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"pdelayRequest must be TimeValue or None, got {type(value).__name__}"
            )
        self._pdelayRequest = value
                # transmitted resp.
        # Pdelay_Resp has been received.
        # A value of 0 or not attribute deactivates this timeout observation.
        self._pdelayRespAnd: Optional[TimeValue] = None

    @property
    def pdelay_resp_and(self) -> Optional[TimeValue]:
        """Get pdelayRespAnd (Pythonic accessor)."""
        return self._pdelayRespAnd

    @pdelay_resp_and.setter
    def pdelay_resp_and(self, value: Optional[TimeValue]) -> None:
        """
        Set pdelayRespAnd with validation.

        Args:
            value: The pdelayRespAnd to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pdelayRespAnd = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"pdelayRespAnd must be TimeValue or None, got {type(value).__name__}"
            )
        self._pdelayRespAnd = value
        # Coupling.
        self._pdelay: Optional[Boolean] = None

    @property
    def pdelay(self) -> Optional[Boolean]:
        """Get pdelay (Pythonic accessor)."""
        return self._pdelay

    @pdelay.setter
    def pdelay(self, value: Optional[Boolean]) -> None:
        """
        Set pdelay with validation.

        Args:
            value: The pdelay to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pdelay = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"pdelay must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._pdelay = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCouplingPort(self) -> CouplingPort:
        """
        AUTOSAR-compliant getter for couplingPort.

        Returns:
            The couplingPort value

        Note:
            Delegates to coupling_port property (CODING_RULE_V2_00017)
        """
        return self.coupling_port  # Delegates to property

    def setCouplingPort(self, value: CouplingPort) -> EthGlobalTimeManagedCouplingPort:
        """
        AUTOSAR-compliant setter for couplingPort with method chaining.

        Args:
            value: The couplingPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to coupling_port property setter (gets validation automatically)
        """
        self.coupling_port = value  # Delegates to property setter
        return self

    def getGlobalTimePort(self) -> "GlobalTimePortRole":
        """
        AUTOSAR-compliant getter for globalTimePort.

        Returns:
            The globalTimePort value

        Note:
            Delegates to global_time_port property (CODING_RULE_V2_00017)
        """
        return self.global_time_port  # Delegates to property

    def setGlobalTimePort(self, value: "GlobalTimePortRole") -> EthGlobalTimeManagedCouplingPort:
        """
        AUTOSAR-compliant setter for globalTimePort with method chaining.

        Args:
            value: The globalTimePort to set

        Returns:
            self for method chaining

        Note:
            Delegates to global_time_port property setter (gets validation automatically)
        """
        self.global_time_port = value  # Delegates to property setter
        return self

    def getGlobalTimeTxPeriod(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for globalTimeTxPeriod.

        Returns:
            The globalTimeTxPeriod value

        Note:
            Delegates to global_time_tx_period property (CODING_RULE_V2_00017)
        """
        return self.global_time_tx_period  # Delegates to property

    def setGlobalTimeTxPeriod(self, value: TimeValue) -> EthGlobalTimeManagedCouplingPort:
        """
        AUTOSAR-compliant setter for globalTimeTxPeriod with method chaining.

        Args:
            value: The globalTimeTxPeriod to set

        Returns:
            self for method chaining

        Note:
            Delegates to global_time_tx_period property setter (gets validation automatically)
        """
        self.global_time_tx_period = value  # Delegates to property setter
        return self

    def getPdelayLatency(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for pdelayLatency.

        Returns:
            The pdelayLatency value

        Note:
            Delegates to pdelay_latency property (CODING_RULE_V2_00017)
        """
        return self.pdelay_latency  # Delegates to property

    def setPdelayLatency(self, value: TimeValue) -> EthGlobalTimeManagedCouplingPort:
        """
        AUTOSAR-compliant setter for pdelayLatency with method chaining.

        Args:
            value: The pdelayLatency to set

        Returns:
            self for method chaining

        Note:
            Delegates to pdelay_latency property setter (gets validation automatically)
        """
        self.pdelay_latency = value  # Delegates to property setter
        return self

    def getPdelayRequest(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for pdelayRequest.

        Returns:
            The pdelayRequest value

        Note:
            Delegates to pdelay_request property (CODING_RULE_V2_00017)
        """
        return self.pdelay_request  # Delegates to property

    def setPdelayRequest(self, value: TimeValue) -> EthGlobalTimeManagedCouplingPort:
        """
        AUTOSAR-compliant setter for pdelayRequest with method chaining.

        Args:
            value: The pdelayRequest to set

        Returns:
            self for method chaining

        Note:
            Delegates to pdelay_request property setter (gets validation automatically)
        """
        self.pdelay_request = value  # Delegates to property setter
        return self

    def getPdelayRespAnd(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for pdelayRespAnd.

        Returns:
            The pdelayRespAnd value

        Note:
            Delegates to pdelay_resp_and property (CODING_RULE_V2_00017)
        """
        return self.pdelay_resp_and  # Delegates to property

    def setPdelayRespAnd(self, value: TimeValue) -> EthGlobalTimeManagedCouplingPort:
        """
        AUTOSAR-compliant setter for pdelayRespAnd with method chaining.

        Args:
            value: The pdelayRespAnd to set

        Returns:
            self for method chaining

        Note:
            Delegates to pdelay_resp_and property setter (gets validation automatically)
        """
        self.pdelay_resp_and = value  # Delegates to property setter
        return self

    def getPdelay(self) -> Boolean:
        """
        AUTOSAR-compliant getter for pdelay.

        Returns:
            The pdelay value

        Note:
            Delegates to pdelay property (CODING_RULE_V2_00017)
        """
        return self.pdelay  # Delegates to property

    def setPdelay(self, value: Boolean) -> EthGlobalTimeManagedCouplingPort:
        """
        AUTOSAR-compliant setter for pdelay with method chaining.

        Args:
            value: The pdelay to set

        Returns:
            self for method chaining

        Note:
            Delegates to pdelay property setter (gets validation automatically)
        """
        self.pdelay = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_coupling_port(self, value: Optional[CouplingPort]) -> EthGlobalTimeManagedCouplingPort:
        """
        Set couplingPort and return self for chaining.

        Args:
            value: The couplingPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_coupling_port("value")
        """
        self.coupling_port = value  # Use property setter (gets validation)
        return self

    def with_global_time_port(self, value: Optional[GlobalTimePortRole]) -> EthGlobalTimeManagedCouplingPort:
        """
        Set globalTimePort and return self for chaining.

        Args:
            value: The globalTimePort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_global_time_port("value")
        """
        self.global_time_port = value  # Use property setter (gets validation)
        return self

    def with_global_time_tx_period(self, value: Optional[TimeValue]) -> EthGlobalTimeManagedCouplingPort:
        """
        Set globalTimeTxPeriod and return self for chaining.

        Args:
            value: The globalTimeTxPeriod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_global_time_tx_period("value")
        """
        self.global_time_tx_period = value  # Use property setter (gets validation)
        return self

    def with_pdelay_latency(self, value: Optional[TimeValue]) -> EthGlobalTimeManagedCouplingPort:
        """
        Set pdelayLatency and return self for chaining.

        Args:
            value: The pdelayLatency to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdelay_latency("value")
        """
        self.pdelay_latency = value  # Use property setter (gets validation)
        return self

    def with_pdelay_request(self, value: Optional[TimeValue]) -> EthGlobalTimeManagedCouplingPort:
        """
        Set pdelayRequest and return self for chaining.

        Args:
            value: The pdelayRequest to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdelay_request("value")
        """
        self.pdelay_request = value  # Use property setter (gets validation)
        return self

    def with_pdelay_resp_and(self, value: Optional[TimeValue]) -> EthGlobalTimeManagedCouplingPort:
        """
        Set pdelayRespAnd and return self for chaining.

        Args:
            value: The pdelayRespAnd to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdelay_resp_and("value")
        """
        self.pdelay_resp_and = value  # Use property setter (gets validation)
        return self

    def with_pdelay(self, value: Optional[Boolean]) -> EthGlobalTimeManagedCouplingPort:
        """
        Set pdelay and return self for chaining.

        Args:
            value: The pdelay to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdelay("value")
        """
        self.pdelay = value  # Use property setter (gets validation)
        return self


class EthGlobalTimeMessageFormatEnum(AREnum):
    """
    EthGlobalTimeMessageFormatEnum enumeration

Specifies which message formats are available to for the Ethernet time sync protocol. Aggregated by EthGlobalTimeDomainProps.messageCompliance

Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH
    """
    # Message format according to IEEE 802.1AS standard.
    IEEE802_1AS = "0"

    # Message format according to IEEE 802.1AS standard with AUTOSAR extensions.
    IEEE802_1AS_AUTOSAR = "1"



class GlobalTimePortRoleEnum(AREnum):
    """
    GlobalTimePortRoleEnum enumeration

Selection of port behavior to Time Slave, Time Master or Dynamic (Time Slave or Time Master at runtime). Aggregated by EthGlobalTimeManagedCouplingPort.globalTimePortRole

Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH
    """
    # Time Slave or Time Master port behavior at runtime.
    dynamic = "2"

    # Template
    System = "None"

    # CP R23-11 timeMaster timeMaster port behavior
    AUTOSAR = "1"

    # TimeSlave port behavior
    timeSlave = "0"
