from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceNeeds


class ErrorTracerNeeds(ServiceNeeds):
    """
    Specifies the need to report failures to the error tracer.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::ErrorTracerNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 263, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 832, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # list of traced failures atpVariation.
        self._tracedFailure: List["TracedFailure"] = []

    @property
    def traced_failure(self) -> List["TracedFailure"]:
        """Get tracedFailure (Pythonic accessor)."""
        return self._tracedFailure

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTracedFailure(self) -> List["TracedFailure"]:
        """
        AUTOSAR-compliant getter for tracedFailure.

        Returns:
            The tracedFailure value

        Note:
            Delegates to traced_failure property (CODING_RULE_V2_00017)
        """
        return self.traced_failure  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
