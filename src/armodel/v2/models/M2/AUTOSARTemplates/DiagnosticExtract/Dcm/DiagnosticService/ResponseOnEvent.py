"""
AUTOSAR Package - ResponseOnEvent

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ResponseOnEvent
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
    DiagnosticServiceInstance,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class DiagnosticResponseOnEvent(DiagnosticServiceInstance):
    """
    This represents an instance of the "Response on Event" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ResponseOnEvent::DiagnosticResponseOnEvent

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 132, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the applicable DiagnosticEventWindows.
        self._eventWindow: List[DiagnosticEventWindow] = []

    @property
    def event_window(self) -> List[DiagnosticEventWindow]:
        """Get eventWindow (Pythonic accessor)."""
        return self._eventWindow
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # reference represents the ability to access among all
                # DiagnosticResponseOnEvent given context.
        self._responseOn: Optional["DiagnosticResponseOn"] = None

    @property
    def response_on(self) -> Optional["DiagnosticResponseOn"]:
        """Get responseOn (Pythonic accessor)."""
        return self._responseOn

    @response_on.setter
    def response_on(self, value: Optional["DiagnosticResponseOn"]) -> None:
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

        if not isinstance(value, DiagnosticResponseOn):
            raise TypeError(
                f"responseOn must be DiagnosticResponseOn or None, got {type(value).__name__}"
            )
        self._responseOn = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventWindow(self) -> List[DiagnosticEventWindow]:
        """
        AUTOSAR-compliant getter for eventWindow.

        Returns:
            The eventWindow value

        Note:
            Delegates to event_window property (CODING_RULE_V2_00017)
        """
        return self.event_window  # Delegates to property

    def getResponseOn(self) -> "DiagnosticResponseOn":
        """
        AUTOSAR-compliant getter for responseOn.

        Returns:
            The responseOn value

        Note:
            Delegates to response_on property (CODING_RULE_V2_00017)
        """
        return self.response_on  # Delegates to property

    def setResponseOn(self, value: "DiagnosticResponseOn") -> DiagnosticResponseOnEvent:
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_response_on(self, value: Optional["DiagnosticResponseOn"]) -> DiagnosticResponseOnEvent:
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



