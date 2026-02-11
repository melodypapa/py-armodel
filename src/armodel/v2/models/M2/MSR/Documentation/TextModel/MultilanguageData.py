"""
AUTOSAR Package - MultilanguageData

Package: M2::MSR::Documentation::TextModel::MultilanguageData
"""


from __future__ import annotations
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    Paginateable,
)


class MultiLanguageOverviewParagraph(ARObject):
    """
    This is the content of a multilingual paragraph in an overview item.

    Package: M2::MSR::Documentation::TextModel::MultilanguageData::MultiLanguageOverviewParagraph

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 53, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 389, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 347, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 65, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._l2: "LOverviewParagraph" = None

    @property
    def l2(self) -> "LOverviewParagraph":
        """Get l2 (Pythonic accessor)."""
        return self._l2

    @l2.setter
    def l2(self, value: "LOverviewParagraph") -> None:
        """
        Set l2 with validation.

        Args:
            value: The l2 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, LOverviewParagraph):
            raise TypeError(
                f"l2 must be LOverviewParagraph, got {type(value).__name__}"
            )
        self._l2 = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getL2(self) -> "LOverviewParagraph":
        """
        AUTOSAR-compliant getter for l2.

        Returns:
            The l2 value

        Note:
            Delegates to l2 property (CODING_RULE_V2_00017)
        """
        return self.l2  # Delegates to property

    def setL2(self, value: "LOverviewParagraph") -> MultiLanguageOverviewParagraph:
        """
        AUTOSAR-compliant setter for l2 with method chaining.

        Args:
            value: The l2 to set

        Returns:
            self for method chaining

        Note:
            Delegates to l2 property setter (gets validation automatically)
        """
        self.l2 = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_l2(self, value: "LOverviewParagraph") -> MultiLanguageOverviewParagraph:
        """
        Set l2 and return self for chaining.

        Args:
            value: The l2 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_l2("value")
        """
        self.l2 = value  # Use property setter (gets validation)
        return self



class MultilanguageLongName(ARObject):
    """
    This meta-class represents the ability to specify a long name which acts in
    the role of a headline. It is intended for human readers. Per language it
    should be around max 80 characters.

    Package: M2::MSR::Documentation::TextModel::MultilanguageData::MultilanguageLongName

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 179, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 163, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 62, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._l4: "LLongName" = None

    @property
    def l4(self) -> "LLongName":
        """Get l4 (Pythonic accessor)."""
        return self._l4

    @l4.setter
    def l4(self, value: "LLongName") -> None:
        """
        Set l4 with validation.

        Args:
            value: The l4 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, LLongName):
            raise TypeError(
                f"l4 must be LLongName, got {type(value).__name__}"
            )
        self._l4 = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getL4(self) -> "LLongName":
        """
        AUTOSAR-compliant getter for l4.

        Returns:
            The l4 value

        Note:
            Delegates to l4 property (CODING_RULE_V2_00017)
        """
        return self.l4  # Delegates to property

    def setL4(self, value: "LLongName") -> MultilanguageLongName:
        """
        AUTOSAR-compliant setter for l4 with method chaining.

        Args:
            value: The l4 to set

        Returns:
            self for method chaining

        Note:
            Delegates to l4 property setter (gets validation automatically)
        """
        self.l4 = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_l4(self, value: "LLongName") -> MultilanguageLongName:
        """
        Set l4 and return self for chaining.

        Args:
            value: The l4 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_l4("value")
        """
        self.l4 = value  # Use property setter (gets validation)
        return self



class MultiLanguageParagraph(Paginateable):
    """
    This is the content model of a multilingual paragraph in a documentation.

    Package: M2::MSR::Documentation::TextModel::MultilanguageData::MultiLanguageParagraph

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 290, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies an entry point in an online help system to with the parent
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"helpEntry must be String or str or None, got {type(value).__name__}"
            )
        self._helpEntry = value

    @property
    def l1(self) -> "LParagraph":
        """Get l1 (Pythonic accessor)."""
        return self._l1

    @l1.setter
    def l1(self, value: "LParagraph") -> None:
        """
        Set l1 with validation.

        Args:
            value: The l1 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, LParagraph):
            raise TypeError(
                f"l1 must be LParagraph, got {type(value).__name__}"
            )
        self._l1 = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHelpEntry(self) -> "String":
        """
        AUTOSAR-compliant getter for helpEntry.

        Returns:
            The helpEntry value

        Note:
            Delegates to help_entry property (CODING_RULE_V2_00017)
        """
        return self.help_entry  # Delegates to property

    def setHelpEntry(self, value: "String") -> MultiLanguageParagraph:
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

    def getL1(self) -> "LParagraph":
        """
        AUTOSAR-compliant getter for l1.

        Returns:
            The l1 value

        Note:
            Delegates to l1 property (CODING_RULE_V2_00017)
        """
        return self.l1  # Delegates to property

    def setL1(self, value: "LParagraph") -> MultiLanguageParagraph:
        """
        AUTOSAR-compliant setter for l1 with method chaining.

        Args:
            value: The l1 to set

        Returns:
            self for method chaining

        Note:
            Delegates to l1 property setter (gets validation automatically)
        """
        self.l1 = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_help_entry(self, value: Optional["String"]) -> MultiLanguageParagraph:
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

    def with_l1(self, value: "LParagraph") -> MultiLanguageParagraph:
        """
        Set l1 and return self for chaining.

        Args:
            value: The l1 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_l1("value")
        """
        self.l1 = value  # Use property setter (gets validation)
        return self



class MultiLanguageVerbatim(Paginateable):
    """
    This class represents multilingual Verbatim. Verbatim means, that
    white-space is maintained. When Verbatim is rendered in PDF or Online media,
    white-space is obeyed. Blanks are rendered as well as newline characters.

    Package: M2::MSR::Documentation::TextModel::MultilanguageData::MultiLanguageVerbatim

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

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"allowBreak must be NameToken or str or None, got {type(value).__name__}"
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"helpEntry must be String or str or None, got {type(value).__name__}"
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

    def setAllowBreak(self, value: "NameToken") -> MultiLanguageVerbatim:
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

    def setFloat(self, value: "FloatEnum") -> MultiLanguageVerbatim:
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

    def setHelpEntry(self, value: "String") -> MultiLanguageVerbatim:
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

    def setL5(self, value: "LVerbatim") -> MultiLanguageVerbatim:
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

    def setPgwide(self, value: "PgwideEnum") -> MultiLanguageVerbatim:
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

    def with_allow_break(self, value: Optional["NameToken"]) -> MultiLanguageVerbatim:
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

    def with_float(self, value: Optional["FloatEnum"]) -> MultiLanguageVerbatim:
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

    def with_help_entry(self, value: Optional["String"]) -> MultiLanguageVerbatim:
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

    def with_l5(self, value: "LVerbatim") -> MultiLanguageVerbatim:
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

    def with_pgwide(self, value: Optional["PgwideEnum"]) -> MultiLanguageVerbatim:
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

    def setL10(self, value: "LPlainText") -> MultiLanguagePlainText:
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

    def with_l10(self, value: "LPlainText") -> MultiLanguagePlainText:
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
