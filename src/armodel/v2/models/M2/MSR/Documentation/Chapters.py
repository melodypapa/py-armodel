from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import (
    Paginateable,
)


class Chapter(Paginateable):
    def __init__(self) -> None:
        super().__init__()

        self.chapterModel: Union[ChapterModel, None] = None
        self.helpEntry: Union[String, None] = None

    def getChapterModel(self):
        return self.chapterModel

    def setChapterModel(self, value):
        if value is not None:
            self.chapterModel = value
        return self

    def getHelpEntry(self):
        return self.helpEntry

    def setHelpEntry(self, value):
        if value is not None:
            self.helpEntry = value
        return self


class ChapterModel(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.chapter: Union[ChapterOrMsrQuery, None] = None
        self.chapterContent: Union[ChapterContent, None] = None
        self.topic1: Union[TopicOrMsrQuery, None] = None

    def getChapter(self):
        return self.chapter

    def setChapter(self, value):
        if value is not None:
            self.chapter = value
        return self

    def getChapterContent(self):
        return self.chapterContent

    def setChapterContent(self, value):
        if value is not None:
            self.chapterContent = value
        return self

    def getTopic1(self):
        return self.topic1

    def setTopic1(self, value):
        if value is not None:
            self.topic1 = value
        return self


class ChapterContent(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.prms: Union[Prms, None] = None
        self.topicContent: Union[TopicContentOrMsrQuery, None] = None

    def getPrms(self):
        return self.prms

    def setPrms(self, value):
        if value is not None:
            self.prms = value
        return self

    def getTopicContent(self):
        return self.topicContent

    def setTopicContent(self, value):
        if value is not None:
            self.topicContent = value
        return self


class Prms(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.parameter = []

    def getParameter(self):
        return self.parameter

    def addParameter(self, value):
        if value is not None:
            self.parameter.append(value)
        return self


class TopicContentOrMsrQuery(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.msrQueryP1: Union[MsrQueryP1, None] = None
        self.topicContent: Union[TopicContent, None] = None

    def getMsrQueryP1(self):
        return self.msrQueryP1

    def setMsrQueryP1(self, value):
        if value is not None:
            self.msrQueryP1 = value
        return self

    def getTopicContent(self):
        return self.topicContent

    def setTopicContent(self, value):
        if value is not None:
            self.topicContent = value
        return self


class MsrQueryP1(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.msrQueryResultP1: Union[TopicContent, None] = None

    def getMsrQueryResultP1(self):
        return self.msrQueryResultP1

    def setMsrQueryResultP1(self, value):
        if value is not None:
            self.msrQueryResultP1 = value
        return self


class TopicContent(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.blockLevel: Union[DocumentationBlock, None] = None
        self.table: Union[Table, None] = None
        self.traceableTable: Union[TraceableTable, None] = None

    def getBlockLevel(self):
        return self.blockLevel

    def setBlockLevel(self, value):
        if value is not None:
            self.blockLevel = value
        return self

    def getTable(self):
        return self.table

    def setTable(self, value):
        if value is not None:
            self.table = value
        return self

    def getTraceableTable(self):
        return self.traceableTable

    def setTraceableTable(self, value):
        if value is not None:
            self.traceableTable = value
        return self


class Table(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.caption = None
        self.rows = []

    def getCaption(self):
        return self.caption

    def setCaption(self, value):
        if value is not None:
            self.caption = value
        return self

    def getRows(self):
        return self.rows

    def addRow(self, value):
        if value is not None:
            self.rows.append(value)
        return self


class TraceableTable(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.caption = None
        self.rows = []

    def getCaption(self):
        return self.caption

    def setCaption(self, value):
        if value is not None:
            self.caption = value
        return self

    def getRows(self):
        return self.rows

    def addRow(self, value):
        if value is not None:
            self.rows.append(value)
        return self


class TopicOrMsrQuery(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.msrQuery: Union[MsrQueryTopic1, None] = None
        self.topic1: Union[Topic1, None] = None

    def getMsrQuery(self):
        return self.msrQuery

    def setMsrQuery(self, value):
        if value is not None:
            self.msrQuery = value
        return self

    def getTopic1(self):
        return self.topic1

    def setTopic1(self, value):
        if value is not None:
            self.topic1 = value
        return self


class MsrQueryTopic1(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.msrQueryResultTopic1: Union[Topic1, None] = None

    def getMsrQueryResultTopic1(self):
        return self.msrQueryResultTopic1

    def setMsrQueryResultTopic1(self, value):
        if value is not None:
            self.msrQueryResultTopic1 = value
        return self


class Topic1(Paginateable):
    def __init__(self) -> None:
        super().__init__()

        self.helpEntry: Union[String, None] = None
        self.topicContent: Union[TopicContentOrMsrQuery, None] = None

    def getHelpEntry(self):
        return self.helpEntry

    def setHelpEntry(self, value):
        if value is not None:
            self.helpEntry = value
        return self

    def getTopicContent(self):
        return self.topicContent

    def setTopicContent(self, value):
        if value is not None:
            self.topicContent = value
        return self


class ChapterOrMsrQuery(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.chapter: Union[Chapter, None] = None
        self.msrQuery: Union[MsrQueryChapter, None] = None

    def getChapter(self):
        return self.chapter

    def setChapter(self, value):
        if value is not None:
            self.chapter = value
        return self

    def getMsrQuery(self):
        return self.msrQuery

    def setMsrQuery(self, value):
        if value is not None:
            self.msrQuery = value
        return self


class MsrQueryChapter(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.msrQueryResultChapter: Union[Chapter, None] = None

    def getMsrQueryResultChapter(self):
        return self.msrQueryResultChapter

    def setMsrQueryResultChapter(self, value):
        if value is not None:
            self.msrQueryResultChapter = value
        return self
