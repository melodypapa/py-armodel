"""
AUTOSAR Package - DiagnosticCommonProps

Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticCommonProps
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class DiagnosticCommonProps(ARObject):
    """
    This meta-class aggregates a number of common properties that are shared
    among a diagnostic extract. Tags: vh.latestBindingTime=codeGenerationTime

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticCommonProps::DiagnosticCommonProps

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 64, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the time (in seconds) that the state is maintained in
                # default-session if no communication from the authenticated client.
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
                # R23-11.
        self._authentication: Optional["TimeValue"] = None

    @property
    def authentication(self) -> Optional["TimeValue"]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication

    @authentication.setter
    def authentication(self, value: Optional["TimeValue"]) -> None:
        """
        Set authentication with validation.

        Args:
            value: The authentication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._authentication = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"authentication must be TimeValue or None, got {type(value).__name__}"
            )
        self._authentication = value
                # DiagnosticCommonProps.
        # is a variety of debouncing algorithms to account and therefore the
                # multiplicity of this set to 0.
        # *.
        self._debounce: List["DiagnosticDebounce"] = []

    @property
    def debounce(self) -> List["DiagnosticDebounce"]:
        """Get debounce (Pythonic accessor)."""
        return self._debounce
        # Defines the default endianness of the data belonging to a or RID which is
        # applicable if the DiagnosticData not define the endianness via the swData.
        self._default: Optional["ByteOrderEnum"] = None

    @property
    def default(self) -> Optional["ByteOrderEnum"]:
        """Get default (Pythonic accessor)."""
        return self._default

    @default.setter
    def default(self, value: Optional["ByteOrderEnum"]) -> None:
        """
        Set default with validation.

        Args:
            value: The default to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._default = None
            return

        if not isinstance(value, ByteOrderEnum):
            raise TypeError(
                f"default must be ByteOrderEnum or None, got {type(value).__name__}"
            )
        self._default = value
        # specific order of reporting is to be maintained.
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
                # (requestCorrectlyReceived-ResponsePending) per request.
        # DCM will send a negative response response code 0x10 (generalReject), in case
                # the limit gets reached.
        # Value 0xFF means that no limit of NRC 0x78 response apply.
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxNumberOf must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxNumberOf = value
        # for the occurrence counter.
        self._occurrence: Optional["DiagnosticOccurrence"] = None

    @property
    def occurrence(self) -> Optional["DiagnosticOccurrence"]:
        """Get occurrence (Pythonic accessor)."""
        return self._occurrence

    @occurrence.setter
    def occurrence(self, value: Optional["DiagnosticOccurrence"]) -> None:
        """
        Set occurrence with validation.

        Args:
            value: The occurrence to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._occurrence = None
            return

        if not isinstance(value, DiagnosticOccurrence):
            raise TypeError(
                f"occurrence must be DiagnosticOccurrence or None, got {type(value).__name__}"
            )
        self._occurrence = value
        # memory entry will be displaced.
        self._resetConfirmed: Optional["Boolean"] = None

    @property
    def reset_confirmed(self) -> Optional["Boolean"]:
        """Get resetConfirmed (Pythonic accessor)."""
        return self._resetConfirmed

    @reset_confirmed.setter
    def reset_confirmed(self, value: Optional["Boolean"]) -> None:
        """
        Set resetConfirmed with validation.

        Args:
            value: The resetConfirmed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resetConfirmed = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"resetConfirmed must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._resetConfirmed = value
                # memory entry will be displaced.
        # In be compliant to ISO 14229-1 [1], this parameter be set to "false".
        self._resetPendingBit: Optional["Boolean"] = None

    @property
    def reset_pending_bit(self) -> Optional["Boolean"]:
        """Get resetPendingBit (Pythonic accessor)."""
        return self._resetPendingBit

    @reset_pending_bit.setter
    def reset_pending_bit(self, value: Optional["Boolean"]) -> None:
        """
        Set resetPendingBit with validation.

        Args:
            value: The resetPendingBit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resetPendingBit = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"resetPendingBit must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._resetPendingBit = value
        # service ID which is in the range to 0x7F or in the range from 0xC0 to 0xFF.
        self._responseOnAll: Optional["Boolean"] = None

    @property
    def response_on_all(self) -> Optional["Boolean"]:
        """Get responseOnAll (Pythonic accessor)."""
        return self._responseOnAll

    @response_on_all.setter
    def response_on_all(self, value: Optional["Boolean"]) -> None:
        """
        Set responseOnAll with validation.

        Args:
            value: The responseOnAll to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._responseOnAll = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"responseOnAll must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._responseOnAll = value
                # (e.
        # g.
        # due to priority assessment).
        # when the second request (Client B) can not be Request processed, it shall be
                # answered with NRC21 BusyRepeat the second request (Client B) can not be shall
                # not be responded.
        self._responseOn: Optional["Boolean"] = None

    @property
    def response_on(self) -> Optional["Boolean"]:
        """Get responseOn (Pythonic accessor)."""
        return self._responseOn

    @response_on.setter
    def response_on(self, value: Optional["Boolean"]) -> None:
        """
        Set responseOn with validation.

        Args:
            value: The responseOn to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._responseOn = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"responseOn must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._responseOn = value
        self._typeOfEvent: Optional["DiagnosticEvent"] = None

    @property
    def type_of_event(self) -> Optional["DiagnosticEvent"]:
        """Get typeOfEvent (Pythonic accessor)."""
        return self._typeOfEvent

    @type_of_event.setter
    def type_of_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set typeOfEvent with validation.

        Args:
            value: The typeOfEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._typeOfEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"typeOfEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._typeOfEvent = value

    def with_debounce(self, value):
        """
        Set debounce and return self for chaining.

        Args:
            value: The debounce to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_debounce("value")
        """
        self.debounce = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthentication(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for authentication.

        Returns:
            The authentication value

        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    def setAuthentication(self, value: "TimeValue") -> DiagnosticCommonProps:
        """
        AUTOSAR-compliant setter for authentication with method chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Note:
            Delegates to authentication property setter (gets validation automatically)
        """
        self.authentication = value  # Delegates to property setter
        return self

    def getDebounce(self) -> List["DiagnosticDebounce"]:
        """
        AUTOSAR-compliant getter for debounce.

        Returns:
            The debounce value

        Note:
            Delegates to debounce property (CODING_RULE_V2_00017)
        """
        return self.debounce  # Delegates to property

    def getDefault(self) -> "ByteOrderEnum":
        """
        AUTOSAR-compliant getter for default.

        Returns:
            The default value

        Note:
            Delegates to default property (CODING_RULE_V2_00017)
        """
        return self.default  # Delegates to property

    def setDefault(self, value: "ByteOrderEnum") -> DiagnosticCommonProps:
        """
        AUTOSAR-compliant setter for default with method chaining.

        Args:
            value: The default to set

        Returns:
            self for method chaining

        Note:
            Delegates to default property setter (gets validation automatically)
        """
        self.default = value  # Delegates to property setter
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

    def setEvent(self, value: "DiagnosticEvent") -> DiagnosticCommonProps:
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

    def setMaxNumberOf(self, value: "PositiveInteger") -> DiagnosticCommonProps:
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

    def getOccurrence(self) -> "DiagnosticOccurrence":
        """
        AUTOSAR-compliant getter for occurrence.

        Returns:
            The occurrence value

        Note:
            Delegates to occurrence property (CODING_RULE_V2_00017)
        """
        return self.occurrence  # Delegates to property

    def setOccurrence(self, value: "DiagnosticOccurrence") -> DiagnosticCommonProps:
        """
        AUTOSAR-compliant setter for occurrence with method chaining.

        Args:
            value: The occurrence to set

        Returns:
            self for method chaining

        Note:
            Delegates to occurrence property setter (gets validation automatically)
        """
        self.occurrence = value  # Delegates to property setter
        return self

    def getResetConfirmed(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for resetConfirmed.

        Returns:
            The resetConfirmed value

        Note:
            Delegates to reset_confirmed property (CODING_RULE_V2_00017)
        """
        return self.reset_confirmed  # Delegates to property

    def setResetConfirmed(self, value: "Boolean") -> DiagnosticCommonProps:
        """
        AUTOSAR-compliant setter for resetConfirmed with method chaining.

        Args:
            value: The resetConfirmed to set

        Returns:
            self for method chaining

        Note:
            Delegates to reset_confirmed property setter (gets validation automatically)
        """
        self.reset_confirmed = value  # Delegates to property setter
        return self

    def getResetPendingBit(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for resetPendingBit.

        Returns:
            The resetPendingBit value

        Note:
            Delegates to reset_pending_bit property (CODING_RULE_V2_00017)
        """
        return self.reset_pending_bit  # Delegates to property

    def setResetPendingBit(self, value: "Boolean") -> DiagnosticCommonProps:
        """
        AUTOSAR-compliant setter for resetPendingBit with method chaining.

        Args:
            value: The resetPendingBit to set

        Returns:
            self for method chaining

        Note:
            Delegates to reset_pending_bit property setter (gets validation automatically)
        """
        self.reset_pending_bit = value  # Delegates to property setter
        return self

    def getResponseOnAll(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for responseOnAll.

        Returns:
            The responseOnAll value

        Note:
            Delegates to response_on_all property (CODING_RULE_V2_00017)
        """
        return self.response_on_all  # Delegates to property

    def setResponseOnAll(self, value: "Boolean") -> DiagnosticCommonProps:
        """
        AUTOSAR-compliant setter for responseOnAll with method chaining.

        Args:
            value: The responseOnAll to set

        Returns:
            self for method chaining

        Note:
            Delegates to response_on_all property setter (gets validation automatically)
        """
        self.response_on_all = value  # Delegates to property setter
        return self

    def getResponseOn(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for responseOn.

        Returns:
            The responseOn value

        Note:
            Delegates to response_on property (CODING_RULE_V2_00017)
        """
        return self.response_on  # Delegates to property

    def setResponseOn(self, value: "Boolean") -> DiagnosticCommonProps:
        """
        AUTOSAR-compliant setter for responseOn with method chaining.

        Args:
            value: The responseOn to set

        Returns:
            self for method chaining

        Note:
            Delegates to response_on property setter (gets validation automatically)
        """
        self.response_on = value  # Delegates to property setter
        return self

    def getTypeOfEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for typeOfEvent.

        Returns:
            The typeOfEvent value

        Note:
            Delegates to type_of_event property (CODING_RULE_V2_00017)
        """
        return self.type_of_event  # Delegates to property

    def setTypeOfEvent(self, value: "DiagnosticEvent") -> DiagnosticCommonProps:
        """
        AUTOSAR-compliant setter for typeOfEvent with method chaining.

        Args:
            value: The typeOfEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to type_of_event property setter (gets validation automatically)
        """
        self.type_of_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_authentication(self, value: Optional["TimeValue"]) -> DiagnosticCommonProps:
        """
        Set authentication and return self for chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_authentication("value")
        """
        self.authentication = value  # Use property setter (gets validation)
        return self

    def with_default(self, value: Optional["ByteOrderEnum"]) -> DiagnosticCommonProps:
        """
        Set default and return self for chaining.

        Args:
            value: The default to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default("value")
        """
        self.default = value  # Use property setter (gets validation)
        return self

    def with_event(self, value: Optional["DiagnosticEvent"]) -> DiagnosticCommonProps:
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

    def with_max_number_of(self, value: Optional["PositiveInteger"]) -> DiagnosticCommonProps:
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

    def with_occurrence(self, value: Optional["DiagnosticOccurrence"]) -> DiagnosticCommonProps:
        """
        Set occurrence and return self for chaining.

        Args:
            value: The occurrence to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_occurrence("value")
        """
        self.occurrence = value  # Use property setter (gets validation)
        return self

    def with_reset_confirmed(self, value: Optional["Boolean"]) -> DiagnosticCommonProps:
        """
        Set resetConfirmed and return self for chaining.

        Args:
            value: The resetConfirmed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reset_confirmed("value")
        """
        self.reset_confirmed = value  # Use property setter (gets validation)
        return self

    def with_reset_pending_bit(self, value: Optional["Boolean"]) -> DiagnosticCommonProps:
        """
        Set resetPendingBit and return self for chaining.

        Args:
            value: The resetPendingBit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reset_pending_bit("value")
        """
        self.reset_pending_bit = value  # Use property setter (gets validation)
        return self

    def with_response_on_all(self, value: Optional["Boolean"]) -> DiagnosticCommonProps:
        """
        Set responseOnAll and return self for chaining.

        Args:
            value: The responseOnAll to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_response_on_all("value")
        """
        self.response_on_all = value  # Use property setter (gets validation)
        return self

    def with_response_on(self, value: Optional["Boolean"]) -> DiagnosticCommonProps:
        """
        Set responseOn and return self for chaining.

        Args:
            value: The responseOn to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_response_on("value")
        """
        self.response_on = value  # Use property setter (gets validation)
        return self

    def with_type_of_event(self, value: Optional["DiagnosticEvent"]) -> DiagnosticCommonProps:
        """
        Set typeOfEvent and return self for chaining.

        Args:
            value: The typeOfEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type_of_event("value")
        """
        self.type_of_event = value  # Use property setter (gets validation)
        return self


class DiagnosticOccurrenceCounterProcessingEnum(AREnum):
    """
    DiagnosticOccurrenceCounterProcessingEnum enumeration

The occurrence counter triggering types. Aggregated by DiagnosticCommonProps.occurrenceCounterProcessing

Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticCommonProps
    """
    # Extract Template
    Diagnostic = "None"

    # CP R23-11
    AUTOSAR = "None"

    # The occurrence counter is incremented when TestFailed bit transitions from 0 to 1 if the fault confirmation was successful (ConfirmedDTC bit is already set).
    confirmedDtcBit = "0"

    # The occurrence counter is incremented when TestFailed bit transitions from 0 to 1 (and the fault confirmation is not considered).
    testFailedBit = "1"



class DiagnosticEventCombinationBehaviorEnum(AREnum):
    """
    DiagnosticEventCombinationBehaviorEnum enumeration

Select type of Event Combination support Aggregated by DiagnosticCommonProps.typeOfEventCombinationSupported

Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticCommonProps
    """
    # Event combination on retrieval is used to combine events. For each event an individual event memory OnRetrieval entry is created, while reporting the data via UDS, the data is combined.
    eventCombination = "1"

    # Event combination on storage is used to combine events. Only one memory entry exists for each
    eventCombination = "None"

    # DTC which is also reported via UDS.
    OnStorage = "0"



class DiagnosticEventCombinationReportingBehaviorEnum(AREnum):
    """
    DiagnosticEventCombinationReportingBehaviorEnum enumeration

Select reporting format of events. Applicable only for Event Combination on Retrieval. Aggregated by DiagnosticCommonProps.eventCombinationReportingBehavior

Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticCommonProps
    """
    # The reporting order for event combination on retrieval is the chronological storage order of the events
    reportingInChronlogicalOrder = "0"
