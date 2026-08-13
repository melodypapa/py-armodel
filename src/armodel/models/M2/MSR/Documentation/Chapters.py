"""
This module contains the Chapter family of AUTOSAR model classes from the
MSR Documentation::Chapters package (spec M2::MSR::Documentation::Chapters).

These classes are referenced by SwComponentDocumentation
(M2::AUTOSARTemplates::SWComponentTemplate::SoftwareComponentDocumentation) but
live in their own package per the AUTOSAR meta-model.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.TextModel.MsrQuery import MsrQueryP1, MsrQueryProps

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class Chapter(Identifiable):
    """
    This meta-class represents a chapter of a document. Chapters are the primary structuring element in documentation.
    """

    # Chapter method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.58, p.329
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setChapterModel     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getChapterModel     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHelpEntry        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHelpEntry        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the overall contents of the chapter.
        self.chapterModel: Optional[ChapterModel] = None

        # This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator. Maybe it is a concatenated Identifier, but as of now we leave it as an arbitrary string.
        self.helpEntry: Optional[String] = None

    def setHelpEntry(self, value: Optional[String]) -> "Chapter":
        """
        This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator. Maybe it is a concatenated Identifier, but as of now we leave it as an arbitrary string.

        A None value is a no-op and does not overwrite an existing helpEntry.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.helpEntry = value
        return self

    def getHelpEntry(self) -> Optional[String]:
        """
        This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator. Maybe it is a concatenated Identifier, but as of now we leave it as an arbitrary string.

        Returns:
            The entry point in an online help system to be linked with the parent class
        """
        return self.helpEntry

    def setChapterModel(self, value: Optional[ChapterModel]) -> "Chapter":
        """
        This represents the overall contents of the chapter.

        A None value is a no-op and does not overwrite an existing chapterModel.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.chapterModel = value
        return self

    def getChapterModel(self) -> Optional[ChapterModel]:
        """
        This represents the overall contents of the chapter.

        Returns:
            The overall contents of the chapter
        """
        return self.chapterModel


class ChapterModel(ARObject):
    """
    This is the basic content model of a chapter except the Chapter title. This can be utilized in general chapters as well as in predefined chapters.

    A chapter has content on three levels:

    1. chapter content

    2. topics

    3. subchapters
    """

    # ChapterModel method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.59, p.330
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setChapter         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getChapter         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setChapterContent  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getChapterContent  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTopic1          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTopic1          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This is a particular subchapter.
        self.chapter: Optional[ChapterOrMsrQuery] = None

        # This is the chapter content which is not a topic or a subchapter. It is the content which is directly in the chapter.
        self.chapterContent: Optional[ChapterContent] = None

        # This is a topic within the chapter.
        self.topic1: Optional[TopicOrMsrQuery] = None

    def setChapterContent(self, value: Optional[ChapterContent]) -> "ChapterModel":
        """
        This is the chapter content which is not a topic or a subchapter. It is the content which is directly in the chapter.

        A None value is a no-op and does not overwrite an existing chapterContent.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.chapterContent = value
        return self

    def getChapterContent(self) -> Optional[ChapterContent]:
        """
        This is the chapter content which is not a topic or a subchapter. It is the content which is directly in the chapter.

        Returns:
            The chapter content which is not a topic or a subchapter
        """
        return self.chapterContent

    def setTopic1(self, value: Optional[TopicOrMsrQuery]) -> "ChapterModel":
        """
        This is a topic within the chapter.

        A None value is a no-op and does not overwrite an existing topic1.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.topic1 = value
        return self

    def getTopic1(self) -> Optional[TopicOrMsrQuery]:
        """
        This is a topic within the chapter.

        Returns:
            A topic within the chapter
        """
        return self.topic1

    def setChapter(self, value: Optional[ChapterOrMsrQuery]) -> "ChapterModel":
        """
        This is a particular subchapter.

        A None value is a no-op and does not overwrite an existing chapter.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.chapter = value
        return self

    def getChapter(self) -> Optional[ChapterOrMsrQuery]:
        """
        This is a particular subchapter.

        Returns:
            A particular subchapter
        """
        return self.chapter


