from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class MultiLanguagePlainText(ARObject):
    """
    This is a multilingual plaint Text.It is intended to be rendered as a
    paragraph.

    Package: M2::MSR::Documentation::TextModel::MultilanguageData::MultiLanguagePlainText

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 349, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._l10: "LPlainText" = None

    @property
    def l10(self) -> "LPlainText":
        """Get l10 (Pythonic accessor)."""
        return self._l10

    @l10.setter
    def l10(self, value: "LPlainText") -> None:
        """
        Set l10 with validation.

        Args:
            value: The l10 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, LPlainText):
            raise TypeError(
                f"l10 must be LPlainText, got {type(value).__name__}"
            )
        self._l10 = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getL10(self) -> "LPlainText":
        """
        AUTOSAR-compliant getter for l10.

        Returns:
            The l10 value

        Note:
            Delegates to l10 property (CODING_RULE_V2_00017)
        """
        return self.l10  # Delegates to property

    def setL10(self, value: "LPlainText") -> "MultiLanguagePlainText":
        """
        AUTOSAR-compliant setter for l10 with method chaining.

        Args:
            value: The l10 to set

        Returns:
            self for method chaining

        Note:
            Delegates to l10 property setter (gets validation automatically)
        """
        self.l10 = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_l10(self, value: "LPlainText") -> "MultiLanguagePlainText":
        """
        Set l10 and return self for chaining.

        Args:
            value: The l10 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_l10("value")
        """
        self.l10 = value  # Use property setter (gets validation)
        return self
