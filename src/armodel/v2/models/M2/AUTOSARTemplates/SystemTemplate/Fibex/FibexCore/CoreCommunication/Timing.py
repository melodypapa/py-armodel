"""
AUTOSAR Package - Timing

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Describable,
)


class TransmissionModeDeclaration(ARObject):
    """
    AUTOSAR COM provides the possibility to define two different TRANSMISSION
    MODES (True and False) for each I-PDU. As TransmissionMode selector the
    signal content can be evaluated via transmissionModeCondition (implemented
    directly in the COM module) or mode conditions can be defined with the
    modeDrivenTrue Condition or modeDrivenFalseCondition (evaluated by BswM and
    invoking Com_SwitchIpduTxMode COM API). If modeDrivenTrueCondition and
    modeDrivenFalseCondition are defined they shall never evaluate to true both
    at the same time. The mixing of Transmission Mode Switch via API and signal
    value is not allowed.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::TransmissionModeDeclaration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 392, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the trigger for the Com_SwitchIpduTxMode Transmission Mode switch.
        # Only if all defined modeDriven evaluate to true (AND associated) the be
                # activated.
        # mode modeDrivenFalseCondition evaluate to true both at the same time.
        self._modeDriven: List["ModeDriven"] = []

    @property
    def mode_driven(self) -> List["ModeDriven"]:
        """Get modeDriven (Pythonic accessor)."""
        return self._modeDriven
        # Timing Specification if the COM Transmission Mode is true.
        # The Transmission Mode Selector is defined to be if at least one Condition
                # evaluates to true.
        self._transmission: Optional["TransmissionMode"] = None

    @property
    def transmission(self) -> Optional["TransmissionMode"]:
        """Get transmission (Pythonic accessor)."""
        return self._transmission

    @transmission.setter
    def transmission(self, value: Optional["TransmissionMode"]) -> None:
        """
        Set transmission with validation.

        Args:
            value: The transmission to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmission = None
            return

        if not isinstance(value, TransmissionMode):
            raise TypeError(
                f"transmission must be TransmissionMode or None, got {type(value).__name__}"
            )
        self._transmission = value

    def with_mode_driven(self, value):
        """
        Set mode_driven and return self for chaining.

        Args:
            value: The mode_driven to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_driven("value")
        """
        self.mode_driven = value  # Use property setter (gets validation)
        return self

    def with_mode(self, value):
        """
        Set mode and return self for chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self

    def with_mode(self, value):
        """
        Set mode and return self for chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeDriven(self) -> List["ModeDriven"]:
        """
        AUTOSAR-compliant getter for modeDriven.

        Returns:
            The modeDriven value

        Note:
            Delegates to mode_driven property (CODING_RULE_V2_00017)
        """
        return self.mode_driven  # Delegates to property

    def getTransmission(self) -> "TransmissionMode":
        """
        AUTOSAR-compliant getter for transmission.

        Returns:
            The transmission value

        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: "TransmissionMode") -> "TransmissionModeDeclaration":
        """
        AUTOSAR-compliant setter for transmission with method chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmission property setter (gets validation automatically)
        """
        self.transmission = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_transmission(self, value: Optional["TransmissionMode"]) -> "TransmissionModeDeclaration":
        """
        Set transmission and return self for chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmission("value")
        """
        self.transmission = value  # Use property setter (gets validation)
        return self



