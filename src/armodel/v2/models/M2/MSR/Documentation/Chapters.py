"""
AUTOSAR Package - Chapters

Package: M2::MSR::Documentation::Chapters
"""

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    Paginateable,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.Prms import (
    Prms,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.Table import (
    Table,
)
from armodel.v2.models.M2.MSR.Documentation.DocumentationBlock import (
    DocumentationBlock,
)
from armodel.v2.models.M2.MSR.Documentation.MsrQueryChapter import (
    MsrQueryChapter,
)
from armodel.v2.models.M2.MSR.Documentation.MsrQueryP1 import (
    MsrQueryP1,
)
from armodel.v2.models.M2.MSR.Documentation.MsrQueryTopic1 import (
    MsrQueryTopic1,
)


class Chapter(Paginateable):
    """
    This meta-class represents a chapter of a document. Chapters are the primary
    structuring element in documentation.

    Package: M2::MSR::Documentation::Chapters::Chapter

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 698, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 329, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the overall contents of the chapter.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._chapterModel: "ChapterModel" = None

    @property
    def chapter_model(self) -> "ChapterModel":
        """Get chapterModel (Pythonic accessor)."""
        return self._chapterModel

    @chapter_model.setter
    def chapter_model(self, value: "ChapterModel") -> None:
        """
        Set chapterModel with validation.

        Args:
            value: The chapterModel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, ChapterModel):
            raise TypeError(
                f"chapterModel must be ChapterModel, got {type(value).__name__}"
            )
        self._chapterModel = value
                # class.
        # The syntax shall be the applied help system respectively help is a
                # concatenated Identifier, but as of now we as an arbitrary string.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChapterModel(self) -> "ChapterModel":
        """
        AUTOSAR-compliant getter for chapterModel.

        Returns:
            The chapterModel value

        Note:
            Delegates to chapter_model property (CODING_RULE_V2_00017)
        """
        return self.chapter_model  # Delegates to property

    def setChapterModel(self, value: "ChapterModel") -> "Chapter":
        """
        AUTOSAR-compliant setter for chapterModel with method chaining.

        Args:
            value: The chapterModel to set

        Returns:
            self for method chaining

        Note:
            Delegates to chapter_model property setter (gets validation automatically)
        """
        self.chapter_model = value  # Delegates to property setter
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

    def setHelpEntry(self, value: "String") -> "Chapter":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_chapter_model(self, value: "ChapterModel") -> "Chapter":
        """
        Set chapterModel and return self for chaining.

        Args:
            value: The chapterModel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_chapter_model("value")
        """
        self.chapter_model = value  # Use property setter (gets validation)
        return self

    def with_help_entry(self, value: Optional["String"]) -> "Chapter":
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



