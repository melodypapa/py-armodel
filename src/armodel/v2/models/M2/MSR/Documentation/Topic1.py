from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.MlFigure import (
    MlFigure,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.MlFormula import (
    MlFormula,
)
from armodel.v2.models.M2.MSR.Documentation.MsrQueryP1 import (
    MsrQueryP1,
)
from armodel.v2.models.M2.MSR.Documentation.MsrQueryP2 import (
    MsrQueryP2,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.MultiLanguageVerbatim import (
    MultiLanguageVerbatim,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.Note import (
    Note,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.StructuredReq import (
    StructuredReq,
)
from armodel.v2.models.M2.MSR.Documentation.TopicContent import (
    TopicContent,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.TraceableText import (
    TraceableText,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.Paginateable import (
    Paginateable,
)
from armodel.v2.models.M2.MSR.Documentation.TopicContentOrMsrQuery import (
    TopicContentOrMsrQuery,
)


class Topic1(Paginateable):
    """
    This meta-class represents a topic of a documentation. Topics are similar to
    chapters but they cannot be nested. They also do not appear in the table of
    content. Topics can be used to produce intermediate headlines thus
    structuring a chapter internally.

    Package: M2::MSR::Documentation::Chapters

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 338, Foundation
      R23-11)
    """
    def __init__(self) -> None:
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

        if not isinstance(value, String):
            raise TypeError(
                f"helpEntry must be String or None, got {type(value).__name__}"
            )
        self._helpEntry = value
        self._topicContent: Optional["TopicContentOrMsrQuery"] = None

    @property
    def topic_content(self) -> Optional["TopicContentOrMsrQuery"]:
        """Get topicContent (Pythonic accessor)."""
        return self._topicContent

    @topic_content.setter
    def topic_content(self, value: Optional["TopicContentOrMsrQuery"]) -> None:
        """
        Set topicContent with validation.

        Args:
            value: The topicContent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._topicContent = None
            return

        if not isinstance(value, TopicContentOrMsrQuery):
            raise TypeError(
                f"topicContent must be TopicContentOrMsrQuery or None, got {type(value).__name__}"
            )
        self._topicContent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHelpEntry(self) -> Optional["String"]:
        """
        AUTOSAR-compliant getter for helpEntry.

        Returns:
            The helpEntry value

        Note:
            Delegates to help_entry property (CODING_RULE_V2_00017)
        """
        return self.help_entry  # Delegates to property

    def setHelpEntry(self, value: Optional["String"]) -> "Topic1":
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

    def getTopicContent(self) -> Optional["TopicContentOrMsrQuery"]:
        """
        AUTOSAR-compliant getter for topicContent.

        Returns:
            The topicContent value

        Note:
            Delegates to topic_content property (CODING_RULE_V2_00017)
        """
        return self.topic_content  # Delegates to property

    def setTopicContent(self, value: Optional["TopicContentOrMsrQuery"]) -> "Topic1":
        """
        AUTOSAR-compliant setter for topicContent with method chaining.

        Args:
            value: The topicContent to set

        Returns:
            self for method chaining

        Note:
            Delegates to topic_content property setter (gets validation automatically)
        """
        self.topic_content = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_help_entry(self, value: Optional["String"]) -> "Topic1":
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

    def with_topic_content(self, value: Optional["TopicContentOrMsrQuery"]) -> "Topic1":
        """
        Set topicContent and return self for chaining.

        Args:
            value: The topicContent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_topic_content("value")
        """
        self.topic_content = value  # Use property setter (gets validation)
        return self
