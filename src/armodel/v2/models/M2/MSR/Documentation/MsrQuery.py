"""
AUTOSAR Package - MsrQuery

Package: M2::MSR::Documentation::MsrQuery
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements import (
    DocumentationBlock,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    Paginateable,
)
from armodel.v2.models.M2.MSR.Documentation.Chapters import (
    Chapter,
    TopicContent,
)


class MsrQueryP1(Paginateable):
    """
    This meta-class represents the ability to express a query which yields the
    content of a topic as a result.

    Package: M2::MSR::Documentation::MsrQuery::MsrQueryP1

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 343, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is argument and properties of the paragraph query.
        self._msrQueryProps: MsrQueryProps = None

    @property
    def msr_query_props(self) -> MsrQueryProps:
        """Get msrQueryProps (Pythonic accessor)."""
        return self._msrQueryProps

    @msr_query_props.setter
    def msr_query_props(self, value: MsrQueryProps) -> None:
        """
        Set msrQueryProps with validation.

        Args:
            value: The msrQueryProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, MsrQueryProps):
            raise TypeError(
                f"msrQueryProps must be MsrQueryProps, got {type(value).__name__}"
            )
        self._msrQueryProps = value
        # xml.
        # sequenceOffset=30.
        self._msrQueryResult: Optional[TopicContent] = None

    @property
    def msr_query_result(self) -> Optional[TopicContent]:
        """Get msrQueryResult (Pythonic accessor)."""
        return self._msrQueryResult

    @msr_query_result.setter
    def msr_query_result(self, value: Optional[TopicContent]) -> None:
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

        # Skip isinstance check for forward references
        self._msrQueryResult = value

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

    def with_chapter(self, value):
        """
        Set chapter and return self for chaining.

        Args:
            value: The chapter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_chapter("value")
        """
        self.chapter = value  # Use property setter (gets validation)
        return self

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

    def setMsrQueryProps(self, value: MsrQueryProps) -> MsrQueryP1:
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

    def getMsrQueryResult(self) -> TopicContent:
        """
        AUTOSAR-compliant getter for msrQueryResult.

        Returns:
            The msrQueryResult value

        Note:
            Delegates to msr_query_result property (CODING_RULE_V2_00017)
        """
        return self.msr_query_result  # Delegates to property

    def setMsrQueryResult(self, value: TopicContent) -> MsrQueryP1:
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

    def with_msr_query_props(self, value: MsrQueryProps) -> MsrQueryP1:
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

    def with_msr_query_result(self, value: Optional[TopicContent]) -> MsrQueryP1:
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



class MsrQueryTopic1(Paginateable):
    """
    This meta-class represents the ability to specify a query which yields a set
    of topics as a result.

    Package: M2::MSR::Documentation::MsrQuery::MsrQueryTopic1

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 343, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is argument and properties of the topic query.
        self._msrQueryProps: MsrQueryProps = None

    @property
    def msr_query_props(self) -> MsrQueryProps:
        """Get msrQueryProps (Pythonic accessor)."""
        return self._msrQueryProps

    @msr_query_props.setter
    def msr_query_props(self, value: MsrQueryProps) -> None:
        """
        Set msrQueryProps with validation.

        Args:
            value: The msrQueryProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, MsrQueryProps):
            raise TypeError(
                f"msrQueryProps must be MsrQueryProps, got {type(value).__name__}"
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

    def setMsrQueryProps(self, value: MsrQueryProps) -> MsrQueryTopic1:
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

    def getMsrQueryResult(self) -> MsrQueryResultTopic1:
        """
        AUTOSAR-compliant getter for msrQueryResult.

        Returns:
            The msrQueryResult value

        Note:
            Delegates to msr_query_result property (CODING_RULE_V2_00017)
        """
        return self.msr_query_result  # Delegates to property

    def setMsrQueryResult(self, value: MsrQueryResultTopic1) -> MsrQueryTopic1:
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

    def with_msr_query_props(self, value: MsrQueryProps) -> MsrQueryTopic1:
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

    def with_msr_query_result(self, value: Optional[MsrQueryResultTopic1]) -> MsrQueryTopic1:
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



class MsrQueryChapter(Paginateable):
    """
    This meta-class represents the ability to express a query which yields a set
    of chapters as a result.

    Package: M2::MSR::Documentation::MsrQuery::MsrQueryChapter

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 343, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is argument and properties of the chapter query.
        self._msrQueryProps: MsrQueryProps = None

    @property
    def msr_query_props(self) -> MsrQueryProps:
        """Get msrQueryProps (Pythonic accessor)."""
        return self._msrQueryProps

    @msr_query_props.setter
    def msr_query_props(self, value: MsrQueryProps) -> None:
        """
        Set msrQueryProps with validation.

        Args:
            value: The msrQueryProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, MsrQueryProps):
            raise TypeError(
                f"msrQueryProps must be MsrQueryProps, got {type(value).__name__}"
            )
        self._msrQueryProps = value
        # Tags: xml.
        # sequenceOffset=30.
        self._msrQueryResult: Optional["MsrQueryResult"] = None

    @property
    def msr_query_result(self) -> Optional["MsrQueryResult"]:
        """Get msrQueryResult (Pythonic accessor)."""
        return self._msrQueryResult

    @msr_query_result.setter
    def msr_query_result(self, value: Optional["MsrQueryResult"]) -> None:
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

        if not isinstance(value, MsrQueryResult):
            raise TypeError(
                f"msrQueryResult must be MsrQueryResult or None, got {type(value).__name__}"
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

    def setMsrQueryProps(self, value: MsrQueryProps) -> MsrQueryChapter:
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

    def getMsrQueryResult(self) -> "MsrQueryResult":
        """
        AUTOSAR-compliant getter for msrQueryResult.

        Returns:
            The msrQueryResult value

        Note:
            Delegates to msr_query_result property (CODING_RULE_V2_00017)
        """
        return self.msr_query_result  # Delegates to property

    def setMsrQueryResult(self, value: "MsrQueryResult") -> MsrQueryChapter:
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

    def with_msr_query_props(self, value: MsrQueryProps) -> MsrQueryChapter:
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

    def with_msr_query_result(self, value: Optional["MsrQueryResult"]) -> MsrQueryChapter:
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



class MsrQueryProps(ARObject):
    """
    This metaclass represents the ability to specificy a query which yields some
    documentation text. The qualities of the result are determined by the
    context in which the query is used.

    Package: M2::MSR::Documentation::MsrQuery::MsrQueryProps

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 344, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element contains a commentary in text form.
        self._comment: Optional[String] = None

    @property
    def comment(self) -> Optional[String]:
        """Get comment (Pythonic accessor)."""
        return self._comment

    @comment.setter
    def comment(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"comment must be String or str or None, got {type(value).__name__}"
            )
        self._comment = value
        self._msrQueryArg: List[MsrQueryArg] = []

    @property
    def msr_query_arg(self) -> List[MsrQueryArg]:
        """Get msrQueryArg (Pythonic accessor)."""
        return self._msrQueryArg
        # This element specifies the name of the MSR-QUERY.
        self._msrQueryName: String = None

    @property
    def msr_query_name(self) -> String:
        """Get msrQueryName (Pythonic accessor)."""
        return self._msrQueryName

    @msr_query_name.setter
    def msr_query_name(self, value: String) -> None:
        """
        Set msrQueryName with validation.

        Args:
            value: The msrQueryName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (String, str)):
            raise TypeError(
                f"msrQueryName must be String or str, got {type(value).__name__}"
            )
        self._msrQueryName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComment(self) -> String:
        """
        AUTOSAR-compliant getter for comment.

        Returns:
            The comment value

        Note:
            Delegates to comment property (CODING_RULE_V2_00017)
        """
        return self.comment  # Delegates to property

    def setComment(self, value: String) -> MsrQueryProps:
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

    def getMsrQueryArg(self) -> List[MsrQueryArg]:
        """
        AUTOSAR-compliant getter for msrQueryArg.

        Returns:
            The msrQueryArg value

        Note:
            Delegates to msr_query_arg property (CODING_RULE_V2_00017)
        """
        return self.msr_query_arg  # Delegates to property

    def getMsrQueryName(self) -> String:
        """
        AUTOSAR-compliant getter for msrQueryName.

        Returns:
            The msrQueryName value

        Note:
            Delegates to msr_query_name property (CODING_RULE_V2_00017)
        """
        return self.msr_query_name  # Delegates to property

    def setMsrQueryName(self, value: String) -> MsrQueryProps:
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

    def with_comment(self, value: Optional[String]) -> MsrQueryProps:
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

    def with_msr_query_name(self, value: String) -> MsrQueryProps:
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



class MsrQueryArg(ARObject):
    """
    This represents an argument to the query. Note that the arguments are not
    standardized and therefore subject to mutual agreement.

    Package: M2::MSR::Documentation::MsrQuery::MsrQueryArg

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 344, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the value of the argument.
        self._arg: String = None

    @property
    def arg(self) -> String:
        """Get arg (Pythonic accessor)."""
        return self._arg

    @arg.setter
    def arg(self, value: String) -> None:
        """
        Set arg with validation.

        Args:
            value: The arg to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (String, str)):
            raise TypeError(
                f"arg must be String or str, got {type(value).__name__}"
            )
        self._arg = value
        self._si: NameToken = None

    @property
    def si(self) -> NameToken:
        """Get si (Pythonic accessor)."""
        return self._si

    @si.setter
    def si(self, value: NameToken) -> None:
        """
        Set si with validation.

        Args:
            value: The si to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"si must be NameToken or str, got {type(value).__name__}"
            )
        self._si = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArg(self) -> String:
        """
        AUTOSAR-compliant getter for arg.

        Returns:
            The arg value

        Note:
            Delegates to arg property (CODING_RULE_V2_00017)
        """
        return self.arg  # Delegates to property

    def setArg(self, value: String) -> MsrQueryArg:
        """
        AUTOSAR-compliant setter for arg with method chaining.

        Args:
            value: The arg to set

        Returns:
            self for method chaining

        Note:
            Delegates to arg property setter (gets validation automatically)
        """
        self.arg = value  # Delegates to property setter
        return self

    def getSi(self) -> NameToken:
        """
        AUTOSAR-compliant getter for si.

        Returns:
            The si value

        Note:
            Delegates to si property (CODING_RULE_V2_00017)
        """
        return self.si  # Delegates to property

    def setSi(self, value: NameToken) -> MsrQueryArg:
        """
        AUTOSAR-compliant setter for si with method chaining.

        Args:
            value: The si to set

        Returns:
            self for method chaining

        Note:
            Delegates to si property setter (gets validation automatically)
        """
        self.si = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_arg(self, value: String) -> MsrQueryArg:
        """
        Set arg and return self for chaining.

        Args:
            value: The arg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_arg("value")
        """
        self.arg = value  # Use property setter (gets validation)
        return self

    def with_si(self, value: NameToken) -> MsrQueryArg:
        """
        Set si and return self for chaining.

        Args:
            value: The si to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_si("value")
        """
        self.si = value  # Use property setter (gets validation)
        return self



