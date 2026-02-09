from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ComManagementMapping(Identifiable):
    """
    Describes a mapping between one or several Mode Management PortGroups and
    communication channels.

    Package: M2::AUTOSARTemplates::SystemTemplate

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 282, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # channel.
        # This reference is optional in that the System Description doesn’t use a
                # complete Description (VFB View).
        # This inclusion of legacy systems.
        # by: PortGroupInSystem.
        self._com: List[RefType] = []

    @property
    def com(self) -> List[RefType]:
        """Get com (Pythonic accessor)."""
        return self._com
        # This reference maps the Mode Management PortGroup network to communication
        # channels.
        self._physical: List["PhysicalChannel"] = []

    @property
    def physical(self) -> List["PhysicalChannel"]:
        """Get physical (Pythonic accessor)."""
        return self._physical

    def with_com(self, value):
        """
        Set com and return self for chaining.

        Args:
            value: The com to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_com("value")
        """
        self.com = value  # Use property setter (gets validation)
        return self

    def with_physical(self, value):
        """
        Set physical and return self for chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_physical("value")
        """
        self.physical = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCom(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for com.

        Returns:
            The com value

        Note:
            Delegates to com property (CODING_RULE_V2_00017)
        """
        return self.com  # Delegates to property

    def getPhysical(self) -> List["PhysicalChannel"]:
        """
        AUTOSAR-compliant getter for physical.

        Returns:
            The physical value

        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
