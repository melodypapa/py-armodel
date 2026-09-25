import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NumericalValueSpecification, ValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, Identifier


class TestNumericalValueSpecification:
    def test_inheritance(self):
        """A numerical ValueSpecification which is intended to be assigned to a Primitive data element. Note that the numerical value is a variant, it can be computed by a formula."""
        spec = NumericalValueSpecification()
        assert isinstance(spec, ValueSpecification)

    def test_initialization(self):
        """A numerical ValueSpecification which is intended to be assigned to a Primitive data element. Note that the numerical value is a variant, it can be computed by a formula."""
        spec = NumericalValueSpecification()
        assert spec is not None
        assert spec.value is None
        assert spec.shortLabel is None

    def test_value_annotation_is_optional(self):
        """value is a Numerical (0..1) attribute — the accessor hints must be Optional[ARNumerical]."""
        hints = typing.get_type_hints(NumericalValueSpecification.getValue)
        assert hints["return"] == typing.Optional[ARNumerical]
        hints = typing.get_type_hints(NumericalValueSpecification.setValue)
        assert hints["value"] == typing.Optional[ARNumerical]

    def test_get_value(self):
        """This is the value itself. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"""
        spec = NumericalValueSpecification()
        assert spec.getValue() is None

    def test_set_value(self):
        """This is the value itself. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"""
        spec = NumericalValueSpecification()
        numerical = ARNumerical()
        numerical.setValue("3.14")
        result = spec.setValue(numerical)
        assert result is spec
        assert spec.getValue() is numerical
        assert spec.getValue().getValue() == 3.14

    def test_set_value_none(self):
        """This is the value itself. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"""
        spec = NumericalValueSpecification()
        numerical = ARNumerical()
        numerical.setValue("3.14")
        spec.setValue(numerical)
        result = spec.setValue(None)
        assert result is spec
        assert spec.getValue() is numerical

    def test_short_label_round_trip(self):
        """This can be used to identify particular value specifications for human readers, for example elements of a record type."""
        spec = NumericalValueSpecification()
        label = Identifier()
        label.setValue("nvs")
        result = spec.setShortLabel(label)
        assert result is spec
        assert spec.getShortLabel() is label
        result = spec.setShortLabel(None)
        assert result is spec
        assert spec.getShortLabel() is label
