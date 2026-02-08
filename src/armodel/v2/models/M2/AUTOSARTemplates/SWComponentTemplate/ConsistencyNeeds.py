from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ConsistencyNeeds(Identifiable):
    """
    This meta-class represents the ability to define requirements on the
    implicit communication behavior.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 221, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 178, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This group of VariableDataPrototypes does not require with respect to the
        # implicit communication atpVariation 1228 Document ID 62:
        # AUTOSAR_CP_TPS_SoftwareComponentTemplate Template R23-11.
        self._dpgDoesNot: List[RefType] = []

    @property
    def dpg_does_not(self) -> List[RefType]:
        """Get dpgDoesNot (Pythonic accessor)."""
        return self._dpgDoesNot
        # This group of VariableDataPrototypes requires coherency respect to the
                # implicit communication behavior, i.
        # e.
        # and write access to VariableDataPrototypes in the the RunnableEntitys of the
                # to be handled in a coherent atpVariation.
        self._dpgRequires: List[RefType] = []

    @property
    def dpg_requires(self) -> List[RefType]:
        """Get dpgRequires (Pythonic accessor)."""
        return self._dpgRequires
        # This group of RunnableEntities does not require stability respect to the
                # implicit communication behavior.
        # atpVariation.
        self._regDoesNot: List[RefType] = []

    @property
    def reg_does_not(self) -> List[RefType]:
        """Get regDoesNot (Pythonic accessor)."""
        return self._regDoesNot
        # This group of RunnableEntities requires stability with to the implicit
                # communication behavior, i.
        # e.
        # all write access to VariableDataPrototypes in the the RunnableEntitys of the
                # to be handled in a stable atpVariation.
        self._regRequires: List[RefType] = []

    @property
    def reg_requires(self) -> List[RefType]:
        """Get regRequires (Pythonic accessor)."""
        return self._regRequires

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDpgDoesNot(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for dpgDoesNot.

        Returns:
            The dpgDoesNot value

        Note:
            Delegates to dpg_does_not property (CODING_RULE_V2_00017)
        """
        return self.dpg_does_not  # Delegates to property

    def getDpgRequires(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for dpgRequires.

        Returns:
            The dpgRequires value

        Note:
            Delegates to dpg_requires property (CODING_RULE_V2_00017)
        """
        return self.dpg_requires  # Delegates to property

    def getRegDoesNot(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for regDoesNot.

        Returns:
            The regDoesNot value

        Note:
            Delegates to reg_does_not property (CODING_RULE_V2_00017)
        """
        return self.reg_does_not  # Delegates to property

    def getRegRequires(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for regRequires.

        Returns:
            The regRequires value

        Note:
            Delegates to reg_requires property (CODING_RULE_V2_00017)
        """
        return self.reg_requires  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
