from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ConstantSpecificationMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestConstantSpecificationMapping:
    def test_inheritance(self):
        """Test that ConstantSpecificationMapping inherits from ARObject"""
        mapping = ConstantSpecificationMapping()
        assert isinstance(mapping, ARObject)

    def test_initialization(self):
        """Test ConstantSpecificationMapping initialization defaults"""
        mapping = ConstantSpecificationMapping()
        assert mapping is not None
        assert mapping.getApplConstantRef() is None
        assert mapping.getImplConstantRef() is None

    def test_get_set_appl_constant_ref(self):
        """Test getApplConstantRef/setApplConstantRef round-trip, chaining and None no-op."""
        mapping = ConstantSpecificationMapping()
        ref = RefType().setValue("/ConstantSpecification/ApplConst")

        assert mapping.setApplConstantRef(ref) is mapping
        assert mapping.getApplConstantRef() is ref

        mapping.setApplConstantRef(None)
        assert mapping.getApplConstantRef() is ref

    def test_get_set_impl_constant_ref(self):
        """Test getImplConstantRef/setImplConstantRef round-trip, chaining and None no-op."""
        mapping = ConstantSpecificationMapping()
        ref = RefType().setValue("/ConstantSpecification/ImplConst")

        assert mapping.setImplConstantRef(ref) is mapping
        assert mapping.getImplConstantRef() is ref

        mapping.setImplConstantRef(None)
        assert mapping.getImplConstantRef() is ref

    def test_no_legacy_members(self):
        """Spec Table 5.118 has no sourceRef/targetRef attributes: the fabricated members must be absent."""
        mapping = ConstantSpecificationMapping()
        assert not hasattr(mapping, "sourceRef")
        assert not hasattr(mapping, "getSourceRef")
        assert not hasattr(mapping, "setSourceRef")
        assert not hasattr(mapping, "targetRef")
        assert not hasattr(mapping, "getTargetRef")
        assert not hasattr(mapping, "setTargetRef")