class ChapterModel(ARObject):
    """
    This is the basic content model of a chapter except the Chapter title. This
    can be utilized in general chapters as well as in predefined chapters. A
    chapter has content on three levels: 1. chapter content 2. topics 3.
    subchapters

    Package: M2::MSR::Documentation::Chapters::ChapterModel

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 699, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 329, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is a particular subchapter.
        self._chapter: Optional["ChapterOrMsrQuery"] = None

    @property
    def chapter(self) -> Optional["ChapterOrMsrQuery"]:
        """Get chapter (Pythonic accessor)."""
        return self._chapter

    @chapter.setter
    def chapter(self, value: Optional["ChapterOrMsrQuery"]) -> None:
        """
        Set chapter with validation.

        Args:
            value: The chapter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._chapter = None
            return

        if not isinstance(value, ChapterOrMsrQuery):
            raise TypeError(
                f"chapter must be ChapterOrMsrQuery or None, got {type(value).__name__}"
            )
        self._chapter = value
        # directly in the.
        self._chapterContent: Optional["ChapterContent"] = None

    @property
    def chapter_content(self) -> Optional["ChapterContent"]:
        """Get chapterContent (Pythonic accessor)."""
        return self._chapterContent

    @chapter_content.setter
    def chapter_content(self, value: Optional["ChapterContent"]) -> None:
        """
        Set chapterContent with validation.

        Args:
            value: The chapterContent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._chapterContent = None
            return

        if not isinstance(value, ChapterContent):
            raise TypeError(
                f"chapterContent must be ChapterContent or None, got {type(value).__name__}"
            )
        self._chapterContent = value
        self._topic1: Optional["TopicOrMsrQuery"] = None

    @property
    def topic1(self) -> Optional["TopicOrMsrQuery"]:
        """Get topic1 (Pythonic accessor)."""
        return self._topic1

    @topic1.setter
    def topic1(self, value: Optional["TopicOrMsrQuery"]) -> None:
        """
        Set topic1 with validation.

        Args:
            value: The topic1 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._topic1 = None
            return

        if not isinstance(value, TopicOrMsrQuery):
            raise TypeError(
                f"topic1 must be TopicOrMsrQuery or None, got {type(value).__name__}"
            )
        self._topic1 = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChapter(self) -> "ChapterOrMsrQuery":
        """
        AUTOSAR-compliant getter for chapter.

        Returns:
            The chapter value

        Note:
            Delegates to chapter property (CODING_RULE_V2_00017)
        """
        return self.chapter  # Delegates to property

    def setChapter(self, value: "ChapterOrMsrQuery") -> "ChapterModel":
        """
        AUTOSAR-compliant setter for chapter with method chaining.

        Args:
            value: The chapter to set

        Returns:
            self for method chaining

        Note:
            Delegates to chapter property setter (gets validation automatically)
        """
        self.chapter = value  # Delegates to property setter
        return self

    def getChapterContent(self) -> "ChapterContent":
        """
        AUTOSAR-compliant getter for chapterContent.

        Returns:
            The chapterContent value

        Note:
            Delegates to chapter_content property (CODING_RULE_V2_00017)
        """
        return self.chapter_content  # Delegates to property

    def setChapterContent(self, value: "ChapterContent") -> "ChapterModel":
        """
        AUTOSAR-compliant setter for chapterContent with method chaining.

        Args:
            value: The chapterContent to set

        Returns:
            self for method chaining

        Note:
            Delegates to chapter_content property setter (gets validation automatically)
        """
        self.chapter_content = value  # Delegates to property setter
        return self

    def getTopic1(self) -> "TopicOrMsrQuery":
        """
        AUTOSAR-compliant getter for topic1.

        Returns:
            The topic1 value

        Note:
            Delegates to topic1 property (CODING_RULE_V2_00017)
        """
        return self.topic1  # Delegates to property

    def setTopic1(self, value: "TopicOrMsrQuery") -> "ChapterModel":
        """
        AUTOSAR-compliant setter for topic1 with method chaining.

        Args:
            value: The topic1 to set

        Returns:
            self for method chaining

        Note:
            Delegates to topic1 property setter (gets validation automatically)
        """
        self.topic1 = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_chapter(self, value: Optional["ChapterOrMsrQuery"]) -> "ChapterModel":
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

    def with_chapter_content(self, value: Optional["ChapterContent"]) -> "ChapterModel":
        """
        Set chapterContent and return self for chaining.

        Args:
            value: The chapterContent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_chapter_content("value")
        """
        self.chapter_content = value  # Use property setter (gets validation)
        return self

    def with_topic1(self, value: Optional["TopicOrMsrQuery"]) -> "ChapterModel":
        """
        Set topic1 and return self for chaining.

        Args:
            value: The topic1 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_topic1("value")
        """
        self.topic1 = value  # Use property setter (gets validation)
        return self



