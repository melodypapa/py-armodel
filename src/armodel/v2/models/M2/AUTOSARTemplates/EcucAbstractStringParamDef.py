from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class EcucAbstractStringParamDef(ARObject, ABC):
    """
    Abstract class that is used to collect the common properties for
    StringParamDefs, LinkerSymbolDef, FunctionNameDef and
    MultilineStringParamDefs. atpVariation: [RS_ECUC_00083] Tags:
    vh.latestBindingTime=codeGenerationTime

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 63, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 183, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is EcucAbstractStringParamDef:
            raise TypeError("EcucAbstractStringParamDef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Default value of the string configuration parameter.
        self._defaultValue: Optional["VerbatimString"] = None

    @property
    def default_value(self) -> Optional["VerbatimString"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional["VerbatimString"]) -> None:
        """
        Set defaultValue with validation.

        Args:
            value: The defaultValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultValue = None
            return

        if not isinstance(value, VerbatimString):
            raise TypeError(
                f"defaultValue must be VerbatimString or None, got {type(value).__name__}"
            )
        self._defaultValue = value
        self._maxLength: Optional["PositiveInteger"] = None

    @property
    def max_length(self) -> Optional["PositiveInteger"]:
        """Get maxLength (Pythonic accessor)."""
        return self._maxLength

    @max_length.setter
    def max_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxLength with validation.

        Args:
            value: The maxLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxLength = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxLength must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxLength = value
        self._minLength: Optional["PositiveInteger"] = None

    @property
    def min_length(self) -> Optional["PositiveInteger"]:
        """Get minLength (Pythonic accessor)."""
        return self._minLength

    @min_length.setter
    def min_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minLength with validation.

        Args:
            value: The minLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minLength = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minLength must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minLength = value
        # parameter value.
        self._regular: Optional["RegularExpression"] = None

    @property
    def regular(self) -> Optional["RegularExpression"]:
        """Get regular (Pythonic accessor)."""
        return self._regular

    @regular.setter
    def regular(self, value: Optional["RegularExpression"]) -> None:
        """
        Set regular with validation.

        Args:
            value: The regular to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._regular = None
            return

        if not isinstance(value, RegularExpression):
            raise TypeError(
                f"regular must be RegularExpression or None, got {type(value).__name__}"
            )
        self._regular = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> "VerbatimString":
        """
        AUTOSAR-compliant getter for defaultValue.

        Returns:
            The defaultValue value

        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: "VerbatimString") -> "EcucAbstractStringParamDef":
        """
        AUTOSAR-compliant setter for defaultValue with method chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_value property setter (gets validation automatically)
        """
        self.default_value = value  # Delegates to property setter
        return self

    def getMaxLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxLength.

        Returns:
            The maxLength value

        Note:
            Delegates to max_length property (CODING_RULE_V2_00017)
        """
        return self.max_length  # Delegates to property

    def setMaxLength(self, value: "PositiveInteger") -> "EcucAbstractStringParamDef":
        """
        AUTOSAR-compliant setter for maxLength with method chaining.

        Args:
            value: The maxLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_length property setter (gets validation automatically)
        """
        self.max_length = value  # Delegates to property setter
        return self

    def getMinLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minLength.

        Returns:
            The minLength value

        Note:
            Delegates to min_length property (CODING_RULE_V2_00017)
        """
        return self.min_length  # Delegates to property

    def setMinLength(self, value: "PositiveInteger") -> "EcucAbstractStringParamDef":
        """
        AUTOSAR-compliant setter for minLength with method chaining.

        Args:
            value: The minLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_length property setter (gets validation automatically)
        """
        self.min_length = value  # Delegates to property setter
        return self

    def getRegular(self) -> "RegularExpression":
        """
        AUTOSAR-compliant getter for regular.

        Returns:
            The regular value

        Note:
            Delegates to regular property (CODING_RULE_V2_00017)
        """
        return self.regular  # Delegates to property

    def setRegular(self, value: "RegularExpression") -> "EcucAbstractStringParamDef":
        """
        AUTOSAR-compliant setter for regular with method chaining.

        Args:
            value: The regular to set

        Returns:
            self for method chaining

        Note:
            Delegates to regular property setter (gets validation automatically)
        """
        self.regular = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_value(self, value: Optional["VerbatimString"]) -> "EcucAbstractStringParamDef":
        """
        Set defaultValue and return self for chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_value("value")
        """
        self.default_value = value  # Use property setter (gets validation)
        return self

    def with_max_length(self, value: Optional["PositiveInteger"]) -> "EcucAbstractStringParamDef":
        """
        Set maxLength and return self for chaining.

        Args:
            value: The maxLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_length("value")
        """
        self.max_length = value  # Use property setter (gets validation)
        return self

    def with_min_length(self, value: Optional["PositiveInteger"]) -> "EcucAbstractStringParamDef":
        """
        Set minLength and return self for chaining.

        Args:
            value: The minLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_length("value")
        """
        self.min_length = value  # Use property setter (gets validation)
        return self

    def with_regular(self, value: Optional["RegularExpression"]) -> "EcucAbstractStringParamDef":
        """
        Set regular and return self for chaining.

        Args:
            value: The regular to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_regular("value")
        """
        self.regular = value  # Use property setter (gets validation)
        return self
