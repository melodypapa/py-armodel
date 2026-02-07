from typing import List


class EcucDefinitionCollection(ARElement):
    """
    This represents the anchor point of an ECU Configuration Parameter
    Definition within the AUTOSAR templates structure.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucDefinitionCollection

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 25, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 185, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # References to the module definitions of individual.
        self._module: List["EcucModuleDef"] = []

    @property
    def module(self) -> List["EcucModuleDef"]:
        """Get module (Pythonic accessor)."""
        return self._module

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModule(self) -> List["EcucModuleDef"]:
        """
        AUTOSAR-compliant getter for module.

        Returns:
            The module value

        Note:
            Delegates to module property (CODING_RULE_V2_00017)
        """
        return self.module  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
