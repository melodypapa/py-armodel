"""
AUTOSAR Package - DiagnosticEvent

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    NameToken,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.__init__ import (
    DiagnosticMapping,
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


class DiagnosticEvent(DiagnosticCommonElement):
    """
    This element is used to configure DiagnosticEvents. (cid:53) 164 of 719
    Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Diagnostic Extract
    Template AUTOSAR CP R23-11 (cid:52)
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent::DiagnosticEvent
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 164, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the identification number that is with the
                # enclosing DiagnosticEvent and allows identify it when placed into a snapshot
                # record or record storage.
        # can be reported as internal data element in or extended data records.
        self._associated: Optional["PositiveInteger"] = None

    @property
    def associated(self) -> Optional["PositiveInteger"]:
        """Get associated (Pythonic accessor)."""
        return self._associated

    @associated.setter
    def associated(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set associated with validation.
        
        Args:
            value: The associated to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._associated = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"associated must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._associated = value
        # This attribute defines the resulting UDS status byte for the related event,
        # which shall not be cleared according to the callback.
        self._clearEvent: Optional["DiagnosticClearEvent"] = None

    @property
    def clear_event(self) -> Optional["DiagnosticClearEvent"]:
        """Get clearEvent (Pythonic accessor)."""
        return self._clearEvent

    @clear_event.setter
    def clear_event(self, value: Optional["DiagnosticClearEvent"]) -> None:
        """
        Set clearEvent with validation.
        
        Args:
            value: The clearEvent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clearEvent = None
            return

        if not isinstance(value, DiagnosticClearEvent):
            raise TypeError(
                f"clearEvent must be DiagnosticClearEvent or None, got {type(value).__name__}"
            )
        self._clearEvent = value
        # This attribute defines the number of operation cycles with failed result
                # before a confirmed DTC is set to 1.
        # The this attribute is a by "1" increased value the confirmation threshold of
                # the "trip in ISO 14229-1 in figure D.
        # 4.
        # A value defines the immediate confirmation of the DTC the first reported
                # failed.
        # This is also sometimes trip DTC".
        # A value of "2" defines a DTC the operation cycle after the first occurred
                # value of "2" is typically used in the US for OBD.
        self._confirmation: Optional["PositiveInteger"] = None

    @property
    def confirmation(self) -> Optional["PositiveInteger"]:
        """Get confirmation (Pythonic accessor)."""
        return self._confirmation

    @confirmation.setter
    def confirmation(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set confirmation with validation.
        
        Args:
            value: The confirmation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._confirmation = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"confirmation must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._confirmation = value
        # Event specific description of Indicators.
        # Stereotypes: atpSplitable; atpVariation.
        self._connected: List["DiagnosticConnected"] = []

    @property
    def connected(self) -> List["DiagnosticConnected"]:
        """Get connected (Pythonic accessor)."""
        return self._connected
        # This attribute defines whether the Dem has access to a "ClearEventAllowed"
        # callback.
        self._eventClear: Optional["DiagnosticEventClear"] = None

    @property
    def event_clear(self) -> Optional["DiagnosticEventClear"]:
        """Get eventClear (Pythonic accessor)."""
        return self._eventClear

    @event_clear.setter
    def event_clear(self, value: Optional["DiagnosticEventClear"]) -> None:
        """
        Set eventClear with validation.
        
        Args:
            value: The eventClear to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventClear = None
            return

        if not isinstance(value, DiagnosticEventClear):
            raise TypeError(
                f"eventClear must be DiagnosticEventClear or None, got {type(value).__name__}"
            )
        self._eventClear = value
        # This attribute is used to distinguish between SWC and events.
        self._eventKind: Optional["DiagnosticEventKind"] = None

    @property
    def event_kind(self) -> Optional["DiagnosticEventKind"]:
        """Get eventKind (Pythonic accessor)."""
        return self._eventKind

    @event_kind.setter
    def event_kind(self, value: Optional["DiagnosticEventKind"]) -> None:
        """
        Set eventKind with validation.
        
        Args:
            value: The eventKind to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventKind = None
            return

        if not isinstance(value, DiagnosticEventKind):
            raise TypeError(
                f"eventKind must be DiagnosticEventKind or None, got {type(value).__name__}"
            )
        self._eventKind = value
        # This attribute describes whether the Prestorage of Freeze is supported by the
                # assigned event or not.
        # of FreezeFrames is supported of FreezeFrames is not supported.
        self._prestorage: Optional["Boolean"] = None

    @property
    def prestorage(self) -> Optional["Boolean"]:
        """Get prestorage (Pythonic accessor)."""
        return self._prestorage

    @prestorage.setter
    def prestorage(self, value: Optional["Boolean"]) -> None:
        """
        Set prestorage with validation.
        
        Args:
            value: The prestorage to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._prestorage = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"prestorage must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._prestorage = value
        # If the Event uses a prestored freeze-frame (using the PrestoreFreezeFrame and
                # ClearPrestored of the service interface DiagnosticMonitor) indicates if the
                # Event requires the data to be non-volatile memory.
        # TRUE = Dem shall store data in non-volatile memory, FALSE = Data lost at
                # shutdown (not stored in Nvm).
        self._prestored: Optional["Boolean"] = None

    @property
    def prestored(self) -> Optional["Boolean"]:
        """Get prestored (Pythonic accessor)."""
        return self._prestored

    @prestored.setter
    def prestored(self, value: Optional["Boolean"]) -> None:
        """
        Set prestored with validation.
        
        Args:
            value: The prestored to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._prestored = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"prestored must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._prestored = value
        # If the attribute is set to true then reporting PASSED will the indication of
        # a failed test in the current operation If the attribute is set to false then
        # reporting be ignored and not lead to a reset of the a failed test.
        self._recoverableIn: Optional["Boolean"] = None

    @property
    def recoverable_in(self) -> Optional["Boolean"]:
        """Get recoverableIn (Pythonic accessor)."""
        return self._recoverableIn

    @recoverable_in.setter
    def recoverable_in(self, value: Optional["Boolean"]) -> None:
        """
        Set recoverableIn with validation.
        
        Args:
            value: The recoverableIn to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._recoverableIn = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"recoverableIn must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._recoverableIn = value

    def with_connected(self, value):
        """
        Set connected and return self for chaining.

        Args:
            value: The connected to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_connected("value")
        """
        self.connected = value  # Use property setter (gets validation)
        return self

    def with_iumpr(self, value):
        """
        Set iumpr and return self for chaining.

        Args:
            value: The iumpr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_iumpr("value")
        """
        self.iumpr = value  # Use property setter (gets validation)
        return self

    def with_iumpr(self, value):
        """
        Set iumpr and return self for chaining.

        Args:
            value: The iumpr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_iumpr("value")
        """
        self.iumpr = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssociated(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for associated.
        
        Returns:
            The associated value
        
        Note:
            Delegates to associated property (CODING_RULE_V2_00017)
        """
        return self.associated  # Delegates to property

    def setAssociated(self, value: "PositiveInteger") -> "DiagnosticEvent":
        """
        AUTOSAR-compliant setter for associated with method chaining.
        
        Args:
            value: The associated to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to associated property setter (gets validation automatically)
        """
        self.associated = value  # Delegates to property setter
        return self

    def getClearEvent(self) -> "DiagnosticClearEvent":
        """
        AUTOSAR-compliant getter for clearEvent.
        
        Returns:
            The clearEvent value
        
        Note:
            Delegates to clear_event property (CODING_RULE_V2_00017)
        """
        return self.clear_event  # Delegates to property

    def setClearEvent(self, value: "DiagnosticClearEvent") -> "DiagnosticEvent":
        """
        AUTOSAR-compliant setter for clearEvent with method chaining.
        
        Args:
            value: The clearEvent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to clear_event property setter (gets validation automatically)
        """
        self.clear_event = value  # Delegates to property setter
        return self

    def getConfirmation(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for confirmation.
        
        Returns:
            The confirmation value
        
        Note:
            Delegates to confirmation property (CODING_RULE_V2_00017)
        """
        return self.confirmation  # Delegates to property

    def setConfirmation(self, value: "PositiveInteger") -> "DiagnosticEvent":
        """
        AUTOSAR-compliant setter for confirmation with method chaining.
        
        Args:
            value: The confirmation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to confirmation property setter (gets validation automatically)
        """
        self.confirmation = value  # Delegates to property setter
        return self

    def getConnected(self) -> List["DiagnosticConnected"]:
        """
        AUTOSAR-compliant getter for connected.
        
        Returns:
            The connected value
        
        Note:
            Delegates to connected property (CODING_RULE_V2_00017)
        """
        return self.connected  # Delegates to property

    def getEventClear(self) -> "DiagnosticEventClear":
        """
        AUTOSAR-compliant getter for eventClear.
        
        Returns:
            The eventClear value
        
        Note:
            Delegates to event_clear property (CODING_RULE_V2_00017)
        """
        return self.event_clear  # Delegates to property

    def setEventClear(self, value: "DiagnosticEventClear") -> "DiagnosticEvent":
        """
        AUTOSAR-compliant setter for eventClear with method chaining.
        
        Args:
            value: The eventClear to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event_clear property setter (gets validation automatically)
        """
        self.event_clear = value  # Delegates to property setter
        return self

    def getEventKind(self) -> "DiagnosticEventKind":
        """
        AUTOSAR-compliant getter for eventKind.
        
        Returns:
            The eventKind value
        
        Note:
            Delegates to event_kind property (CODING_RULE_V2_00017)
        """
        return self.event_kind  # Delegates to property

    def setEventKind(self, value: "DiagnosticEventKind") -> "DiagnosticEvent":
        """
        AUTOSAR-compliant setter for eventKind with method chaining.
        
        Args:
            value: The eventKind to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event_kind property setter (gets validation automatically)
        """
        self.event_kind = value  # Delegates to property setter
        return self

    def getPrestorage(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for prestorage.
        
        Returns:
            The prestorage value
        
        Note:
            Delegates to prestorage property (CODING_RULE_V2_00017)
        """
        return self.prestorage  # Delegates to property

    def setPrestorage(self, value: "Boolean") -> "DiagnosticEvent":
        """
        AUTOSAR-compliant setter for prestorage with method chaining.
        
        Args:
            value: The prestorage to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to prestorage property setter (gets validation automatically)
        """
        self.prestorage = value  # Delegates to property setter
        return self

    def getPrestored(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for prestored.
        
        Returns:
            The prestored value
        
        Note:
            Delegates to prestored property (CODING_RULE_V2_00017)
        """
        return self.prestored  # Delegates to property

    def setPrestored(self, value: "Boolean") -> "DiagnosticEvent":
        """
        AUTOSAR-compliant setter for prestored with method chaining.
        
        Args:
            value: The prestored to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to prestored property setter (gets validation automatically)
        """
        self.prestored = value  # Delegates to property setter
        return self

    def getRecoverableIn(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for recoverableIn.
        
        Returns:
            The recoverableIn value
        
        Note:
            Delegates to recoverable_in property (CODING_RULE_V2_00017)
        """
        return self.recoverable_in  # Delegates to property

    def setRecoverableIn(self, value: "Boolean") -> "DiagnosticEvent":
        """
        AUTOSAR-compliant setter for recoverableIn with method chaining.
        
        Args:
            value: The recoverableIn to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to recoverable_in property setter (gets validation automatically)
        """
        self.recoverable_in = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_associated(self, value: Optional["PositiveInteger"]) -> "DiagnosticEvent":
        """
        Set associated and return self for chaining.
        
        Args:
            value: The associated to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_associated("value")
        """
        self.associated = value  # Use property setter (gets validation)
        return self

    def with_clear_event(self, value: Optional["DiagnosticClearEvent"]) -> "DiagnosticEvent":
        """
        Set clearEvent and return self for chaining.
        
        Args:
            value: The clearEvent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_clear_event("value")
        """
        self.clear_event = value  # Use property setter (gets validation)
        return self

    def with_confirmation(self, value: Optional["PositiveInteger"]) -> "DiagnosticEvent":
        """
        Set confirmation and return self for chaining.
        
        Args:
            value: The confirmation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_confirmation("value")
        """
        self.confirmation = value  # Use property setter (gets validation)
        return self

    def with_event_clear(self, value: Optional["DiagnosticEventClear"]) -> "DiagnosticEvent":
        """
        Set eventClear and return self for chaining.
        
        Args:
            value: The eventClear to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event_clear("value")
        """
        self.event_clear = value  # Use property setter (gets validation)
        return self

    def with_event_kind(self, value: Optional["DiagnosticEventKind"]) -> "DiagnosticEvent":
        """
        Set eventKind and return self for chaining.
        
        Args:
            value: The eventKind to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event_kind("value")
        """
        self.event_kind = value  # Use property setter (gets validation)
        return self

    def with_prestorage(self, value: Optional["Boolean"]) -> "DiagnosticEvent":
        """
        Set prestorage and return self for chaining.
        
        Args:
            value: The prestorage to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_prestorage("value")
        """
        self.prestorage = value  # Use property setter (gets validation)
        return self

    def with_prestored(self, value: Optional["Boolean"]) -> "DiagnosticEvent":
        """
        Set prestored and return self for chaining.
        
        Args:
            value: The prestored to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_prestored("value")
        """
        self.prestored = value  # Use property setter (gets validation)
        return self

    def with_recoverable_in(self, value: Optional["Boolean"]) -> "DiagnosticEvent":
        """
        Set recoverableIn and return self for chaining.
        
        Args:
            value: The recoverableIn to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_recoverable_in("value")
        """
        self.recoverable_in = value  # Use property setter (gets validation)
        return self



class DiagnosticConnectedIndicator(Identifiable):
    """
    Description of indicators that are defined per DiagnosticEvent.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent::DiagnosticConnectedIndicator
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 166, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Behavior of the linked indicator.
        self._behaviorIndicatorBehaviorEnum: Optional["DiagnosticConnected"] = None

    @property
    def behavior_indicator_behavior_enum(self) -> Optional["DiagnosticConnected"]:
        """Get behaviorIndicatorBehaviorEnum (Pythonic accessor)."""
        return self._behaviorIndicatorBehaviorEnum

    @behavior_indicator_behavior_enum.setter
    def behavior_indicator_behavior_enum(self, value: Optional["DiagnosticConnected"]) -> None:
        """
        Set behaviorIndicatorBehaviorEnum with validation.
        
        Args:
            value: The behaviorIndicatorBehaviorEnum to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._behaviorIndicatorBehaviorEnum = None
            return

        if not isinstance(value, DiagnosticConnected):
            raise TypeError(
                f"behaviorIndicatorBehaviorEnum must be DiagnosticConnected or None, got {type(value).__name__}"
            )
        self._behaviorIndicatorBehaviorEnum = value
        # This attribute defines the number of healing cycles for the atpVariation.
        self._healingCycle: Optional["PositiveInteger"] = None

    @property
    def healing_cycle(self) -> Optional["PositiveInteger"]:
        """Get healingCycle (Pythonic accessor)."""
        return self._healingCycle

    @healing_cycle.setter
    def healing_cycle(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set healingCycle with validation.
        
        Args:
            value: The healingCycle to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._healingCycle = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"healingCycle must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._healingCycle = value
        # Reference to the used indicator.
        self._indicator: Optional["DiagnosticIndicator"] = None

    @property
    def indicator(self) -> Optional["DiagnosticIndicator"]:
        """Get indicator (Pythonic accessor)."""
        return self._indicator

    @indicator.setter
    def indicator(self, value: Optional["DiagnosticIndicator"]) -> None:
        """
        Set indicator with validation.
        
        Args:
            value: The indicator to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._indicator = None
            return

        if not isinstance(value, DiagnosticIndicator):
            raise TypeError(
                f"indicator must be DiagnosticIndicator or None, got {type(value).__name__}"
            )
        self._indicator = value
        # This attribute defines the number of failure cycles for the Please note that
        # this is not relevant for the Adaptive Platform.
        self._indicatorFailure: Optional["PositiveInteger"] = None

    @property
    def indicator_failure(self) -> Optional["PositiveInteger"]:
        """Get indicatorFailure (Pythonic accessor)."""
        return self._indicatorFailure

    @indicator_failure.setter
    def indicator_failure(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set indicatorFailure with validation.
        
        Args:
            value: The indicatorFailure to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._indicatorFailure = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"indicatorFailure must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._indicatorFailure = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBehaviorIndicatorBehaviorEnum(self) -> "DiagnosticConnected":
        """
        AUTOSAR-compliant getter for behaviorIndicatorBehaviorEnum.
        
        Returns:
            The behaviorIndicatorBehaviorEnum value
        
        Note:
            Delegates to behavior_indicator_behavior_enum property (CODING_RULE_V2_00017)
        """
        return self.behavior_indicator_behavior_enum  # Delegates to property

    def setBehaviorIndicatorBehaviorEnum(self, value: "DiagnosticConnected") -> "DiagnosticConnectedIndicator":
        """
        AUTOSAR-compliant setter for behaviorIndicatorBehaviorEnum with method chaining.
        
        Args:
            value: The behaviorIndicatorBehaviorEnum to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to behavior_indicator_behavior_enum property setter (gets validation automatically)
        """
        self.behavior_indicator_behavior_enum = value  # Delegates to property setter
        return self

    def getHealingCycle(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for healingCycle.
        
        Returns:
            The healingCycle value
        
        Note:
            Delegates to healing_cycle property (CODING_RULE_V2_00017)
        """
        return self.healing_cycle  # Delegates to property

    def setHealingCycle(self, value: "PositiveInteger") -> "DiagnosticConnectedIndicator":
        """
        AUTOSAR-compliant setter for healingCycle with method chaining.
        
        Args:
            value: The healingCycle to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to healing_cycle property setter (gets validation automatically)
        """
        self.healing_cycle = value  # Delegates to property setter
        return self

    def getIndicator(self) -> "DiagnosticIndicator":
        """
        AUTOSAR-compliant getter for indicator.
        
        Returns:
            The indicator value
        
        Note:
            Delegates to indicator property (CODING_RULE_V2_00017)
        """
        return self.indicator  # Delegates to property

    def setIndicator(self, value: "DiagnosticIndicator") -> "DiagnosticConnectedIndicator":
        """
        AUTOSAR-compliant setter for indicator with method chaining.
        
        Args:
            value: The indicator to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to indicator property setter (gets validation automatically)
        """
        self.indicator = value  # Delegates to property setter
        return self

    def getIndicatorFailure(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for indicatorFailure.
        
        Returns:
            The indicatorFailure value
        
        Note:
            Delegates to indicator_failure property (CODING_RULE_V2_00017)
        """
        return self.indicator_failure  # Delegates to property

    def setIndicatorFailure(self, value: "PositiveInteger") -> "DiagnosticConnectedIndicator":
        """
        AUTOSAR-compliant setter for indicatorFailure with method chaining.
        
        Args:
            value: The indicatorFailure to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to indicator_failure property setter (gets validation automatically)
        """
        self.indicator_failure = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_behavior_indicator_behavior_enum(self, value: Optional["DiagnosticConnected"]) -> "DiagnosticConnectedIndicator":
        """
        Set behaviorIndicatorBehaviorEnum and return self for chaining.
        
        Args:
            value: The behaviorIndicatorBehaviorEnum to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_behavior_indicator_behavior_enum("value")
        """
        self.behavior_indicator_behavior_enum = value  # Use property setter (gets validation)
        return self

    def with_healing_cycle(self, value: Optional["PositiveInteger"]) -> "DiagnosticConnectedIndicator":
        """
        Set healingCycle and return self for chaining.
        
        Args:
            value: The healingCycle to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_healing_cycle("value")
        """
        self.healing_cycle = value  # Use property setter (gets validation)
        return self

    def with_indicator(self, value: Optional["DiagnosticIndicator"]) -> "DiagnosticConnectedIndicator":
        """
        Set indicator and return self for chaining.
        
        Args:
            value: The indicator to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_indicator("value")
        """
        self.indicator = value  # Use property setter (gets validation)
        return self

    def with_indicator_failure(self, value: Optional["PositiveInteger"]) -> "DiagnosticConnectedIndicator":
        """
        Set indicatorFailure and return self for chaining.
        
        Args:
            value: The indicatorFailure to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_indicator_failure("value")
        """
        self.indicator_failure = value  # Use property setter (gets validation)
        return self



class DiagnosticIumpr(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model the in-use monitor
    performance ratio. The latter computes to the number of times a fault could
    have been found divided by the number of times the vehicle conditions have
    been properly fulfilled.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent::DiagnosticIumpr
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 210, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference represents the DiagnosticEvent that the IUMPR computation.
        self._event: Optional["DiagnosticEvent"] = None

    @property
    def event(self) -> Optional["DiagnosticEvent"]:
        """Get event (Pythonic accessor)."""
        return self._event

    @event.setter
    def event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set event with validation.
        
        Args:
            value: The event to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._event = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"event must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._event = value
        # This attribute controls the behavior of how the ratio is.
        self._ratioKind: Optional["DiagnosticIumprKind"] = None

    @property
    def ratio_kind(self) -> Optional["DiagnosticIumprKind"]:
        """Get ratioKind (Pythonic accessor)."""
        return self._ratioKind

    @ratio_kind.setter
    def ratio_kind(self, value: Optional["DiagnosticIumprKind"]) -> None:
        """
        Set ratioKind with validation.
        
        Args:
            value: The ratioKind to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ratioKind = None
            return

        if not isinstance(value, DiagnosticIumprKind):
            raise TypeError(
                f"ratioKind must be DiagnosticIumprKind or None, got {type(value).__name__}"
            )
        self._ratioKind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for event.
        
        Returns:
            The event value
        
        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    def setEvent(self, value: "DiagnosticEvent") -> "DiagnosticIumpr":
        """
        AUTOSAR-compliant setter for event with method chaining.
        
        Args:
            value: The event to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event property setter (gets validation automatically)
        """
        self.event = value  # Delegates to property setter
        return self

    def getRatioKind(self) -> "DiagnosticIumprKind":
        """
        AUTOSAR-compliant getter for ratioKind.
        
        Returns:
            The ratioKind value
        
        Note:
            Delegates to ratio_kind property (CODING_RULE_V2_00017)
        """
        return self.ratio_kind  # Delegates to property

    def setRatioKind(self, value: "DiagnosticIumprKind") -> "DiagnosticIumpr":
        """
        AUTOSAR-compliant setter for ratioKind with method chaining.
        
        Args:
            value: The ratioKind to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ratio_kind property setter (gets validation automatically)
        """
        self.ratio_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticIumpr":
        """
        Set event and return self for chaining.
        
        Args:
            value: The event to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event("value")
        """
        self.event = value  # Use property setter (gets validation)
        return self

    def with_ratio_kind(self, value: Optional["DiagnosticIumprKind"]) -> "DiagnosticIumpr":
        """
        Set ratioKind and return self for chaining.
        
        Args:
            value: The ratioKind to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ratio_kind("value")
        """
        self.ratio_kind = value  # Use property setter (gets validation)
        return self



class DiagnosticIumprGroup(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model a IUMPR groups.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent::DiagnosticIumprGroup
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 210, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference collects DiagnosticIumpr to a Diagnostic.
        self._iumpr: List["DiagnosticIumpr"] = []

    @property
    def iumpr(self) -> List["DiagnosticIumpr"]:
        """Get iumpr (Pythonic accessor)."""
        return self._iumpr
        # This aggregation allows for the variant modeling of the groupIdentifier.
        # atpVariation.
        self._iumprGroup: Optional["RefType"] = None

    @property
    def iumpr_group(self) -> Optional["RefType"]:
        """Get iumprGroup (Pythonic accessor)."""
        return self._iumprGroup

    @iumpr_group.setter
    def iumpr_group(self, value: Optional["RefType"]) -> None:
        """
        Set iumprGroup with validation.
        
        Args:
            value: The iumprGroup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iumprGroup = None
            return

        self._iumprGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIumpr(self) -> List["DiagnosticIumpr"]:
        """
        AUTOSAR-compliant getter for iumpr.
        
        Returns:
            The iumpr value
        
        Note:
            Delegates to iumpr property (CODING_RULE_V2_00017)
        """
        return self.iumpr  # Delegates to property

    def getIumprGroup(self) -> "RefType":
        """
        AUTOSAR-compliant getter for iumprGroup.
        
        Returns:
            The iumprGroup value
        
        Note:
            Delegates to iumpr_group property (CODING_RULE_V2_00017)
        """
        return self.iumpr_group  # Delegates to property

    def setIumprGroup(self, value: "RefType") -> "DiagnosticIumprGroup":
        """
        AUTOSAR-compliant setter for iumprGroup with method chaining.
        
        Args:
            value: The iumprGroup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to iumpr_group property setter (gets validation automatically)
        """
        self.iumpr_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_iumpr_group(self, value: Optional[RefType]) -> "DiagnosticIumprGroup":
        """
        Set iumprGroup and return self for chaining.
        
        Args:
            value: The iumprGroup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_iumpr_group("value")
        """
        self.iumpr_group = value  # Use property setter (gets validation)
        return self



class DiagnosticIumprGroupIdentifier(ARObject):
    """
    This meta-class provides the ability to the define the group identifier for
    an IumprGroup.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent::DiagnosticIumprGroupIdentifier
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 211, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute shall be taken to define an identifier for the Please note
        # that the value of this identifier by regulations outside the scope of AUTOSAR
        # therefore not be limited to the set of characters a shortName.
        self._groupId: Optional["NameToken"] = None

    @property
    def group_id(self) -> Optional["NameToken"]:
        """Get groupId (Pythonic accessor)."""
        return self._groupId

    @group_id.setter
    def group_id(self, value: Optional["NameToken"]) -> None:
        """
        Set groupId with validation.
        
        Args:
            value: The groupId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._groupId = None
            return

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"groupId must be NameToken or str or None, got {type(value).__name__}"
            )
        self._groupId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getGroupId(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for groupId.
        
        Returns:
            The groupId value
        
        Note:
            Delegates to group_id property (CODING_RULE_V2_00017)
        """
        return self.group_id  # Delegates to property

    def setGroupId(self, value: "NameToken") -> "DiagnosticIumprGroupIdentifier":
        """
        AUTOSAR-compliant setter for groupId with method chaining.
        
        Args:
            value: The groupId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to group_id property setter (gets validation automatically)
        """
        self.group_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_group_id(self, value: Optional["NameToken"]) -> "DiagnosticIumprGroupIdentifier":
        """
        Set groupId and return self for chaining.
        
        Args:
            value: The groupId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_group_id("value")
        """
        self.group_id = value  # Use property setter (gets validation)
        return self



class DiagnosticIumprDenominatorGroup(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model a IUMPR denominator groups.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent::DiagnosticIumprDenominatorGroup
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 211, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference collects DiagnosticIumpr to a Diagnostic.
        self._iumpr: List["DiagnosticIumpr"] = []

    @property
    def iumpr(self) -> List["DiagnosticIumpr"]:
        """Get iumpr (Pythonic accessor)."""
        return self._iumpr

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIumpr(self) -> List["DiagnosticIumpr"]:
        """
        AUTOSAR-compliant getter for iumpr.
        
        Returns:
            The iumpr value
        
        Note:
            Delegates to iumpr property (CODING_RULE_V2_00017)
        """
        return self.iumpr  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticAbstractAliasEvent(DiagnosticCommonElement, ABC):
    """
    This meta-class represents an abstract base class for all diagnostic alias
    events.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent::DiagnosticAbstractAliasEvent
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 214, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticAbstractAliasEvent:
            raise TypeError("DiagnosticAbstractAliasEvent is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticFimAliasEventMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to model the mapping of a
    DiagnosticEvent to a DiagnosticAlias Event. By this means the "preliminary"
    modeling by way of a DiagnosticAliasEvent is further substantiated.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent::DiagnosticFimAliasEventMapping
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 262, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the reference to the actual diagnostic.
        self._actualEvent: Optional["DiagnosticEvent"] = None

    @property
    def actual_event(self) -> Optional["DiagnosticEvent"]:
        """Get actualEvent (Pythonic accessor)."""
        return self._actualEvent

    @actual_event.setter
    def actual_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set actualEvent with validation.
        
        Args:
            value: The actualEvent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._actualEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"actualEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._actualEvent = value
        # This represents the reference to the alias event.
        self._aliasEventEvent: Optional["DiagnosticFimAlias"] = None

    @property
    def alias_event_event(self) -> Optional["DiagnosticFimAlias"]:
        """Get aliasEventEvent (Pythonic accessor)."""
        return self._aliasEventEvent

    @alias_event_event.setter
    def alias_event_event(self, value: Optional["DiagnosticFimAlias"]) -> None:
        """
        Set aliasEventEvent with validation.
        
        Args:
            value: The aliasEventEvent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._aliasEventEvent = None
            return

        if not isinstance(value, DiagnosticFimAlias):
            raise TypeError(
                f"aliasEventEvent must be DiagnosticFimAlias or None, got {type(value).__name__}"
            )
        self._aliasEventEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getActualEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for actualEvent.
        
        Returns:
            The actualEvent value
        
        Note:
            Delegates to actual_event property (CODING_RULE_V2_00017)
        """
        return self.actual_event  # Delegates to property

    def setActualEvent(self, value: "DiagnosticEvent") -> "DiagnosticFimAliasEventMapping":
        """
        AUTOSAR-compliant setter for actualEvent with method chaining.
        
        Args:
            value: The actualEvent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to actual_event property setter (gets validation automatically)
        """
        self.actual_event = value  # Delegates to property setter
        return self

    def getAliasEventEvent(self) -> "DiagnosticFimAlias":
        """
        AUTOSAR-compliant getter for aliasEventEvent.
        
        Returns:
            The aliasEventEvent value
        
        Note:
            Delegates to alias_event_event property (CODING_RULE_V2_00017)
        """
        return self.alias_event_event  # Delegates to property

    def setAliasEventEvent(self, value: "DiagnosticFimAlias") -> "DiagnosticFimAliasEventMapping":
        """
        AUTOSAR-compliant setter for aliasEventEvent with method chaining.
        
        Args:
            value: The aliasEventEvent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to alias_event_event property setter (gets validation automatically)
        """
        self.alias_event_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_actual_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticFimAliasEventMapping":
        """
        Set actualEvent and return self for chaining.
        
        Args:
            value: The actualEvent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_actual_event("value")
        """
        self.actual_event = value  # Use property setter (gets validation)
        return self

    def with_alias_event_event(self, value: Optional["DiagnosticFimAlias"]) -> "DiagnosticFimAliasEventMapping":
        """
        Set aliasEventEvent and return self for chaining.
        
        Args:
            value: The aliasEventEvent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_alias_event_event("value")
        """
        self.alias_event_event = value  # Use property setter (gets validation)
        return self


class DiagnosticClearEventAllowedBehaviorEnum(AREnum):
    """
    DiagnosticClearEventAllowedBehaviorEnum enumeration

This enumeration defines the possible behavior for clear event allowed Aggregated by DiagnosticEvent.clearEventAllowedBehavior

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent
    """
    # The event status byte keeps unchanged.
    noStatusByteChange = "0"

    # The OperationCycle and readiness bits of the event status byte are reset.
    onlyThisCycleAndReadiness = "1"



class DiagnosticEventClearAllowedEnum(AREnum):
    """
    DiagnosticEventClearAllowedEnum enumeration

Denotes whether clearing of events is allowed. Aggregated by DiagnosticEvent.eventClearAllowed

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent
    """
    # The clearing is allowed unconditionally.
    always = "0"

    # In case the clearing of a Diagnostic Event has to be allowed or prohibited through the SWC interface
    requiresCallback = "None"

    # CallbackClearEventAllowed, the SWC has to indicate this by defining appropriate ServiceNeeds (i.e.
    Execution = "2"



class DiagnosticEventKindEnum(AREnum):
    """
    DiagnosticEventKindEnum enumeration

Applicability of the diagnostic event. Aggregated by DiagnosticEvent.eventKind

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent
    """
    # The event is assigned to a BSW module.
    bsw = "0"

    # The event is assigned to a SWC.
    swc = "1"



class DiagnosticConnectedIndicatorBehaviorEnum(AREnum):
    """
    DiagnosticConnectedIndicatorBehaviorEnum enumeration

Behavior of the indicator. Aggregated by DiagnosticConnectedIndicator.behavior

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent
    """
    # The indicator blinks when the event has status FAILED.
    blinkMode = "0"

    # The indicator is active and blinks when the event has status FAILED.
    blinkOrContinuousOnMode = "1"

    # The indicator is active when the event has status FAILED.
    continuousOnMode = "2"

    # Flash Indicator Lamp should be set to "Fast Flash".
    fastFlashingMode = "3"

    # Flash Indicator Lamp should be set to "Slow Flash".
    slowFlashingMode = "4"



class DiagnosticIumprKindEnum(AREnum):
    """
    DiagnosticIumprKindEnum enumeration

This enumeration is used to control the ratio calculation behavior. Aggregated by DiagnosticIumpr.ratioKind

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent
    """
    # The calculation is based on the usage of an API.
    apiBased = "0"

    # The calculation is based on the usage of an observer.
    observerBased = "1"
