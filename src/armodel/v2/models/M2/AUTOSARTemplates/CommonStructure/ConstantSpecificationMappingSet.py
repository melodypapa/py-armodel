from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class ConstantSpecificationMappingSet(ARElement):
    """
    This meta-class represents the ability to map two ConstantSpecifications to
    each others. One Constant Specification is supposed to be described in the
    application domain and the other should be described in the implementation
    domain.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 445, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ConstantSpecificationMappings owned by the Constant.
        self._mapping: List["ConstantSpecification"] = []

    @property
    def mapping(self) -> List["ConstantSpecification"]:
        """Get mapping (Pythonic accessor)."""
        return self._mapping

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMapping(self) -> List["ConstantSpecification"]:
        """
        AUTOSAR-compliant getter for mapping.

        Returns:
            The mapping value

        Note:
            Delegates to mapping property (CODING_RULE_V2_00017)
        """
        return self.mapping  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
