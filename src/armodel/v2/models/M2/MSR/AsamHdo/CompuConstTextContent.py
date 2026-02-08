from typing import Optional


class CompuConstTextContent(CompuConstContent):
    """
    This meta-class represents the textual content of a scale.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuConstTextContent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 388, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2010, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a textual constant in the computation.
        self._vt: Optional["VerbatimString"] = None

    @property
    def vt(self) -> Optional["VerbatimString"]:
        """Get vt (Pythonic accessor)."""
        return self._vt

    @vt.setter
    def vt(self, value: Optional["VerbatimString"]) -> None:
        """
        Set vt with validation.

        Args:
            value: The vt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vt = None
            return

        if not isinstance(value, VerbatimString):
            raise TypeError(
                f"vt must be VerbatimString or None, got {type(value).__name__}"
            )
        self._vt = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getVt(self) -> "VerbatimString":
        """
        AUTOSAR-compliant getter for vt.

        Returns:
            The vt value

        Note:
            Delegates to vt property (CODING_RULE_V2_00017)
        """
        return self.vt  # Delegates to property

    def setVt(self, value: "VerbatimString") -> "CompuConstTextContent":
        """
        AUTOSAR-compliant setter for vt with method chaining.

        Args:
            value: The vt to set

        Returns:
            self for method chaining

        Note:
            Delegates to vt property setter (gets validation automatically)
        """
        self.vt = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_vt(self, value: Optional["VerbatimString"]) -> "CompuConstTextContent":
        """
        Set vt and return self for chaining.

        Args:
            value: The vt to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vt("value")
        """
        self.vt = value  # Use property setter (gets validation)
        return self
