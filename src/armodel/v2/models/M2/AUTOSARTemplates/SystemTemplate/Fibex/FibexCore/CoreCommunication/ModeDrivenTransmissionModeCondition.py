from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class ModeDrivenTransmissionModeCondition(ARObject):
    """
    The condition defined by this class evaluates to true if one of the
    referenced modeDeclarations (OR associated) is active. All referenced
    modeDeclarations shall be from the same ModeDeclarationGroup. The condition
    is used to define which TransmissionMode shall be activated using
    Com_SwitchIpduTx Mode.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::ModeDrivenTransmissionModeCondition

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 393, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to one modeDeclaration which is OR in the context of the
        # ModeDrivenTransmission.
        self._mode: List["ModeDeclaration"] = []

    @property
    def mode(self) -> List["ModeDeclaration"]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMode(self) -> List["ModeDeclaration"]:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
