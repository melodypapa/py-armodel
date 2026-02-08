from typing import List


class AliasNameSet(ARElement):
    """
    This meta-class represents a set of AliasNames. The AliasNameSet can for
    example be an input to the A2L-Generator.

    Package: M2::AUTOSARTemplates::CommonStructure::FlatMap::AliasNameSet

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 174, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 968, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 160, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # AliasNames contained in the AliasNameSet.
        # atpVariation.
        self._aliasName: List["AliasNameAssignment"] = []

    @property
    def alias_name(self) -> List["AliasNameAssignment"]:
        """Get aliasName (Pythonic accessor)."""
        return self._aliasName

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAliasName(self) -> List["AliasNameAssignment"]:
        """
        AUTOSAR-compliant getter for aliasName.

        Returns:
            The aliasName value

        Note:
            Delegates to alias_name property (CODING_RULE_V2_00017)
        """
        return self.alias_name  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