class MsrQueryResultChapter(ARObject):
    """
    This metaclass represents the result of an msrquery which is a set of
    chapters.

    Package: M2::MSR::Documentation::MsrQuery::MsrQueryResultChapter

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 344, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular chapter in the query result.
        self._chapter: List[Chapter] = []

    @property
    def chapter(self) -> List[Chapter]:
        """Get chapter (Pythonic accessor)."""
        return self._chapter

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChapter(self) -> List[Chapter]:
        """
        AUTOSAR-compliant getter for chapter.

        Returns:
            The chapter value

        Note:
            Delegates to chapter property (CODING_RULE_V2_00017)
        """
        return self.chapter  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class MsrQueryResultTopic1(ARObject):
    """
    This metaclass represents the ability to express the result of a query which
    is a set of topics.

    Package: M2::MSR::Documentation::MsrQuery::MsrQueryResultTopic1

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 345, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class MsrQueryP2(ARObject):
    """
    This meta-class represents the ability to express a query which yields the
    content of a Documentation Block as a result.

    Package: M2::MSR::Documentation::MsrQuery::MsrQueryP2

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 456, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is argument and properties of the Documentation.
        self._msrQueryProps: MsrQueryProps = None

    @property
    def msr_query_props(self) -> MsrQueryProps:
        """Get msrQueryProps (Pythonic accessor)."""
        return self._msrQueryProps

    @msr_query_props.setter
    def msr_query_props(self, value: MsrQueryProps) -> None:
        """
        Set msrQueryProps with validation.

        Args:
            value: The msrQueryProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, MsrQueryProps):
            raise TypeError(
                f"msrQueryProps must be MsrQueryProps, got {type(value).__name__}"
            )
        self._msrQueryProps = value
        # xml.
        # sequenceOffset=30.
        self._msrQueryResult: Optional[DocumentationBlock] = None

    @property
    def msr_query_result(self) -> Optional[DocumentationBlock]:
        """Get msrQueryResult (Pythonic accessor)."""
        return self._msrQueryResult

    @msr_query_result.setter
    def msr_query_result(self, value: Optional[DocumentationBlock]) -> None:
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

        # Skip isinstance check for forward references
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

    def setMsrQueryProps(self, value: MsrQueryProps) -> MsrQueryP2:
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

    def getMsrQueryResult(self) -> DocumentationBlock:
        """
        AUTOSAR-compliant getter for msrQueryResult.

        Returns:
            The msrQueryResult value

        Note:
            Delegates to msr_query_result property (CODING_RULE_V2_00017)
        """
        return self.msr_query_result  # Delegates to property

    def setMsrQueryResult(self, value: DocumentationBlock) -> MsrQueryP2:
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

    def with_msr_query_props(self, value: MsrQueryProps) -> MsrQueryP2:
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

    def with_msr_query_result(self, value: Optional[DocumentationBlock]) -> MsrQueryP2:
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
