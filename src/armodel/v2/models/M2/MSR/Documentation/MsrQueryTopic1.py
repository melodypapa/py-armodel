from typing import Optional

from armodel.v2.models.M2.MSR.Documentation.BlockElements.Paginateable import (
    Paginateable,
)
from armodel.v2.models.M2.MSR.Documentation.MsrQuery import (
    MsrQueryProps,
    MsrQueryResultTopic1,
)


class MsrQueryTopic1(Paginateable):
    """
    This meta-class represents the ability to specify a query which yields a set
    of topics as a result.

    Package: M2::MSR::Documentation::MsrQuery

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 343, Foundation
      R23-11)
    """
    def __init__(self) -> None:
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is argument and properties of the topic query.
        self._msrQueryProps: Optional[MsrQueryProps] = None

    @property
    def msr_query_props(self) -> Optional[MsrQueryProps]:
        """Get msrQueryProps (Pythonic accessor)."""
        return self._msrQueryProps

    @msr_query_props.setter
    def msr_query_props(self, value: Optional[MsrQueryProps]) -> None:
        """
        Set msrQueryProps with validation.

        Args:
            value: The msrQueryProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._msrQueryProps = None
            return

        if not isinstance(value, MsrQueryProps):
            raise TypeError(
                f"msrQueryProps must be MsrQueryProps or None, got {type(value).__name__}"
            )
        self._msrQueryProps = value
        # xml.
        # sequenceOffset=30.
        self._msrQueryResult: Optional[MsrQueryResultTopic1] = None

    @property
    def msr_query_result(self) -> Optional[MsrQueryResultTopic1]:
        """Get msrQueryResult (Pythonic accessor)."""
        return self._msrQueryResult

    @msr_query_result.setter
    def msr_query_result(self, value: Optional[MsrQueryResultTopic1]) -> None:
        """
        Set msrQueryResult with validation.

        Args:
            value: The msrQueryResult to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._msrQueryResult = None
            return

        if not isinstance(value, MsrQueryResultTopic1):
            raise TypeError(
                f"msrQueryResult must be MsrQueryResultTopic1 or None, got {type(value).__name__}"
            )
        self._msrQueryResult = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMsrQueryProps(self) -> MsrQueryProps:
        """
        AUTOSAR-compliant getter for msrQueryProps.

        Returns:
            The msrQueryProps value

        Note:
            Delegates to msr_query_props property (CODING_RULE_V2_00017)
        """
        return self.msr_query_props  # Delegates to property

    def setMsrQueryProps(self, value: MsrQueryProps) -> "MsrQueryTopic1":
        """
        AUTOSAR-compliant setter for msrQueryProps with method chaining.

        Args:
            value: The msrQueryProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to msr_query_props property setter (gets validation automatically)
        """
        self.msr_query_props = value  # Delegates to property setter
        return self

    def getMsrQueryResult(self) -> Optional[MsrQueryResultTopic1]:
        """
        AUTOSAR-compliant getter for msrQueryResult.

        Returns:
            The msrQueryResult value

        Note:
            Delegates to msr_query_result property (CODING_RULE_V2_00017)
        """
        return self.msr_query_result  # Delegates to property

    def setMsrQueryResult(self, value: Optional[MsrQueryResultTopic1]) -> "MsrQueryTopic1":
        """
        AUTOSAR-compliant setter for msrQueryResult with method chaining.

        Args:
            value: The msrQueryResult to set

        Returns:
            self for method chaining

        Note:
            Delegates to msr_query_result property setter (gets validation automatically)
        """
        self.msr_query_result = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_msr_query_props(self, value: MsrQueryProps) -> "MsrQueryTopic1":
        """
        Set msrQueryProps and return self for chaining.

        Args:
            value: The msrQueryProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_msr_query_props("value")
        """
        self.msr_query_props = value  # Use property setter (gets validation)
        return self

    def with_msr_query_result(self, value: Optional[MsrQueryResultTopic1]) -> "MsrQueryTopic1":
        """
        Set msrQueryResult and return self for chaining.

        Args:
            value: The msrQueryResult to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_msr_query_result("value")
        """
        self.msr_query_result = value  # Use property setter (gets validation)
        return self
