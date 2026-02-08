from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinConfigurationEntry


class AssignNad(LinConfigurationEntry):
    """
    Schedule entry for an Assign NAD master request.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication::AssignNad

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 438, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The newly assigned NAD value.
        self._newNad: Optional["Integer"] = None

    @property
    def new_nad(self) -> Optional["Integer"]:
        """Get newNad (Pythonic accessor)."""
        return self._newNad

    @new_nad.setter
    def new_nad(self, value: Optional["Integer"]) -> None:
        """
        Set newNad with validation.

        Args:
            value: The newNad to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._newNad = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"newNad must be Integer or None, got {type(value).__name__}"
            )
        self._newNad = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNewNad(self) -> "Integer":
        """
        AUTOSAR-compliant getter for newNad.

        Returns:
            The newNad value

        Note:
            Delegates to new_nad property (CODING_RULE_V2_00017)
        """
        return self.new_nad  # Delegates to property

    def setNewNad(self, value: "Integer") -> "AssignNad":
        """
        AUTOSAR-compliant setter for newNad with method chaining.

        Args:
            value: The newNad to set

        Returns:
            self for method chaining

        Note:
            Delegates to new_nad property setter (gets validation automatically)
        """
        self.new_nad = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_new_nad(self, value: Optional["Integer"]) -> "AssignNad":
        """
        Set newNad and return self for chaining.

        Args:
            value: The newNad to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_new_nad("value")
        """
        self.new_nad = value  # Use property setter (gets validation)
        return self
