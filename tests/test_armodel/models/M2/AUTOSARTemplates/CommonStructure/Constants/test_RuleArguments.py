import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    NumericalOrText,
    RuleArguments,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    VerbatimString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import (
    VariationPointCapable,
)

CLASS_NOTE = "This represents the arguments for a rule-based value specification."

V_NOTE = "This represents a numerical value for the RuleBased ValueSpecification."
VF_NOTE = (
    "This represents a numerical value for the RuleBased ValueSpecification which may subject to variability. "
    "The latest binding time of the VariationPoint shall be pre CompileTime. "
    "Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"
)
VT_NOTE = "This represents a textual value for the RuleBasedValue Specification."
VTF_NOTE = (
    "This aggregation represents the ability to provide a value that is either numerical or text which "
    "existence is subject to variability. "
    "Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=vtf, vtf.variationPoint.shortLabel vh.latestBindingTime=preCompileTime"
)


class TestRuleArguments:
    def test_inheritance(self):
        arguments = RuleArguments()
        assert isinstance(arguments, ARObject)
        assert isinstance(arguments, VariationPointCapable)

    def test_initialization(self):
        arguments = RuleArguments()
        assert arguments.getV() is None
        assert arguments.getVf() is None
        assert arguments.getVt() is None
        assert arguments.getVtf() is None

    def test_class_docstring_verbatim(self):
        assert (RuleArguments.__doc__ or "").strip() == CLASS_NOTE

    def test_get_set_v(self):
        arguments = RuleArguments()
        v = Numerical().setValue("1.5")

        assert arguments.setV(v) is arguments
        assert arguments.getV() is v

        arguments.setV(None)
        assert arguments.getV() is v

    def test_get_set_vf(self):
        arguments = RuleArguments()
        vf = Numerical().setValue("2.5")

        assert arguments.setVf(vf) is arguments
        assert arguments.getVf() is vf

        arguments.setVf(None)
        assert arguments.getVf() is vf

    def test_get_set_vt(self):
        arguments = RuleArguments()
        vt = VerbatimString().setValue("TEXT")

        assert arguments.setVt(vt) is arguments
        assert arguments.getVt() is vt

        arguments.setVt(None)
        assert arguments.getVt() is vt

    def test_get_set_vtf(self):
        arguments = RuleArguments()
        vtf = NumericalOrText()

        assert arguments.setVtf(vtf) is arguments
        assert arguments.getVtf() is vtf

        arguments.setVtf(None)
        assert arguments.getVtf() is vtf

    def test_accessor_type_annotations(self):
        assert typing.get_type_hints(RuleArguments.setV)["value"] == typing.Optional[Numerical]
        assert typing.get_type_hints(RuleArguments.getV)["return"] == typing.Optional[Numerical]

        assert typing.get_type_hints(RuleArguments.setVf)["value"] == typing.Optional[Numerical]
        assert typing.get_type_hints(RuleArguments.getVf)["return"] == typing.Optional[Numerical]

        assert typing.get_type_hints(RuleArguments.setVt)["value"] == typing.Optional[VerbatimString]
        assert typing.get_type_hints(RuleArguments.getVt)["return"] == typing.Optional[VerbatimString]

        assert typing.get_type_hints(RuleArguments.setVtf)["value"] == typing.Optional[NumericalOrText]
        assert typing.get_type_hints(RuleArguments.getVtf)["return"] == typing.Optional[NumericalOrText]

    def test_member_docstrings_verbatim(self):
        arguments = RuleArguments()
        assert (arguments.getV.__doc__ or "").strip() == V_NOTE
        assert (arguments.setV.__doc__ or "").strip().split("\n")[0] == V_NOTE
        assert (arguments.getVf.__doc__ or "").strip() == VF_NOTE
        assert (arguments.setVf.__doc__ or "").strip().split("\n")[0] == VF_NOTE
        assert (arguments.getVt.__doc__ or "").strip() == VT_NOTE
        assert (arguments.setVt.__doc__ or "").strip().split("\n")[0] == VT_NOTE
        assert (arguments.getVtf.__doc__ or "").strip() == VTF_NOTE
        assert (arguments.setVtf.__doc__ or "").strip().split("\n")[0] == VTF_NOTE