class TransmissionModeCondition(ARObject):
    """
    Possibility to attach a condition to each signal within an I-PDU. If at
    least one condition evaluates to true, TRANSMISSION MODE True shall be used
    for this I-Pdu. In all other cases, the TRANSMISSION MODE FALSE shall be
    used.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::TransmissionModeCondition

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 392, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Possibilities to define conditions.
        self._dataFilter: Optional["DataFilter"] = None

    @property
    def data_filter(self) -> Optional["DataFilter"]:
        """Get dataFilter (Pythonic accessor)."""
        return self._dataFilter

    @data_filter.setter
    def data_filter(self, value: Optional["DataFilter"]) -> None:
        """
        Set dataFilter with validation.

        Args:
            value: The dataFilter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataFilter = None
            return

        if not isinstance(value, DataFilter):
            raise TypeError(
                f"dataFilter must be DataFilter or None, got {type(value).__name__}"
            )
        self._dataFilter = value
        self._iSignalInIPdu: Optional["RefType"] = None

    @property
    def i_signal_in_i_pdu(self) -> Optional["RefType"]:
        """Get iSignalInIPdu (Pythonic accessor)."""
        return self._iSignalInIPdu

    @i_signal_in_i_pdu.setter
    def i_signal_in_i_pdu(self, value: Optional["RefType"]) -> None:
        """
        Set iSignalInIPdu with validation.

        Args:
            value: The iSignalInIPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignalInIPdu = None
            return

        self._iSignalInIPdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataFilter(self) -> "DataFilter":
        """
        AUTOSAR-compliant getter for dataFilter.

        Returns:
            The dataFilter value

        Note:
            Delegates to data_filter property (CODING_RULE_V2_00017)
        """
        return self.data_filter  # Delegates to property

    def setDataFilter(self, value: "DataFilter") -> "TransmissionModeCondition":
        """
        AUTOSAR-compliant setter for dataFilter with method chaining.

        Args:
            value: The dataFilter to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_filter property setter (gets validation automatically)
        """
        self.data_filter = value  # Delegates to property setter
        return self

    def getISignalInIPdu(self) -> "RefType":
        """
        AUTOSAR-compliant getter for iSignalInIPdu.

        Returns:
            The iSignalInIPdu value

        Note:
            Delegates to i_signal_in_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_signal_in_i_pdu  # Delegates to property

    def setISignalInIPdu(self, value: "RefType") -> "TransmissionModeCondition":
        """
        AUTOSAR-compliant setter for iSignalInIPdu with method chaining.

        Args:
            value: The iSignalInIPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to i_signal_in_i_pdu property setter (gets validation automatically)
        """
        self.i_signal_in_i_pdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_filter(self, value: Optional["DataFilter"]) -> "TransmissionModeCondition":
        """
        Set dataFilter and return self for chaining.

        Args:
            value: The dataFilter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_filter("value")
        """
        self.data_filter = value  # Use property setter (gets validation)
        return self

    def with_i_signal_in_i_pdu(self, value: Optional[RefType]) -> "TransmissionModeCondition":
        """
        Set iSignalInIPdu and return self for chaining.

        Args:
            value: The iSignalInIPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_signal_in_i_pdu("value")
        """
        self.i_signal_in_i_pdu = value  # Use property setter (gets validation)
        return self



