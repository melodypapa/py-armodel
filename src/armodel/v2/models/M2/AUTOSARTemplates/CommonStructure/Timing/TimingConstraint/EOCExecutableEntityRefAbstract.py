from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class EOCExecutableEntityRefAbstract(Identifiable, ABC):
    """
    This is the abstractions for Execution Order Constraint Executable Entity
    References (leaves) and Execution Order Constraint Executable Entity
    Reference Groups (composites).

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 119, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EOCExecutableEntityRefAbstract:
            raise TypeError("EOCExecutableEntityRefAbstract is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The direct successor of an executable entity or a group of entities.
        self._directSuccessor: List["EOCExecutableEntity"] = []

    @property
    def direct_successor(self) -> List["EOCExecutableEntity"]:
        """Get directSuccessor (Pythonic accessor)."""
        return self._directSuccessor

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDirectSuccessor(self) -> List["EOCExecutableEntity"]:
        """
        AUTOSAR-compliant getter for directSuccessor.

        Returns:
            The directSuccessor value

        Note:
            Delegates to direct_successor property (CODING_RULE_V2_00017)
        """
        return self.direct_successor  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
