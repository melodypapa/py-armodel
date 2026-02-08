from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TopicContentOrMsrQuery(ARObject):
    """
    This meta-class represents a topic or a topic content which is generated
    using queries.

    Package: M2::MSR::Documentation::Chapters::TopicContentOrMsrQuery

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 342, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents automatically contributed contents an msrquery.
        self._msrQueryP1: "MsrQueryP1" = None

    @property
    def msr_query_p1(self) -> "MsrQueryP1":
        """Get msrQueryP1 (Pythonic accessor)."""
        return self._msrQueryP1

    @msr_query_p1.setter
    def msr_query_p1(self, value: "MsrQueryP1") -> None:
        """
        Set msrQueryP1 with validation.

        Args:
            value: The msrQueryP1 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, MsrQueryP1):
            raise TypeError(
                f"msrQueryP1 must be MsrQueryP1, got {type(value).__name__}"
            )
        self._msrQueryP1 = value
        # This is the content of a topic.
        self._topicContent: "TopicContent" = None

    @property
    def topic_content(self) -> "TopicContent":
        """Get topicContent (Pythonic accessor)."""
        return self._topicContent

    @topic_content.setter
    def topic_content(self, value: "TopicContent") -> None:
        """
        Set topicContent with validation.

        Args:
            value: The topicContent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, TopicContent):
            raise TypeError(
                f"topicContent must be TopicContent, got {type(value).__name__}"
            )
        self._topicContent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMsrQueryP1(self) -> "MsrQueryP1":
        """
        AUTOSAR-compliant getter for msrQueryP1.

        Returns:
            The msrQueryP1 value

        Note:
            Delegates to msr_query_p1 property (CODING_RULE_V2_00017)
        """
        return self.msr_query_p1  # Delegates to property

    def setMsrQueryP1(self, value: "MsrQueryP1") -> "TopicContentOrMsrQuery":
        """
        AUTOSAR-compliant setter for msrQueryP1 with method chaining.

        Args:
            value: The msrQueryP1 to set

        Returns:
            self for method chaining

        Note:
            Delegates to msr_query_p1 property setter (gets validation automatically)
        """
        self.msr_query_p1 = value  # Delegates to property setter
        return self

    def getTopicContent(self) -> "TopicContent":
        """
        AUTOSAR-compliant getter for topicContent.

        Returns:
            The topicContent value

        Note:
            Delegates to topic_content property (CODING_RULE_V2_00017)
        """
        return self.topic_content  # Delegates to property

    def setTopicContent(self, value: "TopicContent") -> "TopicContentOrMsrQuery":
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

    def with_msr_query_p1(self, value: "MsrQueryP1") -> "TopicContentOrMsrQuery":
        """
        Set msrQueryP1 and return self for chaining.

        Args:
            value: The msrQueryP1 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_msr_query_p1("value")
        """
        self.msr_query_p1 = value  # Use property setter (gets validation)
        return self

    def with_topic_content(self, value: "TopicContent") -> "TopicContentOrMsrQuery":
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
