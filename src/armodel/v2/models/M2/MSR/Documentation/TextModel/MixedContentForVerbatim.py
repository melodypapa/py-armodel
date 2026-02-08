from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class MixedContentForVerbatim(ARObject, ABC):
    """
    This is the text model for preformatted (verbatim) text. It mainly consists
    of attributes which do not change the length on rendering. This class
    represents multilingual verbatim. Verbatim, sometimes called preformatted
    text, means that white-space is maintained. When verbatim is rendered in PDF
    or Online media, it is rendered using a monospaced font while white-space is
    obeyed. Blanks are rendered as well as newline characters. Even if there are
    inline elements, the length of the data shall not be influenced by
    formatting.

    Package: M2::MSR::Documentation::TextModel::InlineTextModel

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 292, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is MixedContentForVerbatim:
            raise TypeError("MixedContentForVerbatim is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element is the same as function here as in a HTML it forces a line
        # break.
        self._br: "Br" = None

    @property
    def br(self) -> "Br":
        """Get br (Pythonic accessor)."""
        return self._br

    @br.setter
    def br(self, value: "Br") -> None:
        """
        Set br with validation.

        Args:
            value: The br to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Br):
            raise TypeError(
                f"br must be Br, got {type(value).__name__}"
            )
        self._br = value
        # This is emphsized text.
        # Note that in verbatim, the attribute not be considered since verbatim is
                # always monospace font.
        self._e: "EmphasisText" = None

    @property
    def e(self) -> "EmphasisText":
        """Get e (Pythonic accessor)."""
        return self._e

    @e.setter
    def e(self, value: "EmphasisText") -> None:
        """
        Set e with validation.

        Args:
            value: The e to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, EmphasisText):
            raise TypeError(
                f"e must be EmphasisText, got {type(value).__name__}"
            )
        self._e = value
        # This represents a technical term in verbatim.
        # Note that it’s of the user not to take a tt that would add to the text (such
                # as SgmlElement).
        self._tt: "Tt" = None

    @property
    def tt(self) -> "Tt":
        """Get tt (Pythonic accessor)."""
        return self._tt

    @tt.setter
    def tt(self, value: "Tt") -> None:
        """
        Set tt with validation.

        Args:
            value: The tt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Tt):
            raise TypeError(
                f"tt must be Tt, got {type(value).__name__}"
            )
        self._tt = value
        # This is a crossreference within a verbatim text.
        # The disturb the arrangement of the text.
        # It is the author to keep this under control.
        self._xref: "Xref" = None

    @property
    def xref(self) -> "Xref":
        """Get xref (Pythonic accessor)."""
        return self._xref

    @xref.setter
    def xref(self, value: "Xref") -> None:
        """
        Set xref with validation.

        Args:
            value: The xref to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Xref):
            raise TypeError(
                f"xref must be Xref, got {type(value).__name__}"
            )
        self._xref = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBr(self) -> "Br":
        """
        AUTOSAR-compliant getter for br.

        Returns:
            The br value

        Note:
            Delegates to br property (CODING_RULE_V2_00017)
        """
        return self.br  # Delegates to property

    def setBr(self, value: "Br") -> "MixedContentForVerbatim":
        """
        AUTOSAR-compliant setter for br with method chaining.

        Args:
            value: The br to set

        Returns:
            self for method chaining

        Note:
            Delegates to br property setter (gets validation automatically)
        """
        self.br = value  # Delegates to property setter
        return self

    def getE(self) -> "EmphasisText":
        """
        AUTOSAR-compliant getter for e.

        Returns:
            The e value

        Note:
            Delegates to e property (CODING_RULE_V2_00017)
        """
        return self.e  # Delegates to property

    def setE(self, value: "EmphasisText") -> "MixedContentForVerbatim":
        """
        AUTOSAR-compliant setter for e with method chaining.

        Args:
            value: The e to set

        Returns:
            self for method chaining

        Note:
            Delegates to e property setter (gets validation automatically)
        """
        self.e = value  # Delegates to property setter
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

    def setTt(self, value: "Tt") -> "MixedContentForVerbatim":
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

    def getXref(self) -> "Xref":
        """
        AUTOSAR-compliant getter for xref.

        Returns:
            The xref value

        Note:
            Delegates to xref property (CODING_RULE_V2_00017)
        """
        return self.xref  # Delegates to property

    def setXref(self, value: "Xref") -> "MixedContentForVerbatim":
        """
        AUTOSAR-compliant setter for xref with method chaining.

        Args:
            value: The xref to set

        Returns:
            self for method chaining

        Note:
            Delegates to xref property setter (gets validation automatically)
        """
        self.xref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_br(self, value: "Br") -> "MixedContentForVerbatim":
        """
        Set br and return self for chaining.

        Args:
            value: The br to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_br("value")
        """
        self.br = value  # Use property setter (gets validation)
        return self

    def with_e(self, value: "EmphasisText") -> "MixedContentForVerbatim":
        """
        Set e and return self for chaining.

        Args:
            value: The e to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_e("value")
        """
        self.e = value  # Use property setter (gets validation)
        return self

    def with_tt(self, value: "Tt") -> "MixedContentForVerbatim":
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

    def with_xref(self, value: "Xref") -> "MixedContentForVerbatim":
        """
        Set xref and return self for chaining.

        Args:
            value: The xref to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_xref("value")
        """
        self.xref = value  # Use property setter (gets validation)
        return self