class ModeDrivenTransmissionModeCondition(ARObject):
    """
    The condition defined by this class evaluates to true if one of the
    referenced modeDeclarations (OR associated) is active. All referenced
    modeDeclarations shall be from the same ModeDeclarationGroup. The condition
    is used to define which TransmissionMode shall be activated using
    Com_SwitchIpduTx Mode.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::ModeDrivenTransmissionModeCondition

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 393, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to one modeDeclaration which is OR in the context of the
        # ModeDrivenTransmission.
        self._mode: List["ModeDeclaration"] = []

    @property
    def mode(self) -> List["ModeDeclaration"]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMode(self) -> List["ModeDeclaration"]:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TransmissionModeTiming(ARObject):
    """
    If the COM Transmission Mode is false the timing is aggregated by the
    TransmissionModeTiming element in the role of transmissionModeFalseTiming.
    If the COM Transmission Mode is true the timing is aggregated by the
    TransmissionModeTiming element in the role of transmissionModeTrueTiming.
    COM supports the following Transmission Modes: • Periodic (Cyclic Timing) •
    Direct /n-times (EventControlledTiming) • Mixed (Cyclic and
    EventControlledTiming are assigned) • None (no timing is assigned)

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::TransmissionModeTiming

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 393, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Periodic Transmission Mode.
        self._cyclicTiming: Optional["CyclicTiming"] = None

    @property
    def cyclic_timing(self) -> Optional["CyclicTiming"]:
        """Get cyclicTiming (Pythonic accessor)."""
        return self._cyclicTiming

    @cyclic_timing.setter
    def cyclic_timing(self, value: Optional["CyclicTiming"]) -> None:
        """
        Set cyclicTiming with validation.

        Args:
            value: The cyclicTiming to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cyclicTiming = None
            return

        if not isinstance(value, CyclicTiming):
            raise TypeError(
                f"cyclicTiming must be CyclicTiming or None, got {type(value).__name__}"
            )
        self._cyclicTiming = value
        self._eventControlledTiming: Optional["EventControlledTiming"] = None

    @property
    def event_controlled_timing(self) -> Optional["EventControlledTiming"]:
        """Get eventControlledTiming (Pythonic accessor)."""
        return self._eventControlledTiming

    @event_controlled_timing.setter
    def event_controlled_timing(self, value: Optional["EventControlledTiming"]) -> None:
        """
        Set eventControlledTiming with validation.

        Args:
            value: The eventControlledTiming to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventControlledTiming = None
            return

        if not isinstance(value, EventControlledTiming):
            raise TypeError(
                f"eventControlledTiming must be EventControlledTiming or None, got {type(value).__name__}"
            )
        self._eventControlledTiming = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCyclicTiming(self) -> "CyclicTiming":
        """
        AUTOSAR-compliant getter for cyclicTiming.

        Returns:
            The cyclicTiming value

        Note:
            Delegates to cyclic_timing property (CODING_RULE_V2_00017)
        """
        return self.cyclic_timing  # Delegates to property

    def setCyclicTiming(self, value: "CyclicTiming") -> "TransmissionModeTiming":
        """
        AUTOSAR-compliant setter for cyclicTiming with method chaining.

        Args:
            value: The cyclicTiming to set

        Returns:
            self for method chaining

        Note:
            Delegates to cyclic_timing property setter (gets validation automatically)
        """
        self.cyclic_timing = value  # Delegates to property setter
        return self

    def getEventControlledTiming(self) -> "EventControlledTiming":
        """
        AUTOSAR-compliant getter for eventControlledTiming.

        Returns:
            The eventControlledTiming value

        Note:
            Delegates to event_controlled_timing property (CODING_RULE_V2_00017)
        """
        return self.event_controlled_timing  # Delegates to property

    def setEventControlledTiming(self, value: "EventControlledTiming") -> "TransmissionModeTiming":
        """
        AUTOSAR-compliant setter for eventControlledTiming with method chaining.

        Args:
            value: The eventControlledTiming to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_controlled_timing property setter (gets validation automatically)
        """
        self.event_controlled_timing = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cyclic_timing(self, value: Optional["CyclicTiming"]) -> "TransmissionModeTiming":
        """
        Set cyclicTiming and return self for chaining.

        Args:
            value: The cyclicTiming to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cyclic_timing("value")
        """
        self.cyclic_timing = value  # Use property setter (gets validation)
        return self

    def with_event_controlled_timing(self, value: Optional["EventControlledTiming"]) -> "TransmissionModeTiming":
        """
        Set eventControlledTiming and return self for chaining.

        Args:
            value: The eventControlledTiming to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_controlled_timing("value")
        """
        self.event_controlled_timing = value  # Use property setter (gets validation)
        return self



