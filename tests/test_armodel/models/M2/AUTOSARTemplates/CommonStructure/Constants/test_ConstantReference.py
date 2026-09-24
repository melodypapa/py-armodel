import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ConstantReference, ValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType


class TestConstantReference:
    def test_inheritance(self):
        """Instead of defining this value inline, a constant is referenced."""
        spec = ConstantReference()
        assert isinstance(spec, ValueSpecification)

    def test_initialization(self):
        """Instead of defining this value inline, a constant is referenced."""
        spec = ConstantReference()
        assert spec is not None
        assert spec.constantRef is None
        assert spec.shortLabel is None

    def test_constant_ref_annotation_is_optional(self):
        """constant is a ConstantSpecification ref (0..1) attribute — the accessor hints must be Optional[RefType]."""
        hints = typing.get_type_hints(ConstantReference.getConstantRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(ConstantReference.setConstantRef)
        assert hints["value"] == typing.Optional[RefType]

    def test_get_constant_ref(self):
        """The referenced constant."""
        spec = ConstantReference()
        assert spec.getConstantRef() is None

    def test_set_constant_ref(self):
        """The referenced constant."""
        spec = ConstantReference()
        ref = RefType()
        ref.setValue("/DemoApplication/ConstantSpecifications/CONST_1")
        result = spec.setConstantRef(ref)
        assert result is spec
        assert spec.getConstantRef() is ref
        assert spec.getConstantRef().getValue() == "/DemoApplication/ConstantSpecifications/CONST_1"

    def test_set_constant_ref_none(self):
        """The referenced constant."""
        spec = ConstantReference()
        ref = RefType()
        ref.setValue("/DemoApplication/ConstantSpecifications/CONST_1")
        spec.setConstantRef(ref)
        result = spec.setConstantRef(None)
        assert result is spec
        assert spec.getConstantRef() is ref

    def test_short_label_round_trip(self):
        """This can be used to identify particular value specifications for human readers, for example elements of a record type."""
        spec = ConstantReference()
        label = Identifier()
        label.setValue("crs")
        result = spec.setShortLabel(label)
        assert result is spec
        assert spec.getShortLabel() is label
        result = spec.setShortLabel(None)
        assert result is spec
        assert spec.getShortLabel() is label
