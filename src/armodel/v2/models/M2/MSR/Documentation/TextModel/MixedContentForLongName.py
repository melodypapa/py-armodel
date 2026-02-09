from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class MixedContentForLongName(ARObject, ABC):
    """
    This is the model for titles and long-names. It allows some emphasis and
    index entries but no reference target (which is provided by the identifiable
    in question). It is intended that the content model can also be rendered as
    plain text. The abstract class can be used for single language as well as
    for multi language elements.

    Package: M2::MSR::Documentation::TextModel::InlineTextModel

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 62, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is MixedContentForLongName:
            raise TypeError("MixedContentForLongName is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is emphasized text.
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
        self._ie: "IndexEntry" = None

    @property
    def ie(self) -> "IndexEntry":
        """Get ie (Pythonic accessor)."""
        return self._ie

    @ie.setter
    def ie(self, value: "IndexEntry") -> None:
        """
        Set ie with validation.

        Args:
            value: The ie to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, IndexEntry):
            raise TypeError(
                f"ie must be IndexEntry, got {type(value).__name__}"
            )
        self._ie = value
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getE(self) -> "EmphasisText":
        """
        AUTOSAR-compliant getter for e.

        Returns:
            The e value

        Note:
            Delegates to e property (CODING_RULE_V2_00017)
        """
        return self.e  # Delegates to property

    def setE(self, value: "EmphasisText") -> "MixedContentForLongName":
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

    def getIe(self) -> "IndexEntry":
        """
        AUTOSAR-compliant getter for ie.

        Returns:
            The ie value

        Note:
            Delegates to ie property (CODING_RULE_V2_00017)
        """
        return self.ie  # Delegates to property

    def setIe(self, value: "IndexEntry") -> "MixedContentForLongName":
        """
        AUTOSAR-compliant setter for ie with method chaining.

        Args:
            value: The ie to set

        Returns:
            self for method chaining

        Note:
            Delegates to ie property setter (gets validation automatically)
        """
        self.ie = value  # Delegates to property setter
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

    def setSub(self, value: "Superscript") -> "MixedContentForLongName":
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

    def setSup(self, value: "Superscript") -> "MixedContentForLongName":
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

    def setTt(self, value: "Tt") -> "MixedContentForLongName":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_e(self, value: "EmphasisText") -> "MixedContentForLongName":
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

    def with_ie(self, value: "IndexEntry") -> "MixedContentForLongName":
        """
        Set ie and return self for chaining.

        Args:
            value: The ie to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ie("value")
        """
        self.ie = value  # Use property setter (gets validation)
        return self

    def with_sub(self, value: "Superscript") -> "MixedContentForLongName":
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

    def with_sup(self, value: "Superscript") -> "MixedContentForLongName":
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

    def with_tt(self, value: "Tt") -> "MixedContentForLongName":
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