class CyclicTiming(Describable):
    """
    Specification of a cyclic sending behavior.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::CyclicTiming

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 396, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the time until first transmission of This attribute
        # defines the time between Com_ the first transmission of the cyclic this
        # transmission request for this I-PDU.
        self._timeOffset: Optional["TimeRangeType"] = None

    @property
    def time_offset(self) -> Optional["TimeRangeType"]:
        """Get timeOffset (Pythonic accessor)."""
        return self._timeOffset

    @time_offset.setter
    def time_offset(self, value: Optional["TimeRangeType"]) -> None:
        """
        Set timeOffset with validation.

        Args:
            value: The timeOffset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeOffset = None
            return

        if not isinstance(value, TimeRangeType):
            raise TypeError(
                f"timeOffset must be TimeRangeType or None, got {type(value).__name__}"
            )
        self._timeOffset = value
        self._timePeriod: Optional["TimeRangeType"] = None

    @property
    def time_period(self) -> Optional["TimeRangeType"]:
        """Get timePeriod (Pythonic accessor)."""
        return self._timePeriod

    @time_period.setter
    def time_period(self, value: Optional["TimeRangeType"]) -> None:
        """
        Set timePeriod with validation.

        Args:
            value: The timePeriod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timePeriod = None
            return

        if not isinstance(value, TimeRangeType):
            raise TypeError(
                f"timePeriod must be TimeRangeType or None, got {type(value).__name__}"
            )
        self._timePeriod = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimeOffset(self) -> "TimeRangeType":
        """
        AUTOSAR-compliant getter for timeOffset.

        Returns:
            The timeOffset value

        Note:
            Delegates to time_offset property (CODING_RULE_V2_00017)
        """
        return self.time_offset  # Delegates to property

    def setTimeOffset(self, value: "TimeRangeType") -> "CyclicTiming":
        """
        AUTOSAR-compliant setter for timeOffset with method chaining.

        Args:
            value: The timeOffset to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_offset property setter (gets validation automatically)
        """
        self.time_offset = value  # Delegates to property setter
        return self

    def getTimePeriod(self) -> "TimeRangeType":
        """
        AUTOSAR-compliant getter for timePeriod.

        Returns:
            The timePeriod value

        Note:
            Delegates to time_period property (CODING_RULE_V2_00017)
        """
        return self.time_period  # Delegates to property

    def setTimePeriod(self, value: "TimeRangeType") -> "CyclicTiming":
        """
        AUTOSAR-compliant setter for timePeriod with method chaining.

        Args:
            value: The timePeriod to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_period property setter (gets validation automatically)
        """
        self.time_period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_time_offset(self, value: Optional["TimeRangeType"]) -> "CyclicTiming":
        """
        Set timeOffset and return self for chaining.

        Args:
            value: The timeOffset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_offset("value")
        """
        self.time_offset = value  # Use property setter (gets validation)
        return self

    def with_time_period(self, value: Optional["TimeRangeType"]) -> "CyclicTiming":
        """
        Set timePeriod and return self for chaining.

        Args:
            value: The timePeriod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_period("value")
        """
        self.time_period = value  # Use property setter (gets validation)
        return self



class EventControlledTiming(Describable):
    """
    Specification of a event driven sending behavior. The PDU is sent n
    (numberOfRepeat + 1) times separated by the repetitionPeriod. If
    numberOfRepeats = 0, then the Pdu is sent just once.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::EventControlledTiming

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 397, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the number of repetitions for the Direct/N-Times mode and the event
        # driven part of Mixed.
        self._numberOf: Optional["Integer"] = None

    @property
    def number_of(self) -> Optional["Integer"]:
        """Get numberOf (Pythonic accessor)."""
        return self._numberOf

    @number_of.setter
    def number_of(self, value: Optional["Integer"]) -> None:
        """
        Set numberOf with validation.

        Args:
            value: The numberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._numberOf = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"numberOf must be Integer or int or None, got {type(value).__name__}"
            )
        self._numberOf = value
                # the next time gap between two pdus).
        # The repetition optional in case that no repetitions are.
        self._repetitionPeriod: Optional["TimeRangeType"] = None

    @property
    def repetition_period(self) -> Optional["TimeRangeType"]:
        """Get repetitionPeriod (Pythonic accessor)."""
        return self._repetitionPeriod

    @repetition_period.setter
    def repetition_period(self, value: Optional["TimeRangeType"]) -> None:
        """
        Set repetitionPeriod with validation.

        Args:
            value: The repetitionPeriod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._repetitionPeriod = None
            return

        if not isinstance(value, TimeRangeType):
            raise TypeError(
                f"repetitionPeriod must be TimeRangeType or None, got {type(value).__name__}"
            )
        self._repetitionPeriod = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNumberOf(self) -> "Integer":
        """
        AUTOSAR-compliant getter for numberOf.

        Returns:
            The numberOf value

        Note:
            Delegates to number_of property (CODING_RULE_V2_00017)
        """
        return self.number_of  # Delegates to property

    def setNumberOf(self, value: "Integer") -> "EventControlledTiming":
        """
        AUTOSAR-compliant setter for numberOf with method chaining.

        Args:
            value: The numberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to number_of property setter (gets validation automatically)
        """
        self.number_of = value  # Delegates to property setter
        return self

    def getRepetitionPeriod(self) -> "TimeRangeType":
        """
        AUTOSAR-compliant getter for repetitionPeriod.

        Returns:
            The repetitionPeriod value

        Note:
            Delegates to repetition_period property (CODING_RULE_V2_00017)
        """
        return self.repetition_period  # Delegates to property

    def setRepetitionPeriod(self, value: "TimeRangeType") -> "EventControlledTiming":
        """
        AUTOSAR-compliant setter for repetitionPeriod with method chaining.

        Args:
            value: The repetitionPeriod to set

        Returns:
            self for method chaining

        Note:
            Delegates to repetition_period property setter (gets validation automatically)
        """
        self.repetition_period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_number_of(self, value: Optional["Integer"]) -> "EventControlledTiming":
        """
        Set numberOf and return self for chaining.

        Args:
            value: The numberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_number_of("value")
        """
        self.number_of = value  # Use property setter (gets validation)
        return self

    def with_repetition_period(self, value: Optional["TimeRangeType"]) -> "EventControlledTiming":
        """
        Set repetitionPeriod and return self for chaining.

        Args:
            value: The repetitionPeriod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_repetition_period("value")
        """
        self.repetition_period = value  # Use property setter (gets validation)
        return self



