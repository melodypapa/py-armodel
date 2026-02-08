from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import MappingConstraint

    RefType,
)


class ComponentSeparation(MappingConstraint):
    """
    Constraint that forces the two referenced SW components (called A and B in
    the following) not to be mapped to the same ECU, Core, Partition depending
    on the defined mappingScope attribute. If mapping Scope is not specified
    then mappingScopeEcu shall be assumed. If a SW component (e.g. A) is a
    composition, none of the atomic SW components making up the A composition
    shall be mapped together with any of the atomic SW components making up the
    B composition. Furthermore, A and B shall be disjoint.

    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::ComponentSeparation

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 205, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute indicates whether the Component constraint applies to
                # different ECUs, cores.
        # If this attribute is not specified then be assumed.
        # 0.
        # 2 iref The two components that have to be mapped to different ECUs by:
                # ComponentInSystem.
        self._mappingScope: RefType = None

    @property
    def mapping_scope(self) -> RefType:
        """Get mappingScope (Pythonic accessor)."""
        return self._mappingScope

    @mapping_scope.setter
    def mapping_scope(self, value: RefType) -> None:
        """
        Set mappingScope with validation.

        Args:
            value: The mappingScope to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mappingScope = None
            return

        self._mappingScope = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMappingScope(self) -> RefType:
        """
        AUTOSAR-compliant getter for mappingScope.

        Returns:
            The mappingScope value

        Note:
            Delegates to mapping_scope property (CODING_RULE_V2_00017)
        """
        return self.mapping_scope  # Delegates to property

    def setMappingScope(self, value: RefType) -> "ComponentSeparation":
        """
        AUTOSAR-compliant setter for mappingScope with method chaining.

        Args:
            value: The mappingScope to set

        Returns:
            self for method chaining

        Note:
            Delegates to mapping_scope property setter (gets validation automatically)
        """
        self.mapping_scope = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mapping_scope(self, value: Optional[RefType]) -> "ComponentSeparation":
        """
        Set mappingScope and return self for chaining.

        Args:
            value: The mappingScope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapping_scope("value")
        """
        self.mapping_scope = value  # Use property setter (gets validation)
        return self
