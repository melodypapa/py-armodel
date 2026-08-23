from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    NotAvailableValueSpecification,
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger


class TestNotAvailableValueSpecification:
    def test_inheritance(self):
        """Test that NotAvailableValueSpecification inherits from ValueSpecification"""
        spec = NotAvailableValueSpecification()
        assert isinstance(spec, ValueSpecification)

    def test_initialization(self):
        """Test NotAvailableValueSpecification initialization defaults"""
        spec = NotAvailableValueSpecification()
        assert spec is not None
        assert spec.getDefaultPattern() is None

    def test_get_set_default_pattern(self):
        """Test getDefaultPattern/setDefaultPattern round-trip, chaining and None no-op."""
        spec = NotAvailableValueSpecification()
        pattern = PositiveInteger().setValue("4")

        assert spec.setDefaultPattern(pattern) is spec
        assert spec.getDefaultPattern() is pattern

        spec.setDefaultPattern(None)
        assert spec.getDefaultPattern() is pattern

    def test_no_reason_member(self):
        """Spec Table 5.116 has no 'reason' attribute: the fabricated member must be absent."""
        spec = NotAvailableValueSpecification()
        assert not hasattr(spec, "reason")
        assert not hasattr(spec, "getReason")
        assert not hasattr(spec, "setReason")
