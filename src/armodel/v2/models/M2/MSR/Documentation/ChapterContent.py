from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class ChapterContent(ARObject):
    """
    This class represents the content which is directly in a chapter. It is
    basically the same as the one in a Topic but might have additional complex
    structures (e.g. Synopsis)

    Package: M2::MSR::Documentation::Chapters

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 330, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is a parameter table within a chapter.
        self._prms: "Prms" = None

    @property
    def prms(self) -> "Prms":
        """Get prms (Pythonic accessor)."""
        return self._prms

    @prms.setter
    def prms(self, value: "Prms") -> None:
        """
        Set prms with validation.

        Args:
            value: The prms to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Prms):
            raise TypeError(
                f"prms must be Prms, got {type(value).__name__}"
            )
        self._prms = value
        # This is that part of a chapter content which may appear in chapter as well as
        # in a topic.
        self._topicContent: Optional["TopicContentOrMsr"] = None

    @property
    def topic_content(self) -> Optional["TopicContentOrMsr"]:
        """Get topicContent (Pythonic accessor)."""
        return self._topicContent

    @topic_content.setter
    def topic_content(self, value: Optional["TopicContentOrMsr"]) -> None:
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

        if not isinstance(value, TopicContentOrMsr):
            raise TypeError(
                f"topicContent must be TopicContentOrMsr or None, got {type(value).__name__}"
            )
        self._topicContent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPrms(self) -> "Prms":
        """
        AUTOSAR-compliant getter for prms.

        Returns:
            The prms value

        Note:
            Delegates to prms property (CODING_RULE_V2_00017)
        """
        return self.prms  # Delegates to property

    def setPrms(self, value: "Prms") -> "ChapterContent":
        """
        AUTOSAR-compliant setter for prms with method chaining.

        Args:
            value: The prms to set

        Returns:
            self for method chaining

        Note:
            Delegates to prms property setter (gets validation automatically)
        """
        self.prms = value  # Delegates to property setter
        return self

    def getTopicContent(self) -> "TopicContentOrMsr":
        """
        AUTOSAR-compliant getter for topicContent.

        Returns:
            The topicContent value

        Note:
            Delegates to topic_content property (CODING_RULE_V2_00017)
        """
        return self.topic_content  # Delegates to property

    def setTopicContent(self, value: "TopicContentOrMsr") -> "ChapterContent":
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

    def with_prms(self, value: "Prms") -> "ChapterContent":
        """
        Set prms and return self for chaining.

        Args:
            value: The prms to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_prms("value")
        """
        self.prms = value  # Use property setter (gets validation)
        return self

    def with_topic_content(self, value: Optional["TopicContentOrMsr"]) -> "ChapterContent":
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
