from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class RptExecutableEntityProperties(ARObject):
    """
    Describes the code preparation for rapid prototyping at ExecutableEntity
    invocation.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 203, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 859, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Highest RPT event id usable for RTE generated service attribute is relevant,
        # if dedicated id range applied to the ExecutableEntitys of a software specific
        # ExecutableEntitys.
        self._maxRptEventId: Optional["PositiveInteger"] = None

    @property
    def max_rpt_event_id(self) -> Optional["PositiveInteger"]:
        """Get maxRptEventId (Pythonic accessor)."""
        return self._maxRptEventId

    @max_rpt_event_id.setter
    def max_rpt_event_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxRptEventId with validation.

        Args:
            value: The maxRptEventId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxRptEventId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxRptEventId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxRptEventId = value
        # Lowest RPT event id usable for RTE generated service attribute is relevant,
        # if dedicated id range applied to the ExecutableEntitys of a software specific
        # ExecutableEntitys.
        self._minRptEventId: Optional["PositiveInteger"] = None

    @property
    def min_rpt_event_id(self) -> Optional["PositiveInteger"]:
        """Get minRptEventId (Pythonic accessor)."""
        return self._minRptEventId

    @min_rpt_event_id.setter
    def min_rpt_event_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minRptEventId with validation.

        Args:
            value: The minRptEventId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minRptEventId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minRptEventId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minRptEventId = value
        # This attribute specifies the rapid prototyping control of the executable.
        self._rptExecution: Optional["RptExecutionControl"] = None

    @property
    def rpt_execution(self) -> Optional["RptExecutionControl"]:
        """Get rptExecution (Pythonic accessor)."""
        return self._rptExecution

    @rpt_execution.setter
    def rpt_execution(self, value: Optional["RptExecutionControl"]) -> None:
        """
        Set rptExecution with validation.

        Args:
            value: The rptExecution to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptExecution = None
            return

        if not isinstance(value, RptExecutionControl):
            raise TypeError(
                f"rptExecution must be RptExecutionControl or None, got {type(value).__name__}"
            )
        self._rptExecution = value
        # Enables generation of service points by the RTE.
        self._rptServicePoint: Optional["RptServicePointEnum"] = None

    @property
    def rpt_service_point(self) -> Optional["RptServicePointEnum"]:
        """Get rptServicePoint (Pythonic accessor)."""
        return self._rptServicePoint

    @rpt_service_point.setter
    def rpt_service_point(self, value: Optional["RptServicePointEnum"]) -> None:
        """
        Set rptServicePoint with validation.

        Args:
            value: The rptServicePoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptServicePoint = None
            return

        if not isinstance(value, RptServicePointEnum):
            raise TypeError(
                f"rptServicePoint must be RptServicePointEnum or None, got {type(value).__name__}"
            )
        self._rptServicePoint = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxRptEventId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxRptEventId.

        Returns:
            The maxRptEventId value

        Note:
            Delegates to max_rpt_event_id property (CODING_RULE_V2_00017)
        """
        return self.max_rpt_event_id  # Delegates to property

    def setMaxRptEventId(self, value: "PositiveInteger") -> "RptExecutableEntityProperties":
        """
        AUTOSAR-compliant setter for maxRptEventId with method chaining.

        Args:
            value: The maxRptEventId to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_rpt_event_id property setter (gets validation automatically)
        """
        self.max_rpt_event_id = value  # Delegates to property setter
        return self

    def getMinRptEventId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minRptEventId.

        Returns:
            The minRptEventId value

        Note:
            Delegates to min_rpt_event_id property (CODING_RULE_V2_00017)
        """
        return self.min_rpt_event_id  # Delegates to property

    def setMinRptEventId(self, value: "PositiveInteger") -> "RptExecutableEntityProperties":
        """
        AUTOSAR-compliant setter for minRptEventId with method chaining.

        Args:
            value: The minRptEventId to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_rpt_event_id property setter (gets validation automatically)
        """
        self.min_rpt_event_id = value  # Delegates to property setter
        return self

    def getRptExecution(self) -> "RptExecutionControl":
        """
        AUTOSAR-compliant getter for rptExecution.

        Returns:
            The rptExecution value

        Note:
            Delegates to rpt_execution property (CODING_RULE_V2_00017)
        """
        return self.rpt_execution  # Delegates to property

    def setRptExecution(self, value: "RptExecutionControl") -> "RptExecutableEntityProperties":
        """
        AUTOSAR-compliant setter for rptExecution with method chaining.

        Args:
            value: The rptExecution to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_execution property setter (gets validation automatically)
        """
        self.rpt_execution = value  # Delegates to property setter
        return self

    def getRptServicePoint(self) -> "RptServicePointEnum":
        """
        AUTOSAR-compliant getter for rptServicePoint.

        Returns:
            The rptServicePoint value

        Note:
            Delegates to rpt_service_point property (CODING_RULE_V2_00017)
        """
        return self.rpt_service_point  # Delegates to property

    def setRptServicePoint(self, value: "RptServicePointEnum") -> "RptExecutableEntityProperties":
        """
        AUTOSAR-compliant setter for rptServicePoint with method chaining.

        Args:
            value: The rptServicePoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_service_point property setter (gets validation automatically)
        """
        self.rpt_service_point = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_rpt_event_id(self, value: Optional["PositiveInteger"]) -> "RptExecutableEntityProperties":
        """
        Set maxRptEventId and return self for chaining.

        Args:
            value: The maxRptEventId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_rpt_event_id("value")
        """
        self.max_rpt_event_id = value  # Use property setter (gets validation)
        return self

    def with_min_rpt_event_id(self, value: Optional["PositiveInteger"]) -> "RptExecutableEntityProperties":
        """
        Set minRptEventId and return self for chaining.

        Args:
            value: The minRptEventId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_rpt_event_id("value")
        """
        self.min_rpt_event_id = value  # Use property setter (gets validation)
        return self

    def with_rpt_execution(self, value: Optional["RptExecutionControl"]) -> "RptExecutableEntityProperties":
        """
        Set rptExecution and return self for chaining.

        Args:
            value: The rptExecution to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_execution("value")
        """
        self.rpt_execution = value  # Use property setter (gets validation)
        return self

    def with_rpt_service_point(self, value: Optional["RptServicePointEnum"]) -> "RptExecutableEntityProperties":
        """
        Set rptServicePoint and return self for chaining.

        Args:
            value: The rptServicePoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_service_point("value")
        """
        self.rpt_service_point = value  # Use property setter (gets validation)
        return self
