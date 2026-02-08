from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class CompuScale(ARObject):
    """
    This meta-class represents the ability to specify one segment of a segmented
    computation method.

    Package: M2::MSR::AsamHdo::ComputationMethod

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 387, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2011, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 177, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The value of this attribute shall be taken for generating text (specifically
        # the OutVal) within the the enclosing CompuMethod in A2L.
        self._a2lDisplayText: Optional["String"] = None

    @property
    def a2l_display_text(self) -> Optional["String"]:
        """Get a2lDisplayText (Pythonic accessor)."""
        return self._a2lDisplayText

    @a2l_display_text.setter
    def a2l_display_text(self, value: Optional["String"]) -> None:
        """
        Set a2lDisplayText with validation.

        Args:
            value: The a2lDisplayText to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._a2lDisplayText = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"a2lDisplayText must be String or None, got {type(value).__name__}"
            )
        self._a2lDisplayText = value
        # This is the inverse value of the constraint.
        # This supports case that the scale is not reversible per se.
        self._compuInverse: Optional["CompuConst"] = None

    @property
    def compu_inverse(self) -> Optional["CompuConst"]:
        """Get compuInverse (Pythonic accessor)."""
        return self._compuInverse

    @compu_inverse.setter
    def compu_inverse(self, value: Optional["CompuConst"]) -> None:
        """
        Set compuInverse with validation.

        Args:
            value: The compuInverse to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuInverse = None
            return

        if not isinstance(value, CompuConst):
            raise TypeError(
                f"compuInverse must be CompuConst or None, got {type(value).__name__}"
            )
        self._compuInverse = value
        # This represents the computation details of the scale.
        self._compuScale: Optional["CompuScaleContents"] = None

    @property
    def compu_scale(self) -> Optional["CompuScaleContents"]:
        """Get compuScale (Pythonic accessor)."""
        return self._compuScale

    @compu_scale.setter
    def compu_scale(self, value: Optional["CompuScaleContents"]) -> None:
        """
        Set compuScale with validation.

        Args:
            value: The compuScale to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuScale = None
            return

        if not isinstance(value, CompuScaleContents):
            raise TypeError(
                f"compuScale must be CompuScaleContents or None, got {type(value).__name__}"
            )
        self._compuScale = value
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
        # In difference to all the other computational methods every be applied
                # including the bit MASK.
        # is allowed for this type of COMPU-METHOD, overlap.
        # the string reverse to a value, the string has to and the according value for
                # each substring has to up.
        # The sum is finally transmitted.
        # has to be done in order of the.
        self._mask: Optional["PositiveUnlimitedInteger"] = None

    @property
    def mask(self) -> Optional["PositiveUnlimitedInteger"]:
        """Get mask (Pythonic accessor)."""
        return self._mask

    @mask.setter
    def mask(self, value: Optional["PositiveUnlimitedInteger"]) -> None:
        """
        Set mask with validation.

        Args:
            value: The mask to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mask = None
            return

        if not isinstance(value, PositiveUnlimitedInteger):
            raise TypeError(
                f"mask must be PositiveUnlimitedInteger or None, got {type(value).__name__}"
            )
        self._mask = value
        # This element specifies a short name for the particular name can for example
        # be used to derive a identifier.
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
        # The symbol, if provided, is used by code generators to get identifier for the
                # CompuScale.
        # The name will be used for the code generation, therefore it needs to be the
                # generation context.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._symbol: Optional["CIdentifier"] = None

    @property
    def symbol(self) -> Optional["CIdentifier"]:
        """Get symbol (Pythonic accessor)."""
        return self._symbol

    @symbol.setter
    def symbol(self, value: Optional["CIdentifier"]) -> None:
        """
        Set symbol with validation.

        Args:
            value: The symbol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbol = None
            return

        if not isinstance(value, CIdentifier):
            raise TypeError(
                f"symbol must be CIdentifier or None, got {type(value).__name__}"
            )
        self._symbol = value
        # This specifies the upper limit of a of the scale.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getA2lDisplayText(self) -> "String":
        """
        AUTOSAR-compliant getter for a2lDisplayText.

        Returns:
            The a2lDisplayText value

        Note:
            Delegates to a2l_display_text property (CODING_RULE_V2_00017)
        """
        return self.a2l_display_text  # Delegates to property

    def setA2lDisplayText(self, value: "String") -> "CompuScale":
        """
        AUTOSAR-compliant setter for a2lDisplayText with method chaining.

        Args:
            value: The a2lDisplayText to set

        Returns:
            self for method chaining

        Note:
            Delegates to a2l_display_text property setter (gets validation automatically)
        """
        self.a2l_display_text = value  # Delegates to property setter
        return self

    def getCompuInverse(self) -> "CompuConst":
        """
        AUTOSAR-compliant getter for compuInverse.

        Returns:
            The compuInverse value

        Note:
            Delegates to compu_inverse property (CODING_RULE_V2_00017)
        """
        return self.compu_inverse  # Delegates to property

    def setCompuInverse(self, value: "CompuConst") -> "CompuScale":
        """
        AUTOSAR-compliant setter for compuInverse with method chaining.

        Args:
            value: The compuInverse to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_inverse property setter (gets validation automatically)
        """
        self.compu_inverse = value  # Delegates to property setter
        return self

    def getCompuScale(self) -> "CompuScaleContents":
        """
        AUTOSAR-compliant getter for compuScale.

        Returns:
            The compuScale value

        Note:
            Delegates to compu_scale property (CODING_RULE_V2_00017)
        """
        return self.compu_scale  # Delegates to property

    def setCompuScale(self, value: "CompuScaleContents") -> "CompuScale":
        """
        AUTOSAR-compliant setter for compuScale with method chaining.

        Args:
            value: The compuScale to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_scale property setter (gets validation automatically)
        """
        self.compu_scale = value  # Delegates to property setter
        return self

    def getDesc(self) -> "MultiLanguageOverview":
        """
        AUTOSAR-compliant getter for desc.

        Returns:
            The desc value

        Note:
            Delegates to desc property (CODING_RULE_V2_00017)
        """
        return self.desc  # Delegates to property

    def setDesc(self, value: "MultiLanguageOverview") -> "CompuScale":
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

    def setLowerLimit(self, value: "Limit") -> "CompuScale":
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

    def getMask(self) -> "PositiveUnlimitedInteger":
        """
        AUTOSAR-compliant getter for mask.

        Returns:
            The mask value

        Note:
            Delegates to mask property (CODING_RULE_V2_00017)
        """
        return self.mask  # Delegates to property

    def setMask(self, value: "PositiveUnlimitedInteger") -> "CompuScale":
        """
        AUTOSAR-compliant setter for mask with method chaining.

        Args:
            value: The mask to set

        Returns:
            self for method chaining

        Note:
            Delegates to mask property setter (gets validation automatically)
        """
        self.mask = value  # Delegates to property setter
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

    def setShortLabel(self, value: "Identifier") -> "CompuScale":
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

    def getSymbol(self) -> "CIdentifier":
        """
        AUTOSAR-compliant getter for symbol.

        Returns:
            The symbol value

        Note:
            Delegates to symbol property (CODING_RULE_V2_00017)
        """
        return self.symbol  # Delegates to property

    def setSymbol(self, value: "CIdentifier") -> "CompuScale":
        """
        AUTOSAR-compliant setter for symbol with method chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbol property setter (gets validation automatically)
        """
        self.symbol = value  # Delegates to property setter
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

    def setUpperLimit(self, value: "Limit") -> "CompuScale":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_a2l_display_text(self, value: Optional["String"]) -> "CompuScale":
        """
        Set a2lDisplayText and return self for chaining.

        Args:
            value: The a2lDisplayText to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_a2l_display_text("value")
        """
        self.a2l_display_text = value  # Use property setter (gets validation)
        return self

    def with_compu_inverse(self, value: Optional["CompuConst"]) -> "CompuScale":
        """
        Set compuInverse and return self for chaining.

        Args:
            value: The compuInverse to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_inverse("value")
        """
        self.compu_inverse = value  # Use property setter (gets validation)
        return self

    def with_compu_scale(self, value: Optional["CompuScaleContents"]) -> "CompuScale":
        """
        Set compuScale and return self for chaining.

        Args:
            value: The compuScale to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_scale("value")
        """
        self.compu_scale = value  # Use property setter (gets validation)
        return self

    def with_desc(self, value: Optional["MultiLanguageOverview"]) -> "CompuScale":
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

    def with_lower_limit(self, value: Optional["Limit"]) -> "CompuScale":
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

    def with_mask(self, value: Optional["PositiveUnlimitedInteger"]) -> "CompuScale":
        """
        Set mask and return self for chaining.

        Args:
            value: The mask to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mask("value")
        """
        self.mask = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["Identifier"]) -> "CompuScale":
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

    def with_symbol(self, value: Optional["CIdentifier"]) -> "CompuScale":
        """
        Set symbol and return self for chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbol("value")
        """
        self.symbol = value  # Use property setter (gets validation)
        return self

    def with_upper_limit(self, value: Optional["Limit"]) -> "CompuScale":
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
