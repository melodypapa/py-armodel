from typing import Optional


class DiagnosticRoutineControl(DiagnosticServiceInstance):
    """
    This represents an instance of the "Routine Control" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::RoutineControl::DiagnosticRoutineControl

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 125, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This refers to the applicable DiagnosticRoutine.
        self._routine: Optional["DiagnosticRoutine"] = None

    @property
    def routine(self) -> Optional["DiagnosticRoutine"]:
        """Get routine (Pythonic accessor)."""
        return self._routine

    @routine.setter
    def routine(self, value: Optional["DiagnosticRoutine"]) -> None:
        """
        Set routine with validation.

        Args:
            value: The routine to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._routine = None
            return

        if not isinstance(value, DiagnosticRoutine):
            raise TypeError(
                f"routine must be DiagnosticRoutine or None, got {type(value).__name__}"
            )
        self._routine = value
        # This reference substantiates that abstract reference in the reference
        # represents the ability to access among all DiagnosticRoutineControl in
        # context.
        self._routineControl: Optional["DiagnosticRoutine"] = None

    @property
    def routine_control(self) -> Optional["DiagnosticRoutine"]:
        """Get routineControl (Pythonic accessor)."""
        return self._routineControl

    @routine_control.setter
    def routine_control(self, value: Optional["DiagnosticRoutine"]) -> None:
        """
        Set routineControl with validation.

        Args:
            value: The routineControl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._routineControl = None
            return

        if not isinstance(value, DiagnosticRoutine):
            raise TypeError(
                f"routineControl must be DiagnosticRoutine or None, got {type(value).__name__}"
            )
        self._routineControl = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRoutine(self) -> "DiagnosticRoutine":
        """
        AUTOSAR-compliant getter for routine.

        Returns:
            The routine value

        Note:
            Delegates to routine property (CODING_RULE_V2_00017)
        """
        return self.routine  # Delegates to property

    def setRoutine(self, value: "DiagnosticRoutine") -> "DiagnosticRoutineControl":
        """
        AUTOSAR-compliant setter for routine with method chaining.

        Args:
            value: The routine to set

        Returns:
            self for method chaining

        Note:
            Delegates to routine property setter (gets validation automatically)
        """
        self.routine = value  # Delegates to property setter
        return self

    def getRoutineControl(self) -> "DiagnosticRoutine":
        """
        AUTOSAR-compliant getter for routineControl.

        Returns:
            The routineControl value

        Note:
            Delegates to routine_control property (CODING_RULE_V2_00017)
        """
        return self.routine_control  # Delegates to property

    def setRoutineControl(self, value: "DiagnosticRoutine") -> "DiagnosticRoutineControl":
        """
        AUTOSAR-compliant setter for routineControl with method chaining.

        Args:
            value: The routineControl to set

        Returns:
            self for method chaining

        Note:
            Delegates to routine_control property setter (gets validation automatically)
        """
        self.routine_control = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_routine(self, value: Optional["DiagnosticRoutine"]) -> "DiagnosticRoutineControl":
        """
        Set routine and return self for chaining.

        Args:
            value: The routine to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_routine("value")
        """
        self.routine = value  # Use property setter (gets validation)
        return self

    def with_routine_control(self, value: Optional["DiagnosticRoutine"]) -> "DiagnosticRoutineControl":
        """
        Set routineControl and return self for chaining.

        Args:
            value: The routineControl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_routine_control("value")
        """
        self.routine_control = value  # Use property setter (gets validation)
        return self
