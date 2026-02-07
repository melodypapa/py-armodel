from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"domainId must be PositiveInteger or None, got {type(value).__name__}"
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
        self._pduTriggering: RefType = None

    @property
    def pdu_triggering(self) -> RefType:
        """Get pduTriggering (Pythonic accessor)."""
        return self._pduTriggering

    @pdu_triggering.setter
    def pdu_triggering(self, value: RefType) -> None:
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

    def getPduTriggering(self) -> RefType:
        """
        AUTOSAR-compliant getter for pduTriggering.
        
        Returns:
            The pduTriggering value
        
        Note:
            Delegates to pdu_triggering property (CODING_RULE_V2_00017)
        """
        return self.pdu_triggering  # Delegates to property

    def setPduTriggering(self, value: RefType) -> "GlobalTimeDomain":
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