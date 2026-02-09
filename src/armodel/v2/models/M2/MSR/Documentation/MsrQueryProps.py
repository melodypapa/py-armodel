from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class MsrQueryProps(ARObject):
    """
    This metaclass represents the ability to specificy a query which yields some
    documentation text. The qualities of the result are determined by the
    context in which the query is used.

    Package: M2::MSR::Documentation::MsrQuery

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 344, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element contains a commentary in text form.
        self._comment: Optional["String"] = None

    @property
    def comment(self) -> Optional["String"]:
        """Get comment (Pythonic accessor)."""
        return self._comment

    @comment.setter
    def comment(self, value: Optional["String"]) -> None:
        """
        Set comment with validation.

        Args:
            value: The comment to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._comment = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"comment must be String or None, got {type(value).__name__}"
            )
        self._comment = value
        self._msrQueryArg: List["MsrQueryArg"] = []

    @property
    def msr_query_arg(self) -> List["MsrQueryArg"]:
        """Get msrQueryArg (Pythonic accessor)."""
        return self._msrQueryArg
        # This element specifies the name of the MSR-QUERY.
        self._msrQueryName: "String" = None

    @property
    def msr_query_name(self) -> "String":
        """Get msrQueryName (Pythonic accessor)."""
        return self._msrQueryName

    @msr_query_name.setter
    def msr_query_name(self, value: "String") -> None:
        """
        Set msrQueryName with validation.

        Args:
            value: The msrQueryName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, String):
            raise TypeError(
                f"msrQueryName must be String, got {type(value).__name__}"
            )
        self._msrQueryName = value

    def with_msr_query_arg(self, value):
        """
        Set msr_query_arg and return self for chaining.

        Args:
            value: The msr_query_arg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_msr_query_arg("value")
        """
        self.msr_query_arg = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComment(self) -> "String":
        """
        AUTOSAR-compliant getter for comment.

        Returns:
            The comment value

        Note:
            Delegates to comment property (CODING_RULE_V2_00017)
        """
        return self.comment  # Delegates to property

    def setComment(self, value: "String") -> "MsrQueryProps":
        """
        AUTOSAR-compliant setter for comment with method chaining.

        Args:
            value: The comment to set

        Returns:
            self for method chaining

        Note:
            Delegates to comment property setter (gets validation automatically)
        """
        self.comment = value  # Delegates to property setter
        return self

    def getMsrQueryArg(self) -> List["MsrQueryArg"]:
        """
        AUTOSAR-compliant getter for msrQueryArg.

        Returns:
            The msrQueryArg value

        Note:
            Delegates to msr_query_arg property (CODING_RULE_V2_00017)
        """
        return self.msr_query_arg  # Delegates to property

    def getMsrQueryName(self) -> "String":
        """
        AUTOSAR-compliant getter for msrQueryName.

        Returns:
            The msrQueryName value

        Note:
            Delegates to msr_query_name property (CODING_RULE_V2_00017)
        """
        return self.msr_query_name  # Delegates to property

    def setMsrQueryName(self, value: "String") -> "MsrQueryProps":
        """
        AUTOSAR-compliant setter for msrQueryName with method chaining.

        Args:
            value: The msrQueryName to set

        Returns:
            self for method chaining

        Note:
            Delegates to msr_query_name property setter (gets validation automatically)
        """
        self.msr_query_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_comment(self, value: Optional["String"]) -> "MsrQueryProps":
        """
        Set comment and return self for chaining.

        Args:
            value: The comment to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_comment("value")
        """
        self.comment = value  # Use property setter (gets validation)
        return self

    def with_msr_query_name(self, value: "String") -> "MsrQueryProps":
        """
        Set msrQueryName and return self for chaining.

        Args:
            value: The msrQueryName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_msr_query_name("value")
        """
        self.msr_query_name = value  # Use property setter (gets validation)
        return self
