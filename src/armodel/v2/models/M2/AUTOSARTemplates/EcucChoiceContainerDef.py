from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    EcucContainerDef,
    EcucParamConf,
)


class EcucChoiceContainerDef(EcucContainerDef):
    """
    Used to define configuration containers that provide a choice between
    several EcucParamConfContainer Def. But in the actual ECU Configuration
    Values only one instance from the choice list will be present.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucChoiceContainerDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 41, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The choices available in a EcucChoiceContainerDef.
        # atpSplitable.
        self._choice: List["EcucParamConf"] = []

    @property
    def choice(self) -> List["EcucParamConf"]:
        """Get choice (Pythonic accessor)."""
        return self._choice

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChoice(self) -> List["EcucParamConf"]:
        """
        AUTOSAR-compliant getter for choice.

        Returns:
            The choice value

        Note:
            Delegates to choice property (CODING_RULE_V2_00017)
        """
        return self.choice  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
