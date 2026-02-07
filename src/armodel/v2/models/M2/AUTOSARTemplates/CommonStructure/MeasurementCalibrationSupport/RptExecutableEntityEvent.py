from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class RptExecutableEntityEvent(Identifiable):
    """
    This describes an ExecutableEntity event instance which can be bypassed.
    
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport::RptExecutableEntityEvent
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 201, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This describes the context in which the event of the entity is executed.
        self._execution: List["RptExecutionContext"] = []

    @property
    def execution(self) -> List["RptExecutionContext"]:
        """Get execution (Pythonic accessor)."""
        return self._execution
        # Reference to related McDataElements describing the implementation of "RP
        # runnable disabler flag" and flag" roles of the RoleBasedMcData are:.
        self._mcData: List["RoleBasedMcData"] = []

    @property
    def mc_data(self) -> List["RoleBasedMcData"]:
        """Get mcData (Pythonic accessor)."""
        return self._mcData
        # RPT event id used for service points call.
        self._rptEventId: Optional["PositiveInteger"] = None

    @property
    def rpt_event_id(self) -> Optional["PositiveInteger"]:
        """Get rptEventId (Pythonic accessor)."""
        return self._rptEventId

    @rpt_event_id.setter
    def rpt_event_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set rptEventId with validation.
        
        Args:
            value: The rptEventId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptEventId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"rptEventId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._rptEventId = value
        # Describes the implemented code preparation for rapid prototyping at
        # ExecutableEntity invocation.
        self._rptExecutable: Optional["RptExecutableEntity"] = None

    @property
    def rpt_executable(self) -> Optional["RptExecutableEntity"]:
        """Get rptExecutable (Pythonic accessor)."""
        return self._rptExecutable

    @rpt_executable.setter
    def rpt_executable(self, value: Optional["RptExecutableEntity"]) -> None:
        """
        Set rptExecutable with validation.
        
        Args:
            value: The rptExecutable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptExecutable = None
            return

        if not isinstance(value, RptExecutableEntity):
            raise TypeError(
                f"rptExecutable must be RptExecutableEntity or None, got {type(value).__name__}"
            )
        self._rptExecutable = value
        # Describes the RptImplPolicy of a RptExecutableEvent for bypassing.
        self._rptImplPolicy: Optional["RptImplPolicy"] = None

    @property
    def rpt_impl_policy(self) -> Optional["RptImplPolicy"]:
        """Get rptImplPolicy (Pythonic accessor)."""
        return self._rptImplPolicy

    @rpt_impl_policy.setter
    def rpt_impl_policy(self, value: Optional["RptImplPolicy"]) -> None:
        """
        Set rptImplPolicy with validation.
        
        Args:
            value: The rptImplPolicy to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptImplPolicy = None
            return

        if not isinstance(value, RptImplPolicy):
            raise TypeError(
                f"rptImplPolicy must be RptImplPolicy or None, got {type(value).__name__}"
            )
        self._rptImplPolicy = value
        # This describes the applicable Pre Service Points for a / BswEvent of a
        # bypassed ExecutableEntity.
        self._rptServicePoint: List["RptServicePoint"] = []

    @property
    def rpt_service_point(self) -> List["RptServicePoint"]:
        """Get rptServicePoint (Pythonic accessor)."""
        return self._rptServicePoint

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getExecution(self) -> List["RptExecutionContext"]:
        """
        AUTOSAR-compliant getter for execution.
        
        Returns:
            The execution value
        
        Note:
            Delegates to execution property (CODING_RULE_V2_00017)
        """
        return self.execution  # Delegates to property

    def getMcData(self) -> List["RoleBasedMcData"]:
        """
        AUTOSAR-compliant getter for mcData.
        
        Returns:
            The mcData value
        
        Note:
            Delegates to mc_data property (CODING_RULE_V2_00017)
        """
        return self.mc_data  # Delegates to property

    def getRptEventId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for rptEventId.
        
        Returns:
            The rptEventId value
        
        Note:
            Delegates to rpt_event_id property (CODING_RULE_V2_00017)
        """
        return self.rpt_event_id  # Delegates to property

    def setRptEventId(self, value: "PositiveInteger") -> "RptExecutableEntityEvent":
        """
        AUTOSAR-compliant setter for rptEventId with method chaining.
        
        Args:
            value: The rptEventId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rpt_event_id property setter (gets validation automatically)
        """
        self.rpt_event_id = value  # Delegates to property setter
        return self

    def getRptExecutable(self) -> "RptExecutableEntity":
        """
        AUTOSAR-compliant getter for rptExecutable.
        
        Returns:
            The rptExecutable value
        
        Note:
            Delegates to rpt_executable property (CODING_RULE_V2_00017)
        """
        return self.rpt_executable  # Delegates to property

    def setRptExecutable(self, value: "RptExecutableEntity") -> "RptExecutableEntityEvent":
        """
        AUTOSAR-compliant setter for rptExecutable with method chaining.
        
        Args:
            value: The rptExecutable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rpt_executable property setter (gets validation automatically)
        """
        self.rpt_executable = value  # Delegates to property setter
        return self

    def getRptImplPolicy(self) -> "RptImplPolicy":
        """
        AUTOSAR-compliant getter for rptImplPolicy.
        
        Returns:
            The rptImplPolicy value
        
        Note:
            Delegates to rpt_impl_policy property (CODING_RULE_V2_00017)
        """
        return self.rpt_impl_policy  # Delegates to property

    def setRptImplPolicy(self, value: "RptImplPolicy") -> "RptExecutableEntityEvent":
        """
        AUTOSAR-compliant setter for rptImplPolicy with method chaining.
        
        Args:
            value: The rptImplPolicy to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rpt_impl_policy property setter (gets validation automatically)
        """
        self.rpt_impl_policy = value  # Delegates to property setter
        return self

    def getRptServicePoint(self) -> List["RptServicePoint"]:
        """
        AUTOSAR-compliant getter for rptServicePoint.
        
        Returns:
            The rptServicePoint value
        
        Note:
            Delegates to rpt_service_point property (CODING_RULE_V2_00017)
        """
        return self.rpt_service_point  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rpt_event_id(self, value: Optional["PositiveInteger"]) -> "RptExecutableEntityEvent":
        """
        Set rptEventId and return self for chaining.
        
        Args:
            value: The rptEventId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rpt_event_id("value")
        """
        self.rpt_event_id = value  # Use property setter (gets validation)
        return self

    def with_rpt_executable(self, value: Optional["RptExecutableEntity"]) -> "RptExecutableEntityEvent":
        """
        Set rptExecutable and return self for chaining.
        
        Args:
            value: The rptExecutable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rpt_executable("value")
        """
        self.rpt_executable = value  # Use property setter (gets validation)
        return self

    def with_rpt_impl_policy(self, value: Optional["RptImplPolicy"]) -> "RptExecutableEntityEvent":
        """
        Set rptImplPolicy and return self for chaining.
        
        Args:
            value: The rptImplPolicy to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rpt_impl_policy("value")
        """
        self.rpt_impl_policy = value  # Use property setter (gets validation)
        return self