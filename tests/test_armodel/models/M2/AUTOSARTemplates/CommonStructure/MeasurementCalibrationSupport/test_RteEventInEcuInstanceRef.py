from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import RteEventInEcuInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


def make_ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    return ref


class TestRteEventInEcuInstanceRefInitialization:
    def test_initialization(self):
        """Test RteEventInEcuInstanceRef __init__ defaults"""
        iref = RteEventInEcuInstanceRef()
        assert iref is not None
        assert iref.baseRef is None
        assert iref.contextRootCompositionRef is None
        assert iref.contextAtomicComponentRef is None
        assert iref.targetRteEventRef is None


class TestRteEventInEcuInstanceRefBase:
    def test_get_set_base_ref(self):
        """Test setBaseRef returns self and getBaseRef round-trips"""
        iref = RteEventInEcuInstanceRef()
        ref = make_ref("/Root")
        result = iref.setBaseRef(ref)
        assert result is iref
        assert iref.getBaseRef() is ref

    def test_set_base_ref_none_is_noop(self):
        """Test setting a None base ref is a no-op"""
        iref = RteEventInEcuInstanceRef()
        ref = make_ref("/Root")
        iref.setBaseRef(ref)
        iref.setBaseRef(None)
        assert iref.getBaseRef() is ref


class TestRteEventInEcuInstanceRefContextRootComposition:
    def test_get_set_context_root_composition_ref(self):
        """Test setContextRootCompositionRef returns self and getContextRootCompositionRef round-trips"""
        iref = RteEventInEcuInstanceRef()
        ref = make_ref("/Root")
        result = iref.setContextRootCompositionRef(ref)
        assert result is iref
        assert iref.getContextRootCompositionRef() is ref

    def test_set_context_root_composition_ref_none_is_noop(self):
        """Test setting a None context root composition ref is a no-op"""
        iref = RteEventInEcuInstanceRef()
        ref = make_ref("/Root")
        iref.setContextRootCompositionRef(ref)
        iref.setContextRootCompositionRef(None)
        assert iref.getContextRootCompositionRef() is ref


class TestRteEventInEcuInstanceRefContextAtomicComponent:
    def test_get_set_context_atomic_component_ref(self):
        """Test setContextAtomicComponentRef returns self and getContextAtomicComponentRef round-trips"""
        iref = RteEventInEcuInstanceRef()
        ref = make_ref("/Root/Comp")
        result = iref.setContextAtomicComponentRef(ref)
        assert result is iref
        assert iref.getContextAtomicComponentRef() is ref

    def test_set_context_atomic_component_ref_none_is_noop(self):
        """Test setting a None context atomic component ref is a no-op"""
        iref = RteEventInEcuInstanceRef()
        ref = make_ref("/Root/Comp")
        iref.setContextAtomicComponentRef(ref)
        iref.setContextAtomicComponentRef(None)
        assert iref.getContextAtomicComponentRef() is ref


class TestRteEventInEcuInstanceRefTarget:
    def test_get_set_target_rte_event_ref(self):
        """Test setTargetRteEventRef returns self and getTargetRteEventRef round-trips"""
        iref = RteEventInEcuInstanceRef()
        ref = make_ref("/Root/Comp/Evt")
        result = iref.setTargetRteEventRef(ref)
        assert result is iref
        assert iref.getTargetRteEventRef() is ref

    def test_set_target_rte_event_ref_none_is_noop(self):
        """Test setting a None target RTE event ref is a no-op"""
        iref = RteEventInEcuInstanceRef()
        ref = make_ref("/Root/Comp/Evt")
        iref.setTargetRteEventRef(ref)
        iref.setTargetRteEventRef(None)
        assert iref.getTargetRteEventRef() is ref
