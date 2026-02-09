from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class EmphasisText(ARObject):
    """
    This is an emphasized text. As a compromise it contains some rendering
    oriented attributes such as color and font.

    Package: M2::MSR::Documentation::TextModel::InlineTextElements

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 316, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This allows to recommend a color of the emphasis.
        # It is on 6 digits RGB hex-code.
        self._color: Optional["String"] = None

    @property
    def color(self) -> Optional["String"]:
        """Get color (Pythonic accessor)."""
        return self._color

    @color.setter
    def color(self, value: Optional["String"]) -> None:
        """
        Set color with validation.

        Args:
            value: The color to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._color = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"color must be String or None, got {type(value).__name__}"
            )
        self._color = value
        self._font: Optional["EEnumFont"] = None

    @property
    def font(self) -> Optional["EEnumFont"]:
        """Get font (Pythonic accessor)."""
        return self._font

    @font.setter
    def font(self, value: Optional["EEnumFont"]) -> None:
        """
        Set font with validation.

        Args:
            value: The font to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._font = None
            return

        if not isinstance(value, EEnumFont):
            raise TypeError(
                f"font must be EEnumFont or None, got {type(value).__name__}"
            )
        self._font = value
        self._sub: "Superscript" = None

    @property
    def sub(self) -> "Superscript":
        """Get sub (Pythonic accessor)."""
        return self._sub

    @sub.setter
    def sub(self, value: "Superscript") -> None:
        """
        Set sub with validation.

        Args:
            value: The sub to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sub must be Superscript, got {type(value).__name__}"
            )
        self._sub = value
        self._sup: "Superscript" = None

    @property
    def sup(self) -> "Superscript":
        """Get sup (Pythonic accessor)."""
        return self._sup

    @sup.setter
    def sup(self, value: "Superscript") -> None:
        """
        Set sup with validation.

        Args:
            value: The sup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sup must be Superscript, got {type(value).__name__}"
            )
        self._sup = value
        self._tt: Optional["Tt"] = None

    @property
    def tt(self) -> Optional["Tt"]:
        """Get tt (Pythonic accessor)."""
        return self._tt

    @tt.setter
    def tt(self, value: Optional["Tt"]) -> None:
        """
        Set tt with validation.

        Args:
            value: The tt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tt = None
            return

        if not isinstance(value, Tt):
            raise TypeError(
                f"tt must be Tt or None, got {type(value).__name__}"
            )
        self._tt = value
        # Note that this a proposal which can be overridden or ignored by engines.
        # Default is BOLD.
        self._type: Optional["EEnum"] = None

    @property
    def type(self) -> Optional["EEnum"]:
        """Get type (Pythonic accessor)."""
        return self._type

    @type.setter
    def type(self, value: Optional["EEnum"]) -> None:
        """
        Set type with validation.

        Args:
            value: The type to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._type = None
            return

        if not isinstance(value, EEnum):
            raise TypeError(
                f"type must be EEnum or None, got {type(value).__name__}"
            )
        self._type = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getColor(self) -> "String":
        """
        AUTOSAR-compliant getter for color.

        Returns:
            The color value

        Note:
            Delegates to color property (CODING_RULE_V2_00017)
        """
        return self.color  # Delegates to property

    def setColor(self, value: "String") -> "EmphasisText":
        """
        AUTOSAR-compliant setter for color with method chaining.

        Args:
            value: The color to set

        Returns:
            self for method chaining

        Note:
            Delegates to color property setter (gets validation automatically)
        """
        self.color = value  # Delegates to property setter
        return self

    def getFont(self) -> "EEnumFont":
        """
        AUTOSAR-compliant getter for font.

        Returns:
            The font value

        Note:
            Delegates to font property (CODING_RULE_V2_00017)
        """
        return self.font  # Delegates to property

    def setFont(self, value: "EEnumFont") -> "EmphasisText":
        """
        AUTOSAR-compliant setter for font with method chaining.

        Args:
            value: The font to set

        Returns:
            self for method chaining

        Note:
            Delegates to font property setter (gets validation automatically)
        """
        self.font = value  # Delegates to property setter
        return self

    def getSub(self) -> "Superscript":
        """
        AUTOSAR-compliant getter for sub.

        Returns:
            The sub value

        Note:
            Delegates to sub property (CODING_RULE_V2_00017)
        """
        return self.sub  # Delegates to property

    def setSub(self, value: "Superscript") -> "EmphasisText":
        """
        AUTOSAR-compliant setter for sub with method chaining.

        Args:
            value: The sub to set

        Returns:
            self for method chaining

        Note:
            Delegates to sub property setter (gets validation automatically)
        """
        self.sub = value  # Delegates to property setter
        return self

    def getSup(self) -> "Superscript":
        """
        AUTOSAR-compliant getter for sup.

        Returns:
            The sup value

        Note:
            Delegates to sup property (CODING_RULE_V2_00017)
        """
        return self.sup  # Delegates to property

    def setSup(self, value: "Superscript") -> "EmphasisText":
        """
        AUTOSAR-compliant setter for sup with method chaining.

        Args:
            value: The sup to set

        Returns:
            self for method chaining

        Note:
            Delegates to sup property setter (gets validation automatically)
        """
        self.sup = value  # Delegates to property setter
        return self

    def getTt(self) -> "Tt":
        """
        AUTOSAR-compliant getter for tt.

        Returns:
            The tt value

        Note:
            Delegates to tt property (CODING_RULE_V2_00017)
        """
        return self.tt  # Delegates to property

    def setTt(self, value: "Tt") -> "EmphasisText":
        """
        AUTOSAR-compliant setter for tt with method chaining.

        Args:
            value: The tt to set

        Returns:
            self for method chaining

        Note:
            Delegates to tt property setter (gets validation automatically)
        """
        self.tt = value  # Delegates to property setter
        return self

    def getType(self) -> "EEnum":
        """
        AUTOSAR-compliant getter for type.

        Returns:
            The type value

        Note:
            Delegates to type property (CODING_RULE_V2_00017)
        """
        return self.type  # Delegates to property

    def setType(self, value: "EEnum") -> "EmphasisText":
        """
        AUTOSAR-compliant setter for type with method chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Note:
            Delegates to type property setter (gets validation automatically)
        """
        self.type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_color(self, value: Optional["String"]) -> "EmphasisText":
        """
        Set color and return self for chaining.

        Args:
            value: The color to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_color("value")
        """
        self.color = value  # Use property setter (gets validation)
        return self

    def with_font(self, value: Optional["EEnumFont"]) -> "EmphasisText":
        """
        Set font and return self for chaining.

        Args:
            value: The font to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_font("value")
        """
        self.font = value  # Use property setter (gets validation)
        return self

    def with_sub(self, value: "Superscript") -> "EmphasisText":
        """
        Set sub and return self for chaining.

        Args:
            value: The sub to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub("value")
        """
        self.sub = value  # Use property setter (gets validation)
        return self

    def with_sup(self, value: "Superscript") -> "EmphasisText":
        """
        Set sup and return self for chaining.

        Args:
            value: The sup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sup("value")
        """
        self.sup = value  # Use property setter (gets validation)
        return self

    def with_tt(self, value: Optional["Tt"]) -> "EmphasisText":
        """
        Set tt and return self for chaining.

        Args:
            value: The tt to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tt("value")
        """
        self.tt = value  # Use property setter (gets validation)
        return self

    def with_type(self, value: Optional["EEnum"]) -> "EmphasisText":
        """
        Set type and return self for chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type("value")
        """
        self.type = value  # Use property setter (gets validation)
        return self
