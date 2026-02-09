from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultilanguageReferrable import (
    MultilanguageReferrable,
)


class Traceable(MultilanguageReferrable, ABC):
    """
    that it is expected that its subclasses inherit either from
    MultilanguageReferrable or from Identifiable. Nevertheless it also inherits
    from MultilanguageReferrable in order to provide a common reference target
    for all Traceables.

    Package: M2::MSR::Documentation::BlockElements::RequirementsTracing

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 312, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 221, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is Traceable:
            raise TypeError("Traceable is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This association represents the ability to trace to / constraints.
        # This supports for bottom up tracing MainRequirements <- Features <- BSW/AI.
        self._trace: List["Traceable"] = []

    @property
    def trace(self) -> List["Traceable"]:
        """Get trace (Pythonic accessor)."""
        return self._trace

    def with_trace(self, value):
        """
        Set trace and return self for chaining.

        Args:
            value: The trace to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trace("value")
        """
        self.trace = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTrace(self) -> List["Traceable"]:
        """
        AUTOSAR-compliant getter for trace.

        Returns:
            The trace value

        Note:
            Delegates to trace property (CODING_RULE_V2_00017)
        """
        return self.trace  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
