"""
This module contains tests for the Chapter family of classes in the
MSR Documentation::Chapters package (Chapter, ChapterModel, ChapterContent,
ChapterOrMsrQuery, TopicOrMsrQuery and the MSR query stub types).
"""

from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import Table
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import TraceableTable
from armodel.models.M2.MSR.Documentation.Chapters import (
    Chapter,
    ChapterContent,
    ChapterModel,
    ChapterOrMsrQuery,
    PredefinedChapter,
    Topic1,
    TopicContent,
    TopicContentOrMsrQuery,
    TopicOrMsrQuery,
)
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryChapter, MsrQueryP1, MsrQueryTopic1
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


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


class TestChapterModel:
    """Test class for ChapterModel class (Table 9.59, AUTOSAR_FO_TPS_GenericStructureTemplate)."""

    def test_initialization(self):
        model = ChapterModel()
        assert model.getChapter() is None
        assert model.getChapterContent() is None
        assert model.getTopic1() is None

    def test_chapter_model_inheritance(self):
        """ChapterModel shall derive from ARObject only (Table 9.59 Base row; XSD 00052 complexType CHAPTER-MODEL carries the AR-OBJECT group alone — no Identifiable, hence the no-argument constructor)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

        model = ChapterModel()
        assert isinstance(model, ARObject)
        assert not isinstance(model, Identifiable)

    def test_chapter_model_has_spec_note(self):
        """The class docstring carries the Table 9.59 Note verbatim."""
        assert cleandoc(ChapterModel.__doc__) == (
            "This is the basic content model of a chapter except the Chapter title. This can be utilized in general chapters as well as in predefined chapters.\n"
            "\n"
            "A chapter has content on three levels:\n"
            "\n"
            "1. chapter content\n"
            "\n"
            "2. topics\n"
            "\n"
            "3. subchapters"
        )

    def test_chapter_model_docstrings_match_spec_notes(self):
        """Each accessor docstring leads with its Table 9.59 attribute Note verbatim (Rule 0001.4)."""
        chapter_note = "This is a particular subchapter." " Tags: xml.roleElement=false xml.roleWrapperElement=false xml.sequenceOffset=200" " xml.typeElement=false xml.typeWrapperElement=false"
        chapter_content_note = (
            "This is the chapter content which is not a topic or a subchapter. It is the content which is directly in the chapter."
            " Tags: xml.roleElement=false xml.roleWrapperElement=false xml.sequenceOffset=30"
            " xml.typeElement=false xml.typeWrapperElement=false"
        )
        topic1_note = "This is a topic within the chapter." " Tags: xml.roleElement=false xml.roleWrapperElement=false xml.sequenceOffset=170" " xml.typeElement=false xml.typeWrapperElement=false"

        assert cleandoc(ChapterModel.setChapter.__doc__).split("\n\n")[0] == chapter_note
        assert cleandoc(ChapterModel.getChapter.__doc__).split("\n\n")[0] == chapter_note
        assert "A None value is a no-op and does not overwrite an existing chapter." in cleandoc(ChapterModel.setChapter.__doc__)

        assert cleandoc(ChapterModel.setChapterContent.__doc__).split("\n\n")[0] == chapter_content_note
        assert cleandoc(ChapterModel.getChapterContent.__doc__).split("\n\n")[0] == chapter_content_note
        assert "A None value is a no-op and does not overwrite an existing chapterContent." in cleandoc(ChapterModel.setChapterContent.__doc__)

        assert cleandoc(ChapterModel.setTopic1.__doc__).split("\n\n")[0] == topic1_note
        assert cleandoc(ChapterModel.getTopic1.__doc__).split("\n\n")[0] == topic1_note
        assert "A None value is a no-op and does not overwrite an existing topic1." in cleandoc(ChapterModel.setTopic1.__doc__)

    def test_chapter_model_member_annotations(self):
        """getChapter/setChapter shall be Optional[ChapterOrMsrQuery], getChapterContent/setChapterContent Optional[ChapterContent] and getTopic1/setTopic1 Optional[TopicOrMsrQuery] (Rule 0003)."""
        import typing

        assert typing.get_type_hints(ChapterModel.getChapter)["return"] == typing.Optional[ChapterOrMsrQuery]
        assert typing.get_type_hints(ChapterModel.setChapter)["value"] == typing.Optional[ChapterOrMsrQuery]
        assert typing.get_type_hints(ChapterModel.getChapterContent)["return"] == typing.Optional[ChapterContent]
        assert typing.get_type_hints(ChapterModel.setChapterContent)["value"] == typing.Optional[ChapterContent]
        assert typing.get_type_hints(ChapterModel.getTopic1)["return"] == typing.Optional[TopicOrMsrQuery]
        assert typing.get_type_hints(ChapterModel.setTopic1)["value"] == typing.Optional[TopicOrMsrQuery]

    def test_set_get_chapter(self):
        model = ChapterModel()
        query = ChapterOrMsrQuery()
        assert model.setChapter(query) is model
        assert model.getChapter() is query
        model.setChapter(None)
        assert model.getChapter() is query

    def test_set_get_chapter_content(self):
        model = ChapterModel()
        content = ChapterContent()
        assert model.setChapterContent(content) is model
        assert model.getChapterContent() is content
        model.setChapterContent(None)
        assert model.getChapterContent() is content

    def test_set_get_topic1(self):
        model = ChapterModel()
        topic_or_msr_query = TopicOrMsrQuery()
        assert model.setTopic1(topic_or_msr_query) is model
        assert model.getTopic1() is topic_or_msr_query
        model.setTopic1(None)
        assert model.getTopic1() is topic_or_msr_query


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


class TestChapterContent:
    """Test class for ChapterContent class (Table 9.60, AUTOSAR_FO_TPS_GenericStructureTemplate)."""

    def test_initialization(self):
        content = ChapterContent()
        assert content.getTopicContent() is None

    def test_chapter_content_inheritance(self):
        """ChapterContent shall derive from ARObject only (Table 9.60 Base row; XSD 00052 complexType CHAPTER-CONTENT carries the AR-OBJECT group alone — no Identifiable, hence the no-argument constructor)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

        content = ChapterContent()
        assert isinstance(content, ARObject)
        assert not isinstance(content, Identifiable)

    def test_chapter_content_has_spec_note(self):
        """The class docstring carries the Table 9.60 Note verbatim."""
        assert (
            cleandoc(ChapterContent.__doc__)
            == "This class represents the content which is directly in a chapter. It is basically the same as the one in a Topic but might have additional complex structures (e.g. Synopsis)"
        )

    def test_chapter_content_docstrings_match_spec_notes(self):
        """Each accessor docstring leads with its Table 9.60 attribute Note verbatim (Rule 0001.4)."""
        topic_content_note = (
            "This is that part of a chapter content which may appear in a chapter as well as in a topic."
            " Tags: xml.roleElement=false xml.roleWrapperElement=false xml.sequenceOffset=40"
            " xml.typeElement=false xml.typeWrapperElement=false"
        )

        assert cleandoc(ChapterContent.setTopicContent.__doc__).split("\n\n")[0] == topic_content_note
        assert cleandoc(ChapterContent.getTopicContent.__doc__).split("\n\n")[0] == topic_content_note
        assert "A None value is a no-op and does not overwrite an existing topicContent." in cleandoc(ChapterContent.setTopicContent.__doc__)

    def test_chapter_content_member_annotations(self):
        """getTopicContent/setTopicContent shall be Optional[TopicContentOrMsrQuery] (Rule 0003)."""
        import typing

        assert typing.get_type_hints(ChapterContent.getTopicContent)["return"] == typing.Optional[TopicContentOrMsrQuery]
        assert typing.get_type_hints(ChapterContent.setTopicContent)["value"] == typing.Optional[TopicContentOrMsrQuery]

    def test_set_get_topic_content(self):
        content = ChapterContent()
        topic_content_or_msr_query = TopicContentOrMsrQuery()
        assert content.setTopicContent(topic_content_or_msr_query) is content
        assert content.getTopicContent() is topic_content_or_msr_query
        content.setTopicContent(None)
        assert content.getTopicContent() is topic_content_or_msr_query


