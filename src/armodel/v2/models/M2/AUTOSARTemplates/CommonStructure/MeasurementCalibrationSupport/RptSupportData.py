from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class RptSupportData(ARObject):
    """
    Root element for rapid prototyping support data related to one
    Implementation artifact on an ECU, in particular the RTE. The rapid
    prototyping support data may reference to elements provided for Mc
    SupportData.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 198, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines an environment for the execution of Executable.
        self._execution: List["RptExecutionContext"] = []

    @property
    def execution(self) -> List["RptExecutionContext"]:
        """Get execution (Pythonic accessor)."""
        return self._execution
        # Description of components for which rapid prototyping implemented.
        # atpVariation.
        self._rptComponent: List["RptComponent"] = []

    @property
    def rpt_component(self) -> List["RptComponent"]:
        """Get rptComponent (Pythonic accessor)."""
        return self._rptComponent
        # This aggregation represents the collection of service with the enclosing
        # RptSuportData atpVariation.
        self._rptServicePoint: List["RptServicePoint"] = []

    @property
    def rpt_service_point(self) -> List["RptServicePoint"]:
        """Get rptServicePoint (Pythonic accessor)."""
        return self._rptServicePoint

    def with_execution(self, value):
        """
        Set execution and return self for chaining.

        Args:
            value: The execution to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_execution("value")
        """
        self.execution = value  # Use property setter (gets validation)
        return self

    def with_rpt_component(self, value):
        """
        Set rpt_component and return self for chaining.

        Args:
            value: The rpt_component to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_component("value")
        """
        self.rpt_component = value  # Use property setter (gets validation)
        return self

    def with_rpt_service_point(self, value):
        """
        Set rpt_service_point and return self for chaining.

        Args:
            value: The rpt_service_point to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_service_point("value")
        """
        self.rpt_service_point = value  # Use property setter (gets validation)
        return self

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

    def getRptComponent(self) -> List["RptComponent"]:
        """
        AUTOSAR-compliant getter for rptComponent.

        Returns:
            The rptComponent value

        Note:
            Delegates to rpt_component property (CODING_RULE_V2_00017)
        """
        return self.rpt_component  # Delegates to property

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
