from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    BswModuleEntity,
    RunnableEntity,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SwcBswRunnableMapping(ARObject):
    """
    Maps a BswModuleEntity to a RunnableEntity if it is implemented as part of a
    BSW module (in the case of an AUTOSAR Service, a Complex Driver or an ECU
    Abstraction). The mapping can be used by a tool to find relevant information
    on the behavior, e.g. whether the bswEntity shall be running in interrupt
    context.

    Package: M2::AUTOSARTemplates::CommonStructure::SwcBswMapping::SwcBswRunnableMapping

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 110, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The mapped BswModuleEntity.
        self._bswEntity: Optional["BswModuleEntity"] = None

    @property
    def bsw_entity(self) -> Optional["BswModuleEntity"]:
        """Get bswEntity (Pythonic accessor)."""
        return self._bswEntity

    @bsw_entity.setter
    def bsw_entity(self, value: Optional["BswModuleEntity"]) -> None:
        """
        Set bswEntity with validation.

        Args:
            value: The bswEntity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswEntity = None
            return

        if not isinstance(value, BswModuleEntity):
            raise TypeError(
                f"bswEntity must be BswModuleEntity or None, got {type(value).__name__}"
            )
        self._bswEntity = value
        # The mapped SWC runnable.
        self._swcRunnable: Optional["RunnableEntity"] = None

    @property
    def swc_runnable(self) -> Optional["RunnableEntity"]:
        """Get swcRunnable (Pythonic accessor)."""
        return self._swcRunnable

    @swc_runnable.setter
    def swc_runnable(self, value: Optional["RunnableEntity"]) -> None:
        """
        Set swcRunnable with validation.

        Args:
            value: The swcRunnable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcRunnable = None
            return

        if not isinstance(value, RunnableEntity):
            raise TypeError(
                f"swcRunnable must be RunnableEntity or None, got {type(value).__name__}"
            )
        self._swcRunnable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswEntity(self) -> "BswModuleEntity":
        """
        AUTOSAR-compliant getter for bswEntity.

        Returns:
            The bswEntity value

        Note:
            Delegates to bsw_entity property (CODING_RULE_V2_00017)
        """
        return self.bsw_entity  # Delegates to property

    def setBswEntity(self, value: "BswModuleEntity") -> "SwcBswRunnableMapping":
        """
        AUTOSAR-compliant setter for bswEntity with method chaining.

        Args:
            value: The bswEntity to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_entity property setter (gets validation automatically)
        """
        self.bsw_entity = value  # Delegates to property setter
        return self

    def getSwcRunnable(self) -> "RunnableEntity":
        """
        AUTOSAR-compliant getter for swcRunnable.

        Returns:
            The swcRunnable value

        Note:
            Delegates to swc_runnable property (CODING_RULE_V2_00017)
        """
        return self.swc_runnable  # Delegates to property

    def setSwcRunnable(self, value: "RunnableEntity") -> "SwcBswRunnableMapping":
        """
        AUTOSAR-compliant setter for swcRunnable with method chaining.

        Args:
            value: The swcRunnable to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_runnable property setter (gets validation automatically)
        """
        self.swc_runnable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_entity(self, value: Optional["BswModuleEntity"]) -> "SwcBswRunnableMapping":
        """
        Set bswEntity and return self for chaining.

        Args:
            value: The bswEntity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_entity("value")
        """
        self.bsw_entity = value  # Use property setter (gets validation)
        return self

    def with_swc_runnable(self, value: Optional["RunnableEntity"]) -> "SwcBswRunnableMapping":
        """
        Set swcRunnable and return self for chaining.

        Args:
            value: The swcRunnable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_runnable("value")
        """
        self.swc_runnable = value  # Use property setter (gets validation)
        return self
