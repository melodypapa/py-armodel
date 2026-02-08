from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceNeeds,
)


class ComMgrUserNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Communication
    Manager for one "user".

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 235, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 711, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum communication mode requested by this ComM.
        self._maxComm: Optional["MaxCommModeEnum"] = None

    @property
    def max_comm(self) -> Optional["MaxCommModeEnum"]:
        """Get maxComm (Pythonic accessor)."""
        return self._maxComm

    @max_comm.setter
    def max_comm(self, value: Optional["MaxCommModeEnum"]) -> None:
        """
        Set maxComm with validation.

        Args:
            value: The maxComm to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxComm = None
            return

        if not isinstance(value, MaxCommModeEnum):
            raise TypeError(
                f"maxComm must be MaxCommModeEnum or None, got {type(value).__name__}"
            )
        self._maxComm = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxComm(self) -> "MaxCommModeEnum":
        """
        AUTOSAR-compliant getter for maxComm.

        Returns:
            The maxComm value

        Note:
            Delegates to max_comm property (CODING_RULE_V2_00017)
        """
        return self.max_comm  # Delegates to property

    def setMaxComm(self, value: "MaxCommModeEnum") -> "ComMgrUserNeeds":
        """
        AUTOSAR-compliant setter for maxComm with method chaining.

        Args:
            value: The maxComm to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_comm property setter (gets validation automatically)
        """
        self.max_comm = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_comm(self, value: Optional["MaxCommModeEnum"]) -> "ComMgrUserNeeds":
        """
        Set maxComm and return self for chaining.

        Args:
            value: The maxComm to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_comm("value")
        """
        self.max_comm = value  # Use property setter (gets validation)
        return self
