from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticCommonElement,
    DiagnosticRequest,
    DiagnosticStartRoutine,
    DiagnosticStopRoutine,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticRoutine(DiagnosticCommonElement):
    """
    This meta-class represents the ability to define a diagnostic routine.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticRoutine

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 124, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the numerical identifier used to identify the the scope of diagnostic
        # workflow.
        self._id: Optional["PositiveInteger"] = None

    @property
    def id(self) -> Optional["PositiveInteger"]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set id with validation.

        Args:
            value: The id to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._id = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"id must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._id = value
        # This represents the ability to request the result of a routine.
        self._requestResult: Optional["DiagnosticRequest"] = None

    @property
    def request_result(self) -> Optional["DiagnosticRequest"]:
        """Get requestResult (Pythonic accessor)."""
        return self._requestResult

    @request_result.setter
    def request_result(self, value: Optional["DiagnosticRequest"]) -> None:
        """
        Set requestResult with validation.

        Args:
            value: The requestResult to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requestResult = None
            return

        if not isinstance(value, DiagnosticRequest):
            raise TypeError(
                f"requestResult must be DiagnosticRequest or None, got {type(value).__name__}"
            )
        self._requestResult = value
        # This represents the routine info byte.
        # The info byte manufacturer-specific value (for the record identifiers) that
                # is reported to the cases for this attribute are mentioned in ISO ISO 26021.
        self._routineInfo: Optional["PositiveInteger"] = None

    @property
    def routine_info(self) -> Optional["PositiveInteger"]:
        """Get routineInfo (Pythonic accessor)."""
        return self._routineInfo

    @routine_info.setter
    def routine_info(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set routineInfo with validation.

        Args:
            value: The routineInfo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._routineInfo = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"routineInfo must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._routineInfo = value
        # This represents the ability to start a routine.
        self._start: Optional["DiagnosticStartRoutine"] = None

    @property
    def start(self) -> Optional["DiagnosticStartRoutine"]:
        """Get start (Pythonic accessor)."""
        return self._start

    @start.setter
    def start(self, value: Optional["DiagnosticStartRoutine"]) -> None:
        """
        Set start with validation.

        Args:
            value: The start to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._start = None
            return

        if not isinstance(value, DiagnosticStartRoutine):
            raise TypeError(
                f"start must be DiagnosticStartRoutine or None, got {type(value).__name__}"
            )
        self._start = value
        # This represents the ability to stop a running routine.
        self._stop: Optional["DiagnosticStopRoutine"] = None

    @property
    def stop(self) -> Optional["DiagnosticStopRoutine"]:
        """Get stop (Pythonic accessor)."""
        return self._stop

    @stop.setter
    def stop(self, value: Optional["DiagnosticStopRoutine"]) -> None:
        """
        Set stop with validation.

        Args:
            value: The stop to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._stop = None
            return

        if not isinstance(value, DiagnosticStopRoutine):
            raise TypeError(
                f"stop must be DiagnosticStopRoutine or None, got {type(value).__name__}"
            )
        self._stop = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> "DiagnosticRoutine":
        """
        AUTOSAR-compliant setter for id with method chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Note:
            Delegates to id property setter (gets validation automatically)
        """
        self.id = value  # Delegates to property setter
        return self

    def getRequestResult(self) -> "DiagnosticRequest":
        """
        AUTOSAR-compliant getter for requestResult.

        Returns:
            The requestResult value

        Note:
            Delegates to request_result property (CODING_RULE_V2_00017)
        """
        return self.request_result  # Delegates to property

    def setRequestResult(self, value: "DiagnosticRequest") -> "DiagnosticRoutine":
        """
        AUTOSAR-compliant setter for requestResult with method chaining.

        Args:
            value: The requestResult to set

        Returns:
            self for method chaining

        Note:
            Delegates to request_result property setter (gets validation automatically)
        """
        self.request_result = value  # Delegates to property setter
        return self

    def getRoutineInfo(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for routineInfo.

        Returns:
            The routineInfo value

        Note:
            Delegates to routine_info property (CODING_RULE_V2_00017)
        """
        return self.routine_info  # Delegates to property

    def setRoutineInfo(self, value: "PositiveInteger") -> "DiagnosticRoutine":
        """
        AUTOSAR-compliant setter for routineInfo with method chaining.

        Args:
            value: The routineInfo to set

        Returns:
            self for method chaining

        Note:
            Delegates to routine_info property setter (gets validation automatically)
        """
        self.routine_info = value  # Delegates to property setter
        return self

    def getStart(self) -> "DiagnosticStartRoutine":
        """
        AUTOSAR-compliant getter for start.

        Returns:
            The start value

        Note:
            Delegates to start property (CODING_RULE_V2_00017)
        """
        return self.start  # Delegates to property

    def setStart(self, value: "DiagnosticStartRoutine") -> "DiagnosticRoutine":
        """
        AUTOSAR-compliant setter for start with method chaining.

        Args:
            value: The start to set

        Returns:
            self for method chaining

        Note:
            Delegates to start property setter (gets validation automatically)
        """
        self.start = value  # Delegates to property setter
        return self

    def getStop(self) -> "DiagnosticStopRoutine":
        """
        AUTOSAR-compliant getter for stop.

        Returns:
            The stop value

        Note:
            Delegates to stop property (CODING_RULE_V2_00017)
        """
        return self.stop  # Delegates to property

    def setStop(self, value: "DiagnosticStopRoutine") -> "DiagnosticRoutine":
        """
        AUTOSAR-compliant setter for stop with method chaining.

        Args:
            value: The stop to set

        Returns:
            self for method chaining

        Note:
            Delegates to stop property setter (gets validation automatically)
        """
        self.stop = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticRoutine":
        """
        Set id and return self for chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_id("value")
        """
        self.id = value  # Use property setter (gets validation)
        return self

    def with_request_result(self, value: Optional["DiagnosticRequest"]) -> "DiagnosticRoutine":
        """
        Set requestResult and return self for chaining.

        Args:
            value: The requestResult to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request_result("value")
        """
        self.request_result = value  # Use property setter (gets validation)
        return self

    def with_routine_info(self, value: Optional["PositiveInteger"]) -> "DiagnosticRoutine":
        """
        Set routineInfo and return self for chaining.

        Args:
            value: The routineInfo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_routine_info("value")
        """
        self.routine_info = value  # Use property setter (gets validation)
        return self

    def with_start(self, value: Optional["DiagnosticStartRoutine"]) -> "DiagnosticRoutine":
        """
        Set start and return self for chaining.

        Args:
            value: The start to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_start("value")
        """
        self.start = value  # Use property setter (gets validation)
        return self

    def with_stop(self, value: Optional["DiagnosticStopRoutine"]) -> "DiagnosticRoutine":
        """
        Set stop and return self for chaining.

        Args:
            value: The stop to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_stop("value")
        """
        self.stop = value  # Use property setter (gets validation)
        return self
