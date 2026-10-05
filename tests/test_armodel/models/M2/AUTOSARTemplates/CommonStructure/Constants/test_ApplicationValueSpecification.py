import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ApplicationValueSpecification,
    CompositeRuleBasedValueArgument,
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier

CLASS_NOTE = (
    "This meta-class represents values for DataPrototypes typed by ApplicationDataTypes "
    "(this includes in particular compound primitives). For further details refer to ASAM CDF 2.0. "
    "This meta-class corresponds to some extent with SW-INSTANCE in ASAM CDF 2.0."
)

CATEGORY_NOTE = (
    "Specifies to which category of ApplicationDataType this ApplicationValueSpecification can be "
    "applied (e.g. as an initial value), thus imposing constraints on the structure and semantics of "
    "the contained values, see [constr_1006] and [constr_2051]."
)

SW_AXIS_CONT_NOTE = (
    "This represents the axis values of a Compound Primitive Data Type (curve or map). The first "
    "swAxisCont describes the x-axis, the second sw AxisCont describes the y-axis, the third "
    "swAxisCont describes the z-axis. In addition to this, the axis can be denoted in swAxisIndex."
)

SW_VALUE_CONT_NOTE = "This represents the values of a Compound Primitive Data Type."


class TestApplicationValueSpecification:
    def test_inheritance(self):
        spec = ApplicationValueSpecification()
        assert isinstance(spec, CompositeRuleBasedValueArgument)
        assert isinstance(spec, ValueSpecification)
        assert isinstance(spec, ARObject)

    def test_initialization(self):
        spec = ApplicationValueSpecification()
        assert spec.getCategory() is None
        assert spec.getSwAxisConts() == []
        assert spec.getSwValueCont() is None
        assert not hasattr(spec, "getSwAxisCont")
        assert not hasattr(spec, "setSwAxisCont")

    def test_class_docstring_verbatim(self):
        docstring = ApplicationValueSpecification.__doc__ or ""
        assert docstring.strip().startswith(CLASS_NOTE)
        assert "[constr_10503]" in docstring
        assert "[constr_10507]" in docstring
        assert "[constr_2052]" in docstring

    def test_get_set_category(self):
        spec = ApplicationValueSpecification()
        category = Identifier().setValue("VALUE")

        assert spec.setCategory(category) is spec
        assert spec.getCategory() is category

        spec.setCategory(None)
        assert spec.getCategory() is category

    def test_add_get_sw_axis_conts(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import SwAxisCont

        spec = ApplicationValueSpecification()
        first = SwAxisCont()
        second = SwAxisCont()

        assert spec.addSwAxisCont(first) is spec
        assert spec.addSwAxisCont(second) is spec
        assert spec.getSwAxisConts() == [first, second]

        spec.addSwAxisCont(None)
        assert spec.getSwAxisConts() == [first, second]

    def test_get_set_sw_value_cont(self):
        from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwValueCont

        spec = ApplicationValueSpecification()
        cont = SwValueCont()

        assert spec.setSwValueCont(cont) is spec
        assert spec.getSwValueCont() is cont

        spec.setSwValueCont(None)
        assert spec.getSwValueCont() is cont

    def test_accessor_type_annotations(self):
        hints = typing.get_type_hints(ApplicationValueSpecification.setCategory)
        assert hints["value"] is OptionalIdentifier
        assert typing.get_type_hints(ApplicationValueSpecification.getCategory)["return"] is OptionalIdentifier

        add_hints = typing.get_type_hints(ApplicationValueSpecification.addSwAxisCont)
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import SwAxisCont

        assert add_hints["value"] is OptionalSwAxisCont
        assert typing.get_type_hints(ApplicationValueSpecification.getSwAxisConts)["return"] == typing.List[SwAxisCont]

        set_hints = typing.get_type_hints(ApplicationValueSpecification.setSwValueCont)

        assert set_hints["value"] is OptionalSwValueCont

    def test_member_docstrings_verbatim(self):
        spec = ApplicationValueSpecification()
        assert (spec.getCategory.__doc__ or "").strip() == CATEGORY_NOTE
        assert (spec.setCategory.__doc__ or "").strip().split("\n")[0] == CATEGORY_NOTE
        assert (spec.getSwAxisConts.__doc__ or "").strip() == SW_AXIS_CONT_NOTE
        assert (spec.addSwAxisCont.__doc__ or "").strip().split("\n")[0] == SW_AXIS_CONT_NOTE
        assert (spec.getSwValueCont.__doc__ or "").strip() == SW_VALUE_CONT_NOTE
        assert (spec.setSwValueCont.__doc__ or "").strip().split("\n")[0] == SW_VALUE_CONT_NOTE


OptionalIdentifier = typing.Optional[Identifier]
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import SwAxisCont  # noqa: E402
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwValueCont  # noqa: E402

OptionalSwAxisCont = typing.Optional[SwAxisCont]
OptionalSwValueCont = typing.Optional[SwValueCont]
