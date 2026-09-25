import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import VariableAccessInEcuInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


def make_ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestVariableAccessInEcuInstanceRefSpec:
    """Spec contract of VariableAccessInEcuInstanceRef (XSD-only, AUTOSAR_00052.xsd L129566)."""

    def test_docstring_documents_xsd_derivation(self):
        """The class docstring documents the XSD-only derivation (no spec Note exists)."""
        assert "ECU extract" in inspect.cleandoc(VariableAccessInEcuInstanceRef.__doc__)
        assert "XSD-only" in inspect.cleandoc(VariableAccessInEcuInstanceRef.__doc__)

    def test_heritage(self):
        """Base chain ARObject + AtpInstanceRef (XSD complexType group refs)."""
        iref = VariableAccessInEcuInstanceRef()
        assert isinstance(iref, AtpInstanceRef)

    def test_initialization(self):
        """All 3 own attributes optional (XSD minOccurs=0); base atpDerived fields inherited."""
        iref = VariableAccessInEcuInstanceRef()
        assert iref.contextRootCompositionRef is None
        assert iref.contextAtomicComponentRef is None
        assert iref.targetVariableAccessRef is None
        # the <<atpDerived>>base association is NOT re-declared on the subclass
        # (it duplicates the inherited AtpInstanceRef.atpBaseRef)
        assert not hasattr(iref, "baseRef")
        assert iref.atpBaseRef is None

    def test_get_set_context_root_composition_ref(self):
        iref = VariableAccessInEcuInstanceRef()
        ref = make_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE")
        assert iref.setContextRootCompositionRef(ref) is iref
        assert iref.getContextRootCompositionRef() is ref
        iref.setContextRootCompositionRef(None)
        assert iref.getContextRootCompositionRef() is ref

    def test_get_set_context_atomic_component_ref(self):
        iref = VariableAccessInEcuInstanceRef()
        ref = make_ref("/Comp", "SW-COMPONENT-PROTOTYPE")
        assert iref.setContextAtomicComponentRef(ref) is iref
        assert iref.getContextAtomicComponentRef() is ref
        iref.setContextAtomicComponentRef(None)
        assert iref.getContextAtomicComponentRef() is ref

    def test_get_set_target_variable_access_ref(self):
        iref = VariableAccessInEcuInstanceRef()
        ref = make_ref("/va", "VARIABLE-ACCESS")
        assert iref.setTargetVariableAccessRef(ref) is iref
        assert iref.getTargetVariableAccessRef() is ref
        iref.setTargetVariableAccessRef(None)
        assert iref.getTargetVariableAccessRef() is ref

    def test_get_type_hints(self):
        """Spec-typed annotations resolve at runtime (plain get_type_hints)."""
        for accessor in ("setContextRootCompositionRef", "setContextAtomicComponentRef", "setTargetVariableAccessRef"):
            hints = typing.get_type_hints(getattr(VariableAccessInEcuInstanceRef, accessor))
            assert hints.get("value") == typing.Optional[RefType], accessor
            assert hints.get("return") is VariableAccessInEcuInstanceRef, accessor
        for accessor in ("getContextRootCompositionRef", "getContextAtomicComponentRef", "getTargetVariableAccessRef"):
            assert typing.get_type_hints(getattr(VariableAccessInEcuInstanceRef, accessor)).get("return") == typing.Optional[RefType], accessor
