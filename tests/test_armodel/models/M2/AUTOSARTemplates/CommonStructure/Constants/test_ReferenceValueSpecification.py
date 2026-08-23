from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ReferenceValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestReferenceValueSpecification:
    def test_inheritance(self):
        """Test that ReferenceValueSpecification inherits from ValueSpecification"""
        spec = ReferenceValueSpecification()
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ValueSpecification

        assert isinstance(spec, ValueSpecification)

    def test_initialization(self):
        """Test ReferenceValueSpecification initialization"""
        spec = ReferenceValueSpecification()
        assert spec is not None
        assert spec.referenceValueRef is None

    def test_get_reference_value_ref(self):
        """Test getReferenceValueRef method"""
        spec = ReferenceValueSpecification()
        assert spec.getReferenceValueRef() is None

    def test_set_reference_value_ref(self):
        """Test setReferenceValueRef method"""
        spec = ReferenceValueSpecification()
        ref_value = RefType()
        ref_value.setValue("/DataPrototype/some_pointer")
        result = spec.setReferenceValueRef(ref_value)
        assert result is spec
        assert spec.getReferenceValueRef() is ref_value

    def test_set_reference_value_ref_none(self):
        """Test setReferenceValueRef with None value"""
        spec = ReferenceValueSpecification()
        ref_value = RefType()
        ref_value.setValue("/DataPrototype/some_pointer")
        spec.setReferenceValueRef(ref_value)
        result = spec.setReferenceValueRef(None)
        assert result is spec
        assert spec.getReferenceValueRef() is ref_value
