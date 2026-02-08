from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class ScaleConstr(ARObject):
    """
    This meta-class represents the ability to specify constraints as a list of
    intervals (called scales).

    Package: M2::MSR::AsamHdo::Constraints::GlobalConstraints::ScaleConstr

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1003, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # <desc> represents a general but brief description of the in question.
        self._desc: Optional["MultiLanguageOverview"] = None

    @property
    def desc(self) -> Optional["MultiLanguageOverview"]:
        """Get desc (Pythonic accessor)."""
        return self._desc

    @desc.setter
    def desc(self, value: Optional["MultiLanguageOverview"]) -> None:
        """
        Set desc with validation.

        Args:
            value: The desc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._desc = None
            return

        if not isinstance(value, MultiLanguageOverview):
            raise TypeError(
                f"desc must be MultiLanguageOverview or None, got {type(value).__name__}"
            )
        self._desc = value
        # This specifies the lower limit of the scale.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._lowerLimit: Optional["Limit"] = None

    @property
    def lower_limit(self) -> Optional["Limit"]:
        """Get lowerLimit (Pythonic accessor)."""
        return self._lowerLimit

    @lower_limit.setter
    def lower_limit(self, value: Optional["Limit"]) -> None:
        """
        Set lowerLimit with validation.

        Args:
            value: The lowerLimit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lowerLimit = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"lowerLimit must be Limit or None, got {type(value).__name__}"
            )
        self._lowerLimit = value
        # This element specifies a short name for the scaleConstr.
        # for example be used to create more specific a constraint checker.
        # The constraints cannot in the meta-model, therefore shortLabel is substitute
                # for shortName.
        self._shortLabel: Optional["Identifier"] = None

    @property
    def short_label(self) -> Optional["Identifier"]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional["Identifier"]) -> None:
        """
        Set shortLabel with validation.

        Args:
            value: The shortLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortLabel = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"shortLabel must be Identifier or None, got {type(value).__name__}"
            )
        self._shortLabel = value
        # This specifies the upper limit of a the scale.
        self._upperLimit: Optional["Limit"] = None

    @property
    def upper_limit(self) -> Optional["Limit"]:
        """Get upperLimit (Pythonic accessor)."""
        return self._upperLimit

    @upper_limit.setter
    def upper_limit(self, value: Optional["Limit"]) -> None:
        """
        Set upperLimit with validation.

        Args:
            value: The upperLimit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upperLimit = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"upperLimit must be Limit or None, got {type(value).__name__}"
            )
        self._upperLimit = value
        # Specifies if the values defined by the scales are to be valid.
        # If the attribute is missing then the is "VALID".
        self._validity: Optional["ScaleConstrValidity"] = None

    @property
    def validity(self) -> Optional["ScaleConstrValidity"]:
        """Get validity (Pythonic accessor)."""
        return self._validity

    @validity.setter
    def validity(self, value: Optional["ScaleConstrValidity"]) -> None:
        """
        Set validity with validation.

        Args:
            value: The validity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._validity = None
            return

        if not isinstance(value, ScaleConstrValidity):
            raise TypeError(
                f"validity must be ScaleConstrValidity or None, got {type(value).__name__}"
            )
        self._validity = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDesc(self) -> "MultiLanguageOverview":
        """
        AUTOSAR-compliant getter for desc.

        Returns:
            The desc value

        Note:
            Delegates to desc property (CODING_RULE_V2_00017)
        """
        return self.desc  # Delegates to property

    def setDesc(self, value: "MultiLanguageOverview") -> "ScaleConstr":
        """
        AUTOSAR-compliant setter for desc with method chaining.

        Args:
            value: The desc to set

        Returns:
            self for method chaining

        Note:
            Delegates to desc property setter (gets validation automatically)
        """
        self.desc = value  # Delegates to property setter
        return self

    def getLowerLimit(self) -> "Limit":
        """
        AUTOSAR-compliant getter for lowerLimit.

        Returns:
            The lowerLimit value

        Note:
            Delegates to lower_limit property (CODING_RULE_V2_00017)
        """
        return self.lower_limit  # Delegates to property

    def setLowerLimit(self, value: "Limit") -> "ScaleConstr":
        """
        AUTOSAR-compliant setter for lowerLimit with method chaining.

        Args:
            value: The lowerLimit to set

        Returns:
            self for method chaining

        Note:
            Delegates to lower_limit property setter (gets validation automatically)
        """
        self.lower_limit = value  # Delegates to property setter
        return self

    def getShortLabel(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "Identifier") -> "ScaleConstr":
        """
        AUTOSAR-compliant setter for shortLabel with method chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to short_label property setter (gets validation automatically)
        """
        self.short_label = value  # Delegates to property setter
        return self

    def getUpperLimit(self) -> "Limit":
        """
        AUTOSAR-compliant getter for upperLimit.

        Returns:
            The upperLimit value

        Note:
            Delegates to upper_limit property (CODING_RULE_V2_00017)
        """
        return self.upper_limit  # Delegates to property

    def setUpperLimit(self, value: "Limit") -> "ScaleConstr":
        """
        AUTOSAR-compliant setter for upperLimit with method chaining.

        Args:
            value: The upperLimit to set

        Returns:
            self for method chaining

        Note:
            Delegates to upper_limit property setter (gets validation automatically)
        """
        self.upper_limit = value  # Delegates to property setter
        return self

    def getValidity(self) -> "ScaleConstrValidity":
        """
        AUTOSAR-compliant getter for validity.

        Returns:
            The validity value

        Note:
            Delegates to validity property (CODING_RULE_V2_00017)
        """
        return self.validity  # Delegates to property

    def setValidity(self, value: "ScaleConstrValidity") -> "ScaleConstr":
        """
        AUTOSAR-compliant setter for validity with method chaining.

        Args:
            value: The validity to set

        Returns:
            self for method chaining

        Note:
            Delegates to validity property setter (gets validation automatically)
        """
        self.validity = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_desc(self, value: Optional["MultiLanguageOverview"]) -> "ScaleConstr":
        """
        Set desc and return self for chaining.

        Args:
            value: The desc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_desc("value")
        """
        self.desc = value  # Use property setter (gets validation)
        return self

    def with_lower_limit(self, value: Optional["Limit"]) -> "ScaleConstr":
        """
        Set lowerLimit and return self for chaining.

        Args:
            value: The lowerLimit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lower_limit("value")
        """
        self.lower_limit = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["Identifier"]) -> "ScaleConstr":
        """
        Set shortLabel and return self for chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_label("value")
        """
        self.short_label = value  # Use property setter (gets validation)
        return self

    def with_upper_limit(self, value: Optional["Limit"]) -> "ScaleConstr":
        """
        Set upperLimit and return self for chaining.

        Args:
            value: The upperLimit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_upper_limit("value")
        """
        self.upper_limit = value  # Use property setter (gets validation)
        return self

    def with_validity(self, value: Optional["ScaleConstrValidity"]) -> "ScaleConstr":
        """
        Set validity and return self for chaining.

        Args:
            value: The validity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_validity("value")
        """
        self.validity = value  # Use property setter (gets validation)
        return self
