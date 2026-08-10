"""This module contains tests for the MsrQuery module in MSR.Documentation.TextModel."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, String
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.MsrQuery import MsrQueryArg, MsrQueryP2, MsrQueryProps


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
