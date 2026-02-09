from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class SdgDef(ARElement):
    """
    A SdgDef groups several SdgClasses which belong to the same extension. The
    concept of an SdgDef is similiar to an UML Profile.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 99, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 207, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The owned sdgClasses which define the structure of the.
        self._sdgClass: List["SdgClass"] = []

    @property
    def sdg_class(self) -> List["SdgClass"]:
        """Get sdgClass (Pythonic accessor)."""
        return self._sdgClass

    def with_sdg_class(self, value):
        """
        Set sdg_class and return self for chaining.

        Args:
            value: The sdg_class to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdg_class("value")
        """
        self.sdg_class = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSdgClass(self) -> List["SdgClass"]:
        """
        AUTOSAR-compliant getter for sdgClass.

        Returns:
            The sdgClass value

        Note:
            Delegates to sdg_class property (CODING_RULE_V2_00017)
        """
        return self.sdg_class  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
