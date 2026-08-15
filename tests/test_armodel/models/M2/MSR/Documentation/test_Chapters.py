"""
This module contains tests for the Chapter family of classes in the
MSR Documentation::Chapters package (Chapter, ChapterModel, ChapterContent,
ChapterOrMsrQuery, TopicOrMsrQuery and the MSR query stub types).
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.Chapters import (
    Chapter,
    ChapterContent,
    ChapterModel,
    ChapterOrMsrQuery,
    MsrQueryChapter,
    MsrQueryTopic1,
    PredefinedChapter,
    Topic1,
    TopicContent,
    TopicContentOrMsrQuery,
    TopicOrMsrQuery,
)
from armodel.models.M2.MSR.Documentation.TextModel.MsrQuery import MsrQueryP1


class TestChapter:
    """Test class for Chapter class."""

    def _parent(self):
        document = AUTOSAR.getInstance()
        return document.createARPackage("AUTOSAR")

    def test_chapter_initialization(self):
        parent = self._parent()
        chapter = Chapter(parent, "MyChapter")
        assert chapter.getShortName() == "MyChapter"
        assert chapter.getHelpEntry() is None
        assert chapter.getChapterModel() is None

    def test_set_get_help_entry(self):
        parent = self._parent()
        chapter = Chapter(parent, "MyChapter")
        help_entry = String().setValue("help.entry")
        assert chapter.setHelpEntry(help_entry) is chapter
        assert chapter.getHelpEntry() is help_entry
        chapter.setHelpEntry(None)
        assert chapter.getHelpEntry() is help_entry

    def test_set_get_chapter_model(self):
        parent = self._parent()
        chapter = Chapter(parent, "MyChapter")
        chapter_model = ChapterModel()
        assert chapter.setChapterModel(chapter_model) is chapter
        assert chapter.getChapterModel() is chapter_model
        chapter.setChapterModel(None)
        assert chapter.getChapterModel() is chapter_model


class TestPredefinedChapter:
    """Test class for PredefinedChapter class."""

    def test_initialization(self):
        predefined = PredefinedChapter()
        assert predefined.getChapterModel() is None

    def test_set_get_chapter_model(self):
        predefined = PredefinedChapter()
        chapter_model = ChapterModel()
        assert predefined.setChapterModel(chapter_model) is predefined
        assert predefined.getChapterModel() is chapter_model
        predefined.setChapterModel(None)
        assert predefined.getChapterModel() is chapter_model


class TestDocumentationLeafClasses:
    """Test classes for the empty/leaf documentation container classes."""

    def _parent(self):
        document = AUTOSAR.getInstance()
        return document.createARPackage("AUTOSAR")

    def test_chapter_content_and_topic_or_msr_query(self):
        content = ChapterContent()
        query = TopicOrMsrQuery()
        assert isinstance(content, object)
        assert isinstance(query, object)

    def test_chapter_or_msr_query_add_get_chapters(self):
        parent = self._parent()
        query = ChapterOrMsrQuery()
        chapter_a = Chapter(parent, "NestedA")
        chapter_b = Chapter(parent, "NestedB")
        assert query.addChapter(chapter_a) is query
        query.addChapter(None)
        query.addChapter(chapter_b)
        assert query.getChapters() == [chapter_a, chapter_b]

    def test_chapter_or_msr_query_msr_query_chapter(self):
        query = ChapterOrMsrQuery()
        msr_chapter = MsrQueryChapter()
        assert query.setMsrQueryChapter(msr_chapter) is query
        assert query.getMsrQueryChapter() is msr_chapter
        query.setMsrQueryChapter(None)
        assert query.getMsrQueryChapter() is msr_chapter

    def test_topic_or_msr_query_add_get_topic1_and_msr_query_topic1(self):
        parent = self._parent()
        query = TopicOrMsrQuery()
        topic_a = Topic1(parent, "TopicA")
        topic_b = Topic1(parent, "TopicB")
        assert query.addTopic1(topic_a) is query
        query.addTopic1(None)
        query.addTopic1(topic_b)
        assert query.getTopic1s() == [topic_a, topic_b]
        msr_topic = MsrQueryTopic1()
        assert query.setMsrQueryTopic1(msr_topic) is query
        assert query.getMsrQueryTopic1() is msr_topic
        query.setMsrQueryTopic1(None)
        assert query.getMsrQueryTopic1() is msr_topic

    def test_msr_query_stub_classes_instantiable(self):
        parent = self._parent()
        assert isinstance(Topic1(parent, "T"), object)
        assert isinstance(MsrQueryChapter(), object)
        assert isinstance(MsrQueryTopic1(), object)


class TestTopicContentOrMsrQuery:
    """Test class for TopicContentOrMsrQuery class."""

    def test_initialization(self):
        content = TopicContentOrMsrQuery()
        assert isinstance(content, object)
        assert content.getMsrQueryP1() is None
        assert content.getTopicContent() is None

    def test_set_get_msr_query_p1(self):
        content = TopicContentOrMsrQuery()
        msr_query_p1 = MsrQueryP1()
        assert content.setMsrQueryP1(msr_query_p1) is content
        assert content.getMsrQueryP1() is msr_query_p1
        content.setMsrQueryP1(None)
        assert content.getMsrQueryP1() is msr_query_p1

    def test_set_get_topic_content(self):
        content = TopicContentOrMsrQuery()
        topic_content = TopicContent()
        assert content.setTopicContent(topic_content) is content
        assert content.getTopicContent() is topic_content
        content.setTopicContent(None)
        assert content.getTopicContent() is topic_content
