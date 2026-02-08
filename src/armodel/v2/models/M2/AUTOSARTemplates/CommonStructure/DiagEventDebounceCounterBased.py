from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagEventDebounceAlgorithm,
)


class DiagEventDebounceCounterBased(DiagEventDebounceAlgorithm):
    """
    This meta-class represents the ability to indicate that the counter-based
    debounce algorithm shall be used by the DEM for this diagnostic monitor.
    This is related to set the ECUC choice container DemDebounceAlgorithmClass
    to DemDebounce CounterBased.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 259, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 196, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 757, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Threshold to allocate an event memory entry and to the Freeze Frame.
        self._counterBased: Optional["Integer"] = None

    @property
    def counter_based(self) -> Optional["Integer"]:
        """Get counterBased (Pythonic accessor)."""
        return self._counterBased

    @counter_based.setter
    def counter_based(self, value: Optional["Integer"]) -> None:
        """
        Set counterBased with validation.

        Args:
            value: The counterBased to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._counterBased = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"counterBased must be Integer or None, got {type(value).__name__}"
            )
        self._counterBased = value
        # This value shall be taken to increment the internal counter.
        # atpVariation.
        self._counter: Optional["Integer"] = None

    @property
    def counter(self) -> Optional["Integer"]:
        """Get counter (Pythonic accessor)."""
        return self._counter

    @counter.setter
    def counter(self, value: Optional["Integer"]) -> None:
        """
        Set counter with validation.

        Args:
            value: The counter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._counter = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"counter must be Integer or None, got {type(value).__name__}"
            )
        self._counter = value
        # This value defines the event-specific limit that indicates "failed" counter
        # status.
        self._counterFailed: Optional["Integer"] = None

    @property
    def counter_failed(self) -> Optional["Integer"]:
        """Get counterFailed (Pythonic accessor)."""
        return self._counterFailed

    @counter_failed.setter
    def counter_failed(self, value: Optional["Integer"]) -> None:
        """
        Set counterFailed with validation.

        Args:
            value: The counterFailed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._counterFailed = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"counterFailed must be Integer or None, got {type(value).__name__}"
            )
        self._counterFailed = value
        # This value represents the initial value of the internal counter if the
                # counting direction changes from decrementing.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._counterJump: Optional["Integer"] = None

    @property
    def counter_jump(self) -> Optional["Integer"]:
        """Get counterJump (Pythonic accessor)."""
        return self._counterJump

    @counter_jump.setter
    def counter_jump(self, value: Optional["Integer"]) -> None:
        """
        Set counterJump with validation.

        Args:
            value: The counterJump to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._counterJump = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"counterJump must be Integer or None, got {type(value).__name__}"
            )
        self._counterJump = value
        # This value represents the initial value of the internal counter if the
        # counting direction changes from incrementing.
        self._counterJumpUp: Optional["Integer"] = None

    @property
    def counter_jump_up(self) -> Optional["Integer"]:
        """Get counterJumpUp (Pythonic accessor)."""
        return self._counterJumpUp

    @counter_jump_up.setter
    def counter_jump_up(self, value: Optional["Integer"]) -> None:
        """
        Set counterJumpUp with validation.

        Args:
            value: The counterJumpUp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._counterJumpUp = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"counterJumpUp must be Integer or None, got {type(value).__name__}"
            )
        self._counterJumpUp = value
        # This value defines the event-specific limit that indicates "passed" counter
        # status.
        self._counterPassed: Optional["Integer"] = None

    @property
    def counter_passed(self) -> Optional["Integer"]:
        """Get counterPassed (Pythonic accessor)."""
        return self._counterPassed

    @counter_passed.setter
    def counter_passed(self, value: Optional["Integer"]) -> None:
        """
        Set counterPassed with validation.

        Args:
            value: The counterPassed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._counterPassed = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"counterPassed must be Integer or None, got {type(value).__name__}"
            )
        self._counterPassed = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCounterBased(self) -> "Integer":
        """
        AUTOSAR-compliant getter for counterBased.

        Returns:
            The counterBased value

        Note:
            Delegates to counter_based property (CODING_RULE_V2_00017)
        """
        return self.counter_based  # Delegates to property

    def setCounterBased(self, value: "Integer") -> "DiagEventDebounceCounterBased":
        """
        AUTOSAR-compliant setter for counterBased with method chaining.

        Args:
            value: The counterBased to set

        Returns:
            self for method chaining

        Note:
            Delegates to counter_based property setter (gets validation automatically)
        """
        self.counter_based = value  # Delegates to property setter
        return self

    def getCounter(self) -> "Integer":
        """
        AUTOSAR-compliant getter for counter.

        Returns:
            The counter value

        Note:
            Delegates to counter property (CODING_RULE_V2_00017)
        """
        return self.counter  # Delegates to property

    def setCounter(self, value: "Integer") -> "DiagEventDebounceCounterBased":
        """
        AUTOSAR-compliant setter for counter with method chaining.

        Args:
            value: The counter to set

        Returns:
            self for method chaining

        Note:
            Delegates to counter property setter (gets validation automatically)
        """
        self.counter = value  # Delegates to property setter
        return self

    def getCounterFailed(self) -> "Integer":
        """
        AUTOSAR-compliant getter for counterFailed.

        Returns:
            The counterFailed value

        Note:
            Delegates to counter_failed property (CODING_RULE_V2_00017)
        """
        return self.counter_failed  # Delegates to property

    def setCounterFailed(self, value: "Integer") -> "DiagEventDebounceCounterBased":
        """
        AUTOSAR-compliant setter for counterFailed with method chaining.

        Args:
            value: The counterFailed to set

        Returns:
            self for method chaining

        Note:
            Delegates to counter_failed property setter (gets validation automatically)
        """
        self.counter_failed = value  # Delegates to property setter
        return self

    def getCounterJump(self) -> "Integer":
        """
        AUTOSAR-compliant getter for counterJump.

        Returns:
            The counterJump value

        Note:
            Delegates to counter_jump property (CODING_RULE_V2_00017)
        """
        return self.counter_jump  # Delegates to property

    def setCounterJump(self, value: "Integer") -> "DiagEventDebounceCounterBased":
        """
        AUTOSAR-compliant setter for counterJump with method chaining.

        Args:
            value: The counterJump to set

        Returns:
            self for method chaining

        Note:
            Delegates to counter_jump property setter (gets validation automatically)
        """
        self.counter_jump = value  # Delegates to property setter
        return self

    def getCounterJumpUp(self) -> "Integer":
        """
        AUTOSAR-compliant getter for counterJumpUp.

        Returns:
            The counterJumpUp value

        Note:
            Delegates to counter_jump_up property (CODING_RULE_V2_00017)
        """
        return self.counter_jump_up  # Delegates to property

    def setCounterJumpUp(self, value: "Integer") -> "DiagEventDebounceCounterBased":
        """
        AUTOSAR-compliant setter for counterJumpUp with method chaining.

        Args:
            value: The counterJumpUp to set

        Returns:
            self for method chaining

        Note:
            Delegates to counter_jump_up property setter (gets validation automatically)
        """
        self.counter_jump_up = value  # Delegates to property setter
        return self

    def getCounterPassed(self) -> "Integer":
        """
        AUTOSAR-compliant getter for counterPassed.

        Returns:
            The counterPassed value

        Note:
            Delegates to counter_passed property (CODING_RULE_V2_00017)
        """
        return self.counter_passed  # Delegates to property

    def setCounterPassed(self, value: "Integer") -> "DiagEventDebounceCounterBased":
        """
        AUTOSAR-compliant setter for counterPassed with method chaining.

        Args:
            value: The counterPassed to set

        Returns:
            self for method chaining

        Note:
            Delegates to counter_passed property setter (gets validation automatically)
        """
        self.counter_passed = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_counter_based(self, value: Optional["Integer"]) -> "DiagEventDebounceCounterBased":
        """
        Set counterBased and return self for chaining.

        Args:
            value: The counterBased to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_counter_based("value")
        """
        self.counter_based = value  # Use property setter (gets validation)
        return self

    def with_counter(self, value: Optional["Integer"]) -> "DiagEventDebounceCounterBased":
        """
        Set counter and return self for chaining.

        Args:
            value: The counter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_counter("value")
        """
        self.counter = value  # Use property setter (gets validation)
        return self

    def with_counter_failed(self, value: Optional["Integer"]) -> "DiagEventDebounceCounterBased":
        """
        Set counterFailed and return self for chaining.

        Args:
            value: The counterFailed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_counter_failed("value")
        """
        self.counter_failed = value  # Use property setter (gets validation)
        return self

    def with_counter_jump(self, value: Optional["Integer"]) -> "DiagEventDebounceCounterBased":
        """
        Set counterJump and return self for chaining.

        Args:
            value: The counterJump to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_counter_jump("value")
        """
        self.counter_jump = value  # Use property setter (gets validation)
        return self

    def with_counter_jump_up(self, value: Optional["Integer"]) -> "DiagEventDebounceCounterBased":
        """
        Set counterJumpUp and return self for chaining.

        Args:
            value: The counterJumpUp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_counter_jump_up("value")
        """
        self.counter_jump_up = value  # Use property setter (gets validation)
        return self

    def with_counter_passed(self, value: Optional["Integer"]) -> "DiagEventDebounceCounterBased":
        """
        Set counterPassed and return self for chaining.

        Args:
            value: The counterPassed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_counter_passed("value")
        """
        self.counter_passed = value  # Use property setter (gets validation)
        return self
