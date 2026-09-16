"""This module contains tests for the MsrQuery module in MSR.Documentation.TextModel."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, String
from armodel.models.M2.MSR.Documentation.Chapters import Chapter, Topic1, TopicContent
from armodel.models.M2.MSR.Documentation.MsrQuery import (
    MsrQueryArg,
    MsrQueryChapter,
    MsrQueryP1,
    MsrQueryP2,
    MsrQueryProps,
    MsrQueryResultChapter,
    MsrQueryResultTopic1,
    MsrQueryTopic1,
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class TestMsrQueryArg:
    """Test class for MsrQueryArg class."""

    def test_msr_query_arg_initialization(self):
        """Test that a MsrQueryArg object can be initialized with default values."""
        msr_query_arg = MsrQueryArg()
        assert msr_query_arg.arg is None
        assert msr_query_arg.si is None

    def test_msr_query_arg_arg_methods(self):
        """Test the arg getter and setter."""
        msr_query_arg = MsrQueryArg()
        arg = String().setValue("value")

        result = msr_query_arg.setArg(arg)
        assert msr_query_arg.getArg() == arg
        assert result == msr_query_arg

        msr_query_arg.setArg(None)
        assert msr_query_arg.getArg() == arg

    def test_msr_query_arg_si_methods(self):
        """Test the si getter and setter."""
        msr_query_arg = MsrQueryArg()
        si = NameToken().setValue("ARG_NAME")

        result = msr_query_arg.setSi(si)
        assert msr_query_arg.getSi() == si
        assert result == msr_query_arg

        msr_query_arg.setSi(None)
        assert msr_query_arg.getSi() == si


class TestMsrQueryProps:
    """Test class for MsrQueryProps class."""

    def test_msr_query_props_initialization(self):
        """Test that a MsrQueryProps object can be initialized with default values."""
        msr_query_props = MsrQueryProps()
        assert msr_query_props.comment is None
        assert msr_query_props.msrQueryName is None
        assert msr_query_props.msrQueryArgs == []

    def test_msr_query_props_comment_methods(self):
        """Test the comment getter and setter."""
        msr_query_props = MsrQueryProps()
        comment = String().setValue("comment")

        result = msr_query_props.setComment(comment)
        assert msr_query_props.getComment() == comment
        assert result == msr_query_props

        msr_query_props.setComment(None)
        assert msr_query_props.getComment() == comment

    def test_msr_query_props_msr_query_name_methods(self):
        """Test the msrQueryName getter and setter."""
        msr_query_props = MsrQueryProps()
        name = String().setValue("QUERY_NAME")

        result = msr_query_props.setMsrQueryName(name)
        assert msr_query_props.getMsrQueryName() == name
        assert result == msr_query_props

        msr_query_props.setMsrQueryName(None)
        assert msr_query_props.getMsrQueryName() == name

    def test_msr_query_props_args_methods(self):
        """Test adding msrQueryArgs."""
        msr_query_props = MsrQueryProps()
        arg = MsrQueryArg()

        result = msr_query_props.addMsrQueryArg(arg)
        assert arg in msr_query_props.getMsrQueryArgs()
        assert result == msr_query_props

        msr_query_props.addMsrQueryArg(None)
        assert msr_query_props.getMsrQueryArgs() == [arg]


class TestMsrQueryP2:
    """Test class for MsrQueryP2 class."""

    def test_msr_query_p2_initialization(self):
        """Test that a MsrQueryP2 object can be initialized with default values."""
        msr_query_p2 = MsrQueryP2()
        assert msr_query_p2.msrQueryProps is None
        assert msr_query_p2.msrQueryResultP2 is None

    def test_msr_query_p2_msr_query_props_methods(self):
        """Test the msrQueryProps getter and setter."""
        msr_query_p2 = MsrQueryP2()
        props = MsrQueryProps()

        result = msr_query_p2.setMsrQueryProps(props)
        assert msr_query_p2.getMsrQueryProps() == props
        assert result == msr_query_p2

        msr_query_p2.setMsrQueryProps(None)
        assert msr_query_p2.getMsrQueryProps() == props

    def test_msr_query_p2_result_methods(self):
        """Test the msrQueryResultP2 getter and setter."""
        msr_query_p2 = MsrQueryP2()
        result = DocumentationBlock()

        ret = msr_query_p2.setMsrQueryResultP2(result)
        assert msr_query_p2.getMsrQueryResultP2() == result
        assert ret == msr_query_p2

        msr_query_p2.setMsrQueryResultP2(None)
        assert msr_query_p2.getMsrQueryResultP2() == result


class TestMsrQueryResultChapter:
    """Test class for MsrQueryResultChapter class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.87)."""

    def test_msr_query_result_chapter_initialization(self):
        """Test that an MsrQueryResultChapter object can be initialized with default values."""
        result = MsrQueryResultChapter()
        assert result.chapters == []

    def test_msr_query_result_chapter_add_methods(self):
        """Test adding chapters with insertion order and None no-op."""
        result = MsrQueryResultChapter()
        chapter1 = Chapter(None, "ch1")
        chapter2 = Chapter(None, "ch2")

        ret = result.addChapter(chapter1)
        result.addChapter(chapter2)
        assert result.getChapters() == [chapter1, chapter2]
        assert ret == result

        result.addChapter(None)
        assert result.getChapters() == [chapter1, chapter2]


class TestMsrQueryResultTopic1:
    """Test class for MsrQueryResultTopic1 class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.88)."""

    def test_msr_query_result_topic1_initialization(self):
        """Test that an MsrQueryResultTopic1 object can be initialized with default values."""
        result = MsrQueryResultTopic1()
        assert result.topic1 == []

    def test_msr_query_result_topic1_add_methods(self):
        """Test adding topics with insertion order and None no-op."""
        result = MsrQueryResultTopic1()
        topic1 = Topic1(None, "topic-1")
        topic2 = Topic1(None, "topic-2")

        ret = result.addTopic1(topic1)
        result.addTopic1(topic2)
        assert result.getTopic1s() == [topic1, topic2]
        assert ret == result

        result.addTopic1(None)
        assert result.getTopic1s() == [topic1, topic2]
        assert ret == result


class TestMsrQueryTopic1:
    """Test class for MsrQueryTopic1 class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.83)."""

    def test_msr_query_topic1_base_chain(self):
        """MsrQueryTopic1 derives from Paginateable only (spec Base: ARObject, DocumentViewSelectable, Paginateable)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import DocumentViewSelectable, Paginateable

        assert issubclass(MsrQueryTopic1, Paginateable)
        assert issubclass(MsrQueryTopic1, DocumentViewSelectable)
        assert not issubclass(MsrQueryTopic1, VariationPointCapable)

    def test_msr_query_topic1_initialization(self):
        """Test that an MsrQueryTopic1 object can be initialized with default values."""
        result = MsrQueryTopic1()
        assert result.msrQueryProps is None
        assert result.msrQueryResultTopic1 is None

    def test_msr_query_topic1_props_methods(self):
        """Test the msrQueryProps getter and setter with chaining and None no-op."""
        result = MsrQueryTopic1()
        props = MsrQueryProps()

        ret = result.setMsrQueryProps(props)
        assert result.getMsrQueryProps() == props
        assert ret == result

        result.setMsrQueryProps(None)
        assert result.getMsrQueryProps() == props

    def test_msr_query_topic1_result_methods(self):
        """Test the msrQueryResultTopic1 getter and setter with chaining and None no-op."""
        result = MsrQueryTopic1()
        query_result = MsrQueryResultTopic1()

        ret = result.setMsrQueryResultTopic1(query_result)
        assert result.getMsrQueryResultTopic1() == query_result
        assert ret == result

        result.setMsrQueryResultTopic1(None)
        assert result.getMsrQueryResultTopic1() == query_result


