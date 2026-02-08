from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    EcucAbstractInternalReferenceDef,
    EcucContainerDef,
)


class EcucChoiceReferenceDef(EcucAbstractInternalReferenceDef):
    """
    Specify alternative references where in the ECU Configuration description
    only one of the specified references will actually be used.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucChoiceReferenceDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 74, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 184, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # All the possible parameter containers for the reference.
        self._destination: List["EcucContainerDef"] = []

    @property
    def destination(self) -> List["EcucContainerDef"]:
        """Get destination (Pythonic accessor)."""
        return self._destination

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestination(self) -> List["EcucContainerDef"]:
        """
        AUTOSAR-compliant getter for destination.

        Returns:
            The destination value

        Note:
            Delegates to destination property (CODING_RULE_V2_00017)
        """
        return self.destination  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
