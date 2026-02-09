from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class EcucEnumerationLiteralDef(Identifiable):
    """
    Configuration parameter type for enumeration literals definition.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 67, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If it evaluates to true the literal definition shall be as specified.
        # Otherwise the literal definition ignored.
        self._ecucCond: Optional["EcucCondition"] = None

    @property
    def ecuc_cond(self) -> Optional["EcucCondition"]:
        """Get ecucCond (Pythonic accessor)."""
        return self._ecucCond

    @ecuc_cond.setter
    def ecuc_cond(self, value: Optional["EcucCondition"]) -> None:
        """
        Set ecucCond with validation.

        Args:
            value: The ecucCond to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecucCond = None
            return

        if not isinstance(value, EcucCondition):
            raise TypeError(
                f"ecucCond must be EcucCondition or None, got {type(value).__name__}"
            )
        self._ecucCond = value
        # vendor-specific.
        self._origin: Optional["String"] = None

    @property
    def origin(self) -> Optional["String"]:
        """Get origin (Pythonic accessor)."""
        return self._origin

    @origin.setter
    def origin(self, value: Optional["String"]) -> None:
        """
        Set origin with validation.

        Args:
            value: The origin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._origin = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"origin must be String or None, got {type(value).__name__}"
            )
        self._origin = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcucCond(self) -> "EcucCondition":
        """
        AUTOSAR-compliant getter for ecucCond.

        Returns:
            The ecucCond value

        Note:
            Delegates to ecuc_cond property (CODING_RULE_V2_00017)
        """
        return self.ecuc_cond  # Delegates to property

    def setEcucCond(self, value: "EcucCondition") -> "EcucEnumerationLiteralDef":
        """
        AUTOSAR-compliant setter for ecucCond with method chaining.

        Args:
            value: The ecucCond to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecuc_cond property setter (gets validation automatically)
        """
        self.ecuc_cond = value  # Delegates to property setter
        return self

    def getOrigin(self) -> "String":
        """
        AUTOSAR-compliant getter for origin.

        Returns:
            The origin value

        Note:
            Delegates to origin property (CODING_RULE_V2_00017)
        """
        return self.origin  # Delegates to property

    def setOrigin(self, value: "String") -> "EcucEnumerationLiteralDef":
        """
        AUTOSAR-compliant setter for origin with method chaining.

        Args:
            value: The origin to set

        Returns:
            self for method chaining

        Note:
            Delegates to origin property setter (gets validation automatically)
        """
        self.origin = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecuc_cond(self, value: Optional["EcucCondition"]) -> "EcucEnumerationLiteralDef":
        """
        Set ecucCond and return self for chaining.

        Args:
            value: The ecucCond to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecuc_cond("value")
        """
        self.ecuc_cond = value  # Use property setter (gets validation)
        return self

    def with_origin(self, value: Optional["String"]) -> "EcucEnumerationLiteralDef":
        """
        Set origin and return self for chaining.

        Args:
            value: The origin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_origin("value")
        """
        self.origin = value  # Use property setter (gets validation)
        return self
