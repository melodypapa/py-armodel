from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class HwCategory(ARElement):
    """
    This metaclass represents the ability to declare hardware categories and its
    particular attributes.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory

    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 24, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation describes particular hardware attribute.
        self._hwAttributeDef: List["HwAttributeDef"] = []

    @property
    def hw_attribute_def(self) -> List["HwAttributeDef"]:
        """Get hwAttributeDef (Pythonic accessor)."""
        return self._hwAttributeDef

    def with_hw_attribute_def(self, value):
        """
        Set hw_attribute_def and return self for chaining.

        Args:
            value: The hw_attribute_def to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_hw_attribute_def("value")
        """
        self.hw_attribute_def = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwAttributeDef(self) -> List["HwAttributeDef"]:
        """
        AUTOSAR-compliant getter for hwAttributeDef.

        Returns:
            The hwAttributeDef value

        Note:
            Delegates to hw_attribute_def property (CODING_RULE_V2_00017)
        """
        return self.hw_attribute_def  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