class ChapterContent(ARObject):
    """
    This class represents the content which is directly in a chapter. It is basically the same as the one in a Topic but might have additional complex structures (e.g. Synopsis)
    """

    # ChapterContent method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.60, p.330
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setTopicContent        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTopicContent        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [ ] setPrms                [x] impl  [ ] docstring  [ ] test  [ ] reader  [ ] writer
    # [ ] getPrms                [x] impl  [ ] docstring  [ ] test  [ ] reader  [ ] writer
    #
    # NOTE: prms (Prms, 1, aggr) is not modeled yet — the Prms class is a deferred
    # placeholder (Rule 0001.10); the stamp is omitted until the real type lands.

    def __init__(self):
        super().__init__()

        # This is that part of a chapter content which may appear in a chapter as well as in a topic.
        self.topicContent: Optional[TopicContentOrMsrQuery] = None

    def setTopicContent(self, value: Optional[TopicContentOrMsrQuery]) -> "ChapterContent":
        """
        This is that part of a chapter content which may appear in a chapter as well as in a topic.

        A None value is a no-op and does not overwrite an existing topicContent.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.topicContent = value
        return self

    def getTopicContent(self) -> Optional[TopicContentOrMsrQuery]:
        """
        This is that part of a chapter content which may appear in a chapter as well as in a topic.

        Returns:
            The chapter content which may appear in a chapter as well as in a topic
        """
        return self.topicContent


class ChapterOrMsrQuery(ARObject):
    """
    This meta-class represents the ability to denote a particular chapter or a query returning a chapter.
    """

    # ChapterOrMsrQuery method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.81, p.342
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addChapter          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getChapters         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMsrQueryChapter  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMsrQueryChapter  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This establishes a subschapter.
        self.chapters: List[Chapter] = []

        # This represents automatically contributed chapters provided by an msrquery.
        self.msrQueryChapter: Optional[MsrQueryChapter] = None

    def addChapter(self, value: Optional[Chapter]) -> "ChapterOrMsrQuery":
        """
        This establishes a subschapter.

        A None value is a no-op and does not append anything.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.chapters.append(value)
        return self

    def getChapters(self) -> List[Chapter]:
        """
        This establishes a subschapter.

        Returns:
            The established subschapters
        """
        return self.chapters

    def setMsrQueryChapter(self, value: Optional[MsrQueryChapter]) -> "ChapterOrMsrQuery":
        """
        This represents automatically contributed chapters provided by an msrquery.

        A None value is a no-op and does not overwrite an existing msrQueryChapter.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.msrQueryChapter = value
        return self

    def getMsrQueryChapter(self) -> Optional[MsrQueryChapter]:
        """
        This represents automatically contributed chapters provided by an msrquery.

        Returns:
            The automatically contributed chapters provided by an msrquery
        """
        return self.msrQueryChapter


class TopicOrMsrQuery(ARObject):
    """
    This class provides the alternative of a Topic with an MsrQuery which delivers a topic.
    """

    # TopicOrMsrQuery method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.80, p.342
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addTopic1           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTopic1s          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMsrQueryTopic1   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMsrQueryTopic1   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This represents automatically contributed topics provided by an msrquery.
        self.msrQueryTopic1: Optional[MsrQueryTopic1] = None

        # This is used to create particular topics within a chapter. A topic is similar to a subchapter, but cannot be nested and will not appear in the table of contents of the document.
        self.topic1: List[Topic1] = []

    def addTopic1(self, value: Optional[Topic1]) -> "TopicOrMsrQuery":
        """
        This is used to create particular topics within a chapter. A topic is similar to a subchapter, but cannot be nested and will not appear in the table of contents of the document.

        A None value is a no-op and does not append anything.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.topic1.append(value)
        return self

    def getTopic1s(self) -> List[Topic1]:
        """
        This is used to create particular topics within a chapter. A topic is similar to a subchapter, but cannot be nested and will not appear in the table of contents of the document.

        Returns:
            The created particular topics within a chapter
        """
        return self.topic1

    def setMsrQueryTopic1(self, value: Optional[MsrQueryTopic1]) -> "TopicOrMsrQuery":
        """
        This represents automatically contributed topics provided by an msrquery.

        A None value is a no-op and does not overwrite an existing msrQueryTopic1.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.msrQueryTopic1 = value
        return self

    def getMsrQueryTopic1(self) -> Optional[MsrQueryTopic1]:
        """
        This represents automatically contributed topics provided by an msrquery.

        Returns:
            The automatically contributed topics provided by an msrquery
        """
        return self.msrQueryTopic1


class Topic1(Identifiable):
    """
    This meta-class represents a topic of a documentation. Topics are similar to chapters but they cannot be nested.

    They also do not appear in the table of content. Topics can be used to produce intermediate headlines thus structuring a chapter internally.
    """

    # Topic1 method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.73, p.338
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setHelpEntry           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHelpEntry           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTopicContent        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTopicContent        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator.
        self.helpEntry: Optional[String] = None

        # This is the content of the topic.
        self.topicContent: Optional[TopicContentOrMsrQuery] = None

    def setHelpEntry(self, value: Optional[String]) -> "Topic1":
        """
        This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator.

        A None value is a no-op and does not overwrite an existing helpEntry.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.helpEntry = value
        return self

    def getHelpEntry(self) -> Optional[String]:
        """
        This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator.

        Returns:
            The entry point in an online help system to be linked with the parent class
        """
        return self.helpEntry

    def setTopicContent(self, value: Optional[TopicContentOrMsrQuery]) -> "Topic1":
        """
        This is the content of the topic.

        A None value is a no-op and does not overwrite an existing topicContent.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.topicContent = value
        return self

    def getTopicContent(self) -> Optional[TopicContentOrMsrQuery]:
        """
        This is the content of the topic.

        Returns:
            The content of the topic
        """
        return self.topicContent


class MsrQueryChapter(ARObject):
    """
    This meta-class represents the ability to express a query which yields a set of chapters as a result.
    """

    # MsrQueryChapter method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.84, p.343
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setMsrQueryProps       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMsrQueryProps       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [ ] setMsrQueryResultChapter  [x] impl  [ ] docstring  [ ] test  [ ] reader  [ ] writer
    # [ ] getMsrQueryResultChapter  [x] impl  [ ] docstring  [ ] test  [ ] reader  [ ] writer
    #
    # NOTE: msrQueryResultChapter (MsrQueryResultChapter, 0..1, aggr) is not modeled
    # yet — the MsrQueryResultChapter class is a deferred placeholder (Rule 0001.10);
    # the stamp is omitted until the real type lands.

    def __init__(self):
        super().__init__()

        # This is argument and properties of the chapter query.
        self.msrQueryProps: Optional[MsrQueryProps] = None

    def setMsrQueryProps(self, value: Optional[MsrQueryProps]) -> "MsrQueryChapter":
        """
        This is argument and properties of the chapter query.

        A None value is a no-op and does not overwrite an existing msrQueryProps.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.msrQueryProps = value
        return self

    def getMsrQueryProps(self) -> Optional[MsrQueryProps]:
        """
        This is argument and properties of the chapter query.

        Returns:
            The argument and properties of the chapter query
        """
        return self.msrQueryProps


