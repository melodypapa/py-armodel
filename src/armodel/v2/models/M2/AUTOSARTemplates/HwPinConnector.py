from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Describable,
)


class HwPinConnector(Describable):
    """
    This meta-class represents the ability to connect two pins.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate

    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 22, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This association connects two hardware pins.
        self._hwPin: List["HwPin"] = []

    @property
    def hw_pin(self) -> List["HwPin"]:
        """Get hwPin (Pythonic accessor)."""
        return self._hwPin

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwPin(self) -> List["HwPin"]:
        """
        AUTOSAR-compliant getter for hwPin.

        Returns:
            The hwPin value

        Note:
            Delegates to hw_pin property (CODING_RULE_V2_00017)
        """
        return self.hw_pin  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
