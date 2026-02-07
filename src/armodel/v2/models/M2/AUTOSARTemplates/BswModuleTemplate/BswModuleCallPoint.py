from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import (
    Referrable,
)


class BswModuleCallPoint(Referrable, ABC):
    """
    Represents a point at which a BswModuleEntity handles a procedure call into
    a BswModuleEntry, either directly or via the BSW Scheduler.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswModuleCallPoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 77, Classic
      Platform R23-11)
    """
    def __init__(self):
        if type(self) is BswModuleCallPoint:
            raise TypeError("BswModuleCallPoint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The existence of this reference indicates that the call point is used only in
        # the context of the referred Bsw.
        self._context: List["BswDistinguished"] = []

    @property
    def context(self) -> List["BswDistinguished"]:
        """Get context (Pythonic accessor)."""
        return self._context

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContext(self) -> List["BswDistinguished"]:
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
