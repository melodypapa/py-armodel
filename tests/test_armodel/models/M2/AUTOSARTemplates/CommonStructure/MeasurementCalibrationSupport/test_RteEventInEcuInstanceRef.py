import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import RteEventInEcuInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


def make_ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestRteEventInEcuInstanceRefSpec:
    """Spec contract of RteEventInEcuInstanceRef (XSD-only, AUTOSAR_00052.xsd L100605)."""

    def test_docstring_documents_xsd_derivation(self):
        """The class docstring documents the XSD-only derivation (no spec Note exists)."""
        assert "ECU extract" in inspect.cleandoc(RteEventInEcuInstanceRef.__doc__)
        assert "XSD-only" in inspect.cleandoc(RteEventInEcuInstanceRef.__doc__)

    def test_heritage(self):
        """Base chain ARObject + AtpInstanceRef (XSD complexType group refs)."""
        iref = RteEventInEcuInstanceRef()
        assert isinstance(iref, AtpInstanceRef)

    def test_initialization(self):
        """All 3 own attributes optional (XSD minOccurs=0); base atpDerived fields inherited."""
        iref = RteEventInEcuInstanceRef()
        assert iref.contextRootCompositionRef is None
        assert iref.contextAtomicComponentRef is None
        assert iref.targetRteEventRef is None
        # the <<atpDerived>>base association is NOT re-declared on the subclass
        # (it duplicates the inherited AtpInstanceRef.atpBaseRef)
        assert not hasattr(iref, "baseRef")
        assert iref.atpBaseRef is None

    def test_get_set_context_root_composition_ref(self):
        iref = RteEventInEcuInstanceRef()
        ref = make_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE")
        assert iref.setContextRootCompositionRef(ref) is iref
        assert iref.getContextRootCompositionRef() is ref
        iref.setContextRootCompositionRef(None)
        assert iref.getContextRootCompositionRef() is ref

    def test_get_set_context_atomic_component_ref(self):
        iref = RteEventInEcuInstanceRef()
        ref = make_ref("/Comp", "SW-COMPONENT-PROTOTYPE")
        assert iref.setContextAtomicComponentRef(ref) is iref
        assert iref.getContextAtomicComponentRef() is ref
        iref.setContextAtomicComponentRef(None)
        assert iref.getContextAtomicComponentRef() is ref

    def test_get_set_target_rte_event_ref(self):
        iref = RteEventInEcuInstanceRef()
        ref = make_ref("/Evt", "RTE-EVENT")
        assert iref.setTargetRteEventRef(ref) is iref
        assert iref.getTargetRteEventRef() is ref
        iref.setTargetRteEventRef(None)
        assert iref.getTargetRteEventRef() is ref

    def test_get_type_hints(self):
        """Spec-typed annotations resolve at runtime (plain get_type_hints)."""
        for accessor in ("setContextRootCompositionRef", "setContextAtomicComponentRef", "setTargetRteEventRef"):
            hints = typing.get_type_hints(getattr(RteEventInEcuInstanceRef, accessor))
            assert hints.get("value") == typing.Optional[RefType], accessor
            assert hints.get("return") is RteEventInEcuInstanceRef, accessor
        for accessor in ("getContextRootCompositionRef", "getContextAtomicComponentRef", "getTargetRteEventRef"):
            assert typing.get_type_hints(getattr(RteEventInEcuInstanceRef, accessor)).get("return") == typing.Optional[RefType], accessor
