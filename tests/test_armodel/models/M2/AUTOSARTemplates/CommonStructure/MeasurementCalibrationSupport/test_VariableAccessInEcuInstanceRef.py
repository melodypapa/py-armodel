from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import VariableAccessInEcuInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


def make_ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    return ref


class TestVariableAccessInEcuInstanceRefInitialization:
    def test_initialization(self):
        """Test VariableAccessInEcuInstanceRef __init__ defaults"""
        iref = VariableAccessInEcuInstanceRef()
        assert iref is not None
        assert iref.baseRef is None
        assert iref.contextRootCompositionRef is None
        assert iref.contextAtomicComponentRef is None
        assert iref.targetVariableAccessRef is None


class TestVariableAccessInEcuInstanceRefBase:
    def test_get_set_base_ref(self):
        """Test setBaseRef returns self and getBaseRef round-trips"""
        iref = VariableAccessInEcuInstanceRef()
        ref = make_ref("/Root")
        result = iref.setBaseRef(ref)
        assert result is iref
        assert iref.getBaseRef() is ref

    def test_set_base_ref_none_is_noop(self):
        """Test setting a None base ref is a no-op"""
        iref = VariableAccessInEcuInstanceRef()
        ref = make_ref("/Root")
        iref.setBaseRef(ref)
        iref.setBaseRef(None)
        assert iref.getBaseRef() is ref


class TestVariableAccessInEcuInstanceRefContextRootComposition:
    def test_get_set_context_root_composition_ref(self):
        """Test setContextRootCompositionRef returns self and getContextRootCompositionRef round-trips"""
        iref = VariableAccessInEcuInstanceRef()
        ref = make_ref("/Root")
        result = iref.setContextRootCompositionRef(ref)
        assert result is iref
        assert iref.getContextRootCompositionRef() is ref

    def test_set_context_root_composition_ref_none_is_noop(self):
        """Test setting a None context root composition ref is a no-op"""
        iref = VariableAccessInEcuInstanceRef()
        ref = make_ref("/Root")
        iref.setContextRootCompositionRef(ref)
        iref.setContextRootCompositionRef(None)
        assert iref.getContextRootCompositionRef() is ref


class TestVariableAccessInEcuInstanceRefContextAtomicComponent:
    def test_get_set_context_atomic_component_ref(self):
        """Test setContextAtomicComponentRef returns self and getContextAtomicComponentRef round-trips"""
        iref = VariableAccessInEcuInstanceRef()
        ref = make_ref("/Root/Comp")
        result = iref.setContextAtomicComponentRef(ref)
        assert result is iref
        assert iref.getContextAtomicComponentRef() is ref

    def test_set_context_atomic_component_ref_none_is_noop(self):
        """Test setting a None context atomic component ref is a no-op"""
        iref = VariableAccessInEcuInstanceRef()
        ref = make_ref("/Root/Comp")
        iref.setContextAtomicComponentRef(ref)
        iref.setContextAtomicComponentRef(None)
        assert iref.getContextAtomicComponentRef() is ref


class TestVariableAccessInEcuInstanceRefTarget:
    def test_get_set_target_variable_access_ref(self):
        """Test setTargetVariableAccessRef returns self and getTargetVariableAccessRef round-trips"""
        iref = VariableAccessInEcuInstanceRef()
        ref = make_ref("/Root/Comp/Var")
        result = iref.setTargetVariableAccessRef(ref)
        assert result is iref
        assert iref.getTargetVariableAccessRef() is ref

    def test_set_target_variable_access_ref_none_is_noop(self):
        """Test setting a None target VariableAccess ref is a no-op"""
        iref = VariableAccessInEcuInstanceRef()
        ref = make_ref("/Root/Comp/Var")
        iref.setTargetVariableAccessRef(ref)
        iref.setTargetVariableAccessRef(None)
        assert iref.getTargetVariableAccessRef() is ref
