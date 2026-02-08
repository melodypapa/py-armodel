from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticClearEvent,
    DiagnosticCommonElement,
    DiagnosticConnected,
    DiagnosticEventClear,
    DiagnosticEventKind,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"associated must be PositiveInteger or None, got {type(value).__name__}"
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"confirmation must be PositiveInteger or None, got {type(value).__name__}"
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"prestorage must be Boolean or None, got {type(value).__name__}"
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"prestored must be Boolean or None, got {type(value).__name__}"
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"recoverableIn must be Boolean or None, got {type(value).__name__}"
            )
        self._recoverableIn = value

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