class TestTopicContentOrMsrQuery:
    """Test class for TopicContentOrMsrQuery class (Table 9.79, AUTOSAR_FO_TPS_GenericStructureTemplate)."""

    def test_initialization(self):
        content = TopicContentOrMsrQuery()
        assert isinstance(content, object)
        assert content.getMsrQueryP1() is None
        assert content.getTopicContent() is None

    def test_topic_content_or_msr_query_inheritance(self):
        """TopicContentOrMsrQuery shall derive from ARObject only (Table 9.79 Base row; XSD 00052 complexType TOPIC-CONTENT-OR-MSR-QUERY carries the AR-OBJECT group alone — no Identifiable, hence the no-argument constructor)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

        content = TopicContentOrMsrQuery()
        assert isinstance(content, ARObject)
        assert not isinstance(content, Identifiable)

    def test_topic_content_or_msr_query_has_spec_note(self):
        """The class docstring carries the Table 9.79 Note verbatim."""
        assert cleandoc(TopicContentOrMsrQuery.__doc__) == "This meta-class represents a topic or a topic content which is generated using queries."

    def test_topic_content_or_msr_query_docstrings_match_spec_notes(self):
        """Each accessor docstring leads with its Table 9.79 attribute Note verbatim (Rule 0001.4)."""
        msr_query_p1_note = "This represents automatically contributed contents provided by an msrquery."
        topic_content_note = "This is the content of a topic. Tags: xml.roleElement=false"

        assert cleandoc(TopicContentOrMsrQuery.setMsrQueryP1.__doc__).split("\n\n")[0] == msr_query_p1_note
        assert cleandoc(TopicContentOrMsrQuery.getMsrQueryP1.__doc__).split("\n\n")[0] == msr_query_p1_note
        assert "A None value is a no-op and does not overwrite an existing msrQueryP1." in cleandoc(TopicContentOrMsrQuery.setMsrQueryP1.__doc__)

        assert cleandoc(TopicContentOrMsrQuery.setTopicContent.__doc__).split("\n\n")[0] == topic_content_note
        assert cleandoc(TopicContentOrMsrQuery.getTopicContent.__doc__).split("\n\n")[0] == topic_content_note
        assert "A None value is a no-op and does not overwrite an existing topicContent." in cleandoc(TopicContentOrMsrQuery.setTopicContent.__doc__)

    def test_topic_content_or_msr_query_member_annotations(self):
        """getMsrQueryP1/setMsrQueryP1 shall be Optional[MsrQueryP1] and getTopicContent/setTopicContent Optional[TopicContent] (Rule 0003).

        MsrQueryP1 is a TYPE_CHECKING-only import in Chapters.py, so the hints
        are resolved with an explicit globals mapping.
        """
        import sys
        import typing

        chapters_module = sys.modules[TopicContentOrMsrQuery.__module__]
        globalns = dict(chapters_module.__dict__)
        globalns["MsrQueryP1"] = MsrQueryP1
        assert typing.get_type_hints(TopicContentOrMsrQuery.getMsrQueryP1, globalns=globalns)["return"] == typing.Optional[MsrQueryP1]
        assert typing.get_type_hints(TopicContentOrMsrQuery.setMsrQueryP1, globalns=globalns)["value"] == typing.Optional[MsrQueryP1]
        assert typing.get_type_hints(TopicContentOrMsrQuery.getTopicContent)["return"] == typing.Optional[TopicContent]
        assert typing.get_type_hints(TopicContentOrMsrQuery.setTopicContent)["value"] == typing.Optional[TopicContent]

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


class TestTopicContent:
    """Test class for TopicContent class."""

    def test_initialization(self):
        topic_content = TopicContent()
        assert isinstance(topic_content, object)
        assert topic_content.getBlockLevelContent() is None
        assert topic_content.getTable() is None
        assert topic_content.getTraceableTable() is None

    def test_set_get_block_level_content(self):
        topic_content = TopicContent()
        block = DocumentationBlock()
        assert topic_content.setBlockLevelContent(block) is topic_content
        assert topic_content.getBlockLevelContent() is block
        topic_content.setBlockLevelContent(None)
        assert topic_content.getBlockLevelContent() is block

    def test_set_get_table(self):
        topic_content = TopicContent()
        table = Table()
        assert topic_content.setTable(table) is topic_content
        assert topic_content.getTable() is table
        topic_content.setTable(None)
        assert topic_content.getTable() is table

    def test_create_traceable_table(self):
        topic_content = TopicContent()
        traceable_table = topic_content.createTraceableTable("TRACEABLE_TABLE")
        assert isinstance(traceable_table, TraceableTable)
        assert traceable_table.getShortName() == "TRACEABLE_TABLE"
        assert traceable_table.getParent() is topic_content
        assert topic_content.getTraceableTable() is traceable_table

    def test_create_traceable_table_returns_existing(self):
        topic_content = TopicContent()
        first = topic_content.createTraceableTable("TRACEABLE_TABLE")
        second = topic_content.createTraceableTable("TRACEABLE_TABLE")
        assert second is first
        assert topic_content.getTraceableTable() is first

    def test_create_traceable_table_replaces_different_short_name(self):
        topic_content = TopicContent()
        first = topic_content.createTraceableTable("FIRST")
        second = topic_content.createTraceableTable("SECOND")
        assert second is not first
        assert second.getShortName() == "SECOND"
        assert topic_content.getTraceableTable() is second
