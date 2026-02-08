from abc import ABC
from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement


class DiagnosticMemoryDestination(DiagnosticCommonElement, ABC):
    """
    This abstract meta-class represents a possible memory destination for a
    diagnostic event.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticMemoryDestination::DiagnosticMemoryDestination

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 181, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticMemoryDestination:
            raise TypeError("DiagnosticMemoryDestination is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether the aging cycle counter is processed aging cycles or else
                # only tested aging cycle are attribute is set to TRUE: only tested aging cycle
                # are aging cycle counter.
        # attribute is set to FALSE: aging cycle counter is aging cycle.
        # classic platform, the value of this attribute has to for each
                # DiagnosticMemoryDestination.
        self._agingRequires: Optional["Boolean"] = None

    @property
    def aging_requires(self) -> Optional["Boolean"]:
        """Get agingRequires (Pythonic accessor)."""
        return self._agingRequires

    @aging_requires.setter
    def aging_requires(self, value: Optional["Boolean"]) -> None:
        """
        Set agingRequires with validation.

        Args:
            value: The agingRequires to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._agingRequires = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"agingRequires must be Boolean or None, got {type(value).__name__}"
            )
        self._agingRequires = value
        # Defines the scope of the DEM_ClearDTC Api.
        # On the classic platform, the value of this attribute has to for each
                # DiagnosticMemoryDestination.
        self._clearDtc: Optional["DiagnosticClearDtc"] = None

    @property
    def clear_dtc(self) -> Optional["DiagnosticClearDtc"]:
        """Get clearDtc (Pythonic accessor)."""
        return self._clearDtc

    @clear_dtc.setter
    def clear_dtc(self, value: Optional["DiagnosticClearDtc"]) -> None:
        """
        Set clearDtc with validation.

        Args:
            value: The clearDtc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clearDtc = None
            return

        if not isinstance(value, DiagnosticClearDtc):
            raise TypeError(
                f"clearDtc must be DiagnosticClearDtc or None, got {type(value).__name__}"
            )
        self._clearDtc = value
        # Mask for the supported DTC status bits by the Dem.
        self._dtcStatus: Optional["PositiveInteger"] = None

    @property
    def dtc_status(self) -> Optional["PositiveInteger"]:
        """Get dtcStatus (Pythonic accessor)."""
        return self._dtcStatus

    @dtc_status.setter
    def dtc_status(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set dtcStatus with validation.

        Args:
            value: The dtcStatus to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dtcStatus = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"dtcStatus must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._dtcStatus = value
        # This attribute defines, whether support for event displacement is enabled or
        # not, and which displacement strategy is followed.
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
        # This attribute fixes the maximum number of event entries the fault memory.
        self._maxNumberOf: Optional["PositiveInteger"] = None

    @property
    def max_number_of(self) -> Optional["PositiveInteger"]:
        """Get maxNumberOf (Pythonic accessor)."""
        return self._maxNumberOf

    @max_number_of.setter
    def max_number_of(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxNumberOf with validation.

        Args:
            value: The maxNumberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOf = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxNumberOf must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxNumberOf = value
        # Describes the trigger to allocate an event memory entry.
        self._memoryEntry: Optional["DiagnosticMemoryEntry"] = None

    @property
    def memory_entry(self) -> Optional["DiagnosticMemoryEntry"]:
        """Get memoryEntry (Pythonic accessor)."""
        return self._memoryEntry

    @memory_entry.setter
    def memory_entry(self, value: Optional["DiagnosticMemoryEntry"]) -> None:
        """
        Set memoryEntry with validation.

        Args:
            value: The memoryEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._memoryEntry = None
            return

        if not isinstance(value, DiagnosticMemoryEntry):
            raise TypeError(
                f"memoryEntry must be DiagnosticMemoryEntry or None, got {type(value).__name__}"
            )
        self._memoryEntry = value
        # This parameter is used to activate/deactivate the storage of the "TestFailed"
                # status bits.
        # storage activated deactivated.
        self._statusBit: Optional["Boolean"] = None

    @property
    def status_bit(self) -> Optional["Boolean"]:
        """Get statusBit (Pythonic accessor)."""
        return self._statusBit

    @status_bit.setter
    def status_bit(self, value: Optional["Boolean"]) -> None:
        """
        Set statusBit with validation.

        Args:
            value: The statusBit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._statusBit = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"statusBit must be Boolean or None, got {type(value).__name__}"
            )
        self._statusBit = value
        # This attribute defines the type of assigning freeze frame record numbers for
        # event-specific freeze frame records.
        self._typeOfFreeze: Optional["DiagnosticTypeOf"] = None

    @property
    def type_of_freeze(self) -> Optional["DiagnosticTypeOf"]:
        """Get typeOfFreeze (Pythonic accessor)."""
        return self._typeOfFreeze

    @type_of_freeze.setter
    def type_of_freeze(self, value: Optional["DiagnosticTypeOf"]) -> None:
        """
        Set typeOfFreeze with validation.

        Args:
            value: The typeOfFreeze to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._typeOfFreeze = None
            return

        if not isinstance(value, DiagnosticTypeOf):
            raise TypeError(
                f"typeOfFreeze must be DiagnosticTypeOf or None, got {type(value).__name__}"
            )
        self._typeOfFreeze = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAgingRequires(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for agingRequires.

        Returns:
            The agingRequires value

        Note:
            Delegates to aging_requires property (CODING_RULE_V2_00017)
        """
        return self.aging_requires  # Delegates to property

    def setAgingRequires(self, value: "Boolean") -> "DiagnosticMemoryDestination":
        """
        AUTOSAR-compliant setter for agingRequires with method chaining.

        Args:
            value: The agingRequires to set

        Returns:
            self for method chaining

        Note:
            Delegates to aging_requires property setter (gets validation automatically)
        """
        self.aging_requires = value  # Delegates to property setter
        return self

    def getClearDtc(self) -> "DiagnosticClearDtc":
        """
        AUTOSAR-compliant getter for clearDtc.

        Returns:
            The clearDtc value

        Note:
            Delegates to clear_dtc property (CODING_RULE_V2_00017)
        """
        return self.clear_dtc  # Delegates to property

    def setClearDtc(self, value: "DiagnosticClearDtc") -> "DiagnosticMemoryDestination":
        """
        AUTOSAR-compliant setter for clearDtc with method chaining.

        Args:
            value: The clearDtc to set

        Returns:
            self for method chaining

        Note:
            Delegates to clear_dtc property setter (gets validation automatically)
        """
        self.clear_dtc = value  # Delegates to property setter
        return self

    def getDtcStatus(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for dtcStatus.

        Returns:
            The dtcStatus value

        Note:
            Delegates to dtc_status property (CODING_RULE_V2_00017)
        """
        return self.dtc_status  # Delegates to property

    def setDtcStatus(self, value: "PositiveInteger") -> "DiagnosticMemoryDestination":
        """
        AUTOSAR-compliant setter for dtcStatus with method chaining.

        Args:
            value: The dtcStatus to set

        Returns:
            self for method chaining

        Note:
            Delegates to dtc_status property setter (gets validation automatically)
        """
        self.dtc_status = value  # Delegates to property setter
        return self

    def getEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for event.

        Returns:
            The event value

        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    def setEvent(self, value: "DiagnosticEvent") -> "DiagnosticMemoryDestination":
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

    def getMaxNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNumberOf.

        Returns:
            The maxNumberOf value

        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: "PositiveInteger") -> "DiagnosticMemoryDestination":
        """
        AUTOSAR-compliant setter for maxNumberOf with method chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of property setter (gets validation automatically)
        """
        self.max_number_of = value  # Delegates to property setter
        return self

    def getMemoryEntry(self) -> "DiagnosticMemoryEntry":
        """
        AUTOSAR-compliant getter for memoryEntry.

        Returns:
            The memoryEntry value

        Note:
            Delegates to memory_entry property (CODING_RULE_V2_00017)
        """
        return self.memory_entry  # Delegates to property

    def setMemoryEntry(self, value: "DiagnosticMemoryEntry") -> "DiagnosticMemoryDestination":
        """
        AUTOSAR-compliant setter for memoryEntry with method chaining.

        Args:
            value: The memoryEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to memory_entry property setter (gets validation automatically)
        """
        self.memory_entry = value  # Delegates to property setter
        return self

    def getStatusBit(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for statusBit.

        Returns:
            The statusBit value

        Note:
            Delegates to status_bit property (CODING_RULE_V2_00017)
        """
        return self.status_bit  # Delegates to property

    def setStatusBit(self, value: "Boolean") -> "DiagnosticMemoryDestination":
        """
        AUTOSAR-compliant setter for statusBit with method chaining.

        Args:
            value: The statusBit to set

        Returns:
            self for method chaining

        Note:
            Delegates to status_bit property setter (gets validation automatically)
        """
        self.status_bit = value  # Delegates to property setter
        return self

    def getTypeOfFreeze(self) -> "DiagnosticTypeOf":
        """
        AUTOSAR-compliant getter for typeOfFreeze.

        Returns:
            The typeOfFreeze value

        Note:
            Delegates to type_of_freeze property (CODING_RULE_V2_00017)
        """
        return self.type_of_freeze  # Delegates to property

    def setTypeOfFreeze(self, value: "DiagnosticTypeOf") -> "DiagnosticMemoryDestination":
        """
        AUTOSAR-compliant setter for typeOfFreeze with method chaining.

        Args:
            value: The typeOfFreeze to set

        Returns:
            self for method chaining

        Note:
            Delegates to type_of_freeze property setter (gets validation automatically)
        """
        self.type_of_freeze = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_aging_requires(self, value: Optional["Boolean"]) -> "DiagnosticMemoryDestination":
        """
        Set agingRequires and return self for chaining.

        Args:
            value: The agingRequires to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_aging_requires("value")
        """
        self.aging_requires = value  # Use property setter (gets validation)
        return self

    def with_clear_dtc(self, value: Optional["DiagnosticClearDtc"]) -> "DiagnosticMemoryDestination":
        """
        Set clearDtc and return self for chaining.

        Args:
            value: The clearDtc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_clear_dtc("value")
        """
        self.clear_dtc = value  # Use property setter (gets validation)
        return self

    def with_dtc_status(self, value: Optional["PositiveInteger"]) -> "DiagnosticMemoryDestination":
        """
        Set dtcStatus and return self for chaining.

        Args:
            value: The dtcStatus to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dtc_status("value")
        """
        self.dtc_status = value  # Use property setter (gets validation)
        return self

    def with_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticMemoryDestination":
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

    def with_max_number_of(self, value: Optional["PositiveInteger"]) -> "DiagnosticMemoryDestination":
        """
        Set maxNumberOf and return self for chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of("value")
        """
        self.max_number_of = value  # Use property setter (gets validation)
        return self

    def with_memory_entry(self, value: Optional["DiagnosticMemoryEntry"]) -> "DiagnosticMemoryDestination":
        """
        Set memoryEntry and return self for chaining.

        Args:
            value: The memoryEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_memory_entry("value")
        """
        self.memory_entry = value  # Use property setter (gets validation)
        return self

    def with_status_bit(self, value: Optional["Boolean"]) -> "DiagnosticMemoryDestination":
        """
        Set statusBit and return self for chaining.

        Args:
            value: The statusBit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_status_bit("value")
        """
        self.status_bit = value  # Use property setter (gets validation)
        return self

    def with_type_of_freeze(self, value: Optional["DiagnosticTypeOf"]) -> "DiagnosticMemoryDestination":
        """
        Set typeOfFreeze and return self for chaining.

        Args:
            value: The typeOfFreeze to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type_of_freeze("value")
        """
        self.type_of_freeze = value  # Use property setter (gets validation)
        return self