class ChapterContent(ARObject):
    """
    This class represents the content which is directly in a chapter. It is
    basically the same as the one in a Topic but might have additional complex
    structures (e.g. Synopsis)

    Package: M2::MSR::Documentation::Chapters::ChapterContent

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



class PredefinedChapter(ARObject):
    """
    This represents a predefined chapter.

    Package: M2::MSR::Documentation::Chapters::PredefinedChapter

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 330, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the content of the predefined chapter.
        self._chapterModel: "ChapterModel" = None

    @property
    def chapter_model(self) -> "ChapterModel":
        """Get chapterModel (Pythonic accessor)."""
        return self._chapterModel

    @chapter_model.setter
    def chapter_model(self, value: "ChapterModel") -> None:
        """
        Set chapterModel with validation.

        Args:
            value: The chapterModel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, ChapterModel):
            raise TypeError(
                f"chapterModel must be ChapterModel, got {type(value).__name__}"
            )
        self._chapterModel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChapterModel(self) -> "ChapterModel":
        """
        AUTOSAR-compliant getter for chapterModel.

        Returns:
            The chapterModel value

        Note:
            Delegates to chapter_model property (CODING_RULE_V2_00017)
        """
        return self.chapter_model  # Delegates to property

    def setChapterModel(self, value: "ChapterModel") -> "PredefinedChapter":
        """
        AUTOSAR-compliant setter for chapterModel with method chaining.

        Args:
            value: The chapterModel to set

        Returns:
            self for method chaining

        Note:
            Delegates to chapter_model property setter (gets validation automatically)
        """
        self.chapter_model = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_chapter_model(self, value: "ChapterModel") -> "PredefinedChapter":
        """
        Set chapterModel and return self for chaining.

        Args:
            value: The chapterModel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_chapter_model("value")
        """
        self.chapter_model = value  # Use property setter (gets validation)
        return self



class Topic1(Paginateable):
    """
    This meta-class represents a topic of a documentation. Topics are similar to
    chapters but they cannot be nested. They also do not appear in the table of
    content. Topics can be used to produce intermediate headlines thus
    structuring a chapter internally.

    Package: M2::MSR::Documentation::Chapters::Topic1

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 338, Foundation
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

    def getHelpEntry(self) -> "String":
        """
        AUTOSAR-compliant getter for helpEntry.

        Returns:
            The helpEntry value

        Note:
            Delegates to help_entry property (CODING_RULE_V2_00017)
        """
        return self.help_entry  # Delegates to property

    def setHelpEntry(self, value: "String") -> "Topic1":
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

    def getTopicContent(self) -> "TopicContentOrMsr":
        """
        AUTOSAR-compliant getter for topicContent.

        Returns:
            The topicContent value

        Note:
            Delegates to topic_content property (CODING_RULE_V2_00017)
        """
        return self.topic_content  # Delegates to property

    def setTopicContent(self, value: "TopicContentOrMsr") -> "Topic1":
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

    def with_topic_content(self, value: Optional["TopicContentOrMsr"]) -> "Topic1":
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