class MsrQueryTopic1(ARObject):
    """
    This meta-class represents the ability to specify a query which yields a set of topics as a result.
    """

    # MsrQueryTopic1 method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.83, p.343
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setMsrQueryProps       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMsrQueryProps       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [ ] setMsrQueryResultTopic1  [x] impl  [ ] docstring  [ ] test  [ ] reader  [ ] writer
    # [ ] getMsrQueryResultTopic1  [x] impl  [ ] docstring  [ ] test  [ ] reader  [ ] writer
    #
    # NOTE: msrQueryResultTopic1 (MsrQueryResultTopic1, 0..1, aggr) is not modeled
    # yet — the MsrQueryResultTopic1 class is a deferred placeholder (Rule 0001.10);
    # the stamp is omitted until the real type lands.

    def __init__(self):
        super().__init__()

        # This is argument and properties of the topic query.
        self.msrQueryProps: Optional[MsrQueryProps] = None

    def setMsrQueryProps(self, value: Optional[MsrQueryProps]) -> "MsrQueryTopic1":
        """
        This is argument and properties of the topic query.

        A None value is a no-op and does not overwrite an existing msrQueryProps.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.msrQueryProps = value
        return self

    def getMsrQueryProps(self) -> Optional[MsrQueryProps]:
        """
        This is argument and properties of the topic query.

        Returns:
            The argument and properties of the topic query
        """
        return self.msrQueryProps


class TopicContent(ARObject):
    """
    This meta-class represents the content of a topic. It is mainly a documentation block, but can also be a table.
    """

    # TopicContent method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.81, p.478
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setBlockLevelContent        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBlockLevelContent        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [ ] setTable                    [ ] impl  [ ] docstring  [ ] test  [ ] reader  [ ] writer
    # [ ] getTable                    [ ] impl  [ ] docstring  [ ] test  [ ] reader  [ ] writer
    # [ ] setTraceableTable           [ ] impl  [ ] docstring  [ ] test  [ ] reader  [ ] writer
    # [ ] getTraceableTable           [ ] impl  [ ] docstring  [ ] test  [ ] reader  [ ] writer
    #
    # NOTE: table (Table, 0..1, aggr) and traceableTable (TraceableTable, 1, aggr) are
    # not modeled yet — the Table and TraceableTable classes are deferred placeholders
    # (Rule 0001.10); the stamp is omitted until the real types land.

    def __init__(self):
        super().__init__()

        # This is that part of the content which may also occur in a table cell.
        self.blockLevelContent: Optional["DocumentationBlock"] = None

    def setBlockLevelContent(self, value: Optional["DocumentationBlock"]) -> "TopicContent":
        """
        This is that part of the content which may also occur in a table cell.

        A None value is a no-op and does not overwrite an existing blockLevelContent.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.blockLevelContent = value
        return self

    def getBlockLevelContent(self) -> Optional["DocumentationBlock"]:
        """
        This is that part of the content which may also occur in a table cell.

        Returns:
            The part of the content which may also occur in a table cell
        """
        return self.blockLevelContent


