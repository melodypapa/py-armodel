from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class DataPrototypeGroup(Identifiable):
    """
    This meta-class represents the ability to define a collection of
    DataPrototypes that are subject to the formal definition of implicit
    communication behavior. The definition of the collection can be nested.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 223, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 180, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # atpVariation by: InnerDataPrototype.
        self._dataPrototypeGroupInCompositionInstanceRef: List[RefType] = []

    @property
    def data_prototype_group_in_composition_instance_ref(self) -> List[RefType]:
        """Get dataPrototypeGroupInCompositionInstanceRef (Pythonic accessor)."""
        return self._dataPrototypeGroupInCompositionInstanceRef
        # belong to the enclosing DataPrototypeGroup atpVariation by:
        # VariableDataPrototypeIn.
        self._implicitData: List[RefType] = []

    @property
    def implicit_data(self) -> List[RefType]:
        """Get implicitData (Pythonic accessor)."""
        return self._implicitData

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

    def getDataPrototypeGroupInCompositionInstanceRef(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for dataPrototypeGroupInCompositionInstanceRef.

        Returns:
            The dataPrototypeGroupInCompositionInstanceRef value

        Note:
            Delegates to data_prototype_group_in_composition_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.data_prototype_group_in_composition_instance_ref  # Delegates to property

    def getImplicitData(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for implicitData.

        Returns:
            The implicitData value

        Note:
            Delegates to implicit_data property (CODING_RULE_V2_00017)
        """
        return self.implicit_data  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