class TimeRangeType(ARObject):
    """
    The timeRange can be specified with the value attribute. Optionally a
    tolerance can be defined.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::TimeRangeType

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 398, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional specification of a tolerance.
        self._toleranceTolerance: Optional["TimeRangeType"] = None

    @property
    def tolerance_tolerance(self) -> Optional["TimeRangeType"]:
        """Get toleranceTolerance (Pythonic accessor)."""
        return self._toleranceTolerance

    @tolerance_tolerance.setter
    def tolerance_tolerance(self, value: Optional["TimeRangeType"]) -> None:
        """
        Set toleranceTolerance with validation.

        Args:
            value: The toleranceTolerance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._toleranceTolerance = None
            return

        if not isinstance(value, TimeRangeType):
            raise TypeError(
                f"toleranceTolerance must be TimeRangeType or None, got {type(value).__name__}"
            )
        self._toleranceTolerance = value
        self._value: Optional["TimeValue"] = None

    @property
    def value(self) -> Optional["TimeValue"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["TimeValue"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"value must be TimeValue or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getToleranceTolerance(self) -> "TimeRangeType":
        """
        AUTOSAR-compliant getter for toleranceTolerance.

        Returns:
            The toleranceTolerance value

        Note:
            Delegates to tolerance_tolerance property (CODING_RULE_V2_00017)
        """
        return self.tolerance_tolerance  # Delegates to property

    def setToleranceTolerance(self, value: "TimeRangeType") -> "TimeRangeType":
        """
        AUTOSAR-compliant setter for toleranceTolerance with method chaining.

        Args:
            value: The toleranceTolerance to set

        Returns:
            self for method chaining

        Note:
            Delegates to tolerance_tolerance property setter (gets validation automatically)
        """
        self.tolerance_tolerance = value  # Delegates to property setter
        return self

    def getValue(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "TimeValue") -> "TimeRangeType":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tolerance_tolerance(self, value: Optional["TimeRangeType"]) -> "TimeRangeType":
        """
        Set toleranceTolerance and return self for chaining.

        Args:
            value: The toleranceTolerance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tolerance_tolerance("value")
        """
        self.tolerance_tolerance = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: Optional["TimeValue"]) -> "TimeRangeType":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self



class RelativeTolerance(ARObject):
    """
    Maximum allowable deviation

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::RelativeTolerance

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 398, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum allowable deviation in percent (percent of the.
        self._relative: Optional["Integer"] = None

    @property
    def relative(self) -> Optional["Integer"]:
        """Get relative (Pythonic accessor)."""
        return self._relative

    @relative.setter
    def relative(self, value: Optional["Integer"]) -> None:
        """
        Set relative with validation.

        Args:
            value: The relative to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._relative = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"relative must be Integer or int or None, got {type(value).__name__}"
            )
        self._relative = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRelative(self) -> "Integer":
        """
        AUTOSAR-compliant getter for relative.

        Returns:
            The relative value

        Note:
            Delegates to relative property (CODING_RULE_V2_00017)
        """
        return self.relative  # Delegates to property

    def setRelative(self, value: "Integer") -> "RelativeTolerance":
        """
        AUTOSAR-compliant setter for relative with method chaining.

        Args:
            value: The relative to set

        Returns:
            self for method chaining

        Note:
            Delegates to relative property setter (gets validation automatically)
        """
        self.relative = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_relative(self, value: Optional["Integer"]) -> "RelativeTolerance":
        """
        Set relative and return self for chaining.

        Args:
            value: The relative to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_relative("value")
        """
        self.relative = value  # Use property setter (gets validation)
        return self



