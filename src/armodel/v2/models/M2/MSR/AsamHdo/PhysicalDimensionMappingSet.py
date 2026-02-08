from typing import List


class PhysicalDimensionMappingSet(ARElement):
    """
    This class represents a container for a list of mappings between
    PhysicalDimensions.

    Package: M2::MSR::AsamHdo::Units

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 399, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents a concrete collections of
        # PhysicalDimensionMappings in the context of one.
        self._physical: List["PhysicalDimension"] = []

    @property
    def physical(self) -> List["PhysicalDimension"]:
        """Get physical (Pythonic accessor)."""
        return self._physical

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPhysical(self) -> List["PhysicalDimension"]:
        """
        AUTOSAR-compliant getter for physical.

        Returns:
            The physical value

        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
