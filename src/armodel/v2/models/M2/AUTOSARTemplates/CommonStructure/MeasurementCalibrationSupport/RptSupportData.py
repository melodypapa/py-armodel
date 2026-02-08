from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    RptComponent,
    RptExecutionContext,
    RptServicePoint,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class RptSupportData(ARObject):
    """
    Root element for rapid prototyping support data related to one
    Implementation artifact on an ECU, in particular the RTE. The rapid
    prototyping support data may reference to elements provided for Mc
    SupportData.

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport::RptSupportData

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