class TopicOrMsrQuery(ARObject):
    """
    This class provides the alternative of a Topic with an MsrQuery which
    delivers a topic.

    Package: M2::MSR::Documentation::Chapters::TopicOrMsrQuery

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 342, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents automatically contributed topics provided an msrquery.
        self._msrQuery: "MsrQueryTopic1" = None

    @property
    def msr_query(self) -> "MsrQueryTopic1":
        """Get msrQuery (Pythonic accessor)."""
        return self._msrQuery

    @msr_query.setter
    def msr_query(self, value: "MsrQueryTopic1") -> None:
        """
        Set msrQuery with validation.

        Args:
            value: The msrQuery to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, MsrQueryTopic1):
            raise TypeError(
                f"msrQuery must be MsrQueryTopic1, got {type(value).__name__}"
            )
        self._msrQuery = value
        # A similar to a subchapter, but cannot be nested and appear in the table of
                # contents of the document.
        # atpVariation.
        self._topic1: "Topic1" = None

    @property
    def topic1(self) -> "Topic1":
        """Get topic1 (Pythonic accessor)."""
        return self._topic1

    @topic1.setter
    def topic1(self, value: "Topic1") -> None:
        """
        Set topic1 with validation.

        Args:
            value: The topic1 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Topic1):
            raise TypeError(
                f"topic1 must be Topic1, got {type(value).__name__}"
            )
        self._topic1 = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMsrQuery(self) -> "MsrQueryTopic1":
        """
        AUTOSAR-compliant getter for msrQuery.

        Returns:
            The msrQuery value

        Note:
            Delegates to msr_query property (CODING_RULE_V2_00017)
        """
        return self.msr_query  # Delegates to property

    def setMsrQuery(self, value: "MsrQueryTopic1") -> "TopicOrMsrQuery":
        """
        AUTOSAR-compliant setter for msrQuery with method chaining.

        Args:
            value: The msrQuery to set

        Returns:
            self for method chaining

        Note:
            Delegates to msr_query property setter (gets validation automatically)
        """
        self.msr_query = value  # Delegates to property setter
        return self

    def getTopic1(self) -> "Topic1":
        """
        AUTOSAR-compliant getter for topic1.

        Returns:
            The topic1 value

        Note:
            Delegates to topic1 property (CODING_RULE_V2_00017)
        """
        return self.topic1  # Delegates to property

    def setTopic1(self, value: "Topic1") -> "TopicOrMsrQuery":
        """
        AUTOSAR-compliant setter for topic1 with method chaining.

        Args:
            value: The topic1 to set

        Returns:
            self for method chaining

        Note:
            Delegates to topic1 property setter (gets validation automatically)
        """
        self.topic1 = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_msr_query(self, value: "MsrQueryTopic1") -> "TopicOrMsrQuery":
        """
        Set msrQuery and return self for chaining.

        Args:
            value: The msrQuery to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_msr_query("value")
        """
        self.msr_query = value  # Use property setter (gets validation)
        return self

    def with_topic1(self, value: "Topic1") -> "TopicOrMsrQuery":
        """
        Set topic1 and return self for chaining.

        Args:
            value: The topic1 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_topic1("value")
        """
        self.topic1 = value  # Use property setter (gets validation)
        return self



class ChapterOrMsrQuery(ARObject):
    """
    This meta-class represents the ability to denote a particular chapter or a
    query returning a chapter.

    Package: M2::MSR::Documentation::Chapters::ChapterOrMsrQuery

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 342, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This establishes a subschapter.
        # atpVariation.
        self._chapter: "Chapter" = None

    @property
    def chapter(self) -> "Chapter":
        """Get chapter (Pythonic accessor)."""
        return self._chapter

    @chapter.setter
    def chapter(self, value: "Chapter") -> None:
        """
        Set chapter with validation.

        Args:
            value: The chapter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Chapter):
            raise TypeError(
                f"chapter must be Chapter, got {type(value).__name__}"
            )
        self._chapter = value
        self._msrQuery: "MsrQueryChapter" = None

    @property
    def msr_query(self) -> "MsrQueryChapter":
        """Get msrQuery (Pythonic accessor)."""
        return self._msrQuery

    @msr_query.setter
    def msr_query(self, value: "MsrQueryChapter") -> None:
        """
        Set msrQuery with validation.

        Args:
            value: The msrQuery to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, MsrQueryChapter):
            raise TypeError(
                f"msrQuery must be MsrQueryChapter, got {type(value).__name__}"
            )
        self._msrQuery = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChapter(self) -> "Chapter":
        """
        AUTOSAR-compliant getter for chapter.

        Returns:
            The chapter value

        Note:
            Delegates to chapter property (CODING_RULE_V2_00017)
        """
        return self.chapter  # Delegates to property

    def setChapter(self, value: "Chapter") -> "ChapterOrMsrQuery":
        """
        AUTOSAR-compliant setter for chapter with method chaining.

        Args:
            value: The chapter to set

        Returns:
            self for method chaining

        Note:
            Delegates to chapter property setter (gets validation automatically)
        """
        self.chapter = value  # Delegates to property setter
        return self

    def getMsrQuery(self) -> "MsrQueryChapter":
        """
        AUTOSAR-compliant getter for msrQuery.

        Returns:
            The msrQuery value

        Note:
            Delegates to msr_query property (CODING_RULE_V2_00017)
        """
        return self.msr_query  # Delegates to property

    def setMsrQuery(self, value: "MsrQueryChapter") -> "ChapterOrMsrQuery":
        """
        AUTOSAR-compliant setter for msrQuery with method chaining.

        Args:
            value: The msrQuery to set

        Returns:
            self for method chaining

        Note:
            Delegates to msr_query property setter (gets validation automatically)
        """
        self.msr_query = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_chapter(self, value: "Chapter") -> "ChapterOrMsrQuery":
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

    def with_msr_query(self, value: "MsrQueryChapter") -> "ChapterOrMsrQuery":
        """
        Set msrQuery and return self for chaining.

        Args:
            value: The msrQuery to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_msr_query("value")
        """
        self.msr_query = value  # Use property setter (gets validation)
        return self



