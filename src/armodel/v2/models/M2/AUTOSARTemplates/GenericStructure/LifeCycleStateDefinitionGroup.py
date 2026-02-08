from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class LifeCycleStateDefinitionGroup(ARElement):
    """
    This meta class represents the ability to define the states and properties
    of one particular life cycle.

    Package: M2::AUTOSARTemplates::GenericStructure::LifeCycles::LifeCycleStateDefinitionGroup

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 388, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 196, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Describes a single life cycle state of this life cycle state.
        self._lcState: List["LifeCycleState"] = []

    @property
    def lc_state(self) -> List["LifeCycleState"]:
        """Get lcState (Pythonic accessor)."""
        return self._lcState

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLcState(self) -> List["LifeCycleState"]:
        """
        AUTOSAR-compliant getter for lcState.

        Returns:
            The lcState value

        Note:
            Delegates to lc_state property (CODING_RULE_V2_00017)
        """
        return self.lc_state  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
