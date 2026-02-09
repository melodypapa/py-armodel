"""
AUTOSAR Package - ImplicitCommunicationBehavior

Package: M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class ConsistencyNeeds(Identifiable):
    """
    This meta-class represents the ability to define requirements on the
    implicit communication behavior.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior::ConsistencyNeeds
    
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
        self._dpgDoesNot: List["RefType"] = []

    @property
    def dpg_does_not(self) -> List["RefType"]:
        """Get dpgDoesNot (Pythonic accessor)."""
        return self._dpgDoesNot
        # This group of VariableDataPrototypes requires coherency respect to the
                # implicit communication behavior, i.
        # e.
        # and write access to VariableDataPrototypes in the the RunnableEntitys of the
                # to be handled in a coherent atpVariation.
        self._dpgRequires: List["RefType"] = []

    @property
    def dpg_requires(self) -> List["RefType"]:
        """Get dpgRequires (Pythonic accessor)."""
        return self._dpgRequires
        # This group of RunnableEntities does not require stability respect to the
                # implicit communication behavior.
        # atpVariation.
        self._regDoesNot: List["RefType"] = []

    @property
    def reg_does_not(self) -> List["RefType"]:
        """Get regDoesNot (Pythonic accessor)."""
        return self._regDoesNot
        # This group of RunnableEntities requires stability with to the implicit
                # communication behavior, i.
        # e.
        # all write access to VariableDataPrototypes in the the RunnableEntitys of the
                # to be handled in a stable atpVariation.
        self._regRequires: List["RefType"] = []

    @property
    def reg_requires(self) -> List["RefType"]:
        """Get regRequires (Pythonic accessor)."""
        return self._regRequires

    def with_dpg_does_not(self, value):
        """
        Set dpg_does_not and return self for chaining.

        Args:
            value: The dpg_does_not to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dpg_does_not("value")
        """
        self.dpg_does_not = value  # Use property setter (gets validation)
        return self

    def with_dpg_requires(self, value):
        """
        Set dpg_requires and return self for chaining.

        Args:
            value: The dpg_requires to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dpg_requires("value")
        """
        self.dpg_requires = value  # Use property setter (gets validation)
        return self

    def with_reg_does_not(self, value):
        """
        Set reg_does_not and return self for chaining.

        Args:
            value: The reg_does_not to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reg_does_not("value")
        """
        self.reg_does_not = value  # Use property setter (gets validation)
        return self

    def with_reg_requires(self, value):
        """
        Set reg_requires and return self for chaining.

        Args:
            value: The reg_requires to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reg_requires("value")
        """
        self.reg_requires = value  # Use property setter (gets validation)
        return self

    def with_runnable_entity(self, value):
        """
        Set runnable_entity and return self for chaining.

        Args:
            value: The runnable_entity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_runnable_entity("value")
        """
        self.runnable_entity = value  # Use property setter (gets validation)
        return self

    def with_runnable_entity_group_in_composition_instance_ref(self, value):
        """
        Set runnable_entity_group_in_composition_instance_ref and return self for chaining.

        Args:
            value: The runnable_entity_group_in_composition_instance_ref to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_runnable_entity_group_in_composition_instance_ref("value")
        """
        self.runnable_entity_group_in_composition_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_data_prototype_group_in_composition_instance_ref(self, value):
        """
        Set data_prototype_group_in_composition_instance_ref and return self for chaining.

        Args:
            value: The data_prototype_group_in_composition_instance_ref to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_prototype_group_in_composition_instance_ref("value")
        """
        self.data_prototype_group_in_composition_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_implicit_data(self, value):
        """
        Set implicit_data and return self for chaining.

        Args:
            value: The implicit_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_implicit_data("value")
        """
        self.implicit_data = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDpgDoesNot(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for dpgDoesNot.
        
        Returns:
            The dpgDoesNot value
        
        Note:
            Delegates to dpg_does_not property (CODING_RULE_V2_00017)
        """
        return self.dpg_does_not  # Delegates to property

    def getDpgRequires(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for dpgRequires.
        
        Returns:
            The dpgRequires value
        
        Note:
            Delegates to dpg_requires property (CODING_RULE_V2_00017)
        """
        return self.dpg_requires  # Delegates to property

    def getRegDoesNot(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for regDoesNot.
        
        Returns:
            The regDoesNot value
        
        Note:
            Delegates to reg_does_not property (CODING_RULE_V2_00017)
        """
        return self.reg_does_not  # Delegates to property

    def getRegRequires(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for regRequires.
        
        Returns:
            The regRequires value
        
        Note:
            Delegates to reg_requires property (CODING_RULE_V2_00017)
        """
        return self.reg_requires  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



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
        self._runnableEntityGroupInCompositionInstanceRef: List["RefType"] = []

    @property
    def runnable_entity_group_in_composition_instance_ref(self) -> List["RefType"]:
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

    def getRunnableEntityGroupInCompositionInstanceRef(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for runnableEntityGroupInCompositionInstanceRef.
        
        Returns:
            The runnableEntityGroupInCompositionInstanceRef value
        
        Note:
            Delegates to runnable_entity_group_in_composition_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.runnable_entity_group_in_composition_instance_ref  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DataPrototypeGroup(Identifiable):
    """
    This meta-class represents the ability to define a collection of
    DataPrototypes that are subject to the formal definition of implicit
    communication behavior. The definition of the collection can be nested.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior::DataPrototypeGroup
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 223, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 180, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # atpVariation by: InnerDataPrototype.
        self._dataPrototypeGroupInCompositionInstanceRef: List["RefType"] = []

    @property
    def data_prototype_group_in_composition_instance_ref(self) -> List["RefType"]:
        """Get dataPrototypeGroupInCompositionInstanceRef (Pythonic accessor)."""
        return self._dataPrototypeGroupInCompositionInstanceRef
        # belong to the enclosing DataPrototypeGroup atpVariation by:
        # VariableDataPrototypeIn.
        self._implicitData: List["RefType"] = []

    @property
    def implicit_data(self) -> List["RefType"]:
        """Get implicitData (Pythonic accessor)."""
        return self._implicitData

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataPrototypeGroupInCompositionInstanceRef(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for dataPrototypeGroupInCompositionInstanceRef.
        
        Returns:
            The dataPrototypeGroupInCompositionInstanceRef value
        
        Note:
            Delegates to data_prototype_group_in_composition_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.data_prototype_group_in_composition_instance_ref  # Delegates to property

    def getImplicitData(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for implicitData.
        
        Returns:
            The implicitData value
        
        Note:
            Delegates to implicit_data property (CODING_RULE_V2_00017)
        """
        return self.implicit_data  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====


__all__ = [
    "ConsistencyNeeds",
    "RunnableEntityGroup",
    "DataPrototypeGroup",
]
