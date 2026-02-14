"""
AUTOSAR Package - Formula

Package: M2::MSR::Documentation::BlockElements::Formula
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    Paginateable,
)


class MlFormula(Paginateable):
    """
    This meta-class represents the ability to express a formula in a
    documentation. The formula can be expressed by various means. If more than
    one representation is available, they need to be consistent. The rendering
    system can use the representation which is most appropriate.

    Package: M2::MSR::Documentation::BlockElements::Formula::MlFormula

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 301, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 309, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element specifies the identification or heading of a.
        self._formulaCaption: Optional["Caption"] = None

    @property
    def formula_caption(self) -> Optional["Caption"]:
        """Get formulaCaption (Pythonic accessor)."""
        return self._formulaCaption

    @formula_caption.setter
    def formula_caption(self, value: Optional["Caption"]) -> None:
        """
        Set formulaCaption with validation.

        Args:
            value: The formulaCaption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._formulaCaption = None
            return

        if not isinstance(value, Caption):
            raise TypeError(
                f"formulaCaption must be Caption or None, got {type(value).__name__}"
            )
        self._formulaCaption = value
        # math-processor.
        self._genericMath: Optional["MultiLanguagePlainText"] = None

    @property
    def generic_math(self) -> Optional["MultiLanguagePlainText"]:
        """Get genericMath (Pythonic accessor)."""
        return self._genericMath

    @generic_math.setter
    def generic_math(self, value: Optional["MultiLanguagePlainText"]) -> None:
        """
        Set genericMath with validation.

        Args:
            value: The genericMath to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._genericMath = None
            return

        if not isinstance(value, MultiLanguagePlainText):
            raise TypeError(
                f"genericMath must be MultiLanguagePlainText or None, got {type(value).__name__}"
            )
        self._genericMath = value
        self._lGraphic: List["LGraphic"] = []

    @property
    def l_graphic(self) -> List["LGraphic"]:
        """Get lGraphic (Pythonic accessor)."""
        return self._lGraphic
        # this is the TeX representation of TeX formula.
        # A TeX be processed by a TeX or a LaTeX processor.
        self._texMath: Optional["MultiLanguagePlainText"] = None

    @property
    def tex_math(self) -> Optional["MultiLanguagePlainText"]:
        """Get texMath (Pythonic accessor)."""
        return self._texMath

    @tex_math.setter
    def tex_math(self, value: Optional["MultiLanguagePlainText"]) -> None:
        """
        Set texMath with validation.

        Args:
            value: The texMath to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._texMath = None
            return

        if not isinstance(value, MultiLanguagePlainText):
            raise TypeError(
                f"texMath must be MultiLanguagePlainText or None, got {type(value).__name__}"
            )
        self._texMath = value
        # be used to denote the formula in a kind of pseudo whatever appears
                # approprate.
        self._verbatim: Optional["MultiLanguageVerbatim"] = None

    @property
    def verbatim(self) -> Optional["MultiLanguageVerbatim"]:
        """Get verbatim (Pythonic accessor)."""
        return self._verbatim

    @verbatim.setter
    def verbatim(self, value: Optional["MultiLanguageVerbatim"]) -> None:
        """
        Set verbatim with validation.

        Args:
            value: The verbatim to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._verbatim = None
            return

        if not isinstance(value, MultiLanguageVerbatim):
            raise TypeError(
                f"verbatim must be MultiLanguageVerbatim or None, got {type(value).__name__}"
            )
        self._verbatim = value

    def with_l_graphic(self, value):
        """
        Set l_graphic and return self for chaining.

        Args:
            value: The l_graphic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_l_graphic("value")
        """
        self.l_graphic = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFormulaCaption(self) -> "Caption":
        """
        AUTOSAR-compliant getter for formulaCaption.

        Returns:
            The formulaCaption value

        Note:
            Delegates to formula_caption property (CODING_RULE_V2_00017)
        """
        return self.formula_caption  # Delegates to property

    def setFormulaCaption(self, value: "Caption") -> MlFormula:
        """
        AUTOSAR-compliant setter for formulaCaption with method chaining.

        Args:
            value: The formulaCaption to set

        Returns:
            self for method chaining

        Note:
            Delegates to formula_caption property setter (gets validation automatically)
        """
        self.formula_caption = value  # Delegates to property setter
        return self

    def getGenericMath(self) -> "MultiLanguagePlainText":
        """
        AUTOSAR-compliant getter for genericMath.

        Returns:
            The genericMath value

        Note:
            Delegates to generic_math property (CODING_RULE_V2_00017)
        """
        return self.generic_math  # Delegates to property

    def setGenericMath(self, value: "MultiLanguagePlainText") -> MlFormula:
        """
        AUTOSAR-compliant setter for genericMath with method chaining.

        Args:
            value: The genericMath to set

        Returns:
            self for method chaining

        Note:
            Delegates to generic_math property setter (gets validation automatically)
        """
        self.generic_math = value  # Delegates to property setter
        return self

    def getLGraphic(self) -> List["LGraphic"]:
        """
        AUTOSAR-compliant getter for lGraphic.

        Returns:
            The lGraphic value

        Note:
            Delegates to l_graphic property (CODING_RULE_V2_00017)
        """
        return self.l_graphic  # Delegates to property

    def getTexMath(self) -> "MultiLanguagePlainText":
        """
        AUTOSAR-compliant getter for texMath.

        Returns:
            The texMath value

        Note:
            Delegates to tex_math property (CODING_RULE_V2_00017)
        """
        return self.tex_math  # Delegates to property

    def setTexMath(self, value: "MultiLanguagePlainText") -> MlFormula:
        """
        AUTOSAR-compliant setter for texMath with method chaining.

        Args:
            value: The texMath to set

        Returns:
            self for method chaining

        Note:
            Delegates to tex_math property setter (gets validation automatically)
        """
        self.tex_math = value  # Delegates to property setter
        return self

    def getVerbatim(self) -> "MultiLanguageVerbatim":
        """
        AUTOSAR-compliant getter for verbatim.

        Returns:
            The verbatim value

        Note:
            Delegates to verbatim property (CODING_RULE_V2_00017)
        """
        return self.verbatim  # Delegates to property

    def setVerbatim(self, value: "MultiLanguageVerbatim") -> MlFormula:
        """
        AUTOSAR-compliant setter for verbatim with method chaining.

        Args:
            value: The verbatim to set

        Returns:
            self for method chaining

        Note:
            Delegates to verbatim property setter (gets validation automatically)
        """
        self.verbatim = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_formula_caption(self, value: Optional["Caption"]) -> MlFormula:
        """
        Set formulaCaption and return self for chaining.

        Args:
            value: The formulaCaption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_formula_caption("value")
        """
        self.formula_caption = value  # Use property setter (gets validation)
        return self

    def with_generic_math(self, value: Optional["MultiLanguagePlainText"]) -> MlFormula:
        """
        Set genericMath and return self for chaining.

        Args:
            value: The genericMath to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_generic_math("value")
        """
        self.generic_math = value  # Use property setter (gets validation)
        return self

    def with_tex_math(self, value: Optional["MultiLanguagePlainText"]) -> MlFormula:
        """
        Set texMath and return self for chaining.

        Args:
            value: The texMath to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tex_math("value")
        """
        self.tex_math = value  # Use property setter (gets validation)
        return self

    def with_verbatim(self, value: Optional["MultiLanguageVerbatim"]) -> MlFormula:
        """
        Set verbatim and return self for chaining.

        Args:
            value: The verbatim to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_verbatim("value")
        """
        self.verbatim = value  # Use property setter (gets validation)
        return self
