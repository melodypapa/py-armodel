import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ConstantSpecification, NumericalValueSpecification, ValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical


class TestConstantSpecification:
    def test_inheritance(self):
        """Specification of a constant that can be part of a package, i.e. it can be defined stand-alone."""
        spec = ConstantSpecification(None, "ConstantSpecification")
        assert isinstance(spec, ARElement)

    def test_initialization(self):
        """Specification of a constant that can be part of a package, i.e. it can be defined stand-alone."""
        spec = ConstantSpecification(None, "MyConstant")
        assert spec is not None
        assert spec.getShortName() == "MyConstant"
        assert spec.getValueSpec() is None

    def test_value_spec_annotation_is_optional(self):
        """valueSpec is a ValueSpecification aggr (0..1) — the accessor hints must be Optional[ValueSpecification]."""
        hints = typing.get_type_hints(ConstantSpecification.getValueSpec)
        assert hints["return"] == typing.Optional[ValueSpecification]
        hints = typing.get_type_hints(ConstantSpecification.setValueSpec)
        assert hints["value"] == typing.Optional[ValueSpecification]

    def test_get_value_spec(self):
        """Specification of an expression leading to a value for this constant."""
        spec = ConstantSpecification(None, "MyConstant")
        assert spec.getValueSpec() is None

    def test_set_value_spec(self):
        """Specification of an expression leading to a value for this constant."""
        spec = ConstantSpecification(None, "MyConstant")
        value_spec = NumericalValueSpecification()
        numerical = ARNumerical()
        numerical.setValue("3.14")
        value_spec.setValue(numerical)
        result = spec.setValueSpec(value_spec)
        assert result is spec
        assert spec.getValueSpec() is value_spec
        assert spec.getValueSpec().getValue().getValue() == 3.14

    def test_set_value_spec_none(self):
        """Specification of an expression leading to a value for this constant."""
        spec = ConstantSpecification(None, "MyConstant")
        value_spec = NumericalValueSpecification()
        numerical = ARNumerical()
        numerical.setValue("3.14")
        value_spec.setValue(numerical)
        spec.setValueSpec(value_spec)
        result = spec.setValueSpec(None)
        assert result is spec
        assert spec.getValueSpec() is value_spec
