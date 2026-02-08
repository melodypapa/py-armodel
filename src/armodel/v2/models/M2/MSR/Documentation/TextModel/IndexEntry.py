from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class IndexEntry(ARObject):
    """
    This class represents an index entry.

    Package: M2::MSR::Documentation::TextModel::InlineTextElements::IndexEntry

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 317, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is subscript text.
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
        # This is superscript text.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSub(self) -> "Superscript":
        """
        AUTOSAR-compliant getter for sub.

        Returns:
            The sub value

        Note:
            Delegates to sub property (CODING_RULE_V2_00017)
        """
        return self.sub  # Delegates to property

    def setSub(self, value: "Superscript") -> "IndexEntry":
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

    def setSup(self, value: "Superscript") -> "IndexEntry":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sub(self, value: "Superscript") -> "IndexEntry":
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

    def with_sup(self, value: "Superscript") -> "IndexEntry":
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
