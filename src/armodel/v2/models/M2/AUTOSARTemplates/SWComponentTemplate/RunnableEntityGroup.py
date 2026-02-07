from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RunnableEntityGroup(Identifiable):
    """
    This meta-class represents the ability to define a collection of
    RunnableEntities. The collection can be nested.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior::RunnableEntityGroup

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 222, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 206, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # the enclosing RunnableEntityGroup.
        # atpVariation runnable by: RunnableEntityIn 1228 Document ID 62:
                # AUTOSAR_CP_TPS_SoftwareComponentTemplate Template R23-11.
        self._runnableEntity: List["RunnableEntity"] = []

    @property
    def runnable_entity(self) -> List["RunnableEntity"]:
        """Get runnableEntity (Pythonic accessor)."""
        return self._runnableEntity
        # atpVariation by: InnerRunnableEntity.
        self._runnableEntityGroupInCompositionInstanceRef: List[RefType] = []

    @property
    def runnable_entity_group_in_composition_instance_ref(self) -> List[RefType]:
        """Get runnableEntityGroupInCompositionInstanceRef (Pythonic accessor)."""
        return self._runnableEntityGroupInCompositionInstanceRef

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRunnableEntity(self) -> List["RunnableEntity"]:
        """
        AUTOSAR-compliant getter for runnableEntity.

        Returns:
            The runnableEntity value

        Note:
            Delegates to runnable_entity property (CODING_RULE_V2_00017)
        """
        return self.runnable_entity  # Delegates to property

    def getRunnableEntityGroupInCompositionInstanceRef(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for runnableEntityGroupInCompositionInstanceRef.

        Returns:
            The runnableEntityGroupInCompositionInstanceRef value

        Note:
            Delegates to runnable_entity_group_in_composition_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.runnable_entity_group_in_composition_instance_ref  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