class AbsoluteTolerance(ARObject):
    """
    Maximum allowable deviation

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::AbsoluteTolerance

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 398, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum allowable deviation in duration (in seconds).
        self._absolute: Optional["TimeValue"] = None

    @property
    def absolute(self) -> Optional["TimeValue"]:
        """Get absolute (Pythonic accessor)."""
        return self._absolute

    @absolute.setter
    def absolute(self, value: Optional["TimeValue"]) -> None:
        """
        Set absolute with validation.

        Args:
            value: The absolute to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._absolute = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"absolute must be TimeValue or None, got {type(value).__name__}"
            )
        self._absolute = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAbsolute(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for absolute.

        Returns:
            The absolute value

        Note:
            Delegates to absolute property (CODING_RULE_V2_00017)
        """
        return self.absolute  # Delegates to property

    def setAbsolute(self, value: "TimeValue") -> "AbsoluteTolerance":
        """
        AUTOSAR-compliant setter for absolute with method chaining.

        Args:
            value: The absolute to set

        Returns:
            self for method chaining

        Note:
            Delegates to absolute property setter (gets validation automatically)
        """
        self.absolute = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_absolute(self, value: Optional["TimeValue"]) -> "AbsoluteTolerance":
        """
        Set absolute and return self for chaining.

        Args:
            value: The absolute to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_absolute("value")
        """
        self.absolute = value  # Use property setter (gets validation)
        return self



class TriggerIPduSendCondition(ARObject):
    """
    The condition defined by this class evaluates to true if one of the
    referenced modeDeclarations (OR associated) is active. The condition is used
    to define when the Pdu is triggered with the Com_Trigger IPDUSend API call.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::TriggerIPduSendCondition

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 399, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to one modeDeclaration which is OR in the context of the
        # TriggerIPduSend.
        self._mode: List["ModeDeclaration"] = []

    @property
    def mode(self) -> List["ModeDeclaration"]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMode(self) -> List["ModeDeclaration"]:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
