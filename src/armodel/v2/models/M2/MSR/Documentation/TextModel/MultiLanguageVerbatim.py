from typing import Optional

from armodel.v2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    Paginateable,
)


class MultiLanguageVerbatim(Paginateable):
    """
    This class represents multilingual Verbatim. Verbatim means, that
    white-space is maintained. When Verbatim is rendered in PDF or Online media,
    white-space is obeyed. Blanks are rendered as well as newline characters.

    Package: M2::MSR::Documentation::TextModel::MultilanguageData

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 291, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This indicates if the verbatim text might be split on Default is "1".
        self._allowBreak: Optional["NameToken"] = None

    @property
    def allow_break(self) -> Optional["NameToken"]:
        """Get allowBreak (Pythonic accessor)."""
        return self._allowBreak

    @allow_break.setter
    def allow_break(self, value: Optional["NameToken"]) -> None:
        """
        Set allowBreak with validation.

        Args:
            value: The allowBreak to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._allowBreak = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"allowBreak must be NameToken or None, got {type(value).__name__}"
            )
        self._allowBreak = value
        # The are allowed:.
        self._float: Optional["FloatEnum"] = None

    @property
    def float(self) -> Optional["FloatEnum"]:
        """Get float (Pythonic accessor)."""
        return self._float

    @float.setter
    def float(self, value: Optional["FloatEnum"]) -> None:
        """
        Set float with validation.

        Args:
            value: The float to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._float = None
            return

        if not isinstance(value, FloatEnum):
            raise TypeError(
                f"float must be FloatEnum or None, got {type(value).__name__}"
            )
        self._float = value
                # class.
        # The syntax shall be the applied help system respectively help.
        self._helpEntry: Optional["String"] = None

    @property
    def help_entry(self) -> Optional["String"]:
        """Get helpEntry (Pythonic accessor)."""
        return self._helpEntry

    @help_entry.setter
    def help_entry(self, value: Optional["String"]) -> None:
        """
        Set helpEntry with validation.

        Args:
            value: The helpEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._helpEntry = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"helpEntry must be String or None, got {type(value).__name__}"
            )
        self._helpEntry = value

    @property
    def l5(self) -> "LVerbatim":
        """Get l5 (Pythonic accessor)."""
        return self._l5

    @l5.setter
    def l5(self, value: "LVerbatim") -> None:
        """
        Set l5 with validation.

        Args:
            value: The l5 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, LVerbatim):
            raise TypeError(
                f"l5 must be LVerbatim, got {type(value).__name__}"
            )
        self._l5 = value
        # Used to indicate wether the figure should take the width (value = "pgwide")
        # or not (value =.
        self._pgwide: Optional["PgwideEnum"] = None

    @property
    def pgwide(self) -> Optional["PgwideEnum"]:
        """Get pgwide (Pythonic accessor)."""
        return self._pgwide

    @pgwide.setter
    def pgwide(self, value: Optional["PgwideEnum"]) -> None:
        """
        Set pgwide with validation.

        Args:
            value: The pgwide to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pgwide = None
            return

        if not isinstance(value, PgwideEnum):
            raise TypeError(
                f"pgwide must be PgwideEnum or None, got {type(value).__name__}"
            )
        self._pgwide = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAllowBreak(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for allowBreak.

        Returns:
            The allowBreak value

        Note:
            Delegates to allow_break property (CODING_RULE_V2_00017)
        """
        return self.allow_break  # Delegates to property

    def setAllowBreak(self, value: "NameToken") -> "MultiLanguageVerbatim":
        """
        AUTOSAR-compliant setter for allowBreak with method chaining.

        Args:
            value: The allowBreak to set

        Returns:
            self for method chaining

        Note:
            Delegates to allow_break property setter (gets validation automatically)
        """
        self.allow_break = value  # Delegates to property setter
        return self

    def getFloat(self) -> "FloatEnum":
        """
        AUTOSAR-compliant getter for float.

        Returns:
            The float value

        Note:
            Delegates to float property (CODING_RULE_V2_00017)
        """
        return self.float  # Delegates to property

    def setFloat(self, value: "FloatEnum") -> "MultiLanguageVerbatim":
        """
        AUTOSAR-compliant setter for float with method chaining.

        Args:
            value: The float to set

        Returns:
            self for method chaining

        Note:
            Delegates to float property setter (gets validation automatically)
        """
        self.float = value  # Delegates to property setter
        return self

    def getHelpEntry(self) -> "String":
        """
        AUTOSAR-compliant getter for helpEntry.

        Returns:
            The helpEntry value

        Note:
            Delegates to help_entry property (CODING_RULE_V2_00017)
        """
        return self.help_entry  # Delegates to property

    def setHelpEntry(self, value: "String") -> "MultiLanguageVerbatim":
        """
        AUTOSAR-compliant setter for helpEntry with method chaining.

        Args:
            value: The helpEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to help_entry property setter (gets validation automatically)
        """
        self.help_entry = value  # Delegates to property setter
        return self

    def getL5(self) -> "LVerbatim":
        """
        AUTOSAR-compliant getter for l5.

        Returns:
            The l5 value

        Note:
            Delegates to l5 property (CODING_RULE_V2_00017)
        """
        return self.l5  # Delegates to property

    def setL5(self, value: "LVerbatim") -> "MultiLanguageVerbatim":
        """
        AUTOSAR-compliant setter for l5 with method chaining.

        Args:
            value: The l5 to set

        Returns:
            self for method chaining

        Note:
            Delegates to l5 property setter (gets validation automatically)
        """
        self.l5 = value  # Delegates to property setter
        return self

    def getPgwide(self) -> "PgwideEnum":
        """
        AUTOSAR-compliant getter for pgwide.

        Returns:
            The pgwide value

        Note:
            Delegates to pgwide property (CODING_RULE_V2_00017)
        """
        return self.pgwide  # Delegates to property

    def setPgwide(self, value: "PgwideEnum") -> "MultiLanguageVerbatim":
        """
        AUTOSAR-compliant setter for pgwide with method chaining.

        Args:
            value: The pgwide to set

        Returns:
            self for method chaining

        Note:
            Delegates to pgwide property setter (gets validation automatically)
        """
        self.pgwide = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_allow_break(self, value: Optional["NameToken"]) -> "MultiLanguageVerbatim":
        """
        Set allowBreak and return self for chaining.

        Args:
            value: The allowBreak to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_allow_break("value")
        """
        self.allow_break = value  # Use property setter (gets validation)
        return self

    def with_float(self, value: Optional["FloatEnum"]) -> "MultiLanguageVerbatim":
        """
        Set float and return self for chaining.

        Args:
            value: The float to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_float("value")
        """
        self.float = value  # Use property setter (gets validation)
        return self

    def with_help_entry(self, value: Optional["String"]) -> "MultiLanguageVerbatim":
        """
        Set helpEntry and return self for chaining.

        Args:
            value: The helpEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_help_entry("value")
        """
        self.help_entry = value  # Use property setter (gets validation)
        return self

    def with_l5(self, value: "LVerbatim") -> "MultiLanguageVerbatim":
        """
        Set l5 and return self for chaining.

        Args:
            value: The l5 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_l5("value")
        """
        self.l5 = value  # Use property setter (gets validation)
        return self

    def with_pgwide(self, value: Optional["PgwideEnum"]) -> "MultiLanguageVerbatim":
        """
        Set pgwide and return self for chaining.

        Args:
            value: The pgwide to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pgwide("value")
        """
        self.pgwide = value  # Use property setter (gets validation)
        return self