class TopicContentOrMsrQuery(ARObject):
    """
    This meta-class represents a topic or a topic content which is generated using queries.
    """

    # TopicContentOrMsrQuery method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.79, p.342
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setMsrQueryP1          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMsrQueryP1          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTopicContent        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTopicContent        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    #
    # NOTE: msrQueryP1 references the MsrQueryP1 stub (Rule 0001.10) which is a deferred
    # placeholder; the stamp is omitted until the real type lands.

    def __init__(self):
        super().__init__()

        # This represents automatically contributed contents provided by an msrquery.
        self.msrQueryP1: Optional[MsrQueryP1] = None

        # This is the content of a topic.
        self.topicContent: Optional[TopicContent] = None

    def setMsrQueryP1(self, value: Optional[MsrQueryP1]) -> "TopicContentOrMsrQuery":
        """
        This represents automatically contributed contents provided by an msrquery.

        A None value is a no-op and does not overwrite an existing msrQueryP1.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.msrQueryP1 = value
        return self

    def getMsrQueryP1(self) -> Optional[MsrQueryP1]:
        """
        This represents automatically contributed contents provided by an msrquery.

        Returns:
            The automatically contributed contents provided by an msrquery
        """
        return self.msrQueryP1

    def setTopicContent(self, value: Optional[TopicContent]) -> "TopicContentOrMsrQuery":
        """
        This is the content of a topic.

        A None value is a no-op and does not overwrite an existing topicContent.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.topicContent = value
        return self

    def getTopicContent(self) -> Optional[TopicContent]:
        """
        This is the content of a topic.

        Returns:
            The content of a topic
        """
        return self.topicContent
