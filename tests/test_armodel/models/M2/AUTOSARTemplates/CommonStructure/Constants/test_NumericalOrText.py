import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NumericalOrText
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, String

CLASS_NOTE = (
    "This meta-class represents the ability to yield either a numerical or a string. A typical use case is that "
    "two or more instances of this meta-class are aggregated with a VariationPoint where some instances yield "
    "strings while other instances yield numerical depending on the resolution of the binding expression."
)

VF_NOTE = (
    "This attribute represents the ability to provide a numerical value. The latest binding time of the "
    "VariationPoint shall be preCompileTime. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime "
    "xml.sequenceOffset=10"
)

VT_NOTE = "This attribute represents the ability to provide a textual value. Tags: xml.sequenceOffset=20"


class TestNumericalOrText:
    def test_inheritance(self):
        not_text = NumericalOrText()
        assert isinstance(not_text, ARObject)
        assert isinstance(not_text, VariationPointCapable)

    def test_initialization(self):
        not_text = NumericalOrText()
        assert not_text.getVf() is None
        assert not_text.getVt() is None

    def test_class_docstring_verbatim(self):
        docstring = (NumericalOrText.__doc__ or "").strip()
        assert docstring.startswith(CLASS_NOTE)
        assert "[constr_1243]" in docstring
        assert "Within the context of one NumericalOrText, either the attribute vf or the attribute vt shall be defined." in docstring

    def test_get_set_vf(self):
        not_text = NumericalOrText()
        vf = Numerical().setValue("42")

        assert not_text.setVf(vf) is not_text
        assert not_text.getVf() is vf

        not_text.setVf(None)
        assert not_text.getVf() is vf

    def test_get_set_vt(self):
        not_text = NumericalOrText()
        vt = String().setValue("text")

        assert not_text.setVt(vt) is not_text
        assert not_text.getVt() is vt
        assert isinstance(not_text.getVt(), String)

        not_text.setVt(None)
        assert not_text.getVt() is vt

    def test_accessor_type_annotations(self):
        hints = typing.get_type_hints(NumericalOrText.setVf)
        assert hints["value"] is typing.Optional[Numerical]
        assert typing.get_type_hints(NumericalOrText.getVf)["return"] is typing.Optional[Numerical]

        vt_hints = typing.get_type_hints(NumericalOrText.setVt)
        assert vt_hints["value"] is typing.Optional[String]
        assert typing.get_type_hints(NumericalOrText.getVt)["return"] is typing.Optional[String]

    def test_member_docstrings_verbatim(self):
        not_text = NumericalOrText()
        assert (not_text.getVf.__doc__ or "").strip() == VF_NOTE
        assert (not_text.setVf.__doc__ or "").strip().split("\n")[0] == VF_NOTE
        assert (not_text.getVt.__doc__ or "").strip() == VT_NOTE
        assert (not_text.setVt.__doc__ or "").strip().split("\n")[0] == VT_NOTE


from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable  # noqa: E402
