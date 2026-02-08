from abc import ABC


class BaseType(ARElement, ABC):
    """
    This abstract meta-class represents the ability to specify a platform
    dependent base type.

    Package: M2::MSR::AsamHdo::BaseTypes

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 302, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 291, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2002, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is BaseType:
            raise TypeError("BaseType is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the actual definition of the base type.
        self._baseType: "BaseTypeDefinition" = None

    @property
    def base_type(self) -> "BaseTypeDefinition":
        """Get baseType (Pythonic accessor)."""
        return self._baseType

    @base_type.setter
    def base_type(self, value: "BaseTypeDefinition") -> None:
        """
        Set baseType with validation.

        Args:
            value: The baseType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, BaseTypeDefinition):
            raise TypeError(
                f"baseType must be BaseTypeDefinition, got {type(value).__name__}"
            )
        self._baseType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBaseType(self) -> "BaseTypeDefinition":
        """
        AUTOSAR-compliant getter for baseType.

        Returns:
            The baseType value

        Note:
            Delegates to base_type property (CODING_RULE_V2_00017)
        """
        return self.base_type  # Delegates to property

    def setBaseType(self, value: "BaseTypeDefinition") -> "BaseType":
        """
        AUTOSAR-compliant setter for baseType with method chaining.

        Args:
            value: The baseType to set

        Returns:
            self for method chaining

        Note:
            Delegates to base_type property setter (gets validation automatically)
        """
        self.base_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base_type(self, value: "BaseTypeDefinition") -> "BaseType":
        """
        Set baseType and return self for chaining.

        Args:
            value: The baseType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base_type("value")
        """
        self.base_type = value  # Use property setter (gets validation)
        return self
