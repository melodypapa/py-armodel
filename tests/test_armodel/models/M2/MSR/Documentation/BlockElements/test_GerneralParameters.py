import inspect
from inspect import cleandoc

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, String
from armodel.models.M2.MSR.AsamHdo.Units import SingleLanguageUnitNames
from armodel.models.M2.MSR.Documentation.BlockElements.GerneralParameters import (
    GeneralParameter,
    PrmChar,
    PrmCharAbsTol,
    PrmCharContents,
    PrmCharMinTypMax,
    PrmCharNumericalContents,
    PrmCharNumericalValue,
    PrmCharTextualContents,
    Prms,
)
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import Paginateable
from armodel.models.M2.MSR.Documentation.Chapters import ChapterContent
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName


class TestPrms:
    def test_base_chain(self):
        assert issubclass(Prms, Paginateable)
        assert issubclass(Prms, ARObject)

    def test_initialization(self):
        prms = Prms()
        assert prms.label is None
        assert prms.prm == []

    def test_set_get_label(self):
        prms = Prms()
        label = MultilanguageLongName()
        assert prms.setLabel(label) is prms
        assert prms.getLabel() is label
        assert prms.setLabel(None) is prms
        assert prms.getLabel() is label

    def test_add_prm(self):
        prms = Prms()
        prm = GeneralParameter(prms, "P1")
        assert prms.addPrm(prm) is prms
        assert prms.getPrms() == [prm]
        assert prms.addPrm(None) is prms
        assert prms.getPrms() == [prm]

    def test_class_docstring_verbatim(self):
        assert cleandoc(Prms.__doc__) == ("This metaclass represents the ability to specify a parameter table." " It can be used e.g. to specify parameter tables in a data sheet.")


class TestGeneralParameter:
    def test_base_chain(self):
        assert issubclass(GeneralParameter, Identifiable)

    def test_initialization(self):
        prms = Prms()
        prm = GeneralParameter(prms, "G1")
        assert prm.getShortName() == "G1"
        assert prm.prmChar == []

    def test_add_get_prm_char(self):
        prm = GeneralParameter(None, "G1")
        char = PrmChar()
        assert prm.addPrmChar(char) is prm
        assert prm.getPrmChars() == [char]
        assert prm.addPrmChar(None) is prm
        assert prm.getPrmChars() == [char]

    def test_class_docstring_verbatim(self):
        assert cleandoc(GeneralParameter.__doc__) == "This represents a parameter in general e.g. an entry in a data sheet."


class TestPrmChar:
    def test_base_chain(self):
        assert issubclass(PrmChar, ARObject)

    def test_initialization(self):
        char = PrmChar()
        assert char.cond is None
        assert char.numericalContents is None
        assert char.textualContents is None
        assert char.remark is None

    def test_set_get_cond_remark(self):
        char = PrmChar()
        cond = DocumentationBlock()
        assert char.setCond(cond) is char
        assert char.getCond() is cond
        assert char.setCond(None) is char
        assert char.getCond() is cond
        remark = DocumentationBlock()
        assert char.setRemark(remark) is char
        assert char.getRemark() is remark

    def test_set_get_contents(self):
        char = PrmChar()
        num = PrmCharNumericalContents()
        assert char.setNumericalContents(num) is char
        assert char.getNumericalContents() is num
        txt = PrmCharTextualContents()
        assert char.setTextualContents(txt) is char
        assert char.getTextualContents() is txt

    def test_class_docstring_verbatim(self):
        assert cleandoc(PrmChar.__doc__) == (
            "This metaclass represents the ability to express the characteristics of one particular parameter."
            " It can be exressed as numerical or as text parameter (provided as subclasses of PrmCharContents)"
        )


class TestPrmCharContentsFamily:
    def test_abstract_contents_raises(self):
        with pytest.raises(TypeError):
            PrmCharContents()

    def test_abstract_numerical_value_raises(self):
        with pytest.raises(TypeError):
            PrmCharNumericalValue()

    def test_abs_tol(self):
        tol = PrmCharAbsTol()
        assert isinstance(tol, PrmCharNumericalValue)
        assert tol.abs is None and tol.tol is None
        abs_val = Numerical()
        assert tol.setAbs(abs_val) is tol
        assert tol.getAbs() is abs_val
        tol_val = Numerical()
        assert tol.setTol(tol_val) is tol
        assert tol.getTol() is tol_val

    def test_min_typ_max(self):
        mtm = PrmCharMinTypMax()
        assert isinstance(mtm, PrmCharNumericalValue)
        assert mtm.min is None and mtm.typ is None and mtm.max is None
        assert mtm.setMin(Numerical()) is mtm
        assert mtm.setTyp(Numerical()) is mtm
        assert mtm.setMax(Numerical()) is mtm
        assert isinstance(mtm.getMin(), Numerical)
        assert isinstance(mtm.getTyp(), Numerical)
        assert isinstance(mtm.getMax(), Numerical)

    def test_numerical_contents(self):
        num = PrmCharNumericalContents()
        assert isinstance(num, PrmCharContents)
        assert num.absTol is None and num.minTypMax is None and num.prmUnit is None
        assert num.setAbsTol(PrmCharAbsTol()) is num
        assert num.setMinTypMax(PrmCharMinTypMax()) is num
        unit = SingleLanguageUnitNames()
        assert num.setPrmUnit(unit) is num
        assert num.getPrmUnit() is unit

    def test_textual_contents(self):
        txt = PrmCharTextualContents()
        assert isinstance(txt, PrmCharContents)
        assert txt.text is None
        assert txt.setText(String().setValue("v")) is txt
        assert txt.getText().getValue() == "v"
        assert txt.setText(None) is txt
        assert txt.getText().getValue() == "v"

    def test_family_docstrings_verbatim(self):
        assert cleandoc(PrmCharContents.__doc__) == "This is the contents of the parameter."
        assert cleandoc(PrmCharNumericalValue.__doc__) == "This metaclass represents a numercial parameter characteristics."
        assert cleandoc(PrmCharAbsTol.__doc__) == "The parameter is specified as ablolute value with a tolerance."
        assert cleandoc(PrmCharMinTypMax.__doc__) == ("This metaclass represents the characteristics of a parameter as minimal, typical maximum value.")
        assert cleandoc(PrmCharNumericalContents.__doc__) == "This metaclass represents the fact that it is a numerical parameter."
        assert cleandoc(PrmCharTextualContents.__doc__) == "This metaclass represents the fact that it is a textual parameter."

    def test_string_type_for_text(self):
        source = inspect.getsource(PrmCharTextualContents)
        assert "Optional[String]" in source


class TestChapterContentPrms:
    def test_set_get_prms(self):
        chapter_content = ChapterContent()
        assert chapter_content.prms is None
        prms = Prms()
        assert chapter_content.setPrms(prms) is chapter_content
        assert chapter_content.getPrms() is prms
        assert chapter_content.setPrms(None) is chapter_content
        assert chapter_content.getPrms() is prms

    def test_field_precedes_topic_content(self):
        """Table 9.60 displayed order: prms is the first attribute row, topicContent the second."""
        source = inspect.getsource(ChapterContent.__init__)
        assert source.index("self.prms") < source.index("self.topicContent")
