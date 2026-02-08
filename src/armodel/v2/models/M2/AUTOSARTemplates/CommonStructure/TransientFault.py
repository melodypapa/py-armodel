from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import TracedFailure


class TransientFault(TracedFailure):
    """
    The reported failure is classified as runtime error.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::TransientFault

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1009, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Describes a possible error reactions for the transient fault.
        self._possibleError: List["PossibleErrorReaction"] = []

    @property
    def possible_error(self) -> List["PossibleErrorReaction"]:
        """Get possibleError (Pythonic accessor)."""
        return self._possibleError

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPossibleError(self) -> List["PossibleErrorReaction"]:
        """
        AUTOSAR-compliant getter for possibleError.

        Returns:
            The possibleError value

        Note:
            Delegates to possible_error property (CODING_RULE_V2_00017)
        """
        return self.possible_error  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