class TestMsrQueryP1:
    """Test class for MsrQueryP1 class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.82)."""

    def test_msr_query_p1_base_chain(self):
        """MsrQueryP1 derives from Paginateable only (spec Base: ARObject, DocumentViewSelectable, Paginateable)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import DocumentViewSelectable, Paginateable

        assert issubclass(MsrQueryP1, Paginateable)
        assert issubclass(MsrQueryP1, DocumentViewSelectable)
        assert not issubclass(MsrQueryP1, VariationPointCapable)

    def test_msr_query_p1_initialization(self):
        """Test that an MsrQueryP1 object can be initialized with default values."""
        result = MsrQueryP1()
        assert result.msrQueryProps is None
        assert result.msrQueryResultP1 is None

    def test_msr_query_p1_props_methods(self):
        """Test the msrQueryProps getter and setter with chaining and None no-op."""
        result = MsrQueryP1()
        props = MsrQueryProps()

        ret = result.setMsrQueryProps(props)
        assert result.getMsrQueryProps() == props
        assert ret == result

        result.setMsrQueryProps(None)
        assert result.getMsrQueryProps() == props

    def test_msr_query_p1_result_methods(self):
        """Test the msrQueryResultP1 getter and setter with chaining and None no-op."""
        result = MsrQueryP1()
        query_result = TopicContent()

        ret = result.setMsrQueryResultP1(query_result)
        assert result.getMsrQueryResultP1() == query_result
        assert ret == result

        result.setMsrQueryResultP1(None)
        assert result.getMsrQueryResultP1() == query_result


class TestMsrQueryChapter:
    """Test class for MsrQueryChapter class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.84)."""

    def test_msr_query_chapter_base_chain(self):
        """MsrQueryChapter derives from Paginateable only (spec Base: ARObject , DocumentViewSelectable , Paginateable)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import DocumentViewSelectable, Paginateable

        assert issubclass(MsrQueryChapter, Paginateable)
        assert issubclass(MsrQueryChapter, DocumentViewSelectable)
        assert not issubclass(MsrQueryChapter, VariationPointCapable)

    def test_msr_query_chapter_initialization(self):
        """Test that an MsrQueryChapter object can be initialized with default values."""
        msr_query_chapter = MsrQueryChapter()
        assert msr_query_chapter.msrQueryProps is None
        assert msr_query_chapter.msrQueryResultChapter is None

    def test_msr_query_chapter_props_methods(self):
        """Test the msrQueryProps getter and setter with chaining and None no-op."""
        msr_query_chapter = MsrQueryChapter()
        props = MsrQueryProps()

        result = msr_query_chapter.setMsrQueryProps(props)
        assert msr_query_chapter.getMsrQueryProps() == props
        assert result == msr_query_chapter

        msr_query_chapter.setMsrQueryProps(None)
        assert msr_query_chapter.getMsrQueryProps() == props

    def test_msr_query_chapter_result_methods(self):
        """Test the msrQueryResultChapter getter and setter with chaining and None no-op."""
        msr_query_chapter = MsrQueryChapter()
        result = MsrQueryResultChapter()

        ret = msr_query_chapter.setMsrQueryResultChapter(result)
        assert msr_query_chapter.getMsrQueryResultChapter() == result
        assert ret == msr_query_chapter

        msr_query_chapter.setMsrQueryResultChapter(None)
        assert msr_query_chapter.getMsrQueryResultChapter() == result
