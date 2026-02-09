"""
AUTOSAR Package - GlobalTime

Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.__init__ import (
    FibexElement,
)


class GlobalTimeDomain(FibexElement):
    """
    This represents the ability to define a global time domain.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::GlobalTimeDomain
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 858, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 225, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the minimum amount of time between two time are transmitted.
        self._debounceTime: Optional["TimeValue"] = None

    @property
    def debounce_time(self) -> Optional["TimeValue"]:
        """Get debounceTime (Pythonic accessor)."""
        return self._debounceTime

    @debounce_time.setter
    def debounce_time(self, value: Optional["TimeValue"]) -> None:
        """
        Set debounceTime with validation.
        
        Args:
            value: The debounceTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._debounceTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"debounceTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._debounceTime = value
        # This represents the ID of the GlobalTimeDomain used in messages sent on
        # behalf of global time.
        self._domainId: Optional["PositiveInteger"] = None

    @property
    def domain_id(self) -> Optional["PositiveInteger"]:
        """Get domainId (Pythonic accessor)."""
        return self._domainId

    @domain_id.setter
    def domain_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set domainId with validation.
        
        Args:
            value: The domainId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._domainId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"domainId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._domainId = value
        # A GlobalTimeGateway may exist in the context of a actively update the global
        # time it is routed from one GlobalTimeDomain to atpVariation.
        self._gateway: List["GlobalTimeGateway"] = []

    @property
    def gateway(self) -> List["GlobalTimeGateway"]:
        """Get gateway (Pythonic accessor)."""
        return self._gateway
        # This represents the single master of a GlobalTime A GlobalTimeDomain may have
        # no GlobalTime when it gets its time from a GPS atpVariation.
        self._globalTime: Optional["GlobalTimeMaster"] = None

    @property
    def global_time(self) -> Optional["GlobalTimeMaster"]:
        """Get globalTime (Pythonic accessor)."""
        return self._globalTime

    @global_time.setter
    def global_time(self, value: Optional["GlobalTimeMaster"]) -> None:
        """
        Set globalTime with validation.
        
        Args:
            value: The globalTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._globalTime = None
            return

        if not isinstance(value, GlobalTimeMaster):
            raise TypeError(
                f"globalTime must be GlobalTimeMaster or None, got {type(value).__name__}"
            )
        self._globalTime = value
        # By this means it is possible to create a hierarchy of sub where one global
                # time domain can declare one other global time domains as its subDomains.
        # atpVariation.
        self._globalTimeSub: List["GlobalTimeDomain"] = []

    @property
    def global_time_sub(self) -> List["GlobalTimeDomain"]:
        """Get globalTimeSub (Pythonic accessor)."""
        return self._globalTimeSub
        # Defines the numerical identification of a GlobalTime sub domain.
        self._network: Optional["NetworkSegment"] = None

    @property
    def network(self) -> Optional["NetworkSegment"]:
        """Get network (Pythonic accessor)."""
        return self._network

    @network.setter
    def network(self, value: Optional["NetworkSegment"]) -> None:
        """
        Set network with validation.
        
        Args:
            value: The network to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._network = None
            return

        if not isinstance(value, NetworkSegment):
            raise TypeError(
                f"network must be NetworkSegment or None, got {type(value).__name__}"
            )
        self._network = value
        # Reference to a synchronized time domain this offset time is based on.
        # The reference source is the offset The reference target is the synchronized
                # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._offsetTime: Optional["GlobalTimeDomain"] = None

    @property
    def offset_time(self) -> Optional["GlobalTimeDomain"]:
        """Get offsetTime (Pythonic accessor)."""
        return self._offsetTime

    @offset_time.setter
    def offset_time(self, value: Optional["GlobalTimeDomain"]) -> None:
        """
        Set offsetTime with validation.
        
        Args:
            value: The offsetTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._offsetTime = None
            return

        if not isinstance(value, GlobalTimeDomain):
            raise TypeError(
                f"offsetTime must be GlobalTimeDomain or None, got {type(value).__name__}"
            )
        self._offsetTime = value
        # This PduTriggering will be taken to transmit the global from a
        # GlobalTimeMaster to a the atpVariation.
        self._pduTriggering: Optional["RefType"] = None

    @property
    def pdu_triggering(self) -> Optional["RefType"]:
        """Get pduTriggering (Pythonic accessor)."""
        return self._pduTriggering

    @pdu_triggering.setter
    def pdu_triggering(self, value: Optional["RefType"]) -> None:
        """
        Set pduTriggering with validation.
        
        Args:
            value: The pduTriggering to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pduTriggering = None
            return

        self._pduTriggering = value
        # This represents the collections of slaves of the Global GlobalTimeDomain may
                # have no Global when it propagates its time sub domains.
        # atpVariation.
        self._slave: List["GlobalTimeSlave"] = []

    @property
    def slave(self) -> List["GlobalTimeSlave"]:
        """Get slave (Pythonic accessor)."""
        return self._slave
        # This attribute describes the timeout for the situation that time
        # synchronization gets lost in the scope of the time.
        self._syncLoss: Optional["TimeValue"] = None

    @property
    def sync_loss(self) -> Optional["TimeValue"]:
        """Get syncLoss (Pythonic accessor)."""
        return self._syncLoss

    @sync_loss.setter
    def sync_loss(self, value: Optional["TimeValue"]) -> None:
        """
        Set syncLoss with validation.
        
        Args:
            value: The syncLoss to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncLoss = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"syncLoss must be TimeValue or None, got {type(value).__name__}"
            )
        self._syncLoss = value

    def with_gateway(self, value):
        """
        Set gateway and return self for chaining.

        Args:
            value: The gateway to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_gateway("value")
        """
        self.gateway = value  # Use property setter (gets validation)
        return self

    def with_global_time_sub(self, value):
        """
        Set global_time_sub and return self for chaining.

        Args:
            value: The global_time_sub to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_global_time_sub("value")
        """
        self.global_time_sub = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDebounceTime(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for debounceTime.
        
        Returns:
            The debounceTime value
        
        Note:
            Delegates to debounce_time property (CODING_RULE_V2_00017)
        """
        return self.debounce_time  # Delegates to property

    def setDebounceTime(self, value: "TimeValue") -> "GlobalTimeDomain":
        """
        AUTOSAR-compliant setter for debounceTime with method chaining.
        
        Args:
            value: The debounceTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to debounce_time property setter (gets validation automatically)
        """
        self.debounce_time = value  # Delegates to property setter
        return self

    def getDomainId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for domainId.
        
        Returns:
            The domainId value
        
        Note:
            Delegates to domain_id property (CODING_RULE_V2_00017)
        """
        return self.domain_id  # Delegates to property

    def setDomainId(self, value: "PositiveInteger") -> "GlobalTimeDomain":
        """
        AUTOSAR-compliant setter for domainId with method chaining.
        
        Args:
            value: The domainId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to domain_id property setter (gets validation automatically)
        """
        self.domain_id = value  # Delegates to property setter
        return self

    def getGateway(self) -> List["GlobalTimeGateway"]:
        """
        AUTOSAR-compliant getter for gateway.
        
        Returns:
            The gateway value
        
        Note:
            Delegates to gateway property (CODING_RULE_V2_00017)
        """
        return self.gateway  # Delegates to property

    def getGlobalTime(self) -> "GlobalTimeMaster":
        """
        AUTOSAR-compliant getter for globalTime.
        
        Returns:
            The globalTime value
        
        Note:
            Delegates to global_time property (CODING_RULE_V2_00017)
        """
        return self.global_time  # Delegates to property

    def setGlobalTime(self, value: "GlobalTimeMaster") -> "GlobalTimeDomain":
        """
        AUTOSAR-compliant setter for globalTime with method chaining.
        
        Args:
            value: The globalTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to global_time property setter (gets validation automatically)
        """
        self.global_time = value  # Delegates to property setter
        return self

    def getGlobalTimeSub(self) -> List["GlobalTimeDomain"]:
        """
        AUTOSAR-compliant getter for globalTimeSub.
        
        Returns:
            The globalTimeSub value
        
        Note:
            Delegates to global_time_sub property (CODING_RULE_V2_00017)
        """
        return self.global_time_sub  # Delegates to property

    def getNetwork(self) -> "NetworkSegment":
        """
        AUTOSAR-compliant getter for network.
        
        Returns:
            The network value
        
        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def setNetwork(self, value: "NetworkSegment") -> "GlobalTimeDomain":
        """
        AUTOSAR-compliant setter for network with method chaining.
        
        Args:
            value: The network to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to network property setter (gets validation automatically)
        """
        self.network = value  # Delegates to property setter
        return self

    def getOffsetTime(self) -> "GlobalTimeDomain":
        """
        AUTOSAR-compliant getter for offsetTime.
        
        Returns:
            The offsetTime value
        
        Note:
            Delegates to offset_time property (CODING_RULE_V2_00017)
        """
        return self.offset_time  # Delegates to property

    def setOffsetTime(self, value: "GlobalTimeDomain") -> "GlobalTimeDomain":
        """
        AUTOSAR-compliant setter for offsetTime with method chaining.
        
        Args:
            value: The offsetTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to offset_time property setter (gets validation automatically)
        """
        self.offset_time = value  # Delegates to property setter
        return self

    def getPduTriggering(self) -> "RefType":
        """
        AUTOSAR-compliant getter for pduTriggering.
        
        Returns:
            The pduTriggering value
        
        Note:
            Delegates to pdu_triggering property (CODING_RULE_V2_00017)
        """
        return self.pdu_triggering  # Delegates to property

    def setPduTriggering(self, value: "RefType") -> "GlobalTimeDomain":
        """
        AUTOSAR-compliant setter for pduTriggering with method chaining.
        
        Args:
            value: The pduTriggering to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pdu_triggering property setter (gets validation automatically)
        """
        self.pdu_triggering = value  # Delegates to property setter
        return self

    def getSlave(self) -> List["GlobalTimeSlave"]:
        """
        AUTOSAR-compliant getter for slave.
        
        Returns:
            The slave value
        
        Note:
            Delegates to slave property (CODING_RULE_V2_00017)
        """
        return self.slave  # Delegates to property

    def getSyncLoss(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for syncLoss.
        
        Returns:
            The syncLoss value
        
        Note:
            Delegates to sync_loss property (CODING_RULE_V2_00017)
        """
        return self.sync_loss  # Delegates to property

    def setSyncLoss(self, value: "TimeValue") -> "GlobalTimeDomain":
        """
        AUTOSAR-compliant setter for syncLoss with method chaining.
        
        Args:
            value: The syncLoss to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sync_loss property setter (gets validation automatically)
        """
        self.sync_loss = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_debounce_time(self, value: Optional["TimeValue"]) -> "GlobalTimeDomain":
        """
        Set debounceTime and return self for chaining.
        
        Args:
            value: The debounceTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_debounce_time("value")
        """
        self.debounce_time = value  # Use property setter (gets validation)
        return self

    def with_domain_id(self, value: Optional["PositiveInteger"]) -> "GlobalTimeDomain":
        """
        Set domainId and return self for chaining.
        
        Args:
            value: The domainId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_domain_id("value")
        """
        self.domain_id = value  # Use property setter (gets validation)
        return self

    def with_global_time(self, value: Optional["GlobalTimeMaster"]) -> "GlobalTimeDomain":
        """
        Set globalTime and return self for chaining.
        
        Args:
            value: The globalTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_global_time("value")
        """
        self.global_time = value  # Use property setter (gets validation)
        return self

    def with_network(self, value: Optional["NetworkSegment"]) -> "GlobalTimeDomain":
        """
        Set network and return self for chaining.
        
        Args:
            value: The network to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_network("value")
        """
        self.network = value  # Use property setter (gets validation)
        return self

    def with_offset_time(self, value: Optional["GlobalTimeDomain"]) -> "GlobalTimeDomain":
        """
        Set offsetTime and return self for chaining.
        
        Args:
            value: The offsetTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_offset_time("value")
        """
        self.offset_time = value  # Use property setter (gets validation)
        return self

    def with_pdu_triggering(self, value: Optional[RefType]) -> "GlobalTimeDomain":
        """
        Set pduTriggering and return self for chaining.
        
        Args:
            value: The pduTriggering to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pdu_triggering("value")
        """
        self.pdu_triggering = value  # Use property setter (gets validation)
        return self

    def with_sync_loss(self, value: Optional["TimeValue"]) -> "GlobalTimeDomain":
        """
        Set syncLoss and return self for chaining.
        
        Args:
            value: The syncLoss to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sync_loss("value")
        """
        self.sync_loss = value  # Use property setter (gets validation)
        return self



class AbstractGlobalTimeDomainProps(ARObject, ABC):
    """
    This abstract class enables a GlobalTimeDomain to specify additional
    properties.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::AbstractGlobalTimeDomainProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 859, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractGlobalTimeDomainProps:
            raise TypeError("AbstractGlobalTimeDomainProps is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class NetworkSegmentIdentification(ARObject):
    """
    This meta-class represents the ability to identify the PhysicalChannel on a
    system scope in a numerical way. One possible application of this approach
    is the Time Validation.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::NetworkSegmentIdentification
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 859, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the numerical identifier of a on system level
        # scope.
        self._network: Optional["PositiveInteger"] = None

    @property
    def network(self) -> Optional["PositiveInteger"]:
        """Get network (Pythonic accessor)."""
        return self._network

    @network.setter
    def network(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set network with validation.
        
        Args:
            value: The network to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._network = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"network must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._network = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNetwork(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for network.
        
        Returns:
            The network value
        
        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def setNetwork(self, value: "PositiveInteger") -> "NetworkSegmentIdentification":
        """
        AUTOSAR-compliant setter for network with method chaining.
        
        Args:
            value: The network to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to network property setter (gets validation automatically)
        """
        self.network = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_network(self, value: Optional["PositiveInteger"]) -> "NetworkSegmentIdentification":
        """
        Set network and return self for chaining.
        
        Args:
            value: The network to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_network("value")
        """
        self.network = value  # Use property setter (gets validation)
        return self



class GlobalTimeMaster(Identifiable, ABC):
    """
    This represents the generic concept of a global time master.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::GlobalTimeMaster
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 860, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is GlobalTimeMaster:
            raise TypeError("GlobalTimeMaster is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The GlobalTimeMaster is bound to the Communication Connector.
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
        # Defines whether an Integrity Check Value (ICV) shall be to the sent time sync
        # messages.
        self._icvSecured: Optional["GlobalTimeIcvSupport"] = None

    @property
    def icv_secured(self) -> Optional["GlobalTimeIcvSupport"]:
        """Get icvSecured (Pythonic accessor)."""
        return self._icvSecured

    @icv_secured.setter
    def icv_secured(self, value: Optional["GlobalTimeIcvSupport"]) -> None:
        """
        Set icvSecured with validation.
        
        Args:
            value: The icvSecured to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._icvSecured = None
            return

        if not isinstance(value, GlobalTimeIcvSupport):
            raise TypeError(
                f"icvSecured must be GlobalTimeIcvSupport or None, got {type(value).__name__}"
            )
        self._icvSecured = value
        # Defines the minimum time between an "immediate" and the next periodic
        # message.
        self._immediate: Optional["TimeValue"] = None

    @property
    def immediate(self) -> Optional["TimeValue"]:
        """Get immediate (Pythonic accessor)."""
        return self._immediate

    @immediate.setter
    def immediate(self, value: Optional["TimeValue"]) -> None:
        """
        Set immediate with validation.
        
        Args:
            value: The immediate to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._immediate = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"immediate must be TimeValue or None, got {type(value).__name__}"
            )
        self._immediate = value
        # If set to TRUE, the GlobalTimeMaster is supposed to act the root of global
        # time information.
        self._isSystemWide: Optional["Boolean"] = None

    @property
    def is_system_wide(self) -> Optional["Boolean"]:
        """Get isSystemWide (Pythonic accessor)."""
        return self._isSystemWide

    @is_system_wide.setter
    def is_system_wide(self, value: Optional["Boolean"]) -> None:
        """
        Set isSystemWide with validation.
        
        Args:
            value: The isSystemWide to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isSystemWide = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isSystemWide must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isSystemWide = value
        # This represents the period.
        # Unit: seconds.
        self._syncPeriod: Optional["TimeValue"] = None

    @property
    def sync_period(self) -> Optional["TimeValue"]:
        """Get syncPeriod (Pythonic accessor)."""
        return self._syncPeriod

    @sync_period.setter
    def sync_period(self, value: Optional["TimeValue"]) -> None:
        """
        Set syncPeriod with validation.
        
        Args:
            value: The syncPeriod to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncPeriod = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"syncPeriod must be TimeValue or None, got {type(value).__name__}"
            )
        self._syncPeriod = value

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

    def setCommunication(self, value: "Communication") -> "GlobalTimeMaster":
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

    def getIcvSecured(self) -> "GlobalTimeIcvSupport":
        """
        AUTOSAR-compliant getter for icvSecured.
        
        Returns:
            The icvSecured value
        
        Note:
            Delegates to icv_secured property (CODING_RULE_V2_00017)
        """
        return self.icv_secured  # Delegates to property

    def setIcvSecured(self, value: "GlobalTimeIcvSupport") -> "GlobalTimeMaster":
        """
        AUTOSAR-compliant setter for icvSecured with method chaining.
        
        Args:
            value: The icvSecured to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to icv_secured property setter (gets validation automatically)
        """
        self.icv_secured = value  # Delegates to property setter
        return self

    def getImmediate(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for immediate.
        
        Returns:
            The immediate value
        
        Note:
            Delegates to immediate property (CODING_RULE_V2_00017)
        """
        return self.immediate  # Delegates to property

    def setImmediate(self, value: "TimeValue") -> "GlobalTimeMaster":
        """
        AUTOSAR-compliant setter for immediate with method chaining.
        
        Args:
            value: The immediate to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to immediate property setter (gets validation automatically)
        """
        self.immediate = value  # Delegates to property setter
        return self

    def getIsSystemWide(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isSystemWide.
        
        Returns:
            The isSystemWide value
        
        Note:
            Delegates to is_system_wide property (CODING_RULE_V2_00017)
        """
        return self.is_system_wide  # Delegates to property

    def setIsSystemWide(self, value: "Boolean") -> "GlobalTimeMaster":
        """
        AUTOSAR-compliant setter for isSystemWide with method chaining.
        
        Args:
            value: The isSystemWide to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to is_system_wide property setter (gets validation automatically)
        """
        self.is_system_wide = value  # Delegates to property setter
        return self

    def getSyncPeriod(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for syncPeriod.
        
        Returns:
            The syncPeriod value
        
        Note:
            Delegates to sync_period property (CODING_RULE_V2_00017)
        """
        return self.sync_period  # Delegates to property

    def setSyncPeriod(self, value: "TimeValue") -> "GlobalTimeMaster":
        """
        AUTOSAR-compliant setter for syncPeriod with method chaining.
        
        Args:
            value: The syncPeriod to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sync_period property setter (gets validation automatically)
        """
        self.sync_period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional["Communication"]) -> "GlobalTimeMaster":
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

    def with_icv_secured(self, value: Optional["GlobalTimeIcvSupport"]) -> "GlobalTimeMaster":
        """
        Set icvSecured and return self for chaining.
        
        Args:
            value: The icvSecured to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_icv_secured("value")
        """
        self.icv_secured = value  # Use property setter (gets validation)
        return self

    def with_immediate(self, value: Optional["TimeValue"]) -> "GlobalTimeMaster":
        """
        Set immediate and return self for chaining.
        
        Args:
            value: The immediate to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_immediate("value")
        """
        self.immediate = value  # Use property setter (gets validation)
        return self

    def with_is_system_wide(self, value: Optional["Boolean"]) -> "GlobalTimeMaster":
        """
        Set isSystemWide and return self for chaining.
        
        Args:
            value: The isSystemWide to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_is_system_wide("value")
        """
        self.is_system_wide = value  # Use property setter (gets validation)
        return self

    def with_sync_period(self, value: Optional["TimeValue"]) -> "GlobalTimeMaster":
        """
        Set syncPeriod and return self for chaining.
        
        Args:
            value: The syncPeriod to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sync_period("value")
        """
        self.sync_period = value  # Use property setter (gets validation)
        return self



class GlobalTimeSlave(Identifiable, ABC):
    """
    This represents the generic concept of a global time slave.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::GlobalTimeSlave
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 860, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is GlobalTimeSlave:
            raise TypeError("GlobalTimeSlave is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The GlobalTimeSlave is bound to the Communication Connector.
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
        # Rx timeout for the follow-up message.
        self._followUpTimeoutValue: Optional["TimeValue"] = None

    @property
    def follow_up_timeout_value(self) -> Optional["TimeValue"]:
        """Get followUpTimeoutValue (Pythonic accessor)."""
        return self._followUpTimeoutValue

    @follow_up_timeout_value.setter
    def follow_up_timeout_value(self, value: Optional["TimeValue"]) -> None:
        """
        Set followUpTimeoutValue with validation.
        
        Args:
            value: The followUpTimeoutValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._followUpTimeoutValue = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"followUpTimeoutValue must be TimeValue or None, got {type(value).__name__}"
            )
        self._followUpTimeoutValue = value
        # Defines how an Integrity Check Value (ICV) shall be at the receiver.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._icvVerification: Optional["GlobalTimeIcv"] = None

    @property
    def icv_verification(self) -> Optional["GlobalTimeIcv"]:
        """Get icvVerification (Pythonic accessor)."""
        return self._icvVerification

    @icv_verification.setter
    def icv_verification(self, value: Optional["GlobalTimeIcv"]) -> None:
        """
        Set icvVerification with validation.
        
        Args:
            value: The icvVerification to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._icvVerification = None
            return

        if not isinstance(value, GlobalTimeIcv):
            raise TypeError(
                f"icvVerification must be GlobalTimeIcv or None, got {type(value).__name__}"
            )
        self._icvVerification = value
        # Defines the maximum allowed positive difference the current Local Time Base
        # value and a newly Time Base value.
        self._timeLeapFuture: Optional["TimeValue"] = None

    @property
    def time_leap_future(self) -> Optional["TimeValue"]:
        """Get timeLeapFuture (Pythonic accessor)."""
        return self._timeLeapFuture

    @time_leap_future.setter
    def time_leap_future(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeLeapFuture with validation.
        
        Args:
            value: The timeLeapFuture to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeLeapFuture = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeLeapFuture must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeLeapFuture = value
        # Defines the required number of updates to the Time Base the time difference
        # to the previous received value remain within the bounds of timeLeapFuture
        # timeLeapPastThreshold until that Time.
        self._timeLeap: Optional["PositiveInteger"] = None

    @property
    def time_leap(self) -> Optional["PositiveInteger"]:
        """Get timeLeap (Pythonic accessor)."""
        return self._timeLeap

    @time_leap.setter
    def time_leap(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set timeLeap with validation.
        
        Args:
            value: The timeLeap to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeLeap = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"timeLeap must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._timeLeap = value
        # Defines the maximum allowed negative difference the current Local Time Base
        # value and a newly Time Base value.
        self._timeLeapPast: Optional["TimeValue"] = None

    @property
    def time_leap_past(self) -> Optional["TimeValue"]:
        """Get timeLeapPast (Pythonic accessor)."""
        return self._timeLeapPast

    @time_leap_past.setter
    def time_leap_past(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeLeapPast with validation.
        
        Args:
            value: The timeLeapPast to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeLeapPast = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeLeapPast must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeLeapPast = value

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

    def setCommunication(self, value: "Communication") -> "GlobalTimeSlave":
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

    def getFollowUpTimeoutValue(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for followUpTimeoutValue.
        
        Returns:
            The followUpTimeoutValue value
        
        Note:
            Delegates to follow_up_timeout_value property (CODING_RULE_V2_00017)
        """
        return self.follow_up_timeout_value  # Delegates to property

    def setFollowUpTimeoutValue(self, value: "TimeValue") -> "GlobalTimeSlave":
        """
        AUTOSAR-compliant setter for followUpTimeoutValue with method chaining.
        
        Args:
            value: The followUpTimeoutValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to follow_up_timeout_value property setter (gets validation automatically)
        """
        self.follow_up_timeout_value = value  # Delegates to property setter
        return self

    def getIcvVerification(self) -> "GlobalTimeIcv":
        """
        AUTOSAR-compliant getter for icvVerification.
        
        Returns:
            The icvVerification value
        
        Note:
            Delegates to icv_verification property (CODING_RULE_V2_00017)
        """
        return self.icv_verification  # Delegates to property

    def setIcvVerification(self, value: "GlobalTimeIcv") -> "GlobalTimeSlave":
        """
        AUTOSAR-compliant setter for icvVerification with method chaining.
        
        Args:
            value: The icvVerification to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to icv_verification property setter (gets validation automatically)
        """
        self.icv_verification = value  # Delegates to property setter
        return self

    def getTimeLeapFuture(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeLeapFuture.
        
        Returns:
            The timeLeapFuture value
        
        Note:
            Delegates to time_leap_future property (CODING_RULE_V2_00017)
        """
        return self.time_leap_future  # Delegates to property

    def setTimeLeapFuture(self, value: "TimeValue") -> "GlobalTimeSlave":
        """
        AUTOSAR-compliant setter for timeLeapFuture with method chaining.
        
        Args:
            value: The timeLeapFuture to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to time_leap_future property setter (gets validation automatically)
        """
        self.time_leap_future = value  # Delegates to property setter
        return self

    def getTimeLeap(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for timeLeap.
        
        Returns:
            The timeLeap value
        
        Note:
            Delegates to time_leap property (CODING_RULE_V2_00017)
        """
        return self.time_leap  # Delegates to property

    def setTimeLeap(self, value: "PositiveInteger") -> "GlobalTimeSlave":
        """
        AUTOSAR-compliant setter for timeLeap with method chaining.
        
        Args:
            value: The timeLeap to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to time_leap property setter (gets validation automatically)
        """
        self.time_leap = value  # Delegates to property setter
        return self

    def getTimeLeapPast(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeLeapPast.
        
        Returns:
            The timeLeapPast value
        
        Note:
            Delegates to time_leap_past property (CODING_RULE_V2_00017)
        """
        return self.time_leap_past  # Delegates to property

    def setTimeLeapPast(self, value: "TimeValue") -> "GlobalTimeSlave":
        """
        AUTOSAR-compliant setter for timeLeapPast with method chaining.
        
        Args:
            value: The timeLeapPast to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to time_leap_past property setter (gets validation automatically)
        """
        self.time_leap_past = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional["Communication"]) -> "GlobalTimeSlave":
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

    def with_follow_up_timeout_value(self, value: Optional["TimeValue"]) -> "GlobalTimeSlave":
        """
        Set followUpTimeoutValue and return self for chaining.
        
        Args:
            value: The followUpTimeoutValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_follow_up_timeout_value("value")
        """
        self.follow_up_timeout_value = value  # Use property setter (gets validation)
        return self

    def with_icv_verification(self, value: Optional["GlobalTimeIcv"]) -> "GlobalTimeSlave":
        """
        Set icvVerification and return self for chaining.
        
        Args:
            value: The icvVerification to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_icv_verification("value")
        """
        self.icv_verification = value  # Use property setter (gets validation)
        return self

    def with_time_leap_future(self, value: Optional["TimeValue"]) -> "GlobalTimeSlave":
        """
        Set timeLeapFuture and return self for chaining.
        
        Args:
            value: The timeLeapFuture to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_time_leap_future("value")
        """
        self.time_leap_future = value  # Use property setter (gets validation)
        return self

    def with_time_leap(self, value: Optional["PositiveInteger"]) -> "GlobalTimeSlave":
        """
        Set timeLeap and return self for chaining.
        
        Args:
            value: The timeLeap to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_time_leap("value")
        """
        self.time_leap = value  # Use property setter (gets validation)
        return self

    def with_time_leap_past(self, value: Optional["TimeValue"]) -> "GlobalTimeSlave":
        """
        Set timeLeapPast and return self for chaining.
        
        Args:
            value: The timeLeapPast to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_time_leap_past("value")
        """
        self.time_leap_past = value  # Use property setter (gets validation)
        return self



class GlobalTimeGateway(Identifiable):
    """
    This represents the ability to define a time gateway for establishing a
    global time domain over several communication clusters.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::GlobalTimeGateway
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 861, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The GlobalTimeGateway is hosted by the referenced Ecu.
        self._host: Optional["EcuInstance"] = None

    @property
    def host(self) -> Optional["EcuInstance"]:
        """Get host (Pythonic accessor)."""
        return self._host

    @host.setter
    def host(self, value: Optional["EcuInstance"]) -> None:
        """
        Set host with validation.
        
        Args:
            value: The host to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._host = None
            return

        if not isinstance(value, EcuInstance):
            raise TypeError(
                f"host must be EcuInstance or None, got {type(value).__name__}"
            )
        self._host = value
        # This represents the master of the global time gateway.
        self._master: Optional["GlobalTimeMaster"] = None

    @property
    def master(self) -> Optional["GlobalTimeMaster"]:
        """Get master (Pythonic accessor)."""
        return self._master

    @master.setter
    def master(self, value: Optional["GlobalTimeMaster"]) -> None:
        """
        Set master with validation.
        
        Args:
            value: The master to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._master = None
            return

        if not isinstance(value, GlobalTimeMaster):
            raise TypeError(
                f"master must be GlobalTimeMaster or None, got {type(value).__name__}"
            )
        self._master = value
        # This represents the slave of the GlobalTimeGateway.
        self._slave: Optional["GlobalTimeSlave"] = None

    @property
    def slave(self) -> Optional["GlobalTimeSlave"]:
        """Get slave (Pythonic accessor)."""
        return self._slave

    @slave.setter
    def slave(self, value: Optional["GlobalTimeSlave"]) -> None:
        """
        Set slave with validation.
        
        Args:
            value: The slave to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._slave = None
            return

        if not isinstance(value, GlobalTimeSlave):
            raise TypeError(
                f"slave must be GlobalTimeSlave or None, got {type(value).__name__}"
            )
        self._slave = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHost(self) -> "EcuInstance":
        """
        AUTOSAR-compliant getter for host.
        
        Returns:
            The host value
        
        Note:
            Delegates to host property (CODING_RULE_V2_00017)
        """
        return self.host  # Delegates to property

    def setHost(self, value: "EcuInstance") -> "GlobalTimeGateway":
        """
        AUTOSAR-compliant setter for host with method chaining.
        
        Args:
            value: The host to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to host property setter (gets validation automatically)
        """
        self.host = value  # Delegates to property setter
        return self

    def getMaster(self) -> "GlobalTimeMaster":
        """
        AUTOSAR-compliant getter for master.
        
        Returns:
            The master value
        
        Note:
            Delegates to master property (CODING_RULE_V2_00017)
        """
        return self.master  # Delegates to property

    def setMaster(self, value: "GlobalTimeMaster") -> "GlobalTimeGateway":
        """
        AUTOSAR-compliant setter for master with method chaining.
        
        Args:
            value: The master to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to master property setter (gets validation automatically)
        """
        self.master = value  # Delegates to property setter
        return self

    def getSlave(self) -> "GlobalTimeSlave":
        """
        AUTOSAR-compliant getter for slave.
        
        Returns:
            The slave value
        
        Note:
            Delegates to slave property (CODING_RULE_V2_00017)
        """
        return self.slave  # Delegates to property

    def setSlave(self, value: "GlobalTimeSlave") -> "GlobalTimeGateway":
        """
        AUTOSAR-compliant setter for slave with method chaining.
        
        Args:
            value: The slave to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to slave property setter (gets validation automatically)
        """
        self.slave = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_host(self, value: Optional["EcuInstance"]) -> "GlobalTimeGateway":
        """
        Set host and return self for chaining.
        
        Args:
            value: The host to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_host("value")
        """
        self.host = value  # Use property setter (gets validation)
        return self

    def with_master(self, value: Optional["GlobalTimeMaster"]) -> "GlobalTimeGateway":
        """
        Set master and return self for chaining.
        
        Args:
            value: The master to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_master("value")
        """
        self.master = value  # Use property setter (gets validation)
        return self

    def with_slave(self, value: Optional["GlobalTimeSlave"]) -> "GlobalTimeGateway":
        """
        Set slave and return self for chaining.
        
        Args:
            value: The slave to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_slave("value")
        """
        self.slave = value  # Use property setter (gets validation)
        return self



class GlobalTimeCorrectionProps(ARObject):
    """
    This meta-class defines the attributes for rate and offset correction.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::GlobalTimeCorrectionProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 862, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Threshold for the correction method.
        # Deviations below value will be corrected by a linear reduction over a Values
                # equal- and greater than this be corrected by immediately setting the correct
                # rate in form of a jump.
        self._offsetCorrection: Optional["TimeValue"] = None

    @property
    def offset_correction(self) -> Optional["TimeValue"]:
        """Get offsetCorrection (Pythonic accessor)."""
        return self._offsetCorrection

    @offset_correction.setter
    def offset_correction(self, value: Optional["TimeValue"]) -> None:
        """
        Set offsetCorrection with validation.
        
        Args:
            value: The offsetCorrection to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._offsetCorrection = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"offsetCorrection must be TimeValue or None, got {type(value).__name__}"
            )
        self._offsetCorrection = value
        # Definition of the time span which is used to calculate the deviation.
        self._rateCorrection: Optional["TimeValue"] = None

    @property
    def rate_correction(self) -> Optional["TimeValue"]:
        """Get rateCorrection (Pythonic accessor)."""
        return self._rateCorrection

    @rate_correction.setter
    def rate_correction(self, value: Optional["TimeValue"]) -> None:
        """
        Set rateCorrection with validation.
        
        Args:
            value: The rateCorrection to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rateCorrection = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"rateCorrection must be TimeValue or None, got {type(value).__name__}"
            )
        self._rateCorrection = value
        # Defines the number of simultaneous rate measurements determine the current
        # rate deviation.
        self._rateCorrections: Optional["PositiveInteger"] = None

    @property
    def rate_corrections(self) -> Optional["PositiveInteger"]:
        """Get rateCorrections (Pythonic accessor)."""
        return self._rateCorrections

    @rate_corrections.setter
    def rate_corrections(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set rateCorrections with validation.
        
        Args:
            value: The rateCorrections to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rateCorrections = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"rateCorrections must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._rateCorrections = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOffsetCorrection(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for offsetCorrection.
        
        Returns:
            The offsetCorrection value
        
        Note:
            Delegates to offset_correction property (CODING_RULE_V2_00017)
        """
        return self.offset_correction  # Delegates to property

    def setOffsetCorrection(self, value: "TimeValue") -> "GlobalTimeCorrectionProps":
        """
        AUTOSAR-compliant setter for offsetCorrection with method chaining.
        
        Args:
            value: The offsetCorrection to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to offset_correction property setter (gets validation automatically)
        """
        self.offset_correction = value  # Delegates to property setter
        return self

    def getRateCorrection(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for rateCorrection.
        
        Returns:
            The rateCorrection value
        
        Note:
            Delegates to rate_correction property (CODING_RULE_V2_00017)
        """
        return self.rate_correction  # Delegates to property

    def setRateCorrection(self, value: "TimeValue") -> "GlobalTimeCorrectionProps":
        """
        AUTOSAR-compliant setter for rateCorrection with method chaining.
        
        Args:
            value: The rateCorrection to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rate_correction property setter (gets validation automatically)
        """
        self.rate_correction = value  # Delegates to property setter
        return self

    def getRateCorrections(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for rateCorrections.
        
        Returns:
            The rateCorrections value
        
        Note:
            Delegates to rate_corrections property (CODING_RULE_V2_00017)
        """
        return self.rate_corrections  # Delegates to property

    def setRateCorrections(self, value: "PositiveInteger") -> "GlobalTimeCorrectionProps":
        """
        AUTOSAR-compliant setter for rateCorrections with method chaining.
        
        Args:
            value: The rateCorrections to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rate_corrections property setter (gets validation automatically)
        """
        self.rate_corrections = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_offset_correction(self, value: Optional["TimeValue"]) -> "GlobalTimeCorrectionProps":
        """
        Set offsetCorrection and return self for chaining.
        
        Args:
            value: The offsetCorrection to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_offset_correction("value")
        """
        self.offset_correction = value  # Use property setter (gets validation)
        return self

    def with_rate_correction(self, value: Optional["TimeValue"]) -> "GlobalTimeCorrectionProps":
        """
        Set rateCorrection and return self for chaining.
        
        Args:
            value: The rateCorrection to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rate_correction("value")
        """
        self.rate_correction = value  # Use property setter (gets validation)
        return self

    def with_rate_corrections(self, value: Optional["PositiveInteger"]) -> "GlobalTimeCorrectionProps":
        """
        Set rateCorrections and return self for chaining.
        
        Args:
            value: The rateCorrections to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rate_corrections("value")
        """
        self.rate_corrections = value  # Use property setter (gets validation)
        return self


class GlobalTimeCrcSupportEnum(AREnum):
    """
    GlobalTimeCrcSupportEnum enumeration

This enumeration is used to define whether and how CRC on the TX side shall be utilized. Aggregated by GlobalTimeCanMaster.crcSecured, GlobalTimeEthMaster.crcSecured, GlobalTimeFrMaster.crc Secured

Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime
    """
    # This indicates that CRC is not supported
    crcNotSupported = "0"

    # This indicates that CRC is supported
    crcSupported = "1"



class GlobalTimeCrcValidationEnum(AREnum):
    """
    GlobalTimeCrcValidationEnum enumeration

This enumeration provides values for the evaluation of the CRC Aggregated by GlobalTimeCanSlave.crcValidated, GlobalTimeEthSlave.crcValidated, GlobalTimeFrSlave.crc Validated

Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime
    """
    # The CRC is supposed to be ignored
    crcIgnored = "0"

    # The CRC is not supposed to be present. If CRC is present the message is ignored.
    crcNotValidated = "1"

    # Either the CRC is present and then shall be validated or the CRC is not present and no CRC check is
    crcOptional = "3"

    # This CRC is supposed to be validated.
    crcValidated = "2"



class GlobalTimeIcvSupportEnum(AREnum):
    """
    GlobalTimeIcvSupportEnum enumeration

Defines whether an Integrity Check Value (ICV) shall be added to the sent time sync messages. Tags: atp.Status=candidate Aggregated by GlobalTimeMaster.icvSecured

Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime
    """
    # The ICV is not supported
    icvNotSupported = "1"

    # The ICV is supported
    icvSupported = "0"



class GlobalTimeIcvVerificationEnum(AREnum):
    """
    GlobalTimeIcvVerificationEnum enumeration

This enumeration is used to define how an Integrity Check Value (ICV) shall be handled at the receiver. Tags: atp.Status=candidate Aggregated by GlobalTimeSlave.icvVerification

Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime
    """
    # If the ICV is present, then it is ignored
    icvIgnored = "2"

    # The ICV is not supposed to be present. If the ICV is present, then the message is ignored.
    icvNotVerified = "1"

    # If the ICV is present, then it will be verified. If the ICV is not present, then this is also a valid reception
    icvOptional = "3"

    # The ICV is required and will be verified.
    icvVerified = "0"


__all__ = [
    "GlobalTimeDomain",
    "AbstractGlobalTimeDomainProps",
    "NetworkSegmentIdentification",
    "GlobalTimeMaster",
    "GlobalTimeSlave",
    "GlobalTimeGateway",
    "GlobalTimeCorrectionProps",
    "GlobalTimeCrcSupportEnum",
    "GlobalTimeCrcValidationEnum",
    "GlobalTimeIcvSupportEnum",
    "GlobalTimeIcvVerificationEnum",
]
