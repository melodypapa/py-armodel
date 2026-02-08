from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwDescriptionEntity

    RefType,
)


class HwElement(HwDescriptionEntity):
    """
    This represents the ability to describe Hardware Elements on an instance
    level. The particular types of hardware are distinguished by the category.
    This category determines the applicable attributes. The possible categories
    and attributes are defined in HwCategory.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 296, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 18, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 991, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2026, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents one particular connection between two elements.
        # atpVariation.
        self._hwElement: List["HwElementConnector"] = []

    @property
    def hw_element(self) -> List["HwElementConnector"]:
        """Get hwElement (Pythonic accessor)."""
        return self._hwElement
        # This aggregation is used to describe the connection a hardware element.
        # Note that hardware no pins but only pingroups.
        # atpVariation.
        self._hwPinGroup: List[RefType] = []

    @property
    def hw_pin_group(self) -> List[RefType]:
        """Get hwPinGroup (Pythonic accessor)."""
        return self._hwPinGroup
        # This association is used to establish hierarchies of hw that one particular
                # HwElement can be this association only once.
        # I.
        # e.
        # multiple the same HwElement is not supported (at level).
        # atpVariation.
        self._nestedElement: List["HwElement"] = []

    @property
    def nested_element(self) -> List["HwElement"]:
        """Get nestedElement (Pythonic accessor)."""
        return self._nestedElement

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwElement(self) -> List["HwElementConnector"]:
        """
        AUTOSAR-compliant getter for hwElement.

        Returns:
            The hwElement value

        Note:
            Delegates to hw_element property (CODING_RULE_V2_00017)
        """
        return self.hw_element  # Delegates to property

    def getHwPinGroup(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for hwPinGroup.

        Returns:
            The hwPinGroup value

        Note:
            Delegates to hw_pin_group property (CODING_RULE_V2_00017)
        """
        return self.hw_pin_group  # Delegates to property

    def getNestedElement(self) -> List["HwElement"]:
        """
        AUTOSAR-compliant getter for nestedElement.

        Returns:
            The nestedElement value

        Note:
            Delegates to nested_element property (CODING_RULE_V2_00017)
        """
        return self.nested_element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