class TopicContent(ARObject):
    """
    This meta-class represents the content of a topic. It is mainly a
    documentation block, but can also be a table.

    Package: M2::MSR::Documentation::Chapters::TopicContent

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 478, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is that part of the content which may also occur in a cell.
        self._blockLevel: "DocumentationBlock" = None

    @property
    def block_level(self) -> "DocumentationBlock":
        """Get blockLevel (Pythonic accessor)."""
        return self._blockLevel

    @block_level.setter
    def block_level(self, value: "DocumentationBlock") -> None:
        """
        Set blockLevel with validation.

        Args:
            value: The blockLevel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"blockLevel must be DocumentationBlock, got {type(value).__name__}"
            )
        self._blockLevel = value
        # atpVariation.
        self._table: Optional["Table"] = None

    @property
    def table(self) -> Optional["Table"]:
        """Get table (Pythonic accessor)."""
        return self._table

    @table.setter
    def table(self, value: Optional["Table"]) -> None:
        """
        Set table with validation.

        Args:
            value: The table to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._table = None
            return

        if not isinstance(value, Table):
            raise TypeError(
                f"table must be Table or None, got {type(value).__name__}"
            )
        self._table = value
        self._traceableTable: "TraceableTable" = None

    @property
    def traceable_table(self) -> "TraceableTable":
        """Get traceableTable (Pythonic accessor)."""
        return self._traceableTable

    @traceable_table.setter
    def traceable_table(self, value: "TraceableTable") -> None:
        """
        Set traceableTable with validation.

        Args:
            value: The traceableTable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, TraceableTable):
            raise TypeError(
                f"traceableTable must be TraceableTable, got {type(value).__name__}"
            )
        self._traceableTable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlockLevel(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for blockLevel.

        Returns:
            The blockLevel value

        Note:
            Delegates to block_level property (CODING_RULE_V2_00017)
        """
        return self.block_level  # Delegates to property

    def setBlockLevel(self, value: "DocumentationBlock") -> "TopicContent":
        """
        AUTOSAR-compliant setter for blockLevel with method chaining.

        Args:
            value: The blockLevel to set

        Returns:
            self for method chaining

        Note:
            Delegates to block_level property setter (gets validation automatically)
        """
        self.block_level = value  # Delegates to property setter
        return self

    def getTable(self) -> "Table":
        """
        AUTOSAR-compliant getter for table.

        Returns:
            The table value

        Note:
            Delegates to table property (CODING_RULE_V2_00017)
        """
        return self.table  # Delegates to property

    def setTable(self, value: "Table") -> "TopicContent":
        """
        AUTOSAR-compliant setter for table with method chaining.

        Args:
            value: The table to set

        Returns:
            self for method chaining

        Note:
            Delegates to table property setter (gets validation automatically)
        """
        self.table = value  # Delegates to property setter
        return self

    def getTraceableTable(self) -> "TraceableTable":
        """
        AUTOSAR-compliant getter for traceableTable.

        Returns:
            The traceableTable value

        Note:
            Delegates to traceable_table property (CODING_RULE_V2_00017)
        """
        return self.traceable_table  # Delegates to property

    def setTraceableTable(self, value: "TraceableTable") -> "TopicContent":
        """
        AUTOSAR-compliant setter for traceableTable with method chaining.

        Args:
            value: The traceableTable to set

        Returns:
            self for method chaining

        Note:
            Delegates to traceable_table property setter (gets validation automatically)
        """
        self.traceable_table = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_block_level(self, value: "DocumentationBlock") -> "TopicContent":
        """
        Set blockLevel and return self for chaining.

        Args:
            value: The blockLevel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_block_level("value")
        """
        self.block_level = value  # Use property setter (gets validation)
        return self

    def with_table(self, value: Optional["Table"]) -> "TopicContent":
        """
        Set table and return self for chaining.

        Args:
            value: The table to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_table("value")
        """
        self.table = value  # Use property setter (gets validation)
        return self

    def with_traceable_table(self, value: "TraceableTable") -> "TopicContent":
        """
        Set traceableTable and return self for chaining.

        Args:
            value: The traceableTable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_traceable_table("value")
        """
        self.traceable_table = value  # Use property setter (gets validation)
        return self