class DiagnosticResponseOnEventClass(DiagnosticServiceClass):
    """
    This represents the ability to define common properties for all instances of
    the "Response on Event" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ResponseOnEvent::DiagnosticResponseOnEventClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 132, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The maximum number of DTCs that can be stored as with change status within
        # one ResponseOnEvent interval.
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
        self._maxNum: Optional["PositiveInteger"] = None

    @property
    def max_num(self) -> Optional["PositiveInteger"]:
        """Get maxNum (Pythonic accessor)."""
        return self._maxNum

    @max_num.setter
    def max_num(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxNum with validation.

        Args:
            value: The maxNum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNum = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxNum must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxNum = value
        # comparison or data change.
        self._maxSupported: Optional["PositiveInteger"] = None

    @property
    def max_supported(self) -> Optional["PositiveInteger"]:
        """Get maxSupported (Pythonic accessor)."""
        return self._maxSupported

    @max_supported.setter
    def max_supported(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxSupported with validation.

        Args:
            value: The maxSupported to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSupported = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxSupported must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxSupported = value
        # (DID) or to detect DTC status.
        self._responseOn: Optional["TimeValue"] = None

    @property
    def response_on(self) -> Optional["TimeValue"]:
        """Get responseOn (Pythonic accessor)."""
        return self._responseOn

    @response_on.setter
    def response_on(self, value: Optional["TimeValue"]) -> None:
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

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"responseOn must be TimeValue or None, got {type(value).__name__}"
            )
        self._responseOn = value
                # shall be supported or not.
        # If true, the storeEvent functionality is available.
        # If set the storeEvent functionality is not available.
        self._storeEvent: Optional["Boolean"] = None

    @property
    def store_event(self) -> Optional["Boolean"]:
        """Get storeEvent (Pythonic accessor)."""
        return self._storeEvent

    @store_event.setter
    def store_event(self, value: Optional["Boolean"]) -> None:
        """
        Set storeEvent with validation.

        Args:
            value: The storeEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._storeEvent = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"storeEvent must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._storeEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNumberOf.

        Returns:
            The maxNumberOf value

        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: "PositiveInteger") -> DiagnosticResponseOnEventClass:
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

    def getMaxNum(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNum.

        Returns:
            The maxNum value

        Note:
            Delegates to max_num property (CODING_RULE_V2_00017)
        """
        return self.max_num  # Delegates to property

    def setMaxNum(self, value: "PositiveInteger") -> DiagnosticResponseOnEventClass:
        """
        AUTOSAR-compliant setter for maxNum with method chaining.

        Args:
            value: The maxNum to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_num property setter (gets validation automatically)
        """
        self.max_num = value  # Delegates to property setter
        return self

    def getMaxSupported(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxSupported.

        Returns:
            The maxSupported value

        Note:
            Delegates to max_supported property (CODING_RULE_V2_00017)
        """
        return self.max_supported  # Delegates to property

    def setMaxSupported(self, value: "PositiveInteger") -> DiagnosticResponseOnEventClass:
        """
        AUTOSAR-compliant setter for maxSupported with method chaining.

        Args:
            value: The maxSupported to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_supported property setter (gets validation automatically)
        """
        self.max_supported = value  # Delegates to property setter
        return self

    def getResponseOn(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for responseOn.

        Returns:
            The responseOn value

        Note:
            Delegates to response_on property (CODING_RULE_V2_00017)
        """
        return self.response_on  # Delegates to property

    def setResponseOn(self, value: "TimeValue") -> DiagnosticResponseOnEventClass:
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

    def getStoreEvent(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for storeEvent.

        Returns:
            The storeEvent value

        Note:
            Delegates to store_event property (CODING_RULE_V2_00017)
        """
        return self.store_event  # Delegates to property

    def setStoreEvent(self, value: "Boolean") -> DiagnosticResponseOnEventClass:
        """
        AUTOSAR-compliant setter for storeEvent with method chaining.

        Args:
            value: The storeEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to store_event property setter (gets validation automatically)
        """
        self.store_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_number_of(self, value: Optional["PositiveInteger"]) -> DiagnosticResponseOnEventClass:
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

    def with_max_num(self, value: Optional["PositiveInteger"]) -> DiagnosticResponseOnEventClass:
        """
        Set maxNum and return self for chaining.

        Args:
            value: The maxNum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_num("value")
        """
        self.max_num = value  # Use property setter (gets validation)
        return self

    def with_max_supported(self, value: Optional["PositiveInteger"]) -> DiagnosticResponseOnEventClass:
        """
        Set maxSupported and return self for chaining.

        Args:
            value: The maxSupported to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_supported("value")
        """
        self.max_supported = value  # Use property setter (gets validation)
        return self

    def with_response_on(self, value: Optional["TimeValue"]) -> DiagnosticResponseOnEventClass:
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

    def with_store_event(self, value: Optional["Boolean"]) -> DiagnosticResponseOnEventClass:
        """
        Set storeEvent and return self for chaining.

        Args:
            value: The storeEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_store_event("value")
        """
        self.store_event = value  # Use property setter (gets validation)
        return self



class DiagnosticEventWindow(ARObject):
    """
    This represents the ability to define the characteristics of the applicable
    event window

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ResponseOnEvent::DiagnosticEventWindow

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 133, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute clarifies the validity of the eventWindow.
        self._eventWindow: Optional[DiagnosticEventWindow] = None

    @property
    def event_window(self) -> Optional[DiagnosticEventWindow]:
        """Get eventWindow (Pythonic accessor)."""
        return self._eventWindow

    @event_window.setter
    def event_window(self, value: Optional[DiagnosticEventWindow]) -> None:
        """
        Set eventWindow with validation.

        Args:
            value: The eventWindow to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventWindow = None
            return

        if not isinstance(value, DiagnosticEventWindow):
            raise TypeError(
                f"eventWindow must be DiagnosticEventWindow or None, got {type(value).__name__}"
            )
        self._eventWindow = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventWindow(self) -> DiagnosticEventWindow:
        """
        AUTOSAR-compliant getter for eventWindow.

        Returns:
            The eventWindow value

        Note:
            Delegates to event_window property (CODING_RULE_V2_00017)
        """
        return self.event_window  # Delegates to property

    def setEventWindow(self, value: DiagnosticEventWindow) -> DiagnosticEventWindow:
        """
        AUTOSAR-compliant setter for eventWindow with method chaining.

        Args:
            value: The eventWindow to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_window property setter (gets validation automatically)
        """
        self.event_window = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_window(self, value: Optional[DiagnosticEventWindow]) -> DiagnosticEventWindow:
        """
        Set eventWindow and return self for chaining.

        Args:
            value: The eventWindow to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_window("value")
        """
        self.event_window = value  # Use property setter (gets validation)
        return self


class DiagnosticEventWindowTimeEnum(AREnum):
    """
    DiagnosticEventWindowTimeEnum enumeration

This represents the ability to define the semantics of the event window. Aggregated by DiagnosticEventWindow.eventWindowTime

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ResponseOnEvent
    """
    # This value specifies that the event window shall stay active for an infinite amount of time (e.g. open Response window until power off).
    infiniteTimeTo = "3"

    # This enumeration value specifies that the server shall send response on event messages until the server is powered down. The server stops sending response on event messages with the power down and will send no more response on event messages after server is up again.
    powerWindowTime = "4"



class DiagnosticResponseOnEventActionEnum(AREnum):
    """
    DiagnosticResponseOnEventActionEnum enumeration

This meta-class has the ability to define sub-functions of the UDS service ResponseOnEvent. Aggregated by DiagnosticResponseOnEvent.responseOnEventAction

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ResponseOnEvent
    """
    # Clears the configured events.
    clear = "2"

    # Reports based on change of data identifier.
    onChangeOfDataIdentifier = "6"

    # Triggered if data condition is met (e.g. RPM over 5000 1/min).
    onComparisonOfValues = "8"

    # Reports based on change of DTC status.
    onDTCStatusChange = "7"

    # Reports the activated events.
    report = "3"

    # Reports the DTC record-related information based on a DTC status change. (Subfunction 0x09)
    reportDTCRecordInformationOnDtc = "5"

    # Triggers the report of the most recent failed or confirmed DTC (Subfunction 0x08).
    reportMostRecentDtcOnStatus = "4"

    # Starts the response on event service.
    start = "1"

    # Stops the response on event service.
    stop = "0"
